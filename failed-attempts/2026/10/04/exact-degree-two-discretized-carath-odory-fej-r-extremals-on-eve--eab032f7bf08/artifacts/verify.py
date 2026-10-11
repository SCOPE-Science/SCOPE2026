import math

def q(x, lam, c):
    return 1.0 + lam*x + c*(2.0*x*x-1.0)

max_err=0.0
strict_count=0
for m in range(4,5001):
    j=(3*m)//8
    k=(3*m + 7)//8
    u=math.cos(2*math.pi*k/m)
    v=math.cos(2*math.pi*j/m)
    den=1.0+2.0*u*v
    assert den > 0.0
    D=-2.0*(u+v)/den
    if m % 8 == 0:
        assert j == k
        assert abs(D-math.sqrt(2.0)) < 5e-12
        c=0.5
    else:
        assert k == j+1
        s=-1.0/math.sqrt(2.0)
        assert u < s < v
        c=1.0/den
        alpha=1.0-2.0*v*v
        beta=2.0*u*u-1.0
        assert alpha > 0.0 and beta > 0.0
        upper=-(alpha+beta)/(alpha*u+beta*v)
        max_err=max(max_err,abs(upper-D))
        assert abs(upper-D) < 2e-10
        assert D > math.sqrt(2.0)
        strict_count += 1
        max_err=max(max_err,abs(q(u,D,c)),abs(q(v,D,c)))
    vals=[q(math.cos(2*math.pi*r/m),D,c) for r in range(m)]
    assert min(vals) > -2e-10
print(f"VERIFY_OK m_max=5000 strict_cases={strict_count} max_error={max_err:.3e}")
