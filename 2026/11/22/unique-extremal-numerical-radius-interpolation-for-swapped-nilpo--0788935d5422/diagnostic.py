"""Numerical cross-checks for a sharp two-point numerical-radius interpolant.
The analytic proof is in RESULT.md; this is finite corroboration only.
"""
import cmath, math

def crit(q,z):
    a=q/(1+q*q)
    return ((0j,a*(1+z*z)-z),(a*(1+z*z)+z,0j))

def numerical_radius_offdiag(u,v):
    return (abs(u)+abs(v))/2

def run():
    tests=0
    for k in range(1,50):
        q=k/50
        t=2*q
        Fm=crit(q,-q); Fp=crit(q,q)
        assert abs(Fm[0][1]-t)<1e-12 and abs(Fm[1][0])<1e-12
        assert abs(Fp[1][0]-t)<1e-12 and abs(Fp[0][1])<1e-12
        tests+=4
        rho=2*q/(1+q*q)
        assert abs(4*t/(4+t*t)-rho)<1e-12
        tests+=1
        for j in range(96):
            z=cmath.exp(2j*math.pi*j/96)
            M=crit(q,z)
            assert abs(numerical_radius_offdiag(M[0][1],M[1][0])-1)<1e-12
            tests+=1
        # For farther-apart sampling, strict contraction via precomposition.
        s=(q+1)/2
        assert s>q
        radial=q/s
        maxrad=max(numerical_radius_offdiag(crit(q,radial*cmath.exp(2j*math.pi*j/96))[0][1],crit(q,radial*cmath.exp(2j*math.pi*j/96))[1][0]) for j in range(96))
        assert maxrad<1-1e-10, (q,maxrad)
        tests+=1
    print('NUSCHUR_RIGIDITY_DIAGNOSTIC_OK',tests)
if __name__=='__main__': run()
