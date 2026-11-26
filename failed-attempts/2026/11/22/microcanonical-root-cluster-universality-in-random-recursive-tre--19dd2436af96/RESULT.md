# Microcanonical root-cluster universality in random recursive tree percolation

## Finding

Let \(T_n\) be a uniform rooted recursive tree on \(\{1,\ldots,n\}\), \(n\ge2\). Delete exactly \(h\) of its \(n-1\) edges, choosing the deleted set uniformly and independently of the tree. Let \(X_{n,h}\) be the number of vertices connected to root \(1\) after deletion. Write \(N=n-1\), \(x^{\overline r}=\prod_{a=0}^{r-1}(x+a)\), and \(e_h\) for the elementary symmetric polynomial of degree \(h\), with \(e_0=1\).

**Exact conditioned factorial-moment law.** For every integer \(r\ge1\), \(n\ge2\), and \(0\le h\le N\),
\[
\boxed{\mathbb E[X_{n,h}^{\overline r}]
=\frac{r!\binom{N+r}{r}}{\binom Nh}
 e_h\left(\frac1{1+r},\frac2{2+r},\ldots,\frac N{N+r}\right).}
\tag{1}
\]
This formula is independent of any auxiliary Bernoulli retention parameter and applies to all possible fixed deletion counts, including the deterministic endpoints.

**Non-Gaussian equivalence of ensembles.** Let \(h_n\) be any deterministic integers with \(0\le h_n\le n-1\), and put \(p_n=1-h_n/(n-1)\). If \(p_n\to p\in(0,1)\), then
\[
\boxed{\frac{X_{n,h_n}}{n^{p_n}}\ \xrightarrow{\ d\ }\ W_p,
\qquad
\lim_{n\to\infty}\mathbb E\left[\left(\frac{X_{n,h_n}}{n^{p_n}}\right)^r\right]
=\frac{r!}{\Gamma(1+rp)}\quad(r=1,2,\ldots).}
\tag{2}
\]
The nonnegative, moment-determinate random variable \(W_p\) has the Mittag--Leffler moment sequence displayed in (2), coinciding with the familiar *unconditioned* independent-edge-retention root-cluster limit. The normalization uses the actual retention fraction \(p_n\), not merely its limit \(p\); no rate of convergence of \(p_n\) is assumed.

## Assumptions and scope

Each vertex \(j\ge2\) independently chooses one of \(1,\ldots,j-1\) uniformly as parent. Conditional on this random tree, each subset of exactly \(h\) edge labels is equally likely to be deleted. Deletion is performed simultaneously: components not containing the root are retained in the forest, but not counted in \(X_{n,h}\). The exact formula holds for all nonnegative deletion counts \(h\le n-1\), whereas the asymptotic assertion requires the limiting retained fraction to lie strictly between zero and one. Every integer moment order \(r\) is fixed before taking \(n\to\infty\).

## Proof

**1. A marked rising-factorial transform.** First introduce an auxiliary, independent-edge model: retain each edge with probability \(u\in(0,1)\), deleting it otherwise. Let \(C_j\) be the root-component size after the first \(j\) vertices, and \(H_j\) the number of deleted edges among them. At stage \(j+1\), the new vertex joins the root component with probability \(uC_j/j\), and the new edge is deleted with probability \(1-u\), independently of its parent. The rising-factorial identity
\[
 (x+1)^{\overline r}-x^{\overline r}
 =\frac rx\,x^{\overline r}\qquad(x\ge1)
\]
gives the *conditional marked recurrence*
\[
\mathbb E\!\left[C_{j+1}^{\overline r}z^{H_{j+1}-H_j}\mid C_j,H_j\right]
 =C_j^{\overline r}\left(u+(1-u)z+\frac{ru}{j}\right).
\]
Starting from \(C_1=1\), \(H_1=0\), induction yields
\[
 \boxed{\mathbb E[C_n^{\overline r}z^{H_n}]
 =r!\prod_{j=1}^{N}\left(u+(1-u)z+\frac{ru}{j}\right).}
 \tag{3}
\]
Here \(H_n\sim\operatorname{Bin}(N,1-u)\), and conditional on \(H_n=h\) the deleted-edge set is exactly uniform among the \(\binom Nh\) possibilities. Thus \(C_n\mid\{H_n=h\}\) has the distribution of \(X_{n,h}\).

