"""Standalone direct comparison of face-orbit Lefschetz traces; no external packages."""
from itertools import combinations

def fibonacci(k):
 a,b=0,1
 for _ in range(k): a,b=b,a+b
 return a

def graph(n):
 w=2*n
 E=set()
 for c in range(w):
  for r in (0,1):E.add(tuple(sorted(((r,c),(r+1,c)))))
  if c+1<w:
   for r in (0,1,2):E.add(tuple(sorted(((r,c),(r,c+1)))))
 return sorted(E)

def perms(E,n):
 ix={e:i for i,e in enumerate(E)};w=2*n
 def go(f):
  return [ix[tuple(sorted((f(u),f(v))))] for u,v in E]
 return {
 'row':go(lambda x:(2-x[0],x[1])),
 'column':go(lambda x:(x[0],w-1-x[1])),
 'half':go(lambda x:(2-x[0],w-1-x[1])),
 }

def perfect(E,n):
 full=set((r,c) for r in range(3) for c in range(2*n)); by={v:[] for v in full}
 for i,(a,b) in enumerate(E):by[a].append((b,i));by[b].append((a,i))
 def search(U,F):
  if not U:
   yield tuple(F);return
  v=min(U)
  for u,i in by[v]:
   if u in U: yield from search(U-{u,v},F+[i])
 return list(search(full,[]))

def direct(n):
 E=graph(n);pm=perfect(E,n);F={0}
 for face in pm:
  bits=[1<<i for i in face]
  parts=[0]
  for b in bits:parts += [x|b for x in parts]
  F.update(parts)
 out=[]
 for name,p in perms(E,n).items():
  tr=0
  for mask in F:
   orbit=0; j=mask
   while j:
    low=j&-j; i=low.bit_length()-1
    orbit|=1<<p[i];j-=low
   if orbit!=mask:continue
   pairs=sum(1 for i in range(len(E)) if mask>>i&1 and p[i]>i and mask>>p[i]&1)
   tr+=(-1)**(mask.bit_count()-1+pairs)
  out.append(tr*((-1)**(n-1)))
 return len(E),len(pm),len(F),out

if __name__=='__main__':
 for n in (2,3,4):
  e,p,f,t=direct(n)
  print(f'n={n} edges={e} tilings={p} simplices={f} homology_traces_row_column_half={t}',flush=True)
