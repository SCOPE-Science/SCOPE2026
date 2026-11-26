from collections import defaultdict,Counter,deque
E=[(i,j,3-i-j) for i in range(4) for j in range(4-i)]
idx={e:i for i,e in enumerate(E)}
assert len(E)==10

def times(a,b):
 r={}
 for ea,ca in a.items():
  for eb,cb in b.items():
   e=tuple(ea[i]+eb[i] for i in range(3))
   r[e]=(r.get(e,0)+ca*cb)%3
 return {e:c for e,c in r.items() if c}

def subst(M):
 T=[]
 v=[{tuple(1 if i==j else 0 for i in range(3)):M[k][j] for j in range(3) if M[k][j]} for k in range(3)]
 for e in E:
  p={(0,0,0):1}
  for k in range(3):
   for a in range(e[k]):p=times(p,v[k])
  t=[p.get(w,0) for w in E]
  T.append(t)
 return T
mats=[[[1,1,0],[0,1,0],[0,0,1]],[[1,0,0],[0,1,1],[0,0,1]],[[0,1,0],[1,0,0],[0,0,1]],[[1,0,0],[0,0,1],[0,1,0]],[[2,0,0],[0,1,0],[0,0,1]]]
Ts=[subst(M) for M in mats]
def coeff(code):
 c=[]
 for i in range(10): c.append(code%3);code//=3
 return c
def enc(c):return sum(v*3**i for i,v in enumerate(c))
def norm(code):
 c=coeff(code)
 if next(i for i in c if i)==2: return enc([(2*v)%3 for v in c])
 return code

def image(code,T):
 c=coeff(code);v=[sum(c[j]*T[j][i] for j in range(10))%3 for i in range(10)]
 return norm(enc(v))
codes={norm(int(l)) for l in open('candidate_codes.txt')}
print('equations',len(codes))
orbits=[]
while codes:
 start=min(codes);seen={start};todo=[start]
 for x in todo:
  for T in Ts:
   y=image(x,T)
   if y not in seen:seen.add(y);todo.append(y)
 assert seen<=codes, ('invariance bug', len(seen-codes))
 codes-=seen
 orbits.append((start,len(seen)))
print('orbits',orbits,'sizes',Counter(v for k,v in orbits)); assert orbits==[(2244,936),(2325,936),(2937,1872)]
for code,size in orbits:
 c=coeff(code)
 print('rep',code,'size',size,'stabilizer',5616//size,'coefs',c,'monomials',E)
