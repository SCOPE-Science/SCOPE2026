"""Enumerate algebra automorphisms directly from the multiplication table of k[x,y]/(x²,y²)."""
from itertools import product

def gf_mul(q,a,b):
    poly={2:3,4:7}[q]
    result=0
    while b:
        if b&1:result ^=a
        b>>=1
        a<<=1
        if a&q:a ^=poly
    return result

def test(q):
    mul=lambda a,b:gf_mul(q,a,b)
    def alg_mul(u,v):
        return (
            mul(u[0],v[0]),
            mul(u[0],v[1])^mul(u[1],v[0]),
            mul(u[0],v[2])^mul(u[2],v[0]),
            mul(u[0],v[3])^mul(u[3],v[0])^mul(u[1],v[2])^mul(u[2],v[1]),
        )
    X=(0,1,0,0)
    Y=(0,0,1,0)
    def eval_map(p,z):
        fx,fy=p
        fxy=alg_mul(fx,fy)
        return tuple((mul(z[0],int(j==0)) ^mul(z[1],fx[j]) ^mul(z[2],fy[j]) ^mul(z[3],fxy[j])) for j in range(4))
    def comp(p,h):return(eval_map(p,h[0]),eval_map(p,h[1]))
    identity=(X,Y)
    automorphisms=[]
    for a,b,c,d,u,v in product(range(q),repeat=6):
        if mul(a,d)^mul(b,c):
            automorphisms.append(((0,a,c,u),(0,b,d,v)))
    expected_group=q*q*(q*q-1)*(q*q-q)
    assert len(automorphisms)==expected_group
    involutions=[g for g in automorphisms if comp(g,g)==identity]
    assert len(involutions)==q**3+q**2-q
    commuting=sum(comp(g,h)==comp(h,g) for g in involutions for h in involutions)
    assert commuting==q**5+2*q**4-q**3-q**2
    print('q=%d: algebra_automorphisms=%d, involutions=%d, commuting_involution_pairs=%d: PASS'%(q,len(automorphisms),len(involutions),commuting))
if __name__=='__main__':
    for q in (2,4):test(q)
    print('ALL_EXTERIOR_AUTOMORPHISM_CHECKS_PASS')
