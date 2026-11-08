from itertools import product

def iterate(b,k):
 w='0'
 for _ in range(k):w=''.join(c*(b-1)+('0' if c=='1' else '1') for c in w)
 return w

def bound(b,k):
 D=(b-2)**k
 H=sum((b-2)**j for j in range(k+1))
 return 2*H-D+1

ncheck=0
for b in range(3,10):
 for k in range(0,8):
  L=b**k
  if L>12000:break
  a=iterate(b,k); aa=''.join('0' if c=='1' else '1' for c in a)
  seen=set()
  for x,y in product((a,aa),repeat=2):
   w=x+y
   c=w[:L].count('1');seen.add(c)
   for i in range(1,L):
    c+= (w[i+L-1]=='1') -(w[i-1]=='1')
    seen.add(c)
  assert seen==set(range(min(seen),max(seen)+1)), (b,k)
  expected=bound(b,k)
  assert len(seen)==expected, (b,k,expected,len(seen))
  D=(b-2)**k
  H=sum((b-2)**j for j in range(k+1))
  M=2*H-D
  assert min(seen)==(L-M)//2 and max(seen)==(L+M)//2,(b,k)
  pref=0;v=[0]
  for char in a:
   pref+=1 if char=='0' else -1;v.append(pref)
  assert max(v)==H,(b,k)
  ncheck+=1
print('VERIFY_OK tested_base_level_pairs',ncheck,'largest_factor_length',max(9**k for k in range(8) if 9**k<=12000))
for b in range(3,10):
 for k in range(1,7):
  L=b**k
  if L>12000: break
  a=iterate(b,k)
  r=1+(b-2)*(L-1)//(b-1)
  h=sum((b-2)**j for j in range(k+1))
  assert sum(1 if c=='0' else -1 for c in a[:r])==h
print('EXTREMAL_PREFIX_OK')
