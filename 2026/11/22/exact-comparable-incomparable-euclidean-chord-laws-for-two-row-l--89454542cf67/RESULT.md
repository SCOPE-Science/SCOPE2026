# Exact comparable–incomparable Euclidean chord laws for two-row ladder order polytopes

## Finding
For every integer \(n\ge2\), let \(P_n=[2]\times[n]\) and let \(\mathcal O_n\subset\mathbb R^{2n}\) be its standard Euclidean order polytope. Write \(D(v,w)=\|v-w\|_2^2\) for a pair of vertices, and call the vertices *comparable* when their underlying upper sets are nested under inclusion. Put
\[
 B_n(j)=\begin{cases}\binom{n-j+2}{2},&0\le j\le n,\\0,&\text{otherwise}.\end{cases}
\]
For every integer \(1\le k\le2n\), the numbers of unordered distinct vertex pairs at squared Euclidean distance \(k\), split by inclusion type, are
\[
\boxed{C_{n,k}=2B_n(k)+\sum_{u=1}^{k-1}B_n(\max\{u,k-u\}),\qquad I_{n,k}=(k-1)B_n(k).}
\]
There are exactly \(N_n=\binom{n+2}{2}\) vertices and \(\binom{n+2}{4}\) incomparable vertex pairs. Consequently, among all distinct pairs, the probability of incomparability is exactly \((n-1)/(3(n+3))\), tending to \(1/3\).

If \(D_n\) is squared Euclidean distance conditioned on the pair being incomparable, then
\[
\boxed{D_n-2\ \stackrel{\mathrm d}=\ \operatorname{BetaBinomial}(n-2;2,3),\quad\mathbb E D_n=\frac{2n+6}{5},\quad\operatorname{Var}(D_n)=\frac{(n-2)(n+3)}{25}.}
\]
Here \(\operatorname{BetaBinomial}(m;\alpha,\beta)\) means sampling \(T\sim\operatorname{Beta}(\alpha,\beta)\) and then \(X\mid T\sim\operatorname{Binomial}(m,T)\). In particular, \(D_n/n\) conditioned on incomparability converges in distribution to \(\operatorname{Beta}(2,3)\).

For a uniformly chosen unordered *distinct* pair without any comparison condition, \(D_n/n\) has the limiting density
\[
\boxed{f(t)=\begin{cases}\frac{t(19t^2-42t+24)}3,&0<t<1,\\\frac{(2-t)^3}3,&1<t<2,\\0,&\text{otherwise}.\end{cases}}
\]
Conditioned on comparability, the limiting density is instead
\[
\boxed{f_C(t)=\begin{cases}4[(1-t/2)^3-(1-t)^3],&0<t<1,\\(2-t)^3/2,&1<t<2,\\0,&\text{otherwise}.\end{cases}}
\]
Thus comparable pairs retain a positive asymptotic probability \(1/8\) of squared distance exceeding \(n\), while incomparable pairs never exceed \(n\). The conditional asymptotic means are \(3/5\) and \(2/5\), respectively, in units of \(n\); the unconditional mean tends to \(8/15\).

## Assumptions and scope
The poset has elements \(A_1,\ldots,A_n,B_1,\ldots,B_n\), with \(A_i\prec A_{i+1}\), \(B_i\prec B_{i+1}\), \(A_i\prec B_i\), and transitive closure. The order polytope consists of all vectors \((x,y)\in[0,1]^{2n}\) satisfying \(x_i\le x_{i+1}\), \(y_i\le y_{i+1}\), and \(x_i\le y_i\) wherever defined. Its vertices are the upper-set indicator vectors. No affine rescaling is allowed: squared Euclidean distance is computed directly in these \(2n\) coordinates. Comparability is inclusion of the two upper sets, not adjacency in the polytope graph. All finite formulas count unordered *distinct* vertex pairs. The conditional laws are defined because \(n\ge2\), when incomparable pairs exist.

