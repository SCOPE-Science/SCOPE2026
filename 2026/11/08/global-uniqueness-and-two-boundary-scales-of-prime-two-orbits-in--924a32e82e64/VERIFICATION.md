---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Every positive primitive 2-cycle 0<u<v<1 satisfies u f(u)=v f(v), forcing equal values of unimodal H(x)=x^2(1-x)(c+mx). Symmetric division with s=u+v,p=uv gives p=s(s-1)(c+ms)/(c+m(2s-1)), then r=R(s)=[c+m(2s-1)]/[(s-1)(c+ms)(c+m(s-1))]. Discriminant equals -s[2ms²+3(c-m)s-4c]/[c+m(2s-1)], positive exactly s in (1,s*), where 1<s*<2 is the unique positive root. R strictly decreases from infinity to r*, thus precisely one unordered primitive 2-cycle for r>r* and none otherwise. Exact complementary product proves u,v lie inside (0,1). As s↓1, singular expansion yields c>0: ru→1/c and r²(1-v)→1/[c(c+m)]; c=0: sqrt(mr)u→1 and (mr)^(3/2)(1-v)→1. Symbolic elimination and boundary expansion independently reconstructed. Restriction to positive cycles, not a claim that all x∈[0,1] remain forward-invariant for all r.

## originality

PASS

The Pires–Andrade–Herrmann June 2026 source develops this generalized Allee-logistic cubic and local fixed-point/period doubling and chaos. Earlier Resultary November 2 theorem establishes c=0 sector sharp no-period-two bound and its existence, but not all-r uniqueness and contrasting two-parameter boundary scales; logistic m=0 is classical. Inspected published formulations do not imply full nonnegative (c,m) uniform global two-cycle uniqueness and singular endpoint rate change. Best-of-knowledge priority only, particularly since Jung et al 2020 special Allee-map full paper was not inspected.

## value

PASS

An exact all-growth prime-two census for a natural cubic population-map family settles whether additional period-two branches can appear even after higher-period bifurcations. Distinct large-r boundary exponents at c=0 are a meaningful singular parameter boundary. Nontrivial exact classification extends substantially beyond the classical logistic endpoint and narrow c=0 existence threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
