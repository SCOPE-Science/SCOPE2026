# Sharp sparse-rank amplification for first Johnson spectral projections

## Finding
For every integer \(n\ge4\) and \(1\le k\le\lfloor n/2\rfloor\), let \(X_{n,k}=\{S\subseteq[n]:|S|=k\}\) carry uniform probability, and let \(P_{n,k}\) be the orthogonal projection of real functions on \(X_{n,k}\) onto the degree-one harmonic subspace
\[
H^1_{n,k}=\left\{T\longmapsto\sum_{i\in T}a_i:\ a_i\in\mathbb R,\ \sum_{i=1}^{n}a_i=0\right\}.
\]
Put \(j=\lfloor k^2/n\rfloor\). The exact endpoint norm is
\[
\Lambda_{n,k}:=\|P_{n,k}\|_{L^\infty\to L^\infty}
=\frac{2(n-1)(k-j)^2}{k(n-k)}\frac{\binom{k}{j}\binom{n-k}{k-j}}{\binom nk}.
\tag{1}
\]
The one-point hypergeometric absolute-deviation reduction underlying (1) is an existing result; it is used as an exact finite tool, not asserted to be a newly discovered identity.

The new cross-rank conclusion is
\[
\boxed{\lim_{n\to\infty}\frac1{\sqrt n}
\max_{1\le k\le\lfloor n/2\rfloor}\Lambda_{n,k}=\sqrt{\frac2e}.}
\tag{2}
\]
Moreover, **every** sequence of maximizing ranks \(k_n\in\operatorname*{argmax}_{1\le k\le\lfloor n/2\rfloor}\Lambda_{n,k}\) satisfies
\[
\boxed{\frac{k_n}{\sqrt n}\longrightarrow\frac1{\sqrt2}.}
\tag{3}
\]
The complete interpolation between sparse and dense ranks is as follows. For any rank sequence \(1\le k_n\le n/2\),
\[
\frac{\Lambda_{n,k_n}}{\sqrt n}\longrightarrow
\begin{cases}
0,& k_n/\sqrt n\to0,\\[2pt]
\displaystyle\frac{\mathbb E|Z_{c^2}-c^2|}{c}
=\frac{2e^{-c^2}(c^2)^{\lfloor c^2\rfloor+1/2}}{\lfloor c^2\rfloor!},&k_n/\sqrt n\to c\in(0,\infty),\\[6pt]
\sqrt{2/\pi},&k_n/\sqrt n\to\infty,
\end{cases}
\tag{4}
\]
where \(Z_\lambda\) has the Poisson distribution of mean \(\lambda\). At positive integer \(c^2\), the displayed Poisson expression is interpreted by continuity, which agrees with either adjacent floor convention. In particular the global sharp constant in (2) is strictly larger than the dense-rank Gaussian constant \(\sqrt{2/\pi}\).

## Assumptions and scope
All operators and extremizing functions are real. The counting measure on \(X_{n,k}\) has total mass one; every \(L^p\) norm uses that normalization. The projection is **the canonical** \(L^2\)-orthogonal projection, not an optimization over all projections with the same range. Complementing subsets identifies the projections at ranks \(k\) and \(n-k\), so restriction to \(k\le n/2\) loses no configurations. The norm is achieved at every evaluation point; for each fixed \(S\), its norming inputs are precisely nonzero scalar multiples of the kernel sign pattern on pairs with nonzero kernel, with arbitrary bounded values of no larger absolute magnitude on its zero set (and the corresponding global row extremal condition).

## Proof
**1. Exact projection kernel and endpoint norm.** Write \(\xi_i(S)=\mathbf1_{\{i\in S\}}-k/n\). By exchangeability, for any coefficient vector \(a\) satisfying \(\sum_i a_i=0\),
\[
\mathbb E\left(\sum_i a_i\xi_i(S)\right)^2
=\frac{k(n-k)}{n(n-1)}\sum_i a_i^2.
\]
Therefore the reproducing kernel of the first-harmonic subspace, with respect to normalized counting measure, is
\[
K(S,T)=\frac{n(n-1)}{k(n-k)}\left(|S\cap T|-\frac{k^2}{n}\right).
\tag{5}
\]
Indeed, evaluation at \(S\) equals the inner product against \(K(S,\cdot)\) on the coefficient hyperplane. Transitivity makes the absolute row sum independent of \(S\). If \(J=|S\cap T|\) for uniform \(T\), then
\[
\Pr(J=t)=p_t:=\frac{\binom{k}{t}\binom{n-k}{k-t}}{\binom nk},\qquad \mathbb EJ=\mu=\frac{k^2}{n},
\]
and (5) gives
\[
\Lambda_{n,k}=\frac{n(n-1)}{k(n-k)}\mathbb E|J-\mu|.
\tag{6}
\]
Equality in the rowwise \(L^\infty\) bound is obtained by the sign of (5).

