# Rare one-point deletion sensitivity and a marked extreme-value law for circular spacings

## Finding
Let \(n\ge2\) points be independently uniform on a circle of circumference one. Let \(M_n\) be the largest clockwise gap before deletion and \(M'_n\) the largest gap after a uniformly chosen one of the \(n\) points is deleted. Put \(A_n=\{M'_n>M_n\}\) and \(H_j=\sum_{r=1}^j 1/r\). Then, at every finite \(n\ge2\),
\[
\Pr(A_n)=\frac{H_{n-1}}{n-1},\qquad
\mathbb E[n(M'_n-M_n)\mid A_n]=1-\frac{n-1}{nH_{n-1}}.
\]
Conditionally on \(A_n\), let \(U_n\) denote the proportion of the new merged gap lying clockwise between its initial endpoint and the deleted point. For \(n\to\infty\),
\[
\left(nM_n-\log n,\ n(M'_n-M_n),\ U_n\right)\mid A_n
\xrightarrow{\mathrm d}
\left(-\log G,\ E,\ U\right),
\]
where \(G\sim\operatorname{Gamma}(2,1)\), \(E\sim\operatorname{Exp}(1)\), and \(U\sim\operatorname{Unif}(0,1)\) are **mutually independent**. In particular \(\Pr(A_n)\sim(\log n)/n\), so a uniformly deleted point rarely changes the worst gap, but the change, conditional on occurring, is typically of order \(1/n\), and the pre-deletion extremum has a non-Gumbel conditional limit. The mark \(U_n\) is uniform and independent of the occurrence of \(A_n\) for every finite \(n\).

There is also an exact finite tail identity in exponential-spacing units. If \(D_1,\ldots,D_n\) are the cyclic gaps, let \(S=E_1+\cdots+E_n\) in the exponential representation \((D_i)\overset{d}= (E_i/S)\), where the \(E_i\) are independent unit exponentials. The random variable \(Y_n=S(M'_n-M_n)\), understood under this coupling, satisfies for every \(t\ge0\)
\[
\Pr(Y_n>t)=e^{-2t}\sum_{j=0}^{n-2}
(-1)^j\binom{n-2}{j}\frac{e^{-jt}}{(j+1)^2}.
\]
This identity is a statement about the coupled exponential variables, not an assertion that \(S\) is observable from the original points.

## Assumptions and scope
The circle has circumference one. Points are independent and uniform with probability-one distinct positions. Exactly one point is selected uniformly from the \(n\) points and removed, independently of its locations. Circular gaps include the wraparound gap. The physical maxima and increase have length units, while \(Y_n\) is measured in exponential-spacing units. The gamma parameterization uses shape two and rate one. The claim concerns a single random deletion, not optimal choice of a deletion, deletion of a prescribed nonuniform site, or a number of deletions that grows with \(n\).

## Proof
**Exponential representation.** Rotation invariance and exchangeability permit labeling the chosen vertex so that its incident clockwise gaps are \(D_1,D_2\). For independent \(E_i\sim\operatorname{Exp}(1)\), put \(S=\sum_iE_i\), \(T=E_1+E_2\), \(R=\max(E_1,E_2)\), and \(Z=\max_{3\le i\le n}E_i\), with \(Z=0\) at \(n=2\). The two physical maxima are \(M_n=\max(R,Z)/S\) and \(M'_n=\max(T,Z)/S\). Because \(T>R\) almost surely, \(A_n=\{T>Z\}\), and \(Y_n=(T-\max(R,Z))_+\).

**Exact probability and tail.** The sum \(T\) has density \(te^{-t}\) on \((0,\infty)\), independently of \(Z\), with \(\Pr(Z<t)=(1-e^{-t})^{n-2}\). Therefore
\[
\Pr(A_n)=\int_0^\infty te^{-t}(1-e^{-t})^{n-2}\,dt
=\int_0^1(-\log u)(1-u)^{n-2}\,du
=\frac{H_{n-1}}{n-1}.
\]
For any \(t\ge0\), \(Y_n>t\) is equivalent to \(E_1>t\), \(E_2>t\), and \(E_1+E_2>Z+t\). By the exponential memoryless property, shift \(E_1,E_2\) downward by \(t\), paying the factor \(e^{-2t}\); the shifted sum is an independent \(\operatorname{Gamma}(2,1)\) variable \(V\). Thus
\[
\Pr(Y_n>t)=e^{-2t}\mathbb E[(1-e^{-t-V})^{n-2}]
=e^{-2t}\sum_{j=0}^{n-2}(-1)^j\binom{n-2}{j}
\frac{e^{-jt}}{(j+1)^2}.
\]
The post-deletion points are an independent uniform sample of size \(n-1\). Using \(\mathbb E M_k=H_k/k\), we get \(\mathbb E[n(M'_n-M_n)]=nH_{n-1}/(n-1)-H_n\). Since the difference is zero outside \(A_n\), division by the exact probability gives the claimed conditional mean.

**Conditional rare-event law.** Let \(m=n-2\) and \(W=T-Z\). Under \(A_n\), the joint density of \((X_n,W)=(Z-\log n,T-Z)\) at \((x,w)\in\mathbb R\times(0,\infty)\) is
\[
\frac{(n-2)e^{-z}(1-e^{-z})^{n-3}(z+w)e^{-z-w}}{H_{n-1}/(n-1)},
\qquad z=\log n+x>0.
\]
Pointwise, this converges to \(e^{-2x-e^{-x}}e^{-w}\). Its integral over \(x\in\mathbb R,w>0\) is one, because \(e^{-2x-e^{-x}}\) is the density of \(-\log\operatorname{Gamma}(2,1)\). Since these are nonnegative probability densities, Scheffé's lemma gives convergence in total variation of the conditional two-dimensional distributions.

The split fraction \(U_n=E_1/T\) is exactly uniform on \((0,1)\) and independent of \((T,Z)\), by the independent exponential gamma--Dirichlet decomposition. It is consequently independent of \(A_n,X_n,W\). Furthermore \(\Pr(R>Z,A_n)\le2/(n-1)\), because \(\Pr(E_1>Z)=1/(n-1)\), and the same bound holds for \(E_2\). Hence \(\Pr(R>Z\mid A_n)\le2/H_{n-1}\to0\). On the complementary high-probability conditional event \(M_n=Z/S\) and \(M'_n-M_n=W/S\).

Finally, the exponential sum obeys the Chernoff bound \(\Pr(|S/n-1|>n^{-1/4})\le 2e^{-c\sqrt n}\) for some \(c>0\) and all sufficiently large \(n\). Dividing by \(\Pr(A_n)\asymp(\log n)/n\) shows that \(n/S=1+o_{\Pr(\cdot\mid A_n)}(1/\log n)\). The established conditional density limit gives \(Z=\log n+O_{\Pr(\cdot\mid A_n)}(1)\) and \(W=O_{\Pr(\cdot\mid A_n)}(1)\). Multiplication by \(n/S\) therefore changes the centered maximum and the increment by \(o_{\Pr(\cdot\mid A_n)}(1)\), proving the three-way joint limit.

## Verification
The optional script `verification.py` uses Python and `mpmath` to compare the beta-integral and binomial formulas for the finite change probability and tail, exact rational conditional-mean identities, and numerical finite-size approximations to the limiting density. Executing `python verification.py` produced 83 passing deterministic assertions. Numerical checks are finite sanity checks; the infinite claims follow from the density and concentration argument above. Install the listed dependency with `pip install -r requirements.txt` if necessary.

## Relationship to prior work
Schlemm (2014) establishes the ordinary maximal-spacing Gumbel law and explicit moments; Mijatović and Vysotsky (2015) establish maximal \(k\)-spacing limits based on sliding sums of exponentials. These concern unconditioned maxima over gaps or **all** candidate merged gaps. The present claim conditions on the exceptional event that a **uniformly selected single** deletion increases the old maximum, and identifies the resulting tilted maximum, overshoot, and location mark jointly. A related Bernoulli-thinning result for circular extremes studies deletion probabilities on the scale \(\varepsilon_n\log n\), which does not resolve this rare single-deletion conditional law. This comparison is about mathematical implication, not merely differing terminology.

## Limitations
The conditional limit is not a distribution-free statement for arbitrary nonuniform sampling on the physical circle. It makes no claim about deleting multiple points or choosing the most damaging point. The derivation uses standard beta, gamma, and extreme-value facts, and its novelty relative to all historical spacing/coverage literature cannot be certified by a finite search. Independent mathematical assessment has not been performed.

## References
- E. Schlemm, *Limiting distribution of the maximal distance between random points on a circle: a moments approach*, arXiv:1405.6114v1, first posted 23 May 2014, https://arxiv.org/abs/1405.6114.
- A. Mijatović and V. Vysotsky, *On the weak limit law of the maximal uniform k-spacing*, arXiv:1508.00944v1, first posted 5 August 2015, https://arxiv.org/abs/1508.00944.
- R. Pyke, *Spacings*, J. Roy. Statist. Soc. B 27 (1965), 395–449 (background for the normalized exponential representation).
