# Exact null-ray X-ray spectra and optimal direction weighting over odd finite fields

## Finding
Let \(q\) be an odd prime power, \(d\ge 3\), and \(Q(x)=x^{\mathsf T}Ax\) a nondegenerate quadratic form on \(V=\mathbb F_q^d\), where \(A=A^{\mathsf T}\) is invertible. Let \(\mathcal D\) be the set of projective null directions \(\ell\le V\) with \(\dim\ell=1\) and \(Q(\ell)=0\). The **null-ray X-ray transform** sends a complex point function to all its affine null-line sums:
\[
(R_Qf)(a+\ell)=\sum_{x\in a+\ell}f(x),\qquad \ell\in\mathcal D,
\]
with counting-measure Hilbert norms on points and affine lines.

Write \(Q^*(\xi)=\xi^{\mathsf T}A^{-1}\xi\), let \(\eta\) be the quadratic character on \(\mathbb F_q\), and define
\[
P_d=\frac{q^{d-2}-1}{q-1},\quad
\varepsilon=\begin{cases}
\eta((-1)^{d/2}\det A),&d\text{ even},\\
\eta((-1)^{(d-1)/2}\det A),&d\text{ odd}.
\end{cases}
\]
For every additive Fourier frequency \(\xi\), the eigenvalue of \(R_Q^*R_Q\) is \(q\,m(\xi)\), where \(m(0)=|\mathcal D|\) and
\[
|\mathcal D|=\frac{q^{d-1}-1}{q-1}+\mathbf1_{2\mid d}\,\varepsilon q^{(d-2)/2}.
\]
For nonzero \(\xi\), the *complete* multiplier classification is
\[
m(\xi)=\begin{cases}
P_d,&d\text{ odd},\ Q^*(\xi)=0,\\
P_d+\varepsilon\eta(Q^*(\xi))q^{(d-3)/2},&d\text{ odd},\ Q^*(\xi)\ne0,\\
P_d+\varepsilon q^{(d-2)/2},&d\text{ even},\ Q^*(\xi)=0,\\
P_d,&d\text{ even},\ Q^*(\xi)\ne0.
\end{cases}
\]
The multiplicities, including frequencies with repeated eigenvalues, are given in the proof below.

**Sharp inversion threshold.** The operator is injective exactly when \(d\ge4\). In dimension three its kernel has dimension \(q(q-1)^2/2\), supported precisely on nonzero frequencies with \(\varepsilon\eta(Q^*(\xi))=-1\). For \(d\ge4\), the exact squared spectral condition number is
\[
\kappa(R_Q)^2=\frac{|\mathcal D|}{m_{\min}},\qquad
m_{\min}=\begin{cases}
P_d-q^{(d-3)/2},&d\text{ odd},\\
P_d+\min\{0,\varepsilon q^{(d-2)/2}\},&d\text{ even}.
\end{cases}
\]
Thus in dimension four the split (\(\varepsilon=1\)) case has \(\kappa(R_Q)=\sqrt{q+1}\), while the nonsplit (\(\varepsilon=-1\)) case has \(\kappa(R_Q)=\sqrt{q^2+1}\). For each fixed \(d\ge5\), \(\kappa(R_Q)/\sqrt q\to1\) as \(q\to\infty\) through odd prime powers.

**Sharp weighting principle.** For any nonnegative direction weights \(w_\ell\), not all zero, let \(R_w\) multiply every line sum with direction \(\ell\) by \(\sqrt{w_\ell}\). Then \(\kappa(R_w)\ge\kappa(R_Q)\) for \(d\ge4\), with infinite condition number allowed when \(R_w\) is singular. Uniform weights attain equality. In \(d=3\), every such weighted transform retains the indicated kernel. The weighting claim concerns weights constant across affine offsets of each direction, not arbitrary per-line weights.

## Assumptions and scope
The characteristic is odd; no prime-field restriction is imposed. For each \(q,d,Q\), all affine lines in every null direction are measured, each exactly once. The input and output use counting \(\ell^2\) norms, not normalized probability norms, and line sums are unnormalized. The singular values are the square roots of the stated normal-operator eigenvalues. The constant Fourier character is included in the condition number; it has the largest normal eigenvalue. The theorem does not concern nonisotropic directions, even characteristic, arbitrary subsets of affine offsets, or noisy nonlinear measurements.

