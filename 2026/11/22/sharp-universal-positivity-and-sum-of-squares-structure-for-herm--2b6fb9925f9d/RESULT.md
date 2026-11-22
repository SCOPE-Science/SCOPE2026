# Sharp universal positivity and sum-of-squares structure for Hermite truncations in Gaussian quadrature

## Finding

Let \(\operatorname{He}_0(x)=1\), \(\operatorname{He}_1(x)=x\), and \(\operatorname{He}_{n+1}(x)=x\operatorname{He}_n(x)-n\operatorname{He}_{n-1}(x)\) be the **probabilists'** Hermite polynomials. Define, for \(m\in\mathbb{Z}_{\ge0}\), \(\gamma\in\mathbb R\), and \(x\in\mathbb R\),
\[
R_m(\gamma,x)=\sum_{j=0}^{m}\frac{\gamma^j}{2^j j!}\operatorname{He}_{2j}(x),\qquad
 a_k(\gamma)=\sum_{i=0}^{k}\binom{1/2}{i}(-\gamma)^i.
\]
The following exact **finite sum-of-squares identity** holds for every real \(\gamma\), real \(x\), and nonnegative integer \(m\):
\[
\boxed{R_m(\gamma,x)=\sum_{j=0}^{m}\frac{\gamma^j}{j!}\,a_{m-j}(\gamma)\,\operatorname{He}_{j}(x/\sqrt2)^2.}
\]
In the entire parameter interval \(0\le\gamma\le1\), every coefficient in this representation is nonnegative and the constant-square coefficient is strictly positive. Quantitatively,
\[
\boxed{R_m(\gamma,x)\ge a_m(\gamma)\ge \binom{2m}{m}4^{-m}>0.}
\]
Moreover, \([0,1]\) is the **largest parameter set** on which \(R_m(\gamma,x)>0\) holds simultaneously for *every* nonnegative integer \(m\) and every real \(x\): for each \(\gamma<0\) the property fails at \(m=1\) for sufficiently large \(|x|\), while for each \(\gamma>1\) it fails at \(x=0\) for sufficiently large odd \(m\).

As an explicit numerical-integration consequence, set \(m=\lfloor(N-1)/2\rfloor\). The positive Hermite polynomial factor conjectured in Karvonen–Särkkä's scaled Gauss–Hermite **Mercer-truncated approximate Gaussian kernel quadrature weights** is strictly positive for every \(N\ge1\), every real node argument, and all \(0<\gamma\le1\). Therefore, for the standard choice \(\alpha=1/\sqrt2\), their approximate weights are strictly positive for every \(N\ge1\) and every finite Gaussian kernel length scale \(\ell>0\). This does **not** establish positivity of the distinct exact kernel-system quadrature weights.

## Assumptions and scope

All polynomial sums are finite; the square root is the positive real root. Generalized binomial coefficients mean \(\binom{1/2}{i}=\prod_{r=0}^{i-1}(1/2-r)/i!\), with the empty product equal to one. These are polynomial identities in \(x\) and \(\gamma\), independent of numerical conditioning. No assumption about Gaussian quadrature nodes is needed for the polynomial theorem. The corollary uses the published weight formula for the first \(N\) Mercer eigenfunctions at appropriately scaled classical Gauss–Hermite nodes, **not** the original full Gaussian-kernel Gram-system weights. In that formula, \(\gamma=(\sqrt{1+8\varepsilon^2}-1)/(\sqrt{1+8\varepsilon^2}+1)\) with \(\varepsilon=1/(\sqrt2\ell)\); hence \(0<\gamma<1\) when \(\ell>0\).

## Proof

**Step 1: generating function of the even Hermite truncations.** The standard Hermite generating function, or a direct coefficient comparison using the Hermite recurrence, gives the formal identity
\[
\sum_{j=0}^{\infty}\frac{u^j}{2^j j!}\operatorname{He}_{2j}(x)
=(1+u)^{-1/2}\exp\!\left(\frac{u x^2}{2(1+u)}\right).
\]
Summing the finite partial sums over their terminal degree yields, as formal power series in \(t\),
\[
\sum_{m=0}^{\infty}R_m(\gamma,x)t^m
=\frac{1}{1-t}(1+\gamma t)^{-1/2}
\exp\!\left(\frac{\gamma t x^2}{2(1+\gamma t)}\right).
\]

**Step 2: a Mehler diagonal and coefficient extraction.** The probabilists' Hermite diagonal Mehler formula is
\[
\sum_{j=0}^{\infty}\frac{u^j}{j!}\operatorname{He}_j(x/\sqrt2)^2
=(1-u^2)^{-1/2}\exp\!\left(\frac{u x^2}{2(1+u)}\right).
\]
Multiplication by \((1-\gamma t)^{1/2}/(1-t)\) reduces its right-hand side, at \(u=\gamma t\), exactly to the generating function from Step 1. Since
\[
\frac{(1-\gamma t)^{1/2}}{1-t}
=\sum_{k\ge0}\left[\sum_{i=0}^{k}\binom{1/2}{i}(-\gamma)^i\right]t^k
=\sum_{k\ge0}a_k(\gamma)t^k,
\]
coefficient comparison proves the stated finite sum-of-squares identity. This is an **identity of formal power series**, so no analytic convergence domain restriction is involved.

