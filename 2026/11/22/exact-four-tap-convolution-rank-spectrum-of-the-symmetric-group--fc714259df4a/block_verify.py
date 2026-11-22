from itertools import permutations
from sympy import Matrix
from collections import Counter,defaultdict
G=list(permutations(range(4))); eid={a:i for i,a in enumerate(G)}
def sign(a):return (-1)**sum(a[i]>a[j] for i in range(4) for j in range(i+1,4))
PAIRINGS=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
def canon(pairs):return tuple(sorted(tuple(sorted(p)) for p in pairs))
match=[canon(x) for x in PAIRINGS]
def matperm(p):return Matrix([[int(p[j]==i) for j in range(4)] for i in range(4)])
def matmatch(p):
 images=[match.index(canon(tuple(tuple(p[t] for t in pair) for pair in pp))) for pp in PAIRINGS]
 return Matrix([[int(images[j]==i) for j in range(3)] for i in range(3)])
def profile(S):
 pm=sum((matperm(G[g]) for g in S),Matrix.zeros(4));mn=sum((sign(G[g])*matperm(G[g]) for g in S),Matrix.zeros(4));q=sum((matmatch(G[g]) for g in S),Matrix.zeros(3));
 eps=int(sum(sign(G[g]) for g in S)!=0)
 # dims 1,1,2,3,3
 r=(1,eps,q.rank()-1,pm.rank()-1,mn.rank()-eps)
 return tuple(map(int,r))
classes=[]
for l in open('independent_orbits.tsv'):
 s,r,n=l.strip().split('\t');S=tuple(map(int,s.split(',')));r=int(r);n=int(n)
 pr=profile(S);calc=pr[0]+pr[1]+2*pr[2]+3*pr[3]+3*pr[4]
 assert calc==r,(S,pr,calc,r)
 classes.append((S,r,n,pr))
h=Counter();hd=defaultdict(Counter)
for S,r,n,pr in classes:
 h[pr]+=n;hd[r][pr]+=n
assert len(classes)==34
assert len(h)==18
print('distinct Fourier rank profiles',len(h))
for r in sorted(hd):
 print('rank',r,'profiles',len(hd[r]),'counts',dict(hd[r]))
with open('block_profiles.tsv','w') as f:
 for S,r,n,pr in classes:f.write(f'{",".join(map(str,S))}\t{r}\t{n}\t{",".join(map(str,pr))}\n')
