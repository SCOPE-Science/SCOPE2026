---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Bernini et al.'s cover formula counts distinct balanced-pair insertion words and gives the stated pair-product deficit, nonnegative and zero for a single arch. For n>2r a component of size n−r is unique; choosing its Catalan interior and the ordered prefix/suffix of total size r gives C_{n−r−1}C_{r+1}. The limiting masses sum to C(1/4)−1=1, so the complement size R_n is tight. Separating the largest arch gives Q_n=(n−R_n)R_n plus the pair products among the remaining arches; those are in [0,R_n²/2]. Thus 0≤R_n−Q_n/n≤R_n²/n, proving convergence at the half-integer thresholds. The Catalan asymptotics give the stated r^(-3/2) mass tail and infinite limiting first moment. Marking two ordered-by-position distinct arches gives C³(zA′)², with no additional factor of two. The identity z²C³/(1−4z)=1/[2(1−4z)]−3/[2√(1−4z)]+C gives the claimed exact finite mean and its asymptotic; at n=1 the mean is zero. RESULT.md, VERIFICATION.md and check.py were inspected; reported finite enumeration through n=8 and recurrence through n=150 were not rerun.

## originality

FAIL

Equivalent coverage is established for the asserted contribution. The separate balanced-deletion record computes the exact generating function for the identical random variable on the identical ensemble, and explicitly gives the Catalan largest-arch remainder law. The insertion identity identifies this variable without a new counting step; elementary coefficient extraction and the tight-remainder bound give the exact finite mean and deficit limit, respectively. This is a finding about substantive overlap, not an inference about publication order between two records dated the same day.

## value

FAIL

The typical-versus-mean discrepancy is useful in interpreting insertion counts, but the proposed additional exact facts are already mechanically supplied for the same natural statistic: a fixed-r remainder transfer and the extraction of coefficients from the exact known mean series. Renaming that statistic as an insertion deficit by the credited deterministic identity does not add a distinct invariant, mechanism or classification. No valuable distinct narrowed claim was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
