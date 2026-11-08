---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Run `python3 verify.py` with standard Python 3. The checker regenerates all unordered full binary shapes for \(2\le n\le11\), counts clade profiles, and uses exact rational Sturm sequences to count distinct interior crossing roots for each distinct profile pair. Expected shape totals are \(1,1,2,3,6,11,23,46,98,207\), with \(194\) distinct mean profiles at eleven leaves and exactly \(15\) pairs possessing two interior roots. The program also checks two witness clade vectors and directly enumerates \(2^{11}\) survival masks at each of three exact rational extinction probabilities. The expected final output is `ALL_EXACT_CHECKS_PASSED`.

The positive all-size result follows from the explicit factorization and a common-root graft, not from finite enumeration. The minimality result depends on complete shape generation and exact Sturm root counting through ten leaves. A separate symbolic-algebra implementation reproduced the enumeration, and gcd checks showed square-free interiors for all fifteen two-root pairs. External independent audit has not been performed.
