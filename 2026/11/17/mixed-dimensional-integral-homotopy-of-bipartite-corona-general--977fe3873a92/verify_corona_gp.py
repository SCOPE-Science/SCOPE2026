"""Independent graph-distance enumeration of the general-position complex of K_{a,b} corona K_1."""
from collections import deque,defaultdict
from itertools import combinations
import json

def build_graph(a,b):
    n=a+b
    adj=[set() for _ in range(2*n)]
    for i in range(a):
        for j in range(a,n):
            adj[i].add(j); adj[j].add(i)
    for i in range(n):
        adj[i].add(n+i); adj[n+i].add(i)
    return adj

def dists(adj):
    distances=[]
    for s in range(len(adj)):
        d=[-1]*len(adj);d[s]=0;q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]<0: d[v]=d[u]+1;q.append(v)
        distances.append(d)
    return distances

def gp_masks(a,b):
    n=a+b; N=2*n
    D=dists(build_graph(a,b))
    bad3=[sum(1<<x for x in tri) for tri in combinations(range(N),3) if any(D[u][w]==D[u][v]+D[v][w] for u,v,w in ((tri[0],tri[1],tri[2]),(tri[0],tri[2],tri[1]),(tri[1],tri[0],tri[2])))]
    gp={0}
    for m in range(1,1<<N):
        # deletion recursion for membership: if first bit deletion not member, cannot member
        lsb=m&-m; sub=m^lsb
        if sub in gp and all(m&bad!=bad for bad in bad3 if (bad&lsb)):
            gp.add(m)
    return gp,len(bad3)

def predicted(a,b):
    n=a+b; N=2*n; faces={0}
    AA=(1<<a)-1;BB=((1<<b)-1)<<a
    A_leaves=AA<<n; B_leaves=BB<<n
    for mask in range(1,1<<N):
        roots=mask&((1<<n)-1); leaves=(mask>>n)&((1<<n)-1)
        rootA=roots&AA; rootB=roots&BB
        paired=roots&leaves
        if paired:
            if mask.bit_count()==2: faces.add(mask)
            continue
        if not roots: faces.add(mask); continue
        if rootA and not rootB:
            if (leaves&BB).bit_count()<=1: faces.add(mask)
            continue
        if rootB and not rootA:
            if (leaves&AA).bit_count()<=1: faces.add(mask)
            continue
        if (roots&AA).bit_count()==1 and (roots&BB).bit_count()==1 and not leaves: faces.add(mask)
    return faces

def rank2(cols):
    basis={}
    for v in cols:
        while v:
            p=v.bit_length()-1
            if p in basis:v ^= basis[p]
            else:basis[p]=v;break
    return len(basis)

def betti(faces):
    by=defaultdict(list)
    for mask in faces:
        if mask:by[mask.bit_count()-1].append(mask)
    dims=sorted(by); ranks={};cnt={d:len(by[d]) for d in dims}
    #  reduced boundary from vertices -> empty face
    for d in dims:
        if d==0: ranks[d]=1 if by[d] else 0;continue
        pos={m:i for i,m in enumerate(by[d-1])}
        cols=[]
        for m in by[d]:
            r=0;u=m
            while u:
                bit=u&-u; u-=bit
                r ^= (1<<pos[m^bit])
            cols.append(r)
        ranks[d]=rank2(cols)
    out={d:cnt[d]-ranks.get(d,0)-ranks.get(d+1,0) for d in dims}
    return {str(d):v for d,v in out.items() if v},cnt,ranks

def main():
    results=[]
    for a,b in [(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)]:
        actual,n_bad=gp_masks(a,b); abstract=predicted(a,b)
        assert actual==abstract, (a,b,len(actual^abstract),list(actual^abstract)[:6])
        reduced,counts,ranks=betti(actual)
        expected={'1':a*b+a+b}
        expected[str(a)]=expected.get(str(a),0)+(b-1)
        expected[str(b)]=expected.get(str(b),0)+(a-1)
        expected={d:v for d,v in expected.items() if v}
        assert reduced==expected,(a,b,reduced,expected)
        record={'a':a,'b':b,'vertices':2*(a+b),'forbidden_triples':n_bad,
                'nonempty_faces':len(actual)-1,'face_vector':counts,
                'mod2_boundary_ranks':ranks,'reduced_mod2_betti':reduced}
        print(json.dumps(record,sort_keys=True))
        results.append(record)
    print('CORONA_GENERAL_POSITION_COMPLETE_INDEPENDENT_ENUMERATION_PASS')
if __name__=='__main__':main()
