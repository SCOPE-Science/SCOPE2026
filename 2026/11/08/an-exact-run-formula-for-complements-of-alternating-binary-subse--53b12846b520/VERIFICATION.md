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

The standard-library Python file `verify_alt_complements.py` returned `ALTERNATING_COMPLEMENT_VERIFY_OK direct_pairs 45 independent_dp_words 23535`.

The first check directly enumerates every position subset selecting the deleted pattern, constructs the entire remainder set, and compares it against the structural formula for every parameter pair with \(0\leq k\leq n\leq8\). The second implements a separate two-pointer shuffle dynamic program and tests **all** balanced binary words of size \(2r\) for \(0\leq r\leq7\) and \(0\leq k\leq4\); it compares membership against the predicted pair-run condition, including non-paired words.

A further seeded check of 4,000 random paired words with \(0\leq r<55\) and \(0\leq k<36\) passed. Neither finite test is offered as a proof for arbitrary lengths. The unbounded conclusion rests on the balance and constructive interleaving lemmas in RESULT.md.

Reproduction: execute `python3 verify_alt_complements.py`. No network, external library, data file, random seed or other artifact is required for the deterministic main verification.
