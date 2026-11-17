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

The displayed quartic F=x³z−cxy³+cxz³−yz³ has in characteristic 3 gradient (c(z³−y³),−z³,x³), with no common projective zero for c≠0, giving smooth genus 3. The two infinity points have tangent order 3. At affine (X,Y), tangent substitution yields coefficient (1−cXa³)t³−ca³t⁴ where a=c(1−Y³), so order-4 rational inflexions are decidable by exact F9 evaluation. Independent enumeration for all eight c gives N1=16,13,10,13,7,10,13,7 and flex count 0,1,2,1,0,2,1,0; exactly c=−1,1±i have (13,1). Independent exhaustive F81/F729 finite-field fiber enumeration for these c gives N2=(109,73,73) and N3=(676,676,676), with complete per-y histograms. Newton identities and the genus-three Weil functional equation uniquely produce P_-1=(1−3T+9T²)(1+3T+9T²)^2 and P_(1±i)=(1+3T+9T²)(1−9T²+81T⁴). Q(X)=X⁴−9X²+81 is irreducible over Q by rational quadratic comparison; Honda–Tate decomposition gives a simple abelian surface in the latter type. P(1) gives Jac orders 1183,949, and normalized Frobenius factors are cyclotomic, hence supersingularity. The finite census is exhaustive over the stated F9, F81, F729, not an extrapolation.

## originality

PASS

PASS, qualified: Homma–Kim 2026 Theorem 46 already identifies the natural three-member (13 rational points, one flex) F9 stratum, and 2024 results show all family members are Hermitian twists with supersingular normalized Frobenius eigenvalues; these are not new. Those inspected statements do NOT specify the two exact degree-six Weil numerators or the elliptic×simple-surface versus 3-elliptic decomposition. The published earlier one-rational-point Hermitian-relative zeta theorem is a different one-point family, so cannot imply these 13-point numerators. Meagher–Top 2010 full text sections 7 and 8 treat Dyck–Fermat/Klein twists in characteristic at least five and thus do not supply these F9 characteristic-three polynomials. A general Hermitian-twist table elsewhere remains a priority risk.

## value

PASS

PASS: within a naturally preclassified complete three-parameter rational point/flex stratum, the exact F9 Jacobian isogeny decomposition splits into two classes despite identical rational-point and tangent-contact profiles. Two exact zeta numerators are invariant classification data a researcher can use to distinguish arithmetic types; the statement is not a mere recomputation of an already known zeta table. Distinction is meaningful and exact even though the census is finite.

The dated certificate retains the supplied scientific assessment, sources and limitations.