For completeness, the known single-boundary mean-absolute-deviation identity also follows directly: set \(q_t=(k-t)^2p_t\), with \(q_{-1}=q_k=0\). Hypergeometric consecutive-mass ratios imply
\[
q_{t-1}-q_t=(nt-k^2)p_t=n(t-\mu)p_t
\qquad(0\le t\le k).
\tag{7}
\]
Writing \(j=\lfloor\mu\rfloor\) and summing over \(t>\mu\) gives \(n\mathbb E(J-\mu)_+=q_j\). Since \(\mathbb E(J-\mu)=0\), \(\mathbb E|J-\mu|=2q_j/n\), proving (1). This reduction is stated as background, and the new comparison begins with the full rank dependence of (6).

**2. Sparse and central limits.** If \(k/\sqrt n\to0\), the elementary nonnegative-variable inequality \(\mathbb E|J-\mu|\le2\mu\) gives
\[
\Lambda_{n,k}\le\frac{2(n-1)k}{n-k}=o(\sqrt n).
\]
If \(k/\sqrt n\to c>0\) finite, then \(k/n\to0\) and \(\mu\to c^2\). The factorial moments \(\mathbb E(J)_r=(k)_r^2/(n)_r\) tend to \(c^{2r}\) for each fixed \(r\). Equivalently, the hypergeometric law converges to \(Z_{c^2}\). Its second moments remain bounded, hence the absolute centered deviations are uniformly integrable. Since \(n(n-1)/(k(n-k)\sqrt n)\to1/c\), (6) yields the middle line of (4). For a Poisson random variable \(Z_\lambda\), telescoping its mass function gives \(\mathbb E|Z_\lambda-\lambda|=2\lambda\Pr(Z_\lambda=\lfloor\lambda\rfloor)\), including integer \(\lambda\) by either adjacent index.

**3. Dense-in-the-root-scale limit.** Suppose \(k/\sqrt n\to\infty\) but \(k\le n/2\). The hypergeometric variance is exactly
\[
\sigma^2=\frac{k^2(n-k)^2}{n^2(n-1)}\longrightarrow\infty.
\]
At \(j=\lfloor\mu\rfloor\), the four entries of the associated \(2\times2\) contingency table are \(j, k-j,k-j,n-2k+j\), all tending to infinity: the smallest is \(j\sim k^2/n\). Applying \(\log s!=(s+\tfrac12)\log s-s+\tfrac12\log(2\pi)+O(s^{-1})\) to the exact mass at \(j\), the entropy terms have their stationary point at \(\mu\); their Taylor remainder at \(j-\mu=O(1)\) is \(o(1)\), and the Gaussian determinant gives
\[
p_j=(1+o(1))(\sqrt{2\pi}\,\sigma)^{-1}.
\tag{8}
\]
The approximation holds for every such sequence because the smallest table cell tends to infinity, not only when \(k/n\) has a positive limit. From (1), \(k-j=(k(n-k)/n)(1+o(1))\). Consequently
\[
\Lambda_{n,k}=\frac{2(n-1)k(n-k)}{n^2}\frac{1+o(1)}{\sqrt{2\pi}\,\sigma}
=(1+o(1))\sqrt{\frac{2n}{\pi}}.
\]
This proves the last line of (4), including the regime \(\sqrt n\ll k\ll n\).

