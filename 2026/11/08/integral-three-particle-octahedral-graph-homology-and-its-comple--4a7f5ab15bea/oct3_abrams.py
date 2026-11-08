from itertools import combinations
from collections import defaultdict
from oct3 import rank_mod_p
from oct3_sym import G, E, gp_data, conj_table
import time, json
from pathlib import Path
N=6+len(E)
SE=sorted([tuple(sorted((u,6+j))) for j,(u,v) in enumerate(E)]+[tuple(sorted((v,6+j))) for j,(u,v) in enumerate(E)])
assert len(SE)==24
seid={e:i for i,e in enumerate(SE)}

def ab_basis(k):
 out=[]
 for i in range(k+1):
  col=[]
  for ee in combinations(range(len(SE)),i):
   endpoints={v for j in ee for v in SE[j]}
   if len(endpoints)!=2*i:continue
   for vv in combinations((v for v in range(N) if v not in endpoints),k-i):
    col.append((ee,vv))
  out.append(col)
 return out
B=ab_basis(3);R=[{b:j for j,b in enumerate(bs)} for bs in B]
print('CUBICAL_BASIS',list(map(len,B)),flush=True)

def differential():
 CC=[None]
 for d in range(1,4):
  cls=[]
  for ee,vv in B[d]:
   out=defaultdict(int)
   for i,e in enumerate(ee):
    newedges=ee[:i]+ee[i+1:]
    for v,coef in [(SE[e][1],1),(SE[e][0],-1)]:
     target=R[d-1][(newedges,tuple(sorted(vv+(v,))))]
     out[target]+=((-1)**i)*coef
   cls.append({j:c for j,c in out.items() if c})
  CC.append(cls)
 return CC

def lift(g):
 ep=gp_data(g)
 return tuple(g[v] for v in range(6))+tuple(6+ep[j] for j in range(len(E)))

def cell_action(g,d,index):
 ee,vv=B[d][index];gg=lift(g)
 mapped=[];sign=1
 for e in ee:
  u,v=SE[e]; a,b=gg[u],gg[v]
  if a>b:sign*=-1
  mapped.append(seid[tuple(sorted((a,b)))])
 sign*=(-1)**sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
 target=R[d][(tuple(sorted(mapped)),tuple(sorted(gg[v] for v in vv)))]
 return target,sign

def signedtrace(g,d):
 return sum(s for j in range(len(B[d])) for tgt,s in [cell_action(g,d,j)] if tgt==j)

def main():
 s=time.monotonic()
 CC=differential()
 for d in (2,3):
  for col in CC[d]:
   vv=defaultdict(int)
   for r,c in col.items():
    for q,a in CC[d-1][r].items():vv[q]+=c*a
   assert not any(vv.values())
 print('CUBICAL_D2_ZERO',flush=True)
 for p in (2,3,1009):
  ranks=[rank_mod_p(CC[d],p)[0] for d in (1,2,3)]
  bettis=[len(B[0])-ranks[0]]+[len(B[d])-ranks[d-1]-ranks[d] for d in (1,2)]+[len(B[3])-ranks[2]]
  print('CUBICAL_FIELD',p,'ranks',ranks,'bettis',bettis,flush=True)
  assert bettis==[1,8,47,0]
 classes=conj_table(G)
 chars=json.load(open(Path(__file__).resolve().parent / 'oct3_chars.json'))
 for (rep,orb),data in zip(classes,chars):
  tr=[signedtrace(rep,i) for i in range(4)]
  L=sum((-1)**i*tr[i] for i in range(4))
  expect=1-data['H1']+data['H2']
  print('ABRAMS_CLASS',list(rep),'tr',tr,'L',L,'derived',expect,flush=True)
  assert L==expect
 for g in G:
  rep=next(c for c in chars if g in next(orb for r,orb in classes if tuple(c['rep'])==r))
  L=sum((-1)**i*signedtrace(g,i) for i in range(4))
  assert L==1-rep['H1']+rep['H2']
 print('OCT3_INDEPENDENT_ABRAMS_CHECK_PASS',flush=True)
if __name__=='__main__':main()
