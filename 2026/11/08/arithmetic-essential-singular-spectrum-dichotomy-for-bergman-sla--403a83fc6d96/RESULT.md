# Arithmetic essential-singular-spectrum dichotomy for Bergman slant monomial commutators

## Finding
For every integer slant order \(k\ge2\) and distinct nonnegative integers \(m,n\), let \(B_r=W_kM_{z^r}\) be the standard \(k\)-slant Toeplitz operators on unweighted analytic Bergman space. Their commutator has the exact essential norm
\[
\|B_mB_n-B_nB_m\|_{\mathrm{ess}}=
\begin{cases}
2,&m\equiv n\pmod{k^2},\\
\sqrt2,&m\not\equiv n\pmod{k^2}.
\end{cases}
\]
More strongly, the essential spectrum of the absolute value is
\[
\sigma_{\mathrm{ess}}\bigl(|B_mB_n-B_nB_m|\bigr)=
\begin{cases}[0,2],&m\equiv n\pmod{k^2},\\
\{0,\sqrt2\},&m\not\equiv n\pmod{k^2}.
\end{cases}
\]
The two cases reflect whether the order-two slant compositions read the *same* residue class or disjoint residue classes modulo \(k^2\). The result sharpens qualitative nonessential-commutation of distinct monomial symbols to an arithmetic and quantitative invariant.

## Assumptions and scope
Let \(A^2(\mathbb D)\) have normalized area measure and orthonormal basis \(e_j(z)=\sqrt{j+1}\,z^j\), \(j\ge0\). Define \(W_ke_j=e_{j/k}\) if \(k\mid j\), and \(W_ke_j=0\) otherwise. This is a norm-one coisometry. The bounded monomial multiplication operator is \(M_{z^r}\), and \(B_r=W_kM_{z^r}\). All spectra called essential are Fredholm essential spectra (the spectrum in the Calkin algebra). The essential norm is the distance to compact operators. Index notation \(m\ne n\) is indispensable: equal symbols give a zero commutator. Both positive and zero symbol degrees are allowed.

## Proof
**1. Compact reduction to the unweighted shift.** Let \(S e_j=e_{j+1}\) denote the ordinary unilateral isometric shift on the basis, while the Bergman multiplier satisfies \(M_z e_j=\sqrt{(j+1)/(j+2)}\,e_{j+1}\). Their difference is a compact weighted shift because its weights tend to zero. For every fixed \(r\ge0\), \(M_{z^r}-S^r\) is compact. Therefore \(B_r-U_r\) is compact, where \(U_r=W_kS^r\), and
\[
[B_m,B_n]-[U_m,U_n]\quad\text{is compact}.
\]
It suffices to calculate the essential singular data of \(D=[U_m,U_n]\).

**2. Exact residue formulas.** For \(j\ge0\),
\[
U_re_j=\begin{cases} e_{(j+r)/k},&k\mid(j+r),\\0,&\text{otherwise.}\end{cases}
\]
Consequently \(A=U_mU_n\) and \(C=U_nU_m\) obey
\[
Ae_j=\begin{cases}e_{(j+n+km)/k^2},& k^2\mid j+n+km,\\0,&\text{otherwise,}\end{cases}\quad
Ce_j=\begin{cases}e_{(j+m+kn)/k^2},& k^2\mid j+m+kn,\\0,&\text{otherwise.}\end{cases}
\]
Because \(m,n\ge0\), each acts as a coordinate bijection from one infinite residue-class tail onto a cofinite output tail, annihilating all other residues. Thus \(AA^*-I\) and \(CC^*-I\) are finite rank. Their source residue classes coincide if and only if \(k^2\mid(k-1)(m-n)\), equivalently \(m\equiv n\pmod{k^2}\), since \(\gcd(k-1,k^2)=1\).

