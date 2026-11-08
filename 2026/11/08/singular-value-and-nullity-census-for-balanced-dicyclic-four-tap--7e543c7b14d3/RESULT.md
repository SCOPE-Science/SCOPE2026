# Singular-value and nullity census for balanced dicyclic four-tap convolution

## Finding

Let \(p\ge3\) be an odd prime and let \(G=\operatorname{Dic}_p=\langle a,x: a^{2p}=1,\ x^2=a^p,\ x^{-1}ax=a^{-1}\rangle\). Select two distinct rotations and two distinct elements of the other coset:
\[
S=\{a^u,a^v,xa^c,xa^d\},\qquad u\not\equiv v,\quad c\not\equiv d\pmod {2p}.
\]
The right-convolution operator on \(\ell^2(G)\) is \((T_Sf)(g)=\sum_{h\in S}f(gh)\). Define the unsigned cyclic separations \(r,s\in\{1,\ldots,p\}\) as the shortest distances between \(u,v\) and between \(c,d\), modulo \(2p\). For \(1\le k\le p-1\), set \(C_k(t)=|\cos(\pi kt/(2p))|\).

**Complete singular-value classification.** The multiset of singular values of \(T_S\), including zeros, is precisely:

* \(4\) once and \(0\) once;
* \(2\sqrt{\mathbf 1_{2\mid r}+\mathbf 1_{2\mid s}}\) twice;
* for each odd \(k\in\{1,\ldots,p-1\}\), \(2\sqrt{C_k(r)^2+C_k(s)^2}\) four times;
* for each even \(k\in\{1,\ldots,p-1\}\), \(2(C_k(r)+C_k(s))\) twice and \(2|C_k(r)-C_k(s)|\) twice.

Every singular value therefore depends only on the pair of unsigned separations \((r,s)\), not on the locations of the four taps. Let \(\nu(T_S)=\dim_\mathbb C\ker T_S\) and define \(E=1\) if \(p\mid(r-s)\) or \(p\mid(r+s)\), and \(E=0\) otherwise. Let \(B=\mathbf1_{r=s=p}\). Then
\[
\boxed{\nu(T_S)=1+2\mathbf1_{r,s\text{ both odd}}+(p-1)E+2(p-1)B.}
\]
Among all \(\binom{2p}{2}^2\) balanced four-point supports, the *complete census* is

| Nullity | Number of supports |
|---|---:|
| \(1\) | \(p^2(p-1)(3p-7)\) |
| \(3\) | \(p^2(p-1)^2\) |
| \(p\) | \(6p^2(p-1)\) |
| \(p+2\) | \(2p^2(p-1)\) |
| \(3p\) | \(p^2\) |

For \(p=3\), the rows for nullity \(3\) and \(p\) are added together. These counts exhaust all supports and all attainable nullities.

**Sharp stability extrema.** Define the visible condition number \(\kappa_+(T_S)=\sigma_{\max}(T_S)/\sigma_{\min}^{+}(T_S)\), using the least strictly positive singular value. Then
\[
\boxed{1\le\kappa_+(T_S)\le\frac{2}{1-\cos(\pi/p)}.}
\]
The lower equality holds *exactly* when \(r=s=p\); the upper equality holds *exactly* when precisely one of \(r,s\) equals \(p\). In particular the worst visible condition number grows as \(4p^2/\pi^2\), and its optimizers include supports with minimal nullity one.

## Assumptions and scope

All Fourier transforms are unnormalized in the group algebra; all singular values refer to counting-measure \(\ell^2(G)\). The taps are unweighted with coefficient one. The two elements in each coset must be distinct; the identity rotation is permitted. The group \(G\) has order \(4p\), and the result is for odd prime \(p\ge3\) (not arbitrary odd composite parameters). The matrix need not be normal or self-adjoint; the visible condition number is not an inverse condition number on the full space, because a zero singular value always occurs.

## Proof

