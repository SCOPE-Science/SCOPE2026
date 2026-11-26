"""Exact checks for pendant-leaf controllability and its integral-lattice invariant."""


def canonical(edges,n):
    g=[[] for _ in range(n)]
    for u,v in edges:
        g[u].append(v);g[v].append(u)
    alive=set(range(n))
    while len(alive)>2:
        leaves=[u for u in alive if sum(v in alive for v in g[u])<=1]
        if not leaves:
            raise AssertionError('not a tree')
        alive.difference_update(leaves)
    def enc(u,parent):
        return '('+''.join(sorted(enc(v,u) for v in g[u] if v!=parent))+')'
    centers=sorted(alive)
    if len(centers)==1:
        return 'a'+enc(centers[0],-1)
    u,v=centers
    return 'b'+''.join(sorted((enc(u,v),enc(v,u))))

def free_trees(nmax):
    trees={1:[()]}
    for n in range(2,nmax+1):
        uniq={}
        for old in trees[n-1]:
            for u in range(n-1):
                edges=old+((u,n-1),)
                uniq.setdefault(canonical(edges,n),edges)
        trees[n]=list(uniq.values())
    return trees

def det_bareiss(M):
    A=[list(map(int,row)) for row in M]
    n=len(A);sign=1;prev=1
    if n==1:return A[0][0]
    for k in range(n-1):
        if not A[k][k]:
            swap=next((r for r in range(k+1,n) if A[r][k]),None)
            if swap is None:return 0
            A[k],A[swap]=A[swap],A[k];sign=-sign
        piv=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                q,rem=divmod(A[i][j]*piv-A[i][k]*A[k][j],prev)
                assert rem==0
                A[i][j]=q
        for i in range(k+1,n): A[i][k]=0
        prev=piv
    return sign*A[-1][-1]

def kalman_det(edges,n,r):
    L=[[0]*n for _ in range(n)]
    for u,v in edges:
        L[u][u]+=1;L[v][v]+=1;L[u][v]-=1;L[v][u]-=1
    col=[int(i==r) for i in range(n)]
    K=[[0]*n for _ in range(n)]
    for j in range(n):
        for i in range(n):K[i][j]=col[i]
        col=[sum(L[i][k]*col[k] for k in range(n)) for i in range(n)]
    return det_bareiss(K)

def run():
    alltrees=free_trees(9)
    known=[0,1,1,1,2,3,6,11,23,47]
    assert [len(alltrees[n]) for n in range(1,10)]==known[1:]
    count={};nonunit=[]
    for n in range(1,10):
        count[n]=[0,0,0]
        for edges in alltrees[n]:
            for root in range(n):
                v=abs(kalman_det(edges,n,root))
                if v==0:count[n][0]+=1
                elif v==1:count[n][1]+=1
                else:
                    count[n][2]+=1
                    nonunit.append((n,edges,root,v))
    assert not any(x[2] for n,x in count.items() if n<=8)
    print('tree_types',{n:len(alltrees[n]) for n in range(1,10)})
    print('rooted_input_counts_zero_unit_nonunit',count)
    print('nonunit_witnesses_n9',nonunit)
    example=nonunit[0]
    n,E,root,value=example
    assert n==9 and value==2
    # For all rooted trees on <=8, adjoining unit leaf at input preserves absolute determinant.
    leafchecks=0
    for n in range(1,9):
        for E0 in alltrees[n]:
            for r in range(n):
                old=abs(kalman_det(E0,n,r))
                new=abs(kalman_det(E0+((r,n),),n+1,n))
                assert old==new,(n,E0,r,old,new)
                leafchecks+=1
    # Construct an arbitrary-size tree by repeatedly appending a leaf at the current controlled vertex.
    G=E; r=root
    for m in range(9,17):
        assert abs(kalman_det(G,m,r))==2
        G=G+((r,m),);r=m
    # The two nonunit roots satisfy a precise parity obstruction on integer targets.
    def matrix_for(edges,n,root):
        L=[[0]*n for _ in range(n)]
        for u,v in edges:
            L[u][u]+=1;L[v][v]+=1;L[u][v]-=1;L[v][u]-=1
        k=[[0]*n for _ in range(n)];v=[int(i==root) for i in range(n)]
        for j in range(n):
            for i in range(n): k[i][j]=v[i]
            v=[sum(L[i][a]*v[a] for a in range(n)) for i in range(n)]
        return k
    witness=matrix_for(E,9,root)
    assert all(sum(witness[i][j] for i in (0,5,6,7))%2==0 for j in range(9))
    assert abs(det_bareiss(witness))==2
    assert abs(kalman_det(E,9,6))==1
    # Check the block-level polynomial identity for several integer leaf weights.
    def extension_certificate(edges,n,root,t):
        old=matrix_for(edges,n,root)
        oe=edges+((root,n),)
        N=n+1
        M=[[0]*N for _ in range(N)]
        for u,v in edges:
            M[u][u]+=1;M[v][v]+=1;M[u][v]-=1;M[v][u]-=1
        M[root][root]+=t;M[n][n]+=t;M[root][n]-=t;M[n][root]-=t
        v=[0]*n+[1]
        vals=[];cols=[]
        for j in range(N):
            vals.append(v[-1]);cols.append(v[:n])
            v=[sum(M[i][a]*v[a] for a in range(N)) for i in range(N)]
        assert vals[0]==1 and vals[1]==t
        assert all(z%t==0 for z in vals[1:])
        # The top block of the new Kalman matrix is -t times old K times U.
        # U is upper-unitriangular over the integers.
        U=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                U[i][j]=vals[j-i+1]//t
        assert all(U[i][i]==1 for i in range(n))
        for i in range(n):
            for j in range(n):
                assert cols[j+1][i]==-t*sum(old[i][a]*U[a][j] for a in range(n))
    for n in range(1,7):
        for E0 in alltrees[n]:
            for r in range(n):
                for w in (1,2,3):extension_certificate(E0,n,r,w)
    print('VERIFY_OK tree_types_1_through_9=95 rooted_cases='+str(sum(n*len(alltrees[n]) for n in range(1,10)))+' leaf_invariance_tests='+str(leafchecks)+' nonunit_min_size=9 magnitude=2 lattice_parity=verified')

if __name__=='__main__':run()
