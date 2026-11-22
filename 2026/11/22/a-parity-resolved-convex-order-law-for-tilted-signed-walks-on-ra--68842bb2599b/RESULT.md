# A parity-resolved convex-order law for tilted signed walks on random regular graphs

## Finding
Fix an integer \(d\geq3\), a sign probability \(p\in(0,1)\) and a tilt \(\beta>0\). Independently sign the edges of a uniform simple \(d\)-regular graph on \(n\) labelled vertices, each edge being positive with probability \(p\). Set the signed strength \(s(v)=\sum_{e\ni v}\sigma_e\). Select a starting vertex with conditional probabilities proportional to \(e^{-\beta s(v)}\), and run an independent ordinary nearest-neighbour simple random walk \((X_k)\). Write \(S_{n,k}=s(X_k)\). Along all \(n\to\infty\) with \(nd\) even, for every fixed \(m\geq1\), the conditional laws of \(S_{n,2m-1}\) and \(S_{n,2m}\), given the signed graph, converge in probability to the laws \(O_m\) and \(E_m\) below.

Put \(q=p e^{-\beta}/[p e^{-\beta}+(1-p)e^{\beta}]\), so \(0<q<p<1\), and let \(B_j(r)\) denote a binomial variable with law \(\operatorname{Bin}(j,r)\), with independent components where added. Define three integer-valued laws, all supported on \(\{-d,-d+2,\ldots,d\}\):
\[
A_0=\mathcal L(2B_d(q)-d),\qquad
A_1=\mathcal L(2[B_1(q)+B_{d-1}(p)]-d),\qquad
A_\infty=\mathcal L(2B_d(p)-d).
\]
Let \(u_m\) be the \(2m\)-step return probability of ordinary simple random walk on the infinite \(d\)-regular tree. Then the two laws are explicitly
\[
\boxed{O_m=d u_m A_1+(1-d u_m)A_\infty,\qquad
E_m=u_m A_0+(1-u_m)A_\infty.}
\]
Here linear combinations denote mixtures, not sums of random variables. The return probabilities have the generating function
\[
\boxed{\sum_{m\ge0}u_m z^m
=\frac{2(d-1)}{d-2+d\sqrt{1-4(d-1)z/d^2}},\quad u_0=1.}
\]
In particular, \(d u_m\leq1\) for \(m\ge1\). The two consecutive-time limits have identical expectations, yet a strict convex-order separation:
\[
\boxed{\mathbb E O_m=\mathbb E E_m=d(2p-1)+2d u_m(q-p),\qquad
O_m\ <_{\rm cx}\ E_m,}
\]
where strictness means \(\mathbb E\phi(O_m)<\mathbb E\phi(E_m)\) for every strictly convex real function \(\phi\) (the variables are bounded). Consequently neither law first-order stochastically dominates the other. The precise variance gap is
\[
\boxed{\operatorname{Var}(E_m)-\operatorname{Var}(O_m)
=4d(d-1)u_m(p-q)^2>0.}
\]
The gap decays, as \(m\to\infty\) after the graph-size limit, according to
\[
\boxed{\operatorname{Var}(E_m)-\operatorname{Var}(O_m)
\sim\frac{4d^2(d-1)^2(p-q)^2}{\sqrt\pi(d-2)^2}
\left(\frac{4(d-1)}{d^2}\right)^m m^{-3/2}.}
\]
All assertions are about fixed walk time followed, if specified, by a separate large-time limit; no uniform joint limit with \(m=m(n)\) is claimed.

As a concrete pair, take \(d=3\), \(p=3/4\), and \(\beta=\tfrac12\log3\), so \(q=1/2\). At times one and two the limiting score probabilities at values \((-3,-1,1,3)\) are respectively \((3,21,45,27)/96\) and \((5,21,39,31)/96\). Both have mean \(1\), but the variance rises from \(5/2\) to \(3\); their cumulative distribution functions cross.

