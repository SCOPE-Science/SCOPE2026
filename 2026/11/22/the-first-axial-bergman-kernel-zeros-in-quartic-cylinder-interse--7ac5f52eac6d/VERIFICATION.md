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

For the stated unweighted Euclidean volume the fiber slice has volume π^m(1−|z|^4)^m. Monomial orthogonality on the complete Reinhardt domain and vanishing of transverse powers on the axis reduce the sum to the axial monomials. Substitution x=r^4 in the radial norm integral gives π^(m+1)2^m m!/A_m(n). In the numerator extraction, the degree-(m+1) coefficient vanishes because the full (m+2)-nd difference is zero and the missing term A_m(−1) is zero. Independently, from A_m(n)=(n+2m+1)A_(m−1)(n) I obtain Q_m=s(1−s)Q'_(m−1)+(2m+1−ms)Q_(m−1), starting at Q_0=1. This gives exactly the displayed Q_9. I checked the supplied Cayley and Routh construction and independently counted roots directly by exact integer Schur reductions. For ascending coefficients, if a is the leading coefficient, b the constant, and Q* the coefficient reversal, reduce to (aQ−bQ*)/s. Strict |a|≠|b| holds at every step, so boundary roots would propagate to the nonzero constant base (they do not exist). Rouché then gives the disk count as 1+the reduced count if |a|>|b|, and deg(Q)−1−the reduced count otherwise. Counts for m=1…9 are 0,0,0,0,0,0,0,0,2. Alternating coefficients exclude negative real roots; the positive generating series excludes nonnegative real roots in the disk. Thus the two roots are a simple conjugate pair, and any disk product is attainable. Independent numerical check gives upper root 0.574805680698193+0.812513725985981i, modulus 0.995278918433690. Replay: python3 /workspace/branches/check_1.py, output check_1.out beside it; mpmath is used only for the displayed approximation. Frozen verify.py and VERIFICATION.md were inspected but not executed. The physical range has nine cases, not ten: m=0 is solely an auxiliary disk. No off-axis zero-freeness or later census is verified.

## originality

PASS

Credit to prior work for the general cylindrical kernel formula and its axial specialization. The supported distinct claim is the exact zero-count cutoff and census in the quartic-axis, varying-fiber family, not the kernel expression itself. The nearest four-cylinder record varies an exponent at fixed fiber number, and no inspected statement supplies or entails the varying-fiber cutoff. The strongest primary full text was not available; this decision is not a historical-priority certification.

## value

PASS

The dimension parameter counts identical geometric fibers rather than arbitrary truncation coefficients, and the axial restriction gives a natural obstruction to Lu Qi-Keng zero-freeness. The exact first obstruction and complete first-pair count are useful benchmarks even without determining the off-axis behavior in lower dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
