---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS. On B=max(Y_i)<1/2 the supporting tangent polygon has area A=sum_i tan(pi Y_i), and the Dirichlet beta marginal gives p=1-n[1-I_{1/2}(alpha,(n-1)alpha)]. At a nearly semicircular gap Y_i=1/2-O(1/x), its density tends to f(1/2)=2^(2-n alpha)/B(alpha,(n-1)alpha), giving each single pole probability f(1/2)/(pi x). Integrating the two-near-half-gap simplex corner is O(x^(-1-(n-2)alpha)), hence negligible. The max/sum squeeze yields constant n f(1/2)/(pi p), and the marginal endpoint rescaling tends to uniform U; the normalized other gaps have exact independent symmetric Dirichlet law, yielding J,U,Z,A/x -> J,U,Z,U^-1. Moment threshold q<1 follows by tail integration. These steps are correct, but were already essentially completed in the earlier November 2 proof.

## originality

FAIL

FAIL, decisive same-model prior. November 2 published full RESULT already proves the exact same conditional tail coefficient for every n>=3, alpha>0, same boundedness p, the iff moment threshold, and negligibility of two near-semicircular gaps. Its proof explicitly uses the conditional independence of the remaining normalized Dirichlet coordinates. Hence the added J,U,Z,U^-1 marked limit is the natural immediate endpoint-conditioning corollary of its full proof, not a new standalone original theorem.

## value

FAIL

FAIL as an independent contribution: the exact fixed-n Dirichlet Pareto constant, infinite-mean result, and the one-large-gap asymptotic mechanism were previously established for the identical model. The extra marked Dirichlet/U limit follows essentially by conditioning the earlier proof's exact independent Dirichlet remainder on its already-controlled one-gap event and continuity of the beta density, without a new motivated structural obstruction. Correctness and reproducibility do not turn this covered extension into valuable independent work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