**1. Irreducibles and singular blocks.** The four one-dimensional characters are determined by \(\chi(a)=\epsilon\in\{\pm1\}\) and \(\chi(x)=\eta\), where \(\eta^2=\epsilon^p\). For \(\epsilon=1\) the two character sums are \(2\pm2\), giving singular values \(4,0\). For \(\epsilon=-1\), the sums are \(\alpha\pm i\beta\), where \(\alpha=(-1)^u+(-1)^v\) and \(\beta=(-1)^c+(-1)^d\). Both have modulus \(2\sqrt{\mathbf1_{2\mid r}+\mathbf1_{2\mid s}}\).

For each \(k=1,\ldots,p-1\), write \(z=e^{\pi i/p}\) and use the two-dimensional unitary representation
\[
\rho_k(a)=\begin{pmatrix}z^k&0\\0&z^{-k}\end{pmatrix},\qquad
\rho_k(x)=\begin{pmatrix}0&(-1)^k\\1&0\end{pmatrix}.
\]
These satisfy all defining relations. They are pairwise inequivalent, and the dimension sum \(4+\sum_{k=1}^{p-1}2^2=4p\) proves completeness. The Fourier matrix of the four taps is
\[
M_k=\sum_{h\in S}\rho_k(h)=
\begin{pmatrix}A_k&(-1)^k\overline{B_k}\\ B_k&\overline{A_k}\end{pmatrix},\quad
A_k=z^{ku}+z^{kv},\quad B_k=z^{kc}+z^{kd}.
\]
The magnitudes are \(|A_k|=2C_k(r)\) and \(|B_k|=2C_k(s)\). When \(k\) is odd, \(M_k^*M_k=(|A_k|^2+|B_k|^2)I_2\), so the two singular values are equal. When \(k\) is even, the eigenvalues of \(M_k^*M_k\) are \((|A_k|\pm|B_k|)^2\). In the regular representation each \(M_k\) occurs twice. This yields every listed singular value with its multiplicity.

**2. Zero sectors.** When \(k\) is odd and \(1\le k<p\), the equation \(A_k=0\) is \(k(v-u)\equiv p\pmod {2p}\). Since \(\gcd(k,2p)=1\), it holds exactly when \(r=p\); likewise \(B_k=0\iff s=p\). Thus all \((p-1)/2\) odd blocks vanish in both dimensions exactly when \(r=s=p\), contributing \(2(p-1)\) regular-representation kernel dimensions. For even \(k=2j\) the two magnitudes agree exactly when \(j(r-s)\equiv0\pmod p\) or \(j(r+s)\equiv0\pmod p\). Since \(j\not\equiv0\pmod p\), this holds exactly when \(E=1\). A vanishing small singular value in each even block gives \(p-1\) kernel dimensions. The other one-dimensional characters contribute two more zeros precisely when both \(r,s\) are odd. Adding the unavoidable trivial zero gives the nullity formula.

**3. Exhaustive support census.** For each unsigned separation \(t<p\) on the \(2p\)-cycle there are \(2p\) unordered pairs; separation \(p\) has \(p\) pairs. Consequently the entire weighted ordered-separation space has size \(p^2(2p-1)^2\). In the region \(r,s<p\), the equation \(E=1\) specifies \(s=r\) or \(s=p-r\), two distinct choices for every \(r\); its total weight is \(8p^2(p-1)\). Exactly \((p-1)/2\) of these ordered separation pairs have both separations odd, all on the diagonal, giving weight \(2p^2(p-1)\). The unique point \((p,p)\) has weight \(p^2\). The total weight of ordered pairs with both separations odd is \(p^4\): each coset has \(p^2\) unordered pairs of odd separation. Therefore the nonresonant, both-odd class has weight \(p^4-2p^2(p-1)-p^2=p^2(p-1)^2\), while the remaining nonresonant class has weight \(p^2(p-1)(3p-7)\). Subtracting the both-odd portion of the nonexceptional resonance gives the other two rows. The five weights sum to \(p^2(2p-1)^2\), as required.

