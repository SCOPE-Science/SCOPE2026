---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For P=(1/10)[[8,1,1],[3,3,4],[1,7,2]] and pi=(14/27,5/18,11/54), independently recomputed pi P=pi, pi_2 P_21=1/12 and pi_2 P_23=1/9. For length-two holes the killed transition matrix B_ij=P with only edge ij zeroed, and survival after n observations is pi B_ij^n 1. Both B matrices remain primitive substochastic. Exact characteristic polynomial of B21 is (10z-7)(20z^2-12z-5)/200, Perron root (3+sqrt(34))/10<9/10. The B23 polynomial z^3-(13/10)z^2+(21/50)z-3/50 changes sign from -3/500 at 9/10 to +3/50 at 1, hence its Perron root exceeds 9/10. As -log decreases, escape(21)>escape(23). The two prime length-two cylinders on a two-symbol stationary chain (12,21) have equal masses by stationarity, proving the restricted alphabet minimum. Finite n checks are not the spectral-limit proof.

## originality

PASS

The original Agarwal--Cheriyath--Tikekar conjecture concerns strict monotonic comparison for equal-length prime-word holes under a Markov measure. It presents nonprime reversals and prime equal-measure cases, neither gives a strict prime/prime reversal. The current Markov matrix is nonproduct, so Bonanno--Cristadoro--Lenci Bernoulli conclusions do not imply the conjecture. No earlier strict 3-symbol length-two counterexample was identified in Resultary searches; exact mathematical priority remains best-of-knowledge.

## value

PASS

Disproving a specifically published dynamical conjecture with a short fully rational and alphabet-minimal example is a motivated structural boundary, not an arbitrary matrix calculation. It exhibits a qualitative failure of the proposed escape-ordering law in the smallest admissible Markov alphabet for length-two prime holes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
