"""Independent GF(2) matrix-rank check for one directed arc toggled on Q_d.
Run: python check_rank.py. No nonstandard modules required.
"""

def rank(rows, n):
    basis = {}
    for x in rows:
        y = x
        while y:
            p = y.bit_length() - 1
            if p in basis:
                y ^= basis[p]
            else:
                basis[p] = y
                break
    return len(basis)

def compose(A, B):
    out = []
    for a in A:
        r = 0
        while a:
            lb = a & -a
            r ^= B[lb.bit_length()-1]
            a ^= lb
        out.append(r)
    return out

def identity(m):
    return [1 << i for i in range(m)]

def cube(d):
    m = 1 << d
    return [sum(1 << (i ^ (1 << j)) for j in range(d)) for i in range(m)]

def checker(d, distance):
    m = 1 << d; r = m//2
    v = (1 << distance)-1; u=0
    A = cube(d)
    A[u] ^= 1 << v
    H = [a ^ ((d&1)<<i) for i,a in enumerate(A)]
    powers = [identity(m)]
    for _ in range(5):
        powers.append(compose(powers[-1], H))
    ranks = [rank(a, m) for a in powers]
    expected = [m,r+1,2,2,2,2] if distance == 1 else [m,r+1,2,1,0,0]
    assert ranks==expected,(d,distance,ranks,expected)
    # Compare the dynamical update against its derived relation, not only a rank.
    F2=compose(A,A); F4=compose(F2,F2)
    if d%2==0:
        assert F4 == F2 if distance==1 else F4 == [0]*m
    else:
        if distance>1: assert F4 == identity(m)
        else: assert F4 == F2
    return (d,distance,ranks)

if __name__=='__main__':
    total=0
    for d in range(2,8):
        for distance in range(1,d+1):
            d0,dis,rks=checker(d,distance)
            print('dimension=%d distance=%d ranks(H+E)^0..5=%s' %(d0,dis,','.join(map(str,rks))))
            total+=1
    print('PASS: %d complete GF(2) rank-filtration and power-identity cases' % total)
