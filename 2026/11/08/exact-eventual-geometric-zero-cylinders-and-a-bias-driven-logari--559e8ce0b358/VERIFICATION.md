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

# Verification notes

The Python standard-library script `CHECK.py` was executed directly from the extracted current package. Its independent rational interval partition integrates the zero-branch selector across all original-position breakpoints, rather than evaluating the finite-sum formula twice. The program reports 423 passed exact identities and inequalities, covering 40 pairs of rational parameters, eight lengths beyond the cutoff for each pair, and exact balanced-parameter identities. No floating-point simulations are used.

The analytic proof additionally establishes the zero-branch product identity, plateau reduction, finite-level weight partition, normalization, the cutoff and strict equality criterion, and both fixed-bias endpoint asymptotics. Checks of source premises used the original map equations (11)--(12), Theorem 3.5, Lemma 3.8, and the \(L^1\)-convergence argument in Lemma 3.11 of Dajani--Kalle--Maggioni, arXiv:2008.04398.

Scope: \(1<\alpha\leq2\), \(0<p<1\); no asserted uniformity of the biased remainder at \(p=1/2\). A finite run does not certify the analytic theorem. No independent external verification has been performed.
