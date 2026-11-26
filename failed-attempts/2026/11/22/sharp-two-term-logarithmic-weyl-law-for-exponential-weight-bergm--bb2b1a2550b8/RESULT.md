# Sharp two-term logarithmic Weyl law for exponential-weight Bergman inclusions

## Finding

Fix an integer \(d\ge 1\), and real numbers \(a,b>0\). On the complex unit ball \(\mathbb B_d\), define the Hilbert space of holomorphic functions
\[
A_a^2=\left\{f:\|f\|_a^2:=\int_{\mathbb B_d}|f(z)|^2\exp\!\left(-\frac{a}{1-|z|^2}\right)dV(z)<\infty\right\}.
\]
The canonical inclusion \(J_{a,b}:A_a^2\to A_{a+b}^2\) is compact. Let \(T_{a,b}=J_{a,b}^*J_{a,b}\), a positive compact operator on \(A_a^2\). Put
\[
\kappa=2(\sqrt{a+b}-\sqrt a),\qquad
c=\frac14\log\frac{a+b}{a}-\frac b2.
\]
Enumerate eigenvalues of \(T_{a,b}\) with their Hilbert-space multiplicities and define \(N(\tau)=\operatorname{Tr}{\mathbf{1}}_{(\tau,\infty)}(T_{a,b})\) for \(\tau>0\). For \(L\to\infty\),
\[
\boxed{N(e^{-L})=\frac{(L+c)^{2d}}{d!\,\kappa^{2d}}+O_{a,b,d}(L^{2d-2}).}
\]
In particular, the explicit first two terms are
\[
\frac{L^{2d}}{d!\kappa^{2d}}+\frac{2dc}{d!\kappa^{2d}}L^{2d-1}.
\]
The remainder order is globally sharp: with \(E(L)=N(e^{-L})-(L+c)^{2d}/(d!\kappa^{2d})\),
\[
\boxed{\limsup_{L\to\infty}\frac{|E(L)|}{L^{2d-2}}\ge\frac{1}{2(d-1)!\kappa^{2d-2}}>0.}
\]
Every positive Schatten power is finite, and its singular spectral zeta function has the small-exponent expansion
\[
\boxed{\operatorname{Tr}(T_{a,b}^{p})=\frac{(2d)!}{d!\kappa^{2d}}p^{-2d}\bigl(1+cp+O_{a,b,d}(p^2)\bigr),\quad p\downarrow0.}
\]
The second Weyl coefficient changes sign exactly at the natural parameter relation \(a=b/(e^{2b}-1)\).

## Assumptions and scope

All limits are at fixed \(d,a,b\); the inclusion changes the exponent in the **same radial exponential weight** from \(a\) to \(a+b\), not the radius of a hard localization cutoff. The volume normalization cancels in eigenvalue ratios. \(N\) uses strict inequality, and eigenvalues are counted according to the dimensions of homogeneous holomorphic polynomial spaces. Since \(T=J^*J\), the singular values of \(J\) are exactly the square roots of the eigenvalues stated here. The Schatten expression is the ordinary trace of \(T^p\) for real \(p>0\), including \(0<p<1\).

## Proof

**1. Exact radial diagonalization.** For each integer \(n\ge0\), define \(M_n(A)=\int_0^1 t^n\exp[-A/(1-t)]\,dt\), for \(A>0\). Radial orthogonality implies that every holomorphic homogeneous polynomial of degree \(k\) is an eigenvector of \(T_{a,b}\) with eigenvalue
\[
\lambda_k=\frac{M_{k+d-1}(a+b)}{M_{k+d-1}(a)},\qquad
m_k=\binom{k+d-1}{d-1}.
\]
These eigenvalues are strictly decreasing in \(k\): the probability density proportional to \(t^{k+d-1}\exp[-a/(1-t)]\) shifts strictly to larger \(t\) as \(k\) increases, while the multiplier \(\exp[-b/(1-t)]\) strictly decreases. Hence \(0<\lambda_{k+1}<\lambda_k<1\).

