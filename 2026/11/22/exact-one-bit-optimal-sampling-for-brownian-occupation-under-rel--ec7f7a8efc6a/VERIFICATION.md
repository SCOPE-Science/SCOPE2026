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

With independent pre-threshold noise of variance eta*x, the correlation at time t is a times sqrt(min(t,x)/max(t,x)), where a=(1+eta)^(-1/2). The Gaussian sign identity and the fair bit give E[Q|S]=1/2+S F(x,a)/pi, with F the integral of the arcsine of that correlation. The same sign identity, integrating over 0<s<t<1 with s=tu, gives Var(Q)=1/8; projection proves that maximizing positive F is equivalent to minimizing risk. Integration by parts on both pieces gives F=arcsin(a sqrt(x))+a sqrt(x(1-a^2 x))-a k(a)x, where k(a)=sqrt(1-a^2)+integral_0^1 u^2/sqrt(1-a^2 u^2) du, including the integrable a=1 endpoint. Thus F'=a(sqrt(1/x-a^2)-k(a)) strictly decreases on (0,1), tends to +infinity at zero, and has negative left limit at one because the integral in k is positive. The unique optimum is x=(a^2+k^2)^(-1), where the last two terms of F cancel and the arcsine equals arctan(a/k). At a=1 k=pi/4; expansion k=4/3-(2/5)a^2-(1/14)a^4+O(a^6) gives the stated high-noise corrections. A fresh split quadrature at eta=0,1,99 matched the score to 9e-37 and gave the stated noiseless risk 0.04201127713216669; stationarity residuals were below 8e-37. Replay: python /workspace/branches/e97b0d37-7e51-48fc-98e8-b1c6d81e4309/brownian_one_bit_repro.py.

## originality

PASS

The supported distinct claim is the unique optimal deterministic time and exact estimator/risk for one threshold-zero Brownian-motion sign bit across all finite relative Gaussian noise levels, including zero noise. Neither the strongest same-day analogues nor the checked primary passages were shown to determine this design. The Gaussian arcsine identity, Bayes projection and occupation variance are not novelty claims.

## value

PASS

Design is nontrivial because the sensor's marginal pre-quantization signal-to-noise ratio is fixed across candidate times but the bit's information about the entire occupation functional is not. The formulas give a reproducible calibration and a risk benchmark for the minimum-information design, show the noiseless bit alone explains about 66.39% of occupation variance, and quantify both limiting time and vanishing information at high noise. A full-valued-snapshot benchmark does not answer this question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
