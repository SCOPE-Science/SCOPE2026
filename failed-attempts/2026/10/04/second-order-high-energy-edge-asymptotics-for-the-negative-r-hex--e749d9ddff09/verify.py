import math

def hplus(k):
    return (1-18*k*k+9*k**4)/(3*k*k+1)**2

def hminus(k):
    return (1-3*k*k)/(1+3*k*k)

def bisect(f,a,b,it=100):
    fa,fb=f(a),f(b)
    if fa==0: return a
    if fb==0: return b
    assert fa*fb<0,(a,b,fa,fb)
    for _ in range(it):
        c=(a+b)/2; fc=f(c)
        if fa*fc<=0: b,fb=c,fc
        else: a,fa=c,fc
    return (a+b)/2

def root_near(m,l,q):
    K=m*math.pi/(2*l)
    if m%2==0:
        a=2/(math.sqrt(3)*l)
        pred=K+q*a/K
        f=lambda k: math.cos(2*l*(k-K))-hplus(k)
    else:
        a=1/(math.sqrt(3)*l)
        pred=K+q*a/K
        f=lambda k: -math.cos(2*l*(k-K))-hminus(k)
    rad=0.45*a/K
    return bisect(f,pred-rad,pred+rad)

def energy_pred(m,l,q):
    K=m*math.pi/(2*l)
    if m%2==0:
        lead=q*4/(math.sqrt(3)*l)
        C=-4/(3*l*l)-q*4*math.sqrt(3)/(27*l)
    else:
        lead=q*2/(math.sqrt(3)*l)
        C=-1/(3*l*l)-q*2*math.sqrt(3)/(27*l)
    return K*K+lead+C/(K*K)

for l in (0.8,1.0,1.7):
    for parity in (0,1):
        prev=None
        for m in ((20,40,80,160) if parity==0 else (21,41,81,161)):
            errs=[]
            for q in (-1,1):
                k=root_near(m,l,q)
                err=abs(k*k-energy_pred(m,l,q))
                errs.append(err)
            mx=max(errs)
            if prev is not None:
                assert mx < prev/8.0, (l,parity,m,mx,prev)
            prev=mx
        print('OK',l,'even' if parity==0 else 'odd','last_error',prev)
# Exact algebraic consistency of center/flat-band parity:
for m in range(2,20,2):
    l=1.3; K=m*math.pi/(2*l)
    assert abs(math.sin(K*l))<1e-12
for m in range(1,20,2):
    l=1.3; K=m*math.pi/(2*l)
    assert abs(abs(math.sin(K*l))-1)<1e-12
print('VERIFY_OK')