**2. Precise moment saddle.** For fixed \(A>0\), use \(u=1-t\), \(s=\sqrt n\,u\). Near the unique saddle \(s=\sqrt A\), the integrand exponent is
\[
n\log(1-s/\sqrt n)-\frac{A\sqrt n}{s}
=-\sqrt n\left(s+\frac As\right)-\frac{s^2}{2}+O_A(n^{-1/2})
\]
locally with differentiable, uniform error. The phase \(s+A/s\) has minimum \(2\sqrt A\), second derivative \(2/\sqrt A\), and its strictly larger values outside a fixed saddle neighborhood give exponentially smaller contributions. Standard one-dimensional Laplace expansion, with Gaussian dominated tails, therefore gives
\[
M_n(A)=\sqrt\pi A^{1/4}n^{-3/4}\exp(-2\sqrt{An}-A/2)\bigl(1+O_A(n^{-1/2})\bigr).
\]
The coefficient follows from \(ds/\sqrt n\) times \(\sqrt{2\pi/(\sqrt n\,2/\sqrt A)}\). Taking the logarithmic ratio at \(n=k+d-1\), and using \(\sqrt{k+d-1}=\sqrt k+O_d(k^{-1/2})\), yields
\[
\log\lambda_k=-\kappa\sqrt k+c+O_{a,b,d}(k^{-1/2}).
\]
Thus \(\lambda_k\to0\), so \(J\) and \(T\) are compact, and \(\sum_k m_k\lambda_k^p<\infty\) for every \(p>0\).

**3. Counting with a uniform lattice remainder.** Write \(y_k=-\log\lambda_k\). The estimate above says \(y_k=\kappa\sqrt{k}-c+O(k^{-1/2})\). Because \(y_k\) increases strictly, the largest index \(K(L)\) for which \(y_k<L\) obeys
\[
K(L)=\frac{(L+c)^2}{\kappa^2}+O_{a,b,d}(1)
\]
for all sufficiently large \(L\), including thresholds equal to a \(y_k\). Indeed at indices differing by a sufficiently large fixed integer from the displayed center, the main term changes by more than the uniform \(O(k^{-1/2})\) error. The exact multiplicity identity gives
\[
N(e^{-L})=\sum_{k=0}^{K(L)}m_k=\binom{K(L)+d}{d}.
\]
For \(X=(L+c)^2/\kappa^2\), the polynomial binomial formula is \(X^d/d!+O_d(X^{d-1})\), and replacing \(X\) by \(K(L)=X+O(1)\) changes it by \(O_d(X^{d-1})\). Hence the claimed \(O(L^{2d-2})\) remainder and the two explicit leading coefficients follow.

**4. Sharpness.** At the increasing sequence \(L=y_n\), \(N(e^{-L})\) jumps upward by exactly \(m_n\); more precisely its left and right one-sided limits differ by \(m_n\). Its smooth comparison function \((L+c)^{2d}/(d!\kappa^{2d})\) is continuous. For either one-sided limiting error, the larger absolute error is therefore at least \(m_n/2\). Since \(L\sim\kappa\sqrt n\),
\[
\frac{m_n/2}{L^{2d-2}}\longrightarrow \frac1{2(d-1)!\kappa^{2d-2}}.
\]
Taking sequences approaching each jump from both sides proves the asserted limsup lower bound. The lower bound is consistent with the upper remainder estimate and does not assert a specific limiting oscillation profile.

