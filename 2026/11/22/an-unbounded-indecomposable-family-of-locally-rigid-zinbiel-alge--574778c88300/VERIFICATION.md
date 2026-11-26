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

The stated table has A²=T⊕W, A³=W=Ann(A), A⁴=0; A² acts trivially on the left and yz+zy is in W, so the Zinbiel identity follows. To verify the annihilator, right multiplication by u_i detects both active u_i,v_i coefficients, then left multiplication by u_i detects the t_i coefficients. Derivations preserve A² and W. For i≠j, differentiating u_i t_j=0 gives a s_j+b w+c s_i=0, killing the u_j,v_j components of D(u_i) and the t_i component of D(t_j); differentiating v_i t_j=0 does the same for D(v_i). Now the u_j u_i and u_j v_i equations eliminate the off-branch t_j components. Differentiating t_i=u_i v_i, w=u_i² and s_i=u_i t_i keeps their images in their branch, so branch projection gives a derivation of the five-dimensional table. Independent base calculation: write D(u)=a u+b v+c t and D(v)=d u+e v+f t modulo W. Comparing D(u²) and D(v²) forces c=0, 2a=2e+f. Differentiating uv+vu=0 yields f=0 and d=-b; then e=a and D(t)=2a t. Differentiating vt=w gives 2a w=3a w-b s, hence a=b=0 and all square images vanish. This applies also to k=1. Conversely any map A/A²→W is a derivation, giving dimension 2k(k+1); locality forces the same constraints pointwise. Every ideal containing an element outside W contains w: apply v_i(xv_i), v_i(xu_i), or v_ix according to which active coordinate is nonzero. In a direct-sum decomposition one ideal would consequently lie in W, while A², containing W, would lie in the other, a contradiction. This is a characteristic-zero proof for every k; the archived finite modular checks are not used as proof.

## originality

PASS

The five-dimensional base is expressly reused. The all-rank common-annihilator quotient, the proof that derivations do not acquire off-branch coordinates, and the resulting indecomposable family are not covered by the closest inspected constructions. The originating paper explicitly poses the unbounded indecomposable existence question. Priority remains bounded by the inspected evidence.

## value

PASS

It answers the motivating paper's explicit unbounded indecomposable-existence question by producing a concrete family and computing its full linear derivation space. The common nonzero product prevents decomposition, unlike the known dimension-padding construction. It does not claim every dimension or nonlinear 2-local rigidity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
