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

Run `python3 decagon_exact.py` in an environment supporting Python 3 standard library `fractions`, `functools`, `collections`, and `math`. The program uses exact arithmetic in the real field \(\mathbb Q(\sqrt5)\) and checks:

- 45 source segments and all pairwise intersections, exactly split into a 171-vertex, 390-edge planar graph with 221 faces and 220 bounded faces.
- Twelve distinct exact normalized area values, with multiplicities totaling 220, sum of all normalized cell areas one, and total transformed polygon area five.
- An explicit set of six distinct bounded faces totaling exactly \(1/20\) of the polygon's area.
- Exhaustion of 6,186 nondecreasing-prefix states for up to five area classes, with no exact target \(1/20\) and justified positive-area pruning, followed by all size-six multisets, exactly two solutions and 8,778,000 distinct minimizing six-cell subsets by binomial counting.

Any failed check raises an assertion. All comparisons and all equalities used by the certificate are exact; displayed decimals are only diagnostic. The verified domain is the single regular ten-gon with its complete vertex-chord arrangement. This certificate has not undergone independent third-party audit.
