# Eight consecutive-site sensors are optimal on every prime square torus

## Finding
For each odd prime \(p\ge5\), eight fixed vertex sensors suffice to recover every complex signal on the Cartesian graph \(C_p\square C_p\) from finitely many iterates of the normalized four-neighbor adjacency operator, and no seven sensors suffice, even with unlimited observation times. One explicit optimal sensing set is the \(4\times2\) contiguous rectangle \(S=\{0,1,2,3\}\times\{0,1\}\). Precisely, the \(8K\) measurements
\[
\bigl\{(T^t f)(s):s\in S,\quad 0\le t<K\bigr\},\qquad K=\frac{(p+1)(p+3)}8,
\]
are injective on the full \(p^2\)-dimensional complex signal space. The result concerns fixed **vertex** measurements for this exact graph operator, not arbitrary linear sensors or generic weighted graphs.

## Assumptions and scope
Write \(\mathbb Z_p\) for the residues modulo the odd prime \(p\ge5\), with all additions taken modulo \(p\). The graph has vertices \(\mathbb Z_p^2\) and four undirected neighbors at offsets \((\pm1,0)\), \((0,\pm1)\). Its normalized adjacency operator is
\[
(Tf)(x,y)=\frac{f(x+1,y)+f(x-1,y)+f(x,y+1)+f(x,y-1)}4.
\]
This self-adjoint operator is related to the normalized graph Laplacian by \(L=I-T\). Sampling its powers (or those of \(L\)) has the same recoverability property because their eigenvalue labels are in bijection. No restriction on the Fourier support of \(f\) is assumed. Let \(r=(p-1)/2\). A sensor records the exact complex number \((T^tf)(s)\) at one fixed vertex \(s\) and at specified nonnegative integer times \(t\).

## Proof
**1. Exact spectral separation.** Write \(\zeta=e^{2\pi i/p}\) and \(\chi_{k,l}(x,y)=\zeta^{kx+ly}\). These \(p^2\) characters form a basis of eigenvectors, with eigenvalue
\[
\lambda_{k,l}=\frac{\zeta^k+\zeta^{-k}+\zeta^l+\zeta^{-l}}4.
\]
Associate to \(k\in\mathbb Z_p\) its radius \(\rho(k)=\min\{k,p-k\}\in\{0,\ldots,r\}\), where \(k\) is represented by an integer between zero and \(p-1\). Clearly \(\lambda_{k,l}\) depends only on the unordered radius pair \(\{\rho(k),\rho(l)\}\).

Conversely, suppose two unordered pairs of radii give the same eigenvalue. Their two sums of four \(p\)-th roots coincide, so the difference polynomial \(P(X)\in\mathbb Z[X]\), obtained by subtracting the corresponding four monomials (counting the zero frequency twice), has degree at most \(p-1\), satisfies \(P(\zeta)=0\), and has \(P(1)=0\). Since \(p\) is prime, the minimal polynomial of \(\zeta\) over \(\mathbb Q\) is \(\Phi_p(X)=1+X+\cdots+X^{p-1}\). Hence \(P=c\Phi_p\) for a rational constant \(c\), and \(0=P(1)=cp\) gives \(P=0\). Equality of all coefficient multiplicities recovers the same four signed frequencies, and therefore the same unordered pair of radii. There are consequently **exactly**
\[
K=\binom{r+2}{2}=\frac{(p+1)(p+3)}8
\]
distinct eigenvalues. This cyclotomic argument rules out every accidental degeneracy, including those not explained by sign and coordinate-swap symmetries.

**2. Eigenspace dimensions and the seven-sensor obstruction.** Denote by \(E_{a,b}\) the eigenspace for the unordered radii \(0\le a\le b\le r\). By the separation just proved, its Fourier basis is exactly the set of characters with \(\{\rho(k),\rho(l)\}=\{a,b\}\). Its dimension is one when \(a=b=0\); four when exactly one radius is zero or when \(a=b>0\); and eight when \(0<a<b\). For \(p\ge5\), radii \(a=1,b=2\) exist, so \(\dim E_{1,2}=8\). Any restriction map from this eigenspace to seven or fewer spatial sites has a nontrivial kernel. If \(0\ne f\in E_{1,2}\) vanishes at those sites, then \((T^tf)(s)=\lambda_{1,2}^t f(s)=0\) there for every \(t\ge0\). Thus no set of at most seven sites can recover all signals.

