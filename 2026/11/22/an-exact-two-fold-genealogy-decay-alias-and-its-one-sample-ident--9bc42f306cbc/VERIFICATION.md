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

For depth-five leaves the distance is twice five minus twice the length of the common prefix. Across different two-bit prefix families it is at least eight; within the four designated families, distances to the named leaves give respectively (0,0,1),(1,0,3),(1,1,1),(1,0,0), and the leading determinant is 1. The binary prefix tree is feasible with positive probability because all finite logits give Binomial probabilities strictly between zero and one. A Binomial(2,p) law determines its logit, and conditional independence gives the joint law from the marginals. Subtract the first predictor from the next two: the gaps are β₁t(1+2t²) and β₁t(1+t). Their ratio is R(t)=(1+t)/(1+2t²). Its coincidence equation is (s−t)[1−2(s+t+st)]=0, so the unique possible partner s=(1−2t)/(2(1+t)) lies in (0,1) precisely for 0<t<1/2, and is distinct except at (sqrt(6)−2)/2. The positive first gap determines β₁ at either candidate, and the first logit determines β₀, proving both necessity and realizability. In particular (t,β₀,β₁)=(1/5,0,1) and (1/4,−1/250,96/125) both give (1,28,31)/125. Differencing rows of the Jacobian gives the t-coordinate determinant β₁[t(1+2t²)]²R'(t); multiplying by −2t gives 2β₁t³(2t²+4t−1) in θ. The Binomial information weights 2p_i(1−p_i) are positive, so precisely the fold is singular despite its singleton fiber. The new row gives gap ratio (1−t²)/(1+2t²), derivative −6t/(1+2t²)², hence unique reconstruction over the entire domain. Its two logits in the exact example differ by 3/250.

## originality

PASS

The distinct claim is the feasible full-rank design that refutes the stated sufficient condition, with its exact fiber/fold classification and a feasible fourth-row repair. Eliminating location and positive scale is a general technique, not new here.

## value

PASS

This is a realizable obstruction to an explicit proposed sufficiency rule, not just an arbitrary rank example. An open region of genuine aliases persists despite nonsingular local information away from the fold. The exact fiber classification, singular point and one-observation repair show what the three-event design cannot identify and how to remove the ambiguity without changing the model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
