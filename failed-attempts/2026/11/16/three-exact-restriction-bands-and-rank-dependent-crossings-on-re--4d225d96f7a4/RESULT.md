# Three exact restriction bands and rank-dependent crossings on real Grassmannian coordinate caps

## Finding

Let \(n\ge4\) and \(1\le k\le n-1\) be integers. On the real Grassmannian of rank-\(k\) orthogonal projectors \(P\in\mathbb R^{n\times n}\) with normalized Haar measure, put
\[
V_{n,k}=\{f_A(P)=\operatorname{tr}(AP): A=A^{\mathsf T},\ \operatorname{tr}A=0\},\quad
\Omega_t=\{P:P_{11}\ge t\},\quad 0<t<1.
\]
The positive restriction/concentration operator on \(V_{n,k}\), defined by
\(\langle T_t f,g\rangle_{L^2}=\int_{\Omega_t} f\overline g\,d\mu\), has precisely three eigenvalue branches, with possible numerical coincidences. Their multiplicities are \(1\), \(n-1\), and \(n(n-1)/2-1\), respectively, called axial, cross, and tangential.

Write \(a=k/2\), \(b=(n-k)/2\), \(B=B(a,b)\), and
\[
\rho(x)=\frac{x^{a-1}(1-x)^{b-1}}{B},\qquad c=\frac{2k(n-k)}{n(n-1)(n+2)}.
\]
All three eigenvalues are **explicit positive incomplete-Beta integrals**
\[
\lambda_J(t)=\int_t^1 W_J(x)\rho(x)\,dx,
\quad J\in\{A,C,T\},
\]
where
\[
W_A(x)=\frac{(n+2)(nx-k)^2}{2k(n-k)},\qquad
W_C(x)=\frac{n(n+2)x(1-x)}{k(n-k)},
\]
\[
W_T(x)=\frac{2}{(n-2)(n+1)c}
\left(k-2x+x^2-\frac{(k-x)^2}{n-1}\right).
\]
In particular, \(0<\lambda_J(t)<1\), so restriction to every nontrivial coordinate cap is injective and its sharp squared conditioning ratio equals \(\max_J\lambda_J(t)/\min_J\lambda_J(t)\).

The pairwise differences have **one affine zero each** after removal of a common positive Beta-density factor. With \(H(t)=t^a(1-t)^b/B\),
\[
\lambda_A-\lambda_C
=H(t)\frac{n(n+2)}{k(n-k)}\left(t-\frac kn\right),
\]
\[
\lambda_A-\lambda_T
=H(t)\frac{n(n-1)(n+2)}{k(n-k)(n+1)}
\left(t-\frac{k(n+2)-2n}{n(n-2)}\right),
\]
\[
\lambda_C-\lambda_T
=H(t)\frac{2n(n+2)}{k(n-k)(n+1)}
\left(\frac{n-k-1}{n-2}-t\right).
\]
Consequently all spectral comparisons are classified by the exact thresholds
\[
t_{AC}=\frac kn,\qquad
t_{AT}=\frac{k(n+2)-2n}{n(n-2)},\qquad
t_{CT}=\frac{n-k-1}{n-2}.
\]
For \(1<k<n/2\) they obey \(0<t_{AT}<t_{AC}<t_{CT}<1\): the **least-concentrated mode** changes from axial to tangential to cross, while the most-concentrated mode changes from cross to axial. For \(n/2<k<n-1\), the order is reversed, \(0<t_{CT}<t_{AC}<t_{AT}<1\): the most-concentrated mode changes from cross to tangential to axial, while the least-concentrated mode changes from axial to cross. At the extreme ranks \(k=1\) and \(k=n-1\), one of these thresholds falls outside the open cap interval and the corresponding transition disappears.

At the balanced rank \(n=2k\), **all three branches coincide if and only if \(t=1/2\)**, where
\[
T_{1/2}=\frac12 I_{V_{n,k}}.
\]
Thus exactly half of the full first-harmonic energy lies in the coordinate half-cap for every function in this space, even though its indicator is not constant.

## Assumptions and scope

The Grassmannian is represented by real orthogonal rank-\(k\) projector matrices; the first harmonic space consists of trace-free real symmetric matrix coefficients and is complexified for the Hermitian concentration operator. Its dimension is \(n(n+1)/2-1\). The mask is a *one-coordinate Schubert-threshold region*; it is not claimed to be a geodesic ball when the rank exceeds one. All integrals use invariant probability, not unnormalized Riemannian volume. Rank \(k=1\) or \(n-1\) is included as a boundary case, although the rank-dependent multistep transitions occur at interior rank.

## Proof

**Invariant degree-one normalization.** For any symmetric traceless \(A,B\), orthogonal conjugation invariance and irreducibility of trace-free symmetric matrices give
\[
\mathbb E[\operatorname{tr}(AP)\operatorname{tr}(BP)]
=c\operatorname{tr}(AB),\qquad
c=\frac{2k(n-k)}{n(n-1)(n+2)}.
\]
Indeed \(\|P-kI/n\|_F^2=k(n-k)/n\) identically and dividing by \(\dim V_{n,k}=(n-1)(n+2)/2\) yields this scalar. This also proves injectivity of \(A\mapsto f_A\).

**The three invariant blocks.** The stabilizer of the first coordinate, \(O(n-1)\), acts by conjugation on \(A\) and has the orthogonal decomposition into (i) the span of \(E_{11}-I/n\); (ii) the off-diagonal coefficients in its first row and column; (iii) the trace-free symmetric lower-right \((n-1)\)-block. Their dimensions are \(1,n-1,n(n-1)/2-1\). These are pairwise inequivalent irreducible real \(O(n-1)\)-modules for \(n\ge4\), so the masked form is scalar on each. (Complexification preserves the eigenvalues.)

