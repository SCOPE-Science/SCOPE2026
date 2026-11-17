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

From the two-type SIR equations, x=I_H/(I_H+I_L) satisfies x'=a(t)x(1-x)+nu(1-2x), a(t)=k(lambda_H-lambda_L)s(t), with strictly decreasing positive a(t). The unique positive root y(a) is strictly increasing in a. Each zero of x-y(a(t)) has strictly positive derivative, hence x changes from increasing to decreasing at most once, any stationary point is a strict maximum. The total removal integral bounds s_infty>=s_0 exp(-k lambda_H/mu)>0, and scalar trapping gives x_infty=y(a_infty). The exact example (lambda_L,lambda_H,k,mu,nu)=(0,1,10,1,1/10), (s,L,H,r)=(9/10,3/100,7/100,0) has x'(0)=37/20>0 and x_infty<7/10 by the concavity r_infty>99/100 bound, proving a real interior peak. All quantifiers require strictly positive classes, k,mu,nu and lambda_H>lambda_L; numerical integration is illustrative only.

## originality

PASS

Best-of-knowledge original model-specific global single-turning theorem for symmetric two-type reflecting mutation SIR, not the underlying Riccati comparison argument or the known continuous-trait moment equation. The cited source treats distinct trait diffusion and epidemiological peaks; no earlier source found that implies this all-initial-state one-peak and reversal example.

## value

PASS

Establishes a global one-peak/no-rebound classification and a mathematically forced reversal in a concrete, physically motivated SIR mutation model, materially distinguishing bounded two-type mutation from the early-time monotone selection picture. All-initial-state and positivity hypotheses give a useful structural theorem beyond a routine linearization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
