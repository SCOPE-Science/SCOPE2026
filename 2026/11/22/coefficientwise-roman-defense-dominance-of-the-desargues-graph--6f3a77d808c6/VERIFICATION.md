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

The two required programs are self-contained, with no external data downloads and no external Python libraries. Execute from the package root:

```bash
g++ -O2 -std=c++17 checks/verify_gp_roman.cpp -o verify_gp_roman
./verify_gp_roman
python3 checks/verify_poly_independent.py
```

The C++ verifier constructs the two generalized Petersen graphs, checks their cubic adjacency, examines each of \(1{,}048{,}576\) distinct two-labelled supports in each graph, computes the polynomial coefficients by exact binomial coefficients, and checks the exact factorization, zero and positive coefficient ranges, known minimum counts, and aggregate counts. The independent Python verifier uses different adjacency arrays, explicit isomorphism permutations to generalized Petersen coordinates, and independently tabulates all support classes. It rechecks every polynomial and support-histogram integer in `data/roman_census.json` and validates the universal counting lemma against all \(3^{10}\) functions on a separate Petersen control graph. Both programs must terminate with their PASS lines.

Critical expected values: the two minimum weights are both \(12\), their weight-\(12\) coefficients are \(20\) and \(340\), and their total counts are \(742{,}721{,}362\) and \(754{,}088{,}530\). The difference is zero for weights outside \(12\)–\(29\); it is strictly positive at each integer weight inside that range and equals \(4z^{12}(1+z)^6Q(z)\) with the exact twelve-coefficient \(Q\) supplied in the theorem and the table.

**Limits:** The computation certifies only the fully specified twenty-vertex graphs. It does not establish a corresponding infinite-family theorem or an explicit injection. Reproducibility and a self-review do not constitute independent external audit.
