# Sharp half-density Gabor frame bounds for asymmetric two-sided exponential windows

## Finding
For every pair \(\alpha,\beta>0\) define
\[
g_{\alpha,\beta}(t)=\begin{cases}e^{-\alpha t},&t\ge0,\\ e^{\beta t},&t<0.\end{cases}
\]
The Gabor system \(\mathcal G(g_{\alpha,\beta},1,1/2)\) has the following **optimal**, strictly positive frame bounds. Write
\[
r=e^{-\alpha},\quad s=e^{-\beta},\quad p=\frac1{1+r^2},\quad h=\frac{s^2}{1+s^2},\quad q=\frac{s(s+r)}{(1+r^2)(1+s^2)}.
\]
Set
\[
y_*=\frac{2\alpha p}{\sqrt{(\alpha-\beta)^2q^2+4\alpha\beta ph}+(\alpha-\beta)q},\quad x_*=\min\left\{1,\max\left\{0,\frac{\log y_*}{\alpha+\beta}\right\}\right\}.
\]
Then
\[
\boxed{A=2\left(pe^{-2\alpha x_*}+he^{2\beta x_*}-2qe^{(\beta-\alpha)x_*}\right)}
\]
and
\[
\boxed{B=2\left[\left(\frac1{1-r^2}+\frac{s^2}{1-s^2}\right)^2+\left(\frac r{1-r^2}+\frac s{1-s^2}\right)^2\right].}
\]
The lower extremum occurs at Zak frequency \(\omega\equiv1/4\pmod{1/2}\) and spatial coordinate \(x_*\); the upper extremum occurs at \(x=0\pmod1\), \(\omega=0\pmod{1/2}\). For \((\alpha,\beta)=(1,2)\), \(x_*\approx0.587918694649\), \(A\approx0.497204372340\), \(B\approx3.396729948180\). The minimizer is genuinely displaced from the symmetric midpoint.

## Assumptions and scope
Use the Fourier/Zak convention \(Zg(x,\omega)=\sum_{k\in\mathbb Z}g(x+k)e^{-2\pi i k\omega}\), \(0\le x<1\). The system consists of \(e^{\pi i m t}g(t-n)\), with \(m,n\in\mathbb Z\), in \(L^2(\mathbb R)\). We allow every strictly positive real decay-rate pair, including equality; the window is unnormalized. Frame bounds refer to
\[
A\lVert f\rVert_2^2\le\sum_{m,n\in\mathbb Z}|\langle f,e^{\pi i m(\cdot)}g((\cdot)-n)\rangle|^2\le B\lVert f\rVert_2^2.
\]

## Proof
The unitary Zak fiberization of translation-by-one, modulation-by-one-half Gabor frames shows that its frame operator has multiplier
\[
F(x,\omega)=|Zg(x,\omega)|^2+|Zg(x,\omega+1/2)|^2.
\]
This normalization follows directly from the standard Fourier-series Parseval identity for the modulation index, followed by the even/odd translation decomposition. Thus optimal bounds are the essential infimum and supremum of \(F\) on one Zak cell. Continuity allows extrema on the closed cell with endpoint quasi-periodicity.

Put \(U=e^{-\alpha x}\), \(V=e^{\beta x}\), \(R=r^2\), \(S=s^2\), and \(\zeta=e^{-4\pi i\omega}\). Splitting even and odd translation indices gives
\[
F=2(|E|^2+|O|^2),\quad E=\frac{U}{1-R\zeta}+\frac{VS}{\zeta-S},\quad O=\frac{rU}{1-R\zeta}+\frac{sV}{\zeta-S}.
\]
An irrelevant unit-modulus factor in the odd Zak sum does not affect \(F\). Over the common denominator \((1-R\zeta)(\zeta-S)\) the numerators are respectively
\[
E:\quad (U-VRS)\zeta+S(V-U),\qquad O:\quad r(U-rsV)\zeta+s(V-rsU).
\]
All four coefficients are nonnegative because \(U/V=e^{-(\alpha+\beta)x}\in[rs,1]\). Consequently the squared numerator sum is nondecreasing as a function of \(c=\operatorname{Re}\zeta\), while the squared denominator \((1+R^2-2Rc)(1+S^2-2Sc)\) decreases strictly on \([-1,1]\). Thus for each \(x\) the minimum of \(F\) occurs at \(c=-1\) and the maximum at \(c=1\).

