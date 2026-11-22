# Complete integral Smith invariants of cyclic GCD-difference matrices at squarefree moduli

## Finding
For each squarefree integer \(N\ge2\), index a symmetric integer matrix \(G_N\) by \(a,b\in\mathbb Z/N\mathbb Z\), with
\[
(G_N)_{a,b}=\gcd(a-b,N),\qquad \gcd(0,N)=N.
\]
Here is a finite, explicit prescription for its **entire integral Smith normal form**, for every squarefree \(N\), without computing any minors of the large matrix.

For a prime \(p\), form the multiset of exactly \(p\) positive integers
\[
\mathcal B_p=\{1\}\uplus\{p-1\}^{\uplus(p-2)}\uplus\{(p-1)(2p-1)\}.
\]
In particular \(\mathcal B_2=\{1,3\}\). Form the multiset of \(N\) products
\[
\mathcal B_N=\left\{\prod_{p\mid N}b_p:\ b_p\in\mathcal B_p\ \text{with multiplicities}\right\}.
\]
For every prime \(\ell\) dividing a member of \(\mathcal B_N\), sort the \(N\) valuations \(\nu_\ell(b)\), \(b\in\mathcal B_N\), as \(e_{\ell,1}\le\cdots\le e_{\ell,N}\), and set
\[
d_i=\prod_{\ell}\ell^{e_{\ell,i}}\quad(1\le i\le N).
\]
Then \(d_1\mid d_2\mid\cdots\mid d_N\), and the integral Smith normal form of \(G_N\) is exactly \(\operatorname{diag}(d_1,\ldots,d_N)\). In particular, its cokernel is \(\bigoplus_{i=1}^{N}\mathbb Z/d_i\mathbb Z\).

A sharp arithmetic consequence concerns the least number \(\mu(N)\) of generators of this finite cokernel:
\[
\boxed{\mu(N)=\begin{cases}
N-1,&N\text{ odd},\\
1,&N=2,\\
N-1,&N=2M>2\text{ and every prime }p\mid M\text{ satisfies }p\equiv1\pmod3,\\
N-2,&N=2M>2\text{ otherwise}.
\end{cases}}
\]
Thus among even squarefree orders the generator number has a strict dichotomy detected by the residue classes of all odd prime divisors modulo three.

For any rational prime \(\ell\), the rank of \(G_N\) modulo \(\ell\) is the multiplicative formula
\[
\operatorname{rank}_{\mathbb F_\ell}(G_N)=\prod_{p\mid N}r_{p,\ell},\qquad
r_{p,\ell}=\begin{cases}
1,&\ell\mid(p-1),\\
p-1,&\ell\mid(2p-1),\\
p,&\ell\nmid(p-1)(2p-1).
\end{cases}
\]
The conditions in the first two branches are mutually exclusive. Finally,
\[
\det G_N=\prod_{p\mid N}\bigl((p-1)^{p-1}(2p-1)\bigr)^{N/p}>0.
\]

## Assumptions and scope
The modulus \(N\) is **squarefree and at least two**, including primes and even squarefree integers. All computations are over \(\mathbb Z\), not merely over a field. Multiplicities in each local multiset are essential; in particular the repeated entry \(p-1\) occurs exactly \(p-2\) times, not \(p-1\) times. The prime \(\ell\) used in Smith valuations or modular ranks need not divide \(N\).

## Proof
**1. Prime matrix.** If \(N=p\) is prime, the diagonal entries of \(G_p\) are \(p\) and its off-diagonal entries are one. Writing \(a=p-1\) and \(J_p\) for the all-ones matrix, \(G_p=aI_p+J_p\). Every minor of size \(r\) with \(1\le r<p\) is divisible by \(a^{r-1}\): expand the determinant multilinearly in the columns of \(aI+J\); a contribution with two columns from \(J\) vanishes because those columns are equal, while a nonzero contribution contains at least \(r-1\) factors \(a\). This also covers determinants of minors using different row and column index sets.

For each \(1\le r<p\), choose rows indexed by \(0,1,\ldots,r-1\) and columns indexed by \(1,2,\ldots,r\). The chosen row and column sets overlap in exactly \(r-1\) indices. Subtract the unmatched row from every other row; the \(r-1\) resulting rows have a single \(a\) on their matching column and zero elsewhere. Expansion along the unmatched row therefore gives a determinant \(\pm a^{r-1}\). Consequently the greatest common divisor of all \(r\)-minors is exactly \(\Delta_r=a^{r-1}\) for \(1\le r<p\).

The vector of all ones is an eigenvector of \(G_p\) with eigenvalue \(a+p=2p-1\). Every vector with coordinate sum zero is an eigenvector with eigenvalue \(a\), yielding \(\Delta_p=\det G_p=a^{p-1}(a+p)\). By determinantal divisors, the Smith factors \(\Delta_r/\Delta_{r-1}\) (with \(\Delta_0=1\)) are precisely \(1\), \(a\) repeated \(p-2\) times, and \(a(a+p)\). This proves the stated local multiset, including \(p=2\).

**2. Squarefree tensor structure.** For squarefree \(N\), the Chinese remainder theorem identifies \(\mathbb Z/N\mathbb Z\) as the product of the residue fields \(\mathbb Z/p\mathbb Z\) over \(p\mid N\). Because \(N\) is squarefree,
\[
\gcd(a-b,N)=\prod_{p\mid N}\gcd(a-b,p).
\]
After the same permutation of rows and columns, \(G_N\) is the Kronecker tensor product \(\bigotimes_{p\mid N}G_p\). For each local Smith form choose unimodular integer matrices \(U_p,V_p\) satisfying \(U_pG_pV_p=\operatorname{diag}(\mathcal B_p)\). Tensoring these transformations gives unimodular integer transformations (their determinants remain \(\pm1\)) and takes \(G_N\) to a diagonal matrix whose entries form exactly \(\mathcal B_N\).

