import cmath, math, random

def qstar(alpha, lamb):
    return 2.0*(1.0+alpha)/((1.0+alpha)+lamb*(1.0-alpha))

def trace_det(alpha, lamb, q):
    tr = 1.0 + alpha - q*(1.0 + lamb*(1.0-alpha))
    det = alpha*(1.0-q)
    return tr, det

def roots(alpha, lamb, q):
    tr, det = trace_det(alpha,lamb,q)
    disc = cmath.sqrt(tr*tr - 4.0*det)
    return ((tr+disc)/2.0, (tr-disc)/2.0)

def schur_terms(alpha,lamb,q):
    tr,det=trace_det(alpha,lamb,q)
    return (1.0-tr+det, 1.0+tr+det, 1.0-det)

def nyquist_gain(alpha,lamb):
    return 1.0 + lamb*(1.0-alpha)/(1.0+alpha)

random.seed(19)

# Exact algebraic identities, evaluated on randomized parameters.
for _ in range(2000):
    a=random.random()*0.999999
    l=random.random()*8.0
    q=10.0**random.uniform(-5,1)
    s1,s2,s3=schur_terms(a,l,q)
    e1=q*(1.0-a)*(1.0+l)
    e2=2.0*(1.0+a)-q*((1.0+a)+l*(1.0-a))
    e3=1.0-a+a*q
    assert abs(s1-e1) < 2e-12*max(1.0,abs(e1))
    assert abs(s2-e2) < 2e-12*max(1.0,abs(e2))
    assert abs(s3-e3) < 2e-12*max(1.0,abs(e3))

# Randomized checks on both sides of the sharp stability boundary.
for _ in range(2000):
    a=random.random()*0.999
    l=random.random()*10.0
    qs=qstar(a,l)
    q=qs*random.uniform(1e-4,0.999999)
    rr=roots(a,l,q)
    assert max(abs(z) for z in rr) < 1.0
    q=qs*random.uniform(1.000001,3.0)
    rr=roots(a,l,q)
    assert max(abs(z) for z in rr) > 1.0

# The sharp boundary is an alternating mode r=-1.
for a,l in ((0.0,0.0),(0.2,0.1),(0.8,5.0),(0.98,2.0),(0.99,5.0)):
    qs=qstar(a,l)
    tr,det=trace_det(a,l,qs)
    poly_at_minus_one=1.0+tr+det
    assert abs(poly_at_minus_one) < 2e-13
    rr=roots(a,l,qs)
    assert min(abs(z+1.0) for z in rr) < 2e-12

# The ceiling is twice the reciprocal total gain at Nyquist frequency.
for _ in range(1000):
    a=random.random()*0.9999
    l=random.random()*10.0
    assert abs(qstar(a,l)-2.0/nyquist_gain(a,l)) < 2e-14

# Documented defaults alpha=0.98, lambda=2.
a=0.98
l=2.0
qs=qstar(a,l)
assert abs(nyquist_gain(a,l)-101.0/99.0) < 2e-15
assert abs(qs-198.0/101.0) < 2e-15
assert abs((1.0+l)-3.0) < 1e-15
relative_margin_loss=1.0-qs/2.0
assert abs(relative_margin_loss-2.0/101.0) < 2e-15

# Aggressive corner of the paper's recommended alpha/lambda ranges.
a=0.8
l=5.0
assert abs(qstar(a,l)-9.0/7.0) < 2e-15

print('verification passed')
