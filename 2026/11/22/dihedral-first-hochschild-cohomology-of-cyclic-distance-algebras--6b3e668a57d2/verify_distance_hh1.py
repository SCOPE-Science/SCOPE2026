"""Standalone finite checks for first Hochschild cohomology of cycle distance algebras.

Run: python verify_distance_hh1.py
Only finite cases are checked; the all-length theorem requires its written proof.
"""
from random import Random


def rank_mod(mat, p, cols):
    a = [[x % p for x in row] for row in mat]
    r = 0
    for j in range(cols):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = pow(a[r][j], -1, p)
        a[r] = [(x * scale) % p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][j]:
                v = a[i][j]
                a[i] = [(x - v * y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def constraint_rows(n):
    if n % 2:
        return []
    m = n // 2
    ans = []
    for x in range(n):
        row = [0] * (2 * n)
        for j in range(m):
            row[(x+j) % n] += 1
            row[n+(x-j-1) % n] -= 1
        ans.append(row)
    return ans


def gradients(n):
    rows = []
    for j in range(n-1):
        row = [0] * (2*n)
        row[j] = 1
        row[(j-1) % n] -= 1
        row[n+j] -= 1
        row[n+(j-1) % n] += 1
        rows.append(row)
    return rows


def oriented_sum(x, y, a, b, n):
    f = (y-x) % n
    rev = (x-y) % n
    if f <= rev:
        return sum(a[(x+j) % n] for j in range(f))
    return sum(b[(x-j-1) % n] for j in range(rev))


def distance(x,y,n):
    z = (y-x) % n
    return min(z,n-z)


def derivation_law(n,a,b,p):
    val={(x,y):oriented_sum(x,y,a,b,n)%p for x in range(n) for y in range(n)}
    for x in range(n):
        for y in range(n):
            for z in range(n):
                product=(distance(x,z,n)==distance(x,y,n)+distance(y,z,n))
                lhs=val[x,z] if product else 0
                rhs=(val[x,y]+val[y,z])%p if product else 0
                assert lhs==rhs, (n,p,x,y,z)
    return True


def build_cocycle(n,p,rng):
    a=[rng.randrange(p) for _ in range(n)]
    if n%2:
        b=[rng.randrange(p) for _ in range(n)]
    else:
        m=n//2
        halves=[rng.randrange(p) for _ in range(m)]
        s=halves+halves
        a[-1]=(sum(halves)-sum(a[:-1]))%p
        b=[(s[i]-a[i])%p for i in range(n)]
    return a,b


def reflect(a,b,n):
    # Reflection of vertices i -> -i, thus arcs i -> i+1 map to
    # reverse arcs indexed -i-1.
    aa=[0]*n;bb=[0]*n
    for i in range(n):
        j=(-i-1)%n
        aa[j]=b[i]
        bb[j]=a[i]
    return aa,bb


def rotate(a,b,n):
    aa=[0]*n;bb=[0]*n
    for i in range(n):
        aa[(i+1)%n]=a[i];bb[(i+1)%n]=b[i]
    return aa,bb


def main():
    rng=Random(772909)
    tally=0
    for n in range(3,17):
        rows=constraint_rows(n)
        for p in (2,3,5,7):
            rc=rank_mod(rows,p,2*n)
            rb=rank_mod(gradients(n),p,2*n)
            assert rb==n-1
            assert rc==(0 if n%2 else n//2+1)
            dim=2*n-rc-rb
            assert dim==(n+1 if n%2 else n//2),(n,p,dim)
            for _ in range(4):
                a,b=build_cocycle(n,p,rng)
                assert derivation_law(n,a,b,p)
                ar,br=rotate(a,b,n)
                af,bf=reflect(a,b,n)
                assert derivation_law(n,ar,br,p)
                assert derivation_law(n,af,bf,p)
                if not n%2:
                    s=[(a[i]+b[i])%p for i in range(n)]
                    assert all(s[i]==s[i+n//2] for i in range(n//2))
                    assert [(ar[i]+br[i])%p for i in range(n)]==[s[(i-1)%n] for i in range(n)]
                    assert [(af[i]+bf[i])%p for i in range(n)]==[s[(-i-1)%n] for i in range(n)]
                tally+=1
            if n%2 and p==2:
                # The unique edge fixed by reflection i -> -i is (n-1)/2.
                e=(n-1)//2
                a=[0]*n;b=[0]*n;b[e]=1
                af,bf=reflect(a,b,n)
                kernel_a=[(a[i]+af[i])%2 for i in range(n)]
                kernel_b=[(b[i]+bf[i])%2 for i in range(n)]
                assert all((kernel_a[i]+kernel_b[i])%2==0 for i in range(n))
                assert sum(kernel_a)%2==1 # Not a gradient; no invariant lift.
    # Explicit test of a reflection-equivariant section in odd characteristic.
    for n in (3,5,7,9):
        for p in (3,5,7):
            s=[(3*i+1)%p for i in range(n)]
            c=pow(2,-1,p)
            a=[c*t%p for t in s]; b=a[:]
            ar,br=rotate(a,b,n);af,bf=reflect(a,b,n)
            assert ar==br and af==bf
            assert derivation_law(n,a,b,p)
    print('CYCLE_DISTANCE_HH1_DIHEDRAL_CHECKS_OK')
    print('finite cyclic orders: 3..16; fields: F2,F3,F5,F7')
    print('random geodesic cocycles and multiplication triples checked:',tally)
    print('rank checks, rotational/reflection equivariance and mod-2 nonsplitting passed')

if __name__=='__main__':
    main()
