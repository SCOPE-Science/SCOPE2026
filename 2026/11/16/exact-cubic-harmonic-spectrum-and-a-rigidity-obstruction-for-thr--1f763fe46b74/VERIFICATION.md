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

PASS. For three independent thresholds 1/sqrt(2)<=c_i<1, the six antipodal coordinate caps are interior disjoint and invariant under coordinatewise sign flips, giving one 1x1 parity block (xyz) and three 2x2 blocks (b_i,d_i). Direct spherical polar circular moments integrate the six given threshold polynomials A,B_a,B_t,C_a,C_t,H, including the opposite-sign mixed moments H(c_j)−H(c_k); with stated sphere norms this gives all seven exact eigenvalues and sharp bounds even at accidental coincidences. The key nontrivial obstruction is H'(c)=(1-c²)(35c^4−10c²−1)/16>0 on the complete interval: scalarity requires H(c_1)=H(c_2)=H(c_3), hence equal widths. In the equal-width case the xyz/b-sector gap (7c(1−c²)/32)(15c^4−48c²+17)<0. Thus scalar concentration is impossible. Independently checked differentiation/factor signs; inspected direct exact integration over all 28 Gram pairings in the package's symbolic checker. Strict 0<eigenvalues<1 follows from analytic nonzero harmonics and open observed/unobserved regions. No inference from sampled widths is necessary.

## originality

PASS

Best-of-knowledge PASS on distinct scientific statement/implication comparisons and primary evidence, with explicit source-access and index limitations. Three unequal antipodal axis cap pairs, cubic spectral rigidity

## value

PASS

PASS. The natural practical problem is choosing independently the widths of six orthogonally oriented antipodal observation windows. The three-parameter exact cubic spectrum and impossibility of a tight cubic sampling form despite independently adjusted widths supply a structural obstruction, not an arbitrary finite computation. The statement is restricted to disjoint unweighted axial caps and pure cubic harmonics, not global sensor conditioning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
