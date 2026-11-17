---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The deterministically equivalent event F_top union F_bottom for n>=5 is cited to Brandt–Chen–Dong–Lederer–Schlenga Theorem 2, not reinvented. Mallows first-choice probabilities are a_n q^(c-1), and second choices conditional on first are b_n q^(h-1-1_{h>c}). Exact distinct-top event probability A_n=n!a_n^n q^{n(n-1)/2}; exactly one duplicate top with two seconds equal to the unchosen house contributes E_n and E_n/A_n→(1+q^2)/(2q(1+q)). Position+label reversal gives bottom symmetry. A conditional suffix union bound makes top∩bottom=o(A_n) for fixed 0<q<1, producing C(q). The q=1 uniform case is calculated separately and yields factor 3. Exact finite first/second event probabilities were independently checked for n=3,4,5; n<5 never tests the external top-cycle classification.

## originality

PASS

The majoritarian-assignment source supplies the exact deterministic exceptional event classification but not its joint top/bottom Mallows probabilities. The Mallows cycle reference concerns cycles of a single random permutation, not this tournament-on-assignments top cycle. Earlier 3-agent top-cycle probability differs in population size and random culture.

## value

PASS

Provides a sharp rare-event probability, explicit fixed-dispersion prefactor and impartial-culture boundary for a nontrivial social-choice object. The deterministic classification and standard Mallows weights are credited; the new probabilistic asymptotic is mathematically motivated rather than a renamed classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
