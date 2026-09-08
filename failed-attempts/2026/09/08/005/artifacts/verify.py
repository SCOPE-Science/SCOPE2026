"""Independent verifier (stdlib only): rebuilds PG(2,q), q=5,7,8,9 from points
CSVs, cross-checks lines CSVs, rechecks arc property, completeness, secant
distributions, stabilizer orders, blocking sets and spectrum gaps."""
import json,csv,os,itertools
D=os.path.dirname(os.path.abspath(__file__))
def A(q,a,b):return(a+b)%q if q in(5,7)else(a^b if q==8 else(a%3+b%3)%3+3*((a//3+b//3)%3))
def N(q,a):return(-a)%q if q in(5,7)else(a if q==8 else(-a%3)+3*(-(a//3)%3))
def S(q,a,b):return A(q,a,N(q,b))
def M(q,a,b):
 if q in(5,7):return a*b%q
 if q==8:
  p=0
  while b:
   if b&1:p^=a
   a<<=1
   if a&8:a^=0xB
   b>>=1
  return p&7
 a0,a1,b0,b1=a%3,a//3,b%3,b//3;return(a0*b0+2*a1*b1)%3+3*((a0*b1+a1*b0)%3)
def V(q,a):
 assert a
 if q in(5,7):return pow(a,-1,q)
 if q==8:
  for x in range(1,8):
   if M(q,a,x)==1:return x
 n=((a%3)*(a%3)+(a//3)*(a//3))%3;w=pow(n,-1,3);return(a%3)*w%3+3*((-(a//3))*w%3)
def R(q,v):
 for x in v:
  if x:
   xi=V(q,x);return tuple(M(q,xi,y)for y in v)
 raise AssertionError(f"zero vector {v}")
def F(q,a,s):
 for _ in range(s):a=M(q,a,a)if q==8 else(a%3)+3*(-(a//3)%3)
 return a
def MV(q,X,v):return tuple(A(q,A(q,M(q,X[i][0],v[0]),M(q,X[i][1],v[1])),M(q,X[i][2],v[2]))for i in range(3))
def MM(q,X,Y):return tuple(tuple(A(q,A(q,M(q,X[i][0],Y[0][j]),M(q,X[i][1],Y[1][j])),M(q,X[i][2],Y[2][j]))for j in range(3))for i in range(3))
def MI(q,X):
 (a,b,c),(d,e,f),(g,h,i)=X;C=lambda p,q2,r,s2:S(q,M(q,p,q2),M(q,r,s2))
 Z=((C(e,i,f,h),C(c,h,b,i),C(b,f,c,e)),(C(f,g,d,i),C(a,i,c,g),C(c,d,a,f)),(C(d,h,e,g),C(b,g,a,h),C(a,e,b,d)))
 t=A(q,A(q,M(q,a,Z[0][0]),M(q,b,Z[1][0])),M(q,c,Z[2][0]));assert t!=0;w=V(q,t)
 return tuple(tuple(M(q,w,x)for x in row)for row in Z)
def build(q):
 P=[tuple(map(int,(r["x"],r["y"],r["z"])))for r in csv.DictReader(open(f"{D}/points_q{q}.csv"))]
 n=len(P);assert n==q*q+q+1;E=range(q if q in(5,7)else(8 if q==8 else 9));L=[]
 for a in E:
  for b in E:
   for c in E:
    if(a,b,c)==(0,0,0)or R(q,(a,b,c))!=(a,b,c):continue
    m=frozenset(i for i,(x,y,z)in enumerate(P)if A(q,A(q,M(q,a,x),M(q,b,y)),M(q,c,z))==0)
    assert len(m)==q+1;L.append(m)
 assert len(L)==n
 G=list(csv.DictReader(open(f"{D}/lines_q{q}.csv")))
 for j,r in enumerate(G):assert set(map(int,r["members"].split()))==set(L[j])
 T={}
 for j,s in enumerate(L):
  for a,b in itertools.combinations(sorted(s),2):T[a,b]=T[b,a]=j
 return P,{p:i for i,p in enumerate(P)},L,T,n
def ST(q,P,I,src,tgt):
 E=[P[h]for h in src[:4]];Bs=((E[0][0],E[1][0],E[2][0]),(E[0][1],E[1][1],E[2][1]),(E[0][2],E[1][2],E[2][2]))
 try:Bi=MI(q,Bs)
 except AssertionError:return 0
 a=MV(q,Bi,E[3])
 if any(x==0 for x in a):return 0
 Ts=set(tgt);seen=set()
 for t in itertools.permutations(tgt,4):
  T=[P[x]for x in t];W=((T[0][0],T[1][0],T[2][0]),(T[0][1],T[1][1],T[2][1]),(T[0][2],T[1][2],T[2][2]))
  try:U=MI(q,W)
  except AssertionError:continue
  b=MV(q,U,T[3])
  if any(x==0 for x in b):continue  # collinear triple: no PGL map from frame
  # unique projective map E->T (fundamental theorem): D=diag(b_i/a_i)
  Dd=tuple(tuple((M(q,b[i],V(q,a[i]))if i==j else 0)for j in range(3))for i in range(3))
  K=MM(q,MM(q,W,Dd),Bi)
  if all(I[R(q,MV(q,K,P[h]))]in Ts for h in src):
   key=tuple(R(q,MV(q,K,P[j]))for j in range(len(P)))
   seen.add(key)
 return len(seen)
def CK(q,P,I,L,T,n,H,rep,pgla=None):
 Hs=set(H);assert all(c not in L[T[a,b]]for a,b,c in itertools.combinations(H,3))
 assert set().union(*(L[T[a,b]]for a,b in itertools.combinations(H,2)))==set(range(n))
 for t,(a,b)in rep["cover_witness"].items():assert int(t)in L[T[a,b]]and int(t)not in Hs
 assert len(rep["cover_witness"])==n-len(H)
 d={0:0,1:0,2:0}
 for s in L:d[len(s&Hs)]+=1
 assert sum(d.values())==n and all(d[i]==rep["secants"][str(i)]for i in(0,1,2))
 assert ST(q,P,I,H,H)==rep["stabilizer_PGL"]
 if pgla:assert sum(ST(q,P,I,[I[R(q,tuple(F(q,c,s)for c in P[h]))]for h in H],H)for s in range(pgla[0]))==pgla[1]
 return d
def main():
 W=json.load(open(f"{D}/witnesses.json"));G={}
 for q in(5,7,8,9):G[q]=build(q);print(f"PG(2,{q}): {G[q][4]} pts/lines, CSV cross-check OK")
 for q in(5,7):
  P,I,L,T,n=G[q];Sp=W["spectra"][str(q)];assert Sp["n"]==n
  for k,Rp in Sp["reps"].items():
   d=CK(q,P,I,L,T,n,[I[tuple(c)]for c in Rp["coords"]],Rp);print(f"q={q} k={k}: arc+complete+sec{d}+stab={Rp['stabilizer_PGL']} OK")
  e=[I[R(q,v)]for v in((1,0,0),(0,1,0),(0,0,1),(1,1,1))]
  Ff=set().union(*(L[T[a,b]]for a,b in itertools.combinations(e,2)));pool=[i for i in range(n)if i not in Ff]
  for k in range(4,max(Sp["spectrum"])+1):
   f=[0];st=[([],0)]
   while st:
    ch,i=st.pop();Az=e+ch
    if len(Az)==k:
     if set().union(*(L[T[a,b]]for a,b in itertools.combinations(Az,2)))==set(range(n)):f[0]+=1
     continue
    for j in range(i,len(pool)):
     p=pool[j]
     if all(p not in L[T[a,b]]for a,b in itertools.combinations(Az,2)):st.append((ch+[p],j+1))
   assert(f[0]>0)==(k in Sp["spectrum"]),(q,k);print(f"q={q} k={k}: complete-extensions={f[0]} ({'in S'if k in Sp['spectrum']else'gap'}) OK")
 for q in(8,9):
  P,I,L,T,n=G[q];E=W[f"q{q}"];H=[I[tuple(c)]for c in E["H_coords"]];assert sorted(H)==E["H"]
  CK(q,P,I,L,T,n,H,E,(3,E["stabilizer_PGammaL"])if q==8 else(2,E["stabilizer_PGammaL"]))
  assert[ii for ii,s in enumerate(L)if not(s&set(H))]==E["skew_lines"]and set(E["skew_example_members"])==L[E["skew_lines"][0]]
  B,Ts=set(E["blocking_line"]),set(E["triangle_set"]);assert all(s&B and s&Ts for s in L)and not any(s<=Ts for s in L)
  c=[0];Tl=sorted(Ts);st=[(0,[])]
  while st:
   p,ch=st.pop()
   if len(ch)==10:c[0]+=1;continue
   if p==len(Tl)or len(ch)+(len(Tl)-p)<10:continue
   st.append((p+1,ch));o=Tl[p]
   if all(o not in L[T[a,b]]for a,b in itertools.combinations(ch,2)):st.append((p+1,ch+[o]))
  assert c[0]==E["triangle_10arcs"]==0
  print(f"q={q}: 10-arc+secants+stab={E['stabilizer_PGL']}/PGammaL={E['stabilizer_PGammaL']}+blocking/T-no-10-arc OK")
 print("ALL VERIFY.PY CHECKS PASSED")
if __name__=="__main__":main()
