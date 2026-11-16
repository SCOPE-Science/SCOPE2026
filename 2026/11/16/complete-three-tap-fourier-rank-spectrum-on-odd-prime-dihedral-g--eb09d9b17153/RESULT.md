# Complete three-tap Fourier-rank spectrum on odd-prime dihedral groups

## Finding
Let \(p\ge3\) be prime and let \(G=D_{2p}=\langle r,s\mid r^p=s^2=e,\ srs=r^{-1}\rangle\). For any function \(f:G\to\mathbb C\) supported at exactly three distinct elements, all with nonzero complex coefficients, write \(T_f h(x)=\sum_{g\in G}f(g)h(g^{-1}x)\) and \(\nu(f)=\dim_{\mathbb C}\ker T_f\). Define its rank-weighted Fourier support by
\[
\sigma(f)=\sum_{\rho\in\widehat G}(\dim\rho)\,\operatorname{rank}\widehat f(\rho)=2p-\nu(f).
\]
Then every fixed three-element support \(S\subset G\) has the following **complete attainable nullity spectrum**:
\[
\{\nu(f):\operatorname{supp} f=S\}=
\begin{cases}
\{0,2,4\},&S\subset\langle r\rangle\ \text{or}\ S\subset\langle r\rangle s,\\
\{0,1,2\},&S\text{ meets both cosets of }\langle r\rangle.
\end{cases}
\]
In particular, across all three-point functions on \(G\), the Fourier-rank support values are exactly
\[
\boxed{\sigma(f)\in\{2p,2p-1,2p-2,2p-4\}},
\]
so \(2p-3\) is **impossible** and the sharp minimum is \(2p-4\). These are exact support strata, not bounds for functions with at most three nonzero coefficients. Every listed value is realized on *every* fixed support of the corresponding type.

## Assumptions and scope
Coefficients are arbitrary complex numbers, individually nonzero; they need not be equal, unimodular, real, or positive. The group order is \(2p\) for an odd prime \(p\). The rotation subgroup \(H=\langle r\rangle\) has exactly two cosets \(H\) and \(Hs\). Nullity is computed over \(\mathbb C\). For an irreducible unitary representation \(\rho\), \(\widehat f(\rho)=\sum_{g\in G}f(g)\rho(g)^*\). The rank-weighted support is not the unweighted count of nonzero Fourier blocks. The group-algebra regular representation identifies the rank of convolution with \(\sigma(f)\), independently of the chosen left/right Fourier convention.

## Proof
**1. Two-coordinate Fourier blocks.** Put \(\zeta=e^{2\pi i/p}\). Write the restrictions of \(f\) to the two cosets as Laurent polynomials
\[
A(z)=\sum_{t\in\mathbb Z_p}f(r^t)z^t,\qquad
B(z)=\sum_{t\in\mathbb Z_p}f(r^ts)z^t.
\]
The regular representation of \(G\), after Fourier transforming its two \(\mathbb Z_p\)-indexed coset coordinates, decomposes into \(p\) fibers of dimension two. One consistent Fourier convention yields, possibly after interchanging the fiber coordinates,
\[
M_j=\begin{pmatrix}
A(\zeta^j)&B(\zeta^j)\\
B(\zeta^{-j})&A(\zeta^{-j})
\end{pmatrix},\qquad j\in\mathbb Z_p.
\]
Consequently \(\nu(f)=\sum_j\dim\ker M_j\). Notice that the opposite-frequency entries are **not complex conjugates** for arbitrary complex coefficients. The direct-sum rank equals the rank-weighted Fourier support by the standard regular-representation multiplicity formula.

**2. Supports in one coset.** Suppose all three taps lie in \(H\). Then \(B=0\), and \(M_j\) is diagonal with entries \(A(\zeta^j),A(\zeta^{-j})\). If all taps lie in \(Hs\), then \(A=0\), and the fibers are off-diagonal. In either case,
\[
\nu(f)=2\#\{j\in\mathbb Z_p:P(\zeta^j)=0\},
\]
where \(P\) is the three-term polynomial formed by the nonzero tap coefficients at their three distinct exponents. Chebotarev's nonvanishing-minors theorem for the prime-order discrete Fourier matrix implies that such a polynomial vanishes at **at most two distinct** \(p\)-th roots of unity. Thus only \(\nu=0,2,4\) are possible.

All three are attained for each prescribed set of exponents \(u,v,w\): coefficients \((10,1,1)\) give no zeros by the triangle inequality; coefficients \((1,2,-3)\) give exactly the zero at \(z=1\), since \(|1+2z^{v-u}|=3\) on the unit circle forces \(z^{v-u}=1\), which for prime \(p\) forces \(z=1\); and a nonzero vector in the kernel of the two prime-DFT rows at frequencies \(j=1,2\) yields exactly two zeros. For the last construction every coefficient is nonzero because all \(2\times2\) prime Fourier minors are nonzero, and a third Fourier zero would contradict the nonvanishing \(3\times3\) minors. These constructions also work on the reflection coset.

