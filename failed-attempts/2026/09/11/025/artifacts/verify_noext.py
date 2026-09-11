"""Exact verifier: each Greaves et al. 57-line R18 parent is unextendable to a real 58th line.
Usage: python3 verify_noext.py [F1|F2|F3|F4|ALL]  (needs sympy + parent JSONs in same dir)
Method: for exact 18-col basis B (det!=0), a unit 58th vector u with dots +-sqrt(2/5)
on basis cols satisfies B^T u = t, t = c*s, c^2=2/5, s in {+1,-1}^18. Norm condition:
2 s^T adj(M) s = 5 det(M), M = B B^T (all integers). Full extension additionally needs
|s^T adj(B) f| = |det B| for every non-basis column f (all integers). Exhausts 2^18.
"""
import json, sys, time
import sympy as sp
BASES = {"F1": [35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54],
         "F2": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18],
         "F3": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],
         "F4": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]}
def check(name):
    F = json.load(open(f"artifacts/{name}.json"))
    sel = BASES[name]
    B = sp.Matrix([[F[r][c] for c in sel] for r in range(18)])
    detB = int(B.det()); assert detB != 0
    D = abs(detB)
    adjB = B.adjugate()
    M = B*B.T; detM = int(M.det()); adjM = M.adjugate()
    A = [[int(adjM[i, j]) for j in range(18)] for i in range(18)]
    rhs = 5*detM
    Fm = sp.Matrix(F)
    rest = [c for c in range(57) if c not in sel]
    Y = {c: [int((adjB*Fm[:, c])[i]) for i in range(18)] for c in rest}
    unit = full = 0
    for b in range(2**18):
        s = [1 if (b >> i) & 1 else -1 for i in range(18)]
        tot = 0
        for i in range(18):
            r = 0; Ai = A[i]
            for j in range(18): r += Ai[j]*s[j]
            tot += s[i]*r
        if 2*tot != rhs: continue
        unit += 1
        if all(abs(sum(s[i]*Y[c][i] for i in range(18))) == D for c in rest):
            full += 1
    print(f"{name}: detB={detB} unit-norm patterns={unit} full 58-extensions={full}")
    assert full == 0
    return unit
if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "ALL"
    names = ["F1","F2","F3","F4"] if arg == "ALL" else [arg]
    t0 = time.time()
    for n in names: check(n)
    print(f"VERIFY_OK ({time.time()-t0:.0f}s)")
