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

The source Hamiltonian is Hermitian; antisymmetric |m> decouples at -2J and the shifted symmetric block B is an irreducible 3x3 Jacobi matrix when Omega,D>0. Each spectral eigenvector has nonzero |p> component. Perfect transfer |00>→|11> is therefore equivalent to e^{-it beta_j}=-1 for every one of three distinct real eigenvalues. det B=-16JD^2<0, tr B=8J>0 imply exactly one negative root. Equating the full cubic characteristic coefficients yields S1=8J/a, S3=-16JD^2/a^3, Omega^2=a^2 Q with Q=(S1^3-4 S1 S2+8S3)/(16S1), so the stated odd-triple positivity and inverse construction are necessary and sufficient; no spectral-phase branch omitted. Countability proves planar nullity; approximating each real Jacobi eigenvalue by a nearby odd integer on scale k and using continuity at S1,Q>0 proves density of the reconstructed positive (J,D). A zero eigenmode with nonzero |p> projection excludes J=0,D>0. Independently constructed scipy expm for (-1,1,3) gives |<11|U|00>|²=0.9999999999999998 and leakage 3e-16, confirming the witness but not proving density.

## originality

PASS

PASS best knowledge for exact joint two-coupling inverse classification and dense measure-zero set, not for classical phase-commensurability or the battery Hamiltonian itself. Primary Ising/DM charging studies analyze ergotropy, power and noisy or time-dependent behavior; the diagonal-shift complete-graph perfect-transfer result has different control parameters. No inspected prior theorem implies the exact S1,S2,S3 inversion over positive (J,D), though a nonindexed exact-transfer specialization remains a risk.

## value

PASS

Sharp natural quantum-battery attainability question: all and only positive Ising/DM tunings for exact full charge and all transfer times, simultaneously topologically dense and planar null, plus unbounded positive DM witnesses and a strict J=0 boundary. This resolves exact versus numerical near-perfect charging and can be used when engineering robust approximations; not a short-time or noisy robustness theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
