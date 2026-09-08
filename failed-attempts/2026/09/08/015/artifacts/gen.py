# gen.py v1.0 - DIMACS generator for F_n^(s,t).
# Variable x_e = True means edge e red. Edges in lexicographic order,
# var(e) = e+1. For each s-set S: clause of negated vars (no red K_s).
# For each t-set T: clause of positive vars (no blue K_t).
# Usage: python3 gen.py n s t out.cnf
import sys, itertools

def main():
    n, s, t, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    vid = {e: k + 1 for k, e in enumerate(edges)}
    clauses = []
    for S in itertools.combinations(range(n), s):
        clauses.append([-vid[(S[i], S[j])] for i in range(s) for j in range(i + 1, s)])
    for T in itertools.combinations(range(n), t):
        clauses.append([vid[(T[i], T[j])] for i in range(t) for j in range(i + 1, t)])
    with open(out, "w") as f:
        f.write("c F_%d^(%d,%d) Ramsey CNF; edge-lex order; True=red\n" % (n, s, t))
        f.write("p cnf %d %d\n" % (len(edges), len(clauses)))
        for c in clauses:
            f.write(" ".join(map(str, c)) + " 0\n")

main()
