# Second-order e-power gain of the admissible Fisher symmetry e-test
## Finding
Let \(Z_1,\ldots,Z_n\) be iid \(N(\theta,1)\), and tune both Fisher-type symmetry e-variables at \(\lambda=\theta\). For one observation define the admissible factor
\[
A_\theta(Z)=\frac{\exp(\theta Z)}{\cosh(\theta Z)}
\]
and the quadratic factor
\[
Q_\theta(Z)=\exp\!\left(\theta Z-\frac{\theta^2Z^2}{2}\right).
\]
Write their one-observation e-powers as
\[
a(\theta)=\mathbb E_\theta\log A_\theta(Z),\qquad q(\theta)=\mathbb E_\theta\log Q_\theta(Z).
\]
Then, as \(\theta\to0\),
\[
a(\theta)=\frac{\theta^2}{2}-\frac{\theta^4}{4}+\frac{\theta^6}{6}-\frac{5\theta^8}{24}+O(\theta^{10}),
\]
whereas exactly
\[
q(\theta)=\frac{\theta^2}{2}-\frac{\theta^4}{2}.
\]
Moreover \(A_\theta(z)\ge Q_\theta(z)\) for every real \(z\), with strict inequality whenever \(\theta z\ne0\). Thus for every nonzero \(\theta\), the admissible Fisher factor has strictly larger e-power under \(N(\theta,1)\).

For a fixed target e-power \(\beta>0\), define the continuous sample-size budgets
\[
N_A(\beta,\theta)=\frac{\beta}{a(\theta)},\qquad N_Q(\beta,\theta)=\frac{\beta}{q(\theta)}.
\]
For sufficiently small nonzero \(\theta\),
\[
N_A(\beta,\theta)=2\beta\theta^{-2}+\beta-\frac{\beta}{6}\theta^2+\frac{5\beta}{12}\theta^4+O(\theta^6),
\]
\[
N_Q(\beta,\theta)=2\beta\theta^{-2}+2\beta+2\beta\theta^2+2\beta\theta^4+O(\theta^6),
\]
and hence
\[
N_Q(\beta,\theta)-N_A(\beta,\theta)=\beta+\frac{13\beta}{6}\theta^2+\frac{19\beta}{12}\theta^4+O(\theta^6).
\]
Therefore the two procedures have the same first-order Pitman efficiency, but their continuous sample-size budgets differ at the next order by \(\beta+o(1)\) observations.

## Assumptions and scope
The alternative is exactly iid Gaussian \(N(\theta,1)\), used as the assay model in Vovk and Wang's efficiency analysis. The tuning \(\lambda=\theta\) is the natural local tuning used there for the Fisher-type e-test. The comparison is between their admissible Fisher factor and the quadratic e-variable that it pointwise dominates. The constant \(\beta\) is a fixed target for expected log e-value (e-power).

The quantity \(N_A\) or \(N_Q\) is a continuous budget. If an integer sample size is required, ceilings introduce an unavoidable bounded lattice effect, so the displayed constant difference should not be read as a limit for the difference of two integer ceilings.

## Proof
Vovk and Wang's Fisher-type e-variable at \(\lambda=\theta\) has one-observation factor \(A_\theta(Z)\). Their quadratic surrogate has factor \(Q_\theta(Z)\). Since
\[
\log\cosh x\le \frac{x^2}{2}
\]
for all real \(x\), with strict inequality for \(x\ne0\), one has \(A_\theta(z)\ge Q_\theta(z)\), strictly when \(\theta z\ne0\). Under a continuous Gaussian alternative and \(\theta\ne0\), strictness holds almost surely and therefore also after taking expected logarithms.

Let \(Z\sim N(\theta,1)\). Because \(\mathbb E_\theta Z=\theta\),
\[
a(\theta)=\theta^2-\mathbb E_\theta\log\cosh(\theta Z).
\]
The real Taylor expansion is
\[
\log\cosh x=\frac{x^2}{2}-\frac{x^4}{12}+\frac{x^6}{45}-\frac{17x^8}{2520}+O(x^{10}).
\]
All derivatives of \(\log\cosh x\) of order at least one are bounded combinations of \(\tanh x\) and \(\operatorname{sech}x\); hence the remainder may be bounded by a constant times \(|x|^{10}\). Since Gaussian moments of \(Z\sim N(\theta,1)\) remain bounded for \(\theta\) near zero, expectation preserves the \(O(\theta^{10})\) remainder.

