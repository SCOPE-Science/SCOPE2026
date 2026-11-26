"""Exact cellular homotopy certificate for the order-four projective matroid Singer quotient.

Uses one 0-cell, ten oriented edge orbit cells, 54 triangle orbit cells. A 3fold
face-stabilizer triangle contributes one disk with boundary the corresponding edge
once, not three times. Each generator-elimination move deletes one relator and its
unique-occurring edge generator and substitutes the solved word everywhere else.
"""
from math import comb,gcd
from itertools import combinations
from functools import reduce
N=21
D=(0,1,4,14,16)
lines=[frozenset((i+x)%N for x in D) for i in range(N)]
assert len(set(lines))==N
assert all(sum({a,b} <= line for line in lines)==1 for a,b in combinations(range(N),2))
triangles=[t for t in combinations(range(N),3) if not any(set(t)<=l for l in lines)]
assert len(triangles)==1120
canon=lambda t:min(tuple(sorted((x+i)%N for x in t)) for i in range(N))
reps=sorted(set(canon(t) for t in triangles))
assert len(reps)==54

def reduceword(word):
 stack=[]
 for a in word:
  if stack and stack[-1]==-a:stack.pop()
  else:stack.append(a)
 return tuple(stack)
def inv(word):return tuple(-x for x in reversed(word))
def ed(x,y):
 d=(y-x)%N
 assert d
 return d if d<=N//2 else -(N-d)

words=[]
for t in reps:
 v=(ed(t[0],t[1]),ed(t[1],t[2]),ed(t[2],t[0]))
 stab=N//len({tuple(sorted((x+i)%N for x in t)) for i in range(N)})
 if stab==3:
  assert t==(0,7,14)
  assert v==(7,7,7)
  v=(7,)
 else: assert stab==1
 words.append(reduceword(v))

def test():
 W=list(words); alive=set(range(1,11));moves=[]
 while len(alive)>1:
  possibilities=[]
  for i,w in enumerate(W):
   for g in sorted(alive):
    where=[k for k,x in enumerate(w) if abs(x)==g]
    if len(where)==1:
     # prefer dropping large g and short relator
     possibilities.append((len(w),len([x for x in w if abs(x) not in alive]),-g,i,g,where[0]))
  if not possibilities:break
  _,_,_,i,g,pos=min(possibilities)
  w=W.pop(i)
  # w = before (+/-g) after => g=(after before)^-1 if +g; else g=after before
  other=tuple(w[pos+1:])+tuple(w[:pos]); sign=1 if w[pos]>0 else -1
  replacement=inv(other) if sign==1 else other
  replacement=reduceword(replacement)
  assert all(abs(x)!=g for x in replacement)
  def subst(w):
   z=[]
   for x in w:
    if x==g:z.extend(replacement)
    elif x==-g:z.extend(inv(replacement))
    else:z.append(x)
   return reduceword(z)
  W=[subst(x) for x in W]
  moves.append((g,i,w,replacement))
  alive.remove(g)
  print('elim',g,'using',w,'replacement',replacement,'remaining',len(alive),'maxlen',max(map(len,W)))
 print('alive',alive,'remaining2cells',len(W),'lengths',sorted(set(map(len,W))))
 if len(alive)==1:
  g=next(iter(alive)); exp=[sum(1 if x==g else -1 for x in w) for w in W]
  print('gcd',reduce(gcd,exp,0),'nonzero exponents',sorted(set(x for x in exp if x)))
  print('nzero',sum(x==0 for x in exp),'total',len(exp),'moves',len(moves))
  assert reduce(gcd,exp,0)==7
  assert sorted(set(exp))==[-7,0,7]
  assert sum(x==0 for x in exp)==31
  assert len(W)==45
  assert len(moves)==9
  print('SINGER_Q4_HOMOTOPY_CERTIFICATE_OK')
 else: print('ELIMINATIONS_INCOMPLETE')
if __name__=='__main__':test()
