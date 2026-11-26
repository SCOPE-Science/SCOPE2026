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

The unchanged theorem in the replacement RESULT.md is specifically about strict crossings. At the interface the left and right normals are 1−y and a+y. The common-positive interval exists only for a>−1 and the common-negative interval only for a<−1; at a=−1 they never have the same nonzero sign. A periodic trajectory with only strict crossings would require both directions. Neither affine saddle can support a cycle within its own open half-plane. At the benchmark the left coordinates (y−x,y−3x−2) have rates (−1,1), and the right coordinates (x+y−2,y−x+1) have rates (3/2,−1/2). Starting at P+, evaluating at e^(T_L)=(1+δ)/(1−δ)=φ⁶ and e^(T_R/2)=(2+δ)/(2−δ)=φ² gives P− in each case. Strict convexity on the left and strict concavity of x_R(t) on the right give the correct interior signs between the contacts. At P+ the normals are (−δ,δ−1/4), and at P− they are (δ,−δ−1/4), so these are repelling and attracting sliding contacts respectively, not fold points. The Filippov tangential field on y<1 is (6y²−5y−2)/(9−8y). Its denominator is positive and its only root on that component is (5−√73)/12; its sign points toward the root on both sides. Each sliding solution is confined between its initial ordinate and the root, hence is global forward and converges. The slope at the root is −3√73/(17+2√73). Independent exact recomputation: /workspace/branches/714facf4-45de-4374-9801-78365fd2cc1a/ordinal4-check-notes.txt. The frozen checker was inspected, not run. Public wording in RESULT.md and SLOGAN.txt was narrowed from nonsliding generally to strict crossing; contacts involving tangencies and cycles with sliding are not classified. The replacement slogan also describes the common endpoint orientation, not monotonicity of the height along both arcs.

## originality

PASS

The primary paper contains the same matrices, level-set matching and contacts, and explicitly calls its Figure 6 loop a limit cycle. The retained result corrects that dynamical interpretation under the same Filippov convention, proves a family-level strict-crossing obstruction for those matrices, and gives the forward flight times and local sliding fate. Related general exclusions inspected here do not cover the pair. Priority remains conditional on the sources inspected.

## value

PASS

This is a checkable counterexample to inferring actual cycling from matched polynomial level sets, tied to a published example claimed to witness sharpness. The strict-crossing obstruction is robust to the two forcing parameters; the exact clocks and sliding capture explain what the two advertised arcs actually do. The correction is valuable even though its decisive interface test is short.

The dated certificate retains the supplied scientific assessment, sources and limitations.
