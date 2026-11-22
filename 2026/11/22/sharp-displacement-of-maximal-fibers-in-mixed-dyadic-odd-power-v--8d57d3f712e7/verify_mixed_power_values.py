"""Independent finite checks for asymmetric odd-power value-set convolutions."""
from collections import Counter

def fibers(d,e,k):
 n=1<<k
 if k==0:return [1]
 A=range(0,k,d); B=range(0,k,e)
 common=set(A)&set(B)
 L=lambda v:1<<(k-v-1)
 result=[]
 for t in range(n):
  if t==0:
   result.append(1+sum(L(v) for v in common));continue
  v=(t&-t).bit_length()-1
  z=sum(L(s) for s in common if s<v)
  if v in A:z+=1+sum(L(s) for s in B if s>v)
  if v in B:z+=1+sum(L(s) for s in A if s>v)
  result.append(z)
 return result

def check():
 nchecks=0
 for d,e in ((3,5),(3,7),(3,9),(3,11),(5,7),(5,9),(7,9)):
  for k in range(0,11):
   n=1<<k
   A={pow(x,d,n) for x in range(n)}
   B={pow(x,e,n) for x in range(n)}
   expected=fibers(d,e,k)
   actual=Counter((a+b)%n for a in A for b in B)
   for t in range(n):
    assert actual[t]==expected[t],(d,e,k,t)
    nchecks+=1
   assert max(expected)==len(B)
   assert sum(expected)==len(A)*len(B)
   if k>d:
    assert expected[1<<d]==len(B)
   if k>=3:
    assert [t for t in range(n) if expected[t]==min(expected)]==list(range(1,n,2))
   nchecks+=4
 print('MIXED_CHECK_OK',nchecks)

if __name__=='__main__':check()
