import numpy as np
L=3.7081493546027438
us=np.load("lane_work/ugrid.npy")
M=len(us)
h=L/M
# Fourier interpolant eval of u at arbitrary x via FFT coeffs
Uh=np.fft.rfft(us)
def u_eval(x):
    # evaluate trig polynomial: us is bandlimited approx; use linear interp on grid (fine enough for scout)
    t=(x/L*M)%M
    i=int(t)%M; f=t-int(t)
    return us[i]*(1-f)+us[(i+1)%M]*f
def monodromy(lam, nsteps=20000):
    hh=L/nsteps
    # RK4 on Y=(y1,y1p,y2,y2p)
    Y=np.array([1.0,0.0,0.0,1.0])
    x=0.0
    for k in range(nsteps):
        def f(xx,YY):
            u=u_eval(xx)
            return np.array([YY[1],(u-lam)*YY[0],YY[3],(u-lam)*YY[2]])
        k1=f(x,Y); k2=f(x+hh/2,Y+hh/2*k1); k3=f(x+hh/2,Y+hh/2*k2); k4=f(x+hh,Y+hh*k3)
        Y=Y+hh/6*(k1+2*k2+2*k3+k4); x+=hh
    return Y[0]+Y[3]
for lam in [0.96734678,1.0,1.32220497,2.27404472,3.99916923,4.0817455,7.59793936,7.59977507,12.61414654,12.61422324]:
    print(f"{lam:.8f} D={monodromy(lam):.8f}")
