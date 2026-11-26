# A universal critical \(1/d\)-cusp in sharp spherical Fourier-extension stability

## Finding

For every integer \(d\ge3\), the exact sharp quadratic stability coefficient \(\Gamma_{d,q}\) of the radial--angular mixed Fourier extension inequality on \(\mathbb S^{d-1}\) has a strictly positive, finite critical rescaling:

\[
\lim_{q\downarrow q_c}\frac{\Gamma_{d,q}}{(q-q_c)^{1/d}}=
(2\pi)^d\frac{d-1}{d}\,\frac{D_d}{A_d^{1/d}}>0,
\qquad q_c=\frac{2d}{d-1}.
\]

The constants are explicit convergent quantities:

\[
\nu=\frac d2-1,\quad
m(t)=\frac{\Gamma((t+1)/2)}{\sqrt\pi\,\Gamma(1+t/2)},\quad
A_d=\frac{2}{d-1}\left(\frac2\pi\right)^{q_c/2}m(q_c),
\]

\[
D_d=\lim_{R\to\infty}\int_0^R
r^{d-1-\nu q_c}\bigl(|J_\nu(r)|^{q_c}-|J_{\nu+1}(r)|^{q_c}\bigr)\,dr.
\]

The displayed limit defining \(D_d\) exists as an *ordinary improper integral*, but generally not as the difference of two individually convergent integrals. Its strict positivity, proved below, makes the exponent \(1/d\) exact (the coefficient is neither of smaller nor larger power order). In particular \(\Gamma_{d,q}\to0\), but \(\Gamma_{d,q}/(q-q_c)^{\alpha}\to\infty\) for every \(\alpha>1/d\).

## Assumptions and scope

All dimensions are fixed integers \(d\ge3\); limits take \(q>q_c\) down to \(q_c\) with \(d\) fixed. Let \(\sigma\) be **unnormalized** area measure on \(\mathbb S^{d-1}\), and \(\widehat{f\sigma}(x)=\int e^{-ix\cdot\omega}f(\omega)\,d\sigma(\omega)\). The radial--angular norm is
\[
\|F\|_{L^q_{\mathrm{rad}}L^2_{\mathrm{ang}}}
=\left[\int_0^\infty\left(\int_{\mathbb S^{d-1}}|F(r\theta)|^2\,d\sigma(\theta)\right)^{q/2}r^{d-1}\,dr\right]^{1/q}.
\]

Write \(P_0\) for angular projection to constants and \(C_{d,q}\) for the optimal extension norm. The stability coefficient is the largest nonnegative constant \(\Gamma_{d,q}\) such that
\[
C_{d,q}^2\|f\|_2^2-\|\widehat{f\sigma}\|_{L^q_{\mathrm{rad}}L^2_{\mathrm{ang}}}^2
\ge \Gamma_{d,q}\|f-P_0f\|_2^2
\]
for all complex-valued \(f\in L^2(\mathbb S^{d-1},\sigma)\). The proof uses the **known sharp identity**, established by Xu (2026, Theorem 1.3),
\[
\Gamma_{d,q}=(2\pi)^d\left(I_{\nu,0}(q)^{2/q}-I_{\nu,1}(q)^{2/q}\right),
\quad I_{\nu,k}(q)=\int_0^\infty|J_{\nu+k}(r)|^q r^{d-1-\nu q}\,dr.
\]
We do not claim this identity or the full modal ordering as new.

## Proof

**Step 1: the common pole.** Put \(\beta=(d-1)/2=\nu+1/2\) and \(\varepsilon=q-q_c>0\). Fixed-order Hankel asymptotics, uniformly as \(q\) ranges over a compact interval above \(q_c\), give, for \(r\ge1\),
\[
J_\nu(r)=\sqrt{\frac2{\pi r}}\bigl(\cos(r-\pi\nu/2-\pi/4)+O_d(r^{-1})\bigr),
\]
\[
J_{\nu+1}(r)=\sqrt{\frac2{\pi r}}\bigl(\sin(r-\pi\nu/2-\pi/4)+O_d(r^{-1})\bigr).
\]
For \(2<q\le q_c+1\), the function \(x\mapsto|x|^q\) is uniformly Lipschitz on bounded intervals. Thus each weighted moment's integrand is
\[
\left(\frac2\pi\right)^{q/2}r^{-1-\beta\varepsilon}
\left(|\cos(r-\pi\nu/2-\pi/4-k\pi/2)|^q+O_d(r^{-1})\right)
\]
with the phase appropriately shifted for \(k=0,1\). The periodic cosine-power factor has mean \(m(q)\), and its mean-zero part has a uniformly bounded primitive. Integration by parts makes its weighted tail uniformly bounded as \(\varepsilon\downarrow0\). The error term is absolutely integrable. The behavior at the origin is uniformly integrable, because the leading Bessel powers cancel the \(-\nu q\) exponent. Therefore, for \(k=0,1\),
\[
I_{\nu,k}(q)=\frac{(2/\pi)^{q/2}m(q)}{\beta\varepsilon}+O_d(1)
=\frac{A_d}{\varepsilon}+O_d(1).
\]
Here the second equality uses the smoothness of \((2/\pi)^{q/2}m(q)\) at \(q=q_c\).

