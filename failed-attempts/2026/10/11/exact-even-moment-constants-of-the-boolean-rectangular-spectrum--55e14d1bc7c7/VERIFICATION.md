---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For arbitrary complex Hilbert x,y, the exact Fourier constant term of (A+bz+conj(b)conj(z))^h is Σ_{k=0}^{⌊h/2⌋} h!/((h−2k)!(k!)²) A^{h−2k}|b|^{2k}. |b|≤A/2 gives the sharp B_h=2^{−h} C(2h,h), and the k=1 term is strictly positive for h>=2, giving equal norms/collinearity in the nonzero equality case. Apply successively to Hilbert pairs in the coefficient direct sum across d coordinates: inductive equality makes all coefficients a common vector times product phases; first-coordinate equality gives the final relative phase. Scalar λ∏(1+η_jz_j) attains equality. The all-zero case is excluded from nonzero equality classification; coefficients may vanish without breaking the inequality. Independently verified 11 binomial identities h=2..12 and 12 exact integer coefficient convolutions for d=1..3,h=2..5. Finite checks are corroborative, not proof of the infinite statement.

## originality

FAIL

The sourcepair theorem proves the exact scalar sharp constant B_h^(1/2h) on span{1,z} for every h>=2. This is not a new calculation in the target. Cavalcante et al. Theorem 3.3 proof already carries one-variable Steinhaus constants through arbitrary tensor orders using Fubini and Minkowski for p>=2. Its printed all-N bound is Btilde_p^d, NOT the smaller N=2 bound; however the identical proof specialized to N=2 with the already known sharp scalar input yields B_h^(d/(2h)) immediately. For independent Steinhaus pairs (u_j,v_j), set z_j=v_j/u_j, so Σ c_eps ∏(u_j if eps_j=0 else v_j)=(∏u_j) F(z); z_j are independent Haar and |∏u_j|=1. The target package claim that the two probability models are different is demonstrably false. Product extremizers follow from the product of balanced scalar extremizers, and equality rigidity follows by strict convexity/equality at successive Minkowski/Hilbert steps. Thus there is no substantive novel sharp tensorization theorem here. The sharp all-even Boolean rectangle norm is an immediate special N=2 application of the already published multiple-Steinhaus tensorization method with the previously established sharp two-character coefficient. The source paper does not explicitly display the same sharp N=2 formula; the rejection rests on the mathematical implication after trivial specialization, not on claiming it printed the exact conclusion. Its statement that the Steinhaus block probability model differs is false after unimodular quotienting.

## value

FAIL

The Boolean rectangular Λ(2h) norm is a natural harmonic-analysis invariant; this is not a rejection of the object. However, the entire exact value and factorized extremizers follow by a direct d-fold application of an already solved sharp two-character input and the established multiple-Steinhaus tensorization induction. The remaining strict-equality argument is routine equality bookkeeping for the same inequalities. There is no independently unknown exact invariant, new cutoff, significant mathematical obstacle, or motivated structural gap surviving this implication; it is a useful exposition/specialization, not a distinct mathematical finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
