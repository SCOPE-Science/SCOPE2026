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

A fresh independent full 2^20 Walsh transform of the explicitly recursively enumerated 2188 length-10 nonnegative Motzkin excursions yielded exactly 67312 zero multipliers, smallest nonzero magnitude 2 and 48 weight-four zeros. A second Walsh transform of the nonzero-support indicator yielded kernel absolute sum 52163296 and square sum 1028929880064, giving projection norm 52163296/1048576 = 1630103/32768. The inspected C++17 code independently implements signed-height transfer recurrence at all 1048576 frequencies and checks three CSV certificates. Odd Motzkin counts M_4..M_9 force no zeros, whereas n=2,3 explicit witnesses give singularity. Translation-averaging arbitrary projection preserves its range and cannot increase endpoint norm, proving unrestricted optimality. All numeric claims are finite n=10; no infinite spectrum claim.

## originality

PASS

Motzkin counting, Jacobi–Rogers recurrences, and 2-adic scalar parity are classical. The exact full time-coordinate Walsh nullity at length ten, minimum-zero degree, and Fourier range projection constant are additional character-sensitive data not implied by scalar Motzkin count or traditional height-weighted generating polynomials. No equivalent table identified in bounded Resultary and published searches.

## value

PASS

A natural embedding of Motzkin excursions into Boolean incidence space yields a first singular return after a six-length invertible interval and an exact optimal projection constant on a 1,048,576-dimensional convolution operator. The precise weight-four first obstruction and recoverability norm are meaningful finite harmonic-analytic invariants, even without an all-n theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
