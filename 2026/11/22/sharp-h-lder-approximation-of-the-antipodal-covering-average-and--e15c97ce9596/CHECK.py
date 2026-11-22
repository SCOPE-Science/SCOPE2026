"""Finite transport diagnostics for concave-metric antipodal covering approximation.

The infinite-dimensional theorem requires a separate mathematical proof. The
checks below verify the explicit test-family costs by finite transport LP
vertex enumeration, independently of the proof's closed formula.
"""
import itertools
import math


def circle_distance(u, v):
    d = (u-v) % 2.0
    return min(d, 2.0-d)


def w1_to_antipodes(sample, phi):
    """Exact finite-minimum form of transport LP with two half-unit sinks."""
    m = len(sample)
    ca = [phi(circle_distance(u, 0.0)) for u in sample]
    cb = [phi(circle_distance(u, 1.0)) for u in sample]
    k = m // 2
    if m % 2 == 0:
        return min((sum(ca[i] if i in A else cb[i] for i in range(m))/m)
                   for A in map(set, itertools.combinations(range(m), k)))
    ans = float('inf')
    for j in range(m):
        other = [i for i in range(m) if i != j]
        for A in itertools.combinations(other,k):
            a = set(A)
            val = (0.5*(ca[j]+cb[j])+sum(ca[i] if i in a else cb[i] for i in other))/m
            ans = min(ans,val)
    return ans


def partial_movement(m,t):
    """Relative sheet coordinates of continuous 1-periodic circle maps."""
    k=m//2
    if m % 2:
        start=[0.0]*(k+1)+[1.0]*k
        order=[]
        for i in range(k):
            order.extend([i,k+1+i])
        order.append(k)
    else:
        start=[0.0]*k+[1.0]*k
        order=[]
        for i in range(k):
            order.extend([i,k+i])
    step=min(int(t*m),m-1)
    frac=min(max(t*m-step,0),1)
    vals=start[:]
    for idx in order[:step]: vals[idx]=1-vals[idx]
    idx=order[step]
    vals[idx]=start[idx]+frac*(1-2*start[idx])
    return vals


def run():
    ncheck=0
    for m in range(1,10):
        for name,phi in (("snowflake 1/4",lambda z:z**0.25),
                         ("snowflake 1/2",lambda z:z**0.5),
                         ("snowflake 3/4",lambda z:z**0.75),
                         ("geodesic boundary",lambda z:z),
                         ("concave blend",lambda z:(z+math.sqrt(z))/2),
                         ("logarithmic",lambda z:math.log1p(3*z)/math.log(4))):
            limit=(phi(0.5) if m%2 else 1.0)/m
            max_value=0.0
            for i in range(10*m+1):
                t=i/(10*m)
                a=partial_movement(m,t)
                error=w1_to_antipodes(a,phi)
                if error>limit+2e-12:
                    raise AssertionError((m,name,t,error,limit))
                max_value=max(max_value,error)
                ncheck+=1
            if abs(max_value-limit)>2e-12:
                raise AssertionError(('sharpness',m,name,max_value,limit))
    for m in range(1,10):
        start=partial_movement(m,0)
        end=partial_movement(m,1)
        for v,w in zip(start,end):
            if abs(v+w-1)>1e-12:
                raise AssertionError(('glue',m,start,end))
            ncheck+=1
    print('CONCAVE_CIRCLE_TRANSPORT_DIAGNOSTIC_OK',ncheck)


if __name__=='__main__':
    run()