Factor the right-hand side of (3) as
\[
 r!\,u^N\prod_{j=1}^{N}\left(1+\frac rj\right)
 \prod_{j=1}^{N}\left(1+\frac{1-u}{u}\frac{j}{j+r}z\right).
\]
The first product equals \(\binom{N+r}{r}\). Extract the coefficient of \(z^h\), and divide by \(\Pr(H_n=h)=\binom Nh u^{N-h}(1-u)^h\). All auxiliary factors involving \(u\) cancel, proving (1). In particular, for \(h=0\) the root component has size \(n\), while for \(h=N\) it has size one; both endpoints are consistent with (1).

**2. Factorial-moment bias converts conditioning into a local limit.** Let \(u=p_n\) for large \(n\). At \(z=1\), (3) gives the exact unconditioned moment
\[
 A_{n,r}(u):=\mathbb E[C_n^{\overline r}]
 =r!\prod_{j=1}^{N}\left(1+\frac{ru}{j}\right)
 =\frac{r!\,\Gamma(n+ru)}{\Gamma(n)\Gamma(1+ru)}.
\]
After dividing (3) by \(A_{n,r}(u)\), its generating polynomial becomes that of a sum \(S_{n,r}(u)=\sum_{j=1}^{N}B_j\) of *independent*, not identically distributed Bernoulli random variables, with
\[
 \Pr(B_j=1)=q_j:=\frac{1-u}{1+ru/j}.
\]
Consequently, exactly,
\[
 \mathbb E[X_{n,h}^{\overline r}]
 =A_{n,r}(u)\,
 \frac{\Pr(S_{n,r}(u)=h)}
 {\Pr(\operatorname{Bin}(N,1-u)=h)}.
 \tag{4}
\]
We show the probability ratio in (4) tends to one when \(h=h_n\). Write \(u=p_n\to p\in(0,1)\). Since \(N(1-u)=h_n\), direct summation gives
\[
 \mathbb E S_{n,r}(u)
 =h_n-r u(1-u)\sum_{j=1}^N\frac1{j+ru}
 =h_n+O_r(\log n),
\]
\[
 \operatorname{Var}(S_{n,r}(u))
 =N u(1-u)+O_r(\log n).
 \tag{5}
\]
Both estimates are uniform once \(u\) stays inside a compact subinterval of \((0,1)\).

For completeness, a local central limit argument supplies the required *point probability*, not merely a weak central limit theorem. For any independent Bernoulli triangular array with at least \(N/2\) success parameters in \([\varepsilon,1-\varepsilon]\) and total variance \(\sigma_N^2\sim Np(1-p)\), Fourier inversion gives
\[
 \sup_{k\in\mathbb Z}\left|\sigma_N\Pr(S_N=k)
 -\frac1{\sqrt{2\pi}}
 \exp\left(-\frac{(k-\mathbb ES_N)^2}{2\sigma_N^2}\right)\right|\longrightarrow0.
 \tag{6}
\]
Indeed, for \(|t|\le M/\sqrt N\), expand the logarithm of the centered characteristic function: it is \(-\sigma_N^2t^2/2+O(N|t|^3)\). Outside that shrinking central range use
\[
 \left|\prod_j(1-q_j+q_j e^{it})\right|
 \le\exp\left(-2\sum_j q_j(1-q_j)\sin^2(t/2)\right)
 \le e^{-cNt^2},\quad -\pi\le t\le\pi,
\]
where the second bound follows from the nondegenerate half of the array and \(\sin(|t|/2)\ge |t|/\pi\). Rescaling the Fourier integral by \(\sqrt N\), dominated convergence and then \(M\uparrow\infty\) prove (6), uniformly in integer \(k\). The same argument applies to the binomial distribution.

The Bernoulli parameters \(q_j\) above are uniformly bounded away from zero and one for \(j\ge N/2\). By (5), \(h_n-\mathbb ES_{n,r}=O_r(\log n)=o(\sqrt N)\), while the two variances have the same leading term. Applying (6) at \(k=h_n\) gives
\[
 \Pr(S_{n,r}(p_n)=h_n)
 \sim\Pr(\operatorname{Bin}(N,1-p_n)=h_n)
 \sim\frac1{\sqrt{2\pi Np(1-p)}}.
 \tag{7}
\]
This relative local limit is the part that cannot be obtained from the unconditioned distributional limit alone.

