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

# Verification of the Fano pair-type obstruction

Run `python3 VERIFY.py` with the Python 3 standard library. The program enumerates Steiner triple systems of order seven using exact cover on all 21 unordered pairs; there are exactly 30 labeled designs. It checks all 45 two-edge old five-point bases: precisely the 15 pairs of triples meeting once have two completions each, and all other pairs have none. It verifies the sole common required new triple for each pair of completions.

For the canonical bow tie it checks all 32 fixed mutual-link sets algebraically. It also independently visits all 1,048,576 assignments to the 20 single-new-vertex triples under the central mutual-link bit being fixed to one; exactly 921,600 assignments avoid both forbidden completions. Its exact arithmetic checks the total 31,522,816, correction 481/512, central bias 225/481, and total-variation distance 93/7696. The captured output appears in `CHECKS.txt`.

These are complete finite checks for the seven-point obstruction and the claimed five-parameter classification, not a general classification of denser bases or a proof for arbitrary forbidden hypergraphs. The mathematical proof in `RESULT.md` supplies the justification of the extension-to-type correspondence, the two checkerboard completions and the conditional independence law.
