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

# Verification record

The finite certificate is `verify_support.py`, with captured output in `support_output.txt`. It enumerates all 3375 possible nonempty support triples, checks the universal four-step identity after time six and the full color transport, then computes the ordered-support-size coefficients for primitive-four configurations. It reports 620 initially periodic support triples: one fixed and 619 primitive four-cyclic, and the support first-entry counts 620, 248, 658, 739, 641, 391, 78 at steps zero through six.

The independent state-level implementation `verify_direct.py` exhaustively checks the actual labelled dynamics on 27 parameter triples with each shore size one, two or three, covering 592704 initial configurations. It verifies the periods, latest entry time, and 16-term orbit polynomial; it additionally tests the sharp witness on the four-vertex graph. Both programs were run directly from the documented package files and their output logs are included verbatim.

The unrestricted conclusion is supported by the proof that the finite mask quotient and its color-transport maps exactly describe all graph sizes. Direct small-system enumeration by itself would not establish that conclusion. Historical priority remains qualified; no independent mathematical audit has been performed.