**4. Sharp nonzero singular values.** The largest singular value equals \(4\), because the constant character gives \(4\) and the triangle inequality \(\|T_S\|\le4\) is sharp. Put \(h=(p-1)/2\). For even \(k\), every \(C_k(t)\) lies in the strictly decreasing set \(\{\cos(\pi j/p):0\le j\le h\}\). The smallest positive difference between two numbers in this set is \(1-\cos(\pi/p)\), uniquely at its first two entries: consecutive differences are \(2\sin((2j+1)\pi/(2p))\sin(\pi/(2p))\), increasing over the stated range. Thus any nonzero smaller even-block singular value is at least \(2(1-\cos(\pi/p))\). The larger even-block value is at least \(4\sin(\pi/(2p))\), and any nonzero odd-block value is at least \(2\sin(\pi/(2p))\), both no smaller than \(2(1-\cos(\pi/p))\) for \(p\ge3\). The nonzero one-dimensional singular values are at least \(2\).

If precisely one separation equals \(p\), choose even \(k=2j\), with \(1\le j\le h\), satisfying \(jt\equiv\pm1\pmod p\) for the other separation \(t\). Then the smaller singular value is \(2(1-\cos(\pi/p))\). If neither separation equals \(p\), the first entry of the cosine set cannot occur in an even block, and odd blocks exceed the bound; if both equal \(p\), all nonzero singular values are \(4\). Hence the asserted upper equality criterion is exact. Finally, if at least one separation is not \(p\), the \(k=1\) odd block is nonzero with singular value strictly below \(4\), so \(\kappa_+>1\); whereas \(r=s=p\) has only nonzero singular values \(4\). This proves both sharp extrema.

## Verification

Run `python verify_dicyclic.py` with Python 3 and NumPy. The standalone checker constructs the exact integer regular-representation convolution matrix, verifies ranks by elimination modulo the prime \(1000003\), compares its singular values with the complete Fourier formula, and exhausts all \(225\) supports at \(p=3\) and all \(2025\) supports at \(p=5\). It also tests \(200\) reproducibly selected supports at \(p=7\). The modular rank calculations alone are finite checks, not proofs of ranks over \(\mathbb C\); the all-prime derivation above establishes the theorem. Both zero and positive spectral endpoints are checked.

## Relationship to prior work

Arezoomand and Taeri's 2013 Fourier block decomposition of Cayley digraphs, especially their cyclic-index-two characteristic-polynomial formula (Corollary 9), supplies a general eigenvalue framework. The present claim does not present finite-group block diagonalization as new. It instead determines *singular* values of potentially nonnormal balanced dicyclic convolutions, performs an all-support nullity census, and solves two sharp condition-number extremal problems with equality classifications. Characteristic polynomials by themselves do not specify singular values. Ghorbani's 2015 analysis concerns eigenvalues of normal edge-transitive Cayley graphs; the full article could not be inspected here, so wider historical coverage remains a risk. The published general dihedral and three-tap convolution classifications are related but do not include the projective odd-frequency dicyclic blocks.

## Limitations

Only odd prime dicyclic parameters and unit-coefficient balanced four-tap supports are treated. The spectral formula applies to a nonnormal convolution matrix, and its positive condition number concerns the recoverable subspace, not an inverse of the singular full operator. Other generator distributions, general odd composite parameters, perturbed weights, and arbitrary generalized dicyclic groups are not covered. The originality assessment is bounded by the retrieved literature and is not a proof of priority; independent mathematical validation has not occurred.

## References

1. M. Arezoomand and B. Taeri, *On the Characteristic Polynomial of n-Cayley Digraphs*, Electronic Journal of Combinatorics 20(3) (2013), P57, DOI: 10.37236/3105, first published 2013-10-07. Corollary 9 and the representation block discussion: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i3p57/pdf/
2. M. Ghorbani, *On the eigenvalues of normal edge-transitive Cayley graphs*, Bulletin of the Iranian Mathematical Society 41(1) (2015), 101–107. Related dicyclic eigenvalues; full text not inspected.
3. X. Liu and S. Zhou, *Eigenvalues of Cayley Graphs*, Electronic Journal of Combinatorics 29(2) (2022), P2.9, DOI: 10.37236/8569, Section 6.5 and bibliography reference [158]. Survey background, not used to establish the archive source date.