**Conditional second moments.** Put \(x=P_{11}\). Since a Haar rank-\(k\) projector is the projection onto a uniformly random \(k\)-plane, \(x\) has the Beta law \(\operatorname{Beta}(k/2,(n-k)/2)\). Its variance is \(2k(n-k)/(n^2(n+2))\). The normalized axial coefficient is \(x-k/n\), and dividing its conditional square by this variance yields \(W_A\). Idempotence gives \(\sum_{j>1}P_{1j}^2=x(1-x)\); conditional orthogonal invariance gives \(\mathbb E[P_{12}^2\mid x]=x(1-x)/(n-1)\). For \(A=E_{12}+E_{21}\), divide the conditional mean of \(4P_{12}^2\) by \(2c\) to obtain \(W_C\).

Write \(Q\) for the lower-right \((n-1)\)-block of \(P\). The two exact identities
\[
\operatorname{tr}Q=k-x,\qquad \operatorname{tr}(Q^2)=k-2x+x^2
\]
follow from the projector equation. If \(B\) is any trace-zero symmetric lower-block matrix, conditional orthogonal averaging gives
\[
\mathbb E[\operatorname{tr}(BQ)^2\mid x]
=\frac{2\operatorname{tr}(B^2)}{(n-2)(n+1)}
\left(\operatorname{tr}(Q^2)-\frac{(\operatorname{tr}Q)^2}{n-1}\right).
\]
Dividing by \(c\operatorname{tr}(B^2)\) gives \(W_T\). All weights have mean one under the full Beta law, establishing exactly the three concentration levels and their multiplicities.

**Exact crossing identities.** For any pair \(J,J'\), the polynomial \(W_J-W_{J'}\) has degree at most two and mean zero against \(\rho\). Direct differentiation of \(t^a(1-t)^b(u+vt)/B\) gives
\[
\frac{d}{dt}\frac{t^a(1-t)^b(u+vt)}{B}
=\rho(t)\left[a(1-t)(u+vt)-bt(u+vt)+vt(1-t)\right].
\]
Solving the two linear coefficient constraints for each pair gives the three displayed identities. The endpoint at \(t=1\) fixes integration constants. Their prefactors are strictly positive for every admissible rank and dimension; hence the indicated zeros and inequalities exhaust all possible spectral order changes. The threshold ordering follows from elementary positive factorizations (or subtracting the displayed rational thresholds). At \(k=n/2\), each threshold is \(1/2\), and for \(t\ne1/2\) the first difference is nonzero; all branches therefore coincide only at the half-cap.

**Balanced half-cap identity.** Independently, at \(n=2k\) the measure-preserving involution \(P\mapsto I-P\) exchanges the regions \(x>1/2\) and \(x<1/2\), while \(f_A\mapsto-f_A\) for every trace-free \(A\). Thus each square norm has equal mass on the two regions and \(T_{1/2}=I/2\). More generally the dual-rank spectra obey \(\lambda_J(n,n-k,1-t)=1-\lambda_J(n,k,t)\) when corresponding sectors are identified.

**Sharpness.** Since all three invariant modules are nonzero and the concentration operator acts there as the stated scalar, its extreme eigenvalues are attained by nonzero test functions in the corresponding sectors. The strict positivity of each Beta-integrated weight on every open tail guarantees invertibility, while distinct masks and complete sector enumeration establish the sharp squared condition number.

## Verification

Running `python checker.py` with dependencies from `requirements.txt` symbolically verifies the invariant-sector trace identity and all three affine threshold differences for unrestricted symbolic dimension and rank. It separately checks incomplete-Beta integrals and trace identities at forty finite parameter cases in ten dimension/rank pairs; the checks are not substitutes for the invariant proof. Direct Haar-projector Monte Carlo at one parameter point independently corroborates normalization, to its sampling error.

## Relationship to prior work

Dick, Ehler, Gräf and Krattenthaler's 2019 preprint develops Fourier harmonics and discrepancy kernels for the real Grassmannian \(\mathcal G_{2,4}\), with Fourier expansion of *invariant two-point discrepancy kernels*. Its Section 7 does not solve one-coordinate truncation of the full first-harmonic space at arbitrary rank. Earlier Grassmannian first-harmonic projector-norm and fourth-moment results concern global function norms, not the cap-restriction Gram spectrum. Standard invariant-moment and Beta-law ingredients are not asserted to be new. The claimed contribution is the **complete rank-sensitive three-band restriction spectrum, exact extremal-sector crossings, and unique balanced-rank half-cap tightness criterion**.

## Limitations

The result concerns only the first, nonconstant Grassmannian harmonic sector and a single coordinate threshold. It does not minimize total sample count, extend to arbitrary masks, or classify higher harmonic degrees. The spectral asymptotic behavior for growing \(n\) is not addressed. Historical priority for equivalent formulas under classical zonal-polynomial notation is not exhaustively resolved; independent audit has not been performed.

## References

1. J. Dick, M. Ehler, M. Gräf and C. Krattenthaler, *Spectral decomposition of discrepancy kernels on the Euclidean ball, the special orthogonal group, and the Grassmannian manifold*, arXiv:1909.12334v1 (first public 2019-09-26), Section 7; primary MSC 42C10. Open manuscript: https://arxiv.org/html/1909.12334v1 .
2. Published 2026 mathematical result, *Minimal first-harmonic projections on real Grassmannians: a strict rank hierarchy*; its operator is the global invariant projection from continuous functions, not coordinate-cap restriction.
3. Published 2026 mathematical result, *A sharp fourth-moment spectral phase transition on real Grassmannians*; its sharp \(L^4/L^2\) problem is not a masked \(L^2\)-spectral problem.
