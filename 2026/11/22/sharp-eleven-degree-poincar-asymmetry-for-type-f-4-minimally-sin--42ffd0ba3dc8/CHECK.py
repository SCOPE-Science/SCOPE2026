"""Exact finite certificate for the type-F4 Schubert asymmetry spectrum.

Requires Python >=3.9; standard library only. Run: python F4_ASYMMETRY_CHECK.py.
The root-lattice construction, two KL recursions and Bruhat enumeration
are all deterministic. Generator indices 1,2,3,4 follow the Cartan matrix.
"""
from collections import Counter, deque

C = ((2,-1,0,0), (-1,2,-2,0), (0,-1,2,-1), (0,0,-1,2))
E = tuple(int(i == j) for j in range(4) for i in range(4))

def right(m,s):
    out=list(m); vi=m[4*s:4*s+4]
    for j in range(4):
        for k in range(4):
            out[4*j+k]=m[4*j+k]-C[j][s]*vi[k]
    return tuple(out)

def left(m,s):
    out=list(m)
    for j in range(4):
        col=m[4*j:4*j+4]
        out[4*j+s]=col[s]-sum(C[k][s]*col[k] for k in range(4))
    return tuple(out)

def plus(a,b,degree=0,scale=1):
    q=list(a)+[0]*max(0,len(b)+degree-len(a))
    for i,v in enumerate(b): q[i+degree]+=scale*v
    while len(q)>1 and q[-1]==0: q.pop()
    return tuple(q)

def main():
    matrices=[E]; indexes={E:0}; degree=[0]; parents=[None]; queue=deque([0]); right_edges=[]
    while queue:
        u=queue.popleft()
        while len(right_edges)<=u: right_edges.append([None]*4)
        for s in range(4):
            mat=right(matrices[u],s)
            if mat not in indexes:
                indexes[mat]=len(matrices); matrices.append(mat)
                degree.append(degree[u]+1); parents.append((u,s))
                queue.append(len(matrices)-1)
            right_edges[u][s]=indexes[mat]
    assert len(matrices)==1152 and max(degree)==24
    # Independent check of Coxeter length: count positive roots sent negative.
    roots=set(tuple(int(i==j) for i in range(4)) for j in range(4)); queue=list(roots)
    while queue:
        r=queue.pop()
        for s in range(4):
            v=list(r);v[s]-=sum(C[k][s]*r[k] for k in range(4));v=tuple(v)
            if v not in roots: roots.add(v);queue.append(v)
    positive=[r for r in roots if all(t>=0 for t in r)]
    assert len(roots)==48 and len(positive)==24
    for w,m in enumerate(matrices):
        count=0
        for r in positive:
            v=[sum(m[4*j+i]*r[j] for j in range(4)) for i in range(4)]
            assert all(t<=0 for t in v) or all(t>=0 for t in v)
            count+=all(t<=0 for t in v)
        assert count==degree[w]
    intervals=[]
    for w in range(1152):
        if w==0: intervals.append(frozenset((0,)))
        else:
            u,s=parents[w]
            intervals.append(frozenset(intervals[u]|{right_edges[v][s] for v in intervals[u]}))
    assert sum(map(len,intervals))==396809
    left_edges=[[indexes[left(matrices[u],s)] for s in range(4)] for u in range(1152)]
    for edges in (right_edges,left_edges):
        assert all(edges[edges[w][s]][s]==w for w in range(1152) for s in range(4))
    # Two genuinely distinct recursion directions: left and right descents.
    def make_kl(edges):
        P={(0,0):(1,)}
        for w in range(1,1152):
            s=next(s for s in range(4) if degree[edges[w][s]]<degree[w])
            ws=edges[w][s]
            corrections=[]
            for z in intervals[ws]:
                if degree[edges[z][s]]>=degree[z]:continue
                d=degree[ws]-degree[z]
                if not d%2:continue
                coeff=(d-1)//2; polynomial=P[(z,ws)]
                if coeff<len(polynomial) and polynomial[coeff]:
                    corrections.append((z,polynomial[coeff],(degree[w]-degree[z])//2))
            for x in intervals[w]:
                xs=edges[x][s]; out=()
                if degree[xs]<degree[x]:
                    if (x,ws) in P: out=plus(out,P[(x,ws)],1)
                    if (xs,ws) in P: out=plus(out,P[(xs,ws)])
                else:
                    if (x,ws) in P: out=plus(out,P[(x,ws)])
                    if (xs,ws) in P: out=plus(out,P[(xs,ws)],1)
                for z,mu,e in corrections:
                    if x in intervals[z]:out=plus(out,P[(x,z)],e,-mu)
                assert out and out[0]==1
                assert len(out)-1<(degree[w]-degree[x])/2 or x==w
                P[(x,w)]=out
        return P
    L=make_kl(left_edges);R=make_kl(right_edges)
    assert L==R and len(L)==396809
    selected=[w for w in range(1152) if sum(L[(0,w)])==2]
    assert len(selected)==217
    assert Counter(L[(0,w)] for w in selected)=={
        (1,1):178, (1,0,1):33, (1,0,0,1):6}
    bettis=[]
    for w in range(1152):
        h=[0]*(degree[w]+1)
        for x in intervals[w]: h[degree[x]]+=1
        bettis.append(h)
    w0=degree.index(24); base=bettis[w0]
    expected_max=[1,4,9,15,18,15,16,14,8,5,2]
    expected_count=[178,48,16,4,4,2,2,2,2,2,2]
    expected_eligible=[217,215,177,111,70,36,16,6,6,2,2]
    expected_bound=[1,4,9,16,25,36,48,60,71,80,87]
    assert base[:11]==expected_bound
    for k in range(1,12):
        values=[bettis[w][degree[w]-k]-bettis[w][k] for w in selected if 2*k<degree[w]]
        assert len(values)==expected_eligible[k-1]
        assert max(values)==expected_max[k-1]
        assert values.count(max(values))==expected_count[k-1]
    print('PASS: 1152 Weyl elements; 48 roots; 396809 Bruhat pairs')
    print('PASS: two opposite KL recursions agree on all 396809 pairs')
    print('PASS: 217 KL-at-identity-two elements (178/33/6)')
    print('PASS: sharp 11-degree asymmetry maxima and maximizer counts')
    for k in range(1,12):
        print(f'{k:2d}: max={expected_max[k-1]:2d}, count={expected_count[k-1]:3d}, '
              f'eligible={expected_eligible[k-1]:3d}, general_bound={expected_bound[k-1]:2d}')

if __name__=='__main__': main()
