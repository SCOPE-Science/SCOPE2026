# Arithmetic nullity and exact three-tap support census on dicyclic groups

## Finding
For each integer \(n\geq2\), consider the dicyclic group
\[
G=\operatorname{Dic}_n=\langle x,y\mid x^{2n}=1,\ y^2=x^n,\ yxy^{-1}=x^{-1}\rangle,
\qquad |G|=4n.
\]
For every three-element subset \(S\subset G\) with distinct elements and unit coefficients, define the complex left-convolution operator
\[
T_Sf(g)=\sum_{s\in S}f(s^{-1}g),\qquad
\nu(S)=\dim_{\mathbb C}\ker T_S.
\]
The following exhaustive classification holds; left translation of a support does not change its nullity.

**Single coset.** Suppose \(S\) is contained in one of the two cosets of \(H=\langle x\rangle\). After left translation write \(S=\{1,x^a,x^b\}\), where \(a,b\in\{1,\ldots,2n-1\}\) and \(a\ne b\). Put \(d=\gcd(a,b,2n)\) and \(M=2n/d\). Then
\[
\nu(S)=
\begin{cases}
4d,&3\mid M\text{ and }\{a/d\bmod3,b/d\bmod3\}=\{1,2\},\\
0,&\text{otherwise}.
\end{cases}
\]

**Mixed cosets.** Suppose two points of \(S\) lie in one coset of \(H\), and the remaining point lies in the other. After left translation write \(S=\{1,x^a,x^b y\}\), where \(1\le a<2n\) and \(0\le b<2n\). Put \(d=\gcd(a,n)\). Then
\[
\nu(S)=\begin{cases}2d,&3\mid n/d,\\0,&\text{otherwise}.\end{cases}
\]
In particular, the mixed-coset nullity does not depend on the location of the singleton point.

For every divisor \(d\mid n\) with \(3\mid n/d\), **exactly** \(8n^2\varphi(n/d)\) mixed-coset supports have nullity \(2d\). For every divisor \(d\mid2n\) with \(3\mid M=2n/d\), **exactly**
\[
\boxed{\frac{4nM^2}{27}\prod_{\substack{p\mid M\\p\ne3}}\left(1-p^{-2}\right)}
\]
single-coset supports have nullity \(4d\). The products range over distinct primes and the empty product is one. When numerical nullity values coincide between different divisor families, their multiplicities are added. All remaining \(\binom{4n}{3}\) supports have nullity zero.

Writing \(v=v_3(n)\), the **total number of singular supports** is
\[
\boxed{8n^3(1-3^{-v})+\frac{2n^3}{3}(1-3^{-2v})}.
\]
Consequently every three-tap convolution is invertible if and only if \(3\nmid n\). If \(3\mid n\), then the sharp maximum nullity is
\[
\boxed{\max_{|S|=3}\nu(S)=\frac{8n}{3}=\frac23|G|},
\]
attained precisely at the \(4n/3\) left cosets of the unique order-three subgroup of \(H\). These are exactly the maximizing supports.

## Assumptions and scope
All assertions concern \(n\in\mathbb Z\), \(n\ge2\), and unordered subsets of **three distinct group elements**, each with coefficient exactly one. The coefficient field is \(\mathbb C\); the convolution need not be self-adjoint, and supports need not be inverse-closed, generating, or disjoint from the identity. The totient function is \(\varphi\), and \(v_3(n)\) is the exponent of three in \(n\). No claim is made for repeated or weighted taps, other coefficient characteristics, or generalized dicyclic groups with a noncyclic index-two subgroup.

## Proof
**1. A complete two-dimensional Fourier-fiber decomposition.** Let \(N=2n\) and \(\zeta=e^{2\pi i/N}\). Write \(e_g\) for the standard basis of the complex group algebra. For each \(0\le k<N\), define
\[
u_k=\sum_{j=0}^{N-1}\zeta^{-kj}e_{x^j},\qquad
v_k=\sum_{j=0}^{N-1}\zeta^{kj}e_{x^j y}.
\]
The \(N\) two-dimensional spaces \(V_k=\operatorname{span}\{u_k,v_k\}\) are linearly independent and together exhaust \(\mathbb C[G]\). Left translation by \(x\) and \(y\) preserves each space, with matrices
\[
L_x\big|_{V_k}=\begin{pmatrix}\zeta^k&0\\0&\zeta^{-k}\end{pmatrix},
\qquad
L_y\big|_{V_k}=\begin{pmatrix}0&(-1)^k\\1&0\end{pmatrix}.
\]
Indeed, \(yx^j=x^{-j}y\) and \(yx^jy=x^{n-j}\), and \(\zeta^{kn}=(-1)^k\). These formulas directly verify all three defining group relations and supply a full (possibly reducible) Fourier decomposition of dimension \(2N=4n\). Since \(T_S=\sum_{s\in S}L_s\) on coefficient vectors, its nullity equals the sum of block nullities. For every \(t\in G\), the supports \(S\) and \(tS\) have equal nullity because \(T_{tS}=L_tT_S\).

