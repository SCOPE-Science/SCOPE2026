# Rank-dependent fourth-moment reversal on real Grassmannians

## Finding
Fix integers \(n\geq4\) and \(1\leq k<n\). Let \(P=U\operatorname{diag}(I_k,0)U^{\mathsf T}\), where \(U\) is Haar-uniform on \(O(n)\). For a nonzero real symmetric traceless matrix \(A\), write
\[
F_A(P)=\operatorname{tr}(AP),\qquad s=k(n-k),\qquad
\rho(A)=\frac{\operatorname{tr}(A^4)}{\operatorname{tr}(A^2)^2}.
\]
Set
\[
H=s(n^2+5n+18)-8n^2-12n+24,\qquad
B=n(n^2+n+2)-(5n+6)s,
\]
and
\[
C=\frac{3n(n-1)(n+2)}{s(n-3)(n-2)(n+1)(n+4)(n+6)}.
\]
Then the exact directional fourth-moment ratio is
\[
\boxed{\frac{\mathbb E F_A^4}{(\mathbb E F_A^2)^2}=C\bigl(H+4B\rho(A)\bigr).}
\]
The full sharp range is determined by
\[
\rho_{\mathrm{lo}}=\frac{n}{\lfloor n/2\rfloor\lceil n/2\rceil}-\frac3n,
\qquad
\rho_{\mathrm{hi}}=\frac{n^2-3n+3}{n(n-1)}.
\]
If \(B>0\), the sharp minimum and maximum are respectively \(C(H+4B\rho_{\mathrm{lo}})\) and \(C(H+4B\rho_{\mathrm{hi}})\). If \(B<0\), their roles reverse. If \(B=0\), the quotient is constant for all nonzero \(A\). In either strict regime all extremizers are determined by the following precise spectral rules, up to scalar multiples and orthogonal conjugation:

* The \(\rho_{\mathrm{hi}}\) spectrum has multiplicities \((1,n-1)\), with one eigenvalue equal to the negative of \(n-1\) times each other eigenvalue; equivalently \(A\) is proportional to \(vv^{\mathsf T}-I_n/n\) for a unit vector \(v\).
* The \(\rho_{\mathrm{lo}}\) spectrum has exactly two eigenvalues of opposite sign, with multiplicities \(p=\lfloor n/2\rfloor\) and \(q=\lceil n/2\rceil\), and their multiplicity-weighted sum zero; either multiplicity assignment is allowed.

In each dimension \(n\ge4\), the sign is positive for \(k=1\) and negative for the central rank \(k=\lfloor n/2\rfloor\). Thus *the maximizing and minimizing spectral geometries reverse* between low-rank and near-middle-dimensional random subspaces. In particular, at \(n=4\), the two signs already differ between ranks one and two. Complementary ranks \(k\) and \(n-k\) have identical moment ratios.

For the real normed space of coefficient functions \(\{F_A:\operatorname{tr}A=0,\ A=A^{\mathsf T}\}\), of dimension \(d=n(n+1)/2-1\), endowed with its \(L^4\) norm, the exact Euclidean Banach--Mazur distance satisfies
\[
\boxed{d_{\mathrm{BM}}^4=\frac{K_{\max}}{K_{\min}}.}
\]
The optimal Euclidean comparison norm is the Hilbert--Schmidt norm on traceless symmetric matrices. Every intermediate fourth-moment quotient is realized. In the exceptional low dimensions \(n=2\) and \(n=3\), for every admissible rank the quotient is constant, respectively \(3/2\) and \(15/7\), and the coefficient spaces are Hilbertian.

## Assumptions and scope
All matrices and test coefficients are real, \(P\) is a uniformly distributed *orthogonal* projection (not an independent-entry matrix), \(1\le k<n\), and expectations use normalized invariant probability on the real Grassmannian. Trace-zero removes the irrelevant constant observable. The quadratic expression \(\operatorname{tr}(A^2)>0\) for \(A\ne0\). No Gaussian limit or large-dimension assumption is imposed. The theorem asserts no equality of real and complex Grassmannian moment laws.

