"""Finite corroboration of a symbolic homotopy theorem for open neighborhood complexes.
Run: python3 verify_neighborhood_four_cycle.py. Standard Python 3 only.
"""
from collections import defaultdict, Counter
from itertools import combinations


def vertices(m):
    return range(4*m)


def bit(i,a,m):
    return 1 << (i*m+a)


def nonempty_submasks(mask):
    s=mask
    while s:
        yield s
        s=(s-1)&mask


def original_complex(m):
    # Start from independently defined graph adjacency, not from proof's facets.
    adj=[]
    for i in range(4):
        for a in range(m):
            nbr=0
            for j in range(4):
                for b in range(m):
                    if (i==j and a!=b) or (a==b and (j-i)%4 in (1,3)):
                        nbr |= bit(j,b,m)
            assert nbr.bit_count()==m+1
            adj.append(nbr)
    F=set()
    for neighborhood in adj:
        F.update(nonempty_submasks(neighborhood))
    return F,adj


def collapse_pair(F, low, high):
    assert low in F and high in F
    assert (low & high)==low and high.bit_count()==low.bit_count()+1
    # Complete free-face test: the only strict coface remaining is high.
    for t in F:
        if t!=low and (t&low)==low:
            assert t==high, (low,high,t)
    F.remove(low);F.remove(high)


def expected_core(m):
    core=set()
    for i in range(4):
        row=sum(bit(i,a,m) for a in range(m))
        core.update(s for s in nonempty_submasks(row) if s!=row)
    for i in range(4):
        for a in range(m):
            for b in range(m):
                if a!=b:
                    core.add(bit(i,a,m)|bit((i+1)%4,b,m))
    for i in range(4):
        for a in range(m):
            h=bit(i,(a+1)%m,m)
            u=bit((i-1)%4,a,m)
            w=bit((i+1)%4,a,m)
            core.add(u|w)
            core.add(u|w|h)
            for off in (u,w):
                for b in range(m):
                    if b!=a and b!=(a+1)%m:
                        core.add(off|h|bit(i,b,m))
    return core


def run_collapses(m):
    F,adj=original_complex(m)
    initial=set(F)
    nfirst=0;nsecond=0
    for i in range(4):
        for a in range(m):
            h=bit(i,(a+1)%m,m)
            P=bit((i-1)%4,a,m)|bit((i+1)%4,a,m)
            U=sum(bit(i,b,m) for b in range(m) if b not in (a,(a+1)%m))
            for A in sorted((s for s in nonempty_submasks(U)),key=lambda s:(-s.bit_count(),s)):
                collapse_pair(F,P|A,P|A|h)
                nfirst+=1
    for i in range(4):
        for a in range(m):
            h=bit(i,(a+1)%m,m)
            U=sum(bit(i,b,m) for b in range(m) if b not in (a,(a+1)%m))
            subs=sorted((s for s in nonempty_submasks(U) if s.bit_count()>=2),key=lambda s:(-s.bit_count(),s))
            for j in ((i-1)%4,(i+1)%4):
                off=bit(j,a,m)
                for A in subs:
                    collapse_pair(F,off|A,off|A|h)
                    nsecond+=1
    assert F==expected_core(m), ('core differs',len(F),len(expected_core(m)),len(F^expected_core(m)))
    assert nfirst==4*m*(2**(m-2)-1)
    assert nsecond==8*m*(2**(m-2)-m+1)
    assert len(F)==len(initial)-2*(nfirst+nsecond)
    return initial,F,nfirst,nsecond


def interface_relations(m):
    # Cross edges of a chosen adjacent-row interface identify pairs of edges
    # via triangles retained after the explicit elementary collapses.
    nodes={(a,b) for a in range(m) for b in range(m) if a!=b}
    rel=[]
    for a in range(m):
        h=(a+1)%m
        for b in range(m):
            if b not in (a,h):
                # fan with shared vertex in first row (the column colors are indices)
                rel.append(((h,a),(b,a)))
                # fan with shared vertex in second row
                rel.append(((a,h),(a,b)))
    graph=defaultdict(set)
    for x,y in rel:
        assert x in nodes and y in nodes
        graph[x].add(y);graph[y].add(x)
    reached={next(iter(nodes))};todo=list(reached)
    while todo:
        x=todo.pop()
        for y in graph[x]-reached:
            reached.add(y);todo.append(y)
    assert reached==nodes
    assert len(rel)==2*m*(m-2)
    return len(nodes),len(rel),len(rel)-len(nodes)+1


def fvector(F):
    return tuple(Counter(x.bit_count()-1 for x in F)[d] for d in range(max(x.bit_count()-1 for x in F)+1))


def betti_mod2(F):
    bydim=defaultdict(list)
    for s in F:
        bydim[s.bit_count()-1].append(s)
    rank={}
    for d in range(1,max(bydim)+1):
        rows={s:i for i,s in enumerate(bydim[d-1])}
        pivots={}
        for s in bydim[d]:
            col=0;x=s
            while x:
                b=x&-x;x-=b
                col^=1<<rows[s^b]
            while col:
                i=col.bit_length()-1
                if i in pivots:col ^= pivots[i]
                else:pivots[i]=col;break
        rank[d]=len(pivots)
    return {d:len(bydim[d])-rank.get(d,0)-rank.get(d+1,0) for d in bydim}



def independent_acyclic_matching(F,m):
    # A second, independent discrete-Morse check; no use of the collapse core.
    from collections import defaultdict
    remaining=set(F)
    pairs=[]
    for v in range(4*m):
        z=1<<v
        for face in sorted(remaining):
            upper=face|z
            if not face&z and face in remaining and upper in remaining:
                pairs.append((face,upper))
                remaining.remove(face);remaining.remove(upper)
    matched=set(pairs)
    indegree={f:0 for f in F}
    outgoing=defaultdict(list)
    covers=0
    for s in F:
        if s.bit_count()<2:continue
        x=s
        while x:
            b=x&-x;x-=b
            t=s^b
            if (t,s) in matched: lo,hi=t,s
            else: lo,hi=s,t
            outgoing[lo].append(hi)
            indegree[hi]+=1
            covers+=1
    queue=[f for f,d in indegree.items() if d==0]
    i=0
    while i<len(queue):
        f=queue[i];i+=1
        for u in outgoing[f]:
            indegree[u]-=1
            if indegree[u]==0:queue.append(u)
    assert len(queue)==len(F)
    counts=Counter(f.bit_count()-1 for f in remaining)
    expected=Counter({0:1,2:4*m*m-10*m+3})
    expected[m-2]+=4
    assert counts==expected, (m,counts,expected)
    return len(pairs),covers,dict(sorted(counts.items()))


def main():
    for m in (4,5,6,7):
        original,core,first,second=run_collapses(m)
        E,q,surplus=interface_relations(m)
        assert surplus==m*m-3*m+1
        pairs,covers,critical=independent_acyclic_matching(original,m)
        b=betti_mod2(original)
        predicted={0:1,2:4*m*m-10*m+3}
        predicted[m-2]=predicted.get(m-2,0)+4
        assert b=={d:predicted.get(d,0) for d in b},(m,b,predicted)
        assert {d:v for d,v in b.items() if v}==predicted
        print('m=%d faces=%d f=%s first_pairs=%d second_pairs=%d core=%d cross_edges=%d wing_triangles_per_interface=%d betti_F2=%s morse_pairs=%d covers=%d critical=%s' % (m,len(original),fvector(original),first,second,len(core),E,q,b,pairs,covers,critical),flush=True)
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
