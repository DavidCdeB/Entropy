The vibrational entropy can be calculated as follows:

![Data flow](https://github.com/DavidCdeB/Entropy/blob/master/S_vib.png)

where:

![Data flow](https://github.com/DavidCdeB/Entropy/blob/master/ET.png)

The `ln` part can present some problems: If there is a negative frequency, then the exponential in the 1st equation will be greater than 1, so that we will have `ln(negative number)`.

In a QHA framework, there might be certain volumes for which there are negative phonons at finte k-points. These negative phonon modes represent transition states to phase transitions. In many cases the energy difference between the broken symmetry strucutre and the "parent" structure is so low, that is below the DFT error bar. In these cases we shall not consider a phase transition, and we can compute the entropy of that volume, excluding this particular negative phonon mode from the summation.

In this repository you can find this file: `calcite_I_FREQCALC_V_110_SHRINK_3_3_RESTART.out`

which contains 2 negative modes:

```
 DISPERSION K POINT NUMBER    16 COORD:  C(  1  0  0 )    WEIGHT:    1.
['-22.12']

  DISPERSION K POINT NUMBER    46 COORD:  C(  3  0  0 )    WEIGHT:    1.
['-22.12']
```

The output states that the entropy has been calculated over 3597 modes:

```
THERMODYNAMICAL PROPERTIES ARE CALCULATED AS A SUM OVER  3597 MODES
```
The attached python script in this repository, calculates the entropy for each phonon mode in a cumulative way, i.e. `S[i] = S[i] + S[i-1]` 

The file `nu_S.dat` will be generated, in which it can be easily seen that when reaching a negative phonon mode, the entropy is `nan`:

```
# nu    S
70.96 9.63277365973e-05
91.79 0.00017935577073
111.67 0.000252374419967
114.45 0.000324147485279
144.93 0.000384110644395
151.7 0.000441828282425
...
1508.01 0.0234301056158
1564.85 0.0234301389345
1579.46 0.0234301696139
1605.22 0.0234301961342
1633.03 0.0234302187896
-22.12 nan
44.83 nan
81.07 nan
```
If the line:
```
#nu = nu[nu >= 0]
```
is uncommented, then only positive frequencies will be considered, the entropy will be calculated over 3595 modes, and the last line of the file `nu_S.dat` is the following: 


```
# nu    S
....
1639.08 0.0934227443243
```
which means that the final value of S(T=231.11 K) is 0.0934227443243 mHartree/K,
which coincides with the value reported in the output:
 
```
THERMODYNAMIC FUNCTIONS WITH VIBRATIONAL CONTRIBUTIONS

 AT (T =  231.11 K, P =   0.10132500E+00 MPA):

                          AU/CELL             EV/CELL                 KJ/MOL
 ET            :       0.012397841928       0.337362430026          32.55052939
 PV            :       0.000005131477       0.000139634598           0.01347269
 TS            :       0.021591231984       0.587527291591          56.68777158
 ET+PV-TS      :      -0.009188258579      -0.250025226967         -24.12376950
 EL+E0+ET+PV-TS:   -3765.932524929880 -102476.233794397034    -9887454.45080837

 OTHER THERMODYNAMIC FUNCTIONS:

                      mHARTREE/(CELL*K)     mEV/(CELL*K)              J/(MOL*K)
 ENTROPY       :       0.093423599930       2.542185396307         245.28362705
 HEAT CAPACITY :       0.101031655667       2.749211117901         265.25857457
```

This confirms that negative frequencies are not considered in the summation in CRYSTAL.