## Assumptions and scope
The finite graphs are uniformly random simple labelled \(d\)-regular graphs; their \(\pm1\) edge signs are independent, each positive with probability \(p\). The walker does not use edge signs in its transitions. The tilt is applied only to the start. All conditional distributions integrate out the random walk while holding the finite signed graph fixed. The subsequent probability limit refers to randomness in that graph. The parameters \(d,p,\beta\) are fixed, with \(d\ge3\), \(p\in(0,1)\), \(\beta>0\), and \(m\ge1\). At the boundary \(\beta=0\), or at \(p\in\{0,1\}\), the two laws coincide; strictness is not asserted there. No statement is made for graph order or time outside the indicated quantifiers.

## Proof
**1. Local weak convergence and the tilt.** At every fixed radius, a uniform root of a random \(d\)-regular graph has the infinite \(d\)-regular tree as its local limit, and independent edge signs persist in the marked local limit. Bounded-radius weighted neighborhood averages concentrate: in a fixed-degree graph only \(O(n)\) ordered pairs of root neighborhoods overlap, so the variance of any bounded local sample average is \(O(1/n)\). The random normalizing denominator \(n^{-1}\sum_v e^{-\beta s(v)}\) converges in probability to \([p e^{-\beta}+(1-p)e^{\beta}]^d>0\). Therefore weighting a root by \(e^{-\beta s}\) yields the tilted marked tree, uniformly for each fixed walk horizon. Under this tilt, each of the \(d\) root-incident signs becomes independently positive with probability \(q\), while every other edge sign retains its original independent \(p\)-biased law. Walk transitions depend only on the unsigned tree.

**2. Three possible score laws.** If the walk is at the root, its vertex score has law \(A_0\). If it is one edge from the root, its score involves exactly one tilted sign (the shared root edge) and \(d-1\) independent signs with positive probability \(p\), giving \(A_1\). At distance at least two, no incident edge touches the root, and its score has law \(A_\infty\). Hence the time-\(k\) score law is a three-component mixture determined only by the radial walk probabilities.

**3. Pairing the two parities.** Bipartiteness of the tree implies that the walk at time \(2m\) can be at the root but cannot be at distance one, while at time \(2m-1\) it can be at distance one but not at the root. Every neighbor of the root has transition probability \(1/d\) to the root, so
\[\Pr(R_{2m}=0)=\frac1d\Pr(R_{2m-1}=1)=u_m.\]
Substitution gives the two displayed mixture laws and \(d u_m\le1\). The expectations of \(A_0,A_1,A_\infty\) are \(d(2q-1)\), \(2q-1+(d-1)(2p-1)\), and \(d(2p-1)\), respectively, proving the paired mean identity.

**4. Convex order and strictness.** For \(0\le j\le d\), let \(H_j\) be the sum of \(j\) independent \(\pm1\) signs with positive probability \(q\) and \(d-j\) signs with positive probability \(p\), and write \(h(j)=\mathbb E\phi(H_j)\) for convex \(\phi\). Replacing two \(p\)-biased signs in succession by \(q\)-biased signs shows that
\[
h(j+2)-2h(j+1)+h(j)=(q-p)^2\,\mathbb E[\phi(W+2)-2\phi(W)+\phi(W-2)]\ge0,
\]
where \(W\) is the sum of the other \(d-2\) signs. (The same formula applies after averaging over their appropriate mixture of \(q\)-biased and \(p\)-biased laws.) Thus \(h\) is convex on \(\{0,\ldots,d\}\), and
\[
\mathbb E\phi(A_1)=h(1)\le\frac1d h(d)+\frac{d-1}{d}h(0)
=\frac1d\mathbb E\phi(A_0)+\frac{d-1}{d}\mathbb E\phi(A_\infty).
\]
Since \(d u_m>0\), the mixture identities yield \(O_m\le_{\rm cx}E_m\). For strictly convex \(\phi\) and \(q\ne p\) every discrete second difference above is positive; the convex-order inequality is strict. The two laws have equal finite means and distinct second moments, so neither can first-order stochastically dominate the other.

