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

# Reproducibility checks

The available artifacts include three stand-alone exact verifiers, all of which were executed against the final code contents:

* `verify_bruteforce.cpp`: C++17 (`c++ -std=c++17 -O2 verify_bruteforce.cpp -o verify_bruteforce && ./verify_bruteforce 3 9`); enumerates valid root-edge subsets for every root order from 3 through 9, checks the degree inequality and every possible single-edge extension, and reproduces `exhaustive_counts.tsv`.
* `verify_incidence.py`: `python3 verify_incidence.py`; directly constructs closed neighborhoods and enumerates every vertex subset for root orders 3 through 7, without using the root-degree identity, and reproduces `incidence_counts.tsv`.
* `verify_formula.py`: `python3 verify_formula.py`; independently evaluates factorial component counts and their inclusion-maximal constraints for root orders 3 through 11, reproducing `formula_counts.tsv`.

The pair of programs in the first two bullets has different mathematical implementation strategies, whereas the third checks the stated symbolic counting consequences. Exact coefficient-by-coefficient comparisons were made for every common checked order; they agreed. Example maximal coefficients: at root order seven, sizes three/four/five have multiplicities 140/1260/105; at root order eight, sizes three/five have multiplicities 280/3360; at root order nine, sizes three/five/six have multiplicities 504/22680/1260.

All-orders correctness rests on the root-degree classification and factorial component counting in RESULT.md, not finite enumeration. These checks are neither an independent mathematical audit nor verification for arbitrary line graphs or capacities.
