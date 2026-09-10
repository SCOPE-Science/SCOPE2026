"""Corrected same-phase analysis + Lemma R2 (r=2, C=H, S=0) verification.
Same-phase (destabilizing) requires M*N>0, i.e. M>0 here (N>0).
Lemma R2: for r=2,C=H,S=0 (any Q): den>0 same-phase => b^2<-2 always;
  den<0 same-phase => 0<M<Q/2, 0<=D2<=M^2/Q. Pure stdlib."""
import json

def scan_corrected(G, H, v, box):
    def dot(A, B):
        return A[0]*(G[0][0]*B[0]+G[0][1]*B[1]) + A[1]*(G[1][0]*B[0]+G[1][1]*B[1])
    Q = dot(H, H); r, C, S = v
    N = dot(C, H); C2 = dot(C, C); v2 = C2 - 2*r*S
    cats = {"den_pos_sp": [], "den_neg_sp": [], "anti": []}
    for d1 in range(-box, box+1):
        for d2 in range(-box, box+1):
            if d1 == 0 and d2 == 0:
                continue
            D = (d1, d2)
            M = dot(D, H); D2 = dot(D, D)
            if (D2+2) % 2 != 0:
                continue
            den = M*r - N; num = 2*M*S - N*(D2+2)
            if den == 0 or num*den <= 0:
                continue
            Y = num/(Q*den)
            CDOT = dot(C, D)
            b2 = r*D2 - 2*CDOT + (v2 + 2*S + 2*r - 2)
            same_phase = (M*N > 0)
            key = ("den_pos_sp" if den > 0 else "den_neg_sp") if same_phase else "anti"
            cats[key].append({"D": list(D), "M": M, "D2": D2, "Y": Y, "b2": b2})
    return {"Q": Q, "N": N, "v2": v2, **{k: v_ for k, v_ in cats.items()}}

for name, G, H, v, box in [
    ("A", [[2, 5], [5, 2]], (1, 0), (2, (1, 0), 0), 25),
    ("B", [[4, 6], [6, 2]], (1, 0), (2, (1, 0), 0), 25),
]:
    d = scan_corrected(G, H, v, box)
    Q, N = d["Q"], d["N"]
    p, n, a = d["den_pos_sp"], d["den_neg_sp"], d["anti"]
    print(f"== {name}: Q={Q} N={N} v2={d['v2']} box={box}")
    print(f"   den>0 same-phase: {len(p)}, b2-passing: {sum(1 for w in p if w['b2'] >= -2)} "
          f"(Lemma R2 predicts 0)")
    assert all(w["b2"] < -2 for w in p), "Lemma R2 violated!"
    assert all(w["M"] <= 0 for w in a), "anti-phase should have M<0 (N>0)"
    print(f"   anti-phase (M<0, correctly non-destabilizing): {len(a)}")
    print(f"   den<0 same-phase: {len(n)}, b2-passing: {sum(1 for w in n if w['b2'] >= -2)}")
    nn = [w for w in n if w["b2"] >= -2]
    if nn:
        assert all(0 < w["M"] < Q/2 for w in nn), "M bound violated"
        assert all(0 <= w["D2"] <= w["M"]**2/Q + 1e-9 for w in nn), "D2 window violated"
        print(f"   passing: maxM={max(w['M'] for w in nn)} (<Q/2={Q/2}), "
              f"maxY={max(w['Y'] for w in nn):.3f}, maxD2={max(w['D2'] for w in nn)}")
        # Y envelope check: Y=(D2+2)/(Q-2M) for this slice; verify identity
        for w in nn:
            assert abs(w["Y"] - (w["D2"]+2)/(Q-2*w["M"])) < 1e-9, "Y identity"
        print("   Y identity Y=(D2+2)/(Q-2M): PASS on all passing walls")
print("LEMMA-R2 REPLAY: PASS")