## Proof
**Vertex coordinates and metric.** Each vertex is uniquely encoded by two integer cutoffs \(0\le a\le b\le n\): choose the upper-tail indicator of \(\{a+1,\ldots,n\}\) in the \(B\)-row and \(\{b+1,\ldots,n\}\) in the \(A\)-row. This satisfies \(x_i\le y_i\), and every binary order-preserving assignment has this form. In particular, there are \(\sum_{b=0}^n(b+1)=\binom{n+2}{2}\) vertices. For vertices with cutoffs \((a,b)\) and \((c,d)\), the squared Euclidean distance is precisely
\[
D=|a-c|+|b-d|.
\]
Their upper sets are incomparable exactly when \((a-c)(b-d)<0\).

**Shift count.** For an ordered pair, put \(u=c-a\), \(v=d-b\), and \(k=|u|+|v|\). The three nonnegative gap coordinates of the first vertex are \(g_1=a\), \(g_2=b-a\), and \(g_3=n-b\), which sum to \(n\). Under the displacement \((u,v)\), they change by \((u,v-u,-v)\). Both vertices lie in the triangular cutoff domain precisely when \(g_i\) exceeds each of the three respective necessary lower bounds. Their sum equals
\[
L(u,v)=\frac{|u|+|v-u|+|v|}{2}=\max\{|u|,|v|,|u-v|\}.
\]
By stars and bars, there are exactly \(\binom{n-L(u,v)+2}{2}\) ordered starting vertices for each displacement, with value zero when \(L(u,v)>n\).

**Comparison classes.** For a displacement with \(u,v\) of opposite strict signs, \(L=k\), and there are exactly \(2(k-1)\) such signed displacements; dividing the resulting ordered count by two gives \(I_{n,k}=(k-1)B_n(k)\). When both signs are the same and nonzero, take \(|u|=j\), \(|v|=k-j\), with \(1\le j<k\). Their common magnitude is \(\max(j,k-j)\), yielding \(\sum_{j=1}^{k-1}B_n(\max(j,k-j))\) unordered pairs. The four axis displacements together give \(2B_n(k)\) unordered comparable pairs. These are exhaustive disjoint displacement types, proving the boxed joint spectrum, including the range beyond \(k=n\).

**Exact conditional law.** Vandermonde's convolution gives
\[
\sum_{k=2}^{n}(k-1)\binom{n-k+2}{2}=\binom{n+2}{4}.
\]
Set \(j=k-2\) and \(m=n-2\). Dividing the incomparable coefficient by this total gives
\[
\mathbb P(D_n-2=j\mid\mathrm{incomparable})
=\frac{12(j+1)(m-j+1)(m-j+2)}{(m+1)(m+2)(m+3)(m+4)},\quad0\le j\le m,
\]
which equals the beta-binomial mixture probability \(\binom mj B(j+2,m-j+3)/B(2,3)\). Its moments follow from total expectation and total variance for the conditional binomial sample: \(\mathbb E(D_n-2)=2m/5\) and \(\operatorname{Var}(D_n-2)=m(m+5)/25\). The mixture construction with the conditional law of large numbers yields the \(\operatorname{Beta}(2,3)\) scaling limit.

**All-pairs limit and comparable limit.** In the exact formula for \(C_{n,k}\), take \(k/n\to t\in(0,2)\). The summand is \(\tfrac12 n^2(1-\max\{x,t-x\})_+^2+O(n)\) for \(x=j/n\), uniformly away from harmless breakpoints. Since the number of unordered distinct vertex pairs is asymptotic to \(n^4/8\), the coefficient-to-density limit from comparable pairs is
\[
\frac83\left[(1-t/2)^3-(1-t)_+^3\right],\qquad0<t<2,
\]
where \((z)_+=\max(z,0)\). The corresponding incomparable unconditional density is \(4t(1-t)^2\) for \(0<t<1\) and zero otherwise. Adding yields \(f\). Since the limiting comparable-pair probability is \(2/3\), dividing its unconditional density by \(2/3\) gives \(f_C\). These continuous densities integrate to one after their respective normalizations; the exact finite support is bounded by \(2n\), so the Riemann-sum convergence of distribution functions follows. Direct integration gives the conditional means, the unconditional \(8/15\), and the comparable tail probability \(\int_1^2(2-t)^3/2\,dt=1/8\).

