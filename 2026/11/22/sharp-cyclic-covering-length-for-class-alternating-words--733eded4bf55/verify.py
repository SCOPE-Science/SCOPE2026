from itertools import product
from collections import Counter,defaultdict

def words(a,b,n):
 A=tuple(range(a));B=tuple(range(a,a+b))
 return [tuple(w) for st in (0,1) for w in product(*([A if (st+i)%2==0 else B for i in range(n)]))]

def edges(a,b,n):
 E=words(a,b,n)
 counts=Counter(E)
 if n%2 and a!=b:
  h=abs(a-b)
  for v in words(a,b,n-1):
   if (a>b and v[0]>=a) or (b>a and v[0]<a):
    counts[v+(v[0],)]+=h
 return counts

def euler(a,b,n):
 ec=edges(a,b,n)
 outgoing=defaultdict(list)
 incoming=Counter();outgoing_counts=Counter()
 for w,num in ec.items():
  u,v=w[:-1],w[1:]
  outgoing[u].extend([(v,w)]*num)
  outgoing_counts[u]+=num;incoming[v]+=num
 assert incoming==outgoing_counts, (a,b,n,incoming-outgoing_counts)
 start=next(iter(outgoing))
 # circuit as sequence of vertices/edges iterative with path edges backtracked
 stack=[(start,None)];tour=[]
 while stack:
  v=stack[-1][0]
  if outgoing[v]:
   nxt,w=outgoing[v].pop();stack.append((nxt,w))
  else:
   tour.append(stack.pop()[1])
 result=list(reversed(tour[:-1]))
 assert len(result)==sum(ec.values()),(a,b,n,len(result),sum(ec.values()))
 assert all(x[1:]==y[:-1] for x,y in zip(result,result[1:]+result[:1]))
 circular=tuple(w[0] for w in result)
 got=Counter(tuple(circular[(i+j)%len(circular)] for j in range(n)) for i in range(len(circular)))
 assert got==ec,(a,b,n,got-ec,ec-got)
 assert set(words(a,b,n)).issubset(set(got))
 pred=2*(a*b)**(n//2)*(max(a,b) if n%2 else 1)
 assert len(circular)==pred,(a,b,n,len(circular),pred)
 return circular

def brute_no_shorter(a,b,n,optimal):
  required=set(words(a,b,n))
  A=tuple(range(a));B=tuple(range(a,a+b))
  # Check every alternating rooted circle of length less than the construction.
  for ell in range(2,optimal,2):
   for start in (0,1):
    pools=[A if (start+i)%2==0 else B for i in range(ell)]
    for circle in product(*pools):
     got={tuple(circle[(i+j)%ell] for j in range(n)) for i in range(ell)}
     assert not required.issubset(got),(a,b,n,ell,circle)

def main():
 total=0
 for a,b in product(range(1,5),repeat=2):
  for n in range(2,7):
   if 2*(a*b)**(n//2)* (max(a,b) if n%2 else 1)>20000:continue
   circ=euler(a,b,n)
   total+=1
 for a,b,n in ((1,1,3),(1,2,3),(2,1,3),(1,3,3),(2,1,5),(1,2,5),(2,2,3),(2,2,2)):
  optimal=2*(a*b)**(n//2)*(max(a,b) if n%2 else 1)
  brute_no_shorter(a,b,n,optimal)
 print('VERIFY_OK: 80 constructive tour families and 8 exact exhaustive shorter-cover obstructions')

if __name__=='__main__':main()
