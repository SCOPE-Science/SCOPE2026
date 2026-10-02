# Independent audit — 2026-10-01

## Final claim

For every smooth strictly convex planar body of fixed perimeter, the fractional-perimeter deficit satisfies the displayed explicit curvature-radius negative-Sobolev lower bound, with the corresponding explicit chord-functional deficit.

## Correctness — PASS

The proof constants check out. The tangent supporting-line deficit is uniformly stronger than the claimed coefficient on the central angular window. The source Willmore/Hölder step then gives the factor with power of two stated in the record; Parseval yields the exact spectral minimum \(\pi-2/3\) at Fourier mode three. For normalized outer parallel bodies, changing from tangent angle to arclength gives the factor \(r/(1+r)^3\). The integral of \(r(1+r)^{q-3}\) is \(1/((1-q)(2-q))\), and substituting the exact chord-to-fractional-perimeter identity produces the displayed constant. The equality implication \(\rho\equiv1\) is also valid.

Checked sources: A Sharp Planar Fractional Isoperimetric Inequality, arXiv:2609.19052; Sharp comparison between the perimeter and its fractional analogue in two dimensions, arXiv:2609.14513; Stability of the ball in isoperimetric inequalities between two fractional perimeters, arXiv:2605.07543; Global quadratic Hausdorff stability for the planar fractional-perimeter comparison, published finding dated 2026-09-19; Assigned Git package and a fresh independent check of the quantitative concavity, Fourier, parallel-body and integration constants

Residual risks: The exact numerical coefficient is explicit but not claimed optimal.; A same-day published result already establishes the same curvature-radius negative-Sobolev deficit with an unspecified positive constant and then derives a stronger Hausdorff consequence.

## Originality — PASS

The exact explicit coefficient and explicit chord-functional coefficient are not stated in the inspected sources. However, the structural negative-Sobolev stability theorem is already present in a separate same-day published result with an unspecified positive constant, so originality is only for the explicit quantitative refinement, not for the existence of this stability mechanism.

### Equivalent formulations

Searches: Resultary semantic search for fractional-perimeter curvature-radius stability and chord functional deficit; arXiv:2609.19052

Evidence: The search located a separate published result, `Global quadratic Hausdorff stability for the planar fractional-perimeter comparison`, whose proof defines the same curvature-radius primitive energy and proves a deficit bound with an unspecified positive constant.; The audited record supplies a specific numerical coefficient and an explicit chord-functional bound.

Reasoning: The earlier statement is equivalent at the level of existence of a positive curvature-radius stability constant, but not logically equivalent to the audited explicit coefficient.

### Broader coverage

Searches: same-day Hausdorff stability finding; Lin--Yang--Yang--Yuan--Zhang sharp inequality; Alberti--Cozzi--Massaccesi--Mirmina fractional-perimeter stability

Evidence: The same-day finding is geometrically broader in deriving Hausdorff control for all convex bodies after first proving the same negative-Sobolev defect with some constant.; The local two-fractional-perimeter theorem has a different endpoint and class.

Reasoning: The broader finding dominates the qualitative structural content but does not provide the audited numerical coefficient.

### Exact database or table

Searches: exact coefficient `(pi-2/3) sin(pi/8)` and explicit chord-functional coefficient in published-findings and primary-source searches

Evidence: No independent exact table or theorem with the displayed numerical coefficient was located.

Reasoning: This supports only the narrow explicit-constant originality claim.

### Claim versus prior implication

Searches: full proof comparison with the same-day Hausdorff-stability result

Evidence: That result already uses the same quantitative tangent-angle, outer-parallel-body and curvature-radius primitive mechanism, but leaves its compactness/spectral constants non-explicit.; The audited proof makes one concrete nonoptimal constant explicit.

Reasoning: Existence of an unspecified constant does not by itself logically imply this exact lower coefficient, so the explicit inequality is not a formal corollary of the prior statement.

### Source inspections

- **Global quadratic Hausdorff stability for the planar fractional-perimeter comparison** — https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-quadratic-hausdorff-stability-planar-fractional-perimeter--3a652b674803
  Trigger: Same fixed-perimeter fractional-perimeter deficit and same curvature-radius primitive
  Material read: Complete published RESULT.md, including the quantitative Willmore step, outer-parallel-body argument, definition of the same curvature-radius energy, and Hausdorff conversion
  Method: Primary published-finding full-text inspection
  Assessment: Covers the structural stability theorem and proof mechanism, but leaves the positive constant unspecified.
  Evidence: It proves \(P_s(B_1)-P_s(K)\ge c_s J(K)\) for the same curvature-radius primitive energy before deriving Hausdorff stability.
- **A Sharp Planar Fractional Isoperimetric Inequality** — https://arxiv.org/abs/2609.19052
  Trigger: Primary source of the chord identity, fractional-Willmore inequality and outer-parallel first variation
  Material read: Abstract and the source theorem/identity statements available through indexed text; the audit reconstructed the constants used by the assigned proof
  Method: Primary-source inspection plus direct proof reconstruction
  Assessment: Supplies the qualitative sharp inequality and machinery but not the audited explicit deficit.
  Evidence: Its abstract identifies the chord-functional, fractional-Willmore and outer-parallel-body route used here.

Checked sources: A Sharp Planar Fractional Isoperimetric Inequality, arXiv:2609.19052; Sharp comparison between the perimeter and its fractional analogue in two dimensions, arXiv:2609.14513; Stability of the ball in isoperimetric inequalities between two fractional perimeters, arXiv:2605.07543; Global quadratic Hausdorff stability for the planar fractional-perimeter comparison, published finding dated 2026-09-19; Assigned Git package and a fresh independent check of the quantitative concavity, Fourier, parallel-body and integration constants

Residual risks: The exact numerical coefficient is explicit but not claimed optimal.; A same-day published result already establishes the same curvature-radius negative-Sobolev deficit with an unspecified positive constant and then derives a stronger Hausdorff consequence.

## Scientific value — FAIL

After the same curvature-radius stability theorem and stronger Hausdorff consequence are already published using the same mechanism, the surviving distinction is a single nonoptimal explicit constant and its corresponding chord-functional coefficient. The record gives no optimality, new metric, new class, or new structural boundary for that constant. Under the required value bar this is a quantitatively explicit but mathematically too small refinement.

Checked sources: A Sharp Planar Fractional Isoperimetric Inequality, arXiv:2609.19052; Sharp comparison between the perimeter and its fractional analogue in two dimensions, arXiv:2609.14513; Stability of the ball in isoperimetric inequalities between two fractional perimeters, arXiv:2605.07543; Global quadratic Hausdorff stability for the planar fractional-perimeter comparison, published finding dated 2026-09-19; Assigned Git package and a fresh independent check of the quantitative concavity, Fourier, parallel-body and integration constants

Residual risks: The exact numerical coefficient is explicit but not claimed optimal.; A same-day published result already establishes the same curvature-radius negative-Sobolev deficit with an unspecified positive constant and then derives a stronger Hausdorff consequence.

## Limitations

- Smooth strictly convex planar bodies with positive curvature only.
- The controlled metric is curvature-radius negative-Sobolev deviation; constants are not optimal.
- Scientific rejection is on value after prior structural coverage, not on correctness.

## Conclusion

Disposition: **failed**. Acceptance requires PASS on all three axes.
