from math import factorial

def vp(n,p):
    c=0
    while n and n%p==0:
        c+=1
        n//=p
    return c

def digit_sum(n,p):
    s=0
    while n:
        s += n%p
        n//=p
    return s

def primes_upto(n):
    out=[]
    for x in range(2,n+1):
        if all(x%q for q in out if q*q<=x):
            out.append(x)
    return out

def stirling2(n,k):
    if n==0:
        return 1 if k==0 else 0
    if k==0:
        return 0
    a=[[0]*(k+1) for _ in range(n+1)]
    a[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            a[i][j]=a[i-1][j-1]+j*a[i-1][j]
    return a[n][k]

def partitions(n, minpart=1):
    # nondecreasing positive integer partitions
    def rec(rem, lo, cur):
        if rem==0:
            yield tuple(cur)
            return
        for x in range(lo, rem+1):
            cur.append(x)
            yield from rec(rem-x, x, cur)
            cur.pop()
    yield from rec(n,minpart,[])

def carry_free(parts,p):
    total=sum(parts)
    maxd=1
    z=total
    while z>=p:
        z//=p; maxd+=1
    for pos in range(maxd+2):
        place=p**pos
        if sum((x//place)%p for x in parts) >= p:
            return False
    return sum(parts)==total and sum(digit_sum(x,p) for x in parts)==digit_sum(total,p)

checked=0
parity_cells={}
for N in range(1,37):
    for parts in partitions(N):
        r=len(parts)
        D=factorial(N+1)
        for x in parts:
            D//=factorial(x)
        assert D == (N+1)*factorial(N)//__import__('math').prod(factorial(x) for x in parts)
        for p in primes_upto(N+1):
            rhs=vp(N+1,p)+(sum(digit_sum(x,p) for x in parts)-digit_sum(N,p))//(p-1)
            assert vp(D,p)==rhs,(N,parts,p,D,vp(D,p),rhs)
            assert (D%p!=0) == (N%p != p-1 and carry_free(parts,p))
        parity_cells[(N,r)] = parity_cells.get((N,r),0) + (D%2)
        checked += 1

for N in range(1,37):
    s=digit_sum(N,2)
    for r in range(1,N+1):
        got=parity_cells.get((N,r),0)
        want=stirling2(s,r) if N%2==0 else 0
        assert got==want,(N,r,got,want,s)

# Named calibration examples.
def degree(parts):
    N=sum(parts)
    D=factorial(N+1)
    for x in parts:
        D//=factorial(x)
    return D
assert degree((1,1))==6
assert degree((2,4))==105
assert degree((2,12))%2==1
assert degree((4,10))%2==1
assert degree((6,8))%2==1
assert degree((2,4,8))%2==1
print('VERIFY_OK', checked, len(parity_cells))