**3. Supports meeting both cosets.** A left translation of the coefficient function multiplies its convolution operator by an invertible group-translation matrix. Hence we may assume the support has two rotations and one reflection. A further translation and a group automorphism \(r\mapsto r^d\), with \(d\not\equiv0\pmod p\), normalize the three positions to \(e,r,s\) without changing nullity or the fact that all coefficients are nonzero. Write their coefficients as \(a,b,c\in\mathbb C^*\). The corresponding fibers have determinant
\[
\det M_j=(a+b\zeta^j)(a+b\zeta^{-j})-c^2
=a^2+b^2-c^2+ab(\zeta^j+\zeta^{-j}).
\]
At frequency \(j=0\), the matrix has eigenvalues \(a+b+c\) and \(a+b-c\), so its nullity is at most one (as \(c\ne0\)). It is singular precisely when \(c=\pm(a+b)\). If this holds, then at every nonzero frequency
\[
\det M_j=ab(\zeta^j+\zeta^{-j}-2)\ne0,
\]
because \(ab\ne0\) and \(\zeta^j\ne1\). Thus a singular zero-frequency block excludes all nonzero-frequency singular blocks.

For nonzero frequencies \(j\), the values \(\zeta^j+\zeta^{-j}=2\cos(2\pi j/p)\) coincide only for opposite indices \(j\) and \(-j\). Since \(ab\ne0\), the affine determinant equation has at most one such pair. Each singular block has rank exactly one, because its off-diagonal entries are nonzero. Therefore the **entire possible nullity is \(0,1,\) or \(2\)**, and \(\nu=3\) can never occur.

For attainment on the normalized support, take \(a=b=1\). The choices \(c=3\), \(c=2\), and
\[
c=\sqrt{2+2\cos(2\pi/p)}
\]
produce nullities \(0,1,2\), respectively. The last coefficient is strictly between zero and two for every odd prime. The inverse translation/automorphism gives all three values on every mixed-coset support. Finally the first and second cases exhaust all three-element subsets of \(G\), completing the theorem.

## Verification
The accompanying standalone file `check_dihedral.py` assembles the \(2p\times2p\) complex left-regular convolution matrices directly and computes their numerical singular-value ranks; it does not use the Fourier-block formulas of the proof. For every three-element support at primes \(p=3,5,7,11\), it tests all three required levels with explicit nonzero weights. It passes all \(6{,}132\) tests. Invoke `python3 check_dihedral.py` in a Python 3 environment with NumPy. These finite precision checks corroborate the claimed configurations but are not a proof of exact nullity in arbitrary dimensions. The preceding group Fourier decomposition and prime-DFT minor theorem supply the universal argument.

## Relationship to prior work
Alagic and Russell introduced the rank-weighted Fourier-support quantity and proved a general uncertainty bound for compact groups; that definition and its regular-representation interpretation are used here, not claimed as new. Garcia, Karaali and Katz discuss prime Fourier minor rigidity and symmetry-adapted uncertainty, including Chebotarev's theorem; the full-spark input for the one-coset case is known. Huang, Huang and Lu study **unweighted undirected** cubic Cayley graphs of dihedral groups, and Al-Tarimshawy studies singularity for similarly graph-theoretic dihedral settings. Those hypotheses do not cover arbitrary complex three-tap coefficients or the exact pairwise mixed-coset nullity classification. Published calculations of **unweighted** three-tap convolution on elementary generalized dihedral groups concern coefficients all equal to one; they cannot imply the possible nullities with freely varying complex coefficients. A published exact three-point Fourier uncertainty formula for cyclic groups supplies a minimum on the one-coset portion, but not the noncommutative mixed-coset spectrum or its forbidden rank.

## Limitations
The result is specific to the exact three-point coefficient stratum, odd-prime dihedral groups, and complex coefficients. It does not assert the same spectrum for composite odd orders, additional tap positions, or different Fourier support conventions. A general Fourier block decomposition by itself does not establish the coefficient-sensitive classification. Historical equivalence with a differently normalized three-term group-algebra or weighted Cayley spectrum remains possible, pending specialist external review. No independent mathematical audit has been performed.

## References
1. G. Alagic and A. Russell, *Uncertainty Principles for Compact Groups*, arXiv:math/0608702 (first posted 2006-08-28), https://arxiv.org/abs/math/0608702 .
2. S. R. Garcia, G. Karaali and D. J. Katz, *An Improved Uncertainty Principle for Functions with Symmetry*, arXiv:1807.07648 (first posted 2018-07-19), https://arxiv.org/abs/1807.07648 .
3. X. Huang, Q. Huang and L. Lu, *Enumeration of Cubic Cayley Graphs on Dihedral Groups*, arXiv:1609.05419 (first posted 2016-09-18), https://arxiv.org/abs/1609.05419 .
4. A. Al-Tarimshawy, *Singular Graphs on which the Dihedral Group Acts Vertex Transitively*, arXiv:1810.03406 (first posted 2018-10-08), https://arxiv.org/abs/1810.03406 .
5. A. Wigderson and Y. Wigderson, *The uncertainty principle: variations on a theme*, arXiv:2006.11206 (first posted 2020-06-19), https://arxiv.org/abs/2006.11206 .
6. *Complete three-tap Fourier-rank census on elementary generalized dihedral groups*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-three-tap-fourier-rank-census-on-elementary-generalized--7d6c365ba4ff .
7. *Exact three-point Fourier uncertainty on every cyclic group*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-three-point-fourier-uncertainty-on-every-cyclic-group--cf7d7124f263 .
