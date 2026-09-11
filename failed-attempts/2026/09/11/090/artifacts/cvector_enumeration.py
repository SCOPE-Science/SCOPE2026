"""c-vector / B-seed BFS for lane-900 target audit (stdlib only).

Candidate initial matrix B0 reconstructed as the acyclic chain 1=>2->3
(B12=2, B21=-1 i.e. C(2,1) type on {1,2}, plus a single arrow 2->3).
CAVEAT: inputs/topic.json references "T0 as in T1" but no T1 is present in
the workspace, so B0 is a documented guess, not a pinned seed.

Checks:
  (a) sign-coherence of every c-vector encountered;
  (b) whether (0,1,-1) or (0,-1,1) ever occurs as a c-vector (the target's
      named blocking-wall normal);
  (c) C-cone sanity positions of m=(-2,2,-1) (advisory only).
"""
from collections import deque
from fractions import Fraction

B0 = [[0, 2, 0], [-1, 0, 1], [0, -1, 0]]
M_TARGET = (-2, 2, -1)
WALL = (0, 1, -1)
DEPTH = 6


def mutB(B, k):
    n = len(B)
    Bp = [r[:] for r in B]
    for i in range(n):
        for j in range(n):
            if i == k or j == k:
                Bp[i][j] = -B[i][j]
            else:
                Bp[i][j] = (B[i][j] + max(0, B[i][k]) * max(0, B[k][j])
                            - max(0, -B[i][k]) * max(0, -B[k][j]))
    return Bp


def mutC(C, B, k):
    """Sign-coherent column mutation; asserts coherence of column k."""
    n = len(B)
    colk = [C[i][k] for i in range(n)]
    pos = all(v >= 0 for v in colk)
    neg = all(v <= 0 for v in colk)
    assert pos or neg, ("non-sign-coherent column", colk)
    Cp = [r[:] for r in C]
    for i in range(n):
        Cp[i][k] = -C[i][k]
    for j in range(n):
        if j == k:
            continue
        b = B[k][j]
        for i in range(n):
            if pos:
                Cp[i][j] = C[i][j] + max(0, -b) * C[i][k]
            else:
                Cp[i][j] = C[i][j] + max(0, b) * C[i][k]
    return Cp


def solve_cone(C, m):
    """Solve C a = m over QQ; return a or None if singular."""
    A = [[Fraction(C[i][j]) for j in range(3)] for i in range(3)]
    b = [Fraction(v) for v in m]
    M = [A[i][:] + [b[i]] for i in range(3)]
    for col in range(3):
        piv = next((r for r in range(col, 3) if M[r][col] != 0), None)
        if piv is None:
            return None
        M[col], M[piv] = M[piv], M[col]
        d = M[col][col]
        for j in range(col, 4):
            M[col][j] /= d
        for r in range(3):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                for j in range(col, 4):
                    M[r][j] -= f * M[col][j]
    return tuple(M[i][3] for i in range(3))


def main():
    C0 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    seen = {}
    q = deque()
    q.append((tuple(tuple(r) for r in B0),
              tuple(tuple(r) for r in C0), []))
    seen[tuple(tuple(r) for r in B0)] = (C0, [])
    cvecs = {(1, 0, 0), (0, 1, 0), (0, 0, 1)}
    incoherent = []
    while q:
        Bt, Ct, path = q.popleft()
        B = [list(r) for r in Bt]
        C = [list(r) for r in Ct]
        if len(path) >= DEPTH:
            continue
        for k in range(3):
            Bp = mutB(B, k)
            Cp = mutC(C, B, k)
            for j in range(3):
                cv = (Cp[0][j], Cp[1][j], Cp[2][j])
                cvecs.add(cv)
                if not (all(v >= 0 for v in cv) or all(v <= 0 for v in cv)):
                    incoherent.append((path + [k], cv))
            key = tuple(tuple(r) for r in Bp)
            if key not in seen:
                seen[key] = (Cp, path + [k])
                q.append((key, tuple(tuple(r) for r in Cp), path + [k]))
    print("B-seeds (distinct B-matrices) to depth %d: %d" % (DEPTH, len(seen)))
    print("distinct c-vectors: %d" % len(cvecs))
    print("c-vectors: %s" % sorted(cvecs))
    print("sign-coherence violations: %d %s" % (len(incoherent), incoherent[:3]))
    print("wall normal %s present as c-vector: %s"
          % (WALL, (WALL in cvecs or tuple(-v for v in WALL) in cvecs)))
    inside = []
    for key, (C, path) in seen.items():
        a = solve_cone(C, M_TARGET)
        if a is not None and all(v >= 0 for v in a):
            inside.append(path)
    print("seeds whose C-cone contains m=%s (advisory): %s"
          % (M_TARGET, inside if inside else "none"))
    print("ENUM_OK")


if __name__ == "__main__":
    main()
