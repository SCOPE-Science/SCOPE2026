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

The full all-size argument derives every update using the number of ones outside a complementary pair; there are no numerical assumptions about the graph size beyond \(n\ge2\).

Run `python3 verify_direct.py`: every initial state for both the \(2n\)-vertex and \(2n+1\)-vertex graph is updated by an independently implemented vertex-neighborhood calculation for \(2\le n\le8\). Checks: fixed and primitive-two populations, two-iterate periodicity bounds, and maximum first entry. The run checks \(262128\) labelled states; exact output is in `direct_output.txt`.

Run `python3 verify_weighted_types.py`: a separate multinomial weighted enumeration over all \(00\), \(11\), and both mixed-pair types for \(2\le n\le60\) verifies the two exact fixed-point and primitive-two formulas, with center inclusion and compressed updates; output in `weighted_output.txt`. Pair-type checking is not an independent infinite proof, and loses the orientations of mixed pairs; the direct checker retains and updates these orientations.

Limits: the complete proof, not the bounded computations, certifies arbitrary \(n\). This record makes no assertion about independent external verification or prior-literature priority.
