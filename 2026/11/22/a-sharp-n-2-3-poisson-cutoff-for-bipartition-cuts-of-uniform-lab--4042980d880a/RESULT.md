# A sharp \(n^{2/3}\) Poisson cutoff for bipartition cuts of uniform labelled trees

## Finding
Let \(T_n\) be a uniform labelled tree on \([n]\), and fix a nonempty deterministic vertex bipartition \((A,B)\) with \(|A|=a\le b=|B|\), \(a+b=n\). Let \(X_{n,a}\) count tree edges with one endpoint in each part. Its probability generating function is exactly
\[
\mathbb E z^{X_{n,a}}=z\left(\frac{a+bz}{n}\right)^{a-1}\left(\frac{b+az}{n}\right)^{b-1}.
\]
Consequently, with independent binomial variables,
\[
X_{n,a}\overset d=a+\operatorname{Bin}(b-1,a/n)-\operatorname{Bin}(a-1,a/n).
\]
For any integer sequence \(1\le a=a_n=o(n)\), set \(\lambda_{n,a}=a(1-2a/n)\). Then
\[
d_{\mathrm{TV}}(\mathcal L(X_{n,a}),\mathcal L(a+\operatorname{Poi}(\lambda_{n,a})))\longrightarrow0.
\]
For all sufficiently large \(n\) with \(a\le n/3\), a quantitative bound is
\[
d_{\mathrm{TV}}\le \frac an+\sqrt{\frac{2a(a-1)}n}\min\{1,\lambda_{n,a}^{-1/2}\}\le\frac an+\sqrt{\frac{6a}n}.
\]
The uncorrected shifted Poisson law undergoes an exact total-variation transition: whenever \(a=o(n)\) and \(a/n^{2/3}\to c\in[0,\infty]\),
\[
\boxed{\lim_{n\to\infty}d_{\mathrm{TV}}(\mathcal L(X_{n,a}),\mathcal L(a+\operatorname{Poi}(a)))=
\begin{cases}0,&c=0,\\ 2\Phi(c^{3/2})-1,&0<c<\infty,\\1,&c=\infty.\end{cases}}
\]
Here \(\Phi\) denotes the standard normal distribution function and the last case means \(a/n^{2/3}\to+\infty\) while retaining \(a=o(n)\).

## Assumptions and scope
The vertex labels are fixed and every one of the \(n^{n-2}\) Cayley trees is equally likely. The bipartition is deterministic and does not arise from properly two-colouring the sampled tree. We always take its smaller side of size \(a\), so \(1\le a\le n/2\). Total variation uses \(\sup_E|\mathbb P(E)-\mathbb Q(E)|\). All limits range over integers \(n\to\infty\); an integer sequence satisfying \(a=o(n)\) may remain bounded or oscillate. The approximation is a probability law on integers with deterministic shift \(a\).

## Proof
**Exact factorization.** Give all edges within either class weight \(1\), and edges between classes weight \(z>0\). The weighted Laplacian of the complete graph has eigenvalues \(0\), \(nz\) (once), \(a+bz\) (multiplicity \(a-1\)), and \(b+az\) (multiplicity \(b-1\)). Indeed, the two last values act on classwise zero-sum vectors, and the first two on classwise constant vectors. The matrix-tree theorem gives the weighted spanning-tree enumerator \(z(a+bz)^{a-1}(b+az)^{b-1}\). Divide by \(n^{n-2}\) to obtain the stated PGF, extending the identity to \(z=0\) polynomially. The binomial representation follows by replacing \(\operatorname{Bin}(a-1,b/n)\) with \((a-1)-\operatorname{Bin}(a-1,a/n)\). Differentiating yields \(\mathbb EX=2ab/n\) and \(\operatorname{Var}(X)=(n-2)ab/n^2\).

**Bias-corrected Poisson coupling.** Put \(p=a/n\), \(D\sim\operatorname{Bin}(a-1,p)\), \(U\sim\operatorname{Bin}(b-1,p)\), independent. Denote \(\mu_D=(a-1)p\) and \(\mu_U=(b-1)p\), so \(\lambda=\mu_U-\mu_D=a(1-2a/n)\). In the sparse-side regime \(a\le n/3\), \(\lambda>0\). The standard binomial-to-Poisson bound gives \(d_{\mathrm{TV}}(U,\operatorname{Poi}(\mu_U))\le p\). Decompose a Poisson variable of mean \(\mu_U\) as independent \(Z+W\), with \(Z\sim\operatorname{Poi}(\lambda)\), \(W\sim\operatorname{Poi}(\mu_D)\), independent also of \(D\). Thus the remaining error is the integer shift \(W-D\), whose mean is zero and whose second moment is \(\operatorname{Var}(W-D)=\mu_D+\mu_D(1-p)\le2\mu_D\). For any integer \(h\), telescoping adjacent Poisson mass functions (each unimodal) gives
\[
d_{\mathrm{TV}}(\mathcal L(Z+h),\mathcal L(Z))\le |h|\max_k\mathbb P(Z=k)\le |h|\min\{1,\lambda^{-1/2}\}.
\]
Average over \(h=W-D\) and apply Cauchy–Schwarz to prove the quantitative bound. Since \(\lambda\ge a/3\) and \(\mu_D\le a^2/n\), this goes to zero whenever \(a=o(n)\), uniformly across bounded and growing \(a\).

