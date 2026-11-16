"""Independent Gaussian jet-covariance check of the directional contact law.

Scientific reproducibility only. Requires numpy; checks algebraic identities against
Gaussian regression computed independently from Hermite coefficient derivatives.
"""
import math
import numpy as np


def formula(s, theta):
    d = 1 + 2*s*s + 2*s*(1-s)*math.cos(2*theta)
    p = (1-s)*math.cos(3*theta) + 3*s*math.cos(theta)
    return 6*s**4/d**2 + 8*s**3*(1-s)*p**2/d**3


def direct_regression(s, theta):
    a, b = math.sqrt(1-s), math.sqrt(s)
    t = np.exp(-1j*theta)
    pi = math.pi
    F = np.array([a,b,0,0],complex)
    Fu = math.sqrt(pi)*np.array([-b*np.conj(t),a*t,math.sqrt(2)*b*t,0],complex)
    Fv = -1j*math.sqrt(pi)*np.array([b*np.conj(t),a*t,math.sqrt(2)*b*t,0],complex)
    Fuu = pi*np.array([0,-2*b,math.sqrt(2)*a*t*t,math.sqrt(6)*b*t*t],complex)
    constraints = np.vstack([F,Fu])
    cond = np.vstack([Fuu,Fv])
    K = constraints @ constraints.conj().T
    det = np.linalg.det(K).real
    cov = cond @ cond.conj().T - cond @ constraints.conj().T @ np.linalg.inv(K) @ constraints @ cond.conj().T
    varP,varQ = cov[0,0].real,cov[1,1].real
    C = cov[1,0]
    moment = (varP*varQ + abs(C)**2 - 2*(C*C).real)/2
    return moment/(4*pi*pi*det)


def main():
    total = 0
    angles = [j*math.pi/37 for j in range(37)]
    for s in [0,0.0003,0.02,0.1,0.17,0.25,0.4,0.51,0.7,0.88,0.999,1]:
        for th in angles:
            independent,closed = direct_regression(s,th),formula(s,th)
            assert math.isclose(independent,closed,rel_tol=2e-9,abs_tol=5e-11),(s,th,independent,closed)
            total+=1
        if 0<s<1:
            time_formula = 2*s**3*(4+7*s-8*s*s)/(1+2*s)**2
            freq_formula = 6*s**4/(1-2*s+4*s*s)**2
            assert math.isclose(formula(s,0),time_formula,rel_tol=2e-12)
            assert math.isclose(formula(s,math.pi/2),freq_formula,rel_tol=2e-12)
            total+=2
    for th in angles:
        assert math.isclose(formula(1,th),2/3,rel_tol=2e-13)
        assert abs(formula(0,th))<1e-14
        total+=2
    for th in angles:
        for s in [1e-5,1e-6,1e-7]:
            leading = 8*math.cos(3*th)**2
            assert abs(formula(s,th)/s**3-leading)<4e-4
            total+=1
    print(f'DIRECTIONAL_CONTACT_CHECKS_PASSED {total}')

if __name__=='__main__':
    main()
