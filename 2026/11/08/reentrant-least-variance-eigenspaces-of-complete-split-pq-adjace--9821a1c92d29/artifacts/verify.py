"""Exact vertex-covariance verification for PQ adjacency polytopes of split graphs."""

def make(p,q):
    n=p+q
    pairs=[]
    for i in range(n):
        for j in range(n):
            if i<p or j<p or i==j:
                pairs.append((i,j))
    N=len(pairs)
    assert N==p*p+2*p*q+q
    sums=[0]*(2*n)
    second=[[0]*(2*n) for _ in range(2*n)]
    for i,j in pairs:
        a,b=i,n+j
        sums[a]+=1; sums[b]+=1
        second[a][a]+=1;second[b][b]+=1
        second[a][b]+=1;second[b][a]+=1
    M=[[N*second[i][j]-sums[i]*sums[j] for j in range(2*n)] for i in range(2*n)]
    return M,N

def mul(M,v):
    return [sum(x*y for x,y in zip(row,v)) for row in M]

def run():
    entries=0;count=0
    for p in range(2,10):
        qs=[2,3,4,5,6,9,10,15, p*(p-2)-4,p*(p-2)-3,p*(p-2)-2,p*(p-2)-1]
        for q in sorted(set(q for q in qs if q>=2 and q<80)):
            M,N=make(p,q);n=p+q
            def test(u,sign,num):
                # scaled covariance numerator eigenvalue num (so actual eigenvalue num/N^2)
                v=u+[sign*x for x in u]
                assert mul(M,v)==[num*z for z in v],(p,q,sign,num)
            for i in range(1,p):
                u=[0]*n;u[i]=1;u[0]=-1
                test(u,1,n*N);test(u,-1,n*N)
            for j in range(p+1,n):
                u=[0]*n;u[j]=1;u[p]=-1
                test(u,1,(p+2)*N);test(u,-1,p*N)
            u=[q]*p+[-p]*q
            test(u,1,n*(p*p+2*p+q));test(u,-1,n*N)
            for u in [[1]*n]:
                test(u,1,0);test(u,-1,0)
            g=p*p*q-2*p*p-2*p*q-q*q
            group=n*(p*p+2*p+q)
            assert (group<p*N)==(g>0)
            assert (group==p*N)==(g==0)
            count+=1;entries+=len(M)**2
    print('PQ_SPLIT_COVARIANCE_CHECKS_PASSED',count,'parameter_cases',entries,'matrix_entries')

if __name__=='__main__':run()
