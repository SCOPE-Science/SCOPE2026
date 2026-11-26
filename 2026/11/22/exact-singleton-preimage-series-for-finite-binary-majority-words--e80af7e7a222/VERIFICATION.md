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

The before-reading state counts each two-bit starting pair once. Appending a bit gives exactly one new input realization for each compatible previous realization and endpoint pair. The end pairs are all counted; no end constraint is imposed. Saturation at two preserves the exact-one predicate because no contributions are negative. An independent present/multiple-set construction yielded 30 reachable states, four accepting, and no edge back to the start. The whole-vector residual of the degree-nine polynomial is -2 at the start and zero elsewhere; applying the transition operator kills that residual. This gives the recurrence for every m>=1 (not at m=0), and exact low coefficients give the displayed numerator. All 16 listed counts and a separate brute-force histogram through m=12 agreed.

## originality

PASS

The contribution is the evaluated singleton count over all unrestricted-end output words by length, not the pointwise predecessor recurrence or the existence of a finite-state representation. The strongest same-day periodic singleton result is a material neighbor but assesses different fibers, and the closest classical pointwise formula does not evaluate this global threshold count.

## value

PASS

An attainable observation need not determine the unobserved source word, including its two end bits. The all-length singleton spectrum resolves this exact finite reconstruction invariant for a classical local rule. It gives both an effective test for an individual target and a recurrence for how many targets pass, complementing the earlier image-language and per-target counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
