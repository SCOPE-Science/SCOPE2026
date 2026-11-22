from collections import Counter
for p,t in [(2,1),(3,1)]:
 # GF(p^2) with t^2 = -t for p2? use p2: t^2+t+1=0; p3: t^2+1=0
 def add(u,v):return ((u[0]+v[0])%p,(u[1]+v[1])%p)
 def mul(u,v):
  a,b=u;c,d=v
  if p==2:return ((a*c-b*d)%p,(a*d+b*c-b*d)%p)
  return ((a*c-b*d)%p,(a*d+b*c)%p)
 one=(1,0);z=(0,0); els=[(a,b) for a in range(p) for b in range(p)];
 def powe(v,n):
  r=one
  while n:
   if n&1:r=mul(r,v)
   v=mul(v,v);n//=2
  return r
 inv={a:powe(a,p*p-2) for a in els if a!=z}
 def normalize(pts):
  for a in pts:
   if a!=z:
    w=inv[a];return tuple(mul(t,w) for t in pts)
  raise ValueError
 pts=sorted(set(normalize(t) for t in __import__('itertools').product(els,repeat=3) if any(x!=z for x in t)))
 def dot(a,b):
  r=z
  for i in range(3):r=add(r,mul(a[i],b[i]))
  return r
 curve=[v for v in pts if sum(powe(x,p+1)[0] for x in v)%p==0 and all(powe(x,p+1)[1]==0 for x in v)]
 tangents=sorted(set(normalize(tuple(powe(x,p) for x in v)) for v in curve))
 external=[v for v in pts if v not in curve]
 mult=Counter(sum(dot(l,v)==z for l in tangents) for v in external)
 rat=lambda v: normalize(tuple(powe(x,p) for x in v))==v
 rat_t=sum(rat(l) for l in tangents);rat_x=sum(rat(v) for v in external);
 ratinc=Counter(sum(dot(l,v)==z and rat(l) for l in tangents) for v in external if rat(v))
 rat_plane=[v for v in pts if rat(v)]
 rat_union=sum(any(dot(l,v)==z for l in tangents) for v in rat_plane)
 assert len(curve)==p**3+1 and len(tangents)==p**3+1
 assert len(external)==p*p*(p*p-p+1)
 assert mult==Counter({p+1:len(external)})
 assert rat_t==p+1 and rat_x==p*p
 assert rat_union==p*p+p+1
 if p%2:
  assert ratinc==Counter({2:p*(p+1)//2,0:p*(p-1)//2})
 else:
  assert ratinc==Counter({p+1:1,1:p*p-1})
 for m in range(1,7):
  q=p;A=(q**3+q+2)//2;B=(q**3-q)//2;c=q**4*(q-1)//2
  via_zeta=1-c-c*(-1)**m+A*q**m+B*(-q)**m
  via_gluing=(q+1)*q**m+1 if m%2 else (q**3+1)*q**m-q**5+q**4+1
  assert via_zeta==via_gluing
 print('q=',p,'curve=',len(curve),'lines=',len(tangents),'external=',len(external),'multiplicities=',mult,'fixed lines=',rat_t,'fixed crossings=',rat_x,'rational fixed tangent incidence=',ratinc,'rat union=',rat_union,'rat P2=',len(rat_plane))

print("HERMITIAN_TANGENT_DIVISOR_OK")
