"""Independent finite-field checks for a four-dimensional perm superalgebra.
Run with Python 3, no external packages. This is a finite check, not the general proof.
"""
from itertools import product

BASIS = [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]

def action(v, v8, p):
    a,b,c,d,h,j,r,s = v8
    x,y,z,w = v
    return ((a*x+c*y)%p, (b*x+d*y)%p, (h*z+r*w)%p, (j*z+s*w)%p)

def prod(x,y,p):
    return (0,(x[2]*y[2])%p,0,(x[0]*y[2])%p)

def add(*vectors,p):
    return tuple(sum(v[i] for v in vectors)%p for i in range(4))

def minus(x,y,p):
    return tuple((x[i]-y[i])%p for i in range(4))

def is_nijenhuis(v,p):
    for x in BASIS:
        for y in BASIS:
            nx=action(x,v,p); ny=action(y,v,p)
            lhs=add(prod(nx,ny,p), action(action(prod(x,y,p),v,p),v,p), p=p)
            rhs=action(add(prod(nx,y,p),prod(x,ny,p),p=p),v,p)
            if lhs!=rhs: return False
    return True

def on_components(v,p):
    a,b,c,d,h,j,r,s=v
    if r%p: return (False,False,False)
    c1=(c%p==0 and (d-h)%p==0 and (a-s)%p==0)
    c2=(c%p==0 and (d-h)%p==0 and (s-h)%p==0)
    c3=((s-h)%p==0 and (a+d-2*h)%p==0 and (b*c+(d-h)**2)%p==0)
    return (c1,c2,c3)

def det(v,p):
    a,b,c,d,h,j,r,s=v
    return ((a*d-b*c)*(h*s-j*r))%p

def check(q,all_r=True):
    values=range(q)
    tested=valid=invertible=0
    comps=[0,0,0]
    # Explicit coordinate order (a,b,c,d,h,j,r,s).
    samples=product(values,repeat=8) if all_r else ((a,b,c,d,h,j,0,s) for a,b,c,d,h,j,s in product(values,repeat=7))
    for v in samples:
        tested+=1
        ci=on_components(v,q); predicted=any(ci)
        actual=is_nijenhuis(v,q)
        if actual!=predicted:
            raise AssertionError(f'Classification failed modulo {q}: {v}: {actual=} {ci=}')
        if actual:
            valid+=1
            invertible+=(det(v,q)!=0)
            for i in range(3): comps[i]+=ci[i]
    expected=q**3*(3*q-2)
    expected_inv=q**2*(q-1)*(3*q-4)
    assert (valid,invertible,comps)==(expected,expected_inv,[q**4]*3), (q,tested,valid,invertible,comps)
    print(f'GF({q}): {tested} tuples checked; {valid} Nijenhuis; {invertible} invertible; components {comps}; PASS')

if __name__=='__main__':
    check(2)
    check(3)
    check(5,all_r=False) # r != 0 is ruled out identically by f2,f2 coefficient r^2.
    print('FOUR_DIMENSIONAL_PERM_SUPER_NIJENHUIS_OK')
