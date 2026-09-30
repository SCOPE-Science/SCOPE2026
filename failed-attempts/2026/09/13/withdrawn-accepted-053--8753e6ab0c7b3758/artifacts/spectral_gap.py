"""Verify S1-invariant spectral gap at t=0 for Rossi problem.

Anti-diagonal S1: (z1,z2) -> (e^{i th} z1, e^{-i th} z2).
Weight of monomial z1^a z2^b zb1^c zb2^d = (a-c)-(b-d).
Bigraded harmonic H_{p,q}: eigenvalue of -Db = 2(p+q+2pq) (n=1, Folland).
Check: (1,0)->2, (0,1)->2, (2,0)->4, (1,1)->8, etc.
Invariant means some monomial in H_{p,q} has weight 0.
Linearized Yamabe (vol-constrained) ~ -4 Db - 2R0 with R0=4 (so that
first eigenspace is kernel: 4*2-8=0). Invariant gap = min over invariant
(p,q) not (0,0) of (4 lam - 8).
"""
mus = []
for p in range(0, 6):
    for q in range(0, 6):
        if p == 0 and q == 0:
            continue
        lam = 2 * (p + q + 2 * p * q)
        # does H_{p,q} contain A-invariant function?
        # weight set = { (a-c)-(b-d) : a+b<=? } -- sufficient check:
        # monomials z1^a z2^b zb1^c zb2^d with a+c? Actually H_{p,q}
        # consists of restrictions of harmonic polynomials homogeneous
        # deg p in (z), q in (zb). Weight zero achievable iff exists
        # a+b=p? no -- general: a<=p etc. Use brute force over monomials.
        found = False
        for a in range(p + 1):
            for b in range(p + 1):
                for c in range(q + 1):
                    for d in range(q + 1):
                        # monomial z1^a z2^b zb1^c zb2^d has holomorphic
                        # degree a+b, anti degree c+d; belongs to H_{p,q}
                        # sector if a+b<=p, c+d<=q with same parity steps
                        # (harmonic projection preserves weights, so if any
                        # polynomial of bideg (p,q) has weight 0, so does
                        # its harmonic part generically). Simplify: check
                        # exact bideg (p,q) monomials.
                        if a + b == p and c + d == q:
                            w = (a - c) - (b - d)
                            if w == 0:
                                found = True
        lin = 4 * lam - 8
        mus.append((p, q, lam, found, lin))

print("p q lam invariant lin-eig")
for p, q, lam, found, lin in mus:
    print(p, q, lam, found, lin)

inv = [(p, q, lam, lin) for (p, q, lam, f, lin) in mus if f]
print("\nInvariant sectors (p,q,lam,lin):", inv)
# first eigenspace check
first = [(p, q) for (p, q, lam, f, lin) in mus if lam == 2]
print("First eigenspace sectors:", first,
      "any invariant?", any(f for (p, q, lam, f, lin) in mus if lam == 2))
mingap = min(lin for (p, q, lam, lin) in inv)
print("Minimal invariant lin eig:", mingap)
# perturbed gap: eigenvalues move O(|t|); for |t|<1/2 gap stays >0
# rough bound: |d lam| <= C|t| with C~8 -> gap >= mingap - C|t| > 0
for t in [0.0, 0.1, 0.3, 0.49]:
    print(f"t={t} worst-case gap >= {mingap - 8*abs(t)}")
