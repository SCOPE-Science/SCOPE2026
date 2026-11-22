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

# Reproduction and limits

Run `python check_exact.py` with the Python standard library. It enumerates all \(3^{n-1}\) codeword vertices for \(2\le n\le6\), checks every unordered pair against two independent combinatorial descriptions of polytope adjacency, counts squared edge lengths, and independently calculates the Laplacian eigenvalues both from the count-triple formula and from explicit finite character sums over the generators. It checks algebraic connectivity and full eigenvalue multiplicities for each tested length. The output terminates in `TERNARY_SPC_EDGE_SPECTRUM_EXACT_PASS`.

Run `python check_lp.py` with NumPy and SciPy installed. The linear program tests whether the midpoint of each candidate pair lies in the convex hull of all other vertices. All 36 pairs for \(n=3\) and all 351 pairs for \(n=4\) matched the claimed edge criterion. Its output ends in `TERNARY_SPC_LP_ADJACENCY_PASS`. These midpoint tests use the geometric coordinates, not the subset-sum criterion to decide feasibility.

No numerical exhaustion beyond the specified finite sizes is claimed. The theorem for all \(n\ge2\) follows from the exact symbolic combinatorial and Fourier proof in RESULT.md. No independent mathematical audit was commissioned.
