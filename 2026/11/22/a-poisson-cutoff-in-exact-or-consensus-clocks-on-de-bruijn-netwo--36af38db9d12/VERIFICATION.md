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

# Reproducibility of the exact hitting-time census

Run `python3 verify_exhaustive.py` and `python3 verify_reachability.py` in the directory containing these files. They use only the Python standard library. Actual recorded outputs are `exhaustive_output.txt` and `reachability_output.txt`; both programs were executed from those paths with their outputs regenerated. All checks terminated successfully.

The first program evolves all \(2^{q^d}\) states for \((q,d)\in\{(2,1),(2,2),(2,3),(2,4),(3,1),(3,2)\}\), determines the actual least full-activity entry, and compares its complete frequency distribution against the exact formula. It then checks a separate suffix-projection criterion against direct evolution for 2,000 pseudorandom initial states across \((2,5)\) and \((3,3)\).

The second program explicitly generates the graph arcs and constructs exact length-\(t\) walk reachability sets, comparing them with the proposed suffix/prefix overlaps at each allowed time in all six small graphs. It separately counts block assignments where tractable and verifies the exact rational mean of missing classes on several critical binary dimensions. The sample computations do not substitute for the all-size word-walk proof or the binomial-to-Poisson argument. In particular, no program attempts exhaustive enumeration of exponentially large graphs.

The proof also covers the boundaries \(d=1\), \(t=0\), \(t=d\), the all-zero nonhitting fixed point, and every integer alphabet size \(q\ge2\). No independent mathematical audit has yet been performed.
