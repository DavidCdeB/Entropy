The entropy contains, among other terms, a summation over the phonon modes. 
This summation is the following:

![Data flow](https://github.com/DavidCdeB/Entropy/blob/master/log_S.png)

This repository will focus on the computation of this summation... Why? Because I have encontered a very interesting thing: This summation can present serious problems on the computation (because of the log dependence).

As has been discussed previously, the frecuencies vary with the volume according to a quadratic behaviour:

![Data flow](https://github.com/DavidCdeB/Entropy/blob/master/quadratic.png)

can be seen in the formula, 


I have created the function `S_sq`, (with input arguments `V`

