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

# Computational verification

The finite result is verified by exhaustive exact-integer enumeration using the two standalone source files in this package.

Run from the extraction directory:

```sh
python3 -S check_python.py
g++ -std=c++17 -O2 -Wall -Wextra check_cpp.cpp -o check_cpp
./check_cpp
```

Both are standard-library-only programs. Both internally specify all \(30\) edges of the twelve-vertex icosahedral graph. The Python script enumerates legal token slides by moving each selected vertex to a neighboring empty vertex. The C++17 program independently finds edges by comparing all pairs of valid bases and then checking that the exchanged positions are adjacent in the original graph.

Both independently find \(160\) metric bases, token-slide degree \(9\) and \(720\) edges, token-jump degree \(21\) and \(1680\) edges, slide eccentricity counts \(20,120,20\) at \(4,5,6\), jump diameter \(3\), and full slide distance counts \(720,2730,4960,3490,810,10\). Each checks all \(12720\) basis pairs and the \(610\) one-slide transport detours using all six token assignments. Python additionally checks all pairwise equidistance witnesses, verifies that no two landmarks resolve, and constructs the unrestricted \(220\)-state three-token graph to check the transport interpretation directly.

The programs have deterministic, finite loops; the bounds of those loops and the exhaustive assertions are inspectable source code. The success messages in `check_python.out` and `check_cpp.out` are convenient replay evidence but do not replace the source. The finite proof does not establish analogues for other graph orders or for other reconfiguration rules.

No independent external review or validation is claimed.
