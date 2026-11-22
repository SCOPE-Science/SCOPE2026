from collections import deque
families=((0,3,10),(0,2,3),(2,0,15),(1,0,2),(2,1,0),(1,6,0))
def valuation(n):
 if n==0:return 1000
 t=0
 while n%3==0:t+=1;n//=3
 return t

def predicted(a,k):
 m=2*3**k
 def pred(r):
  if a==0:return r%2==0 or r%6==3
  if a==1:return r%2==0 or r==m-1 or ((r+1)//3**valuation(r+1))%3==1
  if a==2:return r%2==0 and r%6 in (0,2) or r%2==1 and (r%6==3 if k==1 else r%18 in (9,15))
  if a==3:return r%2==1 or r==0 or (r//(2*3**valuation(r)))%3==1
  if a==4:return r%2==0 or r%6==1
  if a==5:return r%2==1 and r%3 in (0,1) or r%2==0 and (r%6==0 if k==1 else r%18 in (0,6))
 return {r for r in range(m) if pred(r)}

def reachable(a,k):
 m=2*3**k;aa,bb,cc=families[a]
 seen={0};q=deque([0])
 while q:
  x=q.popleft()
  for y in ((2*x+aa)%m,(3*x+bb)%m,(6*x+cc)%m):
   if y not in seen:seen.add(y);q.append(y)
 return seen
if __name__=='__main__':
 checks=0
 for a,abc in enumerate(families):
  for k in range(1,10):
   r=reachable(a,k);p=predicted(a,k)
   assert r==p, (a,k, sorted(r^p)[:20])
   expected=4*3**(k-1) if a in(0,4) else (3**(k+1)+1)//2 if a in(1,3) else 3 if k==1 else 8*3**(k-2)
   assert len(r)==expected,(a,k,len(r),expected)
   checks+=1
  print(abc, [(k,len(reachable(a,k))) for k in range(1,7)])
 print('PASS',checks,'complete orbit-residue set comparisons')
