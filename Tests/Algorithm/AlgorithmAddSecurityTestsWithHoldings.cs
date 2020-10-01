/*
 * QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
 * Lean Algorithmic Trading Engine v2.0. Copyright 2014 QuantConnect Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
*/

using NUnit.Framework;
using QuantConnect.Data.Market;
using System;

namespace QuantConnect.Tests.Algorithm
{
    [TestFixture]
    public partial class AlgorithmAddSecurityTests
    {
        [Test]
        public void AddInteractiveBrokersHoldingsTests()
        {
            var lines = @"
AAXN,40,87.4023,87.04
ABBV,175,83.43714285,88.21
AGG,150,112.798,118.15
ARKG,170,24.84818175,61.67
ARKK,100,35.5526,90.19
ARKW,50,102.44,105.92
ATVI,240,82.19441665,81.69
BAH,200,86.47,85.08
BLDR,-480,30.944197,30.41
BPOP,-300,37.59405,36.28
CAL,800,10.3849,10.38
CIM,-1200,8.967006,8.63
CONE,150,67.495,71.31
COR,50,110.400634,117.335
CRWD,25,138.73,142.62
CSD,150,31.90666665,42.82
DCOM,100,12.9173,10.89
DK,-250,15.5945364,11.255
DLR,175,130.3537,141.31
EIDO,200,13.695,17.19
EPI,300,17.395,23.02
ET,-1200,5.84392675,5.8239999
EWG,75,23.91333335,28.78
EWH,250,19.88488,21.835
EWT,80,44.22885,44.145
FAF,-200,51.44874375,51.2
FFTY,300,32.29288,36.4791
FSLY,50,93.7982,93.47
GLD,100,161.366667,175.1
GMED,150,54.7135,50.11
GNW,-1000,3.2748085,3.035
GOGO,-650,10.01535955,9.28
GOOS,390,28.635,30.515
GPRE,300,14.845,14.45
INVH,-200,27.9257635,27.055
IRM,550,30.2925309,26.695
ISEE,100,5.53,5.26
JETS,-300,17.2444998,17.055
LTRN,1000,17.355,17.81
M,-400,6.29599175,6.31
MCHI,-240,73.93328665,72.91
MDY,25,353.18,332.93
MJ,1000,14.270381,10.575
MPW,500,14.168496,16.44
MSM,-190,64.26846055,61.82
NBR,-150,38.49403,24.42
NET,240,37.68446,40.41
NTES,-35,473.44541715,474.9
NUVA,-200,50.54376385,50.05
NWL,500,17.243,17.18
O,150,55.04478935,60.17
OCFT,-800,20.59467575,20.495
ORLY,-46,467.8695413,453.2
OSTK,60,78.90666665,75.15
OTRK,-145,62.991822,62.78
PH,-40,201.9704168,200.02
QTS,300,48.715,62.34
RQI,500,9.57446,10.935
SE,120,151.92166665,152.205
SEAS,-600,20.0944368,19.95
SFM,-750,20.62642505,20.86
SOGO,100,8.315425,8.625
SPG,-250,64.29545995,64.44
SPHD,600,39.61708335,32.68
SRC,150,30.20666665,34.045
SSL,-950,8.45497945,7.67
SUI,-50,142.6067289,141.16
TLT,250,165.40136,163.81
TRMB,-400,49.24379255,48.35
TRN,-750,19.57444825,19.78
TT,120,119.54733335,120.50253295
USMV,80,59.5225,62.85
VNM,500,12.594,14.68
VNQ,75,83.665,77.68
VSH,-950,16.09452515,15.255
W,20,295.28,288.02
WEC,-200,95.3402735,94.17
WFC,-120,23.59935915,23.37
WMGI,800,30.345625,30.52
WPC,80,58.86,64.38
XBI,175,78.0374857,111.4
XOP,-150,44.3922331,44.165
XRX,-600,18.3286424,18.22
YY,-100,79.58812185,78.85
IWM,0,147.43,147.43
QQQ,0,268.58,268.58
SPY,0,327.87,327.87
IWM 201218P00110000,-1,2.503287,1.14
IWM 201218P00120000,-2,2.3725895,2.15
IWM 201218P00143000,10,9.062758,7.53
QQQ 210319P00255000,32,15.5263255,17.25
QQQ 210331P00205000,-2,7.7924695,6.3
QQQ 210331P00230000,-16,12.756273375,11.34
QQQ 210618P00280000,2,25.303138,32.25
SPY 210319P00285000,-14,11.567397857,11.98
SPY 210319P00320000,30,17.882578,21.59
SPY 210618P00345000,2,27.153138,37.35".Split('\n');

            _algo.SetCash(714273.06);

            foreach (var line in lines)
            {
                var csv = line.Split(',');
                if (csv.Length < 4) continue;

                var symbolStr = csv[0].Split(' ');
                var symbol = Symbol.Create(symbolStr[0], SecurityType.Equity, Market.USA);
                if (symbolStr.Length == 2)
                {
                    var strike = symbolStr[1].Substring(7).ToDecimal() / 1000;
                    var expiry = Parse.DateTimeExact(symbolStr[1].Substring(0, 6), DateFormat.SixCharacter);
                    symbol = Symbol.CreateOption(symbol, Market.USA, OptionStyle.American, OptionRight.Put, strike, expiry);
                }

                var last = csv[3].ToDecimal();

                var security = _algo.AddSecurity(symbol);
                security.Holdings.SetHoldings(csv[2].ToDecimal(), csv[1].ToDecimal());
                security.SetMarketPrice(new Tick(DateTime.Now, symbol, last, last, last));
            }

            var tmu = _algo.Portfolio.TotalMarginUsed;
        }
    }
}