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

# Reproducibility and verification

Run `python3 verify_equal_diagonals.py` from the directory containing the result and its standalone verification script. The script uses only the Python standard library and reports `PASS: 18660 independent finite assertions` in this package.

It independently reconstructs strict intersections from vertex coordinates by solving two line equations for all allowable spans in regular polygons of sizes \(5\le n<60\), checking the count, the actual Euclidean radii and twofold conditioning multiplicities. It also evaluates moment asymptotics for both polygon parities at finite sizes, including moment orders below and above one, near-critical means, and rare-event cutoff counts. Tolerances in these asymptotic checks accommodate the theoretically slow convergence near the critical exponent; they are numerical consistency tests, not proof of limiting claims.

The proof in `RESULT.md` supplies the infinite-parameter arguments: cyclic crossing enumeration, chord support-line geometry, integrable singularity and dominated convergence for the fixed-order moments, a uniform sine-to-linear error estimate for the critical window, and careful treatment of equality at rare-event thresholds. No independent mathematical audit has been performed.
