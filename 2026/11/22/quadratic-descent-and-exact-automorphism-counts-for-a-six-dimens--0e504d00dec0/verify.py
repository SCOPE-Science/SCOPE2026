"""Standalone finite-field checks of the associative family and its automorphisms.
Only standard-library Python is required. Scientific names and algebraic definitions
are contained in RESULT.md.
"""
from itertools import product

MODS={1:0b11,2:0b111,3:0b1011}

def field(m):
    q=1<<m; mod=MODS[m]
    def mul(a,b):
        z=0
        while b:
            if b&1: z^=a
            b >>=1; a <<=1
            if a&q: a ^=mod
        return z
    return q,mul

def addv(u,v): return tuple(a^b for a,b in zip(u,v))

def scale(c,u,mul):return tuple(mul(c,x) for x in u)

def axiom_mul(u,v,mul):
    # basis 1,a,b,c1,c2,w, radical multiplication
    x,y,s,t,z=u[1:]; X,Y,S,T,Z=v[1:]
    val=mul(x,X)^mul(y,Y)^mul(x,Y)^mul(x,S)^mul(s,X)^mul(y,T)^mul(t,Y)
    return (0,0,0,0,0,val)

def prod(u,v,mul,alpha,beta):
    # u* v = scalar product + radical cross + radical product
    c,d=u[0],v[0]
    p=[mul(c,d)]+[mul(c,v[i])^mul(d,u[i]) for i in range(1,6)]
    x,y,s,t,z=u[1:]; X,Y,S,T,Z=v[1:]
    p[5]^=mul(alpha,mul(x,X))^mul(beta,mul(y,Y))^mul(x,Y)^mul(x,S)^mul(s,X)^mul(y,T)^mul(t,Y)
    return tuple(p)

def det(a,b,c,d,mul):return mul(a,d)^mul(b,c)

def quadratic(x,y,a,b,mul):return mul(a,mul(x,x)) ^ mul(x,y) ^ mul(b,mul(y,y))

def gl_isos(m,alpha,beta,A,B):
    q,mul=field(m)
    good=[]
    for p,r,s,t in product(range(q),repeat=4):
        delta=det(p,r,s,t,mul)
        if not delta: continue
        if all(quadratic(mul(p,x)^mul(r,y),mul(s,x)^mul(t,y),A,B,mul)==mul(delta,quadratic(x,y,alpha,beta,mul)) for x,y in product(range(q),repeat=2)):
            good.append((p,r,s,t,delta))
    return good

def basis(k):return tuple(int(i==k) for i in range(6))

def automorphism_from(m,alpha,beta,A,B,L,H,Z,Sh):
    q,mul=field(m)
    p,r,s,t,d=L
    # source basis a,b -> target V plus H in dual and Z in w
    images=[basis(0), (0,p,s,H[0],H[1],Z[0]),(0,r,t,H[2],H[3],Z[1])]
    # (v1,v2) pairing target C, φ(c1) maps to dual of column e1
    # matrix of pairings on v is [[p,s],[r,t]];
    # inverse * delta = [[t,s],[r,p]] in char2
    images += [(0,0,0,t,r,Sh[0]),(0,0,0,s,p,Sh[1]),(0,0,0,0,0,d)]
    return images

def map_vector(v,images,mul):
    w=(0,)*6
    for c,im in zip(v,images):w=addv(w,scale(c,im,mul))
    return w

def validate_images(m,alpha,beta,A,B,images):
    q,mul=field(m)
    src=[basis(i) for i in range(6)]
    for u in src:
        for v in src:
            if map_vector(prod(u,v,mul,alpha,beta),images,mul)!=prod(map_vector(u,images,mul),map_vector(v,images,mul),mul,A,B):return False
    return True

