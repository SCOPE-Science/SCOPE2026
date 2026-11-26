# Sharp Gaussian variation error for positive mixtures of Mehler operators

## Finding

Let \(\gamma\) be standard Gaussian probability measure on \(\mathbb R\). For \(0\le r\le1\), let the Mehler noise operator be
\[
(U_r f)(x)=\int_{\mathbb R}f\bigl(rx+\sqrt{1-r^2}\,z\bigr)\,d\gamma(z).
\]
Given **any** Borel probability measure \(\nu\) on \([0,1]\) with \(\nu([0,1))>0\), define the positive Markov mixture \(T_\nu=\int U_r\,d\nu(r)\), interpreted as a bounded operator on \(L^2(\gamma)\). Let \(\mathcal B\) be the class of real \(L^1_{\rm loc}(\mathbb R)\) functions with finite *ordinary (Lebesgue/distributional)* variation \(V(f)=|Df|(\mathbb R)\); no Lebesgue-integrability condition at infinity is imposed. Then
\[
\boxed{\sup_{f\in\mathcal B,\ V(f)>0}\frac{\|f-T_\nu f\|_{L^2(\gamma)}^2}{V(f)^2}
=\frac14+\frac{\displaystyle\int\!\!\int\arcsin(rs)\,d\nu(r)d\nu(s)-2\displaystyle\int\arcsin r\,d\nu(r)}{2\pi}.}
\]
This constant is strictly positive. **Every** nonconstant equality case, and no other one, is \(f(x)=c+a\mathbf1_{[0,\infty)}(x)\) almost everywhere, where \(a\ne0\) and \(c\in\mathbb R\). The location of the optimal jump is independent of the mixture law, including discrete, singular continuous, and continuous laws and laws with an atom at \(1\).

For the ordinary Ornstein–Uhlenbeck semigroup \(U_{e^{-t}}\), \(t>0\), the same formula becomes
\[
C_t^2=\frac14+\frac{\arcsin(e^{-2t})-2\arcsin(e^{-t})}{2\pi},\qquad
C_t^2\sim\frac{\sqrt2-1}{\pi}\sqrt t\quad(t\downarrow0),
\]
and \(C_t^2=\frac14-e^{-t}/\pi+O(e^{-2t})\) as \(t\to\infty\).

## Assumptions and scope

All inputs and output norms are real scalar-valued, in one spatial dimension. The denominator is **ordinary** variation \(|Df|(\mathbb R)\), not Gaussian-weighted perimeter or the variation seminorm of the time-indexed semigroup. A function in \(\mathcal B\) has finite limits at both infinities after a null-set modification, so it is bounded and belongs to \(L^2(\gamma)\). Constants are annihilated by \(I-T_\nu\). The strict inequality \(\nu([0,1))>0\) excludes the identity operator and is needed for uniqueness.

## Proof

**1. Reduction to one jump.** For \(f\in\mathcal B\), its distributional derivative is a finite real signed measure \(\mu=Df\). After choosing a representative, \(f(x)=c+\int_{\mathbb R}\mathbf1_{[s,\infty)}(x)\,d\mu(s)\) for almost every \(x\). Write \(h_s=\mathbf1_{[s,\infty)}\). Since \(U_r\) is Markov, \(T_\nu\mathbf1=\mathbf1\), and the integrand is uniformly bounded, Fubini and the Bochner integral triangle inequality give
\[
\|(I-T_\nu)f\|_2\le\int\|(I-T_\nu)h_s\|_2\,d|\mu|(s).
\]
Consequently, the sharp squared norm is \(\sup_{s\in\mathbb R}R_\nu(s)\), where \(R_\nu(s)=\|(I-T_\nu)h_s\|_2^2\). This also proves equality for a maximizing step; classification follows once its location is unique.

