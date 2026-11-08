# Fixed-point enumeration and Gaussian law for quasi-idempotent isotone transformations

## Finding
Let \(\mathcal O_n\) be the monoid of all weakly increasing maps \(f:[n]\to[n]\). A **proper quasi-idempotent** means \(f\ne f^2=f^4\); let \(Q_{n,k}\) count these maps with exactly \(k\) fixed points. Put
\[
B(z)=\frac{z(1-z)^2}{(1-2z)^2},\qquad E(z)=\frac{z}{(1-z)^2}.
\]
Then the complete bivariate ordinary generating function is
\[
\boxed{\sum_{n,k\ge0}Q_{n,k}z^nu^k=\frac1{1-uB(z)}-\frac1{1-uE(z)}}.
\]
For \(1\le k\le n\) this is the explicit coefficient formula
\[
Q_{n,k}=[z^{n-k}]\left(\frac{(1-z)^{2k}}{(1-2z)^{2k}}-\frac1{(1-z)^{2k}}\right),
\]
with \(Q_{n,k}=0\) otherwise (including \(n=k=0\)). In particular, writing \(Q_n=\sum_kQ_{n,k}\),
\[
\sum_{n\ge0}Q_nz^n=\frac{(1-2z)^2}{1-5z+6z^2-z^3}-\frac{(1-z)^2}{1-3z+z^2}.
\]
The first positive-length totals, for \(n=1,\ldots,10\), are \(0,0,2,12,53,208,768,2734,9503,32489\).

Let \(\rho\) be the unique smallest positive root of \(1-5z+6z^2-z^3\), and define \(m=\rho B'(\rho)\), \(v=\rho B'(\rho)+\rho^2B''(\rho)-m^2\), \(\mu=1/m\), and \(\sigma^2=v/m^3\). Then \(\rho=0.3079785283699\ldots\), \(\mu=0.3014166091678\ldots\) and \(\sigma^2=0.1935077065776\ldots>0\). For a uniformly chosen proper quasi-idempotent and its number \(K_n\) of fixed points, as \(n\to\infty\),
\[
\frac{K_n-\mu n}{\sqrt{\sigma^2 n}}\ \Longrightarrow\ N(0,1),\qquad Q_n\sim \mu\rho^{-n}.
\]
Since \(|\mathcal O_n|=\binom{2n-1}{n}\), the proportion of proper quasi-idempotents tends to zero exponentially, more precisely
\[
\frac{Q_n}{|\mathcal O_n|}\sim2\mu\sqrt{\pi n}\left(\frac1{4\rho}\right)^n.
\]

## Assumptions and scope
Here \(n\) is any nonnegative integer, \([n]=\{1,\dots,n\}\), and the empty set has one empty isotone self-map, which is idempotent. Composition is conventional function composition; all generating functions are formal in \(z,u\), while limit assertions use real generating functions. For \(n\ge1\), \(f^2=f^4\) is equivalent to \(f^2=f^3\) among isotone maps, because a monotone map of a finite chain has no periodic orbit longer than one. Proper quasi-idempotents are the maps of exact stabilization depth two, not the idempotents of depth at most one. The fixed-point statistic is \(|\{i:f(i)=i\}|\).

## Proof
**1. Basin decomposition.** Every isotone transformation on a finite chain has no nontrivial cycles. For \(f^2=f^3\), the map \(e=f^2\) is idempotent, so each point reaches a fixed point of \(f\) in at most two steps. Fibers of \(e\) are contiguous intervals, since \(e\) is weakly increasing. Each such interval contains exactly one fixed point \(r\), because \(e(r)=r\), and \(f\) preserves that interval: \(e(f(x))=f^3(x)=f^2(x)=e(x)\). Conversely, independent nondecreasing basin maps, each with all points reaching its root in at most two steps, concatenate to a weakly increasing map (their image sets lie in disjoint ordered intervals). Thus the global map is a unique ordered sequence of rooted basins.

**2. Enumerating one basin.** Write its length as \(1+L+R\), with \(L\) vertices left of the fixed root and \(R\) right of it. For the \(L\) left vertices, let \(t\) be the smallest vertex mapped directly to the root. Such a vertex exists: if the last left vertex did not map to the root, monotonicity would prevent its second iterate from reaching the root. Write \(c=t-a\), where \(a\) is the interval's first vertex; then \(0\le c\le L-1\). For \(i<t\), the equation \(f^2(i)=r\) forces \(f(i)\in[t,r-1]\). Those \(c\) entries form a weakly increasing list with \(L-c\) possible values; its count is \(\binom{L-1}{c}\). All subsequent entries on the left equal \(r\). Therefore the left side has \(\sum_{c=0}^{L-1}\binom{L-1}{c}=2^{L-1}\) choices when \(L\ge1\), and one when \(L=0\). Reflection gives the independent right-side count. The side-length series is \(S(z)=1+\sum_{L\ge1}2^{L-1}z^L=(1-z)/(1-2z)\); the full basin series is \(B(z)=zS(z)^2\). Assigning a factor \(u\) per root and concatenating arbitrarily many basins gives \((1-uB(z))^{-1}\).

