# Norming-row rigidity and exponentially flat faces for additive product projections

## Finding

Consider the real orthogonal projector onto additive functions on a finite product probability space. Its sharp endpoint norm was previously expressible from the smallest coordinate atom probabilities. The new result here concerns **all norming evaluation rows**, not another derivation of that norm formula.

**Exact support-gap criterion.** Let \(d\ge2\). In the notation below, for a fixed evaluation point \(x\), successively replace its coordinate masses by the minimum masses in the order \(1,\ldots,d\). A replacement strictly raises the absolute reproducing-kernel row sum exactly when a subset sum of the reciprocal masses of the *other* coordinates lies strictly in an explicit interval. The point is norming if and only if no replacement is strict. The criterion is finite and necessary and sufficient without a genericity assumption.

**A complete flat-versus-rigid regime.** Suppose \([d]=R\sqcup T\) with \(R\ne\varnothing\), and write \(r_i=\min_a\mu_i(a)\). If
\[
r_i<\frac1{d-1}\quad(i\in R),\qquad
\sum_{j\in T}\frac1{r_j}<d-1,
\]
then the **entire** norming evaluation locus consists exactly of those \(x\) with \(\mu_i(x_i)=r_i\) for every \(i\in R\); all coordinates in \(T\) are completely unrestricted. The exact norm in this regime is
\[
\|P\|_{L^\infty\to L^\infty}
=1+2(|R|-1)\prod_{i\in R}(1-r_i).
\]
Every nonminimum choice on \(R\) incurs a strictly positive, explicit norm deficit, while changes in \(T\) cost nothing.

In particular, for every integer \(k\ge1\), there is a biased Bernoulli product with \(d=3k+2\) coordinates, none fair, for which **exactly \(2^k\)** different corners are norming. The first \(2k+2\) success probabilities are \(1/(2d)\); the remaining \(k\) probabilities are \(1/3\). Precisely the rows with all first \(2k+2\) coordinates equal to one are norming, while the final \(k\) coordinates are free.

## Assumptions and scope

For each \(i\in[d]\), let \(X_i\) be a finite alphabet of at least two symbols, with a strictly positive probability mass function \(\mu_i\). Put \(X=\prod_iX_i\) and \(\mu=\bigotimes_i\mu_i\). Let \(\mathcal A\subset L^2(\mu;\mathbb R)\) consist of functions \(c+\sum_i g_i(x_i)\), and let \(P\) be its Hilbert orthogonal projector, also regarded as a map on \(L^\infty(\mu;\mathbb R)\).

The reproducing kernel and its row sum are
\[
K(x,y)=\sum_{i=1}^d\frac{\mathbf1_{\{x_i=y_i\}}}{\mu_i(x_i)}-(d-1),
\qquad L(x)=\sum_{y\in X}\mu(y)|K(x,y)|.
\]
Write \(q_i=\mu_i(x_i)\), \(r_i=\min_a\mu_i(a)\), and
\[
\Phi(q_1,\ldots,q_d)=
\mathbb E\left|\sum_{i=1}^d\frac{B_i}{q_i}-(d-1)\right|,
\quad B_i\sim\operatorname{Bernoulli}(q_i)\text{ independently}.
\]
Thus \(L(x)=\Phi(q)\). Each \(q_i\) lies strictly between zero and one. A **norming row** is an \(x\in X\) such that \(L(x)=\|P\|_{\infty\to\infty}\).

For the support-gap test, fix the natural order on \([d]\) and set \(q^{(0)}=q\), \(q^{(i)}=(r_1,\ldots,r_i,q_{i+1},\ldots,q_d)\). When \(q_i>r_i\), define the Boolean support-gap condition
\[
\exists S\subseteq[d]\setminus\{i\}:\qquad
0<d-1-\sum_{j\in S}\frac{1}{q^{(i-1)}_j}<\frac1{r_i}.
\tag{SG_i}
\]
The test asserts that \(x\) is norming **if and only if** \((SG_i)\) is false for every \(i\) with \(q_i>r_i\). If \(q_i=r_i\), the \(i\)-th comparison is automatically an equality. A different fixed replacement order gives the same final decision.

## Proof

**1. Kernel and row norm.** Let \(E_i f=\mathbb E[f\mid X_i]\) and \(E f=\mathbb E f\). Independence makes the centered coordinate spaces mutually orthogonal, so \(P=\sum_iE_i-(d-1)E\). Evaluating the conditional-expectation kernels gives \(K(x,y)\) as displayed. On a finite full-support space, the sharp \(L^\infty\)-operator norm is \(\max_xL(x)\); each row norm is attained by the real input \(f(y)=\operatorname{sgn}K(x,y)\), with arbitrary values in \([-1,1]\) where the kernel vanishes.

**2. Strict convex-order comparison.** Let \(0<r<s<1\). Write \(W_t=B_t/t\) with \(B_t\sim\operatorname{Bernoulli}(t)\). Couple \(W_r\) to \(W_s\) by setting \(W_r=0\) if \(W_s=0\), and, conditional on \(W_s=1/s\), setting \(W_r=1/r\) with probability \(r/s\), and zero otherwise. Then \(\mathbb E[W_r\mid W_s]=W_s\). For each fixed real \(z\), Jensen's inequality gives \(\mathbb E|z+W_r|\ge\mathbb E|z+W_s|\). Because \(|\cdot|\) is affine on either half-line and has its only kink at zero, the comparison is **strict exactly when** \(-1/r<z<0\); its conditional law has two distinct values with positive weights. With independent remaining coordinates, their sum takes every subset-sum value \(z=1-d+\sum_{j\in S}1/q_j\) with positive probability. Therefore replacing coordinate \(i\) by its minimum mass \(r_i\) strictly increases \(\Phi\) exactly when \((SG_i)\) holds.

