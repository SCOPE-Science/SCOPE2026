---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With k=sqrt(r/D), a reset cycle started at x hits zero before the reset with probability e^(-kx), and has mean duration (1-e^(-kx))/r. The subsequent iid reset cycles have success probability s>=e^(-kb)>0, giving finite MFPT (1-s0)/(rs). For m>max{x0,b}, a jump cannot cross m. The two-boundary Brownian exit probability q satisfies Dq''+r(c-q)=0, q(0)=0, q(m)=1, c=E[q(Z)]. Independently, q(x)=c+A exp(kx)+B exp(-kx), and averaging gives Au+Bs=0, while q(0)=0 sets c=-A-B. Using q(m)=1 gives precisely the frozen formula. After a Brownian hit on m, the path exceeds m immediately almost surely before the next reset or absorption, so there is no atom at an admissible m. The derivative in u is positive since t<s0. Strict Jensen and the strict secant inequality for 1/y on [ell,h] give the unique point-mass and endpoint-mixture extremizers at fixed E[y]=s; mixing those laws fills the entire u interval, and the same strict ordering works for each threshold. At the feasible endpoints there is only one law. Solving the fractional-linear formula identifies u, not the law, and t->0 gives the stated tail coefficient. An independent exact rational ODE comparison passed 63 threshold/interpolation cases (`python3 /workspace/audit_evidence/reproduce.py 5`).

## originality

PASS

The MFPT constraint and the point-reset two-boundary maximum are established premises. The closest same-date record gives fixed-mean envelopes for absorption-time transforms and variance and has essentially the same extremizing measures, but concerns a different observable and uses a random initial position drawn from the reset law. The substantive distinct claim is the exact above-support maximum law and its complete attainable, simultaneously ordered range under arbitrary iid spatial resets at fixed MFPT from x0.

## value

PASS

A mean search time alone does not measure excursions. The result gives sharp differences in excursion risk at precisely equal mean, with unique designs, no threshold-dependent change of the extremizers on the specified domain, a complete one-parameter attainable family and a measurable second moment. The useful content is this exact reduction of the path statistic to two moments and the resulting stochastic order, not the textbook convexity bound by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
