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

# Verification of the orbit-space classification

The accompanying `verify.py` runs as a standalone Python 3 script with no nonstandard dependencies. Execute `python3 verify.py` in the directory containing the script. `verification_output.txt` contains the complete expected output.

The verifier enumerates allowed signatures by partitions of at most four colors, and independently enumerates every actual labeled multipath face in the fully bidirected complete bipartite digraph for \(1\le n\le5\), testing equality of their full orbit signature sets. The direct enumerations count respectively 6, 32, 114, 312 and 710 labeled nonempty faces. The predicted orbit CW cell vectors are \((4,2,0,0)\), \((4,8,4,0)\), \((4,8,8,2)\), and \((4,8,8,3)\) at \(n=1,2,3,4\), remaining constant for \(n\ge4\).

The script checks every prescribed eleven-pair free-face collapse at \(n=4\) against all surviving cofaces. The signature argument proves that the same check applies to all \(n\ge4\), without an extrapolation assumption. It checks four free-face collapses at \(n=3\), verifies the remaining closed-surface links and face incidences, and verifies the smaller \(n=1,2\) descriptions. It terminates with `ALL_VERIFY_OK` only when every assertion holds.

The tests directly corroborate the proof; the unrestricted theorem is the explicit partition-signature classification and collapse sequence in `RESULT.md`. These checks do not provide independent external review or cover different graph families/actions.
