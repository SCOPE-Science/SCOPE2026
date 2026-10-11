---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The hierarchy (1,2,3,5) is correct. Independently over GF(9)=GF(3)[i]/(i^2+1), the three generator rows of the x-i primary component have full GF(3) rank-support dimension four. The combinations i*r0+r1=(1,0,1,0) and i*r1+r2=(0,1,0,1) give a two-dimensional base-field subcode, hence component weights (1,2,4). The (x+1)^2 component is one-dimensional with weight one. Applying the published direct-sum convolution gives (1,2,3,5).

## originality

FAIL

The numerical middle weights are not printed in the source, but the claim is covered under the required implication standard: it is a routine specialization of Berhuy–Molina’s own primary-decomposition/convolution theorem to their Example 4.3, together with immediate base-field words in the displayed component. Special cases and corollaries count as prior coverage even when the final tuple is not written verbatim.

## value

FAIL

Completing two unstated entries of a single published benchmark by a direct application of the same paper’s decomposition theorem and two immediate base-field words is a routine specialization, not a motivated new structural gap under the value bar. Its usefulness as a regression example does not overcome the rule rejecting textbook/routine deductions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
