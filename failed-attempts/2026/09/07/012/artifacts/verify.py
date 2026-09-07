#!/usr/bin/env python3
"""Independent verifier for bordered BH(6,3) completion.
Exact arithmetic in Z[omega] only (integer pairs). No floating point.
Checks: alphabet, dephasing, R2/C2/R3* border, row Gram G=H conj(H^T)=6I,
column Gram, row-sum counts. Usage: python3 verify.py [--matrix bordered_matrix.json]
Exit 0 iff all checks pass; prints certificate lines.
"""
import json, sys, os

# --- Eisenstein integers a+b*omega ---
def e_add(x, y): return (x[0]+y[0], x[1]+y[1])
def e_mul(x, y):
    a1,b1 = x; a2,b2 = y
    return (a1*a2 - b1*b2, a1*b2 + a2*b1 - b1*b2)
def e_conj(x):
    a,b = x
    return (a-b, -b)

E_ONE = (1,0); E_W=(0,1); E_W2=(-1,-1)
E_MAP = {0:E_ONE, 1:E_W, 2:E_W2}

def load_matrix(path):
    with open(path) as f:
        d = json.load(f)
    return d["default_solution_rows"], d

def gram(exp_rows):
    n = len(exp_rows)
    H = [[E_MAP[e] for e in row] for row in exp_rows]
    G = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s=(0,0)
            for k in range(n):
                s = e_add(s, e_mul(H[i][k], e_conj(H[j][k])))
            G[i][j]=s
    return G

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    mp = sys.argv[sys.argv.index("--matrix")+1] if "--matrix" in sys.argv else os.path.join(base,"bordered_matrix.json")
    rows, meta = load_matrix(mp)
    n=6
    assert len(rows)==6 and all(len(r)==6 for r in rows), "shape"
    # alphabet
    assert all(e in (0,1,2) for r in rows for e in r), "alphabet"
    # dephasing
    assert rows[0]==[0]*6, "row1"
    assert all(r[0]==0 for r in rows), "col1"
    # border
    assert rows[1]==[0,0,1,1,2,2], f"R2 {rows[1]}"
    col2=[rows[i][1] for i in range(6)]
    assert col2==[0,0,1,1,2,2], f"C2 {col2}"
    assert rows[2]==[0,1,0,2,1,2], f"R3* {rows[2]}"
    # row-sum counts (2,2,2) for rows>0
    for i,r in enumerate(rows):
        c=[r.count(v) for v in (0,1,2)]
        if i==0:
            assert c==[6,0,0], c
        else:
            assert c==[2,2,2], f"row{i} counts {c}"
    # Gram
    G=gram(rows)
    ok=True
    for i in range(n):
        for j in range(n):
            want=(6,0) if i==j else (0,0)
            if G[i][j]!=want:
                print(f"FAIL G[{i}][{j}]={G[i][j]} want {want}")
                ok=False
    # columns
    cols=[[rows[i][j] for i in range(n)] for j in range(n)]
    Gc=gram(cols)
    for i in range(n):
        for j in range(n):
            want=(6,0) if i==j else (0,0)
            if Gc[i][j]!=want:
                print(f"FAIL colG[{i}][{j}]={Gc[i][j]}")
                ok=False
    print("alphabet {1,w,w2}: PASS")
    print("dephasing row1/col1 all-1: PASS")
    print("border R2=[1,1,w,w,w2,w2], C2 same, R3*=[1,w,1,w2,w,w2]: PASS")
    print("row-sum counts (2,2,2): PASS")
    print("row Gram H conj(H^T) = 6I over Z[omega]:", "PASS" if ok else "FAIL")
    print("column Gram = 6I:", "PASS" if ok else "FAIL")
    for row in G:
        print(row)
    if not ok:
        sys.exit(1)
    print("VERDICT: BH(6,3) completion VALID (existence, claim A).")

if __name__=="__main__":
    main()
