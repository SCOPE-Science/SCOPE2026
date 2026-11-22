import itertools, sympy as s, collections

def run(p):
 # GF(p^2)=F_p[t]/(t^2-tc), char 2 t^2=t+1, char3 t^2=-1
 vals=list(range(p*p));
 def tup(a):return a%p,(a//p)%p
 def ff(a,b):return (a%p)+p*(b%p)
 def add(a,b):
  (u,v),(x,y)=tup(a),tup(b);return ff(u+x,v+y)
 def neg(a):return ff(-tup(a)[0],-tup(a)[1])
 def mul(a,b):
  u,v=tup(a);x,y=tup(b)
  if p==2:return ff(u*x+v*y, u*y+v*x+v*y)
  return ff(u*x-v*y,u*y+v*x)
 def powf(a,n):
  r=1
  for k in range(n):r=mul(r,a)
  return r
 def inv(a):
  assert a!=0
  return powf(a,p*p-2)
 def conj(a):return powf(a,p)
 def scale(a,b):return mul(a,b)
 def matmul(A,B):return [[add(mul(A[i][0],B[0][j]),mul(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]
 def dagger(A):return [[conj(A[j][i]) for j in range(2)] for i in range(2)]
 def coords(H):
  # original H [[x,z+tw],[z+bar(t) w, -y]], t=p
  x,y0=H[0][0],H[1][1]
  assert tup(x)[1]==0 and tup(y0)[1]==0
  u=H[0][1];z,w=tup(u)
  assert H[1][0]==conj(u)
  return (x%p,-y0%p,z,w)
 def herm(x,y,z,w):
  u=ff(z,w);return [[x,u],[conj(u),(-y)%p]]
 def transform(M):
  MD=dagger(M)
  cols=[coords(matmul(matmul(M,herm(*basis)),MD)) for basis in [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]]
  return [[cols[j][i] for j in range(4)] for i in range(4)]
 def vpoly(poly):
  P=s.Poly(poly,x,y,z,w)
  return [int(P.coeff_monomial(mon))%p for mon in monlist]
 x,y,z,w=s.symbols('x y z w'); coords_sym=[x,y,z,w]
 if p==2:
  q=x*y+z*z+z*w+w*w
  f=x**3+y**3+z**3+y*y*w+x*z*w
 else:
  q=x*y+z*z+w*w
  f=x**3+y**3+y*y*z+x*x*w+x*y*w-y*y*w-y*z*w+z*z*w
 monlist=[x**a*y**b*z**c*w**(3-a-b-c) for a in range(4) for b in range(4-a) for c in range(4-a-b)]
 span=[vpoly(f)]+[vpoly(q*v) for v in coords_sym]
 # record all vectors in span for q2 q3 2*3^4=162 vectors
 expected={tuple(sum(c*v[i] for c,v in zip(coeffs,span))%p for i in range(len(monlist))):coeffs for coeffs in itertools.product(range(p), repeat=5) if coeffs[0]!=0}
 print('p',p,'size in span',len(expected))
 stabs=[];hist=collections.Counter(); total=0
 for aa,bb,cc,dd in itertools.product(vals,repeat=4):
  ffour=[aa,bb,cc,dd]
  if not any(ffour):continue
  j=next(i for i,a in enumerate(ffour) if a)
  if ffour[j]!=1:continue
  det=add(mul(aa,dd),neg(mul(bb,cc)))
  if not det:continue
  M=[[aa,bb],[cc,dd]]
  T=transform(M)
  for v in range(2):
   if v:
    # Frobenius conjugation of coordinates: t->conj t, in y z w basis z,w -> z',w'
    # p2: conj(z+t w)=z+(t+1)w -> (z+w)+tw; p3: conj(z+t w)=z-tw -> z-tw
    if p==2:cf=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,1,1)]
    else:cf=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,2)]
    T0=T
    T=[[sum(T0[i][k]*cf[j][k] for k in range(4))%p for j in range(4)] for i in range(4)]
   total+=1
   fs=[sum(T[i][j]*coords_sym[j] for j in range(4)) for i in range(4)]
   ev=vpoly(f.subs(dict(zip(coords_sym,fs)), simultaneous=True))
   hit=expected.get(tuple(ev))
   if hit:
    stabs.append((M,v,T,hit))
    hist[tuple(hit)]+=1
 assert total==({2:120,3:1440}[p]),(p,total)
 assert len(stabs)==5,(p,len(stabs))
 print('CHARACTERISTIC',p,'TOTAL_QUADRIC_AUTOMORPHISMS',total,'CURVE_AUTOMORPHISMS',len(stabs))
 return stabs

# Independent model-level smoothness computation and group generator checks.
def check_model(p):
    import itertools
    x,y,z,w=s.symbols("x y z w")
    v=[x,y,z,w]
    if p==2:
        Q=x*y+z*z+z*w+w*w
        F=x**3+y**3+z**3+y*y*w+x*z*w
        T=s.Matrix([[0,1,0,0],[1,1,1,1],[0,1,1,0],[0,0,1,1]])
        L=x+y
    else:
        Q=x*y+z*z+w*w
        F=x**3+y**3+y*y*z+x*x*w+x*y*w-y*y*w-y*z*w+z*z*w
        T=s.Matrix([[1,2,2,0],[1,1,1,1],[2,0,2,0],[1,2,2,1]])
        L=x+y+z
    linear_sub=dict(zip(v,T*s.Matrix(v)))
    def iszero(P):
        return s.Poly(s.expand(P),*v,modulus=p).is_zero
    assert iszero(Q.subs(linear_sub, simultaneous=True)-Q)
    assert iszero(F.subs(linear_sub, simultaneous=True)-F-Q*L)
    assert s.Poly(T.charpoly().as_expr(),modulus=p).all_coeffs()==[1,1,1,1,1]
    assert all((int((T**5)[i,j])-(i==j))%p==0 for i in range(4) for j in range(4))
    # Smooth geometric curve iff unit belongs to Jacobian-minor ideal
    minors=[s.diff(Q,a)*s.diff(F,b)-s.diff(Q,b)*s.diff(F,a) for a,b in itertools.combinations(v,2)]
    for k in range(4):
        variables=v[:k]+v[k+1:]
        gb=s.groebner([f.subs(v[k],1) for f in [Q,F]+minors],*variables,modulus=p)
        assert gb.contains(s.Integer(1)),('nonsmooth',p,k)
    # No rational projective points on C.
    for u in itertools.product(range(p),repeat=4):
        if not any(u) or next(a for a in u if a)!=1:continue
        d=dict(zip(v,u))
        assert not (int(Q.subs(d))%p==0 and int(F.subs(d))%p==0)
    # Φ_5 irreducible for p=2,3: multiplicative order of p modulo 5 is 4.
    assert len({p**j%5 for j in range(1,5)})==4
    print('SMOOTH_MODEL_AND_CYCLIC_QUINTIC_GENERATOR',p,'PASS')

if __name__=='__main__':
    for prime in (2,3):
        ss=run(prime)
        assert len(ss)==5
        check_model(prime)
    print('EXCESSIVE_GENUS_FOUR_AUTOMORPHISMS_VERIFIED')
