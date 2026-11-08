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
# Verification of the exact two-block sumset theorem

Run `python3 verify.py` from this directory with the Python 3 standard library. Output is embedded in `verification_output.txt` and was reproduced from the packaged script. The checker uses three independently coded finite cardinality calculations: bitset iterated sums, unions of integer intervals, and the closed adjacent-gap formula. The direct 5940 cases cover all block-length pairs from one through six, 15 successive choices of the inter-block start, and indices from two through twelve. For 11520 larger parameter triples it checks contiguous positive index support through 81, and in 4940 cases it checks the positive first-overlap boundary.

These are finite computational cross-checks; they do not prove statements for unbounded block parameters or indices. For those, the proof in RESULT.md explicitly establishes the interval sumset decomposition, gap formula, positivity in the disjoint regime, eventual discrete concavity, and positive gluing at the boundary. The assumptions that both blocks contain at least two integers, together with the index constraint \(n\ge2\), are essential to the stated theorem. No independent scientific audit or external validation has been performed.
