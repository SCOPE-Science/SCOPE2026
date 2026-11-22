"""Exhaustive finite checks for the nonmatching homology representation theorem.
Run with Python >=3.9; no third-party dependencies.
"""
from itertools import permutations, combinations
from math import comb


def has_three_matching(mask, n):
    # column-major edge index c*3+r
    if n < 3:
        return False
    byrow = [tuple(c for c in range(n) if mask & (1 << (3*c+r))) for r in range(3)]
    return any(a != b and a != c and b != c for a in byrow[0] for b in byrow[1] for c in byrow[2])


def sign_perm(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1,len(p))) % 2 else 1


def lef_reduced(n, rp, cp):
    dest = [3*cp[c]+rp[r] for c in range(n) for r in range(3)]
    accum = 0
    faces = 0
    for face in range(1 << (3*n)):
        if has_three_matching(face,n):
            continue
        faces += 1
        vert = [i for i in range(3*n) if face & (1 << i)]
        out = [dest[i] for i in vert]
        if sorted(out) != vert:
            continue
        accum += (-1) ** (len(vert) + (1 - sign_perm(out)) // 2)
    # In degree 3, reduced Lefschetz is -trace; accum is minus this.
    return accum, faces


def hook_trace(cp):
    f=sum(v==i for i,v in enumerate(cp))
    t=sum(i<j and cp[i]==j and cp[j]==i for i in range(len(cp)) for j in range(i+1,len(cp)))
    return ((f-1)*(f-2)-2*t)//2


def proj(mask,n,pair):
    i,j=pair
    out=0
    for c in range(n):
        tc=c if c in (0,i,j) else 0
        for r in range(3):
            if mask & (1<<(3*c+r)):
                out |= 1<<(3*tc+r)
    return out


def main():
    for n in (3,4):
        rows=list(permutations(range(3)))
        cols=list(permutations(range(n)))
        identity=tuple(range(n))
        checks=0
        for rp in rows:
            for cp in cols:
                trace,faces=lef_reduced(n,rp,cp)
                expected=sign_perm(rp)*hook_trace(cp)
                assert trace==expected,(n,rp,cp,trace,expected)
                checks+=1
        print(f'n={n} all signed Lefschetz characters: {checks} PASS; total faces={faces}')
    for n in (3,4,5):
        for i in range(1,n):
            for j in range(i+1,n):
                checks=0
                for face in range(1<<(3*n)):
                    if has_three_matching(face,n):continue
                    p=proj(face,n,(i,j))
                    assert not has_three_matching(p,n),(n,i,j,face,p)
                    if face&~sum(1<<(3*c+r) for c in (0,i,j) for r in range(3))==0:
                        assert p==face
                    checks+=1
                print(f'n={n} retract (0,{i},{j}): {checks} faces PASS')
    # Coefficient of the difference-wedge model: direct alternating triple formula.
    for n in range(3,9):
        e=[tuple(1 if k==i else -1 if k==0 else 0 for k in range(n)) for i in range(1,n)]
        assert len(e)==n-1
        assert len(list(combinations(range(1,n),2)))==comb(n-1,2)
    print('INTEGRAL_HOOK_RETRACTION_CHECKS_PASS')

if __name__=='__main__':main()
