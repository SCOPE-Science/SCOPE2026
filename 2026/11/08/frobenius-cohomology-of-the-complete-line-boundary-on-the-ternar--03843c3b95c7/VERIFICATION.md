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

For the F3 Fermat quartic, the F9 Hermitian-surface structure gives 280 rational points and exactly 112 geometric generator lines, four through each crossing. F3 restriction is a split nondegenerate quadric with 16 points and 8 F3 generator lines; all others are 52 Frobenius pairs. Therefore normalization of the reduced 112-line divisor consists of 8 P1/F3 plus 52 P1/F9, and its 280 singular points are 16 fixed plus 132 pairs. Above fixed nodes 32 branches are fixed and the remaining branch orbits comprise 544 pairs; ordinary fourfold tangent directions yield arithmetic genus 1569 and H1 dimension 729. Exact sheaf normalization sequence gives H1 +1 multiplicity 369, -1 360; H2 weighted component classes are 60*(+3)+52*(-3). K3 Weil bound plus #S(F3)=16, #S(F9)=280 forces its H2 eigenvalues 12*(+3),10*(-3), and subtraction yields U=(Q-3)^2 odd degree and (Q-9)(Q-81) even degree; zeros exactly degrees 1,2,4. Independently reproduced genus, eigenspace trace, and first eight extension counts; the finite Hermitian enumeration source algorithm was inspected, not blindly accepted as infinite proof.

## originality

PASS

PASS with significant qualification: Rams–Schütt and Hermitian generalized-quadrangle theory establish 112 lines and 280 geometric crossings; an earlier published specific-geometry critical-group paper establishes the eight F3-fixed lines and 52 conjugate pairs and the K_(4,4) rational-line subgraph. Those exact ingredients strongly constrain and may make the new formulas accessible by standard descent; nonetheless the inspected earlier main claims concern geometric lines or integral graph critical groups, not the full reduced divisor motivic/cohomological Frobenius class or the precise point-free extension degrees of its OPEN COMPLEMENT. The latter complete natural arithmetic package is independently derived here, but historical equivalence via standard normalization is a material residual risk.

## value

PASS

The boundary of all lines on the maximally lined characteristic-three K3 quartic is a canonical divisor; its cohomology and complete extension-wise point-free criterion for the complementary open K3 are exact natural invariants that can support future arithmetic-geometric and rational-point investigations. This is more than a numerical example, while the source line/point counts are explicitly acknowledged prior results. No new classification of all twists or integral cohomology is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
