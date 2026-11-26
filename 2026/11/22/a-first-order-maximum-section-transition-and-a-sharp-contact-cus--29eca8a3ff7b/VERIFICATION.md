---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Reconstructed the entire centroidal profile and comparison. Horizontal slice area proportional to z gives centroid 2H/3; the plane graph Jacobian is R²√(1+κ²s²), and completing the square in normalized base coordinates gives a disk cut at u=1/(3s), tangent exactly at s=1/3. The vertical integral gives 4RH/3. For s>1/3, writing Fε(w)=√((2/3+w−εw²)₊) on [−2/3,1/3] with ε=s⁻² both proves the strict bound sS<4/3 and justifies the first variation: [F0−Fε]/ε is dominated by w²/√(2/3+w), with pointwise limit half that bound. The integral of the bound is 2/5, yielding T(∞)=5/3. The strict comparison after squaring is κ²<T(s), with equality exactly at κ²=T(s); T increases to contact, T(1/3)>3, and its right derivative at contact is positive. Thus the maximizers of T are contained in a compact subset of (1/3,∞). The finite maximizers near the switch on the oblique side also remain bounded, since having area greater than vertical requires T(s)>κ² and the limiting T is strictly below κ*². Contact depth has derivative 18/5 and disk radius 5/6; direct width integration gives the normalized loss coefficient 24√6/5 (Euclidean area loss also includes the smooth graph factor). Haar probability follows from uniform |N_z| and tan β=κs, with the stated scale inverse. Independently reproduced a numerical stationary candidate at s≈0.36724362585 and √T≈1.98151821145; that is corroboration only. The packaged checker was inspected, not executed; no certified decimal, uniqueness of finite maximizer, or formal verification is inferred.

## originality

PASS

Best-of-knowledge pass for the capped centroidal threshold and combined contact signature, not for classical circular segment geometry or the cap exponent in isolation. No equivalent result emerged from the actual comparisons below.

## value

PASS

This solves the natural orientation extremum over all centroidal planes for a basic nonsymmetric solid, throughout all aspect ratios. The finite-oblique/vertical coexistence and discontinuity are substantive, since they require a global comparison rather than identifying a tangency or performing a standard ellipse integral. The contact cusp and aspect-ratio inference add useful exact geometry but would not alone carry the value case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
