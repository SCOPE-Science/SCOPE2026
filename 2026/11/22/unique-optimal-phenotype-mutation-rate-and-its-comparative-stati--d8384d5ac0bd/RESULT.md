# Unique optimal phenotype-mutation rate and its comparative statics for binary recognition

## Finding

Consider the weak-selection, large-population benefit-to-cost threshold of Kroumi's finite periodic phenotype model, specialized to exactly two recognition phenotypes: the one-dimensional torus with two sites. For every strategy mutation rate \(\mu>0\) and finite discrimination strength \(\alpha>0\), its cooperation threshold as a function of population-scaled phenotype mutation \(\nu>0\) is **globally strictly convex** and has exactly one global minimizer \(\nu_*(\mu,\alpha)>0\). The minimizer is nondegenerate and increases strictly with **each** of \(\mu\) and \(\alpha\), with the other fixed. Explicit algebraic bounds and a unique scalar equation determine it for all positive parameter values.

Set
\[
\xi=\frac{1-e^{-\alpha}}2\in(0,1/2),\qquad
A(\mu)=\frac{2\mu+1}{2(\mu+1)},\qquad
B(\mu)=\frac{(2\mu+1)(2\mu+3)}{8(\mu+1)}.
\]
The unique optimum is the unique solution \(\nu>0\) of
\[
\boxed{\frac{B(\mu)}{\nu^2}-\frac{A(\mu)}{(\mu+2\nu+1)^2}=4(1-\xi).}
\]
It satisfies the strict bounds
\[
\boxed{\frac{\sqrt{2\mu+1}}{4\sqrt{1-\xi}}<\nu_*<
\sqrt{\frac{(2\mu+1)(2\mu+3)}{32(\mu+1)(1-\xi)}}.}
\]
Here the optimality criterion is solely the **first-order weak-selection stationary-abundance threshold**, not a finite-population fixation probability or an intervention recommendation.

## Assumptions and scope

Use the exact model and mutation normalization of Kroumi (2026, arXiv:2608.21872v1, Eq. (29)). The phenotype space is \(\mathbb Z/2\mathbb Z\), with one binary coordinate (\(L=2,n=1\)); cooperator recognition probability at distance \(d\in\{0,1\}\) is \(e^{-\alpha d}\). Strategy and phenotype mutations follow the neutral coalescent large-population scaling \(\mu=Nu/2>0\), \(\nu=Nv/2>0\), respectively, before the weak-selection limit; this is **not** a claim for arbitrary finite \(N\) or arbitrary selection strength. All other conventions are unchanged from the referenced source.

Write \(\Theta(\nu;\mu,\alpha)\) for the critical benefit-to-cost ratio: weak selection favors mean cooperation precisely if the benefit-to-cost ratio exceeds \(\Theta\), subject to the source model's limiting conventions. Our theorem concerns \(\Theta\) only and holds for all \(\mu,\alpha,\nu>0\).

## Proof

**1. Exact two-phenotype reduction.** On the two-site periodic phenotype space, the difference random walk in the source's Eq. (22) has one nonzero Fourier mode. The one-coordinate recognition expectation and its Laplace transform (source Eqs. (24), (28)) become
\[
\Phi_\alpha(\sigma)=1-\xi+\xi e^{-2\sigma},\quad
\mathcal L(\alpha,x)=\frac{1-\xi}{x}+\frac{\xi}{x+2}.
\]
Define \(c_1=1\), \(c_2=1+2\mu\), \(c_3=3+2\mu\), and \(L_j=\mathcal L(\alpha,c_j/(2\nu))\). The source's exact threshold Eq. (29) reads
\[
\Theta=\frac{(1+2\mu)^2L_1+\mu(3+2\mu)L_3-(1+\mu)(1+2\mu)L_2}
{(1+\mu)(1+2\mu)L_2+\mu(3+2\mu)L_3-(1+2\mu)L_1}.
\]
The substitution \(L_j=2\nu[(1-\xi)/c_j+\xi/(c_j+4\nu)]\), followed by exact rational simplification, gives
\[
\boxed{\Theta(\nu;\mu,\alpha)
=\frac{4(1-\xi)}{\xi}\nu+
\frac{2\mu(1-\xi)+3-2\xi}{\xi}-
\frac{2\mu+1}{4\xi(\mu+1)(\mu+2\nu+1)}+
\frac{B(\mu)}{\xi\nu}.}
\]
All denominators are positive. The accompanying symbolic checker verifies the two exact rational expressions are identical without reliance on numerical optimization.

