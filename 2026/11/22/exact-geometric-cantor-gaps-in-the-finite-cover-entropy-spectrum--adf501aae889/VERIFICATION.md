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

# Verification and reproduction

Run `python check.py` with Python 3. No third-party package is required.

The executed checks use high-precision decimal arithmetic for the golden irrational slope, \(\alpha=(\sqrt5-1)/2\). They independently compare the canonical cutoff criterion against direct membership of *each local observation window* in the original gap shift in 18,414 combinations; verify 23 one-step equality/strictness witnesses using the newly forbidden return block; compare 18 jump widths against the geometric prediction at the corresponding irrational-rotation phases; check the total jump-width identity and endpoint span; and compare eight numerically solved finite-cover entropy roots with the proven normalized expansion.

The recorded run completed without failed assertions. Representative estimates were \(\lambda\approx1.4569740225048505\), \(T\approx3.985988427074893\), normalized cluster-set hull length \(\approx0.2508788016561923\), and the first complementary gap width \(\approx0.0786871237120119\). All computations are finite diagnostics and cannot establish the theorem's infinite all-slope quantifiers, completeness of the cluster set, perfection, Hausdorff dimension or historical priority. Those assertions rely on the written proof and the stated classical renewal and Sturmian-complexity inputs. No independent review or certification has been performed.
