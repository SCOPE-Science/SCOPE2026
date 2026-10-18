# Exact leading slope of Fourier-zero distance for elongated bipyramids
## Finding
For every integer \(d\ge 3\), let
\[
\Omega_{\alpha,d}=\{(x,y)\in\mathbb R\times\mathbb R^{d-1}: |x|+\alpha |y|<1\},\qquad \alpha>0,
\]
and let \(\kappa(\Omega)\) be the distance from the origin to the real zero set of the Fourier transform of \(\chi_\Omega\). Write \(\ell=d-1\), let \(F_\ell(u,s)\) be the two-variable Fourier profile of Gómez-Serrano--Levitin--Platt--Polterovich, and define the sharp transverse zero threshold
\[
\rho_d:=\inf\{s\ge0:\exists u\in\mathbb R\text{ with }F_{d-1}(u,s)=0\}.
\]
Then \(0<\rho_d<\infty\), \(\alpha\mapsto\kappa(\Omega_{\alpha,d})\) is nondecreasing, \(\alpha\mapsto\kappa(\Omega_{\alpha,d})/\alpha\) is nonincreasing, and
\[
\lim_{\alpha\to\infty}\frac{\kappa(\Omega_{\alpha,d})}{\alpha}=\rho_d.
\]
Consequently, if \(\Omega_{\alpha,d}^*\) is the equal-volume Euclidean ball and
\[
c_d=j_{d/2,1}\left(\frac{d\,\omega_d}{2\omega_{d-1}}\right)^{1/d},
\]
then the source paper's lower-growth estimate sharpens to the exact leading asymptotic
\[
\lim_{\alpha\to\infty}
\frac{\kappa(\Omega_{\alpha,d})}{\kappa(\Omega_{\alpha,d}^*)\,\alpha^{1/d}}
=\frac{\rho_d}{c_d}>0.
\]
Thus the sharp leading coefficient of the elongated-bipyramid counterexample is exactly the least transverse frequency at which its fixed rescaled Fourier profile acquires a real zero.

The quantity \(\rho_d\) is intrinsic to the fixed two-variable zero set that appears after the anisotropic rescaling of the bipyramid. It is not an auxiliary positivity constant: it is the exact first-order coefficient of the nearest Fourier-zero distance as the body becomes increasingly elongated.

## Assumptions and scope
Fix an integer \(d\ge3\), put \(\ell=d-1\), and let
\[
\Omega_{\alpha,d}=\{(x,y)\in\mathbb R\times\mathbb R^{d-1}:|x|+\alpha|y|<1\},\qquad \alpha>0.
\]
For a bounded balanced set \(\Omega\), define
\[
\widehat{\chi_\Omega}(\xi)=\int_\Omega e^{i\xi\cdot z}\,dz,
\qquad
\kappa(\Omega)=\operatorname{dist}\bigl(0,\{\xi\in\mathbb R^d:\widehat{\chi_\Omega}(\xi)=0\}\bigr).
\]
The source paper defines
\[
F_\ell(u,s)=2\int_0^1\cos(ux)(1-x)^\ell\,\mathcal B_\ell(s(1-x))\,dx,
\]
where \(\mathcal B_\ell\) is the Fourier transform of the unit \(\ell\)-ball, and proves the exact rescaling identity
\[
\widehat{\chi_{\Omega_{\alpha,d}}}(u,\eta)
=\alpha^{-\ell}F_\ell\!\left(u,\frac{|\eta|}\alpha\right).
\]
Define
\[
Z_d=\{(u,s)\in\mathbb R\times[0,\infty):F_{d-1}(u,s)=0\},
\qquad
\rho_d=\inf_{(u,s)\in Z_d}s.
\]
No assertion is made here that the infimum defining \(\rho_d\) is attained or that \(\rho_d\) has a closed Bessel-function form.

## Proof
The Fourier rescaling identity gives an exact parametrization of all real zeros. Rotational symmetry in the last \(d-1\) coordinates implies
\[
\kappa(\Omega_{\alpha,d})
=\inf_{(u,s)\in Z_d}\sqrt{u^2+\alpha^2s^2}.
\]
Indeed, every real Fourier zero determines a point \((u,|\eta|/\alpha)\in Z_d\), and conversely every \((u,s)\in Z_d\) yields a Fourier zero by choosing any \(\eta\) with \(|\eta|=\alpha s\).

The set \(Z_d\) is nonempty. This follows, for example, by applying the source paper's nonemptiness proposition to \(\Omega_{1,d}\) and then using the same rescaling identity. The source paper also proves that there exists \(\sigma_d>0\) for which
\[
F_{d-1}(u,s)>0\qquad\text{for all }u\in\mathbb R\text{ and }0\le s\le\sigma_d.
\]
Hence
\[
0<\sigma_d\le\rho_d<\infty.
\]

