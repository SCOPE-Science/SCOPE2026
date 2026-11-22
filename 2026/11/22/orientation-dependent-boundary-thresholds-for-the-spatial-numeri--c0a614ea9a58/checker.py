"""Deterministic finite numerical diagnostics for spatial numerical-radius boundary formulas.
The infinite-dimensional theorem is proved analytically in RESULT.md.
"""
import numpy as np

def radius_formula(p,t,forward):
    critical=(p-1)/p if forward else 1/p
    if t <= critical:
        return 1.0
    if forward:
        r=(p-1)/(p*t)
        return t+r**(p-1)/p
    r=(1/(p*t))**(1/(p-1))
    return t+(p-1)*r/p

def functional(u,p,t,forward):
    u=np.asarray(u, dtype=np.float64)
    u=u/np.linalg.norm(u,ord=p)
    if forward:
        return t*u[0]**p+np.dot(u[:-1],u[1:]**(p-1))
    return t*u[0]**p+np.dot(u[:-1]**(p-1),u[1:])

def check():
    rng=np.random.default_rng(20260621)
    count=0
    for p in [1.2,1.5,2.,3.,4.5]:
        for forward in [True,False]:
            tc=(p-1)/p if forward else 1/p
            for t in [0,tc*.8,tc,tc*1.02,tc*1.5,tc*3]:
                bound=radius_formula(p,t,forward)
                for n in [4,13,32]:
                    for _ in range(160):
                        u=rng.random(n)
                        value=functional(u,p,t,forward)
                        assert value <=bound+1e-12, (p,t,forward,n,value,bound)
                        count+=1
                if t>tc:
                    r=(p-1)/(p*t) if forward else (1/(p*t))**(1/(p-1))
                    # Closed-form value of the normalized infinite geometric extremizer.
                    value=t*(1-r**p)+(r**(p-1) if forward else r)
                    assert abs(value-bound)<3e-12, (p,t,forward,value,bound)
                    count+=1
                # Local onset (independent of shift orientation) at criticality.
            for delta in [1.e-3, 5.e-4, 2.e-4]:
                predicted=p*p/(2*(p-1))
                quotient=(radius_formula(p,tc+delta,forward)-1)/delta**2
                assert abs(quotient/predicted-1)<0.02,(p,forward,delta,quotient,predicted)
                count+=1
    print('BOUNDARY_NUMERICAL_RADIUS_DIAGNOSTIC_OK',count)

if __name__=='__main__': check()