**2. Exact one-jump residual.** Set \(p(s)=\Pr\{X\ge s\}=\Phi(-s)\), where \(X\) is standard normal, and \(q_r(s)=\Pr\{X\ge s,Y\ge s\}\) for jointly standard normal \((X,Y)\) with correlation \(r\in[0,1]\). Gaussian reversibility and \(U_rU_u=U_{ru}\) imply
\[
R_\nu(s)=p(s)-2\int q_r(s)\,d\nu(r)+\int\!\!\int q_{ru}(s)\,d\nu(r)d\nu(u).
\]
This is a combination of *two distinct correlation levels*, not a single noise-stability extremal problem. If \(\varphi=\Phi'\) and \(b_r=\sqrt{(1-r)/(1+r)}\), differentiation of the bivariate Gaussian tail along its two moving boundary lines yields
\[
q_r'(s)=-2\varphi(s)\Phi(-b_rs),\qquad 0\le r\le1.
\]
At \(r=1\), this remains valid because \(q_1=p\) and \(b_1=0\). The derivative is dominated uniformly by \(2\varphi(s)\), so differentiation may pass through both mixing integrals.

**3. Universal strict median optimality.** For \(r,u\in[0,1]\), the correlation-product identity is
\[
b_{ru}^{\,2}=\frac{b_r^2+b_u^2}{1+b_r^2b_u^2}\le(b_r+b_u)^2.
\]
On the positive half-line, \(\operatorname{erf}\) is strictly increasing and subadditive: \(\operatorname{erf}(v+w)\le\operatorname{erf}(v)+\operatorname{erf}(w)\), strictly for \(v,w>0\). For \(s>0\), using \(2\Phi(-z)=1-\operatorname{erf}(z/\sqrt2)\), we obtain
\[
\frac{R_\nu'(s)}{\varphi(s)}=
\int\!\!\int\operatorname{erf}\!\left(\frac{b_{ru}s}{\sqrt2}\right)d\nu(r)d\nu(u)
-2\int\operatorname{erf}\!\left(\frac{b_rs}{\sqrt2}\right)d\nu(r)<0.
\]
Indeed, the integrand after comparison with the sum of two single-parameter terms is strictly negative whenever \(r,u<1\), an event of positive \(\nu\otimes\nu\) mass. Gaussian reflection symmetry gives \(R_\nu(-s)=R_\nu(s)\). Hence \(s=0\) is the **unique global maximum**, with no compactness or finite-mixture approximation argument needed.

**4. Sharp constant and rigidity.** Sheppard's bivariate-normal identity gives \(q_r(0)=1/4+\arcsin(r)/(2\pi)\), valid at both endpoints. Substitution into step 2 proves the displayed exact constant. Because \(\nu([0,1))>0\), \(h_0-T_\nu h_0\ne0\) in \(L^2(\gamma)\); therefore the sharp constant is positive. In step 1, equality requires \(\|(I-T_\nu)h_s\|_2\) to have its maximum for \(|Df|\)-almost all \(s\). Uniqueness of that maximum forces \(|Df|\) to be supported at \(0\); hence \(Df=a\delta_0\) and \(f=c+a h_0\) almost everywhere. Conversely, every such nonconstant function attains equality.

**5. Semigroup asymptotics.** Put \(\nu=\delta_{e^{-t}}\). The exact formula follows immediately. The elementary expansion \(\arcsin(1-\epsilon)=\pi/2-\sqrt{2\epsilon}+O(\epsilon^{3/2})\) yields the stated small-time asymptotic, while \(\arcsin z=z+O(z^3)\) yields the long-time formula. These conclusions do not extend automatically to signed mixtures or negative correlation parameters.

## Verification

The self-contained \(\texttt{verification_check.py}\) reproduces Gaussian tail probabilities by conditional one-dimensional quadrature independently of the arcsine formula; tests mixed-parameter residual monotonicity and the exact correlation-product identity using rational arithmetic; and checks the one-parameter small-time law numerically. Its 101 checks passed. Numerical quadrature is corroboration only: the all-law, all-function assertion is proved by the analytic steps above.

## Relationship to prior work

Ambrosio–Da Prato–Pallara (2010) analyze *Gaussian-measure* BV and semigroup derivative regularization; their Theorem 3.3 bounds smoothed gradients in \(L^1\) and does not evaluate this ordinary-variation-to-Gaussian-\(L^2\) identity residual. Mossel–Neeman (2012) establish uniqueness for Gaussian noise stability **at fixed Gaussian mass**; their inequality is not a comparison of the opposing two-point terms \(q_r\) and \(q_{ru}\) in the present residual. O'Donnell (2014) gives the Mehler semigroup identities and Sheppard's formula used as premises here, but not the mixture-wide residual norm or its equality classification. Casarino–Ciatti–Sjögren (2023) consider variation in the *time parameter*, with an \(L^1\)-weak type theorem, not ordinary spatial BV-to-\(L^2\) fixed-mixture error.

No directly covering result was identified among the sources inspected and the recorded searchable mathematical findings. This is a best-knowledge originality assessment rather than a theorem of global priority.

## Limitations

The optimality assertion applies only to the explicitly defined one-dimensional, real, finite *ordinary* variation class and positive probability mixtures supported in \([0,1]\). It does not assert the same norm for Gaussian-weighted variation, higher dimensions, negative correlations, signed mixing laws, or a nonlinear noise mechanism. The independent mathematical review of this claim remains unperformed.

## References

1. L. Ambrosio, G. Da Prato, D. Pallara, *BV functions in a Hilbert space with respect to a Gaussian measure*, Rend. Lincei Mat. Appl. 21 (2010), 405–414. https://doi.org/10.4171/RLM/580 (published 2010-12-02).
2. E. Mossel, J. Neeman, *Robust Optimality of Gaussian Noise Stability*, arXiv:1210.4126 (first version 2012-10-15). https://arxiv.org/abs/1210.4126
3. R. O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press (2014), Section 11.1, especially Example 11.19 and Remark 11.14. https://www.math.tau.ac.il/~amnon/Classes/2016-PRG/Analysis-Of-Boolean-Functions.pdf
4. V. Casarino, P. Ciatti, P. Sjögren, *On the variation operator for the Ornstein–Uhlenbeck semigroup in dimension one*, Ann. Mat. Pura Appl., first published 2023-07-25. https://doi.org/10.1007/s10231-023-01358-3
