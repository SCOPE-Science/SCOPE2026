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
# Reproducibility

The bundled standalone `verify_tree_spline.py` uses only Python's standard library and exact fractions. Run `python3 verify_tree_spline.py`.

The executed program returned:

`EXACT_TREE_SPLINE_OK cases=116 exact_cdf_evaluations=10120 exact_weighted_moment_orders=3 mean_distance_branching_identities=116`

For distinct edges of lengths \(a,b\) with connecting path length \(s\), the independent rectangle CDF contribution is
\[
\frac12\big[(r-s)_+^2-(r-s-a)_+^2-(r-s-b)_+^2+(r-s-a-b)_+^2\big].
\]
For an edge of length \(a\), its same-edge contribution before total-length normalization is \(a^2-(a-r)_+^2\). The verifier sums these edge contributions and compares them exactly to the degree-deficit spline across a deterministic collection of 116 trees and 10,120 rational radii. It additionally checks \(S_1=2L\), \(S_2=2L^2\), and \(S_3=2L^3-12\mathcal B(T)\).

These finite rational checks detect computational or algebraic mistakes in tested configurations; they neither exhaust all positive real edge lengths nor constitute independent validation of the theorem. The proof of all positive real cases is in `RESULT.md`.