**4. Unique global maximum of the Poisson profile.** Put \(\lambda=c^2\). On each interval \(m\le\lambda<m+1\), with integer \(m\ge0\), the middle profile in (4) is
\[
\Psi_m(\lambda)=2e^{-\lambda}\frac{\lambda^{m+1/2}}{m!}.
\]
Its unique maximum occurs at \(\lambda=m+1/2\), with height
\[
M_m=2e^{-(m+1/2)}\frac{(m+1/2)^{m+1/2}}{m!}.
\]
The heights are strictly decreasing. Indeed, with \(t=m+1/2\) and \(z=(2m+2)^{-1}\),
\[
\log\frac{M_{m+1}}{M_m}
=-1+\frac{1-z}{z}\operatorname{artanh}z+\log(1+z)
=-\sum_{r=1}^{\infty}\frac{z^{2r}}{2r(2r+1)}<0.
\tag{9}
\]
The expansions converge for every \(m\ge0\), because \(0<z\le1/2\). Thus the unique maximum over \(c>0\) is at \(c=1/\sqrt2\), with value \(M_0=\sqrt{2/e}\). The boundary limits at \(c\downarrow0\) and \(c\to\infty\) are \(0\) and \(\sqrt{2/\pi}\), respectively, and \(\sqrt{2/\pi}<\sqrt{2/e}\).

**5. Maximizing ranks.** Taking \(k_n\) to be an integer nearest \(\sqrt{n/2}\) in (4) proves the liminf in (2). For any maximizing sequence, every subsequence of \(k_n/\sqrt n\) has a further subsequence converging in the compact extended interval \([0,\infty]\). Formula (4) excludes the endpoints \(0,\infty\) because their limits are strictly below \(\sqrt{2/e}\), and (9) forces any positive finite subsequential limit to equal \(1/\sqrt2\). This establishes (2) and (3).

## Verification
The self-contained `verify_johnson.py` uses rational combinatorial probabilities to compare (1) to the direct absolute kernel sum for every \(3\le n<90\) and admissible rank, checks the telescoping mass identity, and verifies exact kernel-matrix idempotence in representative small dimensions. It also tests strict decrease of the first 100 Poisson candidate peaks and reports numerical rank maximizers at several dimensions. These finite checks corroborate (1) and (9); the complete asymptotic and uniqueness assertions are established by the preceding proof, not finite enumeration. The code requires only Python's standard library.

## Relationship to prior work
Filmus established the harmonic decomposition of functions on Johnson slices, and Scarabotti–Tolli developed the finite homogeneous-space representation framework. Their inspected original texts give the underlying eigenspaces and group-invariant projectors, but not a global optimization over ranks of endpoint projector norms. The single-boundary reduction of hypergeometric mean absolute deviation in (7) is already known, including in Elezović's 2026 work; no novelty is claimed for that reduction or for merely applying it to a linear kernel. A published exact degree-two Johnson endpoint-norm theorem concerns a different primitive idempotent, with quadratic rather than linear intersection kernel. Neither the known fixed-density hypergeometric asymptotics nor the fixed-degree result directly supplies the global sharp rank law (2)–(3): the winning regime has \(k/n\to0\) but \(k/\sqrt n\to1/\sqrt2\), and requires comparison of all three scales.

## Limitations
The theorem treats the first nonconstant Johnson spectral projection on uniform finite slices, not degree-two or higher projections and not arbitrary exchangeable measures. It gives the unique limiting optimizing rank ratio, not an exact formula for the finite-dimensional maximizing integer rank or a rate of convergence. The full 2026 hypergeometric mean-absolute-deviation manuscript was not accessible for complete comparison; any assertion there about optimization jointly over both margins would require a separate priority check. Related results in unindexed literature may also exist.

## References
1. F. Scarabotti and F. Tolli, *Harmonic analysis on a finite homogeneous space*, arXiv:math/0701533 (first posted 2007-01-19), Sections 1–3.
2. Y. Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142 (first posted 2014-06-01), Sections 1–3; Electronic Journal of Combinatorics 23 (2016), P1.23.
3. N. Elezović, *The mean absolute deviation of the classical discrete distributions: collapse identities, complete asymptotic expansions, and enveloping series*, arXiv:2608.06232 (2026). The accessible abstract identifies prior coverage of the deviation-to-point-mass reduction and fixed-proportion hypergeometric asymptotics; the full manuscript was inaccessible.
4. *Exact endpoint norm of the second Johnson spherical projector*, published-finding corpus public record `2026/10/11/SCOPE-exact-endpoint-norm-of-the-second-johnson-spherical-projector--f9735429621e`, full `RESULT.md` inspected. This is a distinct degree-two projection.
