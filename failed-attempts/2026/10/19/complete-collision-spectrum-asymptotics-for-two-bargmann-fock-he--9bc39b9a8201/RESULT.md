# Complete collision-spectrum asymptotics for two Bargmann–Fock Hermite clusters

## Finding

For each fixed multiplicity \(m\ge1\), the normalized Gaussian Hermite sampling vectors at two points have a full, exactly computable hierarchy of spectral degeneracies as the points coalesce. For \(1\le r\le m\), define

\[
D_{m,0}=1,\qquad
D_{m,r}=\left(\prod_{i=0}^{r-1}\sqrt{\frac{(m+i)!}{(m-r+i)!}}\right)
\frac{\prod_{i=0}^{r-1} i!}{\prod_{i=0}^{r-1}(r+i)!}.
\]

The \(2m\) eigenvalues split into exactly complementary pairs, \(\lambda_{r,+}(w)+\lambda_{r,-}(w)=2\). When \(w\to0\) and \(m\) is fixed,

\[
\lambda_{r,-}(w)=\frac12\left(\frac{D_{m,r}}{D_{m,r-1}}\right)^2|w|^{4r-2}\bigl(1+O_m(|w|^2)\bigr),\qquad 1\le r\le m.
\]

Every coefficient is strictly positive. In particular the least eigenvalue, for all sufficiently small nonzero \(w\), is

\[
\boxed{\lambda_{\min}(G_m(w))=\frac{|w|^{4m-2}}{2(2m-1)!\binom{2m-2}{m-1}^2}\bigl(1+O_m(|w|^2)\bigr).}
\]

Because the largest eigenvalue tends to \(2\), the spectral condition number obeys

\[
\boxed{\kappa_2(G_m(w))\sim4(2m-1)!\binom{2m-2}{m-1}^2|w|^{-(4m-2)}.}
\]

For example, for multiplicity \(m=3\), the three lower eigenvalues have leading terms \(\tfrac32|w|^2\), \(\tfrac1{12}|w|^6\), and \(\tfrac1{8640}|w|^{10}\). This classifies **all** singular scales, not solely the worst direction.

## Assumptions and scope

Use the Bargmann–Fock Hilbert space \(\mathcal F^2\) with

\[
\|f\|^2=\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z),\qquad
 e_j(z)=\frac{z^j}{\sqrt{j!}}.
\]

Fix an integer \(m\ge1\), define \(E_m=\operatorname{span}\{e_0,\ldots,e_{m-1}\}\), and introduce the unitary Weyl translation

\[
W_wf(z)=\exp(-|w|^2/2+\bar w z)f(z-w).
\]

Let \(G_m(w)\) be the ordered Gram matrix of \(e_0,\ldots,e_{m-1},W_we_0,\ldots,W_we_{m-1}\), with the standard complex Hilbert inner product. Each cluster consists of an orthonormal family. This Gram matrix corresponds to two multiplicity-\(m\) jet-sampling sites with the natural, translation-covariant normalization. The claimed limit is for each **fixed** \(m\), with \(|w|\downarrow0\); the normalization of the Gaussian weight is fixed at exponent one. The spectrum depends only on \(|w|\) by rotational symmetry.

## Proof

**1. Block reduction and positivity.** Let \(P\) denote the orthogonal projection onto \(E_m\), set \(C=P W_w|_{E_m}\) and \(T=(I-P)W_w|_{E_m}\). In the bases chosen above,

\[
G_m(w)=\begin{pmatrix}I_m&C\\ C^*&I_m\end{pmatrix},\qquad C^*C+T^*T=I_m.
\]

The eigenvalues of this block matrix are \(1\pm\sigma_j(C)\), with \(\sigma_j(C)\) the singular values of \(C\). Consequently, if \(s_1(T)\ge\cdots\ge s_m(T)\) are the singular values of \(T\), the lower-branch eigenvalues can be enumerated as

\[
\lambda_{r,-}(w)=1-\sqrt{1-s_r(T)^2},\qquad 1\le r\le m,
\]

and the complementary eigenvalues equal \(2-\lambda_{r,-}(w)\). For \(w\ne0\), \(E_m\cap W_wE_m=\{0\}\): otherwise a nonzero polynomial equals \(e^{\bar w z}\) times a polynomial, which is impossible for \(w\ne0\). Thus \(\sigma_j(C)<1\), proving positive definiteness of \(G_m(w)\).

**2. Exact leakage coefficients.** Unitary rotations reduce the spectral calculation to real \(w=a>0\). For all \(k\ge m\) and \(0\le j<m\), the coefficient of \(e_k\) in \(W_a e_j\) is

\[
T_{kj}(a)=e^{-a^2/2}\sqrt{\frac{j!}{k!}}\,a^{k-j}L_j^{(k-j)}(a^2)
=a^{k-j}\left(\frac{\sqrt{k!/j!}}{(k-j)!}+O_{m,k}(a^2)\right),
\]

using \(L_j^{(k-j)}(0)=\binom{k}{j}\). In particular every entry begins in order \(a^{k-j}\) and has an even analytic correction in \(a\).

**3. The unique minimal exterior minor.** For \(1\le r\le m\), index an \(r\times r\) minor of \(T\) by distinct rows \(k_1<\cdots<k_r\), each at least \(m\), and distinct columns \(j_1<\cdots<j_r<m\). In the determinant, each permutation has the common factor

\[
a^{\sum_{u=1}^r k_u-\sum_{v=1}^r j_v}.
\]

The least possible exponent is \(r^2\). There is exactly one minor at that order: its rows are \(m,m+1,\ldots,m+r-1\) and its columns are \(m-r,\ldots,m-1\). Its leading coefficient is

