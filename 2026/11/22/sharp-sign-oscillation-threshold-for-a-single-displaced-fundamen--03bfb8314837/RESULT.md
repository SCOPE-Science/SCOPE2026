# Sharp sign-oscillation threshold for a single displaced fundamental frequency

## Finding

Let \(0<\alpha<1\). Consider the real vector space \(\mathcal A_\alpha\) of all uniformly convergent series on \(\mathbb R\)
\[
f(t)=a\cos(\alpha t)+b\sin(\alpha t)+\sum_{n=2}^{\infty}\big(c_n\cos(nt)+d_n\sin(nt)\big),
\]
with real coefficients. Each such function is uniformly almost periodic with Bohr mean zero. The following threshold is sharp:
\[
\boxed{\ \text{Every nonzero }f\in\mathcal A_\alpha\text{ takes both signs on every interval of length }2\pi
\quad\Longleftrightarrow\quad \alpha\ge 1/\sqrt2.\ }
\]
In the complementary range \(0<\alpha<1/\sqrt2\), define
\[
r_\alpha=\frac{\alpha^2}{1-\alpha^2},\qquad a_\alpha=\frac{\pi\alpha}{\sin(\pi\alpha)},\qquad
c_{n,\alpha}=2r_\alpha^n+\frac{2(-1)^n\alpha^2}{n^2-\alpha^2}\quad(n\ge2).
\]
Then the explicitly and absolutely convergent almost-periodic series
\[
f_\alpha(t)=a_\alpha\cos(\alpha t)+\sum_{n=2}^{\infty}c_{n,\alpha}\cos(nt)
\]
is **strictly positive throughout** \([-\pi,\pi]\), since there it equals the positive Poisson kernel
\[
\boxed{\ f_\alpha(t)=\frac{1-r_\alpha^2}{1-2r_\alpha\cos t+r_\alpha^2}\quad(-\pi\le t\le\pi).\ }
\]

## Assumptions and scope

All frequencies use radians per unit time. Intervals are closed, though their endpoint convention does not affect the conclusions. Uniform convergence is required for the general series; the explicit witness converges absolutely because \(c_{n,\alpha}=O_\alpha(n^{-2})\). The frequency \(\alpha\) replaces the integer fundamental \(1\), while every integer frequency \(n\ge2\) is retained. The statement concerns exactly this one-defect family, not arbitrary nonharmonic perturbations or other observation lengths.

The sign-changing assertion includes nonzero members whose cosine coefficient \(a\) is zero: there are no nonzero members identically zero on a full interval of length \(2\pi\).

## Proof

**Step 1: Two orthogonal moment constraints.** Translation preserves \(\mathcal A_\alpha\): for any \(s\in\mathbb R\), the translate \(f(t+s)\) has the same frequency set. It therefore suffices to use \(I=[-\pi,\pi]\). Define normalized window moments
\[
M_0(f)=\frac1{2\pi}\int_{-\pi}^{\pi}f(t)\,dt,
\qquad M_1(f)=\frac1{2\pi}\int_{-\pi}^{\pi}f(t)\cos t\,dt.
\]
Orthogonality of the integer harmonics \(n\ge2\) to both \(1\) and \(\cos t\), oddness of the sine terms, and elementary integration yield
\[
M_0(f)=a\,\frac{\sin(\pi\alpha)}{\pi\alpha},\qquad
M_1(f)=a\,\frac{\alpha\sin(\pi\alpha)}{\pi(1-\alpha^2)}
=\frac{\alpha^2}{1-\alpha^2}\,M_0(f).
\tag{1}
\]
Uniform convergence justifies integrating the infinite series termwise.

**Step 2: Obstruction above and at the critical parameter.** Suppose \(f\ge0\) on \(I\). If \(f\) is not identically zero there, then its continuity gives \(M_0(f)>0\). Since \(1-\cos t\ge0\), with strict inequality for almost all \(t\in I\),
\[
M_0(f)-M_1(f)=\frac1{2\pi}\int_I f(t)(1-\cos t)\,dt>0.
\]
But (1) implies
\[
M_0(f)-M_1(f)=M_0(f)\frac{1-2\alpha^2}{1-\alpha^2}\le0
\]
when \(\alpha\ge1/\sqrt2\), a contradiction, including equality at the critical parameter.

It remains to rule out \(f=0\) on \(I\) with nonzero coefficients. Formula (1) first forces \(a=0\). Taking the normalized \(\sin t\)-moment then gives
\[
0=\frac1{2\pi}\int_I f(t)\sin t\,dt
=b\,\frac{\sin(\pi\alpha)}{\pi(1-\alpha^2)},
\]
so \(b=0\). The remaining uniformly convergent integer Fourier series is zero on a full period; Fourier orthogonality forces every \(c_n,d_n\) to vanish. Thus a nonzero \(f\) cannot be nonnegative on \(I\). Applying the same argument to \(-f\), every nonzero member takes strictly positive and strictly negative values on \(I\). Translations give all intervals of length \(2\pi\).

