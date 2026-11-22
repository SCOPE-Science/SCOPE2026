"""Exact symbolic checks for the sixth-period classification of farthest orthogonal projections.
Requires Python 3 and SymPy. This is a finite symbolic identity checker, not a numerical proof of parameter inequalities.
"""
import itertools
import sympy as s
q = s.symbols('q', positive=True)
A = [(s.Integer(-1), s.Integer(0)), (s.Integer(-1), s.Integer(0)), (s.Integer(1), s.Integer(0))]
v = [(s.Integer(2),s.Integer(0)),(s.Integer(1),s.sqrt(q)),(s.Integer(-1),s.sqrt(q))]
def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def determinant(a,b): return a[0]*b[1]-a[1]*b[0]
def simp(x): return s.factor(s.cancel(x))
P={}
for i in range(3):
 for j in range(3):
  if i == j: continue
  P[i,j]=(simp(dot(v[i],v[j])/dot(v[j],v[j])),simp(dot((A[i][0]-A[j][0], A[i][1]-A[j][1]),v[j])/dot(v[j],v[j])))
def d2(i,j,t):
 point=(A[i][0]+v[i][0]*t,A[i][1]+v[i][1]*t)
 r=(point[0]-A[j][0],point[1]-A[j][1])
 return simp(determinant(v[j],r)**2/dot(v[j],v[j]))
def compute(word):
 B,C=s.Integer(1),s.Integer(0)
 pre=[]
 for z in range(6):
  pre.append((B,C))
  b,c=P[word[z],word[(z+1)%6]]
  B,C=simp(b*B),simp(b*C+c)
 t0=simp(C/(1-B))
 t=[simp(b*t0+c) for b,c in pre]
 gap=[]
 for z,i in enumerate(word):
  j=word[(z+1)%6]; k=3-i-j
  gap.append(simp(d2(i,j,t[z])-d2(i,k,t[z])))
 return t,gap,B
words=[]
for word in itertools.product(range(3),repeat=6):
 if any(word[i]==word[(i+1)%6] for i in range(6)):continue
 if any(word==word[j:]+word[:j] for j in range(1,6)):continue
 if word!=min(word[j:]+word[:j] for j in range(6)):continue
 words.append(word)
assert len(words)==9
representatives=[(0,1,0,1,0,2),(0,1,0,1,2,1),(0,1,0,2,1,2),(0,1,2,0,2,1),(0,1,2,1,2,1)]
assert len(representatives)==5
reflected=set()
for w in representatives:
 for z in [w,tuple({0:0,1:2,2:1}[i] for i in w)]:
  reflected.add(min(z[j:]+z[:j] for j in range(6)))
assert reflected==set(words)
D=q*q+q+2
w=representatives[3]
t,g,B=compute(w)
expected_t=[(q+1)/D,2/D,2*(q+1)/D,(q*q+1)/D,2/D,2*(q+1)/D]
assert all(simp(a-b)==0 for a,b in zip(t,expected_t))
expected_g=[4*q*q*(1-q)/((q+1)*D),4*q*(q**3+q*q-1)/D**2,4*q*(-q**4+3*q**3+2*q*q+3*q+1)/((q+1)*D*D)]
assert all(simp(g[j]-expected_g[j%3])==0 for j in range(6))
assert simp(B-(q-1)**2/(q+1)**4)==0
# The other four classes each contain a failed strict inequality, with a split at q=2 for one class.
g0=compute(representatives[0])[1]
assert simp(g0[2]+4*q*(q*q+q+1)/((q+1)*(q*q+3*q+3)))==0
g1=compute(representatives[1])[1]
assert simp(g1[0]+4*q*(q-1)**2*(q+2)/((q+1)*(q+3)*D))==0
g2=compute(representatives[2])[1]
P6=q**6+3*q**5+13*q**4+14*q**3+19*q*q-9*q-9
B3=q**3-q*q-q-3
assert simp(g2[1]+4*q*P6/((q+1)*(q+3)**2*D**2))==0
assert simp(g2[3]-4*q*(q*q+3*q+3)*B3/((q+3)**2*D**2))==0
g4=compute(representatives[4])[1]
Q4=q**4+4*q**3+14*q*q+4*q+9
assert simp(g4[0]+4*q*(q-1)**4/((q+1)*Q4))==0
# Exact-rational sample, including strict tie handling and six distinct points.
for value,expected in [(s.Rational(3,4),False),(s.Rational(4,5),True),(s.Rational(1,1),False),(s.Rational(5,4),False)]:
 positives=all(bool(s.factor(z.subs(q,value))>0) for z in g)
 assert positives==expected
assert bool((q**3+q*q-1).subs(q,s.Rational(3,4))<0)
assert bool((q**3+q*q-1).subs(q,s.Rational(4,5))>0)
print('PASS: 9 cyclic primitive words, 5 reflection classes, exact candidates, choice gaps, return multiplier, obstructions and rational tests')
print('Unique root q0 of q^3+q^2-1:',s.nroots(q**3+q*q-1,maxsteps=100))
