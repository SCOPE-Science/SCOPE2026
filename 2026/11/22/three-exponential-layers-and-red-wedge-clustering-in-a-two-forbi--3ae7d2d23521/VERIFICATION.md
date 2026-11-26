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

Neutral cross-edges give strong amalgamation, and homogeneity in the finite relational language makes each admissible named complete diagram exactly one complete type. Triangles with vertices in different old matching blocks have a neutral edge, so the old blocks impose independent constraints. Each new label has nine pairs of attachment colours less (R,R), giving b(H)^m for a fixed labelled internal graph H. For a red edge the four states without red allow eight choices at the other end, and the four states with one red allow six: 56. For a green edge the two excluded events are that both new vertices attach green to the first old endpoint or that both attach green to the second. They have sizes 9 and 9 with intersection 1, giving 47. The explanatory words about a red attachment in RESULT.md line 15 are a slip; its constraint on line 13 and the stated result use the correct green event. A red wedge has weight 4·8²+4·6²=400. In an independent enumeration (`python3 /workspace/reviews/reproduce_2_3_5.py`), the incident two-edge weights RR,RG,GG are 400,324,301 and the disjoint weights are 3136,2632,2209. Every competitor without a red wedge is bounded by a one-green or nonwedge two-edge pattern strictly below 25/32 after normalizing. Any extra edge in a wedge-containing pattern reduces its weight strictly: colour only the two chosen attachments to a single old endpoint by the extra edge colour, all other attachments neutral. This respects the original wedge and violates the added constraint. Hence for fixed r there is a strict finite gap beyond the three stated layers. Ordered labels give binomial(r,2) red edges and 3 binomial(r,3) wedges; division after restricting to at least two nonneutral internal edges proves concentration under the uniform type distribution. No growing-arity bound is used.

## originality

PASS

Earlier one-colour Henson results give both the product-count structure and a genuinely close three-layer/wedge law. The distinct claim supported here is the exact red/green asymmetric spectrum and the strictly dominant red wedge for this three-state palette and red-matching base. The one-colour results do not compare the additional green competitors or mechanically supply these coefficients. Bounded best-of-knowledge judgment.

## value

PASS

The base and two forbidden relations define a natural asymmetric test of the one-colour clustering phenomenon. The exact third layer and its strict motif classification show clumping specifically in red despite both colours being constrained; an existence theorem or a small-arity count does not capture that. The all-fixed-arity formula and quantitative gap connect the local colour constraints to a limiting structure. Value lies in this asymmetric extension, not in the abstract idea of independent block counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
