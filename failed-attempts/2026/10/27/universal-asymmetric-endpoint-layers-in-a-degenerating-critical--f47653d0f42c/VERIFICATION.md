---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For 1<ϑ<2 the two inverse branches are 1/2±u² and both absolute derivatives are w=u/(K+ϑu), with w(1)=0 and w(0)=λ=(1+ϑ/2)^-1. Applying the fixed-point equation to the W^{2,1} representative gives zero endpoint values; w(x)/(1-x)→1/(2K²) gives the derivative at one, and differentiation at zero gives h'(0)=λ²[h'(0)-h'(1)]. The uniform BV step can be made explicit: on a rank-n cylinder the inverse-iterate weight is a product of n monotone factors, each of sup norm and variation at most λ, so the product has sup ≤λ^n and variation ≤nλ^n. The product inequality followed by sup_C|φ|≤Var_C φ+||φ||_{1,C}/|C| gives a variation coefficient (n+1)λ^n and a weak-norm coefficient at most nλ^n/min_C|C|. Choose a fixed large n and restrict ϑ near two; fixed-rank cylinder lengths tend to 2^-n and the variation coefficient is strictly below one. Compactness then gives L¹ subsequential limits. Invariance passes to the limit: the weights converge in L¹ to 1/2, and the inverse branches converge uniformly; for BV test inputs, the L¹ composition error is bounded by a constant times the inverse-branch displacement times the variation (integrate the variation measure against the affine limiting branch). The unique tent-map density is one: for BV inputs the affine cylinder average differs from the integral by at most 2^-n Var. The disjoint-cylinder sup inequality in RESULT.md then gives locally uniform interior convergence. At x=1-K²s the scaled weight and interior preimages give U uniformly for bounded s. At x=K²s, left-preimage rescaling tends uniformly to s/2, the symmetric right-preimage term uses U, and iteration leaves a uniformly geometric remainder, giving V and slopes 1 and 1/3. Both profiles tend to one at large s by bounded convergence; no global uniform rescaled claim follows. The frozen verify.py and check_output.txt check samples of inversion, weights and profile recursion/slope sum, not the actual density's uniform BV bound or finite-parameter derivative equation; the supplied script was inspected but not run.

## originality

FAIL

A distinct inspected Resultary record, 2026/11/1/SCOPE-distinct-universal-endpoint-layers-when-a-square-root-cusp-disap--101c84be4744, covers the complete frozen finding: the same invariant densities, both modes of bulk convergence, both limiting endpoint profiles, and both slope identities. Rescaling distance by the fixed factor eight converts the statements exactly, and the other record also has stronger derivative-norm conclusions. This is demonstrable equivalent indexed coverage, not a finding about who derived it first. The earlier Oltiboev–Vafoyev article also already supplies the right endpoint derivative; its fixed-parameter and random-response theorems do not by themselves give the profiles.

## value

PASS

As a mathematical statement, bulk statistical stability alongside different profiles at the two endpoints gives quantitatively useful information that cannot be read from L¹ convergence. The layer width and asymmetric slopes describe the singular limit of the invariant measure. This scientific interest does not make the equivalent indexed result original again.

The dated certificate retains the supplied scientific assessment, sources and limitations.