**5. Critical small-power trace.** Since all \(0<\lambda_k<1\), the Laplace-counting identity follows by Tonelli:
\[
\operatorname{Tr}(T^p)=p\int_0^\infty e^{-pL}N(e^{-L})\,dL.
\]
The preceding estimate, after a fixed initial interval, is the polynomial \((L+c)^{2d}/(d!\kappa^{2d})\) plus \(O(L^{2d-2})\). Integrate the polynomial term by term and bound the remainder to obtain
\[
\operatorname{Tr}(T^p)=\frac{(2d)!}{d!\kappa^{2d}}p^{-2d}+\frac{2dc(2d-1)!}{d!\kappa^{2d}}p^{-(2d-1)}+O(p^{-(2d-2)}).
\]
Dividing by the leading term proves the displayed relative expansion. Finally, \(c=0\) is equivalent to \(\log(1+b/a)=2b\), or \(a=b/(e^{2b}-1)\).

## Verification

The standalone `verify.py` evaluates log-radial moments by independent adaptive quadrature in four parameter/dimension cases; it checks 96 finite diagnostics, including eigenvalue monotonicity, the saddle approximation, exact multiplicity counts, and the scaling of the counting remainder. Run `python verify.py` after installing the packages declared in `requirements.txt`. These checks are finite corroboration; the uniform all-degree and small-\(p\) statements follow from the proof rather than from sample values.

## Relationship to prior work

Zhang, Wang and Hu (2021) characterize boundedness, compactness and Schatten membership for Toeplitz operators in exponential-weighted Bergman spaces; their complete primary preprint provides qualitative class criteria, not the present sharp spectral coefficients. Wang, Xia and Liu (2023) characterize Schatten membership for Toeplitz operators in exponential weighted Bergman spaces. Their setting motivates the present natural positive Toeplitz operator, but their membership criteria do not specify its two-term logarithmic counting constants or the optimal lattice remainder. The Gaussian-plunge analysis of radial hard cutoffs on exponential Bergman balls studies an indicator symbol with a *moving cutoff*, not the fixed soft symbol \(e^{-b/(1-|z|^2)}\); its error-function transition does not imply the present stretched-exponential eigenvalue law. Power-weighted Bergman singular-value comparisons of Pushnitski (2017) and El-Fallah--El Ibbaoui (2021) concern polynomially varying regimes rather than the exponential-weight moments here. A broader 2016 weighted-Toeplitz eigenvalue paper by El-Fallah and collaborators remains a possible priority risk because its full text was unavailable in this review.

## Limitations

The result is specific to radial exponential weights with fixed positive \(a,b\) on complex balls. It does not give uniform estimates as either weight parameter varies, does not imply nonradial Toeplitz asymptotics, and does not characterize every higher-order oscillating remainder beyond the proved optimal order. Although the analytical proof establishes the stated assertions, historical priority against inaccessible or unindexed general results remains uncertain, and independent mathematical validation has not been performed.

## References

1. Wang, Xia and Liu, *Schatten class operators on exponential weighted Bergman spaces*, Journal of Inequalities and Applications (2023), DOI: https://doi.org/10.1186/s13660-023-03031-y. Publicly available October 13, 2023.
2. Zhang, Wang and Hu, *Toeplitz operators on Bergman spaces with exponential weights*, arXiv:2107.02481, first posted July 6, 2021, https://arxiv.org/abs/2107.02481.
3. Pushnitski, *Spectral asymptotics for a class of Toeplitz operators on the Bergman space*, arXiv:1710.02652 (2017), https://arxiv.org/abs/1710.02652.
4. El-Fallah and El Ibbaoui, *Trace estimates of Toeplitz operators on Bergman spaces and applications to composition operators*, arXiv:2101.12268 (2021), https://arxiv.org/abs/2101.12268.
5. El-Fallah, Mahzouli, Marrhich and Naqos, *Asymptotic behavior of eigenvalues of Toeplitz operators on weighted analytic spaces*, Journal of Functional Analysis (2016), https://doi.org/10.1016/j.jfa.2016.01.005. Full text not inspected.
6. *Gaussian spectral plunge and sharp projection defect in exponential Bergman balls* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-gaussian-spectral-plunge-and-sharp-projection-defect-in-exponent--79df39d5d5f2. Full statement and proof compared; different hard-cutoff limit.
