"""Finite prime-field exhaustive witness checks for a three-dimensional algebra."""
from itertools import product

def normalize(x,p):
    x=tuple(a%p for a in x)
    for a in x:
        if a:
            t=pow(a,-1,p)
            return tuple((v*t)%p for v in x)
    return None

def dot(a,b,p):return sum(x*y for x,y in zip(a,b))%p

def mul(a,b,L,p):
    u=(-a[0]*b[0]-2*a[1]*b[1]+a[2]*b[2])%p
    v=(L*a[1]*b[1])%p
    return (u, v, (u+v)%p)
# U=e1+e3 and V=e2+e3; matrix coefficients in e_i coordinates: u*U+v*V=(u,v,u+v)
def in_span(x,basis,p):
    return any(tuple(sum(cs[j]*basis[j][i] for j in range(len(basis)))%p for i in range(3))==tuple(x) for cs in product(range(p),repeat=len(basis)))

def test(p,L):
    vec=list(product(range(p),repeat=3))
    lines=sorted(set(n for x in vec if (n:=normalize(x,p)) is not None))
    planes=sorted(lines)
    good_lines=[];good_planes=[]
    for x in lines:
        if in_span(mul(x,x,L,p),[x],p):good_lines.append(x)
    for n in planes:
        plane=[x for x in vec if dot(x,n,p)==0]
        b=[]
        for x in plane:
            if x!=(0,0,0) and not in_span(x,b,p):b.append(x)
            if len(b)==2:break
        if all(in_span(mul(x,y,L,p),b,p) for x in b for y in b):
            good_planes.append(n)
    u=normalize((1,0,1),p)
    w=normalize((1,0,-1),p)
    Uplane=normalize((0,1,0),p) # x_2=0
    Splane=normalize((-1,-1,1),p) # -x1-x2+x3=0
    Tplane=normalize((1,0,1),p) # x1+x3=0
    pred_lines={u,w}
    if L%p !=2:
        z=(pow(L*(2-L),-1,p),pow(L,-1,p),pow(L*(2-L),-1,p)+pow(L,-1,p))
        pred_lines.add(normalize(z,p))
    pred_planes={Uplane,Splane}
    if L%p ==4%p:pred_planes.add(Tplane)
    assert set(good_lines)==pred_lines,(p,L,good_lines,pred_lines)
    assert set(good_planes)==pred_planes,(p,L,good_planes,pred_planes)
    zero=(0,0,0)
    phi={x for x in vec if all(dot(x,n,p)==0 for n in good_planes)}
    predicted_phi={zero} if L%p==4%p else {tuple(t*u[i]%p for i in range(3)) for t in range(p)}
    assert phi==predicted_phi,(p,L,phi,predicted_phi)
    subs={frozenset([zero]),frozenset(vec)}
    for x in good_lines:
        subs.add(frozenset(tuple(t*x[i]%p for i in range(3)) for t in range(p)))
    for n in good_planes:
        subs.add(frozenset(x for x in vec if dot(x,n,p)==0))
    meet_generated=set()
    for mask in range(1<<len(good_planes)):
        meet_generated.add(frozenset(x for x in vec if all(dot(x,n,p)==0 for j,n in enumerate(good_planes) if mask>>j&1)))
    assert (subs==meet_generated)==(L%p==4%p),(p,L,subs,meet_generated)
    return len(good_lines),len(good_planes)

def main():
    cases=0
    for p in (3,5,7,11):
        for L in range(1,p):
            a,b=test(p,L)
            print(f'OK p={p} lambda={L} dimensions: lines={a} planes={b}')
            cases+=1
    print('VERIFY_OK',cases,'complete finite-field configurations')
if __name__=='__main__':main()