**3. Passage to moments and weak convergence.** Combining (4) and (7), followed by the uniform gamma-ratio estimate for \(p_n\to p\), gives, for every fixed integer \(r\ge1\),
\[
 \frac{\mathbb E[X_{n,h_n}^{\overline r}]}{n^{rp_n}}
 \longrightarrow\frac{r!}{\Gamma(1+rp)}.
 \tag{8}
\]
Because \(x^{\overline r}=x^r+\sum_{k=1}^{r-1}a_{r,k}x^k\) with fixed positive coefficients and \(p_n\to p>0\), induction on \(r\) in (8) shows the same limit for ordinary powers. The first moment yields tightness of the nonnegative sequence \(X_{n,h_n}/n^{p_n}\). The limiting moment sequence \(m_r=r!/\Gamma(1+rp)\) satisfies Carleman's criterion: by Stirling's formula, \(m_{2r}^{-1/(2r)}\asymp r^{p-1}\), whose sum diverges for \(0<p<1\). Thus the moment limit uniquely determines the weak limit, which is the already-known Mittag--Leffler law with these moments. This proves (2).

## Verification

The standalone standard-library script `verify.py` independently enumerates every recursive parent assignment and edge-deletion subset for orders \(2\) through \(7\), computes the resulting root-component sizes, and compares five rising-factorial moments at every possible deletion count with (1). Independently, it expands (3) as an exact rational polynomial for multiple nontrivial Bernoulli parameters through size \(22\), checks cancellation into the parameter-free conditioned identity, and tests finite log-concavity of the exact mean up to size \(59\). Run `python3 verify.py`. It completed **3,359 exact rational assertions**. Finite checks corroborate the finite formulas; the all-order identity and the weak limit rely on the analytical proof above, especially the local limit argument.

## Relationship to prior work

Zheng (2026) studies whether the root cluster in a continuously grown, independent Bernoulli-bond-percolated recursive tree stays largest; its model uses an unconditioned fixed per-edge retention probability. Desmarais, Holmgren, and Wagner (2021/2023), especially Section 2.2, establish the canonical root-cluster Mittag--Leffler limit and develop root-cluster generating functions. Kürsten (2015/2016), Section IV, derives exact first and second moments in the independent-edge model. Baur (2014/2016) studies independent-edge percolation chiefly in the retention-approaches-one regime. The same independent-edge root-cluster moment formulas underlie the first product in (3), so their unconditional content is **not** claimed as new.

Conditioning on exactly \(h_n\) deleted edges changes all edge states into a dependent sample without replacement and changes the first-table/innovation process into a globally constrained one. A limiting theorem under independent retention does not directly give a conditional limiting theorem at an event of probability of order \(n^{-1/2}\). The specific contribution here is the exact all-order *conditional* transform and a uniform local-limit comparison at the moving mean, establishing the full non-Gaussian law for every sequence \(p_n\to p\in(0,1)\). The inspected root-degree/root-cluster, singleton-count/root-cluster, and frontier/root-cluster results in the published mathematical repository concern different joint statistics and do not imply this conditional law by their stated theorems.

## Limitations

The limit only covers retained fractions bounded away from zero and one in the limit. It neither treats critical near-zero/near-one scaling nor gives rates of convergence or simultaneous laws for multiple clusters. The exact identity (1) is an algebraic extraction from a marked canonical transform; the mathematical work in the equivalence result is the relative local limit, and a more general pre-existing ensemble-equivalence theorem could potentially subsume it. The literature comparison does not establish exhaustive historical priority. All computational checks are finite and do not replace the infinite proof.

## References

1. Y. Zheng, *Can the root cluster remain largest forever in random recursive tree percolation?*, arXiv:2606.01881v1 (first posted June 1, 2026), primary MSC 60C05. https://arxiv.org/abs/2606.01881
2. C. Desmarais, C. Holmgren and S. Wagner, *Broadcasting-induced colorings of preferential attachment trees*, arXiv:2110.15050v1 (first posted October 28, 2021), *Random Structures & Algorithms* 63 (2023), 364--405. https://doi.org/10.1002/rsa.21142
3. R. Kürsten, *Random Recursive Trees and the Elephant Random Walk*, arXiv:1512.05275v1 (first posted December 16, 2015), Section IV. https://arxiv.org/html/1512.05275v1
4. E. Baur, *Percolation on random recursive trees*, arXiv:1407.2508v1 (first posted July 9, 2014), *Random Structures & Algorithms* 48 (2016), 655--680. https://arxiv.org/html/1407.2508v1
5. *Exact root-degree--percolation-cluster dependence and asymptotic decoupling in recursive trees*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-root-degree-percolation-cluster-dependence-and-asymptotic--3992334979d1
6. *Root-cluster and singleton-component anti-covariance in percolated recursive trees*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-root-cluster-and-singleton-component-anti-covariance-in-percolat--c15d28dd041a
