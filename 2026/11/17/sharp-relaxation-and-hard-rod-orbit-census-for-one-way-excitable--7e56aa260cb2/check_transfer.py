"""Independent transfer-matrix and time-return checks for directed excitable rings."""
from itertools import product
from math import comb,gcd

def step(x,q):
    return tuple((v+1)%q if v else (x[(j-1)%len(x)]==1) * 1
                 for j,v in enumerate(x))

def count(n,q):
    # Sum cyclic binary pulse choices by hard-rod recurrence, computed as compositions.
    total=1
    for k in range(1,n//q+1):
        total += n*comb(n-(q-1)*k-1,k-1)//k
    return total

def matrix_count(n,q):
    # De Bruijn state for the number of zero slots since the last pulse,
    # saturated at q-1; cyclic transfer trace counts labelled cyclic binary words.
    M=[[0]*q for _ in range(q)]
    for s in range(q):
        M[s][min(q-1,s+1)]+=1
        if s==q-1:M[s][0]+=1
    A=[[int(i==j) for j in range(q)] for i in range(q)]
    for _ in range(n):
        A=[[sum(A[i][k]*M[k][j] for k in range(q)) for j in range(q)] for i in range(q)]
    return sum(A[i][i] for i in range(q))

def test():
    total=0
    for q in range(4,8):
        for n in range(3,31):
            assert matrix_count(n,q)==count(n,q),(n,q,matrix_count(n,q),count(n,q))
            total+=1
        for n in range(3,6):
            for t in range(1,2*n+1):
                direct=0
                for x in product(range(q),repeat=n):
                    y=x
                    for _ in range(t):y=step(y,q)
                    direct+=(y==x)
                assert direct==count(gcd(n,t),q),(q,n,t,direct,count(gcd(n,t),q))
    print('PASS transfer identities:',total)
    print('PASS time-return checks: q=4..7, n=3..5, t=1..2n')
if __name__=='__main__':test()
