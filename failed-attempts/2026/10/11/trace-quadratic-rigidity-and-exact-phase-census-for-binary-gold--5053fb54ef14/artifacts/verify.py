"""Exact finite-characteristic-two Gold-graph convolution and phase-code checks.
Public reproducibility script; Python 3 standard library only.
"""
import math
from itertools import product

POLYS = {2: 0b111, 3: 0b1011, 4: 0b10011, 5: 0b100101, 6: 0b1000011, 8: 0x11b}


def mul(a,b,m):
    p=POLYS[m]; q=1<<m; ans=0
    while b:
        if b&1:ans ^=a
        b >>= 1; a<<=1
        if a&q:a ^=p
    return ans


def power(a,n,m):
    ans=1
    while n:
        if n&1:ans=mul(ans,a,m)
        a=mul(a,a,m); n//=2
    return ans


def tr(a,m):
    r=0
    for _ in range(m):
        r ^= a; a=mul(a,a,m)
    assert r in (0,1)
    return r


def gold(t,k,m):return mul(t,power(t,1<<k,m),m)


def fiber_map(m,k):
    q=1<<m; out={}
    for t,u in product(range(q),repeat=2):
        s=t^u; y=gold(t,k,m)^gold(u,k,m)
        out.setdefault((s,y),[]).append(t)
    return out


def fourth(f,m,k):
    fibers=fiber_map(m,k)
    return sum(abs(sum(f[t]*f[t^s] for t in ts))**2 for (s,_),ts in fibers.items())


def deficit_terms(f,m,k):
    q=1<<m; d=math.gcd(m,k); h=1<<d
    M=sum(abs(z)**2 for z in f)
    H=sum(abs(z)**4 for z in f)
    diagonal=M*M-abs(sum(z*z for z in f))**2
    amplitude=h*(H-M*M/q)
    fibers=fiber_map(m,k)
    fiberloss=sum(sum(abs(f[t]*f[t^s]-f[u]*f[u^s])**2
                      for i,t in enumerate(ts) for u in ts[i+1:])
                  for (s,_),ts in fibers.items() if s)
    return diagonal,amplitude,fiberloss


def line_phase_dimension(m,d):
    q=1<<m; h=1<<d; sf=[a for a in range(q) if power(a,h,m)==a]
    assert len(sf)==h
    piv={}
    for s in range(1,q):
        for a in sf:
            if a in (0,1):continue
            v=mul(a,s,m)
            for t in range(q):
                row=(1<<t)^(1<<(t^s))^(1<<(t^v))^(1<<(t^s^v))
                while row:
                    pivot=row.bit_length()-1
                    if pivot in piv:row ^=piv[pivot]
                    else:
                        piv[pivot]=row;break
    return q-len(piv)



def k_coords(m,d):
    """An explicit K-basis of F, with exact coefficient lookup."""
    q=1<<m; h=1<<d
    elems=[x for x in range(q) if power(x,h,m)==x]
    assert len(elems)==h
    basis=[]
    vectors={0:()}
    while len(basis)<m//d:
        candidate=next(x for x in range(1,q) if x not in vectors)
        nextvec={}
        for prev,co in vectors.items():
            for a in elems:
                y=prev^mul(a,candidate,m)
                assert y not in nextvec
                nextvec[y]=co+(a,)
        basis.append(candidate)
        vectors=nextvec
    assert len(vectors)==q
    return basis,vectors


def rank_bitrows(rows):
    piv={}
    for row in rows:
        while row:
            k=row.bit_length()-1
            if k in piv:row ^=piv[k]
            else:piv[k]=row;break
    return len(piv)


def tracek(a,m,d):
    out=0
    for _ in range(d):
        out ^=a
        a=mul(a,a,m)
    assert out in (0,1)
    return out


