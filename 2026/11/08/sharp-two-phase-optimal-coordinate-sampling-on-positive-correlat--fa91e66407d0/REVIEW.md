# Scientific review

**Finding assessed.** A sharp two-phase formula for the globally optimum fixed iid exact-coordinate sampling on positive-correlation friendship-matrix quadratics, for all integers \(m\ge2\), \(0<s<1\), \(t>0\), and \(2mt^2<1+s\). The claim is precisely the theorem in RESULT.md, not a claim that arbitrary coordinate methods or all Hessians share the formula.

## Correctness — PASS

The normalized Hessian is SPD because its eigenvalues split into \(1-s>0\), \(1+s>0\), and the positive radial two-by-two block of determinant \(1+s-2mt^2>0\). The exact expected energy decrement yields a smallest-eigenvalue objective that is concave in the sampling probabilities. Symmetry averaging is globally valid, not an assumption that asymmetry cannot help. With one hub mass and identical leaf masses the spectrum separates into a pair-antisymmetric eigenvalue and a two-by-two radial block. The radial problem is solved exactly by a strictly convex one-variable normalization; the pair-limited problem by a single crossing of a concave radial minimum and a decreasing linear pair branch. The crossing and every denominator are positive throughout the declared domain, with both branches identical at the transition. All endpoints of the probability simplex have zero or lower rate because loss of a coordinate makes the Gram matrix singular. A standalone exact-rational verification replay checks 343 admissible parameter designs, 34,643 comparison-grid points, 46 energy identities, and the rational witness. These finite checks are corroboration; the general result uses the symbolic proof.

## Originality — PASS on inspected evidence, with a residual priority risk

The exact-optimal-sampling SDP and the E-optimal-design equivalence encompass this problem in an implicit sense. They do not, in the inspected sections and statements, evaluate this family or its sharp radial/leaf antisymmetry transition. The closest accessible explicit theorem requires an entrywise nonnegative inverse, which the present family does not satisfy in general (for example, the illustrated two-pair positive triangle matrix has incompatible inverse off-diagonal signs). Claim implications, not just titles, were compared. Primary full texts inspected include Qu–Richtárik 2014, Gower–Richtárik 2015, Pukelsheim–Torsney 1991, and Agaskar–Wang–Lu 2014. A general E-optimal-design formula might be rediscovered as an equivalent earlier specialized identity, so expert priority assessment is not claimed.

## Mathematical value — PASS

The matrix is a natural positive-correlation model on a friendship graph with independently adjustable leaf-pair and hub couplings. Unlike inverse-positive systems it contains frustrated positive triangles, making a standard closed-form optimal-sampling theorem inapplicable. This theorem supplies the complete optimum, positivity domain, and a sharp active-eigenmode phase change across an unbounded family of dimensions, rather than a small enumerated example. Its exact sampler can improve the guaranteed sharp worst-case one-step energy decrement over uniform sampling. The result is for its declared design criterion, not a general performance claim about numerical solvers.

## Literature, evidence, and limits

Relevant full texts and mathematical comparisons are listed in RESULT.md and AUDIT.json. General SDP formulations are broader in admissible matrices but weaker as explicit solved formulas; E-optimal designs pose equivalent optimization without the particular phase diagram. Previously published inverse-positive results have a stronger closed form on a different hypothesis class and do not imply this positive-triangle classification. The scientific priority risk lies in older specialist E-optimal design/diagonal scaling results not exhaustively excluded by literature retrieval. No independent review, formal proof assistant, or external validation is asserted.

Self-review: passed. Independent audit: not yet performed.
