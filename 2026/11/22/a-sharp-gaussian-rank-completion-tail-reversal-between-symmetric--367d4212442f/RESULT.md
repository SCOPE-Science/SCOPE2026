# A sharp Gaussian rank-completion tail reversal between symmetric and independent updates

## Finding
For any fixed real symmetric positive-semidefinite matrix \(A\) of size \(n\ge2\) and corank one, compare two Gaussian rank-completion schemes:
\[
B_{\mathrm{i}}=A+pq^{\mathsf T},\qquad B_{\mathrm{s}}=A+pp^{\mathsf T},
\]
where \(p,q\) are independent \(N(0,I_n)\) vectors. Both completions are nonsingular with probability one; the second is also positive definite with probability one. For \(H=A^\dagger\), set
\[
C_{\mathrm{i}}=\frac{2}{\pi}\mathbb E|1+q^{\mathsf T}Hp|,
\qquad C_{\mathrm{s}}=\sqrt{\frac{2}{\pi}}\mathbb E\sqrt{1+p^{\mathsf T}Hp}.
\]
Both constants are finite and strictly positive. For the matrix operator norm,
\[
\Pr(\|B_{\mathrm{i}}^{-1}\|_2>R)
\sim C_{\mathrm{i}}\frac{\log R}{R},\qquad
\Pr(\|B_{\mathrm{s}}^{-1}\|_2>R)
\sim C_{\mathrm{s}}R^{-1/2},\qquad R\to\infty.
\]
Thus the symmetric update has asymptotically far heavier inverse-norm extremes. In particular the independent update has finite positive inverse-norm moment of order \(t\) precisely for \(t<1\); the symmetric update has one precisely for \(t<1/2\). The ratio of their exceedance probabilities tends to infinity at rate \((C_{\mathrm{s}}/C_{\mathrm{i}})\sqrt R/\log R\).

## Assumptions and scope
All matrices and Gaussian random variables are real. The matrix \(A\) is deterministic, symmetric and positive semidefinite with exactly one zero eigenvalue; no bound on the positive eigenvalues or condition number of its range restriction is needed. The two completions use unnormalized, unit-variance isotropic Gaussian vectors. The asymptotic is at fixed \(n\) and fixed \(A\) as the inverse-norm threshold \(R\) grows. The Moore--Penrose inverse \(H\) vanishes on the one-dimensional kernel. The result does not compare finite-threshold condition-number distributions or regularized solution errors.

## Proof
Choose a unit null vector and an orthonormal eigenbasis for the range of \(A\). Orthogonal invariance of standard Gaussian vectors reduces the deterministic matrix to \(\operatorname{diag}(0,C)\), where \(C\) is positive definite of order \(m=n-1\). Write \(p=(X,u)\), \(q=(Y,v)\) in this basis. Here \(X,Y\) are independent standard normals, independent of the independent standard-normal \(m\)-vectors \(u,v\). Put \(G=C^{-1}\). Direct block multiplication gives the exact almost-sure identities
\[
(A+pq^{\mathsf T})^{-1}=
\begin{pmatrix}
\dfrac{1+v^{\mathsf T}Gu}{XY}&-\dfrac{v^{\mathsf T}G}{Y}\\
-\dfrac{Gu}{X}&G
\end{pmatrix},
\qquad
(A+pp^{\mathsf T})^{-1}=
\begin{pmatrix}
\dfrac{1+u^{\mathsf T}Gu}{X^2}&-\dfrac{u^{\mathsf T}G}{X}\\
-\dfrac{Gu}{X}&G
\end{pmatrix}.
\]
Their determinants equal \(XY\det C\) and \(X^2\det C\), respectively; hence both are nonsingular almost surely. Since \(A\) is positive semidefinite, the symmetric completion is positive definite if \(X\ne0\).

For two independent standard-normal scalars, the classical product density is \(K_0(|z|)/\pi\). Equivalently, a direct conditioning calculation and the normal density at the origin give
\[
F(\varepsilon):=\Pr(|XY|<\varepsilon)
=\frac2\pi\varepsilon\log(1/\varepsilon)+O(\varepsilon),
\qquad\varepsilon\downarrow0.
\]
Also \(\Pr(X^2<\varepsilon)=\sqrt{2/\pi}\sqrt\varepsilon+O(\varepsilon^{3/2})\). Let \(Z=1+v^{\mathsf T}Gu\), \(T=1+u^{\mathsf T}Gu\). The random quantities \(Z,T\) are independent of \(X,Y\), \(T\ge1\), and possess all positive moments. Conditioning gives
\[
\Pr\left(\frac{|Z|}{|XY|}>R\right)
\sim\frac2\pi\mathbb E|Z|\,\frac{\log R}{R},\qquad
\Pr\left(\frac{T}{X^2}>R\right)
\sim\sqrt{\frac2\pi}\mathbb E\sqrt T\,R^{-1/2}.
\]
For the first formula, use \(F(|Z|/R)\), split at \(|Z|=\sqrt R\), and bound the second part by arbitrarily high moments of \(Z\); the integrable term \(|Z\log|Z||\) controls the leading expansion on the first part.

