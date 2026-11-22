# The first lattice-sensitive Gaussian heat-commutator twins among hyperbolic toral automorphisms

## Finding

For a hyperbolic integer matrix \(A\in\mathrm{SL}_2(\mathbb Z)\), let \(U_A\) be its Koopman unitary and \(H_t\) the isotropic Gaussian heat operator on the standard two-torus, as defined below. Set
\[
E_A(t)=\|H_tU_A-U_AH_t\|_{\mathcal S_2}^2,\qquad t>0.
\]
The two matrices
\[
A_1=\begin{pmatrix}-4&-1\\1&0\end{pmatrix},\qquad
A_2=\begin{pmatrix}-2&-3\\-1&-2\end{pmatrix}
\]
have the same characteristic polynomial \(\lambda^2+4\lambda+1\), the same squared Frobenius norm \(18\), and consequently the same pair of ordinary singular values, with squares \(9\pm4\sqrt5\). Nevertheless their Gaussian commutator energies are unequal. More precisely, as \(t\downarrow0\),
\[
E_{A_1}(t)-E_{A_2}(t)
=-\frac{2\pi}{\sqrt5\,t}
\left(e^{-\pi^2/(10t)}-e^{-\pi^2/(5t)}\right)
+O\!\left(t^{-1}e^{-3\pi^2/(10t)}\right).
\]
In particular, \(E_{A_1}(t)<E_{A_2}(t)\) for all sufficiently small positive \(t\), although their complete algebraic power asymptotic expansions at \(t=0\) coincide. Their common leading term is
\[
E_{A_j}(t)=\frac{\pi}{t}\left(1-\frac1{\sqrt5}\right)+O\!\left(t^{-1}e^{-\pi^2/(10t)}\right).
\]

The Frobenius cost \(18\) is **sharp**: whenever \(A,B\in\mathrm{SL}_2(\mathbb Z)\) are hyperbolic, \(\operatorname{tr}A=\operatorname{tr}B\), and \(\|A\|_F^2=\|B\|_F^2<18\), one has \(E_A(t)=E_B(t)\) for every \(t>0\). Thus this is the first possible separation at fixed hyperbolic trace and fixed Euclidean singular-value data, measured by integer squared Frobenius norm.

## Assumptions and scope

Use \(\mathbb T^2=\mathbb R^2/\mathbb Z^2\) with normalized Haar measure and orthonormal Fourier characters \(e_k(x)=e^{2\pi i k\cdot x}\), \(k\in\mathbb Z^2\). For \(A\in\mathrm{SL}_2(\mathbb Z)\), define \(U_Af(x)=f(A^\mathsf T x)\), so \(U_Ae_k=e_{Ak}\). The heat normalization is \(H_t=e^{t\Delta/(4\pi^2)}\), so \(H_te_k=e^{-t|k|^2}e_k\). Only \(t>0\) is considered; the squared Hilbert–Schmidt norm is finite because \(H_t\) is trace class. The hyperbolic condition is \(|\operatorname{tr}A|>2\), which is equivalent to having no eigenvalue on the complex unit circle for matrices of determinant one in two dimensions. Norms on vectors are Euclidean and \(\|A\|_F^2=\sum_{i,j}A_{ij}^2\).

## Proof

**1. Exact commutator formula.** Acting on the Fourier basis,
\[
[H_t,U_A]e_k=(e^{-t|Ak|^2}-e^{-t|k|^2})e_{Ak}.
\]
Since \(k\mapsto Ak\) permutes the integer lattice, expanding the squared norm and collecting quadratic forms gives
\[
E_A(t)=2\sum_{k\in\mathbb Z^2}e^{-2t|k|^2}
-2\sum_{k\in\mathbb Z^2}e^{-t k^\mathsf T Q_A k},\quad
Q_A=I+A^\mathsf TA.
\]
Write \(T_A=\|A\|_F^2\). The identity \(\det Q_A=1+T_A+(\det A)^2=T_A+2\) holds. By the two-dimensional Gaussian Poisson formula,
\[
E_A(t)=\frac\pi t\left(1-\frac2{\sqrt{T_A+2}}\right)
+\frac\pi t\sum_{n\in\mathbb Z^2\setminus\{0\}}e^{-\pi^2|n|^2/(2t)}
-\frac{2\pi}{t\sqrt{T_A+2}}
\sum_{n\in\mathbb Z^2\setminus\{0\}}e^{-\pi^2 n^\mathsf TQ_A^{-1}n/t}.
\]
Every sum converges absolutely for positive \(t\). At fixed \(T_A\), the first two terms are identical for all such matrices. The remaining exponentially small term depends on the **integer-lattice quadratic form**, not merely on the ordinary eigenvalues of \(Q_A\).

**2. Two explicit nonequivalent lattice forms.** For the displayed matrices,
\[
Q_{A_1}=\begin{pmatrix}18&4\\4&2\end{pmatrix},\qquad
Q_{A_2}=\begin{pmatrix}6&8\\8&14\end{pmatrix},\qquad
\det Q_{A_j}=20.
\]
Their inverse forms are
\[
n^\mathsf TQ_{A_1}^{-1}n
=\frac{(n_1-2n_2)^2+5n_2^2}{10},\qquad
n^\mathsf TQ_{A_2}^{-1}n
=\frac{7n_1^2-8n_1n_2+3n_2^2}{10}.
\]
For the first form the smallest nonzero value is \(1/10\), attained exactly at \(n=\pm(1,0)\); its next distinct positive value is \(2/5\). For the second form the smallest nonzero value is \(1/5\), attained exactly at \(n=\pm(1,1)\); its next distinct value is \(3/10\). These values follow by completing squares and checking the bounded integers left by the resulting inequalities; the exact checker also enumerates them. Insert the shortest-vector multiplicities (two in both cases) into the Poisson formula. The Euclidean-dual sum starts at exponent \(\pi^2/(2t)\), while the first omitted unequal term has exponent at least \(3\pi^2/(10t)\). The stated two-exponential expansion follows. Positive definiteness of both inverse forms supplies a fixed positive gap to the next exponent and hence the indicated uniform big-O bound for \(0<t\le1\).

