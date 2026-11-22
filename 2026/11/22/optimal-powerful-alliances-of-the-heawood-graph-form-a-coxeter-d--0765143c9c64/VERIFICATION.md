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

# Verification and reproducibility

The decisive symbolic checks are: (i) the cubic majority characterization, (ii) the crossing-edge lower bound and odd-perfect-matching exclusion, (iii) the projective-plane cap restrictions and the four-point decomposition relative to a nonconcurrent line triple, and (iv) the ordered-disjoint-triangle bijection and line-graph adjacency equivalence. All are proved in RESULT.md.

Two independent implementations operate directly on the Fano incidence convention \(\ell_i=\{i,i+1,i+3\}\) modulo \(7\):

- `python3 check_geometry.py` constructs Coxeter triangle pairs, independently scans all 16,384 initial subsets and checks every optimum, jump and shortest-path distance.
- `g++ -O2 -std=c++17 check_bruteforce.cpp -o check_bruteforce && ./check_bruteforce` performs a standalone direct bitmask test and independent breadth-first traversals.

Observed results from the packaged source files: Python reports 28 Fano triangles, 84 optimizers, 168 jump edges, zero token slides and uniform distance profile \((1,4,8,16,28,22,4,1)\). C++17 independently reports 84, 168, zero and diameter seven. The direct 16,384-subset scan also confirms there is no global powerful alliance below size eight.

The exact line-graph isomorphism and orbit transitivity follow symbolically; the verification programs do not replace those proofs. These checks do not establish publication priority or independently certified proof correctness.
