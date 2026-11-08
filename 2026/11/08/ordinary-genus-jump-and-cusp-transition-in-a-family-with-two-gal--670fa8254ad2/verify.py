"""Exact characteristic-three point-count cross-check for a family of Galois-point curves.

This is finite numerical evidence, not a substitute for the genus and p-rank proof.
"""
# Fixed monic irreducible polynomials over F_3 (descending coefficients).
# The finite-field verifier checks inversion for every nonzero field element.
FIELD_POLYNOMIALS={
1:[1,0], 2:[1,0,1], 3:[1,0,2,1], 4:[1,0,0,1,2],
5:[1,0,0,0,2,1], 6:[1,0,0,0,0,1,2],
7:[1,0,0,0,0,1,0,2], 8:[1,0,0,0,0,0,1,0,2]
}
def choose_poly(n): return FIELD_POLYNOMIALS[n]

class Field:
 def __init__(self,n):
    self.n=n; self.q=3**n;self.p=choose_poly(n)
    self.d=[tuple((x//(3**i))%3 for i in range(n)) for x in range(self.q)]
    self.e=[3**i for i in range(n)]
 def add(self,a,b):
    return sum(((x+y)%3)*w for x,y,w in zip(self.d[a], self.d[b], self.e))
 def neg(self,a):
    return sum(((-x)%3)*w for x,w in zip(self.d[a], self.e))
 def sub(self,a,b):return self.add(a,self.neg(b))
 def mul(self,a,b):
    if not a or not b: return 0
    n=self.n;z=[0]*(2*n-1)
    for i,x in enumerate(self.d[a]):
        if x:
            for j,y in enumerate(self.d[b]):
                z[i+j]+=x*y
    # polynomial p is descending monic: x^n + p[1]x^(n-1)+ ... + p[n]
    for k in range(2*n-2,n-1,-1):
        c=z[k]%3
        if c:
            for j in range(n):z[k-n+j]-=c*self.p[n-j]
    return sum((z[i]%3)*self.e[i] for i in range(n))
 def power(self,a,m):
    out=1
    while m:
        if m&1:out=self.mul(out,a)
        a=self.mul(a,a);m//=2
    return out

def count(n,c):
 f=Field(n);q=f.q
 # Validate basic field properties and inverses.
 assert f.power(2,2)==1
 cubes=[f.power(x,3) for x in range(q)]
 nx=[0]*q;ny=[0]*q
 for x in range(q):
    nx[f.sub(cubes[x],x)]+=1
    ny[f.sub(cubes[x],f.mul(c,x))]+=1
 inv2=2
 affine=0
 for t in range(1,q):
    inv=f.power(t,q-2)
    assert f.mul(t,inv)==1
    z=f.mul(inv2,f.sub(t,inv))
    u=f.mul(inv2,f.add(t,inv))
    affine+=nx[z]*ny[u]
 # Both infinity points have one geometric point in the c!=1 case;
 # in the c=1 case, the p branches at each are individually F_3-rational.
 infinity=6 if c==1 else 2
 return q+1-(affine+infinity), affine+infinity, f.p

def l_coefficients(p,c,g):
 s=[];a=[1]
 for n in range(1,g+1):
    s_n,N,poly=count(n,c)
    s.append(s_n)
    z=s_n+sum(a[i]*s[n-i-1] for i in range(1,n))
    assert z%n==0, ('non-integral L',p,c,n,z)
    a.append(-z//n)
    print(f'p={p} c={c} n={n} polynomial={poly} N={N} S={s_n} a_n={a[-1]}')
 assert a[g]%p !=0, ('p-rank lower than genus',c,g,a)
 print('ordinary-check leading coefficient a_g mod p:',a[g]%p)
 return a

def local_initial(p,c,sigma):
    # In the Y=1 chart at P=(sigma:1:0), write X=sigma+u, Z=w.
    # Compute the lowest total-degree form of the actual homogenized equation.
    def product(A,B):
        C={}
        for (i,j),a in A.items():
            for (k,l),b in B.items():
                C[i+k,j+l]=(C.get((i+k,j+l),0)+a*b)%p
        return {k:v for k,v in C.items() if v%p}
    A={(0,0):sigma,(p,0):1,(0,p-1):-sigma,(1,p-1):-1}
    B={(0,0):1,(0,p-1):-c}
    aa=product(A,A);bb=product(B,B)
    C={k:(aa.get(k,0)-bb.get(k,0))%p for k in aa.keys()|bb.keys()}
    C[(0,2*p)]=(C.get((0,2*p),0)+1)%p
    C={k:v for k,v in C.items() if v}
    d=min(sum(k) for k in C)
    initial={k:v for k,v in C.items() if sum(k)==d}
    if c==1:
        assert d==p and (p,0) in initial and (1,p-1) in initial
        assert len(initial)==2
    else:
        assert d==p-1 and list(initial)==[(0,p-1)]
    return d,initial

if __name__=='__main__':
 for c,g in ((1,4),(2,8)):
    a=l_coefficients(3,c,g)
    print('case',c,'genus',g,'L-first-half',a)
 for p in (3,5,7):
    for c in (1,2):
        for sigma in (1,p-1):
            d,ini=local_initial(p,c,sigma)
            print('local p/c/sigma',p,c,sigma,'multiplicity',d,'tangent',ini)
 print('POINT_COUNT_AND_LOCAL_CHECKS_PASSED')
