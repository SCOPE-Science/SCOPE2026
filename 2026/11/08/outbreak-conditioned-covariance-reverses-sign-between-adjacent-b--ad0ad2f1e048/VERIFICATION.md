---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For independently seeded P3, q in (0,1), independent bond transmissibility p in [0,1], S at least one imported seed, read exact RESULT.md and reconstructed all four edge states and eight seed states. In noninfection form, conditional covariance is [z(1-A-B+C)-(1-A)(1-B)]/z^2 with z=1-(1-q)^3. Independent symbolic algebra reproduced z^2 Cov(X0,X1|S)=q^2t^2(1-p)F_t(p) and z^2 Cov(X0,X2|S)=-q^2t^3(1-p)^2[1+2p(1+t)+tp^2]. The published Bernstein-basis formula for F_t prime is strictly positive on p in [0,1], F_t(0)<0<F_t(1), proving a UNIQUE interior adjacent sign threshold, with two-node failure and endpoint strict negativity for p<1. Verified q=1/2 root approximately .218089980704572 and asymptotic boundary coefficients; unconditioned covariance is nonnegative by product-measure positive association. This is a finite-graph exact symbolic proof, not a simulation of all real parameter values.

## originality

PASS

One-source outbreak component models and unconditioned infection correlations predate this result. A very close published same-week path theorem has one UNIFORMLY CHOSEN initial source, not three independent q-seeds conditioned on nonemptiness. The one-source model is the q-to-zero limit, but it does not imply the finite-q cubic transition and negative endpoint identity. Originality is limited to this conditional multi-seed phase diagram.

## value

PASS

A minimal three-node counterexample where conditioning changes the sign of an intrinsically positively associated final-infection field, with a rigorously unique transmissibility threshold for adjacent sites and persistent endpoint anticorrelation, is a motivated sharp boundary case. It identifies the first path size permitting reversal and clarifies the hazards of outbreak-selection conditioning. It is valuable as a finite exact test case, not a universal epidemic theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
