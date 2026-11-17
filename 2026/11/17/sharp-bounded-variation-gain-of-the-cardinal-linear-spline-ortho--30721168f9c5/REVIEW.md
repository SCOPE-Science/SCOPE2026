# Scientific review

## Correctness — PASS
The Gram inverse is an absolutely summable geometric Green function with ratio \(\sqrt3-2\), and substitution verifies the exact nodal response to any Heaviside jump. The two geometric gradient tails reduce the full variation of a projected jump to \(1-A-B+\sqrt3(|A|+|B|)\). Direct sign analysis gives the three explicit subcell formulas, all bounded by \(\sqrt3\), with knot jumps attaining equality. Distributional derivative decomposition then proves the operator bound for every real bounded finite-variation input. Two well-separated jumps give compactly supported \(L^2\) near-extremizers. The executable checker independently tests Gram equations and exact rational finite-mesh systems. No numerical evidence substitutes for an infinite proof.

## Originality — PASS, with residual risk
The closest primary works treat the same spline projector but with \(L^\infty\) rather than homogeneous \(BV\) operator norms (Oswald 2006 and Passenbrunner 2016), or a different total-variation-diminishing *interpolant* (Nochetto–Salgado 2012). The complete accessible published projector computations on uniform and alternating meshes likewise concern supremum norms, endpoint range or slope response on bounded inputs, and do not state or logically imply the sharp all-line variation norm or subcell jump profile. Searches of exact parameter values, aliases, and stronger norm formulations did not locate coverage. The 2004 Box-spline paper's accessible sections concern \(L^1\)-approximation-error asymptotics for BV data; its entire source could not be inspected, and unindexed earlier equivalents remain possible. Originality is consequently a best-knowledge claim, not a uniqueness certificate.

## Mathematical value — PASS
The exact sharp stability coefficient for a classical nonlocal least-squares smoother is a natural stability invariant: positive quasi-interpolation can diminish variation, whereas an orthogonal projector need not. The result determines the all-input coefficient, its complete within-cell jump-location dependence, and the unusual fact that grid-aligned discontinuities are uniquely worst despite interior jumps. These facts distinguish smoothing norms and inform stability analyses of discontinuity-bearing finite-element data; they are not mere restatements of classical inverse-Gram identities.

## Closest literature and limitations
Oswald, arXiv:math/0611573v1 (2006); Nochetto–Salgado, arXiv:1211.1069v1 (2012); Passenbrunner, arXiv:1608.06720v1 (2016); published exact uniform-spline endpoint overshoot and two-periodic supremum-norm calculations (different target norms). Only full-line real uniform degree-one cardinal splines are classified. Historical priority and distinct nonuniform and finite-domain variants remain unsettled.

Self-review: passed. Independent audit: not yet performed.
