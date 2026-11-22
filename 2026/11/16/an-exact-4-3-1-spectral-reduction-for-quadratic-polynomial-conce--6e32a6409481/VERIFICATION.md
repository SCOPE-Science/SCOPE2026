---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Normalized ball monomial moments follow the gamma/Dirichlet formula and each orthant moment is exactly 2^-d times the corresponding absolute-monomial ball moment. The S_d permutation action on constants, linear terms, diagonal quadratics and unordered-edge monomials decomposes into four trivial modules, three standard modules and one irreducible edge row-sum-zero W. W irreducibility follows from the three-orbit commutant count; dimensions sum 4+3(d-1)+d(d-3)/2=binom(d+2,2), so the two invariant forms reduce to 4×4, 3×3 and one scalar. The explicit edge test (x1-x4)(x2-x3) yields scalar 2^-d(1-2/pi)^2, while O(d)-invariance of the full ball reproducing kernel yields trace binom(d+2,2)2^-d. No nonzero polynomial vanishes on an open orthant or its open complement, proving 0<lambda<1. In independent calculations using the full monomial moment Gram (not the package code), sorted eigenvalues matched the 4/3/1 pencil multiplicities for d=4,5,6, with d4 extremes 0.00007939865604 and 0.4834771886728. Finite checks support but do not replace all-d Schur representation proof.

## originality

PASS

Gerhards–Huang (arxiv:2308.03543) explicitly introduce exactly the total-degree polynomial bandlimit on a ball but their Theorem 2.1 is an n→∞ spectral-clustering/Shannon-number theorem and Appendix B gives Remez-type bounds, not the fixed n=2 exact orthant spectrum. The Khalid–Kennedy–McEwen 2014 ball model uses Fourier–Laguerre/Fourier–Bessel bands, unlike the present polynomial space. Published quadratic *spherical surface* orthant concentration gives a related edge-sector scalar but lacks the solid-ball radial quadratic and four-dimensional trivial multiplicity block. No source read implies the whole exact spectrum or sharp full-volume constants; unindexed specialist exact matrix reductions remain a residual risk.

## value

PASS

The positive orthant is a canonical geometrical observation region and degree two the first full polynomial band containing radial as well as angular quadratic variation. Replacing an unbounded-size dim binom(d+2,2) matrix by fixed 4+3+1 Gram pencils is a useful uniform spectral classification yielding exact best/worst observation energies. A tiny 1/16-volume orthant can concentrate about 0.48348 of a quadratic ball polynomial for d=4, a substantive localization phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
