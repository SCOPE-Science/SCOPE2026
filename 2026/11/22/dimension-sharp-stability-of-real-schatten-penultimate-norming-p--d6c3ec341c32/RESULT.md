# Dimension-sharp stability of real Schatten penultimate norming planes

## Finding

For every even integer \(N\ge4\), let \(E\) be a two-dimensional real linear subspace of the real \(N\)-by-\(N\) matrices. Define its normalized trace-to-spectral restriction factor
\[
R(E)=\sup_{0\ne X\in E}\frac{N\|X\|_{\mathcal S_\infty}}{\|X\|_{\mathcal S_1}},
\qquad \varepsilon(E)=R(E)-1.
\]
The minimum of \(R(E)\) is \(1\). Its complete equality class consists of the *conformal matrix planes*
\[
E_{U,J}=U\operatorname{span}_{\mathbb R}\{I_N,J\},\qquad
U^TU=I_N,\quad J^TJ=I_N,\quad J^T=-J.
\]
More strongly, assume \(\varepsilon(E)\le1/(100N)\). For **every** ordered Hilbert--Schmidt orthogonal basis \(A,B\) of \(E\) normalized by
\[
\operatorname{tr}(A^TA)=\operatorname{tr}(B^TB)=N,\qquad \operatorname{tr}(A^TB)=0,
\]
there exist such \(U,J\) satisfying the dimension-explicit operator-norm estimates
\[
\boxed{\|A-U\|_{\mathcal S_\infty}\le3N\varepsilon(E),\qquad
\|B-UJ\|_{\mathcal S_\infty}\le33N\varepsilon(E).}
\]
To express basis-independent stability, put
\[
\mathfrak d(E)=\inf_{U,J}\ \sup_{\substack{X\in E\\\|X\|_{\mathcal S_2}=\sqrt N}}\ \inf_{Y\in E_{U,J}}\|X-Y\|_{\mathcal S_\infty},
\]
where the infimum ranges over all the above conformal planes. Then
\[
\boxed{\mathfrak d(E)\le34N\varepsilon(E).}
\]
**The linear dimension factor and the first power of the excess are simultaneously optimal up to universal constants.** Indeed, for every \(N=2m\ge4\) and every \(0<t<1/2\), with \(R_0=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\), set
\[
B_t=\operatorname{diag}\left(\underbrace{(1+t/(m-1))R_0,\ldots,(1+t/(m-1))R_0}_{m-1\text{ blocks}},(1-t)R_0\right),
\qquad E_t=\operatorname{span}_{\mathbb R}\{I_N,B_t\}.
\]
For this entire explicit family,
\[
\boxed{\varepsilon(E_t)=\frac{t}{m-1},\qquad
\mathfrak d(E_t)\ge\frac{N\varepsilon(E_t)}{4\sqrt{1+t^2/(m-1)}}.}
\]
Choosing arbitrarily small \(t\) also meets the small-excess assumption. Consequently neither \(o(N\varepsilon)\) uniformly in dimension nor a superlinear small-excess bound can replace the displayed order.

## Assumptions and scope

All matrices, vector spaces, and scalar coefficients are **real**. The Schatten norms \(\|\cdot\|_{\mathcal S_1}\), \(\|\cdot\|_{\mathcal S_2}\), and \(\|\cdot\|_{\mathcal S_\infty}\) are respectively the sum, Euclidean norm, and maximum of the \(N\) singular values. The Hilbert--Schmidt inner product is \(\langle A,B\rangle=\operatorname{tr}(A^TB)\). For every even \(N\), orthogonal skew-symmetric matrices \(J\) exist, and each \(E_{U,J}\) has real dimension two.

The factor \(R(E)\) is \(N\) times the operator norm of the restriction of \(\mathrm{id}:\mathcal S_1^N(\mathbb R)\to\mathcal S_\infty^N(\mathbb R)\) to \(E\). Thus its infimum over two-planes corresponds to the penultimate Gelfand number. The present theorem concerns **rigidity and stability of nearly optimal two-planes**, not a new value of that Gelfand number.

## Proof

