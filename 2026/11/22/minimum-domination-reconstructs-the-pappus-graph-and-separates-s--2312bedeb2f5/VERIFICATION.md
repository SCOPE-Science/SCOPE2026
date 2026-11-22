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

# Reproducibility and limits

The two source files work independently and generate the recorded output using only the Python standard library and the C++17 standard library.

From this directory:

```bash
python3 verify_python.py
c++ -O2 -std=c++17 -Wall -Wextra verify_cpp.cpp -o verify_cpp
./verify_cpp
```

`verify_python.py` enumerates every possible dominating set of size at most five (and all small query supports). It independently tests the explicit affine geometry constructions, every vertex frequency, every pair-concurrence type and every triple trace, and gives concrete branch queries for adaptive depth three.

`verify_cpp.cpp` uses independent loops over every nonempty subset of the eighteen graph vertices (262143 cases), without assuming the geometric characterization, then confirms the optimizer count and shattering profile.

The source model is an incidence graph of nine points and nine lines in a three-class affine net. This is the Pappus graph (the fourth direction of the affine plane of order three is omitted). Both programs label the points by integers zero through eight and the retained lines by nine through seventeen. No preexisting graph or result files are loaded.

The mathematical proof derives the classification and shattering theorem without relying on finite sample extrapolation. The numerical check is exhaustive for this *single* eighteen-vertex graph, not for other incidence structures or generalized Pappus graphs. The verified result is not a claim of historical priority or independent certification.
