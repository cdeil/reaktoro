# The list of chemical elements and their atomic weight
# taken from http://en.wikipedia.org/wiki/List_of_elements.
elements = {
    'H'   : 1.00794,
    'He'  : 4.002602,
    'Li'  : 6.941,
    'Be'  : 9.012182,
    'B'   : 10.811,
    'C'   : 12.0107,
    'N'   : 14.0067,
    'O'   : 15.9994,
    'F'   : 18.9984032,
    'Ne'  : 20.1797,
    'Na'  : 22.989770,
    'Mg'  : 24.3050,
    'Al'  : 26.981538,
    'Si'  : 28.0855,
    'P'   : 30.973761,
    'S'   : 32.065,
    'Cl'  : 35.453,
    'Ar'  : 39.948,
    'K'   : 39.0983,
    'Ca'  : 40.078,
    'Sc'  : 44.955910,
    'Ti'  : 47.867,
    'V'   : 50.9415,
    'Cr'  : 51.9961,
    'Mn'  : 54.938049,
    'Fe'  : 55.845,
    'Co'  : 58.933200,
    'Ni'  : 58.6934,
    'Cu'  : 63.546,
    'Zn'  : 65.409,
    'Ga'  : 69.723,
    'Ge'  : 72.64,
    'As'  : 74.92160,
    'Se'  : 78.96,
    'Br'  : 79.904,
    'Kr'  : 83.798,
    'Rb'  : 85.4678,
    'Sr'  : 87.62,
    'Y'   : 88.90585,
    'Zr'  : 91.224,
    'Nb'  : 92.90638,
    'Mo'  : 95.94,
    'Tc'  : 98.0,
    'Ru'  : 101.07,
    'Rh'  : 102.90550,
    'Pd'  : 106.42,
    'Ag'  : 107.8682,
    'Cd'  : 112.411,
    'In'  : 114.818,
    'Sn'  : 118.710,
    'Sb'  : 121.760,
    'Te'  : 127.60,
    'I'   : 126.90447,
    'Xe'  : 131.293,
    'Cs'  : 132.90545,
    'Ba'  : 137.327,
    'La'  : 138.9055,
    'Ce'  : 140.116,
    'Pr'  : 140.90765,
    'Nd'  : 144.24,
    'Pm'  : 145.0,
    'Sm'  : 150.36,
    'Eu'  : 151.964,
    'Gd'  : 157.25,
    'Tb'  : 158.92534,
    'Dy'  : 162.500,
    'Ho'  : 164.93032,
    'Er'  : 167.259,
    'Tm'  : 168.93421,
    'Yb'  : 173.04,
    'Lu'  : 174.967,
    'Hf'  : 178.49,
    'Ta'  : 180.9479,
    'W'   : 183.84,
    'Re'  : 186.207,
    'Os'  : 190.23,
    'Ir'  : 192.217,
    'Pt'  : 195.078,
    'Au'  : 196.96655,
    'Hg'  : 200.59,
    'Tl'  : 204.3833,
    'Pb'  : 207.2,
    'Bi'  : 208.98038,
    'Po'  : 209.0,
    'At'  : 210.0,
    'Rn'  : 222.0,
    'Fr'  : 223.0,
    'Ra'  : 226.0,
    'Ac'  : 227.0,
    'Th'  : 232.0381,
    'Pa'  : 231.03588,
    'U'   : 238.02891,
    'Np'  : 237.0,
    'Pu'  : 244.0,
    'Am'  : 243.0,
    'Cm'  : 247.0,
    'Bk'  : 247.0,
    'Cf'  : 251.0,
    'Es'  : 252.0,
    'Fm'  : 257.0,
    'Md'  : 258.0,
    'No'  : 259.0,
    'Lr'  : 262.0,
    'Rf'  : 261.0,
    'Db'  : 262.0,
    'Sg'  : 266.0,
    'Hs'  : 264.0,
    'Bh'  : 277.0,
    'Mt'  : 268.0,
    'Uun' : 281.0,
    'Uuu' : 272.0,
    'Uub' : 285.0,
    'Uut' : 284.0,
    'Uuq' : 289.0,
    'Uup' : 288.0,
    'Uuh' : 292.0
}

