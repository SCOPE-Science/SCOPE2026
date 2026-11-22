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

Place `verify.py` and `certificates.json` in the same directory and run `python3 verify.py`. No nonstandard Python packages, network access, cached graphs, or earlier-run artifacts are necessary.

The verifier exhaustively enumerates \(\operatorname{Av}_n(\tau)\) for every \(\tau\in S_3\), \(1\le n\le5\), and checks all adjacent-position-swap outputs. A separate Kendall-distance calculation checks every compatibility edge. One exact Bron–Kerbosch algorithm enumerates maximal codebooks; another increasing-index search counts every codebook of the asserted maximum size and excludes the next size. Both give the same capacities and optimizer counts for the two representative pattern classes. Reversal and complementation, together with direct six-pattern traversal, verify the complete classification.

For the fractional program, exact rational sparse primal and dual witnesses are supplied for representatives \(123\) and \(132\) at lengths three, four and five. The checker regenerates all source and output indices and checks every input-cover and output-packing inequality with `fractions.Fraction`, then verifies equality of objective sums. Lengths one and two are immediate by full-ball intersection.

In the package replay, the last line was `VERIFY_OK`. Exhaustive finite computations are valid for the stated bounded instances only; the result makes no claim about higher-order capacities or external independent mathematical validation.
