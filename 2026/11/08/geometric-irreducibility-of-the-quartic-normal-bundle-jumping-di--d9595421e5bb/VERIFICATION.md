---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The published cohomology matrix is applicable to the specified honest unramified opens. The transpose is a map of binary-form spaces: its first output is v2 b2+v3 b3−wc for cubic multipliers b2,b3,c, and the two other outputs sum the two quartic derivatives against linear multipliers plus the three quadratic derivatives against those cubic multipliers. Thus source coordinate changes preserve nonvanishing on the full coefficient space by the chain rule (an invertible change also on the derivative output pair), and target GL2 mixing v2,v3 is an invertible change of the two corresponding multipliers. The separable double cover given by the coprime quadratics has two distinct ramification points and branch values; moving these to coordinate points puts the cover in square-map form. The independently reproduced first two witness polynomials vanish together only when B=0 and AC=0, and the third excludes each nonzero axis. Hence there is no identically zero quartic fiber over w≠0. The reproduced plane section has three isolated ordinary nodes and no other geometric singularities over F101, so it is reduced. If reducible, a line and the residual cubic meet in three distinct nodes on that line (all intersections must be transverse, with two branches), or two conics meet in four distinct nodes; both contradict the certificate. Specialization preserves the implication from absolute irreducibility modulo 101 to characteristic zero: classes of factorizable quartics are closed by the proper projective multiplication maps in degrees (1,3) and (2,2), and this quartic has nonzero reduction. A nonzero homogeneous restriction cannot send a factor of positive degree to a unit, so the ten-variable quartic fiber is absolutely irreducible too. The two chosen quadratics are coprime and w≠0. The family over w≠0 is a flat projective family of hypersurfaces (relative Cartier), giving a geometrically integral generic fiber. The unique horizontal component has multiplicity one. A vertical divisor could dominate only a codimension-one parameter subset with an identically zero fiber, since nonzero projective quartic fibers have dimension eight in P9. The w=0 set has codimension three and cannot support a divisor. The same argument on the affine quartic coefficients gives the integral divisor before quotient; an effective Cartier hypersurface in the regular coefficient space has no embedded components. Restrict to the honest unramified open, nonempty along the divisor by the published point q0. The Cox parameter projection is locally a torus torsor on the map space; irreducibility passes to the image and reducedness descends faithfully flatly. This proves integrality on U without inferring it from the divisor class or from that one smooth point.

## originality

PASS

The determinant, balanced generic bundle, nonemptiness, divisor class and particular reduced or smooth points are prior; the supported distinct assertion is that the entire determinantal first jumping divisor on U is integral.

## value

PASS

For the natural first degeneracy locus of this specific normal-bundle family, integrality determines that there is a single geometric component with generic scheme multiplicity one, a fact not encoded by the expected splitting, Cartier class, or a transverse section. The explicit fiber and exclusion of parameter-only factors give a way to settle that structural question without classifying the deeper strata.

The dated certificate retains the supplied scientific assessment, sources and limitations.
