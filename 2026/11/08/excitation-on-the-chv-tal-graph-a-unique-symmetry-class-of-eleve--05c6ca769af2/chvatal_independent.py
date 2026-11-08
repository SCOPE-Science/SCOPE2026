#!/usr/bin/env python3
"""Reproducible state-by-state verification of an excitable Chvatal graph."""
from collections import Counter

# Standard 12-vertex realization; edges specified as adjacency sets in a different order.
NEIGHBORS = [
 (9,6,4,1),(7,5,2,0),(8,6,3,1),(9,7,4,2),
 (8,5,3,0),(11,10,4,1),(11,10,2,0),(11,8,3,1),
 (10,7,4,2),(11,10,3,0),(9,8,6,5),(9,7,6,5)]
N = 3 ** 12
P3 = [3**i for i in range(12)]

def successor(code):
    digits=[0]*12; x=code
    for i in range(12):digits[i]=x%3;x//=3
    ans=0
    for i in range(12):
        v=digits[i]
        if v==1:out=2
        elif v==2:out=0
        else:out=int(any(digits[j]==1 for j in NEIGHBORS[i]))
        ans+=out*P3[i]
    return ans

def main():
    succ = [successor(i) for i in range(N)]
    arrival=[-1]*N;period=[0]*N
    for seed in range(N):
        if arrival[seed]>=0:continue
        visit=[];position={};u=seed
        while arrival[u]<0 and u not in position:
            position[u]=len(visit);visit.append(u);u=succ[u]
        if arrival[u]>=0:
            i=len(visit);a=arrival[u];p=period[u]
        else:
            i=position[u];p=len(visit)-i;a=0
            for s in visit[i:]:arrival[s]=0;period[s]=p
        for s in reversed(visit[:i]):
            a+=1;arrival[s]=a;period[s]=p
    joint=Counter(zip(arrival,period));
    orbit_counts={p:joint[(0,p)]//p for p in sorted(set(period))}
    assert sum(joint.values())==N
    assert orbit_counts=={1:1,3:4768,4:294,7:1012,10:504,11:8}
    assert max(arrival)==10 and sum(a==10 for a in arrival)==64
    assert {p:joint[10,p] for p in (3,11)}=={3:32,11:32}
    assert len(joint)==52 and sum(joint[0,p] for p in orbit_counts)==27693
    # Explicitly reconstruct all eight temporal 11-orbits, and prove one automorphism orbit.
    candidates={s for s in range(N) if arrival[s]==0 and period[s]==11}
    cycles=[]
    while candidates:
        s=min(candidates); orbit=[];u=s
        while u not in orbit:
            orbit.append(u);candidates.remove(u);u=succ[u]
        assert u==s and len(orbit)==11
        cycles.append(orbit)
    assert len(cycles)==8
    assert all(all(sum((s//P3[j])%3==1 for s in c)==3 for j in range(12)) for c in cycles)
    print('PERIOD11_VERTEX_EXCITATION_COUNT_OK 3 each vertex')
    print('VERIFY_OK states',N,'temporal_classes',len(joint))
    print('cycles',orbit_counts,'Tmax',max(arrival),'Tmax_states',sum(a==10 for a in arrival))
    print('period11 representatives',[min(c) for c in cycles])
    # Eight explicit maps, each a graph automorphism.
    perm=[
      (0,1,2,3,4,5,6,7,8,9,10,11),
      (0,4,3,2,1,5,9,8,7,6,11,10),
      (1,0,6,11,5,4,2,9,10,7,8,3),
      (4,0,9,10,5,1,3,6,11,8,7,2),
      (1,5,11,6,0,4,7,10,9,2,3,8),
      (4,5,10,9,0,1,8,11,6,3,2,7),
      (5,1,7,8,4,0,11,2,3,10,9,6),
      (5,4,8,7,1,0,10,3,2,11,6,9),
    ]
    graph_edges={tuple(sorted((u,v))) for u in range(12) for v in NEIGHBORS[u]}
    assert len(graph_edges)==24
    assert all(len(set(NEIGHBORS[v]))==4 and v not in NEIGHBORS[v] for v in range(12))
    assert all(not any(w in NEIGHBORS[v] for w in NEIGHBORS[u] if w != v) for u,v in graph_edges)
    def coloring(colors):
        cl=[-1]*12
        order=sorted(range(12),key=lambda v: -sum(1 for w in NEIGHBORS[v] if w<6))
        def bt(i):
            if i==12:return tuple(cl)
            v=order[i]
            for c in range(colors):
                if all(cl[w]!=c for w in NEIGHBORS[v]):
                    cl[v]=c; a=bt(i+1)
                    if a is not None:return a
            cl[v]=-1;return None
        return bt(0)
    assert coloring(3) is None and coloring(4) is not None
    print('GRAPH_CHECK_OK degree4 triangle_free chromatic4')
    reps={s:i for i,c in enumerate(cycles) for s in c}
    images=set()
    for m in perm:
        assert len(set(m))==12
        assert {tuple(sorted((m[u],m[v]))) for u,v in graph_edges}==graph_edges
        x=cycles[0][0];d=[(x//P3[j])%3 for j in range(12)]
        tr=sum(d[j]*P3[m[j]] for j in range(12))
        images.add(reps[tr])
    assert len(images)==8
    print('PERIOD11_AUTOMORPHISM_TRANSITIVITY_OK')
    with open('chvatal_joint_census.csv','w',encoding='utf-8') as out:
        out.write('first_entry_time,least_period,configurations\n')
        for (a,p),count in sorted(joint.items()):out.write(f'{a},{p},{count}\n')
if __name__=='__main__':main()