**3. Removing idempotents.** An idempotent basin has every vertex mapped directly to its root; it has one map for each placement of the root, hence basin generating function \(E(z)=\sum_{h\ge1}h z^h=z/(1-z)^2\). The analogous ordered-basin series is \((1-uE(z))^{-1}\). Subtraction proves both exact formulas. Setting \(u=1\) and clearing denominators gives the displayed rational total series.

**4. Gaussian limit.** The coefficients of \(B(z)\) are nonnegative, with strictly positive coefficients at lengths one and two. Thus there is a unique real \(\rho\in(0,1/2)\) solving \(B(\rho)=1\), and no other singularity of \((1-uB(z))^{-1}\) on \(|z|=\rho\) at \(u=1\). By the implicit-function theorem, for complex \(u\) near one there is a simple analytic dominant pole \(\rho(u)\) satisfying \(uB(\rho(u))=1\). Uniform singularity analysis gives
\[
[z^n](1-uB(z))^{-1}=\frac{\rho(u)^{-n}}{u\rho(u)B'(\rho(u))}\bigl(1+O(c^n)\bigr)
\]
for a fixed \(0<c<1\) in a neighborhood of \(u=1\). The idempotent series has its closest pole at \((3-\sqrt5)/2>\rho\) when \(u=1\), so its coefficients (uniformly for nearby \(u\)) are exponentially smaller; subtraction does not alter the dominant asymptotic. The normalized moment-generating functions of the fixed-point count have logarithm \(n(\log\rho-\log\rho(e^t))+O(1)\). Twice differentiating \(e^tB(\rho(e^t))=1\) at zero yields mean slope \(1/m\) and variance slope \(v/m^3\). The latter is positive: the probability law \(\Pr(X=j)=[z^j]B(z)\,\rho^j\) has support at both \(j=1\) and \(j=2\), hence nonzero variance \(v\). Taylor expansion at \(t=i\theta/\sqrt n\) and convergence of characteristic functions yield the stated central limit theorem. At \(u=1\), the residue amplitude is \((\rho B'(\rho))^{-1}=\mu\), giving \(Q_n\sim\mu\rho^{-n}\). Finally \(\binom{2n-1}{n}\sim4^n/(2\sqrt{\pi n})\) establishes exponential rarity.

## Verification
The attached standalone `verify.py` uses only the Python standard library. It exhaustively enumerates every weakly increasing map of \([n]\) for \(1\le n\le10\); directly computes its second and third iterates, fixed-point count and idempotence; and checks every \(Q_{n,k}\) against the coefficient formula. It also independently checks the one-basin count and validates the rational recurrence through \(n=16\). Its successful execution prints `VERIFY_OK`. These finite checks corroborate but do not replace the universal combinatorial and analytic proofs.

## Relationship to prior work
Imam, Ibrahim, Garba, Usman and Idris (2023) define and characterize quasi-idempotents in \(\mathcal O_n\) and prove quasi-idempotent generation; their results do not provide the displayed joint fixed-point enumeration. Eze, Olaiya, Pokalas Tal and Kasim (2025) discuss structural digraphs and small-degree counts and explicitly propose asymptotic enumeration as future work; they do not prove a bivariate all-degree series or a Gaussian fixed-point law. The unweighted height-at-most-two count \(1,3,10,33,\ldots\) coincides numerically with the pre-existing OEIS sequence A060557, whose recurrence must not be claimed as a newly discovered integer sequence. The constituent single-basin coefficients likewise coincide with the established sequence A045623, so their numeric generating function is not claimed as new. Idempotent total counts are likewise classical. The contribution is the natural exact **semigroup interpretation**, the joint fixed-point refinement, and the asymptotic law together; no universal publication-priority claim is made.

## Limitations
The theorem applies only to full weakly increasing self-maps of finite chains and to stabilization after at most two iterations; it does not classify quasi-idempotents of arbitrary transformation monoids. The Gaussian result concerns the fixed-point statistic, not the size of the one-step image. A source-dependent risk remains that related weighted enumeration may appear elsewhere under functional-digraph or monotone-map terminology. The finite verifier is not a substitute for independent review.

## References
- A. T. Imam, S. Ibrahim, G. U. Garba, L. Usman, A. Idris, “Quasi-idempotents in finite semigroup of full order-preserving transformations,” *Algebra and Discrete Mathematics* 35(1), 62–72 (2023). DOI: 10.12958/adm1846; public text: https://admjournal.luguniv.edu.ua/index.php/adm/article/view/1846.
- C. Eze, O. O. Olaiya, P. Tal, S. Kasim, “Graph-Theoretic and Algebraic Characterization of Stable Quasi-Idempotents in Full Order-Preserving Transformation Semigroups,” *Journal of Mathematics and Artificial Intelligence* 1(2), 58–66 (2025). Public text: https://www.researchgate.net/publication/395110201_Graph-Theoretic_and_Algebraic_Characterization_of_Stable_Quasi-Idempotents_in_Full_Order-Preserving_Transformation_Semigroups.
- OEIS A060557, https://oeis.org/A060557 (known matching unweighted series and INVERT-transform relation); OEIS A045623, https://oeis.org/A045623 (known single-basin coefficient series).
- C. Eze, A. T. Imam, M. Balarabe, O. O. Olaiya, “Graph-Theoretic Characterizations of Quasi-Idempotents in Full Order-Preserving Transformation Semigroup,” *Babylonian Journal of Mathematics* (2025), DOI: 10.58496/BJM/2025/009.
