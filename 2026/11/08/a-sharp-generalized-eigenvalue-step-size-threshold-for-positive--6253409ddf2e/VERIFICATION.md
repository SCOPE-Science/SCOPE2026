---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

For n>=2 and fixed symmetric entrywise nonnegative doubly stochastic 0<W≼I with eigenvalue 1 simple, H positive diagonal, exact tracker initialization yields invariant codimension-one subspace sum(y-Hz)=0. Eliminating y yields the symmetric quadratic pencil Q_alpha(zeta)=(zeta I-W)W^-1(zeta I-W)+alpha(zeta-1)H. Permanent simple eigenvalue 1 has nonadmissible eigenvector (1,0). For zeta=e^{it} nonreal unit-circle, imaginary and real null-form equations imply z*Wz-z*W^-1 z-alpha z*Hz=0, impossible. Small positive alpha puts the second consensus branch 1-alpha mean(h)+O(alpha²) inside the disk; all other branches start at eigenvalues of W of modulus<1. The first crossing must be at -1 and Q_alpha(-1)=W^-1+2I+W-2alpha H gives exact positive-definiteness frontier. For larger alpha a negative min pencil eigenvalue at -1 and positive-leading coefficient as zeta→-∞ yield a real root <-1. The left eigenvector projection argument shows threshold/supercritical bad modes are excitable by some valid primal initialization; primal convergence would force tracker convergence, ruling out false failure. Exact independently reconstructed 2x2 example gives alpha*=9/5, det(C-18H/5)=0, and characteristic (z-1)(z+1)(40z²-12z-19)/40. No finite test is used as a universal proof.

## originality

PASS

Best-of-knowledge: the exact arbitrary-n heterogeneous SPD-graph stability frontier and proof that the only first nontrivial unit-circle crossing is -1 survive direct statement/implication comparisons with two materially inspected primary papers, the 2020 sparse-design abstract, and published homogeneous/two-agent records. The indexed November 8 exact claim is the assigned work itself, not independent older coverage.

## value

PASS

The exact all-network common-step stability threshold for a motivated class of lazy SPD consensus mixing matrices and heterogeneous local curvatures replaces conservative fixed-network tuning by one computable symmetric generalized eigenvalue. The exclusion of nonreal unit-circle crossings supplies structural information about the sharp flip frontier, not merely a numerical bound. It is distinct from optimizing an asymptotic contraction rate or obtaining local online step selection, and arbitrarily many agents are included.

The dated certificate retains the supplied scientific assessment, sources and limitations.
