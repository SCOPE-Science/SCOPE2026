import itertools,json,collections,math
from try_k33_char import G
R=json.load(open('k33four_chars.json'))
D={tuple(q['g']):q for q in R}
I=tuple(range(6));
def compose(a,b):return tuple(a[b[i]] for i in range(6))
def inv(a):return tuple(a.index(i) for i in range(6))
classes=[];left=set(G)
while left:
 g=min(left)
 cl={compose(compose(h,g),inv(h)) for h in G}
 assert cl<=left
 classes.append(sorted(cl));left-=cl
print('classes',len(classes),'sizes',list(map(len,classes)),'sum',sum(map(len,classes)))

def s3char(kind,a):
 fixed=sum(i==a[i] for i in range(3))
 parity=(-1)**sum(a[i]>a[j] for i in range(3) for j in range(i+1,3))
 return {'T':1,'S':parity,'W':fixed-1}[kind]

def ch_irrep(name,g):
 sw=g[0]>=3
 a=tuple((i-3 if sw else i) for i in g[:3])
 b=tuple((i if sw else i-3) for i in g[3:])
 if name[0]=='I':
  u,v=name[1:]
  return 0 if sw else s3char(u,a)*s3char(v,b)+s3char(v,a)*s3char(u,b)
 u,sig=name[1],name[2]
 if not sw:return s3char(u,a)*s3char(u,b)
 prod=tuple(b[a[i]] for i in range(3))
 return sig*s3char(u,prod)
irreps=[('I',u,v) for u,v in itertools.combinations('TSW',2)]+[('D',u,s) for u in 'TSW' for s in (1,-1)]
print('irreps',irreps)
for ir in irreps:
 ch=[ch_irrep(ir,g) for g in G]
 assert sum(x*x for x in ch)==72,(ir,sum(x*x for x in ch))
for k in ('h1','h2','h3'):
 print('degree',k,'id',D[I][k]);decomp={}
 for ir in irreps:
  val=sum(D[g][k]*ch_irrep(ir,g) for g in G)
  assert val%72==0,(k,ir,val)
  if val:decomp[str(ir)]=val//72
 print('decomp',decomp)
 print('invariants',sum(D[g][k] for g in G)//72)
for cl in classes:
 rep=cl[0]; q=D[rep]
 assert all(D[g]['h2']==q['h2'] and D[g]['h3']==q['h3'] and D[g]['h1']==q['h1'] for g in cl)
 print('CLASS',rep,len(cl),q['L'],q['h1'],q['h2'],q['h3'])
