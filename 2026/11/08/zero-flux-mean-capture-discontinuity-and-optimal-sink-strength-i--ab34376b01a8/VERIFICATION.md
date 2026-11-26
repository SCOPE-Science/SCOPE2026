---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In the stated parity basis, H has couplings A=2Jcos(φ/4), B=2Jsin(φ/4), and w=(1,0,1,0)/√2 and v=(1,0,−1,0)/√2 are the sink and source. The real part of a no-jump eigenvalue is −κ|w*ψ|²/(2||ψ||²); equality requires an H-eigenvector orthogonal to w. At generic flux the four H-eigenvalues are distinct and every eigenvector overlaps w, so survival decays. At exact zero flux the decoupled odd mode has no source overlap; the directed reachable three-dimensional restriction has simple H-eigenvalues, all with nonzero sink overlap. The 2π representative is identical by gauge, or by exchanging the parity blocks. At π the Hamiltonian leaves the antisymmetric pair invariant and entirely perpendicular to w, so the prepared state never decays. Independently solving the backward Lyapunov equation K*Q+QK=−I in real coordinates on the stable subspaces gave v*Qv=4/κ+κ(A²+B²)/(A²−B²)² and 3/κ+κ/A² for B=0. The residues therefore differ by 1/κ at fixed κ as φ→0, with no finite-time survival discontinuity. Minimizing c/κ+dκ gives a unique κ=√(c/d), mean 2√(cd); inserting the two coefficients and cos(φ/2)∼−(φ−π)/2 gives all stated optimizer and half-flux scalings. Exact algebra replay: `python3 /workspace/independent_checks.py 1`. The uploaded checker was inspected but not executed.

## originality

PASS

Best-knowledge pass for the localized antipodal jump-time means, finite zero-flux jump and sink-rate law. The capture-probability trichotomy is substantially prior covered and is credited as such, not treated as the originality-bearing result. The closest lifetime record really uses a different initial state, as confirmed in its Finding and Limitations.

## value

PASS

An exactly solvable localized trapping model exposes a finite discontinuity of a mean even though capture remains almost sure on both sides and finite-time evolution is continuous. The sharp fixed-rate and optimized behavior near half flux quantify distinct survival and control regimes in the same physical time convention. Known dark-state mechanisms and the elementary differentiation alone are not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