**3. Necessity and sufficiency of the full row criterion.** Each step in the chain
\[
\Phi(q^{(0)})\le\Phi(q^{(1)})\le\cdots\le\Phi(q^{(d)})=\Phi(r_1,\ldots,r_d)
\]
is nondecreasing. Since any evaluation mass vector can be compared this way, \(\Phi(r)\) is the maximum. Equality from first to last is equivalent to equality at every step, and step equality is exactly the negation of its \((SG_i)\) condition. This proves the complete row criterion without assuming that every nonminimum coordinate gives a strict one-step loss.

**4. Sign masking and norm.** Now assume the displayed conditions on \(R,T\). Fix a row satisfying \(q_i=r_i\) for all \(i\in R\). If any \(R\)-coordinate matches its evaluation symbol in a random \(y\), the corresponding term in \(K(x,y)\) exceeds \(d-1\); hence \(K(x,y)>0\). If none matches, the sum of all \(T\)-coordinate terms is at most \(\sum_{j\in T}1/r_j<d-1\), so \(K(x,y)<0\). Thus the kernel sign depends only on whether at least one \(R\)-coordinate matches. The probability of no such match is \(\prod_{i\in R}(1-r_i)\), and conditional on that event the expected kernel is \(|T|-(d-1)=-(|R|-1)\). Since \(\mathbb E_yK(x,y)=1\), its absolute expectation equals \(1+2(|R|-1)\prod_{i\in R}(1-r_i)\), independently of all chosen \(T\)-symbols. These rows are norming by step 3.

Conversely, suppose a row has \(q_i>r_i\) for some \(i\in R\). In the direct comparison replacing only \(q_i\) by \(r_i\), the event that no other coordinate matches the evaluation point has probability \(\prod_{j\ne i}(1-q_j)>0\) and gives \(z=-(d-1)\). Because \(r_i<1/(d-1)\), this lies strictly between \(-1/r_i\) and zero. Hence the direct replacement is strictly improving; the row cannot be norming. More quantitatively, the exact one-variable difference on this event yields
\[
\|P\|_{\infty\to\infty}-L(x)\ \ge\
2\prod_{j\ne i}(1-q_j)
\min\left\{(d-1)(q_i-r_i),\,1-(d-1)r_i\right\}>0.
\]
This proves both the classification and the strict deficit.

**5. Exponentially many norming corners.** With \(d=3k+2\), \(|R|=2k+2\) and \(|T|=k\), choose Bernoulli masses \(r_i=1/(2d)\) for \(i\in R\) and \(r_j=1/3\) for \(j\in T\). Then \(1/r_i=2d>d-1\), and \(\sum_{j\in T}1/r_j=3k<3k+1=d-1\). The classification permits exactly the \(2^k\) possible choices of the remaining coordinates and no others. The norm equals
\[
1+2(2k+1)\left(1-\frac{1}{2(3k+2)}\right)^{2k+2}.
\]
Every coordinate is strictly biased, so the multiplicity is not a fair-coordinate symmetry artifact.

## Verification

A standalone exact-rational checker (`verify.py`) enumerates every kernel row for the \(k=1,2\) binary instances, tests the complete norming set and quantitative loss bound, and verifies a three-symbol masked-coordinate example. It separately checks the necessary-and-sufficient subset-crossing test against direct row sums for 124 exact-rational one-coordinate comparisons. Execute `python verify.py` from the directory containing this file. All finite computations are supporting checks; steps 1–5 prove the statements for all finite dimensions and strictly positive weights.

## Relationship to prior work

The orthogonal basis and least-squares projection on biased finite products are classical; specifically, Ding, Lax, Chen and Chen (2008) derive weighted pseudo-Boolean least-squares formulas, and Ding, Lax, Chen, Chen and Marx (2010) derive product-measure orthonormal expansions. A preceding finite-product ANOVA endpoint result already gives the **sharp norm and existence of an all-minimum-mass norming row**, so those facts are not claimed new. The contribution here is the complete necessary-and-sufficient **all-row equality test**, an explicit regime of mixed flatness and strict rigidity, a quantitative gap for nonminimum rare rows, and unbounded-dimensional families with exponentially many inequivalent norming rows. A previously recorded iid Bernoulli extremizer classification gives at most a Hamming-nearest-neighbor resonance and does not imply the heterogeneous masking classification by symmetry alone.

## Limitations

All coordinate alphabets are finite and all masses are strictly positive. The theorem concerns real scalar inputs and the first-order additive orthogonal projection, not higher ANOVA orders, arbitrary dependent laws, or arbitrary least-norm projections. The conditions on \(R,T\) are sufficient for the complete simple masked-face classification, not claimed necessary for every flat norming set. The support-gap test is exact but may require exponentially many subset checks. Equivalent characterizations in literature not indexed or accessed remain possible.

## References

1. G. Ding, R. F. Lax, J. Chen and P. P. Chen, “Formulas for approximating pseudo-Boolean random variables,” *Discrete Applied Mathematics* **156** (2008), 1581–1597. DOI: 10.1016/j.dam.2007.08.034. Author preprint: https://www.math.lsu.edu/~lax/pbfformulas.pdf.
2. G. Ding, R. F. Lax, J. Chen, P. P. Chen and B. D. Marx, “Transforms of pseudo-Boolean random variables,” *Discrete Applied Mathematics* **158** (2010), 13–24. DOI: 10.1016/j.dam.2009.08.009. Author's personal copy: https://www.math.lsu.edu/~lax/DAM7433.pdf.
