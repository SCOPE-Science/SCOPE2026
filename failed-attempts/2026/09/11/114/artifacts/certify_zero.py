"""Certify the ZERO-uniform candidate over ALL admissible pairs (any sizes 2..8),
with exact separation certificates for each killing deletion.

Candidate config C* (integer points, vertex order 0..9):
[(0,5,4),(0,6,5),(3,6,1),(6,3,2),(0,4,5),(3,3,4),(0,3,0),(0,0,5),(0,2,3),(6,2,3)]

For each unordered disjoint admissible pair (A,B):
  - if strict_meet(A,B) is False at full strength: pair dead (record full-dead).
  - else: find killing vertex v with strict NON-meet at deletion v AND a
    strict separating-plane certificate (axis or facet normal of D with margin).
    If deletion (A2,B2) has strict_meet False but only by boundary degeneracy
    (no strict separator found among candidates), flag UNCERTIFIED.
Uses exact integer arithmetic throughout; strict_meet sound but incomplete on
boundary: UNCERTIFIED cases must be resolved by exact LP before claiming.
"""
import itertools
C=[(0,5,4),(0,6,5),(3,6,1),(6,3,2),(0,4,5),(3,3,4),(0,3,0),(0,0,5),(0,2,3),(6,2,3)]
P=C
def det3(M):
    (a,b,c),(d,e,f),(g,h,k)=M
    return a*(e*k-f*h)-b*(d*k-f*g)+c*(d*h-e*g)
def sub(u,v): return (u[0]-v[0],u[1]-v[1],u[2]-v[2])
def dot(u,v): return u[0]*v[0]+u[1]*v[1]+u[2]*v[2]
def cross(u,v): return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
def ori(a,b,c,d):
    pa,pb,pc,pd=P[a],P[b],P[c],P[d]
    return det3([[pb[j]-pa[j] for j in range(3)],[pc[j]-pa[j] for j in range(3)],[pd[j]-pa[j] for j in range(3)]])
def pierce(p,q,a,b,c):
    s1=ori(p,a,b,c); s2=ori(q,a,b,c)
    if s1==0 or s2==0 or (s1>0)==(s2>0): return False
    t1=ori(p,q,a,b); t2=ori(p,q,b,c); t3=ori(p,q,c,a)
    if t1==0 or t2==0 or t3==0: return False
    return (t1>0)==(t2>0)==(t3>0)
def inset(x,a,b,c,d):
    o=ori(a,b,c,d)
    if o==0: return False
    return ori(x,b,c,d)*o>0 and ori(x,a,c,d)*ori(b,a,c,d)>0 and ori(x,a,b,d)*ori(c,a,b,d)>0 and ori(x,a,b,c)*ori(d,a,b,c)>0
def meet(A,B):
    A=list(A);B=list(B)
    if len(B)>=4:
        for x in A:
            for q in itertools.combinations(B,4):
                if inset(x,*q): return True
    if len(A)>=4:
        for x in B:
            for q in itertools.combinations(A,4):
                if inset(x,*q): return True
    if len(B)>=3:
        for e in itertools.combinations(A,2):
            for t in itertools.combinations(B,3):
                if pierce(e[0],e[1],*t): return True
    if len(A)>=3:
        for e in itertools.combinations(B,2):
            for t in itertools.combinations(A,3):
                if pierce(e[0],e[1],*t): return True
    return False
def separator(A2,B2):
    """Return strict separating normal (integer triple) + margin sign, or None."""
    D=[sub(P[p],P[q]) for p in A2 for q in B2]
    n=len(D)
    cands=[(1,0,0),(0,1,0),(0,0,1)]
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                u=cross(sub(D[j],D[i]),sub(D[k],D[i]))
                if u!=(0,0,0): cands.append(u)
    for u in cands:
        vals=[dot(u,d) for d in D]
        if all(v>0 for v in vals): return (u,1,min(vals))
        if all(v<0 for v in vals): return (u,-1,min(-v for v in vals))
    return None
verts=list(range(10))
pairs=[]; seen=set()
for r1 in range(2,9):
    for s in itertools.combinations(verts,r1):
        S=frozenset(s); rest=[v for v in verts if v not in S]
        for r2 in range(2,len(rest)+1):
            for t in itertools.combinations(rest,r2):
                T=frozenset(t)
                a,b=(S,T) if str(sorted(S))<=str(sorted(T)) else (T,S)
                if (a,b) in seen: continue
                seen.add((a,b)); pairs.append((sorted(a),sorted(b)))
print("total admissible:",len(pairs))
full_dead=0; certified=0; uncertified=[]; survivors=[]
for (A,B) in pairs:
    if not meet(A,B):
        full_dead+=1; continue
    killed=None
    for v in range(10):
        A2=[x for x in A if x!=v]; B2=[x for x in B if x!=v]
        if not meet(A2,B2):
            sep=separator(A2,B2)
            if sep is not None:
                killed=(v,sep); break
    if killed is None:
        # check whether some deletion at least non-meets (boundary) or full survivor
        nonmeet=[v for v in range(10) if not meet([x for x in A if x!=v],[x for x in B if x!=v])]
        if len(nonmeet)==0: survivors.append((A,B))
        else: uncertified.append((A,B,nonmeet))
    else:
        certified+=1
print("full_dead:",full_dead,"certified-killed:",certified,"uncertified:",len(uncertified),"TRUE survivors:",len(survivors))
for u in uncertified[:20]: print("UNCERT:",u)
for s in survivors[:20]: print("SURV:",s)
