from itertools import permutations
from math import gcd,comb
from collections import Counter

def deck(w):
    q=[0]*3; u=v=t=0
    for a in w:
        if a==0:q[0]+=1
        elif a==1:u+=q[0];q[1]+=1
        else:v+=q[0];t+=q[1];q[2]+=1
    return u,v,t

def words(a,b,c):
    def rec(t,ct):
        if sum(ct)==0:
            yield tuple(t); return
        for j in range(3):
            if ct[j]:
                ct[j]-=1;t.append(j);yield from rec(t,ct);t.pop();ct[j]+=1
    yield from rec([],[a,b,c])

def lattice(a,b,c):
    return {(x,y,z) for x in range(a*b+1) for y in range(a*c+1) for z in range(b*c+1) if 0 <= c*x+a*z-b*y <= a*b*c}

def formula(b,c):
    g=gcd(b,c)
    return ((b*b-1)*(c*c-1)+(g*g-1))//6

cases=0
for a in range(1,5):
 for b in range(1,5):
  for c in range(1,5):
   if a+b+c>10:continue
   S=set(map(deck,words(a,b,c)));L=lattice(a,b,c)
   assert S<=L,(a,b,c,S-L)
   assert (len(S)==len(L))== (sum(x>1 for x in (a,b,c))<=1),(a,b,c)
   if a==1:
    actual=len(L)-len(S)
    assert actual==formula(b,c),((a,b,c),actual,formula(b,c))
   cases+=1
print('PASS independently enumerated',cases,'positive Parikh triples of length <= 10 and checked full hull, saturation iff, and singleton hole formula.')
for b in range(1,26):
 for c in range(1,26):
  L=sum(b*c+1-abs(c*x-b*y) for x in range(b+1) for y in range(c+1))
  D=(b+1)*(c+1)*(2+b*c)//2
  assert L-D==formula(b,c),(b,c,L,D,formula(b,c))
print('PASS exact lattice-point and closed hole count against independent double-sum for 625 singleton pairs')
