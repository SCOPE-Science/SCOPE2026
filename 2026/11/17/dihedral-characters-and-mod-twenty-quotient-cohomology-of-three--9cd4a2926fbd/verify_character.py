"""Exact standalone checks for dihedral characters of four-run-free cycle complexes.
No external dependencies. Finite checks support, but do not replace, the proof.
"""
from math import gcd


def multiply(A, B):
    n=len(A); return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

T=[[1,1,1,1],[-1,0,0,0],[0,-1,0,0],[0,0,-1,0]]
Z=[[int(i==j) for j in range(4)] for i in range(4)]
M=Z
for _ in range(5):M=multiply(T,M)
assert M==[[-int(i==j) for j in range(4)] for i in range(4)]


def signed_path_sum(length, left, right):
    """Weighted strings avoiding four consecutive ones and two endpoint full runs."""
    assert length>=max(left,right)
    states=[0]*4
    # first 'left' bits, reject all-one prefix
    for bits in range(1<<left):
        if bits==(1<<left)-1:continue
        run=0
        for pos in range(left):
            if bits>>pos&1:run+=1
            else:run=0
        states[run]+=(-1)**bits.bit_count()
    for _ in range(left,length):
        states=[sum(states), -states[0], -states[1], -states[2]]
    return sum(states[:right])  # last 'right' all 1 iff run >= right


def W_reflect(n, a):
    if n%2:return signed_path_sum((n+1)//2,3,2)
    if a%2==0:return signed_path_sum(n//2+1,3,3)
    return signed_path_sum(n//2,2,2)


def W_table(n,a):
    # first five lengths in each parity/axis class; five-step antiperiodicity
    if n%2:
        bases={11:-1,13:1,15:0,17:-1,19:1}
        b=11+(n-11)%10
        return bases[b]*(-1)**((n-b)//10)
    bases={12:1,14:-1,16:-1,18:1,20:0}
    b=12+(n-12)%10
    return bases[b]*(-1)**((n-b)//10)* (1 if a%2==0 else -1)


def L(d):
    return (-1)**d * (1-5*int(d%5==0))


def degree(n):
    t,r=divmod(n,5)
    return 3*t-1 if r<=1 else 3*t+r-2


def rank(n):return 4 if n%5==0 else 1


def expected_lefschetz(n,a,reflection):
    return -W_table(n,a) if reflection else L(gcd(n,a))


def valid(n,mask):
    for i in range(n):
        if all(mask&(1<<((i+j)%n)) for j in range(4)):return False
    return True


def independent_lefschetz(n,a,reflection,faces):
    images=([(a-i)%n for i in range(n)] if reflection
            else [(a+i)%n for i in range(n)])
    ans=0
    for mask in faces:
        selected=[i for i in range(n) if mask>>i&1]
        mapped=[images[i] for i in selected]
        if set(mapped)!=set(selected):continue
        inversions=sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
        ans+=(-1)**(len(selected)-1+inversions)
    return ans


def divisors(n):return [d for d in range(1,n+1) if n%d==0]


def phi(n):
    return sum(gcd(k,n)==1 for k in range(n))


def group_invariant_rank(n):
    rotation=sum(phi(n//d)*L(d) for d in divisors(n))
    reflection=sum(-W_table(n,a) for a in range(n))
    numerator=(-1)**degree(n)*(rotation+reflection)
    assert numerator%(2*n)==0,(n,numerator)
    return numerator//(2*n)


if __name__=='__main__':
    for n in range(12,151):
        for a in (0,1):
            assert W_table(n,a)==W_reflect(n,a),(n,a,'fixed-set recurrence')
        expected=(1 if n%20 in (1,7,13,19) else 0)
        assert group_invariant_rank(n)==expected,(n,'invariant')
        assert (-1)**degree(n)*L(n)==rank(n),(n,'identity trace')
    print('TRANSFER_MATRIX_T_FIFTH_EQUALS_MINUS_IDENTITY_PASS')
    print('REFLECTION_PERIODIC_TABLE_AND_ORBIT_INVARIANTS_12_TO_150_PASS')
    counts=0
    for n in range(12,18):
        faces=[mask for mask in range(1<<n) if valid(n,mask)]
        for refl in (False,True):
            for a in range(n):
                actual=independent_lefschetz(n,a,refl,faces)
                expect=expected_lefschetz(n,a,refl)
                assert actual==expect,(n,a,refl,actual,expect)
                counts+=1
        print('DIRECT_SIGNED_SIMPLEX_LEFSCHETZ_PASS',n,len(faces))
    print('ALL_DIHEDRAL_ELEMENTS_INDEPENDENTLY_CHECKED',counts)
    print('CYCLIC_P4_DIHEDRAL_CHARACTER_AND_MOD20_QUOTIENT_PASS')
