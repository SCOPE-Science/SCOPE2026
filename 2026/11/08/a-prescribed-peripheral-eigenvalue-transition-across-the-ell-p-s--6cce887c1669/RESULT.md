# A prescribed peripheral eigenvalue transition across the \(\ell^p\) scale of an unweighted binary tree

## Finding
For every real \(\rho>1\), a *single*, explicitly constructed rooted tree with at most two children per vertex has an unweighted backward-sum shift whose peripheral point spectrum appears exactly when the ambient exponent crosses \(p=\rho\). More precisely, put \(r_p=2^{(1-1/p)/2}\) for \(1\le p<\infty\). On the complex space \(\ell^p(V)\), the spectrum and the Fredholm essential spectrum of \(S_p\) both equal \(\{\lambda:|\lambda|\le r_p\}\), while
\[
\sigma_{\mathrm p}(S_p)=
\begin{cases}
\{\lambda:|\lambda|<r_p\},&1\le p\le\rho,\\
\{\lambda:|\lambda|\le r_p\},&\rho<p<\infty.
\end{cases}
\]
On \(\ell^\infty(V)\), all three spectra are \(\{\lambda:|\lambda|\le\sqrt 2\}\). Every eigenvalue stated above has infinite geometric multiplicity. In particular, the *unweighted* geometric tree itself realizes any prescribed strict transition exponent \(\rho>1\), and the critical endpoint \(p=\rho\) is excluded.

## Assumptions and scope
Fix \(\rho>1\) and \(\kappa=(\rho-1)^{-1}>0\). For each integer \(j\ge1\), define the strictly increasing sequence
\[
N_j=\lceil2^{j/(2\kappa)}\rceil+j.
\]
For each integer \(k\ge1\), concatenate a block of offspring numbers \((2,1)\) and append an additional \(2\) exactly when \(k=N_j\) for some \(j\). The resulting infinite sequence \((b_n)_{n\ge0}\), consisting only of ones and twos, specifies a spherically homogeneous rooted tree: every vertex at level \(n\) has exactly \(b_n\) children. Let \(V\) be the countable vertex set and \(B_n=\prod_{i=0}^{n-1}b_i\), with \(B_0=1\), the level populations. For \(1\le p\le\infty\), define the bounded unweighted backward sum by \((S_pf)(v)=\sum_{u\in\operatorname{Chi}(v)}f(u)\). All assertions concern the ordinary complex \(\ell^p(V)\) norm and Fredholm essential spectrum, not the approximate-point essential spectrum.

