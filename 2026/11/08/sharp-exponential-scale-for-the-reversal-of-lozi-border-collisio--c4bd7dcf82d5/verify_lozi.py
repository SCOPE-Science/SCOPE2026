"""Finite symbolic and numerical consistency checks for a Lozi threshold asymptotic.

The analytic proof is in RESULT.md; this script does not prove uniformity in m.
"""

def poly_add(a,b):
    out=[0]*max(len(a),len(b))
    for i,v in enumerate(a):out[i]+=v
    for i,v in enumerate(b):out[i]+=v
    return out

def poly_mul_a(a):return [0]+a

def poly_sub(a,b):return poly_add(a,[-v for v in b])

def poly_eval(a,x):return sum(v*x**i for i,v in enumerate(a))

def return_poly(m,n):
    x=[0]
    for s in '++'+'-'*(m-2)+'++'+'-'*(n-2):
        x=poly_add(poly_sub([-1,1],[v if s=='+' else -v for v in poly_mul_a(x)]),[0])
    return x

def predicted(m,n):
    # a^(m+n-1)*(2-a)-2*a^(n-1)*(a-1)-1
    x=[-1]
    term=[0]*(m+n-1)+[2,-1]
    x=poly_add(x,term)
    x=poly_sub(x,[0]*(n-1)+[2*(-1),2])
    return x

for m in range(5,21):
    for n in (2,3):
        v=return_poly(m,n);w=predicted(m,n)
        assert poly_add(v,[-z for z in w])==[0]*max(len(v),len(w))


def residual(a,b,m,n):
    x=y=0.0
    dx,dy=0.0,1.0
    for sign in '++'+'-'*(m-2)+'++'+'-'*(n-2):
        q=1 if sign=='-' else -1
        x,y=a-b-1+q*a*x-b*y,x
        dx,dy=q*a*dx-b*dy,dx
    return x+dx*y/(1-dy)

def crossing(m):
    a,b=2-2.375*2**(-m),2**(-m-2)
    for _ in range(35):
        f=residual(a,b,m,2);g=residual(a,b,m,3)
        if max(abs(f),abs(g))<1e-8: return a,b
        ha=1e-7; hb=1e-8
        fa=(residual(a+ha,b,m,2)-f)/ha
        ga=(residual(a+ha,b,m,3)-g)/ha
        fb=(residual(a,b+hb,m,2)-f)/hb
        gb=(residual(a,b+hb,m,3)-g)/hb
        det=fa*gb-fb*ga
        assert abs(det)>1e-8
        da=(-f*gb+fb*g)/det
        db=(-fa*g+ga*f)/det
        assert abs(da)<.1 and abs(db)<.1
        a,b=a+da,b+db
    raise RuntimeError("no convergence")
for m in (6,8,10,12):
    a,b=crossing(m)
    ratio=(2**(m+2))*b
    assert .9<ratio<1.20
    assert abs(residual(a,b,m,2))<1e-7
    assert abs(residual(a,b,m,3))<1e-7
    print(f'm={m} a={a:.11g} b={b:.11g} scaled={ratio:.9f}')
print('LOZI_EXACT_POLYNOMIAL_AND_NUMERICAL_CROSSINGS_OK')
