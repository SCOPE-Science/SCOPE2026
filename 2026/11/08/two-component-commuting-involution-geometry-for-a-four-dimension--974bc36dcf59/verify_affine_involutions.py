"""Independent finite-field enumeration for commuting involutions in AGL(2)."""
from itertools import product

def field(q):
    poly={2:0b11,4:0b111,8:0b1011}[q]
    degree=q.bit_length()-1
    def mul(a,b):
        out=0
        while b:
            if b&1:out^=a
            b>>=1
            a<<=1
            if a&q:a^=poly
        return out
    return mul

def check(q):
    mul=field(q)
    add=lambda a,b:a^b
    ident=(1,0,0,1)
    zero=(0,0,0,0)
    def mm(A,B):
        return (mul(A[0],B[0])^mul(A[1],B[2]),
                mul(A[0],B[1])^mul(A[1],B[3]),
                mul(A[2],B[0])^mul(A[3],B[2]),
                mul(A[2],B[1])^mul(A[3],B[3]))
    def mv(A,b):return (mul(A[0],b[0])^mul(A[1],b[1]),mul(A[2],b[0])^mul(A[3],b[1]))
    def prod(g,h):
        A,a=g;B,b=h
        t=mv(A,b)
        return (mm(A,B),(a[0]^t[0],a[1]^t[1]))
    invol=[]
    for A in product(range(q),repeat=4):
        if mul(A[0],A[3])^mul(A[1],A[2])==0:continue
        if mm(A,A)!=ident:continue
        for a in product(range(q),repeat=2):
            if prod((A,a),(A,a))==(ident,(0,0)):
                invol.append((A,a))
    all_pairs=0
    tcomponent=0
    ecomponent=0
    intersection=0
    for g in invol:
        for h in invol:
            if prod(g,h)!=prod(h,g):continue
            all_pairs+=1
            is_t=(g[0]==ident and h[0]==ident)
            a=g[1];b=h[1]
            collinear=(mul(a[0],b[1])^mul(a[1],b[0])==0)
            is_e=(not is_t) or collinear
            if is_t:tcomponent+=1
            if is_e:ecomponent+=1
            if is_t and is_e:intersection+=1
    expect=(q**5+2*q**4-q**3-q**2,q**4,q**5+q**4-q, q**3+q**2-q)
    obtained=(all_pairs,tcomponent,ecomponent,intersection)
    assert obtained==expect,(q,obtained,expect)
    assert len(invol)==q**3+q**2-q,(q,len(invol))
    print(f'q={q}: involutions={len(invol)}, pairs={all_pairs}, translation_component={tcomponent}, scroll_component={ecomponent}, intersection={intersection}: PASS')

if __name__=='__main__':
    for q in (2,4,8):check(q)
    print('ALL_AFFINE_COMMUTING_INVOLUTION_CHECKS_PASS')
