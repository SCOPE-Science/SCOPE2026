import math

def S_comp(y, lam, kappa):
    return (1.0+y/kappa)**(-lam)

def f_comp(y, lam, kappa):
    return (lam/kappa)*(1.0+y/kappa)**(-lam-1.0)

def evaluate(y, weights, lams, kappas):
    ss=[S_comp(y,l,k) for l,k in zip(lams,kappas)]
    fs=[f_comp(y,l,k) for l,k in zip(lams,kappas)]
    S=sum(w*s for w,s in zip(weights,ss))
    f=sum(w*v for w,v in zip(weights,fs))
    post=[w*s/S for w,s in zip(weights,ss)]
    return S,f,f/S,post

# Unique minimum.
w=[0.2,0.5,0.3]
l=[1.3,2.1,3.0]
k=[2.0,0.7,4.0]
lam=min(l)
C=w[0]*k[0]**lam
prev_err=None
for y in (1e3,1e5,1e7):
    S,f,h,p=evaluate(y,w,l,k)
    assert abs((y**lam)*S/C-1.0) < 0.03 if y==1e3 else abs((y**lam)*S/C-1.0) < 0.002
    assert abs(y*h/lam-1.0) < 0.03 if y==1e3 else abs(y*h/lam-1.0) < 0.002
    err=1.0-p[0]
    if prev_err is not None:
        assert err < prev_err
    prev_err=err
assert evaluate(1e7,w,l,k)[3][0] > 0.99999

# Tied minimum: limiting weights are proportional to w_m kappa_m^lambda.
w=[0.25,0.35,0.40]
l=[1.5,1.5,2.6]
k=[1.0,3.0,0.8]
lam=1.5
raw=[w[0]*k[0]**lam,w[1]*k[1]**lam]
C=sum(raw)
target=[raw[0]/C,raw[1]/C]
S,f,h,p=evaluate(1e8,w,l,k)
assert abs((1e8**lam)*S/C-1.0) < 1e-4
assert abs(1e8*h/lam-1.0) < 1e-4
assert abs(p[0]-target[0]) < 1e-4
assert abs(p[1]-target[1]) < 1e-4
assert p[2] < 1e-8
print('VERIFY_OK')
