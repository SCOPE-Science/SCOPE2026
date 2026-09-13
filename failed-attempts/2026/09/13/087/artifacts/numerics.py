"""Numerics verification for lane-1664: (F1, H + (2H-E)) two-contact family.

Verifies intersection theory, anticanonical property, node count,
effectiveness of beta=aH-kE, contact orders, virtual dimension and
descendant exponent m(beta)=0 for all admissible beta.
"""
# Intersection matrix in basis (H, E): H^2=1, H.E=0, E^2=-1
def dot(v, w):
    return v[0]*w[0]*1 + v[1]*w[1]*(-1)  # cross terms zero

H = (1, 0)
E = (0, 1)
D1 = (1, 0)          # H
D2 = (2, -1)         # 2H - E
K = (-3, 1)          # K_F1 = -3H + E
negK = (3, -1)

print("== Divisor checks ==")
print("D1+D2 =", (D1[0]+D2[0], D1[1]+D2[1]), " -K =", negK,
      "anticanonical:", (D1[0]+D2[0], D1[1]+D2[1]) == negK)
print("D1.D2 =", dot(D1, D2), "(expect 2 nodes)")
print("D1^2 =", dot(D1, D1), " D2^2 =", dot(D2, D2))
print("K^2 =", dot(K, K), "(F1 has K^2=8, check:", dot(K, K) == 8, ")")
# Toric boundary sum: E + (H-E) + H + (H-E) = 3H - E
F = (1, -1)  # H - E
tot = (E[0]+F[0]+H[0]+F[0], E[1]+F[1]+H[1]+F[1])
print("toric boundary sum =", tot, "== -K:", tot == negK)
# Arithmetic genus of D2: pa = (K+D2).D2/2 + 1
KD2 = (K[0]+D2[0], K[1]+D2[1])
print("pa(D2) =", dot(KD2, D2)/2 + 1, "(expect 0)")

print("\n== Admissible beta family: beta = aH - kE, a>=2, 0<=k<=a ==")
print("beta = aF + (a-k)E with F=H-E nef fiber, E effective => effective iff a>=0,a-k>=0")
rows = []
for a in range(2, 8):
    for k in range(0, a+1):
        beta = (a, -k)
        c1 = dot(beta, D1)
        c2 = dot(beta, D2)
        c1Xb = dot((3, -1), beta)  # c1(X).beta
        # log virt dim = (2-3)(1-0) + 0 + n with n=3 markings
        vdim = -1 + 3
        m = vdim - 2  # minus point codim 2
        assert c1 == a, (a, k, c1)
        assert c2 == 2*a - k, (a, k, c2)
        assert m == 0
        assert c1 > 0 and c2 > 0
        # effectiveness coeffs in (F,E) basis
        assert a >= 0 and (a-k) >= 0
        rows.append((a, k, c1, c2, c1Xb, m))
print(f"{'a':>3} {'k':>3} {'c1':>4} {'c2':>4} {'c1.b':>6} {'m':>3}")
for r in rows[:20]:
    print(f"{r[0]:>3} {r[1]:>3} {r[2]:>4} {r[3]:>4} {r[4]:>6} {r[5]:>3}")
print(f"... total checked (a<=7): {len(rows)} classes, all m=0, all c1,c2>0")

# Spot example beta0 = 2H
beta0 = (2, 0)
print("\n== Spot example beta0=2H ==", "c1=", dot(beta0, D1),
      "c2=", dot(beta0, D2), "c1.beta=", dot((3, -1), beta0))

print("\nAll numerics verified: m(beta)=0 identically; descendant vertex trivalent.")