**5. Exact variance.** Write \(a=2p-1\), \(b=2q-1\). The uncentered second moments of \(A_\infty,A_1,A_0\) are respectively \(d+d(d-1)a^2\), \(d+(d-1)(d-2)a^2+2(d-1)ab\), and \(d+d(d-1)b^2\). Their combination \(\mathbb E E_m^2-\mathbb E O_m^2=u_m d(d-1)(a-b)^2=4u_m d(d-1)(p-q)^2\). Subtracting the common squared mean proves the variance gap.

**6. Return law and asymptotics.** A first-return excursion of length \(2j\) from the root has probability \(C_{j-1}(d-1)^{j-1}/d^{2j-1}\), where \(C_{j-1}\) is the Catalan number. Summing excursions gives the first-return generating function \(F(z)=\frac{d}{2(d-1)}[1-\sqrt{1-4(d-1)z/d^2}]\) and the renewal formula \(U(z)=1/(1-F(z))\), yielding the displayed \(U\). For \(d\ge3\), its leading square-root singularity at \(z=d^2/[4(d-1)]\) gives
\[
u_m\sim\frac{d(d-1)}{\sqrt\pi(d-2)^2}
\left(\frac{4(d-1)}{d^2}\right)^m m^{-3/2}.
\]
Multiplying by the exact variance factor proves the final asymptotic.

## Verification
The self-contained Python 3 script `checker.py` performs 5,400 exact-rational assertions, independently evaluating radial transition probabilities and a Catalan renewal recurrence; full signed-score convolution and mixture probabilities; identical paired means; exact variance differences; all lattice hinge inequalities defining convex order; and crossing of cumulative distribution functions for \(d=3,\ldots,8\), several distinct rational underlying and tilted sign probabilities, and \(m=1,\ldots,9\). Run `python3 checker.py`. These finite tests are diagnostics, not substitutes for the proof of all sizes and all positive tilts.

## Relationship to prior work
Louvaris and Trevezas, arXiv:2611.17118 (first posted 2026-11-12), characterize universal signed-score sampling biases and prove stochastic dominance relative to the initial time. Their Example 1 gives an explicit *one-step conditional-mean-bias* distribution for signed random regular graphs, while their text expressly does not claim comparisons between successive walk times. The present result concerns the **score distribution of the actual random walk** and shows consecutive-time *equal means but strict convex order and first-order stochastic incomparability*, together with complete laws and an exact decay profile. It uses the same tilted-root model and elementary local convergence but requires the extra radial parity analysis and convex-order argument. Hazra, den Hollander and Parvaneh, arXiv:2502.17724 (first posted 2025-02-24), study multi-level empirical *degree friendship biases* via backtracking/nonbacktracking exploration, without these independently signed vertex-score marginals. Standard Catalan return laws on homogeneous trees and discrete convexity are used as known ingredients; no novelty is attributed to those stand-alone identities.

## Limitations
The established result concerns a simple discrete-time walk with independent biased signs, a fixed exponential starting tilt, fixed degree at least three, fixed sign bias, and fixed time before taking the graph-order limit. It does not establish uniform-in-time finite-graph error bounds, a mixing-time law, or the analogous convex-order phenomenon for correlated signs or other initial weighting rules. The scientific priority check is based on the identified published sources and targeted research searches, not an exhaustive proof of historical originality. Independent assessment has not been performed.

## References
1. M. Louvaris and S. Trevezas, *Universal sampling rules for the signed friendship paradox*, arXiv:2611.17118v1 (2026-11-12), https://arxiv.org/html/2611.17118v1 .
2. R. S. Hazra, F. den Hollander and A. Parvaneh, *The multi-level friendship paradox for sparse random graphs*, arXiv:2502.17724 (2025-02-24), https://arxiv.org/pdf/2502.17724 .
3. R. S. Hazra, F. den Hollander and A. Parvaneh, *The friendship paradox for sparse random graphs*, arXiv:2312.15105 (2023-12-22), https://arxiv.org/abs/2312.15105 .
