"""Infinite candidate ray: D=-kH gives Y->inf, b^2->inf (b^2-window alone
cannot imply uniform B). Plus primitive fixed-v2 family v=(r,H,0).
Pure stdlib. Target-directed stress test."""
import json

def demo(G, H, r, C, S, ks):
    def dot(A, B):
        return A[0]*(G[0][0]*B[0]+G[0][1]*B[1]) + A[1]*(G[1][0]*B[0]+G[1][1]*B[1])
    Q = dot(H, H); N = dot(C, H); C2 = dot(C, C); v2 = C2 - 2*r*S
    rows = []
    for k in ks:
        D = (-k*H[0], -k*H[1])
        M = dot(D, H); D2 = dot(D, D)
        sa_num = D2 + 2
        assert sa_num % 2 == 0
        den = M*r - N; num = 2*M*S - N*sa_num
        Y = num/(Q*den) if den != 0 else None
        CDOT = dot(C, D)
        b2 = r*D2 - 2*CDOT + (v2 + 2*S + 2*r - 2)
        rows.append({"k": k, "M": M, "D2": D2, "Y": Y,
                     "b2": b2, "num_pos": num > 0, "den_neg": den < 0})
    return {"Q": Q, "N": N, "v2": v2, "rows": rows}

A_G = [[2, 5], [5, 2]]; A_H = (1, 0)
print("== Case A v=(2,H,0), D=-kH ==")
d = demo(A_G, A_H, 2, (1, 0), 0, list(range(1, 11)))
for w in d["rows"]:
    print(f"k={w['k']:2d} M={w['M']:4d} D2={w['D2']:4d} "
          f"Y={w['Y']:.4f} b2={w['b2']:5d} cand={w['b2'] >= -2}")
print(f"Q={d['Q']} v2={d['v2']} N={d['N']}")
# asymptotic Y ~ k/2 claimed: check Y/k -> 1/2
ys = [w["Y"]/w["k"] for w in d["rows"]]
print("Y/k tail:", [round(t, 4) for t in ys[-3:]], "(->0.5)")

print("== Primitive fixed-v2 family v=(r,H,0), k=200, r=2..10 ==")
for r in range(2, 11):
    dd = demo(A_G, A_H, r, (1, 0), 0, [200])
    w = dd["rows"][0]
    print(f"r={r} v2={dd['v2']} Y={w['Y']:.3f} (~k/r={200/r:.1f}) b2={w['b2']}")
with open("output/artifacts/ray_demo.json", "w") as f:
    json.dump({"ray": d}, f, indent=1)
print("wrote output/artifacts/ray_demo.json")