def quad_code_dimension(m,d):
    q=1<<m; r=m//d
    basis, coords=k_coords(m,d)
    coefficient_basis=[]
    # Multiplication-by-subfield scalars on a basis coordinate gives d independent trace characters.
    ker=[x for x in range(q) if power(x,1<<d,m)==x]
    take=[];span={0}
    for x in ker:
        if x not in span:
            take.append(x)
            span={v^mul(c,x,m) for v in span for c in (0,1)}
    assert len(take)==d
    for i in range(r):
        for c in take:
            coefficient_basis.append((i,i,c))
    for i in range(r):
        for j in range(i+1,r):
            for c in take:
                coefficient_basis.append((i,j,c))
    codewords=[]
    for i,j,c in coefficient_basis:
        row=0
        for t in range(q):
            y=coords[t]
            if tracek(mul(c,mul(y[i],y[j],m),m),m,d):row |= 1<<t
        codewords.append(row)
    assert rank_bitrows(codewords)==len(coefficient_basis)
    # Each codeword has vanishing affine-line second differences in independent parameters.
    sf=ker
    for row in codewords:
        for s in range(1,q):
            for alpha in sf:
                if alpha in (0,1):continue
                shift=mul(s,alpha,m)
                for t in range(q):
                    assert (((row>>t)^(row>>(t^s))^(row>>(t^shift))^(row>>(t^s^shift)))&1)==0
    return len(coefficient_basis)

def run():
    checks=0
    for m,k in [(2,1),(3,1),(4,1),(4,2),(5,1),(6,2),(6,3)]:
        q=1<<m; d=math.gcd(m,k); h=1<<d; fibers=fiber_map(m,k)
        assert len(fibers[(0,0)])==q
        assert all(len(ts)==h for (s,y),ts in fibers.items() if s)
        for j in range(11):
            f=[complex(((13*t+7*j)%5)-2,((7*t*t+11*j)%5)-2) for t in range(q)]
            M=sum(abs(z)**2 for z in f)
            D=deficit_terms(f,m,k)
            F=fourth(f,m,k)
            assert abs(((h+1)-h/q)*M*M-F-sum(D))<1.e-7, (m,k,j,D,F)
            checks+=1
        for j in range(5):
            f=[(-1)**((j*t*t+3*t+j*j)&1) for t in range(q)]
            D=deficit_terms(f,m,k)
            assert abs((h+1-h/q)*q*q-fourth(f,m,k)-sum(D))<1.e-7
            checks+=1
        if d==1:
            for j in range(5):
                f=[(-1)**(((t*t+3*j*t+5*j*j)&7).bit_count()&1) for t in range(q)]
                assert fourth(f,m,k)==(h+1-h/q)*q*q
                assert sum(deficit_terms(f,m,k))==0
        dimension=line_phase_dimension(m,d)
        expected=1+d*((m//d)*(m//d+1)//2)
        if d>1:
            assert dimension==expected, (m,d,dimension,expected)
            assert quad_code_dimension(m,d)==expected-1
        else:
            assert dimension==q
        print('CASE',m,k,'q',q,'h',h,'phase_dimension',dimension,'expected',expected if d>1 else q)
    for m,d in [(8,2),(8,4)]:
        dimension=line_phase_dimension(m,d)
        expected=1+d*((m//d)*(m//d+1)//2)
        assert dimension==expected, (m,d,dimension,expected)
        assert quad_code_dimension(m,d)==expected-1
        print('PHASE_ONLY',m,d,'dimension',dimension,'expected',expected)
    # Direct Fourier orthogonality, without relying on the pair-sum identity.
    for m,k in [(2,1),(3,1),(4,2)]:
        q=1<<m
        for j in range(3):
            f=[complex((t*3+j)%3-1,(t*5+2*j)%3-1) for t in range(q)]
            lhs=0
            for u,v in product(range(q),repeat=2):
                val=sum(f[t]*(-1 if tr(mul(u,t,m)^mul(v,gold(t,k,m),m),m) else 1)
                        for t in range(q))
                lhs+=abs(val)**4
            lhs/=q*q
            assert abs(lhs-fourth(f,m,k))<1e-7
    print('VERIFY_OK','parameter_families=7','complex_fiber_deficit_checks='+str(checks),
          'direct_Walsh_cases=9','all_tests=PASS')

if __name__=='__main__':run()
