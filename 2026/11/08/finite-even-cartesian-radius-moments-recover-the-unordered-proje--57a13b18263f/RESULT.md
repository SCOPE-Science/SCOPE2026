# Finite even Cartesian-radius moments recover the unordered projective spectral gaps of unitaries

## Finding

**Theorem (finite inverse determination and its exact ambiguity).** Fix an integer \(n\geq1\). Let \(U\) and \(V\) be complex unitary matrices, each acting on a nonzero complex Hilbert space of dimension at most \(n\). For any \(p\geq1\), define their \(L^p\)-Cartesian radii by
\[
\rho_p(U)=\left(\frac1{2\pi}\int_0^{2\pi}\left\|\operatorname{Re}(e^{-it}U)\right\|^p\,dt\right)^{1/p}.
\]
Pass from the eigenphases of each matrix to distinct points of the projective circle \(\mathbb R/\pi\mathbb Z\) (so phases differing by \(\pi\) are identified). Denote by \(G(U)\) the **multiset** of all positive cyclic gap lengths between these distinct points, including the unique length-\(\pi\) gap when there is only one point. Then
\[
\boxed{\bigl(\rho_{2k}(U)=\rho_{2k}(V)\text{ for }1\le k\le2n\bigr)\quad\Longleftrightarrow\quad G(U)=G(V).}
\]
In fact either condition is equivalent to \(\rho_p(U)=\rho_p(V)\) for every real \(p\ge1\). Thus just \(2n\) even Cartesian radii (orders \(2,4,\ldots,4n\)) determine all projective spectral gap **lengths and repetitions**. Their cyclic order, global phase, individual signs and eigenvalue multiplicities need not be determined.

For constructive recovery, put \(M_k=\rho_{2k}(U)^{2k}\) and let the gap lengths be \(\ell_1,\ldots,\ell_m\), where \(1\le m\le n\). The unknown quantities \(s_j=\sum_{i=1}^m\sin(j\ell_i)\) are uniquely recovered in succession from
\[
\boxed{M_k=4^{-k}\binom{2k}{k}+\frac{2}{\pi4^k}\sum_{j=1}^k\binom{2k}{k-j}\frac{s_j}{j},\quad1\le k\le2n.} \tag{1}
\]
The resulting \(2n\) sine sums are the first \(2n\) polynomial moments, in the Chebyshev basis, of the finite positive atomic measure
\[
\boxed{\mu_U=\sum_{i=1}^m \sin(\ell_i)\,\delta_{\cos\ell_i}.}\tag{2}
\]
These moments uniquely recover that measure among measures supported on at most \(n\) points in \((-1,1)\), and the atom masses divided by \(\sin(\arccos x)\) recover gap multiplicities. The degenerate one-projective-point case has \(G(U)=\{\pi\}\) and \(\mu_U=0\), and is uniquely distinguished by \(s_1=0\).

## Assumptions and scope

All matrices are finite-dimensional and unitary over \(\mathbb C\), possibly of different dimensions, with both dimensions between \(1\) and \(n\). Operator norms are Hilbert-space norms. The projective circle has circumference \(\pi\), and projective spectral points are distinct even if the original unitary eigenvalues have multiplicities or occur in antipodal pairs. A projective singleton is assigned one full-circle gap of length \(\pi\), not zero gaps. The inversion statement recovers only an **unordered** gap multiset, not the ordered spectrum. The count \(2n\) is sufficient; it is not asserted to be the minimum number of measurements.

## Proof

**1. Distance and gap formula.** Set \(S_U\subset\mathbb R/\pi\mathbb Z\) equal to the finite projective eigenphase set. Spectral calculus for the normal matrix yields
\[
\|\operatorname{Re}(e^{-it}U)\|=\max_{\alpha\in S_U}|\cos(t-\alpha)|=\cos d(t,S_U),
\]
where \(d\) is geodesic distance on the projective circle, taking values in \([0,\pi/2]\). The integrand is \(\pi\)-periodic. On a cyclic complementary gap of length \(\ell_i\), the nearest spectral point is one of its endpoints; the distance along the gap is \(\min(x,\ell_i-x)\). Consequently, for **every** real \(p\ge1\),
\[
\rho_p(U)^p=\frac2\pi\sum_{i=1}^m\int_0^{\ell_i/2}\cos^p x\,dx.\tag{3}
\]
This directly proves that equality of unordered gap multisets implies equality of the entire radius profile. It also holds for the singleton gap of length \(\pi\).

**2. Triangular inversion.** For every positive integer \(k\), the binomial identity is
\[
\cos^{2k}x=4^{-k}\left[\binom{2k}{k}+2\sum_{j=1}^k\binom{2k}{k-j}\cos(2jx)\right].
\]
Insert this into (3), integrate \(\cos(2jx)\) on \([0,\ell_i/2]\), and use \(\sum_i\ell_i=\pi\). This gives exactly (1). For the equation indexed by \(k\), the coefficient of \(s_k\) is \(2/(\pi4^k k)\), which is nonzero. Therefore the radii \(\rho_2,\rho_4,\ldots,\rho_{4n}\) determine \(s_1,\ldots,s_{2n}\) recursively, with no unspecified normalization.

