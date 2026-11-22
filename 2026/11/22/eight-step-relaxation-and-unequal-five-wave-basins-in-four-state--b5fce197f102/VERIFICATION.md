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

# Reproducibility and proof limits

The finite domain is exactly \(4^{10}=1{,}048{,}576\) four-color assignments on the ten labelled vertices of the pentagonal prism. The two embedded programs independently construct the graph and evaluate the local four-state Greenberg–Hastings rule on every assignment. The exact counting algorithm is a complete finite proof for this domain, not sampling.

Run from the directory containing `verification`:

```sh
python3 verification/verify_prism_stdlib.py > /tmp/prism_python_stdout.txt
c++ -std=c++17 -O2 verification/verify_prism_indegree.cpp -o /tmp/prism_indegree
/tmp/prism_indegree > /tmp/prism_cpp_stdout.txt
cmp /tmp/prism_python_stdout.txt verification/python_results.txt
cmp /tmp/prism_cpp_stdout.txt verification/cpp_results.txt
```

The Python program uses only the standard library and path-marked functional-graph reconstruction. The C++17 program uses independent transition construction and indegree pruning. Both compute complete \((T,P)\) histograms, independently agreeing on every nonzero cell in `verification/census.csv`. The Python program additionally enumerates all twenty spatial automorphisms, every temporal orbit's canonical representative and basin, and the single spatial class of all twenty maximally delayed states. C++ independently verifies the global equality \(F^{28}=F^8\) on every state and the sharp failure \(F^{27}=F^7\) on exactly twenty states. The output files store exact recorded results; the programs actually reconstruct them.

This is a self-contained finite enumeration and does not prove the same classification for any other graph or color count. No external independent audit has been performed.
