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

# Verification information

The stand-alone `verify.py` uses only the Python 3 standard library. From the directory containing `verify.py`, run `python3 verify.py` and compare its printed output with `verifier_output.txt`.

For every integer \(9\le n\le22\), the program constructs all connected triples, admissible four-sets and every element of the dihedral action, then verifies the complete signed relative-chain character equality against the closed formula (434 elements total). It checks the absence of admissible five-sets for \(9\le n\le14\). It independently constructs the **ordinary** cut complex, enumerates every invariant oriented simplex under every group element and verifies its Lefschetz traces for \(9\le n\le12\). For these four values, it also computes every relevant mod-two simplicial boundary rank and checks the predicted homological concentration and top Betti number.

The check is finite and is not a formal proof for every \(n\); the unrestricted argument appears in `RESULT.md` and depends on the cited nonequivariant shellability theorem. Independent external audit has not been performed.
