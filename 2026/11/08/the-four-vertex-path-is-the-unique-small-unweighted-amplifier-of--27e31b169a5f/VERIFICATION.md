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

# Reproducible exact checks

Run `python3 verify.py` with Python 3. The program uses only `fractions.Fraction` and `itertools`. It lists all 64 labeled undirected simple graphs on four vertices, filters the 38 connected ones, and performs exact rational polynomial checks also on all connected two- and three-vertex graphs. Nine representative generalized characteristic polynomials, graph class multiplicities and the rational witness are checked. Expected output ends with `PASS: 43 connected labeled graphs; 9 exact characteristic polynomials and rational witness.` This output was observed from the embedded program before preparation.

The checker constructs each neighbor-averaging matrix directly from the graph and evaluates determinants by signed permutation expansion, not by floating-point eigenvalue approximations. The exact roots and positivity/nonpositivity in the mathematical proof follow from the factored polynomials and the two-dimensional reflection reduction; the code alone is not a proof for real-valued opinions or larger networks. The precise claim requires only graphs with at most four vertices, no self-loops, no edge weights, and one synchronous step.

Independent scientific verification was not performed.
