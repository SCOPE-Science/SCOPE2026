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

Independent reconstruction: convolution with the target gives m_a = ell/sqrt(S) exp(-a^2/(2S)) and Var(J) = (1+2 tau^2/ell^2)^(-1/2). Multiplying the noisy covariance inverse's numerator and denominator by p_-p_+ gives the quotient (P+2(1-k)z)/(1+P+(1-k^2)z) with k=exp(-2a^2/ell^2), z=p_-p_+. At z=0 this is the exact one-channel answer. At a=0 it is independent of z; for a>0 the sign of its derivative is the sign of (1-k)(2+P(1-k))>0, so the balanced split is unique there. With that split the log-gain derivative in s=a^2 has sign (ell^2+2 tau^2)exp(-2s/ell^2)-ell^2(1+2/P). The sign decreases strictly and is already nonpositive at s=0 precisely for P<=ell^2/tau^2. At equality it vanishes only at the boundary. Otherwise its unique zero gives the stated a_* and, by subtraction from Var(J), the stated risk. Expanding the root at P_c gives a_*^2/(P-P_c) -> tau^4/(ell^2+2 tau^2); sending P to infinity gives the stated limit. Finite-budget risk is positive because an exact Gaussian linear prediction from active channels would have nonzero independent noise variance unless all prediction coefficients were zero. An independent 40-digit decimal evaluation of sqrt(log(5/2)/2) gives 0.67686436302783553519 for the stated P=10 example.

## originality

PASS

Pass the exact joint allocation and placement phase diagram for the specified Gaussian kernel and Gaussian integration measure. Do not credit generic Gaussian conditioning, equal weights at fixed symmetric equal-noise sites, or the existence of a collision transition as such. The strongest same-day different record has a genuine collision transition and different onset, not equivalent coverage; the common date does not settle priority. No compared source established the full claim or a stronger result implying it.

## value

PASS

The tradeoff between measurement accuracy and spatial separation under a common budget is operationally meaningful; a finite threshold, full boundary/equality classification, and different leading response just above the threshold are more informative than noiseless weights or a rate bound. The answer resolves a complete optimization over all allocations, including omitted channels, in a natural symmetry-reduced family. It is an independently useful exact design benchmark, not a claim about unrestricted two-point designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