**1. Every matrix in a nearly optimal plane is uniformly close to orthogonal after Hilbert--Schmidt normalization.** For \(X\in E\) with \(\|X\|_{\mathcal S_2}=\sqrt N\), write its singular values as \(s_1,\ldots,s_N\), with \(s_1\) maximal. Cauchy--Schwarz gives \(\sum_i s_i\le N\). By the definition of \(R(E)=1+\varepsilon\),
\[
\max_i s_i\le \frac{1+\varepsilon}{N}\sum_i s_i\le1+\varepsilon.
\]
Using \(\sum_i s_i^2=N\), for *every* index \(i\),
\[
s_i^2\ge N-(N-1)(1+\varepsilon)^2
=1-(N-1)(2\varepsilon+\varepsilon^2).
\]
For \(0\le\varepsilon\le1/(100N)\) the right side is positive, and \(h=(N-1)(2\varepsilon+\varepsilon^2)\le3N\varepsilon\le0.03\). Since \(\sqrt{1-h}\ge1-h\), all singular values obey
\[
1-3N\varepsilon\le s_i\le1+\varepsilon.
\]
Put \(\delta=3N\varepsilon\). The polar factor \(U_X=X(X^TX)^{-1/2}\) is orthogonal, and the singular-value decomposition yields
\[
\|X-U_X\|_{\mathcal S_\infty}\le\delta,\qquad
\|X^TX-I_N\|_{\mathcal S_\infty}\le\delta.
\]
For the second bound, the positive excess of \(s_i^2\) is at most \(2\varepsilon+\varepsilon^2\le\delta\) since \(N\ge4\), while its negative excess is at most \(h\le\delta\).

**2. The normalized basis is nearly a Clifford pair.** Choose \(A,B\) as stated, and let \(C=(A+B)/\sqrt2\). Hilbert--Schmidt orthogonality makes all three matrices have \(\mathcal S_2\)-norm \(\sqrt N\). Step 1 shows that their Gram matrices differ from \(I_N\) by at most \(\delta\). Therefore
\[
A^TB+B^TA=2C^TC-A^TA-B^TB,
\qquad \|A^TB+B^TA\|_{\mathcal S_\infty}\le4\delta.
\]
Let \(U,V\) be the real orthogonal polar factors of \(A,B\). Then \(\|A-U\|,\|B-V\|\le\delta\), and \(\|A\|,\|B\|\le1+\varepsilon\), with all unlabelled matrix norms in this paragraph being spectral norms. Consequently
\[
\|A^TB-U^TV\|\le\delta(1+\varepsilon)+\delta\le3\delta,
\]
and likewise for its transpose. Writing \(W=U^TV\in O(N)\), we obtain
\[
\|W+W^T\|\le10\delta.
\]

**3. Exact skew-orthogonal correction.** Split \(W=H+K\), where \(H=(W+W^T)/2\) is symmetric and \(K=(W-W^T)/2\) is skew-symmetric. Since \(W\) is orthogonal, \(W\) commutes with its transpose. Thus \(H\) and \(K\) commute, and
\[
K^TK=I_N-H^2,\qquad \|H\|\le5\delta\le0.15.
\]
The matrix
\[
J=K(I_N-H^2)^{-1/2}
\]
is real skew-symmetric and orthogonal: commutation gives \(J^T=-J\), while the identity for \(K^TK\) gives \(J^TJ=I_N\). Moreover,
\[
\|J-W\|\le\|H\|+1-\sqrt{1-\|H\|^2}
\le\|H\|+\|H\|^2\le2\|H\|\le10\delta.
\]
Therefore \(\|B-UJ\|\le\|B-V\|+\|W-J\|\le11\delta=33N\varepsilon\), while \(\|A-U\|\le3N\varepsilon\). At \(\varepsilon=0\), the same proof yields \(E=E_{U,J}\). Conversely, for every \(a,b\in\mathbb R\),
\[
(aI_N+bJ)^T(aI_N+bJ)=(a^2+b^2)I_N,
\]
so each conformal plane has \(R(E_{U,J})=1\). This completes the exact equality classification.

**4. Uniform plane-to-plane distance.** If \(X\in E\) has \(\|X\|_{\mathcal S_2}=\sqrt N\), its normalized basis expansion is \(X=aA+bB\), with \(a^2+b^2=1\). Choose \(Y=aU+bUJ\in E_{U,J}\). By Cauchy--Schwarz on the two scalar coefficients,
\[
\|X-Y\|_{\mathcal S_\infty}\le
\sqrt{(3N\varepsilon)^2+(33N\varepsilon)^2}<34N\varepsilon.
\]
The infima in the definition of \(\mathfrak d\) cannot increase this bound.

