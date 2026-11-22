
def canon(s):
 return min(s[i:]+s[:i] for i in range(len(s)))

def prim(s):
 n=len(s)
 for p in range(1,n+1):
  if n%p==0 and s[:p]*(n//p)==s:return s[:p]

def D(s):
 n=len(s)
 edges=[i for i in range(n) if s[i]!=s[(i+1)%n]]
 if not edges:return None
 p=(edges[0]+1)%n
 s=s[p:]+s[:p]
 runs=[];cnt=1
 for i in range(1,n):
  if s[i]==s[i-1]:cnt+=1
  else:runs.append(cnt);cnt=1
 runs.append(cnt)
 if max(runs)>2:return None
 return canon(prim(''.join(str(a) for a in runs)))

def inv(y,first):
 u=y*(1 if len(y)%2==0 else 2)
 z=''.join(('1' if i%2==0 else '2')*int(run) for i,run in enumerate(u))
 if first=='2':z=z.translate(str.maketrans('12','21'))
 z=canon(prim(z))
 assert D(z)==canon(y), (y,z,D(z))
 return z
expected=[(2,1,2),(2,2,1),(4,3,2),(6,8,1),(8,12,2),(14,18,4),(24,27,8),(30,80,4),(52,120,8),(78,180,16),(128,269,16)]
S={canon('1'),canon('2')}
for k,(count,least,multiplicity) in enumerate(expected):
 assert len(S)==count
 smallest=min(len(w) for w in S)
 assert smallest==least
 assert sum(len(w)==smallest for w in S)==multiplicity
 print(k,count,smallest,multiplicity)
 if k < len(expected)-1:S={inv(s,c) for s in S for c in '12'}
print('exact recurrence verification passed')