**2. Single-coset classification.** In the normalized single-coset case, the block is
\[
\operatorname{diag}(F_k,\overline{F_k}),\qquad F_k=1+\zeta^{ka}+\zeta^{kb}.
\]
A sum of three unit complex numbers is zero exactly when the three terms are the three distinct cube roots of unity. Set \(d=\gcd(a,b,N)\), \(M=N/d\), \(\alpha=a/d\), \(\beta=b/d\); then \(\gcd(\alpha,\beta,M)=1\). If \(F_k=0\), the two exponents \(\alpha k\) and \(\beta k\), modulo \(M\), equal \(M/3\) and \(2M/3\) in either order. Necessarily \(3\mid M\), and Bezout's identity for \(\alpha,\beta,M\) forces \(k\equiv M/3\) or \(2M/3\pmod M\). For either of these congruences to give the prescribed opposite cube roots, \(\{\alpha\bmod3,\beta\bmod3\}=\{1,2\}\) is necessary and sufficient. Each solution modulo \(M\) has \(d\) lifts modulo \(N\). Therefore precisely \(2d\) blocks are zero, each contributing two kernel dimensions. This proves the single-coset nullity formula.

**3. Mixed-coset classification.** For \(S=\{1,x^a,x^b y\}\), the block is
\[
B_k=\begin{pmatrix}
1+\zeta^{ka}&(-1)^k\zeta^{kb}\\
\zeta^{-kb}&1+\zeta^{-ka}
\end{pmatrix},\qquad
\det B_k=2+2\cos\left(\frac{2\pi ka}{2n}\right)-(-1)^k.
\]
For odd \(k\), the determinant is at least one and never vanishes. For even \(k=2r\), it vanishes exactly when the phase \(\zeta^{ka}\) is a primitive cube root of unity, namely
\[
ar\equiv n/3\quad\text{or}\quad ar\equiv2n/3\pmod n.
\]
For \(d=\gcd(a,n)\), these congruences have solutions if and only if \(3\mid n/d\), in which case each has exactly \(d\) solutions modulo \(n\). Thus exactly \(2d\) Fourier blocks are singular. Their off-diagonal entries never vanish, so each singular block has rank one and contributes exactly one null direction. The claimed mixed-coset nullity follows and is independent of \(b\).

**4. Exact support counts.** A mixed support has a unique pair-containing coset. For each divisor \(d\mid n\), the number of nonzero differences \(a\pmod{2n}\) satisfying \(\gcd(a,n)=d\) is \(2\varphi(n/d)\). Choose which of the two cosets contains the pair, choose its first point in \(2n\) ways, its difference in the stated number of ways, and the singleton in \(2n\) ways; divide by two for exchanging the pair. The count is \(8n^2\varphi(n/d)\).

For a single-coset support, fix \(d\mid N\), \(M=N/d\) divisible by three. The number of **ordered** primitive pairs \((\alpha,\beta)\pmod M\) with \(\gcd(\alpha,\beta,M)=1\) and opposite nonzero residues modulo three is
\[
2\left(\frac M3\right)^2\prod_{\substack{p\mid M\\p\ne3}}(1-p^{-2}).
\]
This follows from the Chinese remainder theorem: the two allowed ordered residue pairs modulo three are \((1,2)\) and \((2,1)\), while at each other prime one excludes the simultaneous zero residue. Choose a starting point in one of the two cosets (\(2N\) choices total) and divide by six, the number of permutations of three distinct points. This gives \(2NM^2/27\) times the displayed Euler product, which equals \(4nM^2/27\) times that product. Every support is counted exactly once at its gcd class.

