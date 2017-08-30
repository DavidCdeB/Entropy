#

import numpy as np
import sys

vol, nu, mode  = np.loadtxt('freqs_vol_110.dat', skiprows = 1).T  

# To remove negative modes:
#nu = nu[nu >= 0]

print 'nu = ', nu


################### CONSTANTS   ###############

# KB = boltmann cte, KB = 1.38064852(79)x10-23 J/K
KB = 1.38064852E-23

# h = plank constant, h = 6.626070040(81)x10-34 J s
h = 6.626070040E-34

# T = temperature, T = 298.15 K
#T = 298.15
T = 231.11

# c = speed of light, c = 2.99792458E8 m/s
c = 2.99792458E+8


print 'nu =', nu

# Correct formula of the entropy:
S = -KB * np.log(1 - np.exp(-h * nu * 1E+2 * c  / (KB*T)))     + ( (h/T) * ( nu * 1E+2 * c * ( (np.exp(h *  nu  * 1E+2 * c  / (KB*T)) - 1)**(-1) )    )  )

# Modification of the formula of the entropy:
#S = -KB * np.log(1 - np.exp(-h * nu * 1E+2 * c  / (KB*T)))    # + ( (h/T) * ( nu * 1E+2 * c * ( (np.exp(h *  nu  * 1E+2 * c  / (KB*T)) - 1)**(-1) )    )  )

print 'S= ', S

print 'length of S is = ', len(S)

# S is in J/K.
# Conversion: S above this line is in mHartree/K:
S = S  *((1/4.3597482)*1E+18 * 1E+3)

print S
for i in xrange(1,len(S)):
    S[i] = S[i] + S[i-1]
print 'length of S is = ', len(S)

#S = S *((1/4.3597482)*1E+18 * 1E+3)
#print S

#Now, the normalization of the entropy to the number of K points 
S = S / 60.0
output_array = np.vstack((nu, S)).T
np.savetxt('nu_S.dat', output_array, header="nu\tS", fmt="%0.12g")






