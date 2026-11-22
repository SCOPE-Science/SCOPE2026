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

Run `python3 CHECK.py` with Python 3 standard library only. Its output is `CHECK_OK 90102 exact assertions`, followed by the initial progression counts. The script rederives the complete set of ten reachable states from the binary carry rule, validates the 40 explicitly listed transitions, and checks the ten identities \(H_i=P f_i+z\sum H_j\) in the ring of integer polynomials. These finite algebraic identities imply the rational generating function for *all* binary digit lengths, because \(I-zM\) is invertible in formal power series. Separate direct enumeration verifies the counts and the absence of four-term progressions through length 12, and the digit rules are independently checked at 30,000 indices.

The mathematical proof of four-term exclusion is induction on the positive common difference and is not inferred from any finite enumeration. The result makes no claim that the absence of indexed prior work certifies novelty; an independent scientific audit has not been performed.
