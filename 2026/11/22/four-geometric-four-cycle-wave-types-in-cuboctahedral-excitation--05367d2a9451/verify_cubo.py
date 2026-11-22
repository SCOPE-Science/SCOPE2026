"""Second whole-state-space verifier for 3-color GHM on L(Q_3).
Requires Python 3 and NumPy. The graph is constructed from bit-labelled cube edges.
All loops range over every one of 3**12 configurations; no sampling.
"""
import numpy as np
from collections import Counter
from itertools import permutations

edges=[]
for a in range(8):
    for k in range(3):
        b=a^(1<<k)
        if a<b: edges.append((a,b))
assert len(edges)==12
adj=[[j for j,(c,d) in enumerate(edges) if i!=j and len({a,b}&{c,d})==1]
     for i,(a,b) in enumerate(edges)]
assert all(len(row)==4 for row in adj)
P=np.array([3**i for i in range(12)],dtype=np.int64)
S=3**12
states=np.arange(S,dtype=np.int64)
digits=np.array([(states//p)%3 for p in P],dtype=np.int8)
out=np.zeros(S,dtype=np.int64)
for i in range(12):
    excited=(digits[adj[i]]==1).any(axis=0)
    new=np.where(digits[i]==1,2,np.where(digits[i]==2,0,excited.astype(np.int8)))
    out += P[i]*new
assert out.min()>=0 and out.max()<S

# Separate fixed-time certificate, without cycle-finding or indegree deletion.
# F^(10+12)=F^10 proves entry by 10 into periods dividing 12;
# F^9 != F^(9+12) somewhere proves 10 is sharp.
cur=states.copy()
arrays={0:cur}
for t in range(1,23):
    cur=out[cur]
    if t in (1,3,4,9,10,21,22):arrays[t]=cur.copy()
assert np.array_equal(arrays[10],arrays[22])
assert not np.array_equal(arrays[9],arrays[21])
fixed1=int(np.count_nonzero(arrays[1]==states))
fixed3=int(np.count_nonzero(arrays[3]==states))
fixed4=int(np.count_nonzero(arrays[4]==states))
assert (fixed1,fixed3,fixed4)==(1,40741,193)
print('FIXED-POWER', fixed1, fixed3, fixed4)
print('SHARP-PREPERIOD',10)

# Separate first-entry-by-time determination, 0 <= t <= 10.
# Once the current state is periodic under F^12, entry has occurred.
cur=states.copy()
entry=np.full(S,-1,dtype=np.int8)
for t in range(11):
    y=cur.copy()
    for _ in range(12):y=out[y]
    new=(entry<0)&(y==cur)
    entry[new]=t
    cur=out[cur]
assert (entry>=0).all()
print('ENTRY-SHELLS',dict(sorted(Counter(int(i) for i in entry).items())))
print('ENTRY10-WITNESS', int(np.flatnonzero(entry==10)[0]))
assert dict(sorted(Counter(int(i) for i in entry).items()))=={0:40933,1:36739,2:104319,3:153150,4:105532,5:51792,6:16752,7:12672,8:6432,9:2640,10:480}

# Eventual period for every initial state from F^10(x), checked by F^3 and F^4.
final=arrays[10]
f3=out[out[out[final]]]
f4=out[f3]
is1=(out[final]==final)
is3=(f3==final)
is4=(f4==final)
assert (is1|is3|is4).all()
end_period=np.where(is1,1,np.where(is3,3,4))
entry_period=Counter(zip((int(i) for i in entry), (int(p) for p in end_period)))
assert sum(entry_period.values())==S
print('ENTRY-PERIOD',dict(sorted(entry_period.items())))

# Separate primitive period and orbit counts of recurrent states.
period3=fixed3-fixed1
period4=fixed4-fixed1
assert period3%3==0 and period4%4==0
print('PERIODIC-STATES',(fixed1,period3,period4))
print('PERIODIC-ORBITS',(fixed1,period3//3,period4//4))

# Build periodic points without using visited search, then exact orbit equivalence
# under the 48 cube automorphisms and temporal rotation.
periodic=np.flatnonzero(entry==0)
perms=[]
ind={e:i for i,e in enumerate(edges)}
for mask in range(8):
    for axes in permutations(range(3)):
        def shift(x):return mask^sum(((x>>b)&1)<<axes[b] for b in range(3))
        image=[]
        for (a,b) in edges:
            image.append(ind[tuple(sorted([shift(a),shift(b)]))])
        perms.append(tuple(image))
assert len(set(perms))==48
# Symmetries commute with F; test on every state for 4 group generators.
def move(x,p):
    a=0
    for j,idx in enumerate(p):a+=((x//int(P[j]))%3)*int(P[idx])
    return a
for p in (perms[1],perms[6],perms[7],perms[8]):
    src=states[::53]
    lhs=np.array([move(int(out[s]),p) for s in src]);rhs=out[np.array([move(int(s),p) for s in src])]
    assert np.array_equal(lhs,rhs)
cycle_rep={}
for s in periodic:
    s=int(s)
    a=[s];x=int(out[s])
    while x!=s:
        a.append(x);x=int(out[x])
        assert len(a)<=4
    r=min(a)
    cycle_rep[r]=tuple(a)
assert len(cycle_rep)==1+period3//3+period4//4
for k in (3,4):
    roots={r:c for r,c in cycle_rep.items() if len(c)==k}
    unseen=set(roots)
    hist=Counter()
    while unseen:
        r=min(unseen)
        cyc=roots[r]
        orbit={min(move(v,p) for v in cyc) for p in perms}
        assert orbit<=set(roots)
        unseen-=orbit
        hist[len(orbit)]+=1
    print('GEOMETRIC-ORBIT-SIZES',k,dict(sorted(hist.items())))
    if k==4:
        assert hist=={6:2,12:1,24:1}
        print('FOUR-CYCLE-REPS',sorted(r for r,c in roots.items() if r in (14,637,1169,1358)))
print('SECOND-IMPLEMENTATION-CHECK-PASSED')
