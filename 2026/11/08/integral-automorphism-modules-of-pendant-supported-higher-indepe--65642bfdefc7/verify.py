"""Independent finite checks of a higher-independence homology character.

Run using Python 3: python verify.py. No third-party dependencies.
All complex faces are reconstructed by connected-component breadth-first search.
"""
from itertools import permutations, combinations
from math import comb


def graph(core_edges, leaf_counts):
    n=len(leaf_counts)
    leaves=[];adj=[set() for _ in range(n+sum(leaf_counts))]
    for u,v in core_edges:
        adj[u].add(v);adj[v].add(u)
    for i,l in enumerate(leaf_counts):
        new=[]
        for _ in range(l):
            j=n+len(leaves)
            adj[i].add(j);adj[j].add(i)
            leaves.append(j);new.append(j)
    return adj


def r_ind_faces(adj,r):
    N=len(adj); ans=[]
    for mask in range(1<<N):
        remaining={i for i in range(N) if mask>>i&1};ok=True
        while remaining:
            u=remaining.pop(); count=1;todo=[u]
            while todo:
                v=todo.pop()
                for w in adj[v]:
                    if w in remaining:
                        remaining.remove(w);todo.append(w);count+=1
            if count>r:
                ok=False;break
        if ok:ans.append(mask)
    return ans


def invert_sign(a):
    return -1 if sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))%2 else 1


def lefschetz(faces,p):
    total=0
    for mask in faces:
        if not mask:continue
        face=[i for i in range(len(p)) if mask>>i&1]
        action=[p[i] for i in face]
        if set(action)==set(face):total+=(-1)**(len(face)-1)*invert_sign(action)
    return total


def exterior_aug_character(leaf_perm,k):
    # det(I+tP) / (1+t), evaluated exactly in Z[t].
    N=len(leaf_perm); seen=set();pol=[1]
    for i in range(N):
        if i in seen:continue
        j=i;s=0
        while j not in seen:
            seen.add(j);s+=1;j=leaf_perm[j]
        nxt=pol+[0]*s
        for h,c in enumerate(pol):nxt[h+s]-=(-1)**s*c
        pol=nxt
    if k>N-1:return 0
    return sum((-1)**i*pol[k-i] for i in range(k+1) if k-i<len(pol))


def rank_mod2(cols):
    pivots={}
    for c in cols:
        while c:
            pos=c.bit_length()-1
            if pos in pivots:c^=pivots[pos]
            else:pivots[pos]=c;break
    return len(pivots)


def reduced_betti_mod2(faces,n):
    by_deg=[[m for m in faces if m.bit_count()==j+1] for j in range(n)]
    ranks=[0]*(n+1)
    for j in range(1,n):
        index={m:i for i,m in enumerate(by_deg[j-1])}
        cols=[]
        for mask in by_deg[j]:
            col=0
            for i in range(n):
                if mask>>i&1:col|=1<<index[mask^(1<<i)]
            cols.append(col)
        ranks[j]=rank_mod2(cols)
    betti=[len(by_deg[j])-ranks[j]-ranks[j+1] for j in range(n)]
    betti[0]-=1
    return betti


def actions(core_edges, leaf_counts):
    n=len(leaf_counts);L=sum(leaf_counts); core_edges={frozenset(e) for e in core_edges}
    blocks=[];o=n
    for l in leaf_counts:blocks.append(list(range(o,o+l)));o+=l
    result=[]
    for q in permutations(range(n)):
        if any(leaf_counts[i]!=leaf_counts[q[i]] for i in range(n)):continue
        if {frozenset([q[u],q[v]]) for u,v in core_edges}!=core_edges:continue
        p=list(range(n+L));p[:n]=q
        for i in range(n):
            for x,y in zip(blocks[i],blocks[q[i]]):p[x]=y
        result.append((f'core_{q}',p))
    for i,l in enumerate(leaf_counts):
        if l>1:
            for typ in ['cycle','swap']:
                p=list(range(n+L));a=blocks[i]
                if typ=='cycle':
                    for j,x in enumerate(a):p[x]=a[(j+1)%l]
                else:p[a[0]],p[a[1]]=a[1],a[0]
                result.append((f'leaf_{i}_{typ}',p))
    return result


def check(name,edges,counts):
    n=len(counts);L=sum(counts);total=n+L
    adj=graph(edges,counts)
    expected_cone=0; tests=0
    for r in range(1,total+2):
        F=r_ind_faces(adj,r)
        # Every nonempty deleted-core intersection has an isolated leaf.
        face_set=set(F)
        for nonzero in range(1,1<<n):
            free=[n+sum(counts[:i]) for i in range(n) if nonzero>>i&1][0]
            for f in F:
                if not any(f>>i&1 for i in range(n) if nonzero>>i&1):
                    assert (f|(1<<free)) in face_set,(name,'noncone',r,nonzero,f)
            expected_cone+=1
        Betti=reduced_betti_mod2(F,total)
        degree=r-1
        expected=comb(L-1,r-n) if n<=r<=n+L-1 else 0
        assert all((i==degree and value==expected) or (i!=degree and value==0) for i,value in enumerate(Betti)),(name,r,Betti,expected)
        tests+=1
        for label,p in actions(edges,counts):
            k=r-n
            predicted=(invert_sign(p[:n])*exterior_aug_character([p[n+i]-n for i in range(L)],k)) if 0<=k<=L-1 else 0
            actual=(-1)**degree*(lefschetz(F,p)-1)
            assert predicted==actual,(name,r,label,predicted,actual)
            tests+=1
    return tests,expected_cone


if __name__=='__main__':
    profiles=[
        ('star-4',[],[4]),
        ('edge-2-2',[(0,1)],[2,2]),
        ('edge-1-3',[(0,1)],[1,3]),
        ('path3',[(0,1),(1,2)],[1,2,1]),
        ('path3-symmetric',[(0,1),(1,2)],[2,1,2]),
        ('triangle',[(0,1),(1,2),(2,0)],[1,1,1]),
        ('triangle-2',[(0,1),(1,2),(2,0)],[2,1,2]),
        ('path4',[(0,1),(1,2),(2,3)],[1,1,1,1]),
        ('cycle4',[(0,1),(1,2),(2,3),(3,0)],[1,1,1,1]),
        ('complete4',list(combinations(range(4),2)),[1,1,1,1]),
        ('claw-core',[(0,1),(0,2),(0,3)],[1,1,1,1]),
    ]
    total=0;cones=0
    for name,E,counts in profiles:
        trials,cone=check(name,E,counts)
        print(f'{name}: {trials} homology / character checks, {cone} deletion-cone checks')
        total+=trials;cones+=cone
    print('ALL_VERIFY_OK', 'tests=',total,'cone_checks=',cones)
