"""Dependency-free checks for the sharp bispectral spectral-erasure theorem.

The universal character-extension proof is mathematical, not computational;
these finite checks validate its sharpness construction and small instances.
"""
import cmath
import itertools
import math

S = {0, 1, 3, 4, 5, 7}
N = 8
exponent = {0: 0, 1: 1, 3: -1, 4: 0, 5: 1, 7: -1}
triples = set()
checks = 0
for a, b, c in itertools.product(S, repeat=3):
    if (a + b + c) % N == 0:
        triples.add(tuple(sorted((a, b, c))))
        assert exponent[a] + exponent[b] + exponent[c] == 0
        checks += 1
assert triples == {(0, 0, 0), (0, 1, 7), (0, 3, 5),
                   (0, 4, 4), (1, 3, 4), (4, 5, 7)}
checks += 1
z = cmath.exp(1j * math.pi / 5)
F = [6 if k == 0 else (1 if k in S else 0) for k in range(N)]
B = [F[k] * z ** exponent[k] if k in S else 0 for k in range(N)]
for k in range(N):
    assert abs(F[(-k) % N] - complex(F[k]).conjugate()) < 1e-12
    assert abs(B[(-k) % N] - B[k].conjugate()) < 1e-12
    checks += 2

def inverse(Fcoef):
    return [sum(Fcoef[k] * cmath.exp(2j * math.pi * k * x / N)
                for k in range(N)).real / N for x in range(N)]

f = inverse(F)
g = inverse(B)
assert min(f) > 1 / 8 - 1e-12 and min(g) > 1 / 8 - 1e-12
checks += 1

def correlation(v, order, shift):
    return sum(math.prod(v[(x + u) % N] for u in ((0,) + shift))
               for x in range(N))

assert abs(sum(f) - sum(g)) < 1e-10
checks += 1
for j in range(2, 4):
    for shift in itertools.product(range(N), repeat=j-1):
        assert abs(correlation(f, j, shift) - correlation(g, j, shift)) < 1e-9
        checks += 1
for t in range(N):
    assert max(abs(g[x] - f[(x+t) % N]) for x in range(N)) > 1e-4
    checks += 1
assert abs(z**8 - 1) > 0.1
checks += 1

# Factorization of every ordinary autocorrelation under tensor products.
H = 3
h = [2.0, 1.0, 1.0]
Fprod = {(x,y): f[x]*h[y] for x in range(N) for y in range(H)}
Gprod = {(x,y): g[x]*h[y] for x in range(N) for y in range(H)}
for j in range(1,4):
    shifts = [tuple()] if j==1 else itertools.product(itertools.product(range(N),range(H)), repeat=j-1)
    for shift in shifts:
        vec = ((0,0),)+tuple(shift)
        af = sum(math.prod(Fprod[((x+a)%N,(y+b)%H)] for a,b in vec)
                 for x in range(N) for y in range(H))
        ag = sum(math.prod(Gprod[((x+a)%N,(y+b)%H)] for a,b in vec)
                 for x in range(N) for y in range(H))
        assert abs(af-ag) < 1e-8
        checks += 1

# Sharp dense extension lemma: exhaustively test small finite-alphabet maps
# for each eligible support on selected small cyclic groups.
for n in (3,4,5,6,7):
    rmax=(n-1)//4  # r < n/4
    for r in range(rmax+1):
        for excluded in itertools.combinations(range(1,n),r):
            E=sorted(set(range(n))-set(excluded))
            for vals in itertools.product(range(3),repeat=len(E)-1):
                phase={0:0}
                phase.update(dict(zip((x for x in E if x!=0),vals)))
                valid=all((phase[(a+b)%n]-phase[a]-phase[b])%3==0
                          for a in E for b in E if (a+b)%n in phase)
                if not valid: continue
                # For a character into third roots, each phase must be t*x.
                assert any(all(phase[a]==(t*a)%3 for a in E)
                           for t in range(3) if (t*n)%3==0)
                checks+=1
# Independently test the overlap and connectedness inequalities behind the lemma.
for n in range(2, 17):
    for r in range(n):
        if 4 * r >= n: break
        for excluded in itertools.combinations(range(1,n),r):
            E = set(range(n))-set(excluded)
            for t in range(n):
                Et={a for a in E if (a+t)%n in E}
                assert len(Et)>=n-2*r and len(Et)>2*r
                seen={min(Et)}
                frontier=list(seen)
                while frontier:
                    a=frontier.pop()
                    for b in Et-seen:
                        if ((a-b)%n in E or (b-a)%n in E):
                            seen.add(b)
                            frontier.append(b)
                assert seen==Et
                checks+=1
print('SHARP_BISPECTRAL_CHECKS_PASSED', checks)