## Verification
The accompanying standalone `verify.py` uses exact integer enumeration of all cutoff pairs and independently checks the complete comparable/incomparable distance histogram for every \(2\le n\le18\). It tests the exact number of incomparable pairs, conditional beta-binomial mean and variance, and the stable high-distance coefficients. Symbolic integration additionally verifies the limiting densities and the unconditional first moment. Execute `python3 verify.py` with Python 3 and SymPy; the expected message is `LADDER_CHORD_JOINT_SPECTRUM_PASS`. The general statements are proved above rather than inferred from the finite checks.

## Relationship to prior work
Defant, Féray, Nadeau and Williams, *Wiener Indices of Minuscule Lattices* (arXiv:2304.06113, first public 2023-04-12), treat precisely the lattice of order ideals of rectangles and show that its Hasse-graph distance equals symmetric-difference cardinality, which here equals squared Euclidean vertex distance. Their Theorem 1.2 and Corollary 1.3 determine the **sum** of all distances for every rectangle. Their asymptotic distribution theorem treats rectangular side lengths both proportional to the growing parameter, leading to a Brownian-bridge-area law; it is not the fixed-two-row regime. Their distance identity and Wiener index are credited, not new. Neither their displayed moment generating formulas nor their proportional-growth limit states the full fixed-two-row histogram, its inclusion-comparability split, or the exact beta-binomial conditional law.

Von Bell and collaborators (arXiv:2102.11306, first public 2021-02-22) study generalized snake and ladder-poset triangulations, circuits and volume, but not the two-vertex Euclidean metric spectrum. Freij-Hollanti and Lundström (arXiv:2312.13890, first public 2023-12-21) compare order/chain-polytope face numbers, not vertex-pair distance frequencies. A separately published all-poset **second-moment** vertex-cloud comparison does not determine a full distribution or comparability conditioning. A prior caracol flow-polytope spectrum has a \(\operatorname{Beta}(2,3)\) scaling limit for an **unconditional** metric in a different coordinate realization; that classical beta law itself is not asserted as new here. The original content is the complete joint finite-distance census for the canonical ladder order-polytope vertices and its pair-type refinements.

## Limitations
This result concerns the canonical binary vertex embedding of one poset family, not uniform points in the interior or a general rectangle with both side lengths growing. It does not improve the known general-rectangle Wiener-index formula, which is only a first moment. The fixed-width setting is essential for the displayed beta-binomial shape. Historical priority remains provisional: an unindexed distributional theorem under lattice Hasse distance, partitions, symmetric difference or Young-diagram terminology could give an equivalent conclusion. Independent mathematical audit has not been performed.

## References
1. C. Defant, V. Féray, P. Nadeau and N. Williams, *Wiener Indices of Minuscule Lattices*, arXiv:2304.06113 (first posted 2023-04-12), especially Section 1.3, Theorem 1.2, and Section 7. https://arxiv.org/abs/2304.06113
2. M. von Bell, B. Braun, D. Hanely, K. Serhiyenko, J. Vega, A. R. Vindas-Meléndez and M. Yip, *Triangulations, order polytopes, and generalized snake posets*, arXiv:2102.11306 (first posted 2021-02-22), especially Sections 3 and 5. https://arxiv.org/abs/2102.11306
3. R. Freij-Hollanti and T. Lundström, *\(f\)-vector inequalities for order and chain polytopes*, arXiv:2312.13890 (first posted 2023-12-21). https://arxiv.org/abs/2312.13890
4. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23. https://doi.org/10.1007/BF02187680
