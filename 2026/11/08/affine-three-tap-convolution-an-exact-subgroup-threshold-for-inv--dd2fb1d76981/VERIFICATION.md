---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Translation then ambient scaling automorphisms normalize b=0,u=1; scaling need not be inner in H, but it preserves rank by pullback. Frobenius irreducible decomposition has m nonsingular 1-dimensional blocks and (p-1)/m irreducibles of dimension m. Each nontrivial block is diag(1+zeta^{kh}) plus an m-cycle; cyclic recurrence makes kernel at most one-dimensional, determinant zero exactly when product_h(1+zeta^{kh})=(-1)^m. Reduction modulo cyclotomic prime (1-zeta) forces (-2)^m=1 and hence -2 in the unique subgroup H; conversely if -2 in H, 2H=-H and quotient (1-zeta^{2kh})/(1-zeta^{kh}) telescopes with sum_H h=0, giving determinant zero for all induced blocks. Regular-representation multiplicities give p-1 nullity, none intermediate. Independently computed exact cyclotomic coefficient reduction for p=5,7,11,13,17,19 and all multipliers a!=1, agreeing with iff -2 in H. Finite tests only corroborate full proof.

## originality

PASS

Finite affine group Fourier decomposition and cyclotomic arithmetic are classical; novelty is the exact arithmetic -2 subgroup criterion and no-intermediate-rank law for nonselfadjoint three-tap operator over all primes/complements of order >=3. Earlier generalized-dihedral three-tap census has order-two complement, not the same domain; undirected affine Cayley spectral work analyzes different symmetric supports. Bell–Minei 2006 is a closely related inaccessible primary paper and is a genuine priority risk, explicitly not claimed to have been read.

## value

PASS

Exact invertibility for the minimal natural three-move convolution on an affine Frobenius group gives a crisp recoverability barrier and exact nullity independent of translation and shift. Distinguishing invertible proper-complement groups from always-singular full affine groups is mathematically nontrivial and potentially useful in sparse harmonic analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
