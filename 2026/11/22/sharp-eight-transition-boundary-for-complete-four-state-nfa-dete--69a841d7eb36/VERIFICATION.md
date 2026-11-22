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

# Reproducibility

Use a C++17 compiler, for example `g++ -std=c++17 -O3 verify_sparse_4_full.cpp -o full && ./full`, and analogously for `verify_sparse_4_independent.cpp`.

The first program checks every labeled transition relation with \(0\) through \(8\) edges, and every final subset whenever all \(16\) subsets are reachable. Its recorded edge-budget outputs for \(e=0,\ldots,8\) are \(0,0,0,0,0,0,0,0,5808\) for full subset reachability, and \(56{,}544\) full-minimal cases at \(e=8\). It includes an explicit witness, encoded by the eight-edge mask `19141260` and final mask `2`.

The second program independently loops over all \(10{,}518{,}300\) eight-edge relations and applies iterative distinguishability of every pair of subsets (not class partition refinement). Its full-reach count is \(5{,}808\); its full-minimal count is \(56{,}544\); the results agree for all fifteen nonempty final masks.

These are complete finite computations; they do not establish the analogous threshold for more than four states. Compiler execution logs are not substituted for the source algorithms and numerical coverage arguments. Independent audit has not been performed.
