# An all-core optimum for parallel Haar-subspace simplex gradients

## Finding

For each ambient dimension \(d\ge 2\), core count \(c\ge 1\), and subspace dimension \(1\le p\le d\), consider the exact expected *linear-model* descent score of the Haar-random model-based simplex-gradient step introduced by Hare, Roberts and Royer. Let
\[
B(p)=\frac{\Gamma((p+1)/2)}{\Gamma(p/2)},\qquad C_d=\frac{\Gamma(d/2)}{\Gamma((d+1)/2)}.
\]
Under their parallel evaluation-round cost model, including their more favorable one-dimensional opportunistic cost, the normalized score is
\[
S_{d,c}(p)=C_d B(p)\begin{cases}
2/3,&p=1,\\[2pt]
1/(\lceil p/c\rceil+1),&2\le p\le d.
\end{cases}
\]
The complete set of maximizers, for all integer parameters without upper bounds, is
\[
\operatorname{argmax}_{1\le p\le d}S_{d,c}(p)=
\begin{cases}
\{1\},&c=1,\\
\{2,4\},&c=2\ \text{and}\ d\ge4,\\
\{\min(c,d)\},&\text{otherwise}.
\end{cases}
\]
In particular, with at least two cores the smallest subspace using all available cores is optimal (or the full space if smaller), and the only nonuniqueness occurs at two cores and four available dimensions.

## Assumptions and scope

The score is the *expected local linear decrease* for a unit gradient direction distributed uniformly on the sphere and a uniformly Haar-distributed \(p\)-dimensional subspace, as derived in the cited primary paper. The cost model counts \(\lceil p/c\rceil\) parallel rounds for forming a simplex gradient, followed by one sequential evaluation; for \(p=1\), the paper shows that evaluating the final point only when needed instead gives mean cost \(3/2\). All cores are identical, evaluations have equal duration, and communication, scheduling, interpolation algebra and nonlinearity costs are excluded. No claim about actual wall-clock runtime on hardware or the global convergence rate for nonlinear objectives is made.

The classification applies to every pair of positive integers \(c\ge1\), \(d\ge2\), with \(p\) taking all integers from one through \(d\). The factor \(C_d>0\) is independent of \(p,c\) and therefore does not influence the maximizing subspace dimension.

## Proof

Set \(B(s)=\Gamma((s+1)/2)/\Gamma(s/2)\) for real \(s>0\). Its logarithmic derivative is strictly positive and has the integral representation
\[
L(s):=\frac{d}{ds}\log B(s)
=\frac12\left[\psi\left(\frac{s+1}{2}\right)-\psi\left(\frac{s}{2}\right)\right]
=\int_0^\infty\frac{e^{-su}}{1+e^{-u}}\,du>0,
\]
where \(\psi\) is the digamma function. For \(s>1\), the pointwise inequality \(1/(1+e^{-u})<e^u/2\) for \(u>0\) implies
\[
0<L(s)<\frac1{2(s-1)}.
\]
The Gamma recurrence also gives the exact two-step identity
\[
B(s+2)=\frac{s+1}{s}B(s).
\]

Fix \(c\ge1\) and put \(H_c(s)=B(s)/(s+c)\). Whenever \(s\ge c+2\),
\[
\frac{d}{ds}\log H_c(s)
=L(s)-\frac1{s+c}
<\frac1{2(s-1)}-\frac1{s+c}\le0.
\]
Thus \(H_c\) is strictly decreasing on \([c+2,\infty)\). The Gamma recurrence shows a second, *exact* identity,
\[
H_c(c+2)=\frac{B(c+2)}{2c+2}
=\frac{B(c)}{2c}=H_c(c).
\]

First suppose \(c\ge2\) and \(d\ge c\). For \(2\le p\le c\), the evaluation cost is two rounds and the strict increase of \(B\) gives \(B(p)/2\le B(c)/2\), with equality only at \(p=c\). For \(p>c\), set \(k=\lceil p/c\rceil\ge2\). Then \(p\le kc\) and \(kc\ge c+2\), hence
\[
\frac{B(p)}{k+1}
\le\frac{B(kc)}{k+1}
=cH_c(kc)
\le cH_c(c+2)=\frac{B(c)}2.
\]
The first inequality is strict unless \(p=kc\); the second is strict unless \(kc=c+2\). The latter equation with integers \(k\ge2,c\ge2\) has the unique solution \((k,c)=(2,2)\), which gives the exceptional tie \(p=4\). When \(c>d\), all \(2\le p\le d\) cost two rounds and the strictly increasing \(B(p)\) makes \(p=d\) uniquely best among them. These arguments establish the assertion for \(p\ge2\) when \(c\ge2\).

