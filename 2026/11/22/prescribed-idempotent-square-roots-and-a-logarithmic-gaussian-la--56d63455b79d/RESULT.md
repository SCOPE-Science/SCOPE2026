# Prescribed idempotent square roots and a logarithmic Gaussian law in increasing partial injections

## Finding
For every integer \(n\ge0\), let \(P_n\) be the monoid of all injective order-preserving partial maps of \([n]=\{1,\ldots,n\}\), including the empty map. For each \(S=\{s_1<\cdots<s_k\}\subseteq[n]\), write \(e_S\) for its partial identity, put \(s_0=0\), \(s_{k+1}=n+1\), and define \(g_i=s_{i+1}-s_i-1\) for \(0\le i\le k\). Let
\[
T_m=\sum_{j=0}^{\lfloor m/2\rfloor}\frac{m!}{j!^2(m-2j)!}\qquad(m\ge0)
\]
be the central trinomial numbers. The **complete prescribed-idempotent square-root fiber** is
\[
\boxed{\#\{f\in P_n:f^2=e_S\}=\prod_{i=0}^{k}T_{g_i}.}
\]
In particular, these fibers depend on the *positions* of the fixed points, not just on their number: in \(P_5\), the partial identities on \(\{1\}\) and on \(\{3\}\) have respectively \(19\) and \(9\) square roots.

Let \(S_n\) be a uniformly chosen subset of \([n]\), and let \(H_n\) be the natural logarithm of the number of square roots of \(e_{S_n}\). Define the positive, absolutely convergent constants
\[
\begin{split}
\gamma&=\frac12\sum_{m\ge0}2^{-(m+1)}\log T_m,\\
\eta&=\frac12\sum_{m\ge0}2^{-(m+1)}\bigl(\log T_m-\gamma(m+1)\bigr)^2.
\end{split}
\]
Then \(\gamma=0.2529313782\ldots\), \(\eta=0.3041901353\ldots>0\), and
\[
\boxed{\frac{H_n-\gamma n}{\sqrt{\eta n}}\ \Longrightarrow\ \mathcal N(0,1).}
\]
Moreover, \(\mathbb E H_n=\gamma n+O(1)\) and \(\operatorname{Var}(H_n)=\eta n+O(1)\). By contrast, the *arithmetic* mean number of square roots per partial identity is asymptotic to
\[
\boxed{\mathbb E\,e^{H_n}\sim\frac1{\sqrt5}\left(\frac{1+\sqrt5}{2}\right)^n.}
\]
Thus typical prescribed root multiplicities grow exponentially on a strictly smaller exponential scale than their arithmetic mean. The scalar mean sequence and its asymptotic are previously recorded; the contributions assessed here are the semigroup fiber identification and the logarithmic limit law for uniformly sampled target idempotents.

## Assumptions and scope
Composition is ordinary partial-map composition, \(f^2(x)\) being defined only if \(x\in\operatorname{dom}(f)\) and \(f(x)\in\operatorname{dom}(f)\). Order-preserving means strict increase between distinct points in the domain, as the map is injective. Every \(e_S\) is an idempotent, and all idempotents of \(P_n\) have this form. The uniform target distribution is uniform among the \(2^n\) partial identities, **not** the distribution induced by a uniform choice of a square root. Both \(n=0\) and the empty target are included. The central limit and mean/variance assertions concern \(n\to\infty\).

## Proof
**1. Classification of roots.** Suppose \(f^2=e_S\). If \(s\in S\), then \(f^2(s)=s\). As \(f\) is strictly order-preserving, it cannot have a nontrivial 2-cycle: if \(f(s)=y>s\), then \(f(y)>f(s)=y>s\), while \(f^2(s)=s\), a contradiction; the case \(y<s\) is symmetric. Hence \(f(s)=s\). Conversely, if \(f(x)=x\), then \(f^2(x)=x\), so \(x\in S\). Thus the fixed points of \(f\) are exactly \(S\).

For \(x\in\operatorname{dom}(f)\setminus S\), let \(y=f(x)\). Necessarily \(y\notin\operatorname{dom}(f)\), or \(f^2(x)\) would be defined outside \(S\). In particular, the moving domain and moving image are disjoint. No moving arrow can touch a fixed point, by injectivity, or cross a fixed point \(s\): strict isotonicity together with \(f(s)=s\) precludes \(x<s<f(x)\) and \(f(x)<s<x\). Therefore every moving arrow lies within a single gap between consecutive prescribed fixed points.

Inside a gap of length \(m\), choose disjoint sets \(D,R\) of the same size \(j\), of moving-domain and moving-image points. There is exactly one order-preserving bijection \(D\to R\), and it is square-zero because \(D\cap R=\varnothing\). Conversely every square-zero increasing partial injection in the gap arises this way. The number of such choices is \(m!/(j!^2(m-2j)!)\), summed over \(0\le j\le\lfloor m/2\rfloor\). All gaps are independent; their product proves the exact fiber formula. In particular the root of every \(e_S\) exists (\(e_S\) itself).

**2. Enumerative control and previously tabulated totals.** The central trinomial generating function follows by a direct binomial series calculation:
\[
T(z):=\sum_{m\ge0}T_mz^m
=\sum_{j\ge0}\binom{2j}{j}\frac{z^{2j}}{(1-z)^{2j+1}}
=\frac1{\sqrt{1-2z-3z^2}}.
\]
For a prescribed number \(k\) of fixed points, summing the product formula over all gap compositions gives \(z^kT(z)^{k+1}\). Therefore
\[
\sum_{n\ge0}\sum_{S\subseteq[n]}u^{|S|}z^n\#\{f:f^2=e_S\}
=\frac{T(z)}{1-uzT(z)}
=\frac1{\sqrt{1-2z-3z^2}-uz}.
\]
This *numerical* coefficient triangle is already OEIS A111960 and its row-sum sequence is A111961; neither the triangle, the row sums, nor the row-sum exponential asymptotic are claimed as newly discovered. What the triangle alone does not give is the number attached to **each individual target** \(S\), or the distribution of the logarithm of that number under a uniformly sampled target.

At \(u=1\), the generating function has a unique dominant simple pole \(\rho=1/(1+\sqrt5)\), with principal part \(\frac1{\sqrt5}(1-z/\rho)^{-1}\). Its other singularities have strictly larger modulus (the nearest square-root branch point is \(1/3\)). Hence
\[
\sum_{S\subseteq[n]}\#\{f:f^2=e_S\}\sim\frac{(1+\sqrt5)^n}{\sqrt5}.
\]
Dividing by \(2^n\) proves the arithmetic-mean formula.

**3. Moment generating function for the uniform target.** For real or complex \(t\) near zero define
\[
B_t(z)=\sum_{m\ge0}T_m^t z^m,
\quad G(z,t)=\sum_{n\ge0}\Bigl(\sum_{S\subseteq[n]}e^{tH_n(S)}\Bigr)z^n
=\frac{B_t(z)}{1-zB_t(z)}.
\]
Here \(H_n(S)=\sum_{i=0}^{|S|}\log T_{g_i}\). Since \(T_m\le3^m\), the series \(B_t(z)\) is analytic in a disk of radius exceeding \(1/2\) for all complex \(t\) sufficiently near zero. At \(t=0\), \(B_0(z)=1/(1-z)\), so \(G(z,0)=1/(1-2z)\). The equation \(\rho(t)B_t(\rho(t))=1\) therefore has a unique analytic solution near \((t,z)=(0,1/2)\), with a simple pole of \(G\) at \(z=\rho(t)\). Analytic perturbation of the simple pole and a slightly larger common coefficient contour show uniformly for small complex \(t\) that
\[
\mathbb E[e^{tH_n}]=C(t)\left(\frac{\rho(0)}{\rho(t)}\right)^n(1+O(\theta^n)),
\]
where \(C(t)\) is nonzero and analytic near zero, \(C(0)=1\), and \(0<\theta<1\) is independent of sufficiently small \(t\). This follows directly from the residue at the simple pole; the remaining analytic coefficient integral is exponentially smaller.

Write \(h(t)=\log(\rho(0)/\rho(t))\). Set \(p_m=2^{-(m+1)}\), \(L_m=m+1\) and \(X_m=\log T_m\). The defining equation for \(\rho(t)\) is exactly
\[
\sum_{m\ge0}p_m\exp\bigl(tX_m-h(t)L_m\bigr)=1.
\]
At \(t=0\), this is a probability distribution with \(\sum p_m L_m=2\). Differentiate once to obtain \(h'(0)=\sum p_mX_m/2=\gamma\). Differentiate twice, using the first derivative identity, to obtain
\[
h''(0)=\frac12\sum_{m\ge0}p_m\bigl(X_m-\gamma L_m\bigr)^2=\eta.
\]
Both sums converge absolutely as \(0\le X_m\le m\log3\). Positivity of \(\eta\) follows because \(X_0=0\) but \(X_2=\log3>0\), so \(X_m\) is not proportional to \(L_m\).

The uniform analytic moment-generating-function expansion now gives \(\mathbb E H_n=nh'(0)+O(1)\) and \(\operatorname{Var}(H_n)=nh''(0)+O(1)\). For the centered variable, evaluate the expansion at \(t=s/\sqrt{\eta n}\) and use \(h(t)=\gamma t+\eta t^2/2+O(t^3)\). The moment-generating functions converge locally to \(e^{s^2/2}\), proving the claimed Gaussian limit.

**4. Difference between typical and mean multiplicity.** The two numerical rates \(\gamma=0.252931\ldots\) and \(\log((1+\sqrt5)/2)=0.481211\ldots\) are strictly different. They may also be separated with certified truncation: for every \(N\ge0\), \(0\le\gamma-\sum_{m=0}^N2^{-(m+2)}\log T_m\le (N+2)2^{-(N+2)}\log3\). Thus the displayed decimal values and strict inequality follow without relying on experiments. The preceding Gaussian law says a typical target has \(\log\#\{f:f^2=e_S\}=\gamma n+O_{\mathbb P}(\sqrt n)\), whereas the previously tabulated arithmetic mean has the greater exponential rate.

## Verification
The standalone standard-library program `verify.py` lists every increasing partial injection on \([n]\) for \(0\le n\le9\) **without** using the gap parametrization. It directly composes each map with itself, tests idempotence, records its actual square, and matches every individual fiber with the proposed product of central trinomial numbers. It separately calculates the coefficients of \(T(z)^{k+1}\), and matches the counts. Across the checked dimensions, the largest input monoid has \(\binom{18}{9}=48620\) elements and \(512\) target idempotents. A separate differentiation recurrence computes finite-size cumulants of \(H_n\) for dimensions \(30,60,100\), checking their approach to the analytic constants. Its captured output ends with `VERIFY_OK` and `ENTROPY_RECURSION_OK`. Finite checks do **not** prove the formulas or the asymptotic law; those follow from the arguments above.

## Relationship to prior work
Fernandes and Quinteiro (first arXiv posting February 21, 2015) study the order-preserving partial-permutation monoid and its decomposition into extensive and co-extensive parts, but not prescribed square-root multiplicities or the log-fiber law. Alvarez's 2016 paper, *On kth Roots in Semigroups of Order-preserving Partial Permutations*, was read in its main theorem and proof context: it gives a criterion for which targets have roots only through \(n=7\), not an all-dimensional count for each partial-identity target. Laradji and Umar (2015) enumerate nilpotent order-preserving subpermutations and other statistics, which accounts for the central-trinomial ingredient; the accessible abstract does not settle the log-root-fiber distribution. That paper's full text remained inaccessible and is an explicit priority risk.

OEIS A111960 (recorded since 2005) is exactly the numerical bivariate fixed-point triangle obtained after *summing* these fibers by target rank, while A111961 records the unweighted total and its simple-pole asymptotic. They are fully credited; neither is asserted original. For example, A111960's rank-one total \(61\) at \(n=5\) combines five distinct targets with fiber sizes \(19,7,9,7,19\), a positional statistic absent from the table. The previously published Motzkin fiber theorem for the **extensive-only** injective partial Catalan monoid uses a different class of maps, different per-gap factors, and a Rayleigh fixed-point law under a different sampling scheme. It does not imply the prescribed two-direction root fibers or uniform-target log-normal asymptotics here. The new result does not claim any new abstract renewal or central-limit technique.

## Limitations
The theorem applies to increasing **injective** partial transformations, not arbitrary partial transformations or general symmetric inverse monoids. The normal law concerns the logarithm of root multiplicity under **uniform target idempotents**, not root multiplicities directly and not uniform random roots. The already-known OEIS numerical triangle and unweighted asymptotic cannot be claimed as novel results. The historical-priority claim is qualified by the inaccessible full text of Laradji–Umar (2015) and possible unindexed semigroup interpretations of the same renewal array; no independent audit or originality certification is asserted.

## References
1. V. H. Fernandes and T. M. Quinteiro, *A note on bilateral semidirect product decompositions of some monoids of order-preserving partial permutations*, arXiv:1502.06097, first publicly posted 2015-02-21. https://arxiv.org/abs/1502.06097
2. U. Alvarez, *On kth Roots in Semigroups of Order-preserving Partial Permutations*, DIMENSIONS 18, Spring 2016, pp. 123–132, Theorem 3.1 and Sections 2–3. https://www.fullerton.edu/nsmssc/_resources/pdfs/2016_dimensions.pdf
3. A. Laradji and A. Umar, *Combinatorial results for semigroups of order-preserving or order-reversing subpermutations*, J. Difference Equ. Appl. 21 (2015), 269–283, DOI:10.1080/10236198.2015.1005080. https://doi.org/10.1080/10236198.2015.1005080
4. OEIS A002426 (central trinomial numbers), A111960 (renewal array), and A111961 (already-known row sums and mean asymptotic). https://oeis.org/A111960 ; https://oeis.org/A111961
5. *Motzkin square-root fibers and a Rayleigh fixed-point law in injective partial Catalan monoids*, published research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-motzkin-square-root-fibers-and-a-rayleigh-fixed-point-law-in-inj--d449e4ff8b1b
