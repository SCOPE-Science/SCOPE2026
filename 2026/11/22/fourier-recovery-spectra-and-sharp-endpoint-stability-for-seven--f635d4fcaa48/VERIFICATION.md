---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The seventh cyclotomic polynomial forces equal fibre counts at a Fourier zero; a blind projective direction therefore removes exactly six frequencies, and the trivial multiplier is 7. Normalizing three directions gives f and f-x permutations. Their first and second sums remove the degree-6 and degree-5 coefficients; the cubic case is impossible by its squared sum after depression, and in the quartic case the squared sum after translation removes the quadratic coefficient. The square/nonsquare test gives the 35 affine and 98 nonlinear graphs for a fixed triple; each nonlinear graph has precisely three blind directions. Independent enumeration of the 5040 permutation graphs confirmed these facts, and single-, pair- and triple-incidence counts recover the five rank populations, summing to 85,900,584. For the representative quartic, the two Gauss periods have sum -1 and product 2; the origin, the punctured diagonals and the two sign cases off the diagonals yield squared singular values 49,14,7,0 with multiplicities 1,12,18,18. A fresh exact cyclotomic calculation reproduced these and the kernel numerators 31 (once), -4 (18 times), 3 (30 times), with denominator 49. Both endpoint norms equal the kernel l1 norm (columns, respectively rows), and averaging any projection by translations preserves identity on the range and cannot increase either norm. The only resulting invariant projection has precisely the visible frequencies as its support. Thus 193/49 is sharp for arbitrary linear projections, and the pseudoinverse norm is 1/sqrt(7). The frozen verification programs were inspected, not executed; independent reproduction used the fixed-triple census and cyclotomic calculation rather than replaying the 85.9-million-subset program. Replay specifications: RESULT.md Proof 1–5 and the bounded procedures in VERIFICATION.md.

## originality

PASS

Credit the classical extremal geometry, the known orthomorphism count and the previously known zero-translation kernel. The distinct conclusion supported by the comparisons is the full additive-convolution singular-value law and sharp endpoint projection constant for the extremal masks. The global rank census is contextual and reconstructible from prior direction geometry plus transversal incidence counts, not a new general direction theorem.

## value

PASS

The masks are selected intrinsically by the least nontrivial convolution rank, not by an arbitrary instance. The singular spectrum determines sharp l2 recovery stability and the endpoint constant determines the least amplification when projecting to admissible data, even without equivariance. Together the constants give reusable sharp stability information across the entire extremal affine orbit; the rank census situates it within the full population.

The dated certificate retains the supplied scientific assessment, sources and limitations.
