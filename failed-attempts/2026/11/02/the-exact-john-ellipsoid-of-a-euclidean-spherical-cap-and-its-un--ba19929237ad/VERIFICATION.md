---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

PASS. Exact relations u t=d(1-a^2)/(d+1)^2, t-u=a, v^2=u^2+dut yield containment identity 1-[(t+us)^2+v^2(1-s^2)]=dut(s-1/d)^2>=0. At s=-1 one plane contact, at s=1/d sphere contacts; a d-dimensional regular simplex of d+1 normalized contact points satisfies sum c_i x_i=0 and sum c_i x_i x_i^T=I with c_i=d/(d+1), certifying global maximality for every d>=3, -1<a<1 by John’s theorem. Independently checked containment numerically across d=3,4,10,100 and five offset values; asymptotics follow elementary expansions. Correctness is independent of originality.

## originality

FAIL

FAIL. Decisive stronger prior coverage: Güler and Gürtuna arXiv:0709.0707 (2007), §7, Theorem 7.1(ii), already explicitly solves the maximal INSCRIBED ellipsoid of a unit ball slab B_{alpha,beta}. Take beta=1 and alpha=a, then for every -1<a<1, 4d(1-a^2)<(d+1)^2(1-a^2) (strict for d>1). Theorem 7.1(ii) gives EXACTLY t=[a+sqrt(a^2+4d(1-a^2)/(d+1)^2)]/2, u=t-a, v^2=u(u+d t), i.e., the central claimed all-dimensional/all-cut John ellipsoid. Source proof even derives curved contact parameter s=1/d via (7.9), and the convex optimality is global. The remaining simplex demonstration is an elementary equality-case John-certificate for this already solved ellipsoid; pointwise asymptotics follow algebraically from the known closed forms. Neither alters coverage of the original core claim. No repaired final theorem or full protected replacement files were supplied; reject original for O, preserving whole package.

## value

PASS

PASS independently of originality: explicit maximal-volume inscribed ellipsoids and their simplex-contact geometry for truncated balls are natural and mathematically useful convex-geometric objects; however their priority is already established and this submission adds insufficient independent originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