**5. Total and sharp extremizers.** For \(v=v_3(n)\), the totient identity gives
\[
\sum_{\substack{m\mid n\\3\mid m}}\varphi(m)=n(1-3^{-v}).
\]
The single-coset Euler products sum multiplicatively over divisors of \(2n\). At primes \(p\ne3\), the local sum telescopes to the full squared prime power; at three, the positive-exponent sum is \(\sum_{j=1}^v3^{2j}=9(9^v-1)/8\). Consequently the total singular count is exactly the boxed expression, with the zero case when \(v=0\).

In the mixed family the largest possible singular nullity is \(2n/3\) (attained for \(d=n/3\)); in the single-coset family the largest is \(4(2n/3)=8n/3\), attained only for \(d=2n/3\), \(M=3\). Those three points necessarily form a left coset of the unique subgroup of order three in \(H\). There are \(4n/3\) such cosets in \(G\), proving uniqueness of the maximizer geometry and sharpness.

## Verification
`check_q.py` is a standalone Python 3 checker. It implements the defining group product and constructs the **full left-convolution matrix** for chosen supports, independently of the Fourier-fiber proof; modular Gaussian elimination over \(\mathbb F_{1000000007}\) compares the resulting nullity to the formula on 1,081 distinct sampled supports across \(2\le n\le12\). Sampling exhausts all supports for \(2\le n\le4\); it uses a fixed seeded selection for larger groups. Separately, for **every** \(2\le n\le24\), it enumerates all \(\binom{4n}{3}\) supports by the classification conditions and compares their exact multiplicities against the independent divisor/product census formula. Execute `python3 check_q.py` from the directory holding that file. The observed successful run printed `PASS 1081` and `CENSUS_PASS`. Finite-field ranks may differ from complex ranks in general, and finite tests never establish an all-\(n\) theorem; the Fourier decomposition and arithmetic argument above establish the unrestricted claim.

## Relationship to prior work
Arezoomand and Taeri (2013) give the general block-representation and characteristic-polynomial framework for Cayley digraphs, including graphs with a cyclic index-two subgroup. This fully anticipates the Fourier-block *method* and in principle yields individual spectra by substitution. The contribution here is not the block decomposition, but the explicit necessary-and-sufficient **three-tap singularity geometry for every support**, exact complex nullities, complete arithmetic all-support census, and sharp global extremizer family; those conclusions do not appear as stated in the inspected prior paper.

Abdollahi and Jazaeri (2013) classify groups for which every inverse-closed Cayley graph is integral; their coefficient and graph-symmetry assumptions and objective differ. Behajaina and Legrand (2022) study inverse-closed generalized-dicyclic Cayley graphs, focusing on integrality and other spectral properties, without the present general asymmetric three-support census. Published analyses of three-tap convolution on elementary generalized-dihedral groups and on ternary Heisenberg groups concern distinct nonisomorphic families and do not imply the dicyclic result by specialization; the shared general Fourier strategy is acknowledged. Older work on three-valent Cayley graphs potentially contains special inverse-closed instances. A stronger implicit theorem in the comprehensive group-algebra spectral literature cannot be ruled out by finite searching.

## Limitations
The formulas concern unweighted three-element supports and complex nullity. They do not determine complete eigenvalue multisets, weighted or self-adjoint variants, or all generalized dicyclic extensions. The extensive counts are proof-supported, but independent mathematical auditing and comprehensive historical priority verification are not claimed. Finite modular computations are corroboration only.

## References
1. M. Arezoomand and B. Taeri, *On the Characteristic Polynomial of n-Cayley Digraphs*, Electronic Journal of Combinatorics 20(3) (2013), P57; published October 7, 2013. DOI: https://doi.org/10.37236/3105 . Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i3p57/pdf/ .
2. A. Abdollahi and M. Jazaeri, *Groups all of whose undirected Cayley graphs are integral*, arXiv:1307.5413, initially public July 20, 2013. https://arxiv.org/abs/1307.5413 .
3. A. Behajaina and J. Legrand, *On Cayley graphs over generalized dicyclic groups*, arXiv:2202.11398, initially public February 23, 2022. https://arxiv.org/abs/2202.11398 .
4. *The Structure of Cayley Graph of Generalized Quaternion Group of Valency Less than or Equal 3*, publicly posted June 30, 2025, https://www.preprints.org/frontend/manuscript/9919c10f9d44d04aa88629317c866699/download_pub .