**Step 3: Exact positive witness below the threshold.** Let \(0<\alpha<1/\sqrt2\), so \(0<r_\alpha<1\), and consider the ordinary periodic Poisson kernel
\[
P_r(t)=\frac{1-r^2}{1-2r\cos t+r^2}
=1+2\sum_{n=1}^{\infty}r^n\cos(nt)>0.
\]
The constant Fourier coefficient of \(a_\alpha\cos(\alpha t)\) on \(I\) is one by (1). Its coefficient of \(\cos(nt)\), for every integer \(n\ge1\), is exactly
\[
\frac{a_\alpha}{\pi}\int_{-\pi}^{\pi}\cos(\alpha t)\cos(nt)\,dt
=\frac{2(-1)^n\alpha^2}{\alpha^2-n^2}.
\tag{2}
\]
For \(n=1\), this is \(2\alpha^2/(1-\alpha^2)=2r_\alpha\), matching the first cosine coefficient of \(P_{r_\alpha}\). Hence the even function \(P_{r_\alpha}(t)-a_\alpha\cos(\alpha t)\), viewed on \(I\) and extended periodically, has zero zeroth and first cosine Fourier coefficients, and its remaining cosine coefficients are exactly \(c_{n,\alpha}\) from the finding. The periodic extension is continuous at the endpoints and piecewise continuously differentiable; formula (2) gives \(O(n^{-2})\) coefficient decay. Its Fourier series therefore converges absolutely and uniformly and represents the stated difference on all of \(I\). This proves the exact Poisson identity and strict positivity there.

**Step 4: Conclusion.** The two cases cover the entire open interval \(0<\alpha<1\), giving the sharp threshold. All series have Bohr mean zero because their frequency set excludes zero and uniform limits preserve the invariant mean. \(\square\)

## Verification

`CHECK.py` uses only the Python standard library. It checks the exact projection identities numerically and tests the Poisson synthesis for parameters on the strictly positive side. Four sampled parameters, a 4096-term truncation and 41 evenly spaced test locations per parameter yield 344 supplementary assertions. An explicit tail estimate is built into the numerical checks. The finite checker does not prove positivity for the infinite series or the universal oscillation claim; those statements follow from the exact integral and Fourier identities above.

To reproduce: `python CHECK.py`.

## Relationship to prior work

Haraux, *An oscillation result for slightly perturbed trigonometric series* (arXiv:2611.04738v1, first public November 3, 2026), proves two-sign oscillation on every interval of length \(2\pi\) when the squared \(\ell^2\) displacement of the frequencies from the positive integers is below \(1/(8\pi^2)\). Applied to one shifted fundamental, that hypothesis only permits \((1-\alpha)^2<1/(8\pi^2)\); it does not establish the present sharp \(\alpha\ge1/\sqrt2\) threshold or the explicit positive witnesses beneath it. Its main theorem and proof were read in the public preprint.

Haraux and Komornik's 1985 paper studies general positive dual weights and oscillation lengths for sums of periodic-function subspaces. The inspected statements and proofs concern periods, subspaces and generic oscillation bounds, not the exact two-moment classification for a one-frequency-replacement spectrum. Delage's later work treats positive orthogonal functions for sums of periodic subspaces with three periods; its abstract does not provide the present classification. Those related works motivate interpreting the decisive inequality as an explicit dual positive test \(1-\cos t\).

## Limitations

The classification applies only to a displaced fundamental with all other positive integer harmonics retained. It does not give a sharp condition for arbitrary square-summable perturbations, for deletion of several low modes, or for different interval lengths. The constructed series is uniformly and absolutely convergent, but no differentiability or optimal coefficient norm is claimed. The 1985 full article was sampled at relevant pages rather than exhaustively analyzed; a bibliographic possibility of an equivalent older single-defect theorem remains. This mathematical result has not undergone an independent audit.

## References

1. A. Haraux, *An oscillation result for slightly perturbed trigonometric series*, arXiv:2611.04738v1, publicly submitted 2026-11-03, https://arxiv.org/abs/2611.04738.
2. A. Haraux, *Uniform oscillation properties of almost periodic functions*, arXiv:2610.06515v1, publicly submitted 2026-10-05, https://arxiv.org/abs/2610.06515.
3. A. Haraux and V. Komornik, *Oscillations of Anharmonic Fourier Series and the Wave Equation*, Rev. Mat. Iberoam. 1 (1985), no. 4, 57–77, https://doi.org/10.4171/RMI/18.
4. F. Delage, *Positive orthogonal functions*, arXiv:1510.04911, 2015, https://arxiv.org/abs/1510.04911.
