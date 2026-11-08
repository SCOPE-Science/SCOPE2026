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

# Reproducible finite verification

Run `python3 verify.py` in the directory containing `verify.py`, `counts.tsv`, `noc_incremental.cpp`, and `noc_direct.cpp`. The runner needs `g++` supporting C++17 and Python 3.10 or newer. It makes no internet requests and writes temporary executables outside the source directory.

The runner first parses the 15 entries of `counts.tsv` and checks all reference integers. A naive independently implemented Python enumerator tests every optional-cluster family for ground-set sizes two, three and four; accepted families are assigned their Hasse parent counts directly. Each C++ enumerator is then compiled and run for every size two through six. The incremental enumerator uses maintained witness sets, descending-cardinality cluster order, and certified hereditary pruning. The other enumerator computes NOC conditions from scratch in increasing-mask order and implements its own cover relation. All ten C++ histograms agree with the table. The executable verification ended:

```
CPP_CENSUS_OK noc_incremental.cpp 6 9654368
CPP_CENSUS_OK noc_direct.cpp 6 9654368
VERIFY_OK 2 independent full six-leaf enumerators; naive small-n control
```

The equality and reticulation transfer to strong-phylogenetic normal networks use Lindeberg and Hellmuth's published Corollary 11. The computations certify only the stated finite domains; they do not give an infinite formula, statistical estimate, or independent peer validation.
