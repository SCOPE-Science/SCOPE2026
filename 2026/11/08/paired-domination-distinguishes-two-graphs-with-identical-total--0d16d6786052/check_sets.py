"""Independent verifier: set-theoretic graph model and combinations enumeration."""
from itertools import combinations

V={(i,j) for i in range(4) for j in range(4)}
D={(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)}


def neighborhoods(which):
    if which=='S':
        return {v:{((v[0]+a)%4,(v[1]+b)%4) for a,b in D} for v in V}
    return {v:{u for u in V if u!=v and (u[0]==v[0] or u[1]==v[1])} for v in V}


def pairable(sel,nb):
    sel=frozenset(sel)
    if not sel: return True
    u=min(sel)
    for v in sorted(sel & nb[u]):
        if pairable(sel-{u,v},nb): return True
    return False


def run(which):
    nb=neighborhoods(which)
    T=[]; P=[]
    verts=sorted(V)
    for k in range(17):
        tot=pair=0
        for tup in combinations(verts,k):
            chosen=set(tup)
            if any(not(nb[x]&chosen) for x in V): continue
            tot+=1
            if k%2==0 and pairable(chosen,nb):pair+=1
        T.append(tot);P.append(pair)
    return T,P

T_S,P_S=run('S')
T_R,P_R=run('R')
assert T_S==T_R
assert T_S[:5]==[0,0,0,0,80]
assert P_S[4]==48 and P_R[4]==80
assert [P_R[i]-P_S[i] for i in range(17)] == [0,0,0,0,32,0,80,0,96]+[0]*8
print('PASS independent set-theoretic search over all 2^16 subsets')
print('PASS T_S = T_R =',T_S)
print('PASS P_S=',P_S)
print('PASS P_R=',P_R)
