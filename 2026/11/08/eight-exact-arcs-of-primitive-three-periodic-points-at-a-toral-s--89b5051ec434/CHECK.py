import sympy as s,itertools
eta=s.Rational(1,3); lam=1-eta
L=s.Matrix([[1,s.Rational(3,2)],[1,s.Rational(5,2)]]); R=s.Matrix([[1,-3],[1,-2]])
t=s.symbols('t',real=True)
lines={}
for br in itertools.product('LR',repeat=3):
 for wraps in itertools.product(range(4),repeat=3):
  A=s.eye(2);b=s.zeros(2,1)
  for branch,w in zip(br,wraps):
   B=L if branch=='L' else R;c=0 if branch=='L' else 3
   v=s.Matrix([c-(w%2),c-(w%2)-(w//2)]); A,b=B*A,B*b+v
  C=s.eye(2)-A
  if C.det()!=0:continue
  xx,yy=s.symbols('xx yy');sol=s.linsolve((C,b),(xx,yy))
  if sol==s.EmptySet:continue
  x,y=list(sol)[0]
  syms=x.free_symbols|y.free_symbols
  if len(syms)!=1:continue
  free=next(iter(syms)); x=x.subs(free,t);y=y.subs(free,t)
  X=x;Y=y;lo=-s.oo;hi=s.oo
  def bounded(z,a,b):
   global lo,hi
   z=s.expand(z)
   if t not in z.free_symbols:
    return a<=z<=b
   slope=z.coeff(t);off=z.subs(t,0)
   lo1=(a-off)/slope;hi1=(b-off)/slope
   if slope<0:lo1,hi1=hi1,lo1
   lo=max(lo,lo1);hi=min(hi,hi1)
   return hi>=lo
  ok=True
  for branch,w in zip(br,wraps):
   for z,a,bnd in [(X,0,1),(Y,0,1),(Y,0,lam if branch=='L' else 1),(Y,lam if branch=='R' else 0,1)]:
    if not bounded(z,a,bnd):ok=False;break
   if not ok:break
   f=Y* s.Rational(3,2) if branch=='L' else 3*(1-Y)
   nxtx=s.expand(X+f-(w%2));nxty=s.expand(Y+nxtx-(w//2));X,Y=nxtx,nxty
  if ok and lo<hi:
   p=s.Matrix([x.subs(t,lo),y.subs(t,lo)]);q=s.Matrix([x.subs(t,hi),y.subs(t,hi)])
   v1=tuple(p);v2=tuple(q);key=tuple(sorted([v1,v2]));lines.setdefault(key,[]).append((''.join(br),wraps))
for (p,q), labels in sorted(lines.items()):print(p,'->',q, 'branches',labels)
print('total UNIQUE SEGMENTS:',len(lines))

# Collapse adjacent itinerary cells with the same slope into eight geometric arcs.
expected = {
 ((s.Rational(0),s.Rational(7,9)), (s.Rational(2,9),s.Rational(8,9))),
 ((s.Rational(0),s.Rational(8,9)), (s.Rational(2,9),s.Rational(1))),
 ((s.Rational(7,9),s.Rational(2,3)), (s.Rational(1),s.Rational(7,9))),
 ((s.Rational(7,9),s.Rational(7,9)), (s.Rational(1),s.Rational(8,9))),
 ((s.Rational(2,9),s.Rational(2,9)), (s.Rational(4,9),s.Rational(2,9))),
 ((s.Rational(5,9),s.Rational(4,9)), (s.Rational(7,9),s.Rational(4,9))),
 ((s.Rational(2,9),s.Rational(2,3)), (s.Rational(4,9),s.Rational(8,9))),
 ((s.Rational(5,9),s.Rational(7,9)), (s.Rational(7,9),s.Rational(1))),
}
assert len(lines) == 12
all_verified = set()
for (p,q) in lines:
 for P,Q in expected:
  a,b=s.Matrix(P),s.Matrix(Q);v=b-a
  if s.det(s.Matrix.hstack(s.Matrix(p)-a,v))==0 and s.det(s.Matrix.hstack(s.Matrix(q)-a,v))==0:
   if all(0 <= (s.Matrix(w)-a).dot(v) <= v.dot(v) for w in (p,q)):
    all_verified.add((P,Q))
    break
 else:raise AssertionError(('unexpected nondegenerate cell',p,q))
assert all_verified==expected
for P,Q in expected:
 for i in range(1,60):
  V=s.Matrix(P)*(1-s.Rational(i,60))+s.Matrix(Q)*s.Rational(i,60)
  x,y=map(s.Rational,V)
  original=(x%1,y%1)
  for _ in range(3):
   f=s.Rational(3,2)*y if y<=s.Rational(2,3) else 3*(1-y)
   x=(x+f)%1;y=(y+x)%1
  assert (x,y)==original,(P,Q,i,(x,y),original)
print('PERIOD_THREE_RESONANT_EIGHT_ARCS_OK; cells=12; arcs=8; exact_points=472')
# Independent exact symbolic check of the parameter-uniform determinant factors.
h=s.symbols('h')
Ld=s.Matrix([[1,1/(1-h)],[1,1+1/(1-h)]])
Rd=s.Matrix([[1,-1/h],[1,1-1/h]])
expected_dets=[(3*h-4)**2/(h-1)**3,(3*h-4)*(3*h-2)/(h*(h-1)**2),3*(3*h-1)/h**2,(3*h-1)**2/h**3]
for num_r in range(4):
 for word in set(itertools.permutations('L'*(3-num_r)+'R'*num_r)):
  A=s.eye(2)
  for letter in word:A=(Ld if letter=='L' else Rd)*A
  assert s.factor((s.eye(2)-A).det()-expected_dets[num_r])==0,(word,A)
print('PARAMETER_UNIFORM_DETERMINANTS_OK')
# Check that the twelve enumerated cells cover each stated arc without gaps.
for P,Q in expected:
 a,b=s.Matrix(P),s.Matrix(Q);v=b-a;vv=v.dot(v)
 pieces=[]
 for (u,w) in lines:
  U,W=s.Matrix(u),s.Matrix(w)
  if s.det(s.Matrix.hstack(U-a,v)) or s.det(s.Matrix.hstack(W-a,v)):continue
  j=(U-a).dot(v)/vv;k=(W-a).dot(v)/vv
  if 0<=j<=1 and 0<=k<=1:pieces.append((min(j,k),max(j,k)))
 pieces.sort();assert pieces and pieces[0][0]==0 and pieces[-1][1]==1,(P,Q,pieces)
 for left,right in zip(pieces,pieces[1:]):assert left[1]==right[0],(P,Q,pieces)
# Exact all-R translation obstruction, with the four possible wrap pairs.
for ws in itertools.product(range(4),repeat=3):
 R0=s.Matrix([[1,-3],[1,-2]]);A=s.eye(2);translation=s.zeros(2,1)
 for w in ws:
  z=s.Matrix([3-w%2,3-w%2-w//2]);A,translation=R0*A,R0*translation+z
 assert A==s.eye(2)
 assert (translation==s.zeros(2,1))==(len(set(ws))==1),ws
print('AFFINE_CELL_COVERAGE_AND_ALL_RIGHT_OBSTRUCTION_OK')