# The list of aqueous complexes and their dissociation formula into ions
aqueous_complexes = {
    'AgCl(aq)'        : '1:Ag+ 1:Cl-',
    'AgF(aq)'         : '1:Ag+ 1:F-',
    'AgNO3(aq)'       : '1:Ag+ 1:NO3-',
    'AlF3(aq)'        : '1:Al+++ 3:F-',
    'As(OH)3(aq)'     : '1:H+ 1:H2AsO3-',
    'CaCl2(aq)'       : '1:Ca++ 2:Cl-',
    'CaHPO4(aq)'      : '1:Ca++ 1:HPO4--',
    'CaSO4(aq)'       : '1:Ca++ 1:SO4--',
    'Cd(CN)2(aq)'     : '1:Cd++ 2:CN-',
    'Cd(N3)2(aq)'     : '1:Cd++ 2:N3-',
    'Cd(SCN)2(aq)'    : '1:Cd++ 2:SCN-',
    'CdBr2(aq)'       : '1:Cd++ 2:Br-',
    'CdCl2(aq)'       : '1:Cd++ 2:Cl-',
    'CdI2(aq)'        : '1:Cd++ 2:I-',
    'CdSO4(aq)'       : '1:Cd++ 1:SO4--',
    'CdSeO4(aq)'      : '1:Cd++ 1:SeO4--',
    'CeCl3(aq)'       : '1:Ce+++ 3:Cl-',
    'CeF3(aq)'        : '1:Ce+++ 3:F-',
    'Co(HS)2(aq)'     : '1:Co++ 2:HS-',
    'CoBr2(aq)'       : '1:Co++ 2:Br-',
    'CoI2(aq)'        : '1:Co++ 2:I-',
    'CoSO4(aq)'       : '1:Co++ 1:SO4--',
    'CoSeO4(aq)'      : '1:Co++ 1:SeO4--',
    'CsBr(aq)'        : '1:Br- 1:Cs+',
    'CsCl(aq)'        : '1:Cl- 1:Cs+',
    'CsI(aq)'         : '1:Cs+ 1:I-',
    'Cu(NO2)2(aq)'    : '1:Cu++ 2:NO2-',
    'CuCl2(aq)'       : '1:Cu++ 2:Cl-',
    'CuHPO4(aq)'      : '1:Cu++ 1:HPO4--',
    'CuSO4(aq)'       : '1:Cu++ 1:SO4--',
    'DyCl3(aq)'       : '1:Dy+++ 3:Cl-',
    'DyF3(aq)'        : '1:Dy+++ 3:F-',
    'ErCl3(aq)'       : '1:Er+++ 3:Cl-',
    'ErF3(aq)'        : '1:Er+++ 3:F-',
    'EuCl2(aq)'       : '1:Eu++ 2:Cl-',
    'EuCl3(aq)'       : '1:Eu+++ 3:Cl-',
    'EuF2(aq)'        : '1:Eu++ 2:F-',
    'EuF3(aq)'        : '1:Eu+++ 3:F-',
    'FeCl2(aq)'       : '1:Fe++ 2:Cl-',
    'FeHPO4(aq)'      : '1:Fe++ 1:HPO4--',
    'FeSO4(aq)'       : '1:Fe++ 1:SO4--',
    'GdCl3(aq)'       : '1:Gd+++ 3:Cl-',
    'GdF3(aq)'        : '1:Gd+++ 3:F-',
    'H2CrO4(aq)'      : '1:CrO4-- 2:H+',
    'H2F2(aq)'        : '2:F- 2:H+',
    'H2S(aq)'         : '1:H+ 1:HS-',
    'H2SO3(aq)'       : '1:SO3-- 2:H+',
    'H2SO4(aq)'       : '1:SO4-- 2:H+',
    'H2Se(aq)'        : '1:Se-- 2:H+',
    'H2SeO3(aq)'      : '1:SeO3-- 2:H+',
    'H2TcO4(aq)'      : '1:TcO4-- 2:H+',
    'H3AsO4(aq)'      : '1:H+ 1:H2AsO4-',
    'H3PO4(aq)'       : '1:HPO4-- 2:H+',
    'HBrO(aq)'        : '1:BrO- 1:H+',
    'HCN(aq)'         : '1:CN- 1:H+',
    'HCl(aq)'         : '1:Cl- 1:H+',
    'HClO(aq)'        : '1:ClO- 1:H+',
    'HClO2(aq)'       : '1:ClO2- 1:H+',
    'HF(aq)'          : '1:F- 1:H+',
    'HIO3(aq)'        : '1:H+ 1:IO3-',
    'HN3(aq)'         : '1:H+ 1:N3-',
    'HNO2(aq)'        : '1:H+ 1:NO2-',
    'HNO3(aq)'        : '1:H+ 1:NO3-',
    'HoCl3(aq)'       : '1:Ho+++ 3:Cl-',
    'HoF3(aq)'        : '1:Ho+++ 3:F-',
    'KBr(aq)'         : '1:Br- 1:K+',
    'KCl(aq)'         : '1:Cl- 1:K+',
    'KHSO4(aq)'       : '1:H+ 1:K+ 1:SO4--',
    'KI(aq)'          : '1:I- 1:K+',
    'LaCl3(aq)'       : '1:La+++ 3:Cl-',
    'LaF3(aq)'        : '1:La+++ 3:F-',
    'LiCl(aq)'        : '1:Cl- 1:Li+',
    'LuCl3(aq)'       : '1:Lu+++ 3:Cl-',
    'LuF3(aq)'        : '1:Lu+++ 3:F-',
    'MgHPO4(aq)'      : '1:HPO4-- 1:Mg++',
    'MgSO4(aq)'       : '1:Mg++ 1:SO4--',
    'Mn(NO3)2(aq)'    : '1:Mn++ 2:NO3-',
    'MnHPO4(aq)'      : '1:HPO4-- 1:Mn++',
    'MnSO4(aq)'       : '1:Mn++ 1:SO4--',
    'MnSeO4(aq)'      : '1:Mn++ 1:SeO4--',
    'NaBr(aq)'        : '1:Br- 1:Na+',
    'NaCl(aq)'        : '1:Cl- 1:Na+',
    'NaF(aq)'         : '1:F- 1:Na+',
    'NaHCO3(aq)'      : '1:HCO3- 1:Na+',
    'NaI(aq)'         : '1:I- 1:Na+',
    'NdCl3(aq)'       : '1:Nd+++ 3:Cl-',
    'NdF3(aq)'        : '1:Nd+++ 3:F-',
    'Ni(NO3)2(aq)'    : '1:Ni++ 2:NO3-',
    'NiSO4(aq)'       : '1:Ni++ 1:SO4--',
    'NiSeO4(aq)'      : '1:Ni++ 1:SeO4--',
    'Np(H2PO4)3(aq)'  : '1:Np+++ 3:H+ 3:HPO4--',
    'Np(HPO4)2(aq)'   : '1:Np++++ 2:HPO4--',
    'Np(SO4)2(aq)'    : '1:Np++++ 2:SO4--',
    'NpO2Cl(aq)'      : '1:Cl- 1:NpO2+',
    'NpO2F(aq)'       : '1:F- 1:NpO2+',
    'NpO2F2(aq)'      : '1:NpO2++ 2:F-',
    'NpO2H2PO4(aq)'   : '1:H+ 1:HPO4-- 1:NpO2+',
    'NpO2HPO4(aq)'    : '1:HPO4-- 1:NpO2++',
    'NpO2SO4(aq)'     : '1:NpO2++ 1:SO4--',
    'Pb(BrO3)2(aq)'   : '1:Pb++ 2:BrO3-',
    'Pb(ClO3)2(aq)'   : '1:Pb++ 2:ClO3-',
    'Pb(SCN)2(aq)'    : '1:Pb++ 2:SCN-',
    'PbBr2(aq)'       : '1:Pb++ 2:Br-',
    'PbCl2(aq)'       : '1:Pb++ 2:Cl-',
    'PbF2(aq)'        : '1:Pb++ 2:F-',
    'PbHPO4(aq)'      : '1:HPO4-- 1:Pb++',
    'PbI2(aq)'        : '1:Pb++ 2:I-',
    'PdCl2(aq)'       : '1:Pd++ 2:Cl-',
    'PrCl3(aq)'       : '1:Pr+++ 3:Cl-',
    'PrF3(aq)'        : '1:Pr+++ 3:F-',
    'Pu(HPO4)2(aq)'   : '1:Pu++++ 2:HPO4--',
    'Pu(SO4)2(aq)'    : '1:Pu++++ 2:SO4--',
    'PuF4(aq)'        : '1:Pu++++ 4:F-',
    'PuO2F2(aq)'      : '1:PuO2++ 2:F-',
    'PuO2SO4(aq)'     : '1:PuO2++ 1:SO4--',
    'RbBr(aq)'        : '1:Br- 1:Rb+',
    'RbCl(aq)'        : '1:Cl- 1:Rb+',
    'RbF(aq)'         : '1:F- 1:Rb+',
    'RbI(aq)'         : '1:I- 1:Rb+',
    'Ru(Cl)3(aq)'     : '1:Ru+++ 3:Cl-',
    'Ru(OH)2Cl2(aq)'  : '1:Ru(OH)2++ 2:Cl-',
    'Ru(OH)2SO4(aq)'  : '1:Ru(OH)2++ 1:SO4--',
    'RuSO4(aq)'       : '1:Ru++ 1:SO4--',
    'SmCl3(aq)'       : '1:Sm+++ 3:Cl-',
    'SmF3(aq)'        : '1:Sm+++ 3:F-',
    'Sn(SO4)2(aq)'    : '1:Sn++++ 2:SO4--',
    'SnCl2(aq)'       : '1:Sn++ 2:Cl-',
    'SnF2(aq)'        : '1:Sn++ 2:F-',
    'SrHPO4(aq)'      : '1:HPO4-- 1:Sr++',
    'SrSO4(aq)'       : '1:SO4-- 1:Sr++',
    'TbCl3(aq)'       : '1:Tb+++ 3:Cl-',
    'TbF3(aq)'        : '1:Tb+++ 3:F-',
    'Th(HPO4)2(aq)'   : '1:Th++++ 2:HPO4--',
    'Th(SO4)2(aq)'    : '1:Th++++ 2:SO4--',
    'ThCl4(aq)'       : '1:Th++++ 4:Cl-',
    'ThF4(aq)'        : '1:Th++++ 4:F-',
    'TmCl3(aq)'       : '1:Tm+++ 3:Cl-',
    'TmF3(aq)'        : '1:Tm+++ 3:F-',
    'U(SO4)2(aq)'     : '1:U++++ 2:SO4--',
    'UF4(aq)'         : '1:U++++ 4:F-',
    'UO2(H2PO4)2(aq)' : '1:UO2++ 2:H+ 2:HPO4--',
    'UO2(IO3)2(aq)'   : '1:UO2++ 2:IO3-',
    'UO2(N3)2(aq)'    : '1:UO2++ 2:N3-',
    'UO2(SCN)2(aq)'   : '1:UO2++ 2:SCN-',
    'UO2Cl2(aq)'      : '1:UO2++ 2:Cl-',
    'UO2F2(aq)'       : '1:UO2++ 2:F-',
    'UO2HPO4(aq)'     : '1:HPO4-- 1:UO2++',
    'UO2SO3(aq)'      : '1:SO3-- 1:UO2++',
    'UO2SO4(aq)'      : '1:SO4-- 1:UO2++',
    'VO2F(aq)'        : '1:F- 1:VO2+',
    'VO2H2PO4(aq)'    : '1:H+ 1:HPO4-- 1:VO2+',
    'VOF2(aq)'        : '1:VO++ 2:F-',
    'VOSO4(aq)'       : '1:SO4-- 1:VO++',
    'YF3(aq)'         : '1:Y+++ 3:F-',
    'YbCl3(aq)'       : '1:Yb+++ 3:Cl-',
    'YbF3(aq)'        : '1:Yb+++ 3:F-',
    'Zn(N3)2(aq)'     : '1:Zn++ 2:N3-',
    'Zn(SCN)2(aq)'    : '1:Zn++ 2:SCN-',
    'ZnBr2(aq)'       : '1:Zn++ 2:Br-',
    'ZnCl2(aq)'       : '1:Zn++ 2:Cl-',
    'ZnHPO4(aq)'      : '1:HPO4-- 1:Zn++',
    'ZnI2(aq)'        : '1:Zn++ 2:I-',
    'ZnSO4(aq)'       : '1:SO4-- 1:Zn++',
    'ZnSeO4(aq)'      : '1:SeO4-- 1:Zn++',
    'Zr(SO4)2(aq)'    : '1:Zr++++ 2:SO4--',
    'ZrF4(aq)'        : '1:Zr++++ 4:F-',
}