**Step 2: cancellation in the difference.** Subtract the two Hankel expansions before integrating. The leading difference is the mean-zero periodic function
\[
\left(\frac2\pi\right)^{q/2}r^{-1-\beta\varepsilon}
\bigl(|\cos\theta|^q-|\sin\theta|^q\bigr),\qquad
\theta=r-\pi\nu/2-\pi/4,
\]
plus an \(O_d(r^{-2-\beta\varepsilon})\) integrable error. The mean-zero primitive argument bounds the tail from \(R\) uniformly by \(O_d(R^{-1})\), for every \(\varepsilon\) in a small nonnegative interval. On finite radii the difference depends continuously on \(q\). Consequently
\[
I_{\nu,0}(q)-I_{\nu,1}(q)\longrightarrow D_d\in\mathbb R,
\]
where \(D_d\) is the finite improper integral in the statement. Crucially this is a limit of differences, not the subtraction of two divergent critical integrals.

**Step 3: strict positivity.** For all real \(\nu\ge0\) and every \(q>2\), Xu's Theorem 3.9 proves strict positivity of the difference integrals on each interval between successive positive zeros of \(J_{\nu+1}\) (including the first interval from zero). At \(q=q_c\), these intervals contribute strictly positive finite values. Step 2 proves their infinite sum converges (the integral has a finite limit along every sequence of cutoffs). Hence its sum \(D_d\) is strictly positive, and cannot vanish by cancellation of positive cells. This step invokes the specifically cited positive-cell theorem; mere positivity of the divergent moments separately would not suffice.

**Step 4: taking the sharp power.** By the mean-value theorem with \(t=2/q\), for positive \(x,y\),
\[
x^t-y^t=t\,(x-y)\,\xi^{t-1},
\]
where \(\xi\) lies between \(x\) and \(y\). Use \(x=I_{\nu,0}(q)\), \(y=I_{\nu,1}(q)\). Steps 1–2 yield \(\xi=(A_d/\varepsilon)(1+O_d(\varepsilon))\) and \(x-y\to D_d\). Because \(2/q\to(d-1)/d\), and \(\varepsilon^{O(\varepsilon)}\to1\),
\[
\left(I_{\nu,0}(q)^{2/q}-I_{\nu,1}(q)^{2/q}\right)
\sim\frac{d-1}{d}\,D_d A_d^{-1/d}\varepsilon^{1/d}.
\]
Multiplying by \((2\pi)^d\) gives the stated exact limit and establishes the power exponent's sharpness.

## Verification

The complete argument uses the fixed-order Bessel expansion and the explicitly inspected positive-cell result of Xu, Theorem 3.9. A standalone numerical program `check_critical.py` evaluates both moments by quadrature on a long finite interval and adds the common leading mean-tail. The program compares finite-\(q\) ratios with the predicted limit for \(d=3,4,5\) and checks finite cutoff positivity. Those floating-point calculations are supplementary stress tests only, not the infinite-integral proof or a certification of the exact constant. The exact defining integral and proof permit reproducibility without floating-point evaluation.

## Relationship to prior work

Xu (2026, arXiv:2610.19648, Theorems 1.3 and 3.9) supplies both the exact best stability coefficient throughout the open admissible range and the positive-cell Bessel comparison used here. The present assertion is the **additional singular boundary asymptotic** of that known exact expression: it extracts and cancels two poles and establishes the exact dimensional Hölder exponent and strictly positive renormalized amplitude. Carneiro--Oliveira e Silva--Sousa (2017) initiated the mixed-norm modal reduction, and Ciccone--Sousa (2023) improved its extremizer ranges. An indexed result, "Exact critical fourth-moment gaps in circular Fourier extension" (2026), has a related boundary calculation for \(d=2\), which is expressly **outside** the present \(d\ge3\) range. Another indexed result on three-dimensional sharp stability concerns the opposite limit \(q\to\infty\), not \(q\downarrow q_c\). A critical-truncation result concerns logarithmic growth of finite-radius norms, not the full optimal gap's approach in the open admissible region.

## Limitations

The formula is for fixed integer \(d\ge3\), with the precise unnormalized measure and Fourier conventions stated above; it is not claimed uniform as dimension grows. The constant \(D_d\) is specified by a conditionally convergent oscillatory integral, not a closed elementary expression. This result does not extend the sharp stability inequality to the excluded critical exponent itself, where individual modal moments diverge, and it does not assert the corresponding limit for \(d=2\). Numerical integration does not independently establish positive-cell theory. A logically equivalent asymptotic under different notation cannot be completely ruled out by indexed-literature searches.

## References

- Zewei Xu, *Sharp radial--angular mixed norm Fourier extension and global stability on spheres*, 2026, arXiv:2610.19648, especially Theorems 1.3 and 3.9, https://arxiv.org/abs/2610.19648 (first public 2026-10-14).
- Emanuel Carneiro, Diogo Oliveira e Silva, Mateus Sousa, *Sharp mixed norm spherical restriction*, 2017, arXiv:1710.10365, https://arxiv.org/abs/1710.10365.
- Valentina Ciccone, Mateus Sousa, *Global and local maximizers for some Fourier extension estimates on the sphere*, 2023, arXiv:2312.07309, https://arxiv.org/abs/2312.07309.
- *Exact critical fourth-moment gaps in circular Fourier extension*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-exact-critical-fourth-moment-gaps-in-circular-fourier-extension--4d8d086fa937 (indexed abstract inspected; full text not accessed).
- *Sharp logarithmic endpoint approach of spherical Fourier extension stability in three dimensions*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-logarithmic-endpoint-approach-of-spherical-fourier-extensi--4e0625f91d3b (indexed abstract inspected; full text not accessed).
