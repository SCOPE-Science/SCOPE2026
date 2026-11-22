import itertools,collections
P=[(0,1,2)]+[p for p in itertools.permutations(range(3)) if p != (0,1,2)]
index={p:i for i,p in enumerate(P)}
comp=lambda a,b: index[tuple(P[a][P[b][j]] for j in range(3))]
G=[[comp(i,j) for j in range(6)] for i in range(6)]
E=[]
for p in itertools.product(range(6),repeat=6):
 if p[0]!=0:continue
 if all(p[G[i][j]]==G[p[i]][p[j]] for i in range(6) for j in range(6)):E.append(p)
print('End(S3)',len(E));print('ranks',collections.Counter(len(set(p)) for p in E))
I={p:i for i,p in enumerate(E)}
T=[[I[tuple(E[i][v] for v in E[j])] for j in range(len(E))] for i in range(len(E))]
e=I[tuple(range(6))]
ident=next(j for j,r in enumerate(T) if all(r[k]==k and T[k][j]==k for k in range(len(E))))
z=next(j for j,r in enumerate(T) if all(r[k]==j and T[k][j]==j for k in range(len(E))))
idem=[j for j in range(len(E)) if T[j][j]==j]
units=[j for j in range(len(E)) if any(T[j][k]==ident==T[k][j] for k in range(len(E)))]
outs=[j for j in range(len(E)) if j not in units]
print('identity',e,ident,'zero',z,'idempotents',idem,'units',units,'outs',outs,'rankout',[(j,len(set(E[j]))) for j in outs])
# Homomorphisms M->M map identity to identity, units to units; restriction corresponds to any U=S3 endomorphism (10), and images of idempotents outs in the 5 idempotents.
UH=[]
for p in itertools.product(units,repeat=len(units)):
 f=dict(zip(units,p))
 if f[ident]!=ident:continue
 if all(T[f[i]][f[j]]==f[T[i][j]] for i in units for j in units):UH.append(f)
print('unit homs',len(UH))
answers=[]
for u in UH:
 for v in itertools.product(idem,repeat=len(outs)):
  f=u|dict(zip(outs,v))
  if all(T[f[i]][f[j]]==f[T[i][j]] for i in range(len(E)) for j in range(len(E))):
   answers.append(tuple(f[i] for i in range(len(E))))
print('End2',len(answers),'ranks',sorted(collections.Counter(len(set(v)) for v in answers).items()));print('AutEnd1',len([x for x in answers if len(set(x))==len(E)]))
print('End2 range',sorted(set(len(set(v)) for v in answers)))
# Semigroup endomorphisms not required to preserve identity.
S=[tuple(x) for x in answers]
for d in idem:
 if d==ident:continue
 space=[x for x in range(len(E)) if T[d][x]==x==T[x][d]]
 for v in itertools.product(space,repeat=len(outs)):
  f={u:d for u in units}|dict(zip(outs,v))
  if all(T[f[a]][f[b]]==f[T[a][b]] for a in range(len(E)) for b in range(len(E))):
   S.append(tuple(f[i] for i in range(len(E))))
print('ALL SEMIGROUP End2',len(S),'rank-spectrum',sorted(collections.Counter(len(set(v)) for v in S).items()))
assert len(S)==43 and sorted(collections.Counter(len(set(v)) for v in S).items()) == [(1,5),(2,14),(3,9),(4,3),(7,6),(10,6)]
assert len(set(S))==43
print('S3_SECOND_ENDOMORPHISM_TOWER_43_OK')