# The critical properties of the gases in the SUPCRT database, where:
#     omega = acentric factor
#        Tc = critical temperature (in units of K)
#        Pc = critical pressure (in units of bar)
critical_properties = {
    'Ar(g)'    : {'omega' : 0.0000,  'Tc' : 150.90,  'Pc' : 48.98},
    'CH4(g)'   : {'omega' : 0.0120,  'Tc' : 190.60,  'Pc' : 45.99},
    'C6H6O(g)' : {'omega' : 0.4440,  'Tc' : 694.30,  'Pc' : 61.30},
    'CO(g)'    : {'omega' : 0.0480,  'Tc' : 132.90,  'Pc' : 34.99},
    'CO2(g)'   : {'omega' : 0.2240,  'Tc' : 304.20,  'Pc' : 73.83},
    'C2H4(g)'  : {'omega' : 0.0870,  'Tc' : 282.30,  'Pc' : 50.40},
    'H2(g)'    : {'omega' : -0.2160, 'Tc' : 33.19,   'Pc' : 13.13},
    'H2O(g)'   : {'omega' : 0.3450,  'Tc' : 647.10,  'Pc' : 220.55},
    'H2S(g)'   : {'omega' : 0.0940,  'Tc' : 373.50,  'Pc' : 89.63},
    'He(g)'    : {'omega' : -0.3900, 'Tc' : 5.20,    'Pc' : 2.28},
    'Kr(g)'    : {'omega' : 0.0000,  'Tc' : 209.40,  'Pc' : 55.02},
    'N2(g)'    : {'omega' : 0.0380,  'Tc' : 126.20,  'Pc' : 34.00},
    'Ne(g)'    : {'omega' : 0.0000,  'Tc' : 44.00,   'Pc' : 27.00},
    'NH3(g)'   : {'omega' : 0.2530,  'Tc' : 405.70,  'Pc' : 112.80},
    'O2(g)'    : {'omega' : 0.0220,  'Tc' : 154.60,  'Pc' : 50.43},
    'Rn(g)'    : {'omega' : 0.0000,  'Tc' : 377.00,  'Pc' : 62.80},
    'SO2(g)'   : {'omega' : 0.2450,  'Tc' : 430.80,  'Pc' : 78.84},
    'Xe(g)'    : {'omega' : 0.0000,  'Tc' : 289.70,  'Pc' : 58.40},
    'NO(g)'    : {'omega' : 0.5830,  'Tc' : 180.20,  'Pc' : 64.80},
    'N2O(g)'   : {'omega' : 0.1410,  'Tc' : 309.60,  'Pc' : 72.45},
}