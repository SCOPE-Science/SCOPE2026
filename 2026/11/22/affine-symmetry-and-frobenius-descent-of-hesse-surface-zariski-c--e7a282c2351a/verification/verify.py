"""Exact verification for affine actions on the Hesse negative-support complex.
Uses only Python 3 standard library.  Geometry is assumed as in the references.
"""
import itertools,collections,time
P=[(x,y) for x in range(3) for y in range(3)]
D=[(1,0),(0,1),(1,1),(1,2)]
lines=[(a,b,c) for a,b in D for c in range(3)]
inc=[[int((a*x+b*y-c)%3==0) for x,y in P] for a,b,c in lines]
opts=[(),(0,),(1,),(2,),(0,1),(0,2),(1,2)]

def det(M):
 n=len(M)
 if n==0:return 1
 a=[r.copy() for r in M]
 sign=1; prev=1
 for k in range(n-1):
  if a[k][k]==0:
   sw=next((i for i in range(k+1,n) if a[i][k]!=0),None)
   if sw is None:return 0
   a[k],a[sw]=a[sw],a[k];sign=-sign
  p=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    z=a[i][j]*p-a[i][k]*a[k][j]
    assert z%prev==0
    a[i][j]=z//prev
  for i in range(k+1,n):a[i][k]=0
  prev=p
 return sign*a[-1][-1]

def enumerate_all():
 start=time.monotonic()
 sup=[];counts=collections.Counter();by_fiber=collections.Counter();tested=0
 def search(Q,eligible,bits,chosen,prefix,lsmask):
  nonlocal tested
  smask=0
  for i in chosen:smask|=1<<i
  sup.append(smask|(lsmask<<9));counts[len(chosen)+len(prefix)]+=1
  for pos in range(bits,len(eligible)):
   i=eligible[pos];s=chosen+[i];tested+=1
   if det([[Q[a][b] for b in s] for a in s])>0:search(Q,eligible,pos+1,s,prefix,lsmask)
 for choice in itertools.product(opts,repeat=4):
  chosen_lines=[3*d+k for d,o in enumerate(choice) for k in o]
  lmask=sum(1<<i for i in chosen_lines)
  Q=[[6*(i==j) for j in range(9)] for i in range(9)]
  for d,cs in enumerate(choice):
   if len(cs)==1:
    v=inc[3*d+cs[0]]
    for i in range(9):
     for j in range(9):Q[i][j]-=3*v[i]*v[j]
   elif len(cs)==2:
    v,w=(inc[3*d+cs[k]] for k in range(2))
    for i in range(9):
     for j in range(9): Q[i][j]-=2*(2*v[i]*v[j]+v[i]*w[j]+w[i]*v[j]+2*w[i]*w[j])
  eligible=[i for i in range(9) if Q[i][i]>0]
  search(Q,eligible,0,[],chosen_lines,lmask)
 print('support counts',sorted(counts.items()),'total',len(sup),'tested',tested,'time',time.monotonic()-start)
 return sup, counts