**3. Integral invariant-factor alignment.** The cokernel of a diagonal matrix with positive entries \(b_1,\ldots,b_N\) is \(\bigoplus_j\mathbb Z/b_j\mathbb Z\). For each prime \(\ell\), its \(\ell\)-primary part is determined by the multiset of exponents \(\{\nu_\ell(b_j)\}\). Sorting these exponents and aligning their positions over all primes constructs the uniquely determined invariant factors \(d_1\mid\cdots\mid d_N\). This proves the full Smith prescription. Taking determinants of the tensor product gives \(\det(A\otimes B)=\det(A)^{\dim B}\det(B)^{\dim A}\), proving the displayed positive determinant formula.

**4. Modular ranks.** For a prime \(\ell\), \(G_p=(p-1)I_p+J_p\) has rank one if \(\ell\mid(p-1)\). Otherwise \(p-1\) is invertible: if \(\ell\mid(2p-1)\) its one-dimensional constant direction is the kernel and its rank is \(p-1\); in all other cases it is invertible. When \(\ell\mid p\) the matrix is still invertible, because \(p-1\) is nonzero and \(J_p\) has square zero over \(\mathbb F_\ell\). The two exceptional divisibility conditions cannot coincide since \(\gcd(p-1,2p-1)=1\). Ranks of tensor products over fields multiply.

**5. Sharp generator count.** Since the matrix is nonsingular over \(\mathbb Q\), the minimal number of generators of its finite cokernel is
\[
\mu(N)=N-\min_{\ell\ \mathrm{prime}}\operatorname{rank}_{\mathbb F_\ell}(G_N).
\]
For odd squarefree \(N\), every local factor has rank one modulo two, so the product rank is one; a nonsingular integer matrix reduced modulo a prime cannot have rank zero here because all entries of \(G_N\) include the unit \(\gcd(1,N)=1\). Hence \(\mu(N)=N-1\).

For \(N=2M>2\) with \(M\) odd, the factor at \(p=2\) has rank two modulo two, while every odd-prime factor has rank one; thus the total rank modulo two is exactly two. A rank-one reduction at a different prime \(\ell\) is possible only if the \(p=2\) factor has rank one, forcing \(\ell=3\). Modulo three, an odd-prime local factor has rank one exactly when its prime is \(1\pmod3\); it has rank three for \(p=3\), and rank \(p-1\ge4\) when \(p\equiv2\pmod3\). Therefore the rank modulo three is one exactly when **every** odd prime factor of \(M\) is \(1\pmod3\), and is greater than two otherwise. At every other prime, the rank contributed by \(p=2\) is two, so rank at least two. These observations establish the claimed dichotomy. The remaining case \(N=2\) has local Smith form \(\operatorname{diag}(1,3)\) and \(\mu(2)=1\).

## Verification
The attached standalone program `verify_gcd_snf.py` reconstructs the integer matrices directly, computes determinants with exact fraction-free elimination, independently checks modular ranks by Gaussian elimination over finite fields, and exhaustively calculates determinantal divisors for \(N=2,3,5,6\). It also compares the published Smith prescription against direct integer Smith-form calculations at \(N=10,14,15,21,22\) when SymPy is available; these optional comparisons are not premises of the proof. The proof above applies to **every** squarefree modulus and does not extrapolate from these finite tests.

For example the invariant factors of \(G_6\) are \((1,1,2,6,30,30)\). The least generator counts for \(N=10,14,21,22\) are respectively \(8,13,20,20\), illustrating both sides of the even-modulus dichotomy.

## Relationship to prior work
Integral circulant (GCD) graphs are a well-established framework. Sander and Sander, arXiv:1112.3205 (first public version December 14, 2011), and arXiv:1205.4603 (May 21, 2012), work with adjacency matrices selected by **sets** of allowed values of \(\gcd(a-b,N)\), primarily studying spectral graph energy. The matrix here instead uses the **numerical GCD itself as every matrix entry**, includes its diagonal, and asks for integral Smith invariant factors, which are not determined by ordinary spectral data. Known analyses of Ramanujan-sum convolution matrices concern a different kernel and do not furnish this Smith prescription by a direct specialization. The local rank-one Smith calculation, the CRT tensor argument and the general theory of Smith normal form are classical methods; novelty is limited to their exact arithmetic combination and resulting whole-family classification.

## Limitations
The result does not determine Smith forms at nonsquarefree moduli; the multiplicative identity for GCD entries used here is specific to coprime CRT factors, not to prime powers individually. A direct statement of this classification could exist in older arithmetic-matrix literature not surfaced by the inspected searches. No claim about independent validation is made, and the theorem is not a new general Smith-form algorithm for arbitrary circulants.

## References
1. J. W. Sander and T. Sander, *Integral circulant graphs of prime power order with maximal energy*, arXiv:1112.3205, first public version December 14, 2011. https://arxiv.org/abs/1112.3205
2. J. W. Sander and T. Sander, *The maximal energy of classes of integral circulant graphs*, arXiv:1205.4603, first public version May 21, 2012. https://arxiv.org/abs/1205.4603
3. J. W. Sander, *Integral circulant Ramanujan graphs via multiplicativity and ultrafriable integers*, Linear Algebra Appl. 477 (2015), 21–41, DOI:10.1016/j.laa.2015.03.012. Background on GCD-defined circulants and spectral questions.
