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

For P^2=P, N^2=0 and PNP=0 over any field, the rank parameters (r,h,t) satisfy 0<=h<=floor(n/2), 0<=r<=n-h, 0<=t<=min(r,h). The flag U=im N subset K=ker N with V/K isomorphic to U and the idempotent splitting S+W=V reduce PNP=0 to S intersect N(S)=0, W containing N(S). The choices of A=S mod K, B=S intersect K disjoint T=N(S), S extensions and W complements are flag/open/affine bundles. This proves smooth geometrically irreducible *reduced* rank strata and the Gaussian-binomial population [n h]_q[n-h h]_q|GL_h|[h t]_q[n-h-t r-t]_q q^(t(n-h)+r(n-r-t)), with dimension 2h(n-h)+2r(n-r)-hr+ht-t^2. The completed-square identity yields floor(11n^2/13). Finite bounded 13-residue checks plus inequality constraints yield top-dimensional component multiplicities (1,4,2,3,2,1,2,2,1,2,3,2,4) for n>=13, with n=1,3 exceptions. New independent integer enumeration checked all integer feasible triples through n=104 and all claimed extrema and period; that finite check corroborates but does not replace the geometric bundle proof for all n and fields.

## originality

PASS

Best-of-knowledge original: the one-sided PN=0 variety is precisely the t=0 slice and has five-periodic top-component counts, not the nonzero-t sandwich relation; Richmond's module variety stratification offers general geometry but neither these finite-field pair counts nor this thirteen-periodic exact optimization. Schröer's two mutually annihilating nilpotents concern distinct polynomial relations. Novelty in the exact three-rank sandwich enumeration and component period, not generic flag bundles.

## value

PASS

The algebraic variety defined by a square-zero operator interacting with an idempotent via a sandwich relation is a natural representation-theoretic object. Its full labeled finite-field rank census, smooth reduced stratum geometry and unusual sharp thirteen-periodic top-component law are substantive, nontrivial structural invariants, not a mere renamed rank calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
