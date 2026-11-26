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

The prefix-count recurrence Z(j)=j−Z(floor(j/2)) yields the base-four weights 0,1,−1,0. In a carry-free addition of m_t, the increments are −2 to +1, with extremes realized at i=m_t and i=0. A remaining carry costs a digit with increment zero, offsetting the one higher-tail increment. Lower equality then requires the first carry at the last digit, because a digit receiving a carry cannot contribute −2; for t=1 its initial 3 string ends at a digit 1, giving odd valuation of i+1. At upper equality a carry from digit zero must persist with +1 increments until its higher increment at a 0 or 2, yielding even valuation. Thus the extreme factors have the required initial bits. Recurrence and unit sliding steps supply each interior zero count with both initial bits. Palindromic prefixes give reversal closure, so the terminal endpoint at even source starts adds no vectors. The arbitrary-length carry bound is logarithmic and the geometric subsequence gives the matching lower running maximum. A separate check in /workspace/branches/5728e89d-7db6-44fb-bb13-de493e568f0a/independent_spectrum_check.py and independent_spectrum_check_output.txt matched the exact spectra at all starts 0–131071 for t=1–7; this is finite corroboration only. The frozen code and its log were inspected, not executed.

## originality

FAIL

The full spectrum and global bound follow directly from the published exact endpoint recurrences for zero counts of the overlapping 2-block word of the same period-doubling sequence. A different complexity name does not prevent this implication. The two similar indexed findings inspected are not themselves equivalent.

## value

FAIL

Factorwise run collapse is natural and a complete spectrum would be useful if it added substantive information. Here the exact result is the parity recoding of a previously determined interval at a prescribed length sequence; the global bound is also inherited. The alternative digit proof does not establish a new invariant or further scope in the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
