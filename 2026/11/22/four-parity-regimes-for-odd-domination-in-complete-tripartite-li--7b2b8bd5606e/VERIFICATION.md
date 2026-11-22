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

# Reproducible finite verification and proof scope

The universally quantified classification over all positive \(a,b,c\) follows from the two symbolic parity relations (1) and (2) in `RESULT.md`, with the four parity cases proved separately. The computational tests below independently verify instances but are **not** asserted to establish the universal theorem.

Compile and run the exhaustive test from this directory:

```sh
g++ -O2 -std=c++17 verify_direct.cpp -o verify_direct
./verify_direct
```

The direct checker iterates every vertex subset of eleven line graphs (up to 21 vertices), computes the oddness of every closed-neighborhood intersection and tests induced connectivity by graph traversal. The output is recorded in `verify_direct_output.txt` and ends in `ALL_DIRECT_CASES_PASS`.

Independently, run the complete finite-field linear-system enumeration:

```sh
python3 verify_linear.py
```

The second program constructs the entire closed-neighborhood matrix and performs exact binary Gauss–Jordan elimination. It compares all solution-weight coefficients against the theorem and checks connectivity in fourteen examples (up to forty line-graph vertices). Its reference output is `verify_linear_output.txt` and ends in `ALL_GAUSSIAN_CASES_PASS`.

The two checks employ distinct search mechanisms and do not rely on downloaded or precomputed graph data. They do not establish historical uniqueness, imply an independent validation, or verify graphs of unrestricted size by exhaustion.