At \(c=1\),
\[
F(x,0)=2\left[\left(\frac{U}{1-R}+\frac{VS}{1-S}\right)^2+\left(\frac{rU}{1-R}+\frac{sV}{1-S}\right)^2\right].
\]
The right side is a convex function of \(x\): expansion is a positive linear combination of \(e^{-2\alpha x}\), \(e^{2\beta x}\), and \(e^{(\beta-\alpha)x}\); each exponential is convex and the coefficients are nonnegative. Therefore its maximum on \([0,1]\) lies at an endpoint. These endpoints agree by Zak quasi-periodicity; substitution at \(x=0\) gives exactly \(B\).

At \(c=-1\),
\[
\frac12F(x,1/4)=\left(\frac{U}{1+R}-\frac{VS}{1+S}\right)^2+\left(\frac{rU}{1+R}-\frac{sV}{1+S}\right)^2
=pU^2+hV^2-2qUV.
\]
Differentiating and setting \(y=e^{(\alpha+\beta)x}\), we find
\[
\frac14\frac{d}{dx}F(x,1/4)=e^{-2\alpha x}\bigl[-\alpha p+(\alpha-\beta)qy+\beta hy^2\bigr].
\]
The quadratic in brackets is negative at \(y=0\), strictly positive for sufficiently large \(y\), and has precisely one positive root (product of its roots is negative). The root is exactly \(y_*\), so \(F(x,1/4)\) strictly decreases until its unique unconstrained minimizer and then strictly increases. Restricting to \([0,1]\) gives the stated clipped optimizer \(x_*\) and \(A\).

Finally \(ph-q^2=s^2(1-rs)^2/[(1+r^2)^2(1+s^2)^2]>0\), so \(pU^2+hV^2-2qUV>0\) whenever \(U,V>0\). This proves \(A>0\) for all admissible parameters and completes the exact sharp-bound proof.

## Verification
Run `python CHECK.py` with NumPy. The checker reconstructs the original truncated Zak series for eight asymmetric and symmetric decay-rate pairs, checks its rational fiber representation on spatial-frequency grids, compares the predicted extrema and reflection symmetry, and independently reduces the equal-rate case to the published symmetric integer-oversampling expression. It returned `ASYMMETRIC_HALF_DENSITY_GABOR_CHECKS_PASSED 2644`. The proof above, rather than the finite grid, establishes correctness for all \(\alpha,\beta>0\).

## Relationship to prior work
De Dios Pont, Gröchenig, Liehr, Shafkulovska, and Taylor (2026, first public August 5) characterize **whether** a Gabor system of a continuous integrable totally positive function is a frame; this does not imply the numerical optimal constants or the asymmetric interior optimizer. Kloos and Stöckler's treatment of the **even** two-sided exponential in their Zak-transform paper derives bounds and asymptotics, not this exact two-rate minimization. Existing symmetric two-sided exponential sharp formulas are recovered on the diagonal \(\alpha=\beta\), where \(x_*=1/2\), but cannot determine the independent two-parameter frame-bound surface. General Zak-transform frame formulas provide the starting point but leave a nontrivial two-variable optimization, solved here.

## Limitations
Only translation spacing \(1\), modulation spacing \(1/2\), unnormalized two-sided exponentials, and strict positive decay rates are covered. No claim is made for arbitrary rectangular lattices, multiwindow systems, noisy data, or optimal dual-window localization. Equivalent sharp formulas might exist in older or differently indexed Gabor/Zak literature; independent publication-priority review has not occurred.

## References
- J. de Dios Pont, K. Gröchenig, L. Liehr, I. Shafkulovska, M. A. Taylor, *Gabor Frames of Totally Positive Functions: A Complete Characterization*, arXiv:2608.04992v1 (first public August 5, 2026), https://arxiv.org/abs/2608.04992.
- T. Kloos, J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359 (2013), https://arxiv.org/abs/1311.7359.
- K. Gröchenig, J. L. Romero, J. Stöckler, *Sampling theorems for shift-invariant spaces, Gabor frames, and totally positive functions*, Inventiones Mathematicae (2017), doi:10.1007/s00222-017-0760-2.