**5. Exact obstruction to dimension-free or superlinear stability.** Write \(N=2m\) and put \(b_+=1+t/(m-1)\), \(b_-=1-t\). For \(X=aI_N+bB_t\), its singular values are the two numbers
\[
r_+(a,b)=\sqrt{a^2+b^2b_+^2},\qquad r_-(a,b)=\sqrt{a^2+b^2b_-^2},
\]
with multiplicities \(2(m-1)\) and \(2\), respectively. Since \(r_-/r_+\) is minimized when \(a=0\),
\[
R(E_t)=\max_{(a,b)\ne(0,0)}\frac{m r_+}{(m-1)r_++r_-}
=\frac{m b_+}{(m-1)b_++b_-}=b_+.
\]
The mean \(( (m-1)b_++b_- )/m=1\), hence \(\varepsilon(E_t)=t/(m-1)\) exactly.

Normalize \(B_t\) in Hilbert--Schmidt norm, \(\widetilde B_t=B_t/\sqrt{1+t^2/(m-1)}\), so \(\|\widetilde B_t\|_{\mathcal S_2}=\sqrt N\). Every nonzero member \(Y\) of every conformal plane has all its singular values equal; the zero member has the same property. Singular-value perturbation therefore gives, for any such \(Y\),
\[
2\|\widetilde B_t-Y\|_{\mathcal S_\infty}\ge
s_{\max}(\widetilde B_t)-s_{\min}(\widetilde B_t)
=\frac{tm/(m-1)}{\sqrt{1+t^2/(m-1)}}.
\]
As \(\widetilde B_t\in E_t\), the definition of \(\mathfrak d\) yields the advertised lower bound \(\mathfrak d(E_t)\ge N\varepsilon(E_t)/(4\sqrt{1+t^2/(m-1)})\). For each even dimension, \(t\) can tend to zero through values satisfying \(\varepsilon(E_t)\le1/(100N)\). The upper and lower estimates therefore match in both dimension and excess order. \(\square\)

## Verification

The standalone `checker.py` uses only the Python standard library, constructs the explicit block family in orders \(4,6,8,10,12,14,16\), samples the two-plane quotient as a secondary check of the exact formula, and evaluates the normalized witness singular-value separation and explicit near-conformal correction. It reports `NEAR_CONFORMAL_TWO_PLANE_DIAGNOSTIC_OK 42`. Execute `python checker.py` with Python 3. The finite angle samples cannot certify a continuum supremum; the exact monotonicity in Step 5 and the all-matrix bounds in Steps 1--4 provide the proof. No numerical error bounds are claimed beyond the stated deterministic test tolerances.

## Relationship to prior work

The penultimate real Schatten Gelfand number was previously determined exactly, including its dimension-parity behavior, in [2]. Its scalar identity implies \(\inf_E R(E)=1\) for even order, but does not determine stability of arbitrary near-minimizing planes. A complete restriction-norm landscape and exact stability profile are known for real matrices of order two [3]. That planar result is credited; the present statement starts in order four, has a *dimension-dependent* sharp modulus, and includes a lower-witness family in every even order. Prochno's recent article [1] and earlier work [4,5] give Schatten width asymptotics and general s-number estimates, not this quantitative Clifford-polar rigidity statement.

The matrix-polar, singular-value and Cauchy--Schwarz ingredients themselves are standard and are not claimed as new. The contribution is their uniform two-plane combination with an explicit sharp dependence on both the dimension and restriction-norm deficit.

## Limitations

Only **real, square, even-order** matrices and the trace-to-operator endpoint are addressed. The explicit upper coefficient \(34\) is not claimed to be optimal; the dimension and deficit *orders*, not the leading constant, are sharp. No assertion is made for larger-dimensional subspaces, odd order, or other exponents. Related results outside the inspected literature could affect bibliographic priority. The diagnostic computations are finite sanity checks, not proof. Independent mathematical validation has not been performed.

## References

1. J. Prochno, *Gelfand numbers of Schatten class embeddings in the quasi-Banach range*, arXiv:2611.08448v1 (first publicly posted 2026-11-05), https://arxiv.org/abs/2611.08448.
2. *A parity law for the penultimate Gelfand number of real Schatten embeddings*, published-finding corpus finding dated 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-parity-law-for-the-penultimate-gelfand-number-of-real-schatten--fc1996e343be.
3. *Exact Grassmannian landscape and endpoint stability for real two-by-two Schatten widths*, published-finding corpus finding dated 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-grassmannian-landscape-and-endpoint-stability-for-real-two--9d93319a3182.
4. J. Prochno and M. Strzelecki, *Approximation, Gelfand, and Kolmogorov numbers of Schatten class embeddings*, arXiv:2103.13050v1 (2021), https://arxiv.org/abs/2103.13050.
5. A. Hinrichs, J. Prochno and J. Vybíral, *Gelfand numbers of embeddings of Schatten classes*, arXiv:2011.06554v1 (2020), https://arxiv.org/abs/2011.06554.
