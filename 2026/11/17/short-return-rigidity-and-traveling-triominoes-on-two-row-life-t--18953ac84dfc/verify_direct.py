"""Independent direct cell-by-cell checks for periodic two-row Life."""

def update(rows):
    n = len(rows[0]); out=[[0]*n for _ in range(2)]
    for y in (0,1):
        for x in range(n):
            neighbors=0
            for dy in (-1,0,1):
                for dx in (-1,0,1):
                    if dx==0 and dy==0:continue
                    neighbors += rows[(y+dy)%2][(x+dx)%n]
            out[y][x] = int(neighbors==3 or (rows[y][x]==1 and neighbors==2))
    return out

def from_int(v,n):
    return [[(v>>(y*n+x))&1 for x in range(n)] for y in (0,1)]

def lucas(n):
    if n==0:return 2
    p,q=2,1
    for k in range(2,n+1):p,q=q,p+q
    return q

phase = (2,1,-1,-2,-1,1)
for n in range(3,9):
    fixed=two=0
    for v in range(1<<(2*n)):
        a=from_int(v,n);b=update(a)
        if b==a:fixed+=1
        if update(b)==a:two+=1
    predicted=lucas(n)+2+(-1)**n+phase[n%6]
    assert fixed==predicted,(n,fixed,predicted)
    assert two==fixed + (12 if n%4==0 else 0),(n,two,fixed)
    print('n=%d fixed=%d fixed_after_two=%d'%(n,fixed,two))
for n in range(5,31):
    a=from_int(0,n)
    a[0][0]=a[0][1]=a[1][0]=1
    b=update(a);c=update(b)
    target=from_int(0,n)
    target[0][(n-2)%n]=target[0][(n-1)%n]=target[1][(n-2)%n]=1
    assert c==target,(n,'two-step translation')
    assert sum(map(sum,a))==3 and sum(map(sum,b))==4
    k=n//__import__('math').gcd(n,2)
    state=a
    for t in range(1,2*k+1):
        state=update(state)
        assert (state!=a)==(t<2*k),(n,t)
print('PASS: all direct exhaustive comparisons and glider periods n=5,...,30')
