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

# Verification of the Heawood edge-general-position census

The graph is defined from the Fano lines \(L_j=\{j,j+1,j+3\}\pmod7\). It has 14 vertices, 21 edges and diameter three. Each of its 28 nonincident point-line pairs gives exactly three three-edge geodesics: hence precisely 84 forbidden 3-edge subsets.

## Reproduction

From the directory containing the files:

```sh
g++ -O2 -std=c++17 verify_fano.cpp -o verify_fano
./verify_fano
python3 verify_bfs.py
```

The first program uses a geometric forbidden-triple construction and exhaustive 21-bit recurrence. The second independently builds graph distances by BFS, enumerates shortest paths and generates valid subsets through DFS. Each evaluates exact integer counts rather than floating-point approximations.

Expected face coefficients for degrees zero through ten: `1 21 210 1246 4725 11592 17962 16446 7875 1617 84`; all later coefficients zero. Expected inclusion-maximal coefficients: degree seven `66`, degree eight `546`, degree nine `861`, degree ten `84`, zero elsewhere. Total face count `61779`, total facet count `1557`.

## Scope and limits

The two computations exhaustively verify one finite graph; no claim about larger projective planes, automorphism orbits, or a general infinite family is made. These reproducible computational checks supplement the explicit correctness argument and do not constitute independent human audit.
