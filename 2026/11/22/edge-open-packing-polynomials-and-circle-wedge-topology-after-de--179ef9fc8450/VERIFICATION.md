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
# Reproducible mathematical checks

The proof in `RESULT.md` classifies all edge-open packing sets, identifies their inclusion-maximal members, and applies the simplicial nerve lemma plus one-simplex attachments to give the integral homotopy equivalence. These are the unrestricted arguments; executable tests cover finite parameters only.

- `python3 artifacts/check_small.py` runs a direct three-distinct-edge test for every pair, an exhaustive edge-subset enumeration, and an extension test for inclusion-maximality. **17 cases passed**, including all deletion counts for shore sizes \((3,3)\), \((3,4)\), \((4,4)\) and \((3,5)\). Actual output: `artifacts/check_small.log`.
- `c++ -O3 -std=c++17 artifacts/check_fast.cpp -o check_fast && ./check_fast` independently enumerates compatible subsets via a conflict-bitmask dynamic program and counts maximal subsets. **33 cases passed**, restricted to manageable edge counts. Actual output: `artifacts/check_fast.log`.
- `python3 artifacts/check_topology.py` constructs the small edge-open-packing simplicial complexes from literal third-edge compatibility tests and computes boundary ranks over \(\mathbb F_2\). **Six cases passed**, with \(\beta_0=1\), \(\beta_1=(m-1)(n-1)-t+\binom t2\), and vanishing higher Betti numbers. Actual output: `artifacts/check_topology.log`.

The homology checker uses \(\mathbb F_2\), so does not exclude torsion on its own; the integral, all-parameter assertion follows separately from the simplicial nerve equivalence and explicit one-simplex attachments. No outside source independently audited the proof.
