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

# Reproducibility and scientific limits

The package includes `verify_python.py` and `verify_cpp.cpp`, both readable standalone source files. In a directory containing them, run:

```
python3 verify_python.py
g++ -std=c++17 -O2 verify_cpp.cpp -o verify_cpp
./verify_cpp
```

The projective-coordinate Python computation recovers 234 noncollinear point triangles and 234 point ovals, validates all 468 geometric minimizers and every inclusion edge, and checks a breadth-first-search histogram from every state. The independent C++17 affine-coordinate program constructs the incidence graph from 9 affine and 4 infinite points and 12 affine plus one infinity line. It exhaustively checks every subset of sizes one to seven using the original outside-vertex neighbourhood criterion, finds no optimum smaller than seven, counts exactly 234+234 minimum configurations, checks all one-vertex replacements, and computes all 468 shortest-path profiles. Both report a degree-four graph on 468 vertices, 936 edges, diameter nine, and common profile `(1,4,12,30,60,96,114,96,47,8)`.

No random sampling or unbounded-order inference occurs. The proof is structural for the optimum classification, and the finite graph metric uses independently reproduced exhaustive code; it is not an external certification. No independent audit has been performed.