**3. Eight adjacent sites resolve every eigenspace.** Let
\[
S=\{0,1,2,3\}\times\{0,1\}\subset\mathbb Z_p^2.
\]
Take any \(h\in E_{a,b}\) vanishing on \(S\). Expand \(h(x,y)=\sum_{(k,l)\in F_{a,b}} c_{k,l}\zeta^{kx+ly}\), where \(F_{a,b}\) is the character set for that eigenspace. The projection of \(F_{a,b}\) onto its first coordinate has **at most four** distinct frequencies, among \(\{\pm a,\pm b\}\). Fix \(y=0\) or \(y=1\). The four equations \(h(x,y)=0\) for \(x=0,1,2,3\) form a Vandermonde system in these at most four distinct nodes \(\zeta^k\); hence for every first-coordinate frequency \(k\),
\[
\sum_{l:(k,l)\in F_{a,b}}c_{k,l}\zeta^{ly}=0\qquad (y=0,1).
\]
For each fixed \(k\), the allowed second-coordinate frequencies comprise **at most two** distinct values: either \(\{\pm b\}\) or \(\{\pm a\}\), with the singleton possibility at radius zero. The two equations at \(y=0,1\) are another Vandermonde system, so every \(c_{k,l}=0\). Thus the restriction \(E_{a,b}\to\mathbb C^S\) is injective for every spectral block, including all boundary cases \(a=0\) and \(a=b\).

**4. Temporal interpolation yields full reconstruction.** For a general signal decompose \(f=\sum_{0\le a\le b\le r}f_{a,b}\) into its mutually orthogonal spectral components. At each sensor \(s\in S\),
\[
(T^tf)(s)=\sum_{0\le a\le b\le r}\lambda_{a,b}^{\,t}\,f_{a,b}(s),\qquad t=0,1,\ldots,K-1.
\]
The \(K\times K\) temporal Vandermonde matrix is invertible because all \(K\) eigenvalues are distinct, including any zero eigenvalue. This recovers every \(f_{a,b}(s)\) at all eight sensors. The spatial Vandermonde argument of step 3 then reconstructs all Fourier coefficients within each spectral component. Hence the stated sampling map is injective. Coupled with step 2, its eight sensors are optimal. \(\square\)

## Verification
The accompanying standard-library Python checker `CHECK.py` performs exact rank calculations modulo suitable auxiliary primes containing primitive \(p\)-th roots of unity. It checks spatial eigenspace restrictions for \(p=5,7,11,13,17\), with total dimensions \(25,49,121,169,289\) respectively. For \(p=5,7,11\) it additionally builds the full finite-time sample matrix and verifies rank \(p^2\) exactly modulo the auxiliary prime. It reports `ALL_PRIME_TORUS_CHECKS_PASSED` upon success. The modular rank checks are independent finite tests, not a proof for infinitely many primes. The preceding cyclotomic and Vandermonde arguments provide the uniform proof.

## Relationship to prior work
Dynamical sampling of finite graph signals is characterized generally by the spanning properties of operator orbits and their restrictions to spectral subspaces; see Cabrelli, Cordero, Bulai, Saliani, and Molter, *Dynamical Sampling in Graph Paley--Wiener Spaces* (2026), especially its finite-graph recovery criterion. The 2026 dynamical-sampling survey by Aldroubi, Cabrelli, Krishtal, and Molter discusses the minimal number of generators for operator-orbit frames. These general criteria motivate the problem but do not themselves establish that one fixed contiguous rectangle of eight **vertex evaluation** sensors works simultaneously for every prime square torus, or prove the exact prime-dependent spectral separation needed here.

Parlangeli and Notarstefano study observability on **single** cycle and path graphs, rather than the repeated-eigenvalue Cartesian-square problem. Work on Cartesian-product **structural** observability concerns generic edge weights and is not equivalent to recoverability for the fixed, equal-weight four-neighbor operator. The numerical and analytic construction here isolates a concrete, arithmetic point-sensor design, not merely the abstract maximum-eigenspace-multiplicity criterion.

## Limitations
The theorem requires odd prime side length \(p\ge5\); the proof does not claim the same sharp sensor count for composite cycles, unequal side lengths, generic graph weights, time-dependent operators, or other measurement models. It proves exact reconstruction in exact arithmetic and, for each fixed \(p\), finite-dimensional frame stability, but does **not** give uniform noise conditioning as \(p\to\infty\), nor does it optimize the number of temporal samples. The minimal eight sensors are optimal in cardinality, not necessarily in noise stability. An independently established publication-priority judgment is not asserted.

## References
1. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter, S. Saliani, *Dynamical Sampling in Graph Paley--Wiener Spaces* (first public 2026-09-21), arXiv:2609.25472, https://arxiv.org/abs/2609.25472.
2. A. Aldroubi, C. Cabrelli, I. Krishtal, U. Molter, *Dynamical Sampling: A Survey*, La Matematica 5 (2026), article 37, https://doi.org/10.1007/s44007-026-00215-y.
3. D. Parlangeli, G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556, https://arxiv.org/abs/1109.3556.
4. M. Doostmohammadian, *Recovering the Structural Observability of Composite Networks via Cartesian Product*, arXiv:2001.04699, https://arxiv.org/abs/2001.04699.
5. C. Cabrelli, U. Molter, V. Paternostro, F. Philipp, *Dynamical Sampling on Finite Index Sets*, arXiv:1702.03384, https://arxiv.org/abs/1702.03384.
