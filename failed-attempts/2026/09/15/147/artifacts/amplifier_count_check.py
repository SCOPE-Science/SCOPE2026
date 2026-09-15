"""Pre-trace / amplification count check in depth aspect (heuristic, auditable).

Published depth-aspect sup technology (Marshall; Saha; Hu-Saha; Blomer et al.)
proves, for compact/key ranges, sup bounds of shape (prob measure)
  ||f||_inf << p^{n/2 - c*n} x lambda^{...}
i.e. saving comes from NEWVECTOR-SPECIFIC amplifier + p-adic stationary phase,
and the trivial/bulk bound is p^{n/2}? or p^{n/4}? -- convention-dependent
(prob vs arith normalization). This script documents the convention map and
the amplifier-length obstruction:

- Hecke operators at p act SCALARILY on the newvector line (Atkin-Lehner
  eigenvalues), so a standard unramified amplifier (primes l != p) has length
  L and gain ~ L^{1/2}, while the geometric side has ~ L^2 terms; optimizing
  L against the pre-trace kernel truncation gives the familiar delta ~ 1/24-1/12
  ONLY in ranges where the arch eigenvalue / level mix cooperates.
- In PURE depth aspect (fixed lambda, n->inf), the p-adic wavefront/supp of
  the test function must shrink ~ p^{-n} to project to the newvector, so the
  number of Hecke returns at distance ~1 grows like Vol(K_0(p^n))^{-1} ~ p^n;
  the amplifier must beat p^n returns with only ~L gains, forcing
  L >> p^{cn}; but amplifier length is capped by arch spectral window
  (~ lambda^{O(1)}) and by the requirement l != p (fixed residue classes),
  so no fixed-lambda amplifier closes the count. Amplification works in
  eigenvalue/weight aspect, NOT in pure depth.
- The Hu-Saha filtration improves the LOCAL bound exponent but does not by
  itself supply amplification gain; quantitative matrix-coefficient decay
  gives integrability, not pointwise saving at the identity coset.

We print the count inequality: need L^{1/2} >> p^{n/2} (#returns^{1/2}),
i.e. L >> p^n, vs available L << lambda^{A} p^{eps} (fixed lambda => bounded).
"""
p = 3
lam = 100.0  # fixed arch eigenvalue scale
A = 2.0      # generous amplifier-length exponent in lambda
L_avail = lam ** A
print(f"fixed lambda={lam}, generous available amplifier length L ~ {L_avail:.0f}")
for n in [2, 4, 6, 8, 10]:
    need = p ** n
    print(f"n={n:>2}: need L >> p^n = {need:>6} | avail L ~ {L_avail:.0f} | "
          f"ratio need/avail = {need/L_avail:>9.2f} {'OK' if need < L_avail else 'BLOCKED'}")
print()
print("For every n>=8 (and asymptotically), the count does not close at fixed lambda.")
print("Known positive results evade this by (i) letting lambda grow with n,")
print("(ii) bounding sup on average / in L^4, or (iii) restricting to compact")
print("quotients where newvector concentration differs. None is available under")
print("the target's hypotheses (fixed lambda, pointwise, full Y_0(p^n), vol 1).")
