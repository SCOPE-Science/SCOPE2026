import itertools,collections
raw='''000000000000000
000000000000101
000000000100010
000000000100100
000000001100100
000000010100101
000001000001000
000001000010000
000001000100000
000001000100101
000001000110101
000001100101110
000011000010000
000011000110101
000101000001000
000101000010001
000101000100000
000101000100001
000101000100101
001001000010101
001001000110111
010000000110101
010000010001000
010000100010101
010001000101100
010001000110101
010001000111101
100000001000000
100000001100100
100000010000000
100000010100101
100000100000000
100000100000101
100001000000000
100001000000101
100001000001000
100001000100100
100001000100101
100001010001000
100001010010001
100001010100000
100001010100001
100001100010101
100001100100010
100001100100100
100001100101110
100101001001000
100101100100010
101001001010101
101001010001101
101001100010101
101001100100110
110001001011000
110001001110101
110001010110000
110001100110010'''.splitlines()
assert len(raw)==56
# Convert strings into adjacency matrices first horizontal binary orientation
adjs=[]
for s in raw:
 adj=[[0]*6 for _ in range(6)];k=0
 for i in range(6):
  for j in range(i+1,6):
   adj[i][j]=int(s[k]);adj[j][i]=1-int(s[k]);k+=1
 adjs.append(adj)
C=[[0]*6 for _ in adjs]
for it in range(10):
 keys=[]
 for g,adj in enumerate(adjs):
  for i in range(6):
   keys.append((C[g][i],tuple(sorted(C[g][j] for j in range(6) if adj[i][j])),tuple(sorted(C[g][j] for j in range(6) if adj[j][i]))))
 mapping={t:i for i,t in enumerate(sorted(set(keys)))}
 new=[[mapping[keys[g*6+i]] for i in range(6)] for g in range(56)]
 if new==C:break
 C=new
sig=collections.defaultdict(list)
for g,c in enumerate(C): sig[tuple(sorted(c))].append(g)
print('MCKAY',len(adjs),len(sig),[v for v in sig.values() if len(v)>1]); assert len(adjs)==56 and len(sig)==55 and [v for v in sig.values() if len(v)>1]==[[48,49]]
for v in sig.values():
 if len(v)>1:
  for i in v:
   a=adjs[i];counts=sum(all(a[p[k]][p[h]] for k in range(4) for h in range(k+1,4)) for p in itertools.permutations(range(6),4))
   print('colliding index',i,'word',raw[i],'degrees',sorted(map(sum,a)),'transitive-4',counts)

assert sorted(sum(all(adjs[g][p[k]][p[h]] for k in range(4) for h in range(k+1,4)) for p in __import__("itertools").permutations(range(6),4)) for g in (48,49))==[0,3]
print("MCKAY_VERIFY_OK")
