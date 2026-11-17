"""Reproducibility diagnostics for the critical three-species food-chain map.
Finite numerical checks are not a proof of the asymptotic theorem.
Run with python3 CHECKER.py; only the standard library is used.
"""
import math


def simulate(beta, gamma, x, y, z, max_n=100000):
    assert 0 < x < 1 and 0 < y and 0 < z < x/2
    assert x+y+z < .5 and beta*x < .5 and gamma*y < .25
    ly, lz = math.log(y), math.log(z)
    results={}
    for n in range(1, max_n+1):
        oldx,oldy,oldz=x,y,z
        xn=oldx*(1-oldx-oldy-oldz)
        lnyn=ly+math.log(beta)+math.log(oldx-oldz)
        lnzn=lz+math.log(gamma)+ly
        yn=math.exp(lnyn) if lnyn > -700 else 0.
        zn=math.exp(lnzn) if lnzn > -700 else 0.
        # Algebraic reciprocal increment identity (double precision).
        tn=1/oldx; delta=1/xn-tn
        rhs=1/(1-oldx)+tn*(oldy+oldz)/((1-oldx-oldy-oldz)*(1-oldx))
        assert abs(delta-rhs)<1e-8*max(1,abs(delta))
        assert 0<xn<oldx and lnyn<ly and lnzn<lz
        x,y,z,ly,lz=xn,yn,zn,lnyn,lnzn
        if n in (1000,10000,100000):
            H=1/x-n-math.log(n)
            ell=ly+math.lgamma(n)-n*math.log(beta)+H*math.log(n)+.5*math.log(n)**2
            apex=(lz+.5*n*n*math.log(n))/(n*n)
            results[n]=(H,ell,apex)
    assert abs(results[100000][0]-results[10000][0])<.015
    assert abs(results[100000][1]-results[10000][1])<.2
    assert abs(results[100000][2]-(.75+.5*math.log(beta)))<.008
    return results

if __name__=='__main__':
    for beta,gamma,x,y,z in [(3.,7.,.04,.004,.001),(2.5,5.,.03,.003,.0005),(5.,9.4,.015,.002,.0001)]:
        result=simulate(beta,gamma,x,y,z)
        print(f'beta={beta:g}, gamma={gamma:g}, target_apex_second={.75+.5*math.log(beta):.9f}')
        for n, (H,ell,apex) in result.items():
            print(f'  n={n}: inverse_shift={H:.9f}, log_normalized_middle={ell:.9f}, apex_second={apex:.9f}')
    print('FINITE_DIAGNOSTICS_PASS')
