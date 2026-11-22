"""Independent GF(2) matrix-rank verification of an edge-defective biclique theorem.
Usage: python3 verify_ranks.py. Only the Python standard library is needed.
"""

def matrix(m,n,deleted):
    N=m+n
    cols=[]
    for j in range(N):
        c=0
        for i in range(N):
            if (i<m)!=(j<m) and (not deleted or set((i,j)) != set((0,m))):
                c |= 1<<i
        cols.append(c)
    return cols

def product(a,b):
    return [sum_columns(a,v) for v in b]

def sum_columns(a,mask):
    x=0
    while mask:
        b=mask&-mask
        x ^= a[b.bit_length()-1]
        mask ^= b
    return x

def rank(a):
    piv={}
    for w in a:
        while w:
            b=w.bit_length()-1
            if b in piv:w ^= piv[b]
            else:piv[b]=w;break
    return len(piv)

def identity(N):return [1<<j for j in range(N)]

def ranks(a,upto=7):
    p=identity(len(a)); out=[]
    for k in range(upto+1):
        out.append(rank(p));p=product(a,p)
    return out

def theory(m,n):
    N=m+n
    if m%2==n%2==0:return [N]+[4]*7
    if m%2==n%2==1:return [N,4,2]+[0]*5
    return [N,4,3]+[2]*5

def run():
    checks=0
    for m in range(2,17):
        for n in range(2,17):
            A=matrix(m,n,True)
            assert ranks(A)==theory(m,n),(m,n,ranks(A),theory(m,n))
            r=ranks(matrix(m,n,False),3)
            if m%2 and n%2:
                assert r==[m+n,2,2,2],(m,n,r)
            elif m%2==0 and n%2==0:
                assert r==[m+n,2,0,0],(m,n,r)
            else:
                assert r==[m+n,2,1,0],(m,n,r)
            # Global matrix identities, not just ranks.
            N=m+n; powers=[identity(N)]
            for k in range(9):powers.append(product(A,powers[-1]))
            if m%2==n%2==0:
                assert powers[7]==powers[1] and powers[4]!=powers[1]
            elif m%2==n%2==1:
                assert powers[3]==[0]*N and powers[2]!=[0]*N
            else:
                assert powers[5]==powers[3] and powers[4]!=powers[3]
            checks+=1
    print('RANK_AND_MATRIX_IDENTITY_CHECKS_PASSED',checks)

if __name__=='__main__':run()
