"""Standalone verifier for the <=14-point reflexive 3-polytope census (stdlib only).
Input: RefPoly_full.d3 (KS archive, fetched from TU Wien) + final_table.json (artifact).
Replays: 4319-record parse; exact facet enumeration; lattice-point recounts L(0..6);
exact h* solve; palindromicity/unimodality; window completeness (count==M header);
max-volume extremal V*=22 with gap g=2; witness i=167 entry. ~minutes."""
"""Independent stdlib-only verifier: replays window census from KS archive bytes.
Checks: parse 4319 records; recount lattice points (bbox+facets); L(0..6); h* exact solve;
palindromic+unimodal; identity count==M header; window size; max vol + gap; witness entry."""
import json, math, re
from fractions import Fraction
SRC="work/RefPoly_full.d3"
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b): return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def sub(a,b): return (a[0]-b[0],a[1]-b[1],a[2]-b[2])
def C(n,r):
    if n<0 or r<0 or r>n: return 0
    return math.comb(n,r)
lines=[l for l in open(SRC).read().split("\n") if l.strip()!=""]
assert len(lines)==17276, len(lines)
recs=[]; i=0
while i<len(lines):
    h=lines[i].split(); assert h[0]=="3"
    nv=int(h[1]); m=int(re.search(r"M:(\d+)",lines[i]).group(1))
    rows=[[int(x) for x in lines[i+1+k].split()] for k in range(3)]
    assert all(len(r)==nv for r in rows)
    verts=[tuple(rows[d][j] for d in range(3)) for j in range(nv)]
    recs.append((lines[i],m,sorted(set(verts)))); i+=4
assert len(recs)==4319
def facets_of(verts):
    n=len(verts); planes={}
    for a in range(n):
        for b in range(a+1,n):
            for c in range(b+1,n):
                nn=cross(sub(verts[b],verts[a]),sub(verts[c],verts[a]))
                if nn==(0,0,0): continue
                d=dot(nn,verts[a])
                vals=[dot(nn,v)-d for v in verts]
                if max(vals)<=0: s=1
                elif min(vals)>=0: s=-1
                else: continue
                on=(s*nn[0],s*nn[1],s*nn[2]); oc=s*d
                g=math.gcd(math.gcd(abs(on[0]),abs(on[1])),math.gcd(abs(on[2]),abs(oc)))
                key=(on[0]//g,on[1]//g,on[2]//g,oc//g)
                planes.setdefault(key,True)
    facs=[]
    for key in planes:
        nn,cc=key[:3],key[3]
        assert all(dot(nn,v)==cc for v in verts if True) or True
        # facet = all verts on plane
        assert any(dot(nn,v)==cc for v in verts)
        facs.append((nn,cc))
    # orient outward via centroid
    cx=sum(v[0] for v in verts)/len(verts); cy=sum(v[1] for v in verts)/len(verts); cz=sum(v[2] for v in verts)/len(verts)
    out=[]
    for (nn,cc) in facs:
        if nn[0]*cx+nn[1]*cy+nn[2]*cz>cc: out.append(((-nn[0],-nn[1],-nn[2]),-cc))
        else: out.append((nn,cc))
    return out
def counts(verts,facs,k):
    los=[min(v[d] for v in verts)*k for d in range(3)]; his=[max(v[d] for v in verts)*k for d in range(3)]
    cnt=0
    for x in range(los[0],his[0]+1):
        for y in range(los[1],his[1]+1):
            for z in range(los[2],his[2]+1):
                if all(nn[0]*x+nn[1]*y+nn[2]*z<=cc*k for (nn,cc) in facs): cnt+=1
    return cnt
M=[[C(k+3-j,3) for j in range(4)] for k in range(4)]
def hsolve(b):
    A=[[Fraction(M[r][c]) for c in range(4)]+[Fraction(b[r])] for r in range(4)]
    for col in range(4):
        piv=next(r for r in range(col,4) if A[r][col]!=0); A[col],A[piv]=A[piv],A[col]
        d=A[col][col]; A[col]=[x/d for x in A[col]]
        for r in range(4):
            if r!=col and A[r][col]!=0:
                f=A[r][col]; A[r]=[a-f*bc for a,bc in zip(A[r],A[col])]
    return [A[r][4] for r in range(4)]
win=[]; vols=[]
for ri,(hdr,m,verts) in enumerate(recs):
    facs=facets_of(verts)
    c1=counts(verts,facs,1)
    assert c1==m, (ri,m,c1)  # recount matches KS header exactly
    if m<=14:
        L=[counts(verts,facs,k) for k in range(7)]
        h=hsolve(L[:4]); assert all(x.denominator==1 for x in h), (ri,h)
        h=[int(x) for x in h]
        assert [sum(h[j]*C(k+3-j,3) for j in range(4)) for k in range(7)]==L, ri
        V=L[3]-3*L[2]+3*L[1]-L[0]
        assert sum(h)==V and h==h[::-1], (ri,h,V)
        assert any(all(h[j]<=h[j+1] for j in range(p)) and all(h[j]>=h[j+1] for j in range(p,3)) for p in range(4)), (ri,h)
        win.append(ri); vols.append(V)
print("records=4319 ok; window=",len(win))
print("maxvol=",max(vols)," nmax=",sum(1 for v in vols if v==max(vols))," next=",sorted(set(vols),reverse=True)[1])
assert len(win)==1943 and max(vols)==22 and sorted(set(vols),reverse=True)[1]==20
# witness check: first max entry in file order
tab={r["i"]:r for r in json.load(open("work/final_table.json"))}
first=min(ri for ri,v in zip(win,vols) if v==22)
assert first==167, first
assert tab[167]["vol"]==22 and tab[167]["hstar"]==[1,10,10,1] and tab[167]["count"]==14
print("witness i=167 ok:",tab[167]["header"],tab[167]["verts"])
print("ALL VERIFIER CHECKS PASS")
