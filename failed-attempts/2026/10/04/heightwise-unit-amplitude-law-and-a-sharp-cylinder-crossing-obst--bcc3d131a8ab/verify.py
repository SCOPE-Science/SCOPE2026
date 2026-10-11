from fractions import Fraction as F

N = 3

def mon(*e):
    return {tuple(e): F(1)}

def const(q):
    return {(0,)*N: F(q)}

def add(p,q):
    r=dict(p)
    for k,v in q.items():
        r[k]=r.get(k,F(0))+v
        if not r[k]:
            del r[k]
    return r

def neg(p):
    return {k:-v for k,v in p.items()}

def sub(p,q):
    return add(p,neg(q))

def mul(p,q):
    r={}
    for e,u in p.items():
        for f,v in q.items():
            g=tuple(e[i]+f[i] for i in range(N))
            r[g]=r.get(g,F(0))+u*v
    return {k:v for k,v in r.items() if v}

def scale(p,s):
    s=F(s)
    return {k:s*v for k,v in p.items() if s*v}

def deriv(p,i):
    r={}
    for e,v in p.items():
        if e[i]:
            g=list(e)
            g[i]-=1
            g=tuple(g)
            r[g]=r.get(g,F(0))+v*e[i]
    return {k:v for k,v in r.items() if v}

def eq(p,q):
    return sub(p,q)=={}

x=mon(1,0,0)
y=mon(0,1,0)
z=mon(0,0,1)

fx=mul(y,z)
fy=sub(x,y)
fz=sub(const(1),mul(x,x))
field=[fx,fy,fz]

def L(p):
    r={}
    for i in range(N):
        r=add(r,mul(deriv(p,i),field[i]))
    return r

assert eq(L(z), sub(const(1),mul(x,x)))
assert eq(L(mul(y,y)), scale(mul(y,sub(x,y)),2))
assert eq(L(mul(x,y)), add(add(mul(mul(y,y),z),mul(x,x)),neg(mul(x,y))))

lhs=mul(sub(x,y),sub(x,y))
rhs=add(sub(mul(x,x),mul(y,y)),scale(mul(y,sub(y,x)),2))
assert eq(lhs,rhs)

print("VERIFY_OK")
