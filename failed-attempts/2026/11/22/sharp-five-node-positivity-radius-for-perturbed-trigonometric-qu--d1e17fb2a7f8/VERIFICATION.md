---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Five distinct nodes give uniqueness: after multiplication by z^2, any trigonometric polynomial of degree two vanishing there becomes an ordinary polynomial of degree at most four with five distinct roots. The cardinal four-sine denominator is positive in the lifted cyclic order (four negative sine factors); integrating the constant moment gives the sum of three cosines divided by 8D. With half-gaps u,v,w the numerator is cos(u+2v+w)+2 cos(u)cos(w). For alpha<=alpha_*<1/4 the outside angle derivatives are strictly positive in a and negative in d, since u,w are in (0,pi/2) and u+2v+w in (0,pi). Thus the minimum uses a at its left endpoint and d at its right endpoint. Expanding the four inner corners gives the displayed three distinct expressions; the stated difference factors are positive for 0<pi*alpha/5<=pi/20 by the bounds on the sines. In either inner angle each term satisfies S''+S/4=0. On its interval the sine interpolation coefficients are nonnegative with sum at least one, and strictly positive in the interior. Consequently the nonnegative corner lower bound extends to the box, and at the threshold only the alternating corner gives zero; the target offset enters only D and can be arbitrary. The corner numerator strictly decreases on [0,1/2), is 1/2 at zero and 1-sqrt(5)/2<0 at 1/4, so the exact arccos root and the larger-radius negativity follow. Both the specified exactness and the comparison with conditioning are meant for the same dimensionless grid-spacing jitter. The exact formula is correct; the last printed decimal digit is a roundoff artifact: the value is 0.20145942246051052177..., not 0.2014594224605106.... The supplied verifier was inspected, not run. A separate 50-digit complex cardinal-polynomial coefficient calculation (python3 /workspace/review_checks.py 5) confirms the sign switch and unique alternating corner for the fixed unperturbed target; this finite check does not replace the interior proof.

## originality

FAIL

The distinct indexed finding 02df184d2d31 explicitly gives the same sharp universal nonnegative-weight radius for the same degree, five independently perturbed equispaced nodes, the same boundary zero phenomenon with an alternating pattern and failure beyond the boundary. If theta=arccos(sqrt(cos(pi/5)/2)), then 2theta lies in (0,pi), cos(2theta)=cos(pi/5)-1, and the two advertised radii are identical. This is verified equivalent coverage of the central assertion, not merely similarity of titles or of parameters. The shared date does not establish publication order. The available summary does not settle whether every equality configuration including unrestricted target offset is included in the other proof; the audit does not assert that it is. That unresolved refinement does not make the frozen record's principal sharp-radius claim distinct.

## value

FAIL

The exact tolerance is a meaningful stability invariant in itself, but it is already supplied by a distinct exact record at the same size and degree. The frozen presentation does not establish a separate worthwhile increment sufficient to validate it as a distinct finding. The potentially narrower exclusivity claim is true here, but the alternating boundary design is already reported and the free target is immediate from the cardinal numerator; the distinctness of the complete classification was not established. No repair is submitted: a decimal correction or a relabeling of the overlapping threshold could not remedy that problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
