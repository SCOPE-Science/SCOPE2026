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

# Verification scope

Run `python3 verify_narayana.py` with a standard Python 3 installation; no third-party packages or external resources are used. It separately computes all recurrence values over one candidate least period and the formula using matrix logarithm critical centers, compares the complete fibre vectors, checks their total counts, checks return of the triple of initial states, and checks the exact number of unique-preimage residues.

Complete comparisons passed for all nine moduli \(3^k\), \(1\le k\le9\), i.e. target counts \(3,9,27,81,243,729,2187,6561,19683\). At \(k=9\) the largest fibre count observed is \(176\). These finite experiments cannot independently establish the general symbolic theorem, the analytic normal-form lemma, or literature originality. All such assertions are stated and justified separately in RESULT.md.