def group_and_table(supports):
 def compose(p,q):return tuple(p[q[i]] for i in range(21))
 def inverse(p):
  inv=[None]*21
  for i,j in enumerate(p):inv[j]=i
  return tuple(inv)
 def cycles(p,first,last):
  seen=set();cy=[]
  for i in range(first,last):
   if i not in seen:
    j=i;n=0
    while j not in seen:seen.add(j);n+=1;j=p[j]
    cy.append(n)
  return tuple(sorted(cy))
 line_sets={frozenset(j for j,(x,y) in enumerate(P) if (a*x+b*y-c)%3==0):i for i,(a,b,c) in enumerate(lines)}
 G=[]
 for a,b,c,d in itertools.product(range(3),repeat=4):
  det=(a*d-b*c)%3
  if not det:continue
  for tx,ty in P:
   pp=[P.index(((a*x+b*y+tx)%3,(c*x+d*y+ty)%3)) for x,y in P]
   perm=tuple(pp+[9+line_sets[frozenset(pp[j] for j in ls)] for ls in line_sets])
   # line_sets dictionary insertion preserves order of lines
   G.append((det,perm,(a,b,c,d,tx,ty)))
 assert len(G)==432
 idx={p:i for i,(_,p,_) in enumerate(G)}; assert len(idx)==432
 invs=[inverse(p) for _,p,_ in G]
 classes=[];unused=set(range(432))
 while unused:
  i=min(unused);g=G[i][1]
  cl={idx[compose(compose(h,g),invs[k])] for k,(_,h,_) in enumerate(G)}
  assert cl<=unused
  unused-=cl
  classes.append((len(cl),i,cl))
 assert len(classes)==11
 # put classes in deterministic order
 classes.sort(key=lambda val:(G[val[1]][0],sum(1 for t in cycles(G[val[1]][1],0,21)),val[0],cycles(G[val[1]][1],0,9)))
 allbits=(1<<21)-1
 def applymask(mask,perm):
  out=0
  while mask:
   b=mask&-mask;i=b.bit_length()-1;out|=1<<perm[i];mask-=b
  return out
 table=[]
 for cs,i,members in classes:
  p=G[i][1];cy=cycles(p,0,21);order=__import__('math').lcm(*cy)
  count=collections.Counter()
  for mask in supports:
   if applymask(mask,p)==mask:count[mask.bit_count()]+=1
  row=dict(det=G[i][0],order=order,class_size=cs,point_cycles=cycles(p,0,9),line_cycles=cycles(p,9,21),curve_cycles=cy, fixed_counts=[count[k] for k in range(10)],fixed_total=sum(count.values()),representative=G[i][2])
  table.append(row)
  print(row)
 # Burnside whole group and det1 subgroup, and orbit enumeration of all masks
 bytyp=collections.Counter((G[i][0],tuple(G[i][1])) for i in range(432))
 orbits=sum(row['class_size']*row['fixed_total'] for row in table)//432
 assert sum(row['class_size']*row['fixed_total'] for row in table)%432==0
 print('orbits',orbits,'orbits det1',sum(row['class_size']*row['fixed_total'] for row in table if row['det']==1)//216)
 return G,table

def independent_supports():
 line_points=[sum(1<<i for i,b in enumerate(v) if b) for v in inc]
 out=set();count=collections.Counter()
 for choice in itertools.product(opts,repeat=4):
  ls=[3*d+k for d, o in enumerate(choice) for k in o]
  lm=sum(1<<i for i in ls)
  for sm in range(512):
   if any(sum(bool(sm&line_points[i]) for i in ls if inc[i][p])>1 for p in range(9) if sm>>p&1):continue
   if any((sm&line_points[i]).bit_count()>1 for i in ls):continue
   if any((sm & (line_points[3*d+o[0]]|line_points[3*d+o[1]])).bit_count()>1 for d,o in enumerate(choice) if len(o)==2):continue
   out.add(sm|(lm<<9));count[sm.bit_count()+len(ls)]+=1
 return out,count

def independent_orbits(supports,G):
 perms={t:p for _,p,t in G}
 gens=[(1,0,0,1,1,0),(1,0,0,1,0,1),(1,1,0,1,0,0),(0,2,1,0,0,0),(0,1,1,0,0,0)]
 def pmask(mask,p):
  n=0
  while mask:
   x=mask&-mask;n|=1<<p[x.bit_length()-1];mask-=x
  return n
 supp=set(supports)
 for size in [4,5]:
  seen=set();n=0
  for s in supp:
   if s in seen: continue
   n+=1;stack=[s];seen.add(s)
   while stack:
    u=stack.pop()
    for t in gens[:size]:
     v=pmask(u,perms[t]);assert v in supp
     if v not in seen:seen.add(v);stack.append(v)
  assert seen==supp
  print('direct orbits',size,n)
  assert n== (299 if size==4 else 239)


if __name__ == '__main__':
    import json
    from pathlib import Path
    supports, coefficients = enumerate_all()
    assert len(supports) == 50165
    G, table = group_and_table(supports)
    expected = json.loads(Path(__file__).with_name('fixed_table.json').read_text(encoding='utf-8'))
    assert json.loads(json.dumps(table)) == expected
    independent, independent_coefficients = independent_supports()
    assert independent == set(supports)
    assert independent_coefficients == coefficients
    print('Second combinatorial enumeration agrees:', len(independent))
    independent_orbits(independent, G)
    standard_frobenius = next(p for _,p,t in G if t == (2,0,0,1,0,0))
    def apply(mask, p):
        result = 0
        while mask:
            bit = mask & -mask
            result |= (1 << p[bit.bit_length()-1])
            mask -= bit
        return result
    standard_fixed = sum(apply(mask,standard_frobenius)==mask for mask in supports)
    assert standard_fixed == 1037
    print('Unsplit standard Hesse Frobenius:', standard_fixed)
    print('HESSE_AFFINE_CHAMBER_11_CLASSES_OK')
