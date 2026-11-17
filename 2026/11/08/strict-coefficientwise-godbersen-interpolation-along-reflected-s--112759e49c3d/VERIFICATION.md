---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For full-dimensional simplex Δ, K_t=(1-t)Δ+t(-Δ), normalized mixed volume Q_{n,k}=V(K_t[n-k],-K_t[k])/vol(K_t). Orthant slicing gives F_n(a,b)=Σ binom(n,j)^2 a^(n-j)b^j. With a+b=1 and p=ab, H_n(p)=Σ n!p^j/[(n-2j)! j!²] has positive-factor product from simple zeros of Legendre P_n. The normalized reflected polynomial factors as (s+u)^n∏(1+r_i(p)su/(s+u)^2), r_i(p)=λ_i(1-4p)/(1+λ_i p) strictly decreasing. Every interior coefficient includes positive binom(n-2,k-1)e_1, hence strict decrease from binom(n,k) to 1 as t grows 0 to 1/2. Hypergeometric binomial-square second moment yields center quadratic 2k(n-k)/(2n-1). Verified by separate exact rational coefficient calculations for n=2..8.

## originality

PASS

PASS best of knowledge. Fryš–Kotrbatý–Mouamine–Wang prove the general Godbersen inequality and simplex extremizer, fixing endpoint t=0 but not an ordered all-index path of ratios for the mixed body K_t. Artstein-Avidan–Putterman study unbalanced difference-body primal volumes rather than normalized opposite mixed volumes of K_t. Separate Resultary Mahler-profile and vertex-truncated-simplex results concern distinct invariants/deformations. Relevant Fryš full text could not be retrieved with permitted institutional access, so stronger hidden coefficient identities are a documented risk rather than automatic rejection.

## value

PASS

PASS. It provides a natural interpolation among sharp Godbersen extremizers and the symmetric equality body; the simultaneous strict order of all mixed-volume coefficients and exact universal second-order stability quantify the entire coefficient vector, not a repackaging of endpoint bounds. The proof introduces a valuable Legendre-root positive-factor representation rather than a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