## Proof
**1. Exact logarithmic population correction.** Define \(h(k)=\#\{j:N_j\le k\}\). Because \(2^{j/(2\kappa)}\le N_j\le 2^{j/(2\kappa)}+j+1\), and the exponential eventually dominates its linear correction, for fixed \(\kappa\) we have
\[
h(k)=2\kappa\log_2(k+1)+O_\kappa(1).
\]
Indeed, for all sufficiently large \(j\), \(2^{j/(2\kappa)}\le N_j\le 2\cdot 2^{j/(2\kappa)}\); these inequalities sandwich the counting function between two shifted base-two logarithms. At the end of block \(k\), the word length is \(n=2k+h(k)\), and the number of twos is \(k+h(k)\). Thus \(\log_2 B_n-n/2=h(k)/2\) at those endpoints. Between successive endpoints, the discrepancy changes by at most a fixed amount; also \(n=2k+O_\kappa(\log(k+1))\). Consequently, uniformly for all integers \(n\ge0\),
\[
\log_2 B_n=\frac n2+\kappa\log_2(n+2)+O_\kappa(1),\qquad
B_n\asymp_\kappa 2^{n/2}(n+2)^\kappa.
\tag{1}
\]
Here both constants in the two-sided bound are positive and depend only on \(\kappa\).

**2. Necessary and sufficient eigenvalue test.** Fix finite \(1\le p<\infty\) and suppose \(S_pf=\lambda f\) with \(f\ne0\). Put \(A_n=\sum_{|v|=n}|f(v)|^p\). Hölder's inequality (the triangle inequality at \(p=1\)) at every vertex of level \(n\) gives
\[
|\lambda|^p A_n\le b_n^{p-1} A_{n+1}.
\]
Choose a level \(N\) where \(A_N>0\). Iterating yields
\[
A_{N+j}\ge A_N |\lambda|^{pj}(B_N/B_{N+j})^{p-1}\quad(j\ge0).
\tag{2}
\]
When \(|\lambda|\ge r_p\), equation (1) (applied to the tail ratio for each fixed \(N\)) forces the right side of (2) to have infinite sum whenever \(|\lambda|>r_p\), or when \(|\lambda|=r_p\) and \(\kappa(p-1)\le1\). Therefore no nonzero eigenvector exists in those cases. Conversely the level-radial vector
\[
f_\lambda(v)=\lambda^{|v|}/B_{|v|}
\]
satisfies \(S_pf_\lambda=\lambda f_\lambda\). Its norm is determined *exactly* by
\[
\|f_\lambda\|_p^p=\sum_{n\ge0}\frac{|\lambda|^{pn}}{B_n^{p-1}}.
\tag{3}
\]
By equation (1), this converges for \(|\lambda|<r_p\), diverges for \(|\lambda|>r_p\), and on the critical circle is comparable to \(\sum_{n\ge0}(n+2)^{-\kappa(p-1)}\). Therefore the circle is in the point spectrum iff \(\kappa(p-1)>1\), equivalently \(p>\rho\). The case \(\lambda=0\) is also covered by (3), with the convention \(0^0=1\).

For \(p=\infty\), the same radial eigenfunction is bounded for all \(|\lambda|\le\sqrt2\), by equation (1). If \(f\ne0\) satisfies the eigenvalue equation, choose \(v\) with \(f(v)\ne0\). Iteration gives
\[
|\lambda|^j|f(v)|\le (B_{|v|+j}/B_{|v|})\|f\|_\infty.
\]
Taking the \(j\)-th root and letting \(j\to\infty\) forces \(|\lambda|\le\sqrt2\).

**3. Exact growth, full spectrum and Fredholm essential spectrum.** Descendant sets of distinct vertices at the same depth are disjoint. Hölder's inequality on each \(j\)-generation descendant set, together with a constant-on-descendants test vector, therefore yields the exact operator norm
\[
\|S_p^j\|=\left(\sup_{n\ge0}\frac{B_{n+j}}{B_n}\right)^{1-1/p}
\qquad(1\le p\le\infty),
\tag{4}
\]
with \(1-1/\infty=1\). In the case \(p=1\), both sides equal one. Equation (1) implies for every \(n,j\ge0\)
\[
\frac{B_{n+j}}{B_n}\le C_\kappa 2^{j/2}
\left(\frac{n+j+2}{n+2}\right)^\kappa\le C_\kappa2^{j/2}(j+2)^\kappa.
\]
At \(n=0\), the reverse bound up to a positive constant holds. Thus equation (4) and Gelfand's formula show \(r(S_p)=r_p\) for finite \(p\), and \(r(S_\infty)=\sqrt2\). The spectrum is contained in the associated closed disk; by Step 2 it contains its interior, hence equals the disk.

Finally, because infinitely many levels branch into two children and \(B_n\to\infty\), for any eigenvalue from Step 2 choose a branching level with arbitrarily many distinct parents. At each such parent, put opposite unit-amplitude values at two children, and continue *within each child subtree* by the same normalized radial eigenfunction, with the corresponding signs. The values sum to zero at that parent; all higher vertices are zero, so this is a global eigenvector. By equation (3) on the shifted tail (and by the corresponding boundedness argument for \(p=\infty\)), these vectors belong to \(\ell^p\) and have disjoint supports. Their number can be made arbitrarily large, so each eigenspace is infinite-dimensional. Hence every eigenvalue in the *interior* is non-Fredholm. The Fredholm essential spectrum is a closed subset of the full spectrum and therefore contains the closure of that interior: the whole disk.

## Verification
The attached standalone `CHECKER.py` exactly regenerates the first several thousand offspring values for three rational sample parameters, verifies the population accounting and the exact descendant-count operator-norm formula at finite horizons, and checks boundary-series exponents by rational arithmetic. Finite checks illustrate—but cannot replace—the above asymptotic counting, Hölder, and Fredholm arguments. In particular, the claimed endpoint phase transition is proved through the infinite-series criterion, not numerical data.

## Relationship to prior work
Buckley and Seco's 2026 study of Rota universality for tree shifts analyzes Hilbert-space radii and full-spectrum regions; its verified earlier public preprint motivated the remaining peripheral eigenvalue question. The present result concerns a single unweighted tree across the entire Banach \(\ell^p\) scale, with an exact tunable critical exponent on the spectral circle. Martínez-Avendaño treats hypercyclicity of tree shifts on \(\ell^p\), whereas Budzyński, Dymek, Płaneta, and Ptak study Hilbert-space weighted tree shifts, their multipliers and decompositions. Rivera-Guasco and Martínez-Avendaño study tree shifts on Lipschitz spaces, not the present Banach sequence-space phase. The standard weighted-shift ratio criterion alone does not supply the logarithmically biased binary-tree construction or its simultaneous essential/point spectrum across all \(p\). No claim of independent priority certification is made.

## Limitations
The tree depends on the chosen threshold \(\rho>1\), though it does not depend on the subsequently chosen \(p\). The conclusions concern unweighted *backward* sums, not forward shifts, arbitrary nonhomogeneous trees or weighted \(\ell^p\) norms. The Fredholm essential spectrum is used; other definitions of essential spectrum are not asserted. Full independent validation and exhaustive historical priority review have not been performed.

## References
- J. Buckley and D. Seco, *Rota universality of shifts on trees*, arXiv:2610.40089v1, publicly posted 2026-10-29.
- R. A. Martínez-Avendaño, *Hypercyclicity of Shifts on Weighted Lp Spaces of Directed Trees*, arXiv:1805.10243.
- P. Budzyński, P. Dymek, A. Płaneta, and M. Ptak, *Weighted shifts on directed trees. Their multiplier algebras, reflexivity and decompositions*, arXiv:1702.00765.
- E. Rivera-Guasco and R. A. Martínez-Avendaño, *The forward and backward shift on the Lipschitz space of a tree*, arXiv:1906.02372.
