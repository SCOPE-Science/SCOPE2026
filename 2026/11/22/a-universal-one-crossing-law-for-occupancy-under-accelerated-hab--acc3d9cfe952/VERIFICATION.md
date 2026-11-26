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

For the initially unsuitable patch, suitability H_s solves H_s'=s(p-H_s) and occupancy solves P_s'=c H_s-lambda_s P_s. Direct convolution yields the formula including the coalescing-rate limit t*exp(-s*t). Setting q=1-p and A=exp(-s1*t)-exp(-s2*t), the occupancy difference is forced by cp*A-q*(s2-s1)*P_s1. For y=exp(-s1*t), r=s2/s1>1, the y-derivative of (y-y^r)/(1-y) has numerator 1-r*y^(r-1)+(r-1)*y^r, positive because its derivative is negative and it is zero at y=1. Consequently A/H_s1 strictly falls in time; P_s1/H_s1 strictly rises because H_s1(t-v)/H_s1(t) rises for each v in (0,t) by strict decrease of the log derivative of H_s1, and the positive convolution domain expands. Hence A/P_s1 strictly falls from infinity to zero (P_s1 is order t^2 at onset and approaches cp/lambda_s1 at late times). The forcing has one positive-to-negative change. The integrating-factor transform of the occupancy difference starts at zero, rises, and then strictly decreases to minus infinity by the strictly negative stationary gap. It has exactly one positive-time root. No rate-order or nonresonance assumption entered this proof. Independent uniformization of the U,E,O row generator used nu=max(ps,qs+c,qs+e) and summed the O coordinate of exp(-nu*t) times the Poisson series in I+Q/nu through term 160. Bisection gives 1.950825084705 for the displayed case and 3.596619389093 for p=0.75,c=1.5,e=0,s1=0.6,s2=2, in which the faster process is resonant.

## originality

PASS

Credit neither the three-state representation nor a generic transient benefit of turnover. The supported distinct claim is the exact single positive-time crossing of the occupancy curves at arbitrary pairs of turnover speeds with fixed stationary suitability, external colonization and initial state U. Available statement-level evidence compares different objects or gives different endpoints; the historical assessment remains best-of-knowledge because the full closest published models were not recovered.

## value

PASS

There are two opposing physical mechanisms even at fixed stationary habitat fraction: faster access to suitable habitat from U and faster removal of occupancy after suitability is reached. The result rules out oscillating policy rankings over deadlines for a natural memoryless model, and does so for all pairs of turnover speeds rather than just under a small-perturbation or rate-order assumption. The proof controls the transient forcing, not only the two easy endpoint signs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
