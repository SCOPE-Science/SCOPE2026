import math

def solve_N(p):
    lo, hi = 1.000000001, 1.0/p
    f=lambda x: x*math.log(x)**4-1.0/p
    for _ in range(220):
        mid=(lo+hi)/2
        if f(mid)<0: lo=mid
        else: hi=mid
    return (lo+hi)/2
prev=None
for p in [1e-6,1e-10,1e-20,1e-40,1e-80]:
    n=solve_N(p)
    assert abs(p*n*math.log(n)**4-1)<1e-8
    r=p*n*math.log(1/p)**4
    if prev is not None: assert abs(r-1)<abs(prev-1)
    prev=r
assert abs(prev-1)<0.7
print("VERIFY_OK")