**Step 3: positivity and the quantitative lower bound.** For every \(i\ge1\), \((-1)^i\binom{1/2}{i}<0\). Thus \(a_k(\gamma)\) is nonincreasing on \([0,1]\) and
\[
 a_k(\gamma)\ge a_k(1)=[t^k](1-t)^{-1/2}=\frac{\binom{2k}{k}}{4^k}>0.
\]
Every nonconstant square coefficient is nonnegative for \(0\le\gamma\le1\), and the \(j=0\) square equals \(a_m(\gamma)\). The bound and strict positivity follow.

**Step 4: sharpness of the common parameter range.** If \(\gamma<0\), then \(R_1(\gamma,x)=1+\gamma(x^2-1)/2<0\) for sufficiently large \(|x|\). For \(\gamma>1\), evaluate at zero using \(\operatorname{He}_{2j}(0)=(-1)^j(2j)!/(2^j j!)\):
\[
R_m(\gamma,0)=\sum_{j=0}^{m}(-\gamma)^j c_j,
\qquad c_j=\binom{2j}{j}4^{-j}.
\]
Since \(c_j\sim(\pi j)^{-1/2}\), the ratio to its last term obeys
\[
\frac{R_m(\gamma,0)}{(-\gamma)^m c_m}
=\sum_{r=0}^{m}(-\gamma)^{-r}\frac{c_{m-r}}{c_m}
\longrightarrow \sum_{r=0}^{\infty}(-\gamma)^{-r}=\frac{\gamma}{\gamma+1}>0.
\]
To justify the interchange, for \(r\le m/2\) the central-binomial ratio \(c_{m-r}/c_m\) is uniformly bounded and converges to one at each fixed \(r\); for \(r>m/2\), the entire tail is \(O(\sqrt{m}\,\gamma^{-m/2})\). Thus sufficiently large odd \(m\) give \(R_m(\gamma,0)<0\). This proves sharpness.

**Step 5: quadrature corollary.** Formula (2.11) of Karvonen–Särkkä [2] writes each Mercer-truncated approximate weight as a strictly positive classical Gauss–Hermite weight multiplied by a positive normalization and exponential, times the polynomial \(R_{\lfloor(N-1)/2\rfloor}(\gamma,x_n^{\mathrm{GH}})\). Their Sect. 2.4 explicitly identifies the same polynomial positivity assertion as unproved. For their standard scale \(\alpha=1/\sqrt2\), the displayed \(\gamma\) lies in \((0,1)\), so Step 3 implies each such approximate weight is positive for every \(N\) and kernel length scale.

## Verification

The standalone `verify_hermite.py` computes all polynomial identities symbolically with exact rational input at five values of \(\gamma\), for \(0\le m\le12\); checks positivity at six rational arguments each; verifies exact endpoint binomial values; and tests sample parameters beyond the sharp universal range. Command: `python verify_hermite.py` (requires Python 3 and SymPy). It reports `PASS: 528 exact rational/symbolic assertions`. Finite tests supplement, but **do not replace**, the all-degree generating-function and asymptotic arguments above.

## Relationship to prior work

Särkkä, Hartikainen, Svensson and Sandblom [1] give an earlier Gaussian-process-quadrature/sigma-point and Gauss–Hermite motivation. Karvonen and Särkkä [2] explicitly derive the closed-form approximate Mercer weights and state the Hermite partial-sum positivity as an unproved numerical conjecture (their Sect. 2.4, Eq. (2.11) and following paragraph). Their exact formula and experimental positivity evidence are prior work; the new point is the finite sum-of-squares certificate, the universal lower bound, and the **sharp full-real parameter classification**. The distinct positivity theorems of Karvonen, Kanagawa and Särkkä [3] concern Bayes weights on locally optimal design points or other geometric hypotheses, not this all-degree Hermite truncation. Mehler's classical formula itself is not claimed as new. No priority claim beyond the inspected and searched sources is established.

## Limitations

The result proves positivity of the explicitly defined Hermite partial sums and thereby of the associated **Mercer-truncated approximate** quadrature weights. It does not prove positivity of exact Gaussian-kernel-system weights, stability or accuracy of numerical evaluation, rate of convergence of weight sums, or positivity for parameter choices outside \([0,1]\) in isolated degrees. Finite checking cannot certify the infinite theorem; the proof does. Equivalent identities may exist under Laguerre, Mehler or generalized hypergeometric notation and remain a bibliographic priority risk.

## References

[1] S. Särkkä, J. Hartikainen, L. Svensson and F. Sandblom, *On the relation between Gaussian process quadratures and sigma-point methods*, first public arXiv version 22 April 2015. https://arxiv.org/abs/1504.05994

[2] T. Karvonen and S. Särkkä, *Gaussian kernel quadrature at scaled Gauss–Hermite nodes*, arXiv first public version 26 March 2018; BIT Numer. Math. 59 (2019), 877–902. https://arxiv.org/abs/1803.09532 ; https://doi.org/10.1007/s10543-019-00758-3 (Theorem 2.2, Sect. 2.4).

[3] T. Karvonen, M. Kanagawa and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, Stat. Comput. 29 (2019), 1317–1333. https://doi.org/10.1007/s11222-019-09901-0