## Proof
**1. Fourier reduction.** Fix a nontrivial additive character \(\psi\) of \(\mathbb F_q\). The characters \(e_\xi(x)=\psi(\xi\cdot x)\) form an orthogonal basis. For any direction \(\ell=\mathbb F_qv\), a character summed over its affine line satisfies \(\sum_{t\in\mathbb F_q}\psi(t\xi\cdot v)=q\) if \(\xi\cdot v=0\), and zero otherwise. From
\[
(R_Q^*R_Qf)(x)=\sum_{\ell\in\mathcal D}\sum_{t\in\mathbb F_q}f(x+tv_\ell)
\]
we obtain the exact Fourier multiplier
\[
q\,m(\xi),\qquad m(\xi)=\#\{\ell\in\mathcal D:\xi\cdot\ell=0\}.
\]
This identity fixes the normalization, all eigenvalues, and the only possible nullspace.

**2. Quadratic zero counts.** Standard additive-character orthogonality, one-dimensional quadratic Gauss sums, and \(G(\eta,\psi)^2=\eta(-1)q\) give, for every nondegenerate quadratic form \(F\) of dimension \(r\) and determinant \(\delta\),
\[
\#\{y:F(y)=0\}=\begin{cases}
q^{r-1},&r\text{ odd},\\
q^{r-1}+(q-1)\eta((-1)^{r/2}\delta)q^{(r-2)/2},&r\text{ even},
\end{cases}
\]
and, for any nonzero value \(t\),
\[
\#\{y:F(y)=t\}=\begin{cases}
q^{r-1}+\eta((-1)^{(r-1)/2}\delta)\eta(t)q^{(r-1)/2},&r\text{ odd},\\
q^{r-1}-\eta((-1)^{r/2}\delta)q^{(r-2)/2},&r\text{ even}.
\end{cases}
\]
For completeness: expand \(\mathbf1_{\{F(y)=t\}}=q^{-1}\sum_s\psi(s(F(y)-t))\), diagonalize \(F\), evaluate \(\sum_z\psi(sa z^2)=\eta(sa)G(\eta,\psi)\) for \(s\ne0\), and sum over \(s\). These evaluations hold for extension fields as well.

**3. Hyperplane sections and exact eigenvalues.** Identify a frequency \(\xi\) with \(u=A^{-1}\xi\), so \(\xi\cdot v=u^{\mathsf T}Av\) and \(Q(u)=Q^*(\xi)\). If \(u\) is anisotropic, its orthogonal hyperplane is nondegenerate of dimension \(d-1\) and determinant square class \(\det A/Q(u)\). If \(u\ne0\) is isotropic, its orthogonal hyperplane has radical \(\langle u\rangle\); the quotient by that radical is a nondegenerate space of dimension \(d-2\), whose even-dimensional quadratic sign equals \(\varepsilon\). The latter follows by splitting off a hyperbolic plane with determinant square class \(-1\). Count zeros in the relevant hyperplane, subtract the zero vector, and divide by \(q-1\) for projectivization. This gives precisely the displayed four cases for \(m(\xi)\); applying the same zero count in \(V\) gives \(|\mathcal D|\).

The exact *frequency multiplicities* are as follows. If \(d\) is odd, there is one zero frequency, \(q^{d-1}-1\) nonzero isotropic frequencies, and for each \(\sigma\in\{-1,1\}\), the multiplier \(P_d+\sigma q^{(d-3)/2}\) occurs
\[
\frac{q-1}{2}\left(q^{d-1}+\sigma q^{(d-1)/2}\right)
\]
times. If \(d\) is even, there is one zero frequency, the multiplier \(P_d+\varepsilon q^{(d-2)/2}\) occurs
\[
q^{d-1}+\varepsilon(q-1)q^{(d-2)/2}-1
\]
times, and the multiplier \(P_d\) occurs
\[
(q-1)\left(q^{d-1}-\varepsilon q^{(d-2)/2}\right)
\]
times. Multiplicity totals equal \(q^d\).

