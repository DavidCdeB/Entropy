The vibrational entropy can be calculated as follows:

![Data flow](https://github.com/DavidCdeB/Entropy/blob/master/S_vib.png)

where:

![Data flow](https://github.com/DavidCdeB/Entropy/blob/master/ET.png)

The `ln` part can present some problems: If there is a negative frequency, then the exponential will be greater than 1, so that we will have `ln(negative number)`.

In a QHA framework, there might be certain volumes for which there are negative phonons at finte k-points. These negative phonon modes represent transition states to phase transitions. In many cases the energy difference between the broken symmetry strucutre and the "parent" structure is so low, that is below the DFT error bar. In these cases we shall not consider a phase transition, and we can compute the entropy of that volume, excluding this particular negative phonon mode from the summation.



The entropy contains, among other terms, a summation over the phonon modes. 
This summation is the following:

![Data flow](https://github.com/DavidCdeB/Entropy/blob/master/log_S.png)

This repository will focus on the computation of this summation... Why? Because I have encontered a very interesting thing: this summation can present serious problems on the computation (because of the log dependence).

As has been discussed previously, the frecuencies vary with the volume according to a quadratic behaviour:

![Data flow](https://github.com/DavidCdeB/Entropy/blob/master/quadratic.png)

The workflow is very simple:

**1)** The file `./done_modes_sorted.dat` contains the parameters for each normal mode:

```
# c               d                f                   mode
0.0685265337707 -30.0101460555174 3356.3806811965342 1.0000000000000
0.1422518723231 -65.3036881624374 7575.6223344565860 2.0000000000000
0.0071781843348 -5.8386124006698 1050.9676820938350 3.0000000000000
0.1262549911900 -58.3147083487940 6834.6861875675886 4.0000000000000
........
....
```

**2)** The function `nu` with input arguments `V` (Volume), `c`, `d` and `f` parameters

**3)** The function `S_sq` with input arguments `V` (Volume), `T` (Temperature), and  `c`, `d` and `f` parameters.

Thus:

```
def nu(V, c, d, f):
   return (c*V**2 + d*V + f) * conv_fac_nu

def S_sq(V, T, c, d, f):
   return  np.log (1.0 - np.exp((-h * nu(V, c, d, f))/(KB*T))  )

Gs = []
for V in Vs:
        aux = []
        for T in Ts:
                S_sq_sum = 0.0
                for c, d, f in zip(Cs, Ds, Fs):
                        S_sq_sum += S_sq(V, T, c, d, f)
                aux.append(S_sq_sum )

        Gs.append(aux)

print Gs
```

(`conv_fac_nu` is just a conversion factor)

When computing this summation for calcite I:

`python I.py`,

 it works OK. 

The interesting thing is that when computing this summation for calcite II:

`python II.py`,

there is a problem with the `log`:

`II.py:35: RuntimeWarning: invalid value encountered in log`

In this repository you can find:

```
done_modes_sorted_I.dat
done_modes_sorted_II.dat
I.py
II.py
```