**2. Strict convexity and uniqueness.** Differentiate and multiply by \(\xi>0\):
\[
F(\nu;\mu,\xi):=\xi\,\partial_\nu\Theta
=4(1-\xi)+\frac{A(\mu)}{(\mu+2\nu+1)^2}
-\frac{B(\mu)}{\nu^2}.
\]
Since \(B-A/4=(2\mu+1)/4>0\), and \(\mu+2\nu+1>2\nu\),
\[
\partial_\nu F=\frac{2B}{\nu^3}-\frac{4A}{(\mu+2\nu+1)^3}
>\frac{2B-A/2}{\nu^3}>0.
\]
Furthermore, \(F\to-\infty\) at \(\nu\downarrow0\), and \(F\to4(1-\xi)>0\) at \(\nu\to\infty\). Thus there is exactly one stationary point, the unique strict global minimum, and \(\Theta''=F_\nu/\xi>0\) everywhere. The optimum is nondegenerate. From \(F(\nu_*)=0\) and \(0<A/(\mu+2\nu+1)^2<A/(4\nu^2)\) one gets
\[
\frac{B-A/4}{4(1-\xi)}<\nu_*^2<\frac{B}{4(1-\xi)},
\]
which is equivalent to the stated bounds.

**3. Strict comparative statics.** The implicit-function theorem applies because \(F_\nu>0\). Since \(F_\xi=-4\) and \(d\xi/d\alpha=e^{-\alpha}/2>0\),
\[
\partial_\alpha\nu_* = \frac{2e^{-\alpha}}{F_\nu(\nu_*)}>0.
\]
For the strategy mutation derivative, write \(A=1-[2(\mu+1)]^{-1}\) and \(B=(\mu+1)/2-[8(\mu+1)]^{-1}\). Thus
\[
A'(\mu)=\frac1{2(\mu+1)^2},\qquad
B'(\mu)=\frac12+\frac1{8(\mu+1)^2},
\]
and
\[
F_\mu=\frac{A'}{(\mu+2\nu+1)^2}-\frac{2A}{(\mu+2\nu+1)^3}-\frac{B'}{\nu^2}
<\frac{A'/4-B'}{\nu^2}=-\frac1{2\nu^2}<0.
\]
Consequently \(\partial_\mu\nu_*=-F_\mu/F_\nu>0\). This completes the theorem for the entire stated parameter domain.

## Verification

Run `python check_threshold.py` in an environment with Python, SymPy and SciPy. The script independently implements the source's Laplace-form expression (Eq. (29)), symbolically checks equality with the rational partial-fraction formula and both derivatives, and checks positive unique roots, analytic bracketing and comparative-statics sample grids. These finite checks supplement rather than replace the all-parameter proof.

An exact calibration is \(\mu=1/2\), \(e^{-\alpha}=1/2\) (so \(\xi=1/4\)). Then the optimum is the unique positive root of
\[
48\nu^4+72\nu^3+19\nu^2-16\nu-6=0,
\]
namely \(\nu_*=0.462745752709\ldots\), with \(\Theta(\nu_*)=23.765935983469\ldots\). Changing only the recognition parameter to \(e^{-\alpha}=1/4\) gives \(\nu_*=0.505817407022\ldots\), as predicted by monotonicity. These are numerical evaluations of exact identities, not the basis for the global result.

## Relationship to prior work

Kroumi (2026) derives the full torus threshold, proves divergence as \(\nu\downarrow0\) and \(\nu\to\infty\), and concludes only that **at least one** interior minimum exists (Result 3 and Corollary D.5). The binary-case rational reduction above yields stronger, previously unspecified global strict convexity, uniqueness, a single algebraic characterization, bracketing, and the strictly increasing location of that optimum with both recognition strength and strategy mutation. Kroumi and Lessard (2015) study the unbounded lattice \(\mathbb Z^n\); their high-mutation conclusion is not the finite periodic high-mutation regime. Antal et al. (2009) also analyze unbounded phenotypes and do not state this finite two-tag optimization result. The reduction uses standard Laplace-transform and implicit-function techniques, which are not claimed as new.

## Limitations

The theorem is confined to the natural minimal nontrivial periodic phenotype space (two sites and one coordinate). No uniqueness claim is made for larger cycles, hypercubes of dimension greater than one, or finite population sizes. We do not infer a numerical real-world mutation optimum, or that phenotypic mutation should be manipulated. The evaluated literature may not exhaust older two-allele matching models; priority remains literature-bounded, and there has been no independent audit.

## References

1. D. Kroumi, *Phenotypic Assortment and the Evolution of Cooperation in Finite Periodic Phenotype Spaces*, arXiv:2608.21872v1 (first public 2026-08-22), https://arxiv.org/abs/2608.21872; Phys. Rev. E 114, 054406 (2026), DOI:10.1103/7pzd-gtdv. Source Eqs. (22), (24), (28), (29), Result 3, Appendix D.
2. D. Kroumi and S. Lessard, *Evolution of cooperation in a multidimensional phenotype space*, Theoretical Population Biology 102 (2015), 60–75, DOI:10.1016/j.tpb.2015.03.007.
3. T. Antal, H. Ohtsuki, J. Wakeley, P. D. Taylor and M. A. Nowak, *Evolution of cooperation by phenotypic similarity*, Proc. Natl. Acad. Sci. USA 106 (2009), 8597–8600, DOI:10.1073/pnas.0902528106.
4. D. Kroumi, *The evolution of cooperation under imperfect phenotypic recognition*, arXiv:2607.27570 (2026); unbounded phenotype-space comparison.
