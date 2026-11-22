from collections import Counter
for n in range(5,22):
 lower=Counter();upper=Counter()
 for m in range(1<<n):
  k=m.bit_count()
  if k>2*(n//7)+3:continue
  cnt=[sum(m>>((i+d)%n)&1 for d in [-2,-1,1,2]) for i in range(n)]
  if min(cnt)>=1:
   lower[k]+=1
   if max(cnt)<=2:upper[k]+=1
 kk=min(lower)
 if n%7==1 and n>=8:
  q=n//7
  assert lower[kk]==(2*q+1)*n
  assert upper[kk]==(2*q-1)*n
  assert lower[kk]-upper[kk]==2*n
 print(n,kk,lower[kk],upper[kk],lower[kk]-upper[kk])
