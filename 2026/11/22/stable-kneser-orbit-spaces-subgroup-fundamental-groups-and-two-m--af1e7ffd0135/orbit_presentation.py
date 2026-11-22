from orbit_complex import *

def reduce_word(w):
 a=[]
 for x in w:
  if a and a[-1]==-x:a.pop()
  else:a.append(x)
 return a

def pi1(m,group):
 v,f,orb,b,c=flags_and_quotient(m,group)
 _,_,mp=get_complex(m)
 if group=="cyclic":mp=mp[::2]
 O={o:i for i,o in enumerate(orb)}
 def idx(fl):return O[min(tuple(pp[x] for x in fl) for pp in mp)]
 active,ma=collapse(orb,b)
 vv=sorted(i for i in active if len(orb[i])==1)
 ee=sorted(i for i in active if len(orb[i])==2)
 tt=sorted(i for i in active if len(orb[i])==3)
 V={a:k for k,a in enumerate(vv)}
 edges={}
 for e in ee:
  s=idx((orb[e][0],));t=idx((orb[e][1],));edges[e]=(s,t)
 par={i:i for i in vv}
 def find(x):
  while par[x]!=x:x=par[x]
  return x
 tree=set()
 for e in ee:
  s,t=edges[e]
  if find(s)!=find(t):par[find(s)]=find(t);tree.add(e)
 assert len(tree)==len(vv)-1
 gen={e:j+1 for j,e in enumerate(e for e in ee if e not in tree)}
 rel=[]
 for t in tt:
  # orbit triangle flags f0 f1 f2 : (edge:f0,f1), (edge:f1,f2), (edge:f0,f2)  
  fid=orb[t]
  # Boundary path f0->f1->f2->f0, use canonical orbit indices of edge flags.
  word=[]
  for pair,sgn in [((fid[0],fid[1]),1),((fid[1],fid[2]),1),((fid[0],fid[2]),-1)]:
   cell=idx(pair)
   if cell not in active:raise ValueError(('collapsed boundary edge',t,cell))
   if cell in gen:word.append(gen[cell]*sgn)
  rel.append(reduce_word(word))
 print('m',m,group,'C',(len(vv),len(ee),len(tt)),'gen',len(gen),'rels',rel)
 removed=[]
 while 1:
  picked=None
  for j,r in enumerate(rel):
   ctr=collections.Counter(abs(x) for x in r)
   for x in ctr:
    if ctr[x]==1:
     picked=(j,x);break
   if picked:break
  if not picked:break
  i,g=picked; w=rel[i]; pos=next(k for k,x in enumerate(w) if abs(x)==g)
  # w = a*g^e*b =1 hence g^e = (b*a)^-1 ; g = (b*a)^(-e)
  a=w[:pos];bb=w[pos+1:]; rhs=[-x for x in (bb+a)[::-1]]
  if w[pos]<0:rhs=[-x for x in rhs[::-1]]
  new=[]
  for j,r in enumerate(rel):
   if j==i:continue
   tmp=[]
   for x in r:
    if abs(x)==g:tmp.extend(rhs if x>0 else [-y for y in rhs[::-1]])
    else:tmp.append(x)
   new.append(reduce_word(tmp))
  rel=new;removed.append((g,len(w)))
  if len(removed)>100:break
 print('elim',removed,'remain rel',rel,'remaining generators',sorted(set(abs(x) for r in rel for x in r)))
 return v,f,orb,b,active,ma,gen,rel