**3. Exact minimality at cost \(18\).** For any four integer entries of a matrix with \(\|A\|_F^2\le18\), every entry lies in \([-4,4]\). Exhaustively impose \(\det A=1\) and \(|\operatorname{tr}A|>2\). The *complete* possible pairs \((|\operatorname{tr}A|,\|A\|_F^2)\) are
\[
(3,7),\quad(3,11),\quad(4,15),\quad(4,18).
\]
For each of the first three pairs, every resulting \(Q_A\) is integrally equivalent under a determinant-\(\pm1\) change of variables; respective representative quadratic forms, expressed as \(u x^2+2vxy+w y^2\), may be chosen as
\[
3x^2+3y^2,\qquad 2x^2+2xy+7y^2,\qquad 3x^2-2xy+6y^2.
\]
These equivalences are verified exactly by the self-contained exhaustive checker, which exhibits a unimodular change of basis for each matrix, not merely equal finite theta coefficients. Integral equivalence implies equality of the full theta sum for every \(t>0\). Consequently all same-trace, same-cost hyperbolic matrices below \(18\) have identical commutator energies. At cost \(18\) the two displayed matrices have different shortest dual lengths and thus different complete theta series; they supply the first possible separation. The same table applies to positive and negative traces.

## Verification

Run \(\texttt{python3 CHECK.py}\) with standard Python 3 (no third-party modules). The checker: (i) exhaustively lists all hyperbolic unimodular matrices with squared Frobenius cost at most \(18\); (ii) explicitly finds a unimodular change of variables for all three lower-cost trace classes; (iii) establishes both short-dual-vector multiplicities with exact integer/Fraction arithmetic; (iv) checks the next positive dual lengths; and (v) compares truncated direct Gaussian sums and their Poisson-dual expressions at ten positive parameter choices. The bounds on matrix entries make (i) genuinely exhaustive. For (iii), if \(\det Q_A\le20\), then \(Q_A^{-1}\succeq I/\det Q_A\) and a coordinate unit vector gives dual length at most \(1/2\); hence every shortest integer vector has squared Euclidean length at most \(10\), so enumeration in the checker covers all minimizers. The finite floating-point checks do **not** prove Poisson summation or the infinite series bounds; those follow from the standard analytic identity and positive definiteness.

## Relationship to prior work

The Fourier representation and spectral study of measure-preserving Koopman operators is standard; Korda–Putinar–Mezić (2017) and Colbrook–Townsend (2021) analyze Koopman spectral approximations and measures, not a fixed-metric Gaussian heat-commutator theta law. Delgado–Ruzhansky (2017) give general Schatten criteria for integral operators on manifolds and lattices, without this specific discrete dynamical comparison. Giannakis–Ourmazd–Slawinska–Zhao (2017 preprint, 2019 publication) prove commutation for a distinct *infinite-delay-limit* family of data-derived kernels; their commutation theorem does not assert a small-heat-time estimate for the isotropic Laplacian kernel, nor the sharp minimal integer witness. Classical Gaussian Poisson summation and equivalence of binary quadratic forms are used here as established tools; the new object is their combination into the first exact fixed-entropy, fixed-matrix-singular-spectrum separation of heat-commutator energies for hyperbolic toral automorphisms.

## Limitations

The claim is for the normalized flat two-torus, integer determinant-one hyperbolic automorphisms, and isotropic heat smoothing. It does not assert strict separation at *every* positive heat time, a universal classification beyond squared Frobenius cost \(18\), any inverse reconstruction theorem, or an independently validated mathematical result. The precise exponential constants depend on the chosen Euclidean flat metric and heat normalization, not only on dynamical conjugacy data. The analytic Gaussian identity is classical, and historical published quadratic-form identities may offer alternative derivations of some components; the precise minimal operator-theoretic comparison was not identified in the literature inspected.

## References

1. J. Delgado and M. Ruzhansky, *Schatten-von Neumann classes of integral operators*, arXiv:1709.06446, publicly posted 18 September 2017; https://arxiv.org/abs/1709.06446.
2. M. Korda, M. Putinar and I. Mezić, *Data-driven spectral analysis of the Koopman operator*, arXiv:1710.06532, first posted 18 October 2017; https://arxiv.org/abs/1710.06532.
3. D. Giannakis, A. Ourmazd, J. Slawinska and Z. Zhao, *Spatiotemporal pattern extraction by spectral analysis of vector-valued observables*, arXiv:1711.02798, first posted 8 November 2017; https://arxiv.org/abs/1711.02798; DOI:10.1007/s00332-019-09548-1.
4. M. J. Colbrook and A. Townsend, *Rigorous data-driven computation of spectral properties of Koopman operators for dynamical systems*, arXiv:2111.14889, first posted 29 November 2021; https://arxiv.org/abs/2111.14889.