**Uncorrected approximation and its critical scale.** Write \(\Delta=a-\lambda=2a^2/n\), and compare \(P=\operatorname{Poi}(a)\) with \(Q=\operatorname{Poi}(a-\Delta)\). Their Kullback–Leibler divergence satisfies
\[
D(Q\Vert P)=(a-\Delta)\log(1-\Delta/a)+\Delta\le \Delta^2/a,
\]
by \(\log(1-x)\le-x\), so Pinsker's inequality shows \(d_{\mathrm{TV}}(P,Q)\to0\) when \(\Delta/\sqrt a\to0\). At the critical scale \(a/n^{2/3}\to c\in(0,\infty)\), the likelihood ratio of the Poisson masses crosses one at the integer nearest \(t=\Delta/\log(a/(a-\Delta))\). Since \(\Delta/\sqrt a\to2c^{3/2}\), \(\Delta/a\to0\), expansion gives \(t=a-\Delta/2+O(\Delta^2/a)\). The ordinary Poisson central limit theorem, applied to the difference of the two upper tails at this crossing, yields \(2\Phi(c^{3/2})-1\). If \(a/n^{2/3}\to\infty\) while \(a=o(n)\), the difference in means \(\Delta\) exceeds their standard deviations by an unbounded factor. Chebyshev's inequality at the midpoint \(a-\Delta/2\) then gives total variation tending to one. At \(c=0\), the preceding divergence bound applies directly, including bounded \(a\). Finally, the bias-corrected approximation error vanishes in all these regimes; the total-variation triangle inequality transfers each of the Poisson-to-Poisson limits to the actual cut law. This proves the full three-phase statement.

## Verification
A standalone standard-library checker `verify_cut.py` enumerates independent Prüfer codes on \(2\le n\le7\) and every nontrivial cut size. It checks the exact polynomial coefficients against separately decoded trees, as well as the exact expectation and variance in rational arithmetic. Its completed run passed 21 distribution comparisons encompassing 107,877 fully decoded Prüfer trees. These finite tests are consistency checks; the preceding determinant, coupling and central-limit proof establishes the claims for all sizes.

## Relationship to prior work
Classical Cayley–Prüfer enumeration and weighted spanning-tree generating functions are documented by Remmel–Williamson (2002) and Martin–Reiner (2003). The latter's weighted enumerator methodology makes the elementary exact-PGF step unsurprising; that factorization is not separately asserted as a new general technique. Hackl–Panholzer–Wagner (2023, Sect. 2) give independent-binomial laws for induced-edge counts during uncovering of labelled trees, rather than this fixed-cut total-variation transition. Xu–Balakrishnan (2011) study convolutions and orders of heterogeneous Bernoulli variables, not the present random-tree cut and corrected/uncorrected Poisson phase diagram. The claimed contribution is precisely the corrected total-variation approximation throughout the sparse-side regime and its sharp \(n^{2/3}\) failure profile for the naive approximation, rather than generic matrix-tree enumeration or the Poisson central limit theorem alone.

## Limitations
The theorem is for deterministic bipartitions of a complete-graph uniform spanning tree. The corrected-Poisson total-variation claim is not extended to cuts with \(a/n\) bounded away from zero, nor to nonuniform spanning trees. The limit profile is a theorem about one specific uncorrected reference law, not a universal minimax threshold. Published and indexed literature overlap was checked, but historical unindexed or alternate-language equivalences remain a priority risk. There is no claim of independent external mathematical audit.

## References
- J. B. Remmel and S. G. Williamson, *Spanning Trees and Function Classes*, Electronic Journal of Combinatorics 9 (2002), R34, https://doi.org/10.37236/1650 (first published 2002-08-12).
- J. L. Martin and V. Reiner, *Factorizations of Some Weighted Spanning Tree Enumerators* (2003), https://arxiv.org/abs/math/0302213 (first posted 2003-02-18).
- B. Hackl, A. Panholzer and S. Wagner, *The Uncover Process for Random Labeled Trees*, La Matematica 2 (2023), 861–892, https://arxiv.org/abs/2301.00664 (first posted 2023-01-02).
- M. Xu and N. Balakrishnan, *On the Convolution of Heterogeneous Bernoulli Random Variables*, Journal of Applied Probability 48 (2011), 877–884, https://doi.org/10.1239/jap/1316796922.
