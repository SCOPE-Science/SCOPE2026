---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In the fixed-root tree model the only vertices whose reachability is changed by vaccinating v are its descendants, each reached without the intervention with probability p to the power of its root depth. A deeper candidate is strictly dominated by its root-neighbor ancestor at every interior p. If one eligible candidate is optimal at two parameters but not at an intermediate one, fix one competitor that beats it strictly in the middle. Their nonzero difference has two distinct interior roots even if either endpoint is a tie. Their two disjoint branch profiles have combined size at most 12 for n<=13; each tail is exactly a positive composition of the branch size minus one, including the empty tail. I reproduced the exhaustive bound with an independently written standard-library certificate at /workspace/review-evidence/4_profile_certificate.py, run with python3. Bit-mask separators generate all 6144 ordered pairs; ordinary Descartes leaves 150, and exact integer coefficients of (1+t)^d Q(t/(1+t)) give zero variations for 140 and one for 10, none with two. Since t>0 corresponds exactly to 0<p<1, the certificate also excludes isolated multiple roots that could affect the tie-inclusive definition. The 14-vertex witness gives the stated quartic times -p^2; the quartic is positive at 0 and 1 and negative at 1/2, with exactly two positive roots by Descartes. These are simple and the switch intervals and strict dominance follow. Decimal bisection independently agrees with the stated roots. The reviewed frozen code was not executed; its recorded exact checks are consistent with the separate polynomial certificate.

## originality

FAIL

The sharp threshold and underlying complete two-profile comparison are mathematically covered by the distinct indexed 14-site gateway-closure finding. Root-neighbor vaccination and closing the corresponding outbound root edge have exactly the same benefit. The indexed integer certificate excludes every pair with two interior roots, not just two strict reversals, and so also covers the original's broader definition with ties. The original uses a different 14-vertex witness, but not a distinct threshold or an independently motivated exact invariant of that witness. This is a finding of substantive equivalent coverage in the inspected corpus, not a conclusion about which work was disclosed first or borrowed from which.

## value

FAIL

A first possible size for this sort of reentrance is a meaningful finite boundary, and the abstract tree proof is sound. In the inspected corpus that boundary is already mathematically covered, including two-root exclusion and a minimal two-switch witness. Recasting edge closure as vertex vaccination preserves the exact two-profile objective. The remaining different quartic witness and its precise switch points do not answer a motivated further question, such as classifying all minimal witnesses. No separately valuable new remainder was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
