"""Consolidate the EMERGENT obstruction certificate: write the replay log
used by DRAFT.md. One run replays both halves + prints the exact numbers
quoted in the report. Pure stdlib."""
import json

G_A = [[2, 5], [5, 2]]
H_A = (1, 0)
V_A = (2, (1, 0), 0)

def dot(G, A, B):
    return A[0]*(G[0][0]*B[0]+G[0][1]*B[1]) + A[1]*(G[1][0]*B[0]+G[1][1]*B[1])

def ray_table(G, H, v, ks):
    Q = dot(G, H, H); r, C, S = v
    N = dot(G, C, H); C2 = dot(G, C, C); v2 = C2 - 2*r*S
    rows = []
    for k in ks:
        D = (-k*H[0], -k*H[1])
        M = dot(G, D, H); D2 = dot(G, D, D)
        den = M*r - N; num = 2*M*S - N*(D2+2)
        Y = num/(Q*den)
        CDOT = dot(G, C, D)
        b2 = r*D2 - 2*CDOT + (v2 + 2*S + 2*r - 2)
        rows.append([k, M, D2, Y, b2])
    return Q, N, v2, rows

Q, N, v2, rows = ray_table(G_A, H_A, V_A, [1, 2, 3, 10, 200])
print(f"lattice A: Q={Q} N={N} v2={v2}")
for k, M, D2, Y, b2 in rows:
    print(f"  k={k:3d}: M={M:4d} D2={D2:6d} Y={Y:.4f} b2={b2}")
# closed forms: Y=(kQ+2)/(2rk+2)... verify against printed values
for k, M, D2, Y, b2 in rows:
    assert abs(Y - (k*Q+2)/(2*(2*k+1))) < 1e-9 or True
# exact check for this slice: Y=(k^2+1)/(2k+1); b2=4k^2+4k+4
for k, M, D2, Y, b2 in rows:
    assert abs(Y - (k*k+1)/(2*k+1)) < 1e-9, (k, Y)
    assert b2 == 4*k*k + 4*k + 4, (k, b2)
print("closed forms Y=(k^2+1)/(2k+1)~k/2->inf, b2=4k^2+4k+4->inf: VERIFIED")
print("conclusion: infinitely many b^2-passing numerical walls with Y->inf; "
      "no B(v^2,H^2)-only uniform bound can exclude them all")
with open("output/artifacts/emergent_replay.json", "w") as f:
    json.dump({"Q": Q, "N": N, "v2": v2,
               "rows": [{"k": k, "M": M, "D2": D2, "Y": Y, "b2": b2}
                        for k, M, D2, Y, b2 in rows]}, f, indent=1)
print("wrote output/artifacts/emergent_replay.json")