**3. Distinct residues.** If \(m\not\equiv n\pmod{k^2}\), then \(AC^*=CA^*=0\) exactly, because the initial supports are orthogonal. Hence
\[
DD^*=AA^*+CC^*=2I+F
\]
with finite-rank self-adjoint \(F\). The image of \(DD^*\) in the Calkin algebra is exactly \(2I\), so the nonzero essential singular value is \(\sqrt2\). Because \(D\) vanishes on the infinitely many other residue coordinates, zero also belongs to the essential spectrum of \(|D|\). Therefore its essential spectrum is \(\{0,\sqrt2\}\), and its essential norm is \(\sqrt2\).

**4. Identical residues.** If \(m\equiv n\pmod{k^2}\) and \(m\ne n\), both operators use the same input residue class. Upon identifying that class with \(\ell^2(\mathbb N_0)\) and discarding finitely many inputs and outputs, the two maps are integer translates by an output offset
\[
\Delta=\frac{(k-1)(m-n)}{k^2}\in\mathbb Z\setminus\{0\}.
\]
Modulo compact operators, \(D\) is thus the difference of two integer powers of the unilateral shift, restricted to that one source class; its Calkin absolute value is unitarily equivalent (on the nonzero corner) to \(|I-S^{|\Delta|}|\). In the Calkin algebra the unilateral shift has spectrum the unit circle and is unitary. Continuous functional calculus therefore gives
\[
\sigma_{\mathrm{ess}}(|I-S^{|\Delta|}|)
=\{|1-\zeta^{|\Delta|}|:|\zeta|=1\}=[0,2].
\]
The complementary infinitely many source residues contribute zero, already in this interval. Hence the asserted essential spectrum and norm \(2\) follow.

**5. Compact invariance.** The Calkin classes of \([B_m,B_n]\) and \(D\) agree. Taking absolute values and spectra in the Calkin algebra preserves this equality; so both essential-singular-spectrum conclusions also hold for the original Bergman slant operators.

## Verification
The script `check_slant.py` tests the exact residue congruence and product-coordinate formulas for a range of \(k,m,n,j\), as well as finite-grid Gram identities for disjoint residues. It supplies corroboration only: the proof of the entire essential spectrum uses compact reduction, Calkin algebra and continuous functional calculus, not finite truncation.

## Relationship to prior work
Cui, Li and Lu, *Commuting slant Toeplitz operators for polyanalytic and harmonic symbols*, arXiv:2610.09728v1, establish qualitative commutativity and finite-rank commutator rigidity but do not give the present modulo-\(k^2\) essential-singular-spectrum phase diagram in their publicly accessible abstract. Liu and Lu, *Product and Commutativity of kth-Order Slant Toeplitz Operators*, Abstract and Applied Analysis (2013), give product and commutativity formulas on Bergman spaces; these imply noncompactness of the commutator but do not state the exact two essential norms or spectral dichotomy in the accessible article text. Singh, Singh and Singh, *Algebraic and Spectral properties of slant Toeplitz and slant little Hankel Operators on weighted Bergman Space*, arXiv:2507.06546, give the normalized slant-coisometry representation and study essential spectra of individual operators, rather than the present monomial commutators.

## Limitations
The result concerns monomial *analytic* symbols; general linear combinations, coanalytic symbols, and the ordinary (nonessential) norm are not classified. An older general result about slant-symbol Calkin algebra may imply this special phase diagram without using the same wording; publication priority is not independently certified. The newest 2026 preprint's full text could not be inspected through accessible lawful sources, though its stated results and the relevant older full texts were compared. No independent audit has been performed.

## References
Cui, P., Li, R. and Lu, Y., *Commuting slant Toeplitz operators for polyanalytic and harmonic symbols*, arXiv:2610.09728v1, first public October 7, 2026.

Liu, C. and Lu, Y., *Product and Commutativity of kth-Order Slant Toeplitz Operators*, Abstract and Applied Analysis **2013**, Article 473916, DOI:10.1155/2013/473916.

Singh, O. N., Singh, M. P. and Singh, T. S., *Algebraic and Spectral properties of slant Toeplitz and slant little Hankel Operators on weighted Bergman Space*, arXiv:2507.06546v1, first public July 9, 2025.