**3. Recovery of a positive atomic measure.** If there is more than one distinct projective spectral point, then each gap \(0<\ell_i<\pi\), so all masses \(\sin\ell_i\) in (2) are strictly positive. For \(j\ge1\), the Chebyshev polynomials of the second kind satisfy \(\sin(j\ell)=\sin\ell\,\mathrm U_{j-1}(\cos\ell)\). Thus
\[
 s_j=\int_{-1}^{1}\mathrm U_{j-1}(x)\,d\mu_U(x),\qquad j=1,\ldots,2n.
\]
Because \(\mathrm U_j\) has degree \(j\) and leading coefficient \(2^j\), the first \(2n\) sine sums are equivalent to all power moments of degrees \(0,1,\ldots,2n-1\). Suppose two positive measures of the form (2), each with at most \(n\) distinct support points, have these same moments. Their difference is a signed measure on at most \(2n\) distinct nodes \(x_1,\ldots,x_r\). Writing its masses as \(a_1,\ldots,a_r\), we have \(\sum_{h=1}^r a_h x_h^j=0\) for every \(0\le j\le r-1\). The square Vandermonde matrix is invertible since the nodes are distinct, so every \(a_h=0\). Thus the two measures coincide. Each node \(x\in(-1,1)\) determines exactly one gap length \(\ell=\arccos x\in(0,\pi)\); the associated mass is the positive integer repetition count times \(\sin\ell\). Hence equality of measures implies equality of the full unordered gap multisets.

If \(s_1=\sum_i\sin\ell_i=0\), positivity forces there to be no gaps strictly between \(0\) and \(\pi\); since the projective spectral set is nonempty and finite, it is a singleton, and its sole gap is \(\pi\). Therefore the zero-measure case is handled as well. Combining Steps 1–3 proves both equivalences. \(\square\)

**4. Optimal information boundary (explicit obstruction).** In projective phase units \(\pi/10\), let \(U\) have four distinct eigenphases \(\{0,1,3,6\}\) and let \(V\) have four distinct eigenphases \(\{0,1,4,6\}\). Their cyclic gaps, in those units, are respectively \((1,2,3,4)\) and \((1,3,2,4)\). The multisets agree, so all their \(\rho_p\) agree by (3). However, neither a rotation nor a reflection of the projective circle changes the first cyclic gap word into the second: the dihedral orbit of \((1,2,3,4)\) consists of its four rotations and the four rotations of \((4,3,2,1)\), none of which is \((1,3,2,4)\). Therefore even the *entire* radius profile cannot recover cyclic order up to rotation and reflection. This confirms that the inverse statement reconstructs the maximal information available from this family of measurements.

## Verification

The finite-determinacy proof is the explicit triangular inversion (1), the Chebyshev moment identity and the invertible Vandermonde system, independently of any experiment. An optional standalone standard-library Python script `verify_inverse.py` checks the even-moment binomial formula against angular quadrature, checks the inverse triangular and Chebyshev transforms, and tests the noncongruent projective-gap example. Run with `python verify_inverse.py`. On the examined run it produced `PASS: 1637 numerical and algebraic consistency assertions`. This diagnostic has no role as an infinite or all-dimension proof, and finite arithmetic tolerances are only diagnostic.

## Relationship to prior work

Audeh, Kittaneh, Moradi and Sahoo introduced the integrated Cartesian \(L^p\) radius, giving general comparisons and operator inequalities (arXiv:2610.04844; first public version 2026-10-04). The published published-finding corpus result *Exact projective spectral-gap formula and optimal finite spectra for the \(L^2\)-Cartesian radius of unitaries* already evaluates the \(p=2\) unitary radius in terms of projective spectral gap lengths and optimizes it at fixed matrix dimension. These are specifically **not** claimed as new. The present statement instead proves a finite **inverse** theorem from a family of even exponents, including the explicit multiset reconstruction, repetition counts, and the exact obstruction to recovering cyclic order. The previous single-exponent formula by itself does not imply the inverse determination. Classical spectral calculus, Chebyshev polynomial identities and finite Vandermonde uniqueness supply elementary ingredients, but an identified published theorem already asserting the complete inverse classification was not found in the compared sources.

## Limitations

The projective spectral gap multiset is coarser than eigenvalue data. Even infinitely many exponent measurements do not generally recover cyclic order, a global rotation, antipodal choices or eigenvalue multiplicities. The proof requires a bound \(n\) on the number of distinct projective spectral points (matrix dimension is a sufficient such bound); it does not yield a finite-determinacy count uniform over arbitrary infinite spectra. No claim of minimality of \(2n\) is made. A broader classical result about inverse circular-distance distributions or finite atomic moments could subsume this formulation; literature search does not certify publication priority. Numerical diagnostics are not proofs.

## References

1. W. Audeh, F. Kittaneh, H. R. Moradi and S. Sahoo, *The \(L^2\)-Cartesian Numerical Radius of Hilbert Space Operators*, arXiv:2610.04844v1 (2026-10-04), https://arxiv.org/abs/2610.04844 ; version 2 including the \(L^p\) family: https://arxiv.org/html/2610.04844v2 .
2. *Exact projective spectral-gap formula and optimal finite spectra for the \(L^2\)-Cartesian radius of unitaries*, published-finding corpus research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-projective-spectral-gap-formula-and-optimal-finite-spectra--f6644dc86b39 .
3. Standard unitary spectral theorem, Chebyshev-polynomial identity, and finite Vandermonde interpolation uniqueness (proofs provided above for the needed special cases).
