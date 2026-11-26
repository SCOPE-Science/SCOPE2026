---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Pass is for the corrected RESULT.md only. The frozen Finding lines 22–24 stated the finite global maximum without the amplification qualification. As an unrestricted assertion it fails: for p=2,q=1 it predicts 1/64, but at kappa=9 the ratio is 1600/14641>1/64, and a flat noncoordinate spike gives positive ordinary variance. The repair states the maximum only in the amplifying regime and gives the nonattained supremum otherwise. I rederived the one-node interpolant and the functional identity A=(a+b)I−ab A^{-1}; subtracting the trace eliminates the residual's identity component probe by probe because the sign norm is fixed. With H=(p+q)^2 kappa/(p+q kappa)^2, the variance ratio is (1−H)^2 and H'=n²(p−q kappa)/(p+q kappa)^3. Finite amplification requires H>2, which occurs only for p>q with n²>8pq. The resulting roots are as stated; the peak gives the unique maximum and exceeds 1 in that regime. Otherwise 0<H<2 at finite contrast (the threshold equality would require an irrational p/q), and H tends to 0 at infinity, proving nonattainment of the supremum 1. The exact-cancellation root follows by factoring in sqrt(kappa). Minimizing pq at fixed n gives n−1, so n²>8(n−1) first holds at n=7. Substitution at n=7 gives alpha=−25/24, window (9/2,8), and residual eigenvalues 25/144 and 25/24 with the stated multiplicities; summing squares verifies the norm ratio. The sign variance formula gives positive variance for the rotated model and the explicit flat spike. Independently authored exact-rational spot checks tested the counterexample, the dimension-seven values, and 1449 discretized parameter choices; the continuum and all-multiplicity conclusions rest on the analytic proof. The frozen checker was inspected, not executed, and does not certify the formerly unqualified maximum.

## originality

PASS

Pass for the repaired sharp optimization and classification: exact multiplicity threshold and contrast interval, corrected fixed-multiplicity maximum/supremum, minimum dimension seven, and its explicit Frobenius counterpoint. Not a pass for priority of the two-level multiplier in isolation: a distinct same-day record gives the same off-diagonal scaling and variance ratio, from which the samplewise statement follows. The repair credits that coverage directly and leaves priority ordering open.

## value

PASS

The one-node correction is a deterministic trace approximation plus an unbiased stochastic residual, not a variance guarantee. The first order at which exact sign variance can increase and the complete spectrum-dependent window answer when the simplest implementation can backfire. The sharp low-dimensional witness also shows why a smaller total residual Frobenius norm is insufficient evidence for sign-probe variance reduction. This exact boundary has use beyond algebraically restating the multiplier.

The dated certificate retains the supplied scientific assessment, sources and limitations.
