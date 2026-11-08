"""Alternative generation and modular/CRT arborescence audit for weak-order overlap graphs."""
from itertools import product
from math import factorial, prod
from collections import defaultdict, Counter

TARGET_TAU={2:1,3:2,4:37908,5:27571102170646823740986252600397906575360}
TARGET_COUNTS={2:1,3:8,4:113192681472,
5:6214252301172599252248681937277855126085721393995382376959963220030028306692926790213752299261892430397440}

def words(n):
    # Surjective functions from [n] onto [h+1], summed over h.
    return [v for h in range(n) for v in product(range(h+1), repeat=n)
            if len(set(v))==h+1]

def full_graph(n):
    out=defaultdict(list)
    for i,w in enumerate(words(n)):
        out[w[:-1]].append((w[1:],i))
    return out

def matrix(n,reduce):
    out=full_graph(n)
    if reduce:
        vertices=sorted(u for u in out if len(out[u])>1)
    else:
        vertices=sorted(out)
    vi={u:i for i,u in enumerate(vertices)}
    d=[0]*len(vertices)
    adj=[[0]*len(vertices) for _ in vertices]
    for u in vertices:
        for to,label in out[u]:
            d[vi[u]]+=1
            loops=0
            while to not in vi:
                assert reduce and len(out[to])==1
                to=out[to][0][0]
                loops+=1
                assert loops<n
            adj[vi[u]][vi[to]]+=1
    lap=[[((d[i] if i==j else 0)-adj[i][j]) for j in range(len(vertices))]
         for i in range(len(vertices))]
    return vertices, [r[1:] for r in lap[1:]], d

def moddet(a,p):
    b=[[(v%p) for v in row] for row in a]
    m=len(b)
    ans=1
    for i in range(m):
        j=next((j for j in range(i,m) if b[j][i]),None)
        if j is None:return 0
        if j!=i:
            b[i],b[j]=b[j],b[i]
            ans=(-ans)%p
        pivot=b[i][i]
        ans=(ans*pivot)%p
        inv=pow(pivot,-1,p)
        for k in range(i+1,m):
            if not b[k][i]:continue
            mlt=(b[k][i]*inv)%p
            rowk=b[k]
            rowi=b[i]
            for j in range(i+1,m):
                rowk[j]=(rowk[j]-mlt*rowi[j])%p
            rowk[i]=0
    return ans

def primes():
    # Fixed distinct well-known primes near 10^9; primality independently trial-checked.
    return [1000000007,1000000009,998244353,1004535809,1007681537,
            1045430273,1051721729,1053818881,1073479681]

def is_prime(x):
    if x<2:return False
    for d in range(2,int(x**0.5)+1):
        if x%d==0:return False
    return True

def crt_determinant(mat):
    modulus=1;result=0
    for p in primes():
        assert is_prime(p)
        residue=moddet(mat,p)
        t=((residue-result)*pow(modulus,-1,p))%p
        result+=modulus*t
        modulus*=p
    # Row i has L2 norm <= sum_j abs(row_i[j]) <= 2*n_max,
    # so Hadamard ensures the nonnegative determinant < (max norm1)^matrix order.
    bound=prod(sum(abs(x) for x in row) for row in mat)
    assert modulus>bound
    assert 0<=result<=bound
    return result,modulus,bound

def small_direct_euler_circuit_count():
    # Direct permutation of edge IDs, anchored to the unique all-zero word for n=3.
    ww=words(3); edgeid={w:i for i,w in enumerate(ww)}
    start=(0,0,0)
    s=edgeid[start]
    out=full_graph(3)
    cur=start[1:]
    def extend(u,used):
        if used==(1<<len(ww))-1: return int(u==start[:-1])
        return sum(extend(v,used|(1<<i)) for v,i in out[u]
                   if not ((used>>i)&1))
    return extend(cur,1<<s)

if __name__=='__main__':
    assert small_direct_euler_circuit_count()==8
    for n in range(2,6):
        vertices,mat,d=matrix(n,n>=5)
        determinant,modulus,bound=crt_determinant(mat)
        factorials=prod(factorial(deg-1) for deg in d)
        count=determinant*factorials
        assert determinant==TARGET_TAU[n]
        assert count==TARGET_COUNTS[n]
        print('n',n,'matrix',len(mat),'determinant',determinant,
              'Euler_cycles',count,'CRT_modulus_digits',len(str(modulus)),
              'Hadamard_upper_digits',len(str(bound)))
    print('CROSSCHECK_OK')