## Proof
**Exact second moment.** Orthogonal invariance implies \(\mathbb E P=(k/n)I_n\) and, on traceless symmetric coefficients,
\[
\mathbb EF_A=0,\qquad
\mathbb E F_A^2=\frac{2s}{n(n-1)(n+2)}\operatorname{tr}(A^2).
\]
For instance, for \(A=E_{11}-I_n/n\), the random variable is \(S-k/n\), where \(S=P_{11}\sim\operatorname{Beta}(k/2,(n-k)/2)\), so the displayed covariance coefficient follows from its beta variance. Conjugation invariance and irreducibility then establish it for all traceless symmetric \(A\).

**Two exact fourth-moment witnesses.** By orthogonal invariance and the fundamental theorem of symmetric polynomials, the fourth moment for any trace-zero \(A\) has the form
\[\mathbb E F_A^4=c_{22}\operatorname{tr}(A^2)^2+c_4\operatorname{tr}(A^4).\]
For \(n\ge4\), these two spectral invariants are linearly independent. It suffices to use \(A_1=E_{11}-I_n/n\) and \(A_2=\operatorname{diag}(1,-1,0,\ldots,0)\). The first gives \(F_{A_1}=S-k/n\). The second gives \(F_{A_2}=S-T\), where \(T=P_{22}\). Conditioned on the first row of \(U\), the second row is uniform on the unit sphere of its \((n-1)\)-dimensional perpendicular space. The restriction of the fixed rank-\(k\) coordinate projector to that perpendicular space has eigenvalues \(1\) with multiplicity \(k-1\), \(1-S\) with multiplicity one, and \(0\) with multiplicity \(n-k-1\). Consequently, for all nonnegative integers \(a,b\),
\[
\mathbb E[S^aT^b]=\frac{1}{((n-1)/2)_b}\sum_{j=0}^{b}\binom bj
\bigl((k-1)/2\bigr)_{b-j}(1/2)_j
\frac{(k/2)_a((n-k)/2)_j}{(n/2)_{a+j}},
\]
where \((z)_j=z(z+1)\cdots(z+j-1)\), with \((z)_0=1\). This is an exact finite beta/spherical integration formula, including the ranks one and \(n-1\). Expanding \((S-k/n)^4\) and \((S-T)^4\), then solving the two linear equations, yields
\[
c_{22}=\frac{12sH}{D},\qquad c_4=\frac{48sB}{D},\quad
D=n(n-3)(n-2)(n-1)(n+1)(n+2)(n+4)(n+6).
\]
Dividing by the square of the second moment gives the stated exact \(C(H+4B\rho)\) identity.

**Sharp spectral optimization.** For real numbers \(x_1,\ldots,x_n\) with \(\sum_i x_i=0\) and \(\sum_i x_i^2=1\), extrema of \(\sum_i x_i^4\) exist. Lagrange multipliers force each coordinate at an extremum to be a root of one cubic \(4z^3-2\lambda z-\mu=0\), hence at most three distinct values. If three distinct roots \(a,b,c\) occurred, their sum would be zero. Select one coordinate of each value. Rotating this triple while preserving its sum and squared sum also preserves its fourth-power sum, because any zero-sum real triple obeys \(a^4+b^4+c^4=(a^2+b^2+c^2)^2/2\). At least one other coordinate remains fixed when \(n\ge4\). A generic small rotation would therefore produce at least four distinct coordinate values at the same global extremum, contradicting the cubic stationarity condition. Thus every global extremizer has exactly two values. If their multiplicities are \(p\) and \(n-p\), trace zero gives
\[
\rho=\frac{n}{p(n-p)}-\frac3n.
\]
This decreases as \(p(n-p)\) increases. The largest value uses \(p=1\), and the smallest uses \(p=\lfloor n/2\rfloor\), giving both sharp endpoints and *all* equality spectra.

