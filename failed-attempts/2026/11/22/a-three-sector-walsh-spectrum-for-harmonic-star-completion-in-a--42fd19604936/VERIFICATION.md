---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The connected cube grounded on the star has a unique harmonic solution. Center-only data extend by zero off the center, and leaf-only harmonic weights sum to one off the center. By coordinate permutation symmetry their column sums are (2^d−1)/d, giving that eigenvalue on equal leaves; weighted Jensen and boundary reproduction give the extremal bounds. The leaf Gram matrix has constant diagonal and constant off-diagonal, so a single leaf difference evaluates the whole zero-sum sector. Transposition antisymmetry leaves opposite copies of v(z) on (1,0,z),(0,1,z), with v(0)=1 and (2I+L_{Q_{d−2}})v=0 elsewhere. The two copies cancel the squared-norm factor of two in the input. Walsh diagonalization of the normalized massive Green column gives the exact reciprocal-binomial ratio; simple binomial coefficient shifts give the stated Λ_d. For d=2, the slice is one point and the contrast ties the center at 1. For d≥3 the massive Green column is positive off the origin by its convergent adjacency Neumann series, so Λ_d>1, and Jensen is strictly lossy at e₁+e₂, which can hit each contrasting leaf in one step. For the rate, Taylor-expand the reciprocal around m/2 for K~Bin(m,1/2), m=d−1: odd terms cancel, the variance term is 2/m², the fourth-moment remainder is O(m⁻³), and the excluded tail is exponentially small. Multiplying by (m/2)(1−2⁻ᵐ)⁻² proves the expansion. Parseval postcomposition is an isometry, preserving the Gram operator, and restriction after synthesis is a left inverse. The exact-rational checker was inspected as text, not run; its d=2,…,6 checks are supplementary only.

## originality

FAIL

The distinct indexed cubical-face theorem gives exactly the nontrivial leaf-contrast amplification after a norm-preserving reduction to its edge case. It does not have the same full boundary problem, and the dates do not establish who derived the common quantity first. In the star contrast (0;1,−1,0,…,0), swap coordinates 1 and 2. The equal-coordinate slices are identically zero and the other slices are v(z),−v(z), z in Q_{d−2}, with v(0)=1. In the smaller cube Q_{d−1}, put values +1 and −1 on the coordinate edge (0,0),(1,0). Its harmonic extension is v(z),−v(z) on the two end slices: the single transverse sign-flip neighbor contributes −v(z), while the degree is d−1, so the resulting equation is the same d v(z)=sum of v over the d−2 cube neighbors. The identification preserves both counting norms (both inputs have squared norm 2 and both outputs two copies of v). Hence for every d≥3 the middle eigenvalue is literally λ_{d−2,1} of the face theorem (k=1); d=2 is the trivial one-point slice. The center and constant leaves are elementary invariant sectors, and the multiplicity d−1 follows from the constant-diagonal/constant-off-diagonal leaf Gram block. Thus the precise nontrivial exact sequence is already covered, not merely similar numerically. The first inverse-dimension correction is a routine binomial moment expansion of that sequence and does not leave a distinct substantive claim. This is a scientific coverage judgment, not an assertion of chronological priority.

## value

FAIL

The conditioned norm and exact spectrum are natural diagnostics for a coordinate-star signal embedding. But the only nontrivial sector is the already evaluated edge contrast in one fewer dimension. Identity on the center, equal leaves and their amplification by vertex count, sector multiplicity by symmetry, and Parseval invariance do not supply an additional valuable exact invariant beyond that coverage. A separate report of the same special-mode evaluation is not enough under the value criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
