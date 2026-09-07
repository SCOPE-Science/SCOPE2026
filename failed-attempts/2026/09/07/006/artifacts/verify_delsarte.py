"""Independent Delsarte certificate checker (stdlib only).
Loads artifacts/delsarte_certificate.json, recomputes Eberlein from comb,
checks dual feasibility y>=0, B^T y >= 1, and objective b^T y = 3141/5 (M<=629.2).
Also checks primal feasibility Bx<=b and strong duality gap 0.
Usage: python3 verify_delsarte.py [cert_path]
"""
import json, sys
from math import comb
from fractions import Fraction

def E(n, w, k, x):
    s = 0
    for j in range(k+1):
        if j > x: continue
        if k-j > w-x or k-j > n-w-x: continue
        t = comb(x, j)*comb(w-x, k-j)*comb(n-w-x, k-j)
        s += -t if (j % 2) else t
    return s

def main(path):
    with open(path) as f:
        cert = json.load(f)
    n, w = cert["n"], cert["w"]
    assert (n, w) == (16, 7)
    var_idx = cert["var_idx"]
    x = [Fraction(v) for v in cert["primal_x"]]
    y = [Fraction(v) for v in cert["dual_y"]]
    assert len(x) == 5 and len(y) == 7
    # recompute E and check stored table
    for k in range(8):
        for i in range(8):
            assert E(n, w, k, i) == cert["E"][k][i], f"E mismatch {k},{i}"
    # dual: y>=0
    assert all(v >= 0 for v in y), "dual y>=0 failed"
    # B^T y >= 1 for each var i
    for jj, i in enumerate(var_idx):
        lhs = sum(Fraction(-E(n, w, k+1, i))*y[k] for k in range(7))
        assert lhs >= 1, f"dual constraint i={i} lhs={lhs} <1"
        print(f"dual constr i={i}: lhs={lhs} >=1 OK")
    b = [Fraction(comb(w, k+1)*comb(n-w, k+1)) for k in range(7)]
    dobj = sum(b[k]*y[k] for k in range(7))
    assert dobj == Fraction(3141, 5), f"dual obj {dobj} != 3141/5"
    print(f"dual obj b^Ty = {dobj} = 628.2; M bound = {dobj+1} = 629.2 OK")
    # primal
    assert all(v >= 0 for v in x), "primal x>=0 failed"
    for k in range(7):
        lhs = sum(Fraction(-E(n, w, k+1, i))*x[jj] for jj, i in enumerate(var_idx))
        assert lhs <= b[k], f"primal row K{k+1} {lhs} > {b[k]}"
    pobj = sum(x)
    assert pobj == Fraction(3141, 5), f"primal obj {pobj} != 3141/5"
    print(f"primal obj = {pobj}, gap 0, strong duality OK")
    print("DELSARTE CERTIFICATE VERIFIED: LP optimum = 3146/5 = 629.2 >> Johnson 122")
    print("Conclusion: plain Delsarte does NOT improve 122 (negative result, rigorous).")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "delsarte_certificate.json")
