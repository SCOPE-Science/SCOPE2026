---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For E=[0,a] union [a+g,a+g+b], a,b,g>0, set s=a+b, r=ab, d=g+s/2 and c_2=I''(0)/2, c_4=I^(4)(0)/24, I=|Fourier 1_E|² with exponent -itx. Direct double-integration/sinc expansion yields c2=-s^4/12-r(d²-s²/4), hence q=-c2-s^4/12=rg(g+s)>0. Eliminating d² from c4 gives c4=s^6/360+q s²/12+q²/(12r)-qr/12. For fixed s,q>0 this is strictly decreasing for 0<r<=s²/4; the quadratic qr²+yr-q²=0 (y=12c4-s^6/30-qs²) has one positive root, recovering r, the unordered lengths and g. Its endpoint at r=s²/4 gives sharp necessary and sufficient feasible-jet bound c4>=s^6/360+q s²/16+q²/(3s²), equality iff a=b. Varying r at fixed s,q gives infinitely many same zeroth/second-jet noncongruent intervals, proving minimality. Independently verified 27 exact-rational examples using difference moments. The proof handles all positive lengths/gaps, not noise stability.

## originality

PASS

Best-of-knowledge PASS, with significant named priority risk. Xia–Xu 2026 arxiv:2606.19855 proves full Fourier-magnitude uniqueness and stability for finite unions of intervals, including two intervals. Whole-magnitude uniqueness does not logically imply that only derivatives through order four suffice, that this order is minimal, or the precise feasible-jet inequality. The same-object Xia–Xu paper's FULL text could not be retrieved despite arXiv/OA attempts; authorized Oxford access reported VPN disconnected. Only its abstract was inspected, so no whole-document NOT_COVERING conclusion is made. Independent finite-jet identities remain unimplicated by observed statements subject to latent coverage in unread full text.

## value

PASS

Reducing infinite Fourier intensity measurement to exactly three real Taylor-jet numbers is a substantial identification fact for a natural two-component geometric signal class. The sharp minimality and feasible measurement region are useful for moment-based inverse geometry, even though derivative measurement is idealized and the inverse becomes ill-conditioned at degenerations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
