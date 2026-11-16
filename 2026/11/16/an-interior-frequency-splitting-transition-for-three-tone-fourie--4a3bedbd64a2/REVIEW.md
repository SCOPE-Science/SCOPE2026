# Scientific review: interior Fourier leverage transition

## Correctness

**PASS.** The three-tone Gram matrix is diagonal in the orthogonal basis \(1\), \(\cos(dt)-\operatorname{sinc}d\), \(\sin(dt)\), yielding the stated exact evaluation norm. The removable collision expansion through order four follows from entire factorial series and rational division. The cubic is negative through \(1/2\), strictly increasing thereafter, and has one root in \((0.645,0.646)\). The quartic coefficient at that root is negative by the exact division remainder \(-4R/5\). The analytic implicit-function theorem then yields the unique small positive critical-gap branch and the stated square-root and gain laws. The standalone exact-rational and independent Gram checks execute successfully, but computational samples do not substitute for this proof.

## Originality

**PASS against the inspected literature, not certified publication priority.** Zhang (2026), arXiv:2607.10501, §5.3, bounds sparse-Fourier **exterior** leverage but does not state the signed **interior** collision-opening transition. The published *Sharp endpoint Nikolskii constant for symmetric three-tone Fourier sums* supplies the same orthogonal basis and handles only endpoint evaluation; its conclusion at \(|x|=1\) cannot give the present interior algebraic threshold or bifurcating branch. Erdélyi (2016), Theorem 2.3, gives a generic trigonometric exponential-sum pointwise norm inequality rather than the exact splitting geometry. Classical Legendre interpolation gives the collision-limit value but not the effect of opening a gap. A separately known exact sharp midpoint norm concerns a global optimum at \(x=0\), not the interior transition at \(x\approx0.803739\). Relevant published-record searches for aliases, interior Christoffel functions, and local frequency splitting did not reveal a dominating theorem. Differently indexed exact Gram perturbation literature remains a priority risk.

## Mathematical value

**PASS.** The natural inverse problem is worst-case noise amplification when evaluating a three-tone sparse Fourier reconstruction at a point within the observation window as the frequencies emerge from an unresolved cluster. The algebraic transition divides measurement points where a small physical frequency separation worsens amplification from those where it improves it; the critical fourth-order cancellation and square-root emerging optimal gap give a nontrivial local phase diagram. This goes beyond reporting an isolated Taylor coefficient, while avoiding an unsupported global-optimality assertion.

## Limitations and closest material

The claim is only local near a triple collision and for equally spaced frequencies under averaged Lebesgue \(L^2\) observation. It does not settle the unrestricted frequency-gap optimum, arbitrary nonsymmetric triples or off-interval prediction. The closest mathematical writings inspected were Zhang, arXiv:2607.10501 (full accessible HTML including §5.3), the complete published symmetric three-tone endpoint proof, and Erdélyi, arXiv:1602.02315 (Theorem 2.3 and its proof). An older exact identity may still exist outside indexed terminology; independent mathematical audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
