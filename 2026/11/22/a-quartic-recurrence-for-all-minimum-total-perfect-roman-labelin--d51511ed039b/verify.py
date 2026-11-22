"""Exact finite checks for minimum total-perfect-Roman labelings of cycles.
Standard-library only. Run: python3 verify.py
"""
from itertools import product

STATE = [(a, b) for a in range(3) for b in range(3)]
INDEX = {s: i for i,s in enumerate(STATE)}
POTENTIAL = {s: (-2 if s == (0, 2) else 0 if s == (2, 0) else -1) for s in STATE}


def legal(a,b,c):
    if b == 0:
        return (int(a == 2) + int(c == 2)) == 1
    return a > 0 or c > 0


def matmul(A,B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def brute(n):
    result=0
    best=10*n
    for f in product(range(3),repeat=n):
        if all(legal(f[(i-1)%n],f[i],f[(i+1)%n]) for i in range(n)):
            w=sum(f)
            if w<best:best=w;result=1
            elif w==best:result+=1
    return best,result


def main():
    size=len(STATE)
    Z=[[0]*size for _ in range(size)]
    critical=[];full=0
    for a,b,c in product(range(3),repeat=3):
        if not legal(a,b,c):continue
        full+=1
        s=(a,b);t=(b,c)
        red=b-1+POTENTIAL[s]-POTENTIAL[t]
        assert red>=0,(s,t,red)
        if red==0:
            Z[INDEX[s]][INDEX[t]] +=1
            critical.append((s,t))
    assert full==20,(full,critical)
    assert len(critical)==16
    # Newton identities: k*c[k]= -sum_{j=1..k}c[k-j]*trace(Z**j)
    A=[[int(i==j) for j in range(size)] for i in range(size)]
    traces=[0]
    for k in range(1,61):
        A=matmul(A,Z)
        traces.append(trace(A))
    c=[1]
    for k in range(1,size+1):
        v=-sum(c[k-j]*traces[j] for j in range(1,k+1))
        assert v%k==0
        c.append(v//k)
    assert c==[1,-1,0,-2,-1,0,0,0,0,0],c
    for n in range(3,13):
        best,actual=brute(n)
        assert best==n, (n,best)
        assert actual==traces[n],(n,actual,traces[n])
    for n in range(5,61):
        assert traces[n]==traces[n-1]+2*traces[n-3]+traces[n-4]
    assert traces[3:13]==[7,13,16,31,64,109,187,346,628,1111]
    print('CRITICAL_EDGES',len(critical),'DETERMINANT',c)
    print('COUNTS',traces[3:16])
    print('VERIFY_OK')

if __name__=='__main__':main()