For each fixed \((u,s)\in Z_d\), the function \(\alpha\mapsto\sqrt{u^2+\alpha^2s^2}\) is nondecreasing. Taking infima over the same fixed set \(Z_d\) shows that \(\kappa(\Omega_{\alpha,d})\) is nondecreasing. Dividing by \(\alpha\) gives
\[
\frac{\kappa(\Omega_{\alpha,d})}\alpha
=\inf_{(u,s)\in Z_d}\sqrt{\frac{u^2}{\alpha^2}+s^2},
\]
and each function inside this infimum is nonincreasing in \(\alpha\); therefore the quotient is nonincreasing.

The same formula gives the exact limit. Since every \((u,s)\in Z_d\) has \(s\ge\rho_d\),
\[
\frac{\kappa(\Omega_{\alpha,d})}\alpha\ge\rho_d
\]
for every \(\alpha>0\). Conversely, for each \(\varepsilon>0\), the definition of infimum supplies some \((u_\varepsilon,s_\varepsilon)\in Z_d\) with \(s_\varepsilon<\rho_d+\varepsilon\). Hence
\[
\limsup_{\alpha\to\infty}\frac{\kappa(\Omega_{\alpha,d})}\alpha
\le
\lim_{\alpha\to\infty}
\sqrt{\frac{u_\varepsilon^2}{\alpha^2}+s_\varepsilon^2}
=s_\varepsilon<\rho_d+\varepsilon.
\]
Letting \(\varepsilon\downarrow0\) proves
\[
\lim_{\alpha\to\infty}\frac{\kappa(\Omega_{\alpha,d})}\alpha=\rho_d.
\]

Finally, the source paper computes the equal-volume ball exactly:
\[
\kappa(\Omega_{\alpha,d}^*)
=j_{d/2,1}\left(\frac{d\omega_d}{2\omega_{d-1}}\right)^{1/d}\alpha^{(d-1)/d}
=c_d\alpha^{(d-1)/d}.
\]
Therefore
\[
\frac{\kappa(\Omega_{\alpha,d})}{\kappa(\Omega_{\alpha,d}^*)\alpha^{1/d}}
=\frac1{c_d}\frac{\kappa(\Omega_{\alpha,d})}\alpha
\longrightarrow\frac{\rho_d}{c_d},
\]
which is positive because \(\rho_d>0\).

## Verification
Every step is analytic and exact. The proof uses only: the source's exact Fourier-profile identity; nonemptiness of the real Fourier zero set; its uniform positive strip near \(s=0\); and the source's exact formula for the equal-volume ball. No finite experiment, numerical root search, or asymptotic fit is used.

The critical quantifier check is that \(Z_d\) is independent of \(\alpha\). This makes both monotonicity statements pointwise-before-infimum arguments on one fixed set. The limiting upper bound uses an arbitrary \(\varepsilon\)-minimizer of the transverse coordinate and therefore does not assume attainment of \(\rho_d\).

## Relationship to prior work
Gómez-Serrano, Levitin, Platt, and Polterovich introduce the family \(\Omega_{\alpha,d}\), derive the fixed profile \(F_{d-1}\), prove a positive zero-free strip, and conclude a lower bound \(\kappa(\Omega_{\alpha,d})\ge\alpha\sigma_d\). Their Theorem 1.2 records a positive lower bound for the normalized liminf, rather than an exact limit or an intrinsic leading coefficient. The present observation identifies the exact coefficient as the sharp transverse zero threshold \(\rho_d\).

Benguria, Levitin, and Parnovski's earlier Remark 4.11 uses the same three-dimensional elongated body to show qualitatively that \(\kappa\) tends to infinity while the diameter stays fixed. It does not give a linear asymptotic coefficient.

A later published comparison result, *A Pólya–Bessel zero-free strip for Fourier bipyramids*, gives an explicit Bessel-root lower strip \(r_d\) and hence an explicit inequality \(\kappa(\Omega_{\alpha,d})\ge\alpha r_d\). That implies \(r_d\le\rho_d\), but a lower strip does not imply the equality \(\kappa(\Omega_{\alpha,d})/\alpha\to\rho_d\) or identify the exact leading coefficient unless the strip is independently known to be sharp.

## Limitations
The theorem identifies the exact leading coefficient variationally but does not evaluate \(\rho_d\) in closed form, prove that the infimum defining it is attained, or locate a minimizing pair \((u,s)\). It also does not rigorously certify any particular finite \(\alpha\) threshold at which the bipyramid first beats its equal-volume ball. Those are separate quantitative problems.

## References
1. J. Gómez-Serrano, M. Levitin, D. Platt, I. Polterovich, *An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies*, arXiv:2609.10517v1, 2026.
2. R. Benguria, M. Levitin, L. Parnovski, *Fourier transform, null variety, and Laplacian's eigenvalues*, Journal of Functional Analysis 257 (2009), 2088--2123, DOI 10.1016/j.jfa.2009.06.022.
3. *A Pólya–Bessel zero-free strip for Fourier bipyramids*, published comparison record 2026/9/18/SCOPE-polya-bessel-zero-free-strip-for-fourier-bipyramids--72c1da0f9bb0.