Using
\[
\mathbb E_\theta Z^2=1+\theta^2,
\]
\[
\mathbb E_\theta Z^4=3+6\theta^2+\theta^4,
\]
\[
\mathbb E_\theta Z^6=15+45\theta^2+15\theta^4+\theta^6,
\]
and
\[
\mathbb E_\theta Z^8=105+420\theta^2+210\theta^4+28\theta^6+\theta^8,
\]
substitution gives
\[
\mathbb E_\theta\log\cosh(\theta Z)=\frac{\theta^2}{2}+\frac{\theta^4}{4}-\frac{\theta^6}{6}+\frac{5\theta^8}{24}+O(\theta^{10}),
\]
which proves the expansion for \(a(\theta)\).

For the quadratic factor no asymptotic expansion is needed:
\[
q(\theta)=\theta\mathbb E_\theta Z-\frac{\theta^2}{2}\mathbb E_\theta Z^2
=\frac{\theta^2}{2}-\frac{\theta^4}{2}.
\]
Factoring \(\theta^2/2\) from both e-powers and formally inverting their convergent local series yields
\[
\frac1{a(\theta)}=2\theta^{-2}+1-\frac{\theta^2}{6}+\frac{5\theta^4}{12}+O(\theta^6)
\]
and
\[
\frac1{q(\theta)}=2\theta^{-2}+2+2\theta^2+2\theta^4+O(\theta^6).
\]
Multiplication by \(\beta\) and subtraction prove the sample-budget formulas.

## Verification
The accompanying `verify.py` uses exact rational arithmetic. It reconstructs the centered-normal moment polynomials, composes them with the Taylor coefficients of \(\log\cosh\), checks the coefficients of \(a(\theta)\) through order eight, verifies the exact polynomial for \(q(\theta)\), and multiplies the claimed inverse series back through the required orders. It prints `VERIFY_OK` only if every exact identity passes.

The strict pointwise domination is analytic: it is equivalent to \(\log\cosh x<x^2/2\) for \(x\ne0\). One proof differentiates \(x^2/2-\log\cosh x\): its derivative is \(x-\tanh x\), which is positive for \(x>0\), and the function is even and vanishes at zero.

## Relationship to prior work
Vovk and Wang introduce the admissible Fisher-type symmetry e-variable, exhibit the quadratic de la Peña e-variable that it dominates, and note that the domination is especially close in the small-signal regime. In their Gaussian assay model they derive the leading Fisher e-power \(n\theta^2/2\) and therefore first-order asymptotic relative efficiency one. Their displayed derivation stops at the leading term.

The present refinement keeps enough terms to distinguish the admissible and quadratic factors at second order. It quantifies the pointwise admissibility improvement as a \(\theta^4/4\) leading gain in one-observation e-power and as a \(\beta+o(1)\) reduction in the corresponding continuous sample-size budget. Targeted searches of the source article and of relevant research indexes did not locate these coefficients or this sample-budget comparison. The broader literature on admissible anytime-valid inference explains why inadmissible e-processes can be dominated, but does not by itself imply these Gaussian local coefficients.

## Limitations
This is a local \(\theta\to0\) refinement under the Gaussian assay model, not a uniform efficiency theorem over all symmetric alternatives. It does not optimize over data-dependent or mixture choices of \(\lambda\), and it does not compare the other admissible alternatives discussed in the sequential-inference literature. The sample-budget statement is for expected log e-value and continuous budgets; integer ceiling effects remain bounded but can prevent a literal integer-valued difference from converging.

The literature comparison cannot rule out an older or differently phrased derivation of the same Taylor coefficients. The claim is therefore limited to the mathematical refinement and the inspected-source comparison, not an assertion of exhaustive historical priority.

## References
1. V. Vovk and R. Wang, “Efficiency of nonparametric e-tests,” arXiv:2208.08925, first posted 2022-08-18; journal version “Nonparametric E-tests of Symmetry,” New England Journal of Statistics in Data Science, 2024. https://arxiv.org/abs/2208.08925
2. A. Ramdas, J. Ruf, M. Larsson, and W. Koolen, “Admissible anytime-valid sequential inference must rely on nonnegative martingales,” arXiv:2009.03167, first posted 2020-09-07. https://arxiv.org/abs/2009.03167