**4. Inversion and sharp singular values.** When \(d=3\), \(P_d=1\) and the negative-sign multiplier vanishes with multiplicity \((q-1)(q^2-q)/2=q(q-1)^2/2\). All other frequencies have positive multipliers. For odd \(d\ge5\), \(P_d>q^{(d-3)/2}\). For even \(d\ge4\), \(P_d>q^{(d-2)/2}\) (strictly, including \(d=4\), when \(P_d=q+1\)). Thus all eigenvalues are strictly positive in \(d\ge4\), and the stated minimum follows from the available classes. Every \(m(\xi)\le |\mathcal D|\), with equality for \(\xi=0\). The inverse on \(d\ge4\) is obtained by Fourier filtering \(R_Q^*R_Qf\), dividing its \(\xi\)-coefficient by \(q m(\xi)\). The condition formulas and fixed-dimension asymptotics follow directly.

**5. Optimality of uniform direction weighting.** Write \(W=\sum_{\ell\in\mathcal D}w_\ell>0\). The weighted normal operator has Fourier multipliers \(q\sum_{\ell\in\mathcal D:\xi\cdot\ell=0}w_\ell\), with maximum \(qW\) attained by the constant character. Choose a nonzero frequency \(\xi_*\) minimizing the unweighted value \(m(\xi_*)=m_{\min}\). The full orthogonal group of \(Q\) acts transitively on isotropic projective lines by Witt extension. Averaging the weighted multiplier at all orthogonal translates of \(\xi_*\) therefore gives exactly \(qWm_{\min}/|\mathcal D|\). At least one translate has multiplier no larger than this average. Hence every nonsingular weighted transform has squared condition number at least \(|\mathcal D|/m_{\min}\), and singular ones have infinite condition number. Constant weights give equality. In dimension three the zero-frequency class persists under any weighting because no null line is orthogonal to those frequencies.

## Verification
Run `python check_null_xray.py` with Python 3. The standalone script enumerates projective null directions and every dual Fourier frequency over \(\mathbb F_3\), \(\mathbb F_5\), and the extension field \(\mathbb F_9\), checking every predicted multiplier and multiplicity; it also tests nonuniform positive weights and directly diagonalizes two small incidence normal matrices when NumPy is installed. The tested dimensions are three, four, and five as appropriate, with both even-dimensional Witt signs. The run reported `NULL_RAY_FOURIER_VERIFICATION_PASS`. These finite tests corroborate but do not replace the general Gauss-sum and hyperplane-count proof.

## Relationship to prior work
Koh's 2012 paper, *Sharp endpoint estimates for the X-ray transform and the Radon transform in finite fields* (arXiv:1209.1215), studies unrestricted finite-field line and hyperplane transforms and sharp mapping estimates. The inspected full text does not impose null-direction restrictions, classify a quadratic-dual Fourier multiplier, or give the corresponding singular-value and weighting theorems. Feldman and Grinberg's *Admissible Complexes for the Projective X-Ray Transform over a Finite Field* (arXiv:1707.06695) concerns point-to-projective-line transforms and minimal line-complex admissibility, not affine null-line sums on the full vector space. Finite quadratic-form zero counts and orthogonal-group transitivity are classical ingredients, not novel lemmas. The theorem here is the assembled exact inverse-problem classification and optimal stability barrier for the null-line measurement family.

## Limitations
Priority has been compared only with accessible material and bounded searches; a previously unlocated treatment of null-line tomography or an implicit specialization of a general finite Radon theorem could overlap. No claim is made for characteristic two, \(d<3\), per-affine-line weights, or nonlinear stability. The dimension-four nonsplit instability cannot be mitigated by direction-only scalar weights, but no assertion is made about arbitrary preprocessing or changing the acquisition geometry. Mathematical inspection and executable small-field checks are not independent validation.

## References
1. Doowon Koh, *Sharp endpoint estimates for the X-ray transform and the Radon transform in finite fields*, arXiv:1209.1215, first posted 2012-09-06; https://arxiv.org/html/1209.1215v2 .
2. David V. Feldman and Eric L. Grinberg, *Admissible Complexes for the Projective X-Ray Transform over a Finite Field*, arXiv:1707.06695, first posted 2017-07-20; https://arxiv.org/abs/1707.06695 .
3. Ethan Bolker, *The finite Radon transform*, Contemporary Mathematics 63 (1987), 27–50. A potentially relevant general historical framework; full text not inspected.