For \(c\ge2\), the more favorable one-dimensional score is still smaller than the score at \(p=2\), because
\[
\frac23 B(1)=\frac2{3\sqrt\pi}
<\frac{\sqrt\pi}{4}=\frac12B(2)
\]
by \(3\pi>8\). Since \(p=2\) is always admissible, this also excludes \(p=1\).

Finally suppose \(c=1\). For every integer \(p\ge3\), strict decrease of \(H_1\) on \([3,\infty)\) gives
\[
\frac{B(p)}{p+1}\le H_1(3)=\frac1{2\sqrt\pi}
< H_1(2)=\frac{\sqrt\pi}{6}
<\frac23 B(1)=\frac2{3\sqrt\pi}.
\]
The last two strict comparisons use \(3<\pi<4\). Thus \(p=1\) uniquely maximizes the score for \(c=1\). All possibilities are exhausted.

## Verification

The standalone program `verify_parallel_haar.py` evaluates the stated score by log-Gamma arithmetic, compares all allowed dimensions \(2\le d\le119\) and all core counts \(1\le c\le64\), and tests the exact tie and Gamma-ratio inequalities. It is a supplementary finite test, **not** an exhaustive proof over all integers. The integral inequality and Gamma recurrence above provide the complete infinite proof.

Run `python3 verify_parallel_haar.py` with the Python standard library. The program has no data files or nonstandard software dependencies.

## Relationship to prior work

Hare, Roberts and Royer (first public preprint 2023-08-09, Theorem 4.2 and Section 4.2) derive the precise expected-decrease Gamma quotient and the parallel-round cost model. In the parallel model-based case they report numerical optimality of \(p=c\) only for \(c\le256\) and integer multiples \(p\le100c\), and explicitly note the \(c=2\), \(p=2,4\) tie. Those formulas, the cost model and the tie are **prior results, not claimed as new here**. The contribution is an all-integer analytic proof together with exclusion of nonmultiples and a complete characterization of maximizers when \(d<c\) or \(c=1\).

Roberts and Royer (2022) give general probabilistic convergence theory for randomized direct search. Kozak et al. (2020/2021) study randomized subspace descent and convergence using directional derivatives; neither of the inspected analyses establishes this model-based parallel-round optimizer. A publisher-hosted final version of the first paper was identified bibliographically but its complete text could not be inspected; any later proof of the same scheduling claim would eliminate priority.

## Limitations

This optimizes the published *idealized local expected-decrease / synchronous-round* metric, not the total number of iterations or true elapsed time of a finite-precision optimizer. In particular the model neglects the variable expense of forming and solving subspace models and any unequal evaluation times. The result is an analytic completion of a specific previously numerically supported subspace-size rule; it does not invent a new derivative-free algorithm. Published equivalent formulations in uninspected later revisions remain an originality risk. The proof does not imply that larger subspaces never help on nonlinear objectives.

## References

1. W. Hare, L. Roberts, C. W. Royer, *Expected decrease for derivative-free algorithms using random subspaces*, arXiv:2308.04734, first posted 2023-08-09, Theorem 4.2 and Section 4.2, https://arxiv.org/abs/2308.04734. Journal version: *Mathematics of Computation* **94** (2025), 277–304, DOI:10.1090/mcom/4011 (published electronically 2024-08-23).
2. L. Roberts, C. W. Royer, *Direct search based on probabilistic descent in reduced spaces*, arXiv:2204.01275, first posted 2022-04-04, https://arxiv.org/abs/2204.01275.
3. D. Kozak, S. Becker, A. Doostan, L. Tenorio, *A stochastic subspace approach to gradient-free optimization in high dimensions*, arXiv:2003.02684, first posted 2020-03-05, https://arxiv.org/abs/2003.02684.
