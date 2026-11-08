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

Exact source checks: `verify_orbits.py` independently constructs all 255 orbit patterns from set partitions of up to six indices and enumerates every possible one-pebble move. `verify_direct.py` enumerates all concrete three-variable assignments, their atomic diagrams, and all variable replacements over each of the six finite semigroups. Both derive the same rank partition and terminal rank-four stabilization, with their outputs preserved in `orbit_output.txt` and `direct_output.txt`.

The unrestricted upper bound for index sizes at least six is a separate mathematical argument: after one move there are at most four fixed endpoint labels and at most two labels to be added. The finite calculations prove only the exceptional index comparisons, not anything about untested larger structures.

No independent mathematical review or external certification has been performed. The relevant language contains a named zero and a ternary multiplication relation, not a binary multiplication function.
