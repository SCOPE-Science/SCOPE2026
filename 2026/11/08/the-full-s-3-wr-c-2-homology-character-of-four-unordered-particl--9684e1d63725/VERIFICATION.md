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

# Reproducible verification

The graph is the simple complete bipartite graph with first part `0,1,2` and second part `3,4,5`, edges in lexicographic order. All programs require only the Python 3 standard library. With the embedded artifacts extracted into one directory, execute the following commands:

```
python try_k33_4.py > mod_rank_output.txt
python k33_smith_assert.py > smith_assert_output.txt
python try_k33_char.py > character_output.txt
python k33_chaincheck.py > chain_output.txt
python k33_lformula.py > formula_output.txt
python k33_irreps.py > irreps_output.txt
```

`try_k33_4.py` builds all 6,855 chain bases in five degrees, checks every boundary-square column and obtains exact finite-field ranks. `k33_smith_assert.py` uses unimodular cancellations and asserts each Smith invariant and the rank-one residual with divisor two (the cancellation algorithm is implemented in `integer_pivot_k33.py`). `try_k33_char.py` enumerates all 72 automorphisms, calculates direct alternating chain traces, obtains a degree-three homology generator modulo 101 and verifies its action, producing `k33four_chars.json` with explicit class functions and signed chain traces. `k33_chaincheck.py` checks all chain-map equations for five group generators. `k33_lformula.py` reproduces all 72 alternating traces via a separate combinatorial orbit-coefficient formula. `k33_irreps.py` checks the nine conjugacy-class sizes, computes all irreducible characters and their inner products, and verifies the decomposition. The resulting output files and JSON contain the evaluated values and can be compared with the included recorded outputs.

A finite modular rank alone is **not** an integral Smith form. The integer routine performs exact row/column operations and verifies the remaining factor-two matrix. The modular calculation of the top action is decisive only because the integral top group is previously shown to be rank-one free, constraining each induced automorphism to \(\pm1\). No infinite classification, integral representation lattice, or independent external audit is asserted.