**Rank reversal.** The coefficient of \(\rho\) has the sign of \(B=n(n^2+n+2)-(5n+6)k(n-k)\). At rank one, \(B=(n-3)(n-2)(n+1)>0\). At the central rank it is strictly negative for every \(n\ge4\), by \(k(n-k)\ge(n^2-1)/4\). The two endpoints exchange their minimizing/maximizing roles whenever \(B\) changes sign. Orthogonal complementarity sends \(F_A\) to \(-F_A\), explaining symmetry in \(k\) and \(n-k\).

**Optimal Euclidean comparison.** The Hilbert--Schmidt quadratic form is invariant under orthogonal conjugation on the traceless symmetric coefficient space. Every other positive-definite Euclidean comparison quadratic form can be averaged under this compact group; because \(\|F_A\|_4\) is conjugation invariant, the same comparison constants survive averaging. An invariant quadratic form on the irreducible real traceless-symmetric representation is a scalar multiple of \(\operatorname{tr}(A^2)\). Therefore the optimal distortion is exactly the ratio of the maximum and minimum fourth-power radial factors, namely \(K_{\max}/K_{\min}\). Connectedness of the unit coefficient sphere gives every intermediate moment quotient. For \(n=2,3\), the identity \(\operatorname{tr}(A^4)=\operatorname{tr}(A^2)^2/2\) makes the ratio independent of direction; evaluating one rank-one projector yields \(3/2\) and \(15/7\).

## Verification
The standalone `verify.py` reconstructs both fourth-moment witness formulas symbolically using beta integrals and conditional spherical moments, verifies all displayed rational coefficients, evaluates the sharp endpoint ordering in dimensions four through ninety, checks the low-dimensional exceptions, and tests the zero-sum triple identity. An independent Gaussian-QR generation of Haar subspaces supplies 110,000 random projection diagnostics. The exact symbolic identities and the analytical spectral argument, not the finite diagnostics, establish the universal conclusions. Run `python3 verify.py` with SymPy and NumPy installed.

## Relationship to prior work
Collins and Śniady (first public version 2004) derive general polynomial Haar integration over the orthogonal group. Banica--Collins--Schlenker (first public version 2009) develop explicit two-row orthogonal polynomial integrals. These formulas provide moment-integration mechanisms but do not supply the sharp real Grassmannian fourth-moment extremizer reversal or its exact Euclidean distance. Tropp (first public version 2011) proves Gaussian comparisons for Stiefel norms, not the exact test-matrix-dependent Grassmannian kurtosis. Classical finite-sample kurtosis studies motivate the zero-sum spectral optimization, which is reconstructed above independently. The complex Hermitian Grassmannian analogue is not an implication: it has a different fourth-order coefficient and different dimension/rank transition. The present theorem concerns the real orthogonal case only.

## Limitations
No result is asserted for complex Grassmannians, nonsymmetric coefficients, higher moments, nonlinear Grassmannian observables, or non-Haar measures. The conditional statement for \(B=0\) does not assert existence of integer parameters satisfying that equation. The paper supplies no classification of such integer solutions. The exact moment formula is a consequence of general integration principles; the claimed value lies in the simultaneous sharp extrema, equality rigidity, rank reversal, and Euclidean distortion. Historical mathematical equivalence outside the inspected literature remains possible. Independent mathematical audit has not been carried out.

## References
1. B. Collins and P. Śniady, *Integration with respect to the Haar measure on unitary, orthogonal and symplectic group*, arXiv:math-ph/0402073, first posted 2004-02-26; *Communications in Mathematical Physics* **264** (2006), 773–795.
2. T. Banica, B. Collins, and J.-M. Schlenker, *On polynomial integrals over the orthogonal group*, arXiv:0910.1258, first posted 2009-10-07.
3. J. A. Tropp, *A comparison principle for functions of a uniformly random subspace*, arXiv:1102.0534, first posted 2011-02-02; *Probability Theory and Related Fields* **153** (2012), 759–769.
4. N. J. Cox, *Speaking Stata: The limits of sample skewness and kurtosis*, *Stata Journal* **10** (2010), 482–495, DOI:10.1177/1536867X1001000311.
