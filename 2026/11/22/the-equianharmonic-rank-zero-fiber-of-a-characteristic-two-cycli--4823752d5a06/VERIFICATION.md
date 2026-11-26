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

For t not 0 or 1, Riemann–Hurwitz for four full tame ramification points gives genus 6. The six listed differential forms are regular; at a finite branch the bound 6-j suffices (at x=0 the actual order for x^i dx/y^j is 6-j+7i); the infinity orders follow from x,y,dx having orders -7,-3,-8. Kummer characters distinguish the groups, and 1,x are independent in each double group. Write c=sqrt(t), d=sqrt(1+t). Extracting odd coefficients of x^i f for odd j, and of x^i for even j, checks the action, including C(e5)=e0 and C(e1)=C(e4)=0. Put v=c e2+e3 and w=c sqrt(c) e4+(sqrt(c)+d)e5. Image C has basis v,e4,e5,e0 because c,d are nonzero, so image C^2 has basis w,v,e0. On this latter space, e0 maps to v, v to w, and w to sqrt(sqrt(c)+d)e0, with inverse-Frobenius semilinearity. The last coefficient is zero exactly when t=(1+t)^2. In that case subsequent images are span(v,w), span(w), and zero; otherwise the three-line image is stable. Stable rank is the 2-rank and the Cartier kernel dimension is the a-number. The two roots are exchanged equivariantly by x=tX, rescaling y by a seventh root of t^3. The recorded finite-field replay starts at C^1 and matches both profiles; the code and record were inspected, not rerun, and the symbolic proof handles all t.

## originality

PASS

The family-wide classification of ranks, the exact locus of the jump, and its interpretation as one exceptional cover class were not covered in the inspected comparisons. The exceptional member's Cartier profile itself is already a consequence of the Fermat-curve result of Pries–Ulmer and should not be credited as a stand-alone novelty. The generic stable rank is also the natural character-orbit upper bound; the substantive comparison is exact everywhere outside the exceptional locus and for all powers, not just a bound or an example of attainment.

## value

PASS

For a natural tame family rather than an isolated table entry, the explicit return scalar detects a dramatic smooth-fiber drop of stable rank even though the first two ranks never jump. The full power profiles identify when the degeneration becomes visible and what nilpotence it produces. This exact coefficientwise invariant is useful for distinguishing these fibers; the covered Fermat case alone would not satisfy the value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
