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

# Verification record

Run the included standard-library program with `python3 verify.py`. It constructs the vertices of each Cartesian product, applies the direct \(2\)-plex definition, and checks all single-vertex additions for maximality. The structural-family generator independently constructs distant pairs, full coordinate lines and coordinate squares. The all-set and maximal-set polynomials are compared to brute-force subset counts where exhaustive checking is feasible.

The verified terminal summary was:

`VERIFY_OK instances=14 tested_subsets=468037 generated_maximal=881 exact_families=PASS all_and_maximal_polynomials=PASS`

The eleven instances with at most \(18\) vertices were checked against all nonempty subsets. For the remaining three instances of orders \(24,27,24\), the program checked the maximality of all proposed members and coefficient computations but did not exhaustively search all subsets. The proof in `RESULT.md` is the justification for arbitrarily large parameters. No independent mathematical audit has been performed.
