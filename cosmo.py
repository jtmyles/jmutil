import numpy as np

def Hz(z, H0=70, Omega_M=0.3, Omega_Lambda=0.7):
    tmp = H0**2 * (Omega_M * (1+z)**3 + Omega_Lambda)
    return np.sqrt(tmp)

def hz(z, H0=70, Omega_M=0.3, Omega_Lambda=0.7):
    return (1./100) * Hz(z, H0=H0, Omega_M=Omega_M, Omega_Lambda=Omega_Lambda)

def Ez(z, H0=70, Omega_M=0.3, Omega_Lambda=0.7):
    return Hz(z, H0=H0, Omega_M=0.3, Omega_Lambda=0.7) / H0
