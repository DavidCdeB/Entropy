#
import numpy as np

################### CONSTANTS: 
global KB, h, speed_of_light, U0, V0, B0, B0_prime, N_k, conv_fac_nu, conv_fac_denu

# Value of the constants:
# KB = boltmann cte, KB = 1.38064852(79)x10-23 J/K
KB = 1.38064852E-23

# h = plank constant, h = 6.626070040(81)x10-34 J s
h = 6.626070040E-34

# c = speed of light, c = 2.99792458E8 m/s
speed_of_light = 2.99792458E+8

conv_fac_nu =  1E+2 * speed_of_light  

##### For each "i" frequency, there is a c_i, d_i and f_i :
Cs, Ds, Fs, mode = np.loadtxt('./done_modes_sorted_I.dat', skiprows = 1).T


#### Here I set the values of "T" and "V" for which I would like
# to calculate G.
Ts = np.linspace(10.0, 2000.0, 100)
print Ts

#Vs = np.linspace(116.573346,137.200672, 100) 

# The same Vs as we computed on DFT:
Vs = np.array([ 116.573346 , 118.139505 , 119.713653 , 121.297131 , 122.894958 , 124.510211, \
  124.512598,  125.884132 , 127.054446 , 127.265886 , 128.656314,  130.054927,\
  131.463313 , 132.880152 , 134.309582 , 135.750582 , 137.200672])


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