\[
\begin{aligned}
&\det_{0\le i,h<r}\left[\frac{\sqrt{(m+i)!/(m-r+h)!}}{(r+i-h)!}\right]\\
&=\left(\prod_{i=0}^{r-1}\sqrt{\frac{(m+i)!}{(m-r+i)!}}\right)
 \det_{0\le i,h<r}\left[\frac1{(r+i-h)!}\right]
 =D_{m,r}.
\end{aligned}
\]

The reciprocal-factorial determinant evaluates to

\[
\det_{0\le i,h<r}\frac1{(r+i-h)!}
=\frac{\prod_{i=0}^{r-1}i!}{\prod_{i=0}^{r-1}(r+i)!},
\]

Multiplying row \(i\) by \((r+i)!\) gives the entries \((r+i)^{\underline h}\), where \(x^{\underline h}=x(x-1)\cdots(x-h+1)\). These are monic polynomials in \(r+i\) of degrees \(h\), so their determinant is the Vandermonde product \(\prod_{h=1}^{r-1}h!\). The coefficient \(D_{m,r}\) is positive and cannot cancel.

**4. Control of the infinite matrix and each singular value.** Regard all \(r\times r\) minors as matrix entries of the exterior-power map \(\bigwedge^rT\), whose domain is finite dimensional. The full Fock expansion of \(e^{az}(z-a)^j\) gives convergent, locally norm-analytic coefficient sequences for fixed \(j\), and therefore a locally convergent Hilbert–Schmidt power series for \(\bigwedge^rT\). The preceding order count yields one entry \(D_{m,r}a^{r^2}(1+O_m(a^2))\); the squared sum of all remaining entries is \(O_m(a^{2r^2+2})\). Its operator norm is squeezed between that leading entry's modulus and the Hilbert–Schmidt norm. Consequently

\[
\prod_{j=1}^{r}s_j(T)=\|\bigwedge^rT\|
=D_{m,r}a^{r^2}(1+O_m(a^2)).
\]

Dividing adjacent identities (with \(D_{m,0}=1\)) gives

\[
s_r(T)=\frac{D_{m,r}}{D_{m,r-1}}a^{2r-1}(1+O_m(a^2)),
\]

and using \(1-\sqrt{1-t}=\tfrac12t(1+O(t))\) establishes each asserted lower eigenvalue. All orders \(2,6,\ldots,4m-2\) are distinct and positive, and hence the least eigenvalue corresponds to \(r=m\) for sufficiently small \(a\).

**5. Sharp extremal coefficient.** Direct cancellation of the explicit factorial products gives

\[
\left(\frac{D_{m,m}}{D_{m,m-1}}\right)^2
=\frac1{(2m-1)!\binom{2m-2}{m-1}^{2}}.
\]

The largest eigenvalue equals \(2-o(1)\), giving the stated condition number. Rotating the variable returns \(a=|w|\) without affecting the spectrum.

## Verification

The standalone Python program `verify.py` performs exact rational arithmetic checks of the reciprocal-factorial determinant for \(1\le r\le7\) and high-precision checks of the explicit last-channel coefficient for \(1\le m\le6\). Independently formed finite overlap and Fock leakage-tail matrices agree in the predicted singular spectra. For all \(1\le m\le6\), every leakage channel is checked at \(a=0.04,0.07,0.10\); the expected leading-power ratios are within 12%. The script reports 139 successful assertions; see `verification_output.txt`. Those finite computations corroborate but do not replace the all-multiplicity proof, which depends on the unique minimal minor and norm-analytic exterior powers.

## Relationship to prior work

Escudero, Haimi, and Romero's multiple Fock interpolation framework uses the same Weyl shifts and normalized monomials and characterizes when weighted infinite arrays interpolate in terms of separation and Beurling density [1]. Borichev, Hartmann, Kellay, and Massaneda prove geometric existence and separation criteria for multiple interpolation with possibly unbounded multiplicities [2]. Cruz, Massaneda, and Ortega-Cerdà establish related interpolation-array conditions in finite polynomial spaces [3]. Their inspected main results and proofs do not provide the fixed-multiplicity collision spectrum, its full hierarchy of exponents, or its sharp factorial constants. The present result is a local, finite two-site conditioning statement, not a strengthening of global density characterizations. An equivalent statement in older displaced-number-state or confluent-kernel spectral literature remains possible.

## Limitations

The expansion is for fixed \(m\) as \(w\to0\), with an implicit constant allowed to depend on \(m\). No claim is made about a joint limit in which \(m\to\infty\), about more than two sites or unequal jet multiplicities, or about non-Gaussian weights. The normalized Gram eigenvalues do not directly equal singular values of a differently normalized, raw derivative-sampling matrix. No independent scholarly priority audit has been performed.

## References

[1] L. A. Escudero, A. Haimi, and J. L. Romero, *Multiple sampling and interpolation in weighted Fock spaces of entire functions*, arXiv:2004.12922 (first posted 2020-04-27), https://arxiv.org/abs/2004.12922.

[2] A. Borichev, A. Hartmann, K. Kellay, and X. Massaneda, *Geometric conditions for multiple sampling and interpolation in the Fock space*, arXiv:1508.03932 (2015), https://arxiv.org/abs/1508.03932.

[3] C. A. Cruz, X. Massaneda, and J. Ortega-Cerdà, *Multiple sampling and interpolation in a space of polynomials*, arXiv:2405.19945 (first posted 2024-05-30), https://arxiv.org/abs/2405.19945.
