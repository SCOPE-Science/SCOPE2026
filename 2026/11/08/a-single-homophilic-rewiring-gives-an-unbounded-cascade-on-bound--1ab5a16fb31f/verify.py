from fractions import Fraction

def edges(m):
 V=('a','b','u','v','x','y')+tuple(f'w{i}' for i in range(1,m+1))
 E={frozenset(e) for e in [('a','u'),('b','u'),('b','v'),('v','x'),('v','y'),('v','w1')]+[(f'w{i}',f'w{i+1}') for i in range(1,m)]}
 assert len(E)==len(V)-1
 return V,E

def closure(V,E,threshold):
 A={'a','b'}
 while True:
  R=set(A)
  for v in V:
   if v not in A:
    n={next(iter(e-{v})) for e in E if v in e}
    if n and Fraction(len(n&A),len(n))>threshold:R.add(v)
  if R==A: return A
  A=R

def test(m, theta):
 V,E=edges(m); N=len(V); S={'a','b'}
 assert len(closure(V,E,theta))==3
 active=[e for e in E if len(e&S)==1]
 assert len(active)==3
 results=[]
 for e in active:
  v=next(iter(e-S))
  targets=[w for w in V if w not in S and w!=v and frozenset({v,w}) not in E]
  assert targets
  for w in targets:
   F=E-{e}|{frozenset({v,w})}
   ans=closure(V,F,theta)
   assert len(ans) in (3,N), (m, theta,e,w,ans)
   assert (len(ans)==N)==(v=='u'),(m,theta,e,w,ans)
   results.append((e,v,w,len(ans),Fraction(1,3*len(targets))))
 p=sum(p for e,v,w,n,p in results if n==N)
 expected=sum(n*p for e,v,w,n,p in results)
 assert p==Fraction(2,3), (m,theta,p)
 assert expected==3+Fraction(2*(m+3),3),(m,theta,expected)
 return len(results),p,expected
if __name__=='__main__':
 for m in range(1,21):
  for theta in [Fraction(1,4),Fraction(3,10),Fraction(333,1000)]: test(m,theta)
 # Independent boundary controls: below 1/4, original diffusion is global;
 # at the upper boundary 1/3 a rewiring into an interior path vertex cannot ignite the path.
 for m in range(1,21):
  V,E=edges(m)
  assert len(closure(V,E,Fraction(1,5)))==len(V)
 for m in range(2,21):
  V,E=edges(m)
  assert len(closure(V,E,Fraction(1,3)))==3
  F=E-{frozenset({'a','u'})}|{frozenset({'u','w1'})}
  assert len(closure(V,F,Fraction(1,3)))==3
 print('PASS: 60 exact case families and 39 endpoint controls, n=7 to 26; every permissible one-shot rewiring')
 for m in [1,2,3,10,20]:print(m,test(m,Fraction(3,10)))
