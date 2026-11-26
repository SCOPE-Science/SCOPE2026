---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Kroumi's (A7) for one coordinate on four cyclic states uses cosines 1,0,−1,0. The four-point transform of (1,q,q²,q) gives (1+q)²,1−q²,(1−q)²,1−q². At transform argument s/(2ν), (A7) therefore yields (ν/2)F_s; (29) at μ=1 takes s=1,3,5 and the common factor cancels, leaving the submitted ratio. An independent bounded integer-polynomial reconstruction multiplies both forms by T=∏_{s=1,3,5}(s+2ν)(s+4ν). The multiplied denominator is 64ν(1−q)U; U is positive on the stated open domain. If P is the multiplied numerator divided by 32 and V=νU, the derivative numerator is P'V−PV'; its coefficient rows agree with every listed coefficient of H_q. The two mixed-sign rows h_5 and h_4 are strictly negative by bounding their positive terms with q²,q³≤1 and discarding their negative linear terms. All degrees ≥6 are positive, all lower degrees negative. Since H(0)<0 and its leading coefficient is positive, Descartes' rule and continuity give exactly one positive root counted with multiplicity. The derivative changes from negative to positive there, and its simple zero and positive denominator give positive second derivative. The q=1/2 isolate is illustrative, not part of the universal argument. The submitted supporting files were inspected without running the supplied script. This conclusion is only for the abstract weak-selection, large-population four-state model with μ=1.

## originality

PASS

The Fourier threshold and existence of an interior optimum are covered by Kroumi; the rational specialization is not a new threshold. The supported distinct claim is uniqueness and nondegeneracy for every α>0 on the four-state cycle at μ=1, certified by a controlled sign change in its two-rate derivative. Neither the finite-periodic existence theorem nor the distinct indexed binary-cycle theorem implies that claim.

## value

PASS

Four sites are the first cyclic phenotype space with two distinct nonzero decay rates. This makes it a natural minimal check of whether the single-rate uniqueness phenomenon survives spectral competition. At the fixed scaled benchmark μ=1 the theorem answers this uniformly in discrimination strength and gives an exact criterion for the unique design point. This is a usable exact classification within the stated abstract model, not a general mutation prescription or a result extrapolated from the example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
