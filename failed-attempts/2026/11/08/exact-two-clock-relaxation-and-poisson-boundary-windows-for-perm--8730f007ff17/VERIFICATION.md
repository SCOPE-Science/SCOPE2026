---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The scalar u=2x_m-1 satisfies u_next=u², and dividing remaining coordinates by 1-x_m yields p_next=[alpha I+(1-alpha)P]p exactly. Fourier roots on each permutation cycle produce the stated sharp contraction factor with the longest cycle length. Factoring Q_alpha=P[I+alpha(P^{-1}-I)] gives the residue P^r and standard matrix exponential for n alpha→t; alpha→1 gives e^{t(P-I)}. Independently checked exact iterates for n<=7 and both endpoint limits for a four-cycle and t=.3,2. All boundaries specified (fixed interior initial data) are coherent.

## originality

FAIL

The earlier published November 1 result supplies EXACTLY the same nonlinear/linear finite-time factorization and the Fourier one-step modulus identity for arbitrary varying alpha_n, strictly dominating the fixed-alpha theorem. The submitted sharp fixed-alpha norm is immediate by taking the maximum Fourier modulus; both Poisson windows are the standard Euler/Poisson limit of that already published finite product, with residue P^n from the earlier decomposition. There is no independently non-implied theorem remaining.

## value

FAIL

Under the prior exact arbitrary-schedule factorization and Fourier decomposition, the submitted new endpoint formulas are direct finite-dimensional matrix-exponential scalings, not an independently motivated unproved invariant or a substantively new structural law; the main two clocks were already explicitly proved. Thus the total claimed finding lacks independent value despite correct algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