def run():
    # two forms: split Q=xy, nonsplit Q=x^2+xy+y^2 over F_2, parameter 1 extended
    for m in (1,2,3):
        q,mul=field(m)
        for alpha,beta in ((0,0),(1,1)):
            zeros=sum(quadratic(x,y,alpha,beta,mul)==0 for x,y in product(range(q),repeat=2))
            expected=2*q-1 if alpha==0 or m%2==0 else 1
            assert zeros==expected,(m,alpha,beta,zeros,expected)
            good=gl_isos(m,alpha,beta,alpha,beta)
            target=2*(q-1)**2 if zeros==2*q-1 else 2*(q*q-1)
            assert len(good)==target,(m,alpha,len(good),target)
            print('FIELD_CHECK',q,alpha,beta,'zeros',zeros,'similitudes',len(good))
        between=gl_isos(m,0,0,1,1)
        assert bool(between)==(m%2==0)
        print('BASE_CHANGE',q,'isomorphic',bool(between))
    # Direct algebraic checks: associativity, center and central essentiality for q=2,4
    for m in (1,2):
        q,mul=field(m)
        for alpha,beta in ((0,0),(1,1)):
            all_el=[(0,x,y,z,v,w) for x,y,z,v,w in product(range(q),repeat=5)] if q==2 else None
            if all_el is not None:
                for x in all_el:
                    for y in all_el:
                        for z in all_el:
                            assert prod(prod(x,y,mul,alpha,beta),z,mul,alpha,beta)==prod(x,prod(y,z,mul,alpha,beta),mul,alpha,beta)
                noncen=[x for x in all_el if x[1] or x[2]]
                for x in noncen:
                    assert any(prod(x,basis(i),mul,alpha,beta)[5] for i in (3,4))
            for L in gl_isos(m,alpha,beta,alpha,beta):
                p,r,s,t,d=L
                # For H, product(a,b) correction constraint ensures one linear equation:
                # target ab coefficient = d (alpha*0+1 etc)
                # a' b' product before H correction: B(L e1,L e2)
                B12=mul(alpha,mul(p,r))^mul(beta,mul(s,t))^mul(p,t)
                good_H=[]
                for h11,h12,h21,h22 in product(range(q),repeat=4):
                    c12=mul(p,h21)^mul(s,h22)^mul(r,h11)^mul(t,h12)
                    if B12^c12==d:good_H.append((h11,h12,h21,h22))
                assert len(good_H)==q**3
                if m==2:
                    for H in (good_H[0],good_H[-1]):
                        for Z,Sh in [((0,0),(0,0)),((1,1),(1,1))]:
                            im=automorphism_from(m,alpha,beta,alpha,beta,L,H,Z,Sh)
                            assert validate_images(m,alpha,beta,alpha,beta,im)
                if m==1:
                    for H in good_H:
                        for Z in product(range(q),repeat=2):
                            for Sh in product(range(q),repeat=2):
                                im=automorphism_from(m,alpha,beta,alpha,beta,L,H,Z,Sh)
                                assert validate_images(m,alpha,beta,alpha,beta,im)
            print('AUT_CHECK',q,alpha,beta,'count',q**7*len(gl_isos(m,alpha,beta,alpha,beta)))
    # Explicit F4 (α,β)=(0,0) to (1,1) check. t=2 satisfies t²+t+1=0, t²=3.
    m=2;q,mul=field(m);omega=2;omega2=mul(omega,omega)
    # φ(a)=ω A+B, φ(b)=ω² A+B+ω² C2,
    # φ(c1)=C1+ω² C2, φ(c2)=C1+ω C2, φ(w)=W
    images=[basis(0),(0,omega,1,0,0,0),(0,omega2,1,0,omega2,0),
            (0,0,0,1,omega2,0),(0,0,0,1,omega,0),basis(5)]
    assert validate_images(m,0,0,1,1,images)
    print('EXPLICIT_F4_ISOMORPHISM_OK')
    # Entire sixteen-member parameter family over F4, including nonsplit cases.
    m=2;q,mul=field(m)
    split_count=0; nonsplit_count=0
    for alpha,beta in product(range(q), repeat=2):
        zeros=sum(quadratic(x,y,alpha,beta,mul)==0 for x,y in product(range(q),repeat=2))
        split=(zeros==2*q-1)
        assert zeros in (1,2*q-1)
        if split:split_count+=1
        else:nonsplit_count+=1
        target=2*(q-1)**2 if split else 2*(q*q-1)
        assert len(gl_isos(m,alpha,beta,alpha,beta))==target
        assert bool(gl_isos(m,0,0,alpha,beta))==split
    assert (split_count,nonsplit_count)==(q*(q+1)//2,q*(q-1)//2)
    print('F4_PARAMETER_CENSUS',split_count,nonsplit_count)
    print('VERIFY_OK')
if __name__=='__main__':run()
