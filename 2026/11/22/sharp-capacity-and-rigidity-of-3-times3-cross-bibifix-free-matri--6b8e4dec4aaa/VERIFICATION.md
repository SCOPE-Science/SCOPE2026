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

# Verification performed

- The proof reduces the full code problem to \(abq^2\) disjoint complete bipartite conflict components and isolated vertices for any disjoint corner sets \(A,B\).
- `check_binary_optima.py` directly generated binary matrices and overlap edges. Each of two oriented candidate graphs has \(128\) vertices and splits into four \(K_{16,16}\) components, giving \(16\) optimal codebooks per orientation; all \(32\) satisfy both overlap conditions. Exactly four distinct complete-cylinder lifts are checked; the remaining 28 optimum codebooks are non-lifts.
- Independently, `check_milp.py` solved each binary oriented graph as a \(128\)-variable binary integer program with \(1024\) overlap constraints, returning optimum \(64\) twice. Requires SciPy.
- `check_exhaustive.py` enumerated full candidate matrix sets for the indicated corner partitions with alphabets of sizes \(2,3,4\), checked the component decomposition and every selected code's validity, and checked the integer optimization through alphabet size \(500\).

Finite checks do not certify unbounded parameters; the symbolic conflict-graph proof supplies those. This is not an independently audited or externally certified proof.
