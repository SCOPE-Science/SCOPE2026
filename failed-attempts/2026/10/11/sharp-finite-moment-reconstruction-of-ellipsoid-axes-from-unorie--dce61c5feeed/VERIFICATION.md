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

For every d≥2, P=∏a_i>0, the codimension-one Jacobian gives S(U)=κ_(d−1)P/(Σ_i a_i² U_i²)^(1/2), so X=Σ b_iU_i², b_i=a_i²/P²>0. Squared Haar coordinates have Dirichlet(1/2,...,1/2) law. The exact generating function Σ_k[(d/2)_k m_k/k!]z^k=∏(1−b_i z)^(−1/2) yields degree-d polynomial H=G^(−2) and the axis inversion a_i=√b_i (∏b_j)^(−1/(2(d−1))). Formal inversion to degree d is triangular and valid with repeated axes. With known P the last elementary symmetric coefficient is known and d−1 moments suffice. For pairwise distinct roots, vary the constant term of monic polynomial (or t coefficient with determinant fixed) and retain positive simple roots; the first d−1 (respectively d−2) moments remain fixed, proving the stated local sharpness including d=2. The finite verifier was independently reconstructed and run, but is not a proof for arbitrary dimension.

## originality

FAIL

The same weighted generating function and its exact determinant inversion are already explicit for arbitrary symmetric matrix spectra in Hillier–Kan–Wang (2008): D(t)=det(I−tA)^(−1/2), E(t)=det(I−tA), and for zero-mean Gaussian ratios with B=I the formula E[(z^TAz/z^Tz)^k]=k!/(d/2)_k [t^k]D(t). With A=diag(a_i²/P²), these are precisely the candidate moments and polynomial inverse. Extracting the first d polynomial coefficients, or d−1 given determinant, is a direct corollary of that prior general framework; perturbing one free elementary-symmetric coefficient at simple positive roots gives the routine generic lower bounds. The geometric section Jacobian and positive-axis conversion do not change this mathematical implication. The source is fully read at the relevant equations; an inaccessible 2001 article is not the reason for failure. Neither identical wording nor explicit restatement of the cutoff in prior literature is required for coverage.

## value

FAIL

Ellipsoid identification from direction-free central sections is a natural inverse problem and the d/d−1 moment budgets would be useful if genuinely new. However the precise invariant here is already mechanically obtainable from the previously published all-symmetric-matrix Gaussian-ratio moment formula and determinant generating function, together with standard sectional Jacobian geometry and elementary root continuity. The known-volume refinement is only the pre-fixed determinant coefficient. The candidate adds no nonstandard ellipsoid lemma, stability/error analysis, new observation model, difficult boundary case or independently motivated unknown exact invariant beyond that established consequence. In view of explicit prior coverage this is a repackaging of known analytic machinery rather than a substantive new mathematical gap, not a rejection merely for being elementary or lacking broad downstream theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
