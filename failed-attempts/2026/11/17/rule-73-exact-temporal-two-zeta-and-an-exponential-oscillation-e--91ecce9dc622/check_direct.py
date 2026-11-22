"""Independent bit-level exhaustive test of the Rule 73 period-one/two zeta formulas."""

# Coefficients in ascending powers of z, including constant term.
D1 = [1,0,0,-1,-1]  # det(I-z B)

def multiply(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

D2 = multiply(multiply(multiply([1,-1],[1,-1]),multiply([1,0,1],[1,0,1])),[1,0,-2,-1,1])

def predicted(D,N):
    # -zD'(z)/D(z) generates traces of powers of the adjacency matrix.
    a=[0]*(N+1)
    for n in range(1,N+1):
        rhs=-n*(D[n] if n<len(D) else 0)
        for j in range(1,min(n,len(D)-1)+1):rhs-=D[j]*a[n-j]
        a[n]=rhs
    return a

# This update is coded directly from the positions of the three 1 bits in 73=2^0+2^3+2^6,
# without use of the graph-construction routine.
def update(word,n):
    out=0
    for i in range(n):
        triple= 4*((word>>((i-1)%n))&1) +2*((word>>i)&1) + ((word>>((i+1)%n))&1)
        if triple in (0,3,6):out|=1<<i
    return out

p1=predicted(D1,18)
p2=predicted(D2,18)
for n in range(1,19):
    fixed=twice=0
    for w in range(1<<n):
        y=update(w,n)
        if y==w:fixed+=1
        if update(y,n)==w:twice+=1
    assert (fixed,twice)==(p1[n],p2[n]),(n,fixed,twice,p1[n],p2[n])
    assert (twice-fixed)%2==0
print('BRUTE_OK n=1..18; total states=',sum(1<<n for n in range(1,19)))
print('n=5 fixed / two-period / primitive orbits =',p1[5],p2[5],(p2[5]-p1[5])//2)
print('n=18 fixed / two-period / primitive orbits =',p1[18],p2[18],(p2[18]-p1[18])//2)
