"""Independent exact finite-size checks of the zero-temperature staircase.
Run with Python 3.8+; no third-party modules required.
"""

def graph(n):
    vertices = [(i,j) for i in range(n) for j in range(n) if i!=j]
    address = {v: k for k,v in enumerate(vertices)}
    edges = []
    for i in range(n):
        row = [address[i,j] for j in range(n) if j!=i]
        edges += [(row[a],row[b]) for a in range(len(row)) for b in range(a+1,len(row))]
    edges += [(address[i,j], address[j,i]) for i in range(n) for j in range(i+1,n)]
    return vertices, edges


def sector_data(n):
    vertices,edges=graph(n)
    N=len(vertices)
    assert N <= 20
    adj=[0]*N
    for i,j in edges:
        adj[i] |= 1<<j
        adj[j] |= 1<<i
    degree=[a.bit_count() for a in adj]
    cuts=[0]*(1<<N)
    best={}
    for mask in range(1<<N):
        if mask:
            bit=mask & -mask
            i=bit.bit_length()-1
            prev=mask^bit
            cuts[mask]=cuts[prev]+degree[i]-2*(adj[i]&prev).bit_count()
        M=N-2*mask.bit_count()
        c=cuts[mask]
        if M not in best or c>best[M][0]:best[M]=(c,1)
        elif c==best[M][0]:best[M]=(c,best[M][1]+1)
    return len(edges),best


def expected_energy(n,x):
    k_vals=list(range((n-1)%2,n,2))
    energies=[n*(k*k/2+(1-x)*k-(n-1)) for k in k_vals]
    if n%2==0:energies.append(n/2-n*(n-1))
    return min(energies)


def expected_unique_mag(n,x):
    N=n*(n-1)
    if n%2==0 and x<1:return 0
    k_vals=list(range((n-1)%2,n,2))
    return n*min(k_vals,key=lambda k:(k-(x-1))**2)


def check():
    checks=0
    for n in (3,4,5):
        edge_count,sector=sector_data(n)
        N=n*(n-1)
        assert edge_count==n*(n-1)**2//2
        for x2 in range(0,2*(n+2)+1):
            x=x2/2
            energies={M:edge_count-2*c-x*M for M,(c,_) in sector.items()}
            e_min=min(energies.values())
            winners=[M for M,v in energies.items() if abs(v-e_min)<1e-9]
            assert abs(e_min-expected_energy(n,x))<1e-9, (n,x,e_min)
            critical=([1]+list(range(3,n,2))) if n%2==0 else list(range(2,n,2))
            if x not in critical:
                assert winners==[expected_unique_mag(n,x)], (n,x,winners)
            checks+=2
        if n==4:
            assert sector[0][1]==24 and sector[4][1]==30 and sector[12][1]==1
            checks+=1
        if n==5:
            assert sector[0][1]==24 and sector[10][1]==444 and sector[20][1]==1
            checks+=1
    print(f'PASS: {checks} finite energy/magnetization/degeneracy assertions; exhaustive n=3,4,5')

if __name__=='__main__':check()
