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

# Exact finite verification

From the package root, run `g++ -std=c++17 -O2 -Wall -Wextra verification/peeling.cpp -o plurality_peeling` then `./plurality_peeling`, and compare with `verification/peeling_output.txt`. Run `python3 verification/direct_trace.py` and compare with `verification/direct_trace_output.txt`. These exact commands were executed against the actual embedded paths and both emitted byte-identical output to the accompanying certificates.

The C++ enumerator visits every integer in \(\{0,\ldots,59048\}\), computes the graph transition using the explicit trit tie rule, deletes indegree-zero states, identifies all directed cycles, and propagates first-entry time, orbit ID and eventual period backwards. Its complete printed entry and basin histograms sum to \(59{,}049\) for each graph. The Python checker constructs neighborhood sets independently, evaluates plurality by counting votes, and traces every trajectory until repetition. It separately enumerates the binary majority dynamics on all \(2^{10}\) states per graph. Its complete outputs exactly match the C++ ternary counts.

The witnesses with maximal preperiods of \(5\) and \(7\) updates are printed as exact base-three state integers. Because the entire finite state set is enumerated, no unobserved finite-state orbit is being extrapolated away. These computations prove only the stated finite numerical claim. Search-based novelty comparison does not prove absolute priority. Independent external scientific verification has not been performed.