The remaining inverse blocks have operator norm at most
\[
\|G\|_2+\frac{\|Gu\|_2}{|X|}+\frac{\|Gv\|_2}{|Y|}
\]
in the independent case, and at most \(\|G\|_2+2\|Gu\|_2/|X|\) in the symmetric case. Each remainder has exceedance probability \(O(R^{-1})\), because \(\Pr(|X|<a)\le\sqrt{2/\pi}\,a\) and the Gaussian-vector norms have finite means. They are therefore negligible relative to both preceding leading tail terms. Bounding the full operator norm above and below by its upper-left block, with an arbitrary relative tolerance and then letting the tolerance tend to zero, proves the two asserted equivalences. Orthogonal invariance identifies \(Z=1+q^{\mathsf T}Hp\) and \(T=1+p^{\mathsf T}Hp\), establishing the coordinate-free constants.

For positive moment order \(t\), the upper-left blocks give a lower bound with factors \(|X|^{-t}|Y|^{-t}\) and \(|X|^{-2t}\). The inverse-block identities and subadditivity/finite-dimensional norm bounds give the matching upper integrability conditions, because all Gaussian polynomial numerators have every positive moment. A standard normal variable has finite inverse absolute moment exactly below order one. This proves both sharp moment cutoffs.

## Verification
The accompanying standalone `verification.py` uses exact rational arithmetic to check both full-matrix inverse identities on 375 independently generated positive-definite range blocks of dimensions one through five, using both symmetric and independent rank-one updates. It checks both left and right products and nonzero determinants, totaling 2,250 exact matrix assertions. Eight additional scalar checks compare the independent-normal product small-ball formula with its leading logarithm and the one-normal square small-ball formula with its leading square-root term; the complete script reports **2,258 passing assertions**. These finite checks are diagnostic; the proof for arbitrary dimension and threshold is the preceding analytic argument.

For the illustrative range block \(C=(1)\), numerical one-dimensional Gaussian integrals give \(C_{\mathrm{s}}\approx1.0807592176\) and \(C_{\mathrm{i}}\approx0.7475140857\). These constants serve only as independently reproducible examples.

## Relationship to prior work
Sifuentes, Gimbutas and Greengard (first publicly posted on arXiv January 14, 2014) prove almost-sure solvability for randomized rank completion and provide a deterministic block-inverse identity and conditioning bounds. Their result is the starting point here, but their analysis does not state the competing Gaussian inverse-norm tail asymptotics or the sharp fractional-moment separation. Classical Gaussian-product distribution work supplies the needed scalar density; it does not itself treat nullspace completion. Existing Gaussian matrix condition-number bounds concern different full random matrix ensembles, not these fixed-corank-one rank updates. The contribution here is the universal comparison, including the precise prefactors and all moment boundaries, for arbitrary fixed positive range spectra.

## Limitations
The result is asymptotic in the high inverse-norm threshold, not a finite-threshold preference theorem. It does not assert that the independent update is symmetric or positive definite, nor that its typical condition number is smaller. It assumes real, standard Gaussian rank-one corrections and precisely one null direction; complex fields, higher corank and non-Gaussian laws are not covered. The two scalar small-ball facts and the block-inverse identity have extensive prior histories, so originality is claimed only for their explicit matrix-completion tail comparison; publication priority beyond the inspected sources is not certain.

## References
- J. Sifuentes, Z. Gimbutas and L. Greengard, *Randomized methods for rank-deficient linear systems*, arXiv:1401.3068v1 (public January 14, 2014), https://arxiv.org/abs/1401.3068 .
- Z. Chen and J. J. Dongarra, *Condition Numbers of Gaussian Random Matrices*, SIAM Journal on Matrix Analysis and Applications 27 (2005), https://doi.org/10.1137/040616413 .
- S. Nadarajah and T. K. Pogány, *On the distribution of the product of correlated normal random variables*, first online December 21, 2015, https://doi.org/10.1016/j.crma.2015.10.019 .
- M. D. Springer and W. E. Thompson, *The Distribution of Products of Independent Random Variables*, SIAM Journal on Applied Mathematics 14 (1966), https://doi.org/10.1137/0114046 .
