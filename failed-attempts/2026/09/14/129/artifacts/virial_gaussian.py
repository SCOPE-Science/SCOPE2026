"""Gaussian virial blowup data for focusing quintic NLS on R^4.
(i d_t + Delta) v = -|v|^4 v,  v0(x) = A exp(-|x|^2).
Verifies: mass, kinetic, potential, energy, variance, virial time,
negativity threshold A^4 > 108, and N^{-2} blowup-time scaling.
All integrals analytic for Gaussians; cross-checked by quadrature.
"""
import math

pi = math.pi

def stats(A):
    # analytic Gaussian integrals on R^4
    mass = A*A * pi*pi/4.0            # ||v0||_2^2
    kin = A*A * pi*pi                 # ||grad v0||_2^2
    pot6 = A**6 * pi*pi/36.0          # ||v0||_6^6
    E = 0.5*kin - pot6/6.0            # energy
    V0 = A*A * pi*pi/4.0              # variance int |x|^2|v0|^2
    Tvir = float('inf') if E >= 0 else math.sqrt(V0/(-8.0*E))
    return dict(A=A, mass=mass, kin=kin, pot6=pot6, E=E, V0=V0, Tvir=Tvir)

def quad_check(A, R=6.0, n=200000):
    # numerical radial quadrature check of mass and variance
    # int_R^4 f(r) dx = 2 pi^2 int_0^inf f(r) r^3 dr
    import numpy as np
    r = np.linspace(0, R, n)
    dr = r[1]-r[0]
    w = 2*pi*pi * r**3 * dr
    rho = A*A*np.exp(-2*r*r)
    return float(np.sum(w*rho)), float(np.sum(w*r*r*rho))

print("A, mass, kin, ||.||_6^6, E, V0, Tvir")
for A in [2.0, 2.5, 108**0.25, 3.5, 4.0, 5.0]:
    s = stats(A)
    print("A=%.4f mass=%.5f kin=%.5f P=%.5f E=%.5f V0=%.5f Tvir=%.6f"
          % (s['A'], s['mass'], s['kin'], s['pot6'], s['E'], s['V0'], s['Tvir']))

print("threshold 108^1/4 =", 108**0.25)
print("threshold 54^1/4 (wrong-kinetic warning) =", 54**0.25)

m, v = quad_check(4.0)
s = stats(4.0)
print("quad A=4: mass=%.5f (analytic %.5f) V0=%.5f (analytic %.5f)"
      % (m, s['mass'], v, s['V0']))

print("scaled torus blowup window T*/N^2 with T*=%.6f:" % s['Tvir'])
for N in [10, 50, 100, 500, 1000]:
    print("N=%5d  T*/N^2=%.3e  N^-1=%.1e" % (N, s['Tvir']/N/N, 1.0/N))

# concentration scalings: ||N^{1/2} v0(N.)||_{L^q} = N^{1/2-4/q}||v0||_q
print("data concentration scalings (relative to Euclidean v0 norms):")
for q in [2, 6]:
    for N in [10, 100, 1000]:
        print("q=%d N=%d factor N^{1/2-4/q}=%.3e" % (q, N, N**(0.5-4.0/q)))
