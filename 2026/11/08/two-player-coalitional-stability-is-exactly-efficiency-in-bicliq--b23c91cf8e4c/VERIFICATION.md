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

# Verification

The proof uses elementary best-response inequalities, the exact support dichotomy, an explicit two-coordinate update for every jointly improving cross-part pair, and independent labeled surjection/multinomial counting. No computational subroutine is needed for the universal theorem.

Reproduce the bounded direct checks by running `python3 verify_maxcut_biclique.py`. The script requires only Python's standard library and independently enumerates every coloring for \(q\in\{2,3,4\}\), \(1\le a,b\le4\), \(a+b\le7\). It checks \(45\) cases and \(58{,}547\) complete labeled profiles, including unilateral best responses, all joint deviations of pairs on Nash profiles, unique profitable cross-part exchanges, welfare and exact equilibrium counts against inclusion-exclusion surjection counts. A successful execution prints `VERIFIED: instances=45 profiles=58547; Nash, 2-strong, counts, blocking pairs`.

The enumerated finite cases confirm consistency but do not establish general statements for larger inputs. The analytic proof handles unrestricted positive \(a,b\) and integer \(q\ge2\). The source comparison is best-knowledge, rather than a computer-certified global priority search.
