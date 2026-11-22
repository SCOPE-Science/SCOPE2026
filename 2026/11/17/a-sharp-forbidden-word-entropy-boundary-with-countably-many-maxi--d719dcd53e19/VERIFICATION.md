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

A legal indicator word has <=1 marker, or equal marker spacing k>=2 with both end gaps <k. For n>=2 this yields exactly n+floor(n^2/4) binary words, each with q^n independent symbol lifts. Minimal forbidden indicators are 11 and, for each k>=2, 0^k10^(k-1)1 and 10^(k-1)10^k; their colored counts are q^2 or 2q^(2k+1). Each k>=2 component is a cyclic k-phase full q-shift with a unique Bernoulli maximal-entropy measure; the at-most-one-marker component contributes only the B full q-shift under invariant measures. Thus precisely countably many ergodic MME. Fixed points q^n sigma_1(n) and product zeta follow divisor sums. Independent enumeration of all binary words n=2..13 verified the exact word and minimal forbiddens; these scans are not a universal proof.

## originality

PASS

Wu–Zhang Theorem A requires strict entropy gap for finiteness; their Example 1(2) displays an equality-class forbidden-word construction, but the inspected full text has a different four-letter boundary structure and does not supply this simultaneous infinite-phase periodic-marker census. Prior Resultary spacing and sparse-periodic shift findings have distinct entropy phases and zeta laws. Arithmetic marker union gives an explicit equality-boundary counterexample with a complete antidictionary rather than a restatement of strict-gap theory.

## value

PASS

The equality boundary of a meaningful finite-MME entropy criterion is sharp: an explicit nontransitive positive-entropy subshift has infinitely many maximal measures at h_M=h_top, with exact forbidden-word census and partition-form zeta. The complete construction is independently useful for symbolic dynamics and clearly states its nontransitive limitation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
