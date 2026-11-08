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

# Reproducible verification and limitations

Run `python3 verify.py` with the Python 3 standard library. This script generates the initial binary configurations, simulates synchronous firing and absorption at the final sink, constructs all nonempty simplices, and checks every proposed elementary collapse for a unique coface. It independently computes mod-two simplicial homology for smaller parameters using explicit boundary matrices represented by bit vectors.

A successful run reports:

`ALL_VERIFY_OK cases=156 n_range=5..28 face_instances=14196 elementary_pairs=5772 independent_mod2_cases=42`

The 156 collapse replays cover integers \(3\le L\le14\) and \(0\le t\le12\); the 42 independent mod-two checks use \(3\le L\le8\), \(0\le t\le6\). The script checks the actual complex after each dominated-vertex deletion against the complex generated for the shortened path and confirms the terminal polygon exactly. The mathematical proof does not depend on these parameter cutoffs. The checked mod-two groups do not alone establish integral homology: the unrestricted integral conclusion follows from explicit simplicial collapses.

The paper source's sandpile convention excludes the absorbing sink from firing sets. No external validator has assessed this work. The accompanying proof and executable are self-contained except for the cited definition of avalanche complexes and previously published three-grain comparison.
