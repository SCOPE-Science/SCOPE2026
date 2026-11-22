#!/usr/bin/env python3
"""Reproducible finite checks for the cosine-map inverse-tail identities.

Numerical finite diagnostics only; the stated infinite laws require the written proof.
"""
import math


def g(x, theta, omega):
    return x * math.cos(theta - omega*x)


def gp(x, theta, omega):
    return math.cos(theta-omega*x) + omega*x*math.sin(theta-omega*x)


def large_roots(q, theta, omega, R):
    # Only use phase cells whose |center|>20, where monotonicity holds
    # at this diagnostic q and omega.
    kk = int(abs(omega)*(R+10)/math.pi)+20
    roots=[]
    for k in range(-kk,kk+1):
        z=(theta-(k+0.5)*math.pi)/omega
        if abs(z)<=20 or abs(z)>R+2: continue
        a=z-math.pi/(3*abs(omega))
        b=z+math.pi/(3*abs(omega))
        fa=g(a,theta,omega)-q
        fb=g(b,theta,omega)-q
        if fa*fb>0: continue
        for _ in range(55):
            m=(a+b)/2
            fm=g(m,theta,omega)-q
            if fa*fm<=0: b=m; fb=fm
            else: a=m;fa=fm
        x=(a+b)/2
        if abs(x)<=R: roots.append(x)
    return roots


def test():
    a,B,d,e = 0.01,1.2,1.,1.
    U,V = a+0.37*B,0.2
    q=(U-a)/B; theta=d*V; omega=d*e
    out=[]
    for R in (200,1000,2000,10000):
        roots=large_roots(q,theta,omega,R)
        for x in roots:
            y=V-e*x
            assert abs(a+B*x*math.cos(d*y)-U)<1e-7
            assert abs(y+e*x-V)<1e-10
            assert abs(gp(x,theta,omega))>0
        val=sum(1/(abs(B)*abs(gp(x,theta,omega))) for x in roots)
        out.append((R,len(roots),val))
    expected_count=2*abs(omega)/math.pi
    expected_weight=2/(math.pi*abs(B))
    for R,n,w in out:
        assert abs(n/R-expected_count)<1.1
    for (R1,n1,w1),(R2,n2,w2) in zip(out,out[1:]):
        target=expected_weight*math.log(R2/R1)
        assert abs((w2-w1)-target)<0.08, (R1,R2,w2-w1,target)
    print('COSINE_MAP_INVERSE_TAIL_VERIFY_OK')
    print('Count coefficient 2|de|/pi:',format(expected_count,'.10f'))
    print('Weight coefficient 2/(pi|bc|):',format(expected_weight,'.10f'))
    for R,n,w in out:
        print('R=%d distant_root_count=%d weighted_tail=%.10f'%(R,n,w))
    for i in range(len(out)-1):
        r1,n1,w1=out[i];r2,n2,w2=out[i+1]
        print('R=%d..%d observed_delta=%.7f expected_delta=%.7f'%(r1,r2,w2-w1,expected_weight*math.log(r2/r1)))

if __name__=='__main__':test()
