# Sharp conditioning barrier for critical Herglotz Cauchy Gabor frames

## Finding

For every real \(\alpha>0\), set \(\beta=1/\alpha\). Consider a finite positive Cauchy mixture
\[
g(t)=\sum_{j=1}^{N}\frac{a_j}{t-iw_j},\qquad N\ge1,\quad a_j>0,\quad w_j>0,
\]
and its rectangular critical-density Gabor system \(\{e^{2\pi i\beta n t}g(t-\alpha m):m,n\in\mathbb Z\}\) in \(L^2(\mathbb R)\). Let \(A_g\) and \(B_g\) be the **optimal squared-norm frame bounds**: the largest admissible lower and smallest admissible upper constants in the usual Gabor-frame inequality. Put
\[
r_j=e^{-2\pi w_j/\alpha}\in(0,1),\qquad
L=\sum_{j=1}^N\frac{a_jr_j}{1+r_j},\qquad
U=\sum_{j=1}^N\frac{a_j}{1-r_j}.
\]
Then the exact bounds for **every** finite positive mixture are
\[
\boxed{A_g=\frac{4\pi^2}{\alpha}L^2,\qquad
B_g=\frac{4\pi^2}{\alpha}U^2.}
\]
The frame-operator condition number has the universal sharp minimum
\[
\boxed{\frac{B_g}{A_g}\ge(1+\sqrt2)^4.}
\]
The equality cases, up to a positive overall multiplier, are **exactly** the single-pole Cauchy windows with pole height
\[
\boxed{w_*=\frac{\alpha}{2\pi}\log(1+\sqrt2).}
\]
In particular, adding positive-residue poles at different heights can never improve the best possible critical-lattice conditioning.

There is an **exact stability identity**, stronger than the inequality. Define
\[
r_*=\sqrt2-1,\quad
q_j=\frac{a_jr_j/(1+r_j)}{L},\quad
\mathcal D=\sum_{j=1}^{N}q_j\frac{(r_j-r_*)^2}{r_j(1-r_j)}.
\]
Here \(q_j>0\) and \(\sum_jq_j=1\). Then
\[
\boxed{\frac{B_g}{A_g}=(1+\sqrt2)^4(1+\mathcal D)^2.}
\]
Consequently, for every \(\delta>0\), the weighted fraction of poles with \(|r_j-r_*|\ge\delta\) satisfies
\[
\sum_{\{j:|r_j-r_*|\ge\delta\}}q_j\le\frac{\mathcal D}{4\delta^2}.
\]
Thus close-to-optimal conditioning quantitatively forces concentration of the effective pole distribution near the unique optimal height. If the pole heights are required to be pairwise distinct and \(N\ge2\), the inequality is strict, although its infimum remains sharp.

## Assumptions and scope

All Fourier transforms use \(\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi it\xi}\,dt\). Each window is a nonzero finite sum of positive residues at purely imaginary poles in the upper half-plane. Its \(L^2\) membership follows from decay \(O(|t|^{-1})\) at infinity and the absence of real poles. Translation spacing is \(\alpha\) and modulation spacing is exactly \(\beta=1/\alpha\), with no normalization of the window's \(L^2\) norm. The condition number is the ratio of **squared frame bounds** \(B_g/A_g\), not its square root (the latter is the condition number of the analysis operator). Duplicate heights may be merged by adding their positive residues.

The finding makes no assertion about overcomplete lattices, nonrectangular lattices, complex or negative residues, or poles on opposite sides of the real axis. The results are quantified over every \(N\ge1\), all \(\alpha>0\), and all stated residues and heights.

## Proof

**1. Zak-fiber reduction and normalization.** Use the \(\alpha\)-Zak transform
\[
(Z_\alpha f)(x,\omega)=\sum_{k\in\mathbb Z}f(x-\alpha k)e^{2\pi i\alpha k\omega},
\quad 0<x<\alpha,\quad 0<\omega<1/\alpha.
\]
At critical density the frame operator is unitarily equivalent to multiplication by \(\alpha |Z_\alpha g|^2\), so its optimal bounds are the essential infimum and supremum of that multiplier. For a single pole \((t-iw)^{-1}\), residue summation, or the half-line Fourier transform followed by Poisson summation, gives the almost-everywhere identity
\[
Z_\alpha[(\cdot-iw)^{-1}](x,\omega)
=-\frac{2\pi i}{\alpha}
\frac{e^{2\pi ix\omega}e^{2\pi w\omega}}
{1-e^{2\pi ix/\alpha}e^{2\pi w/\alpha}}.
\]
This expression is standard and recorded explicitly for the Cauchy kernel in Belov–Kulikov–Lyubarskii (2022). Linearity is legitimate for the finite sum. With \(z=e^{-2\pi ix/\alpha}\) and \(t=1-\alpha\omega\in(0,1)\), factoring a common unimodular phase gives
\[
|Z_\alpha g(x,\omega)|=\frac{2\pi}{\alpha}
\left|\sum_{j=1}^N\frac{a_jr_j^t}{1-r_jz}\right|,\qquad |z|=1.
\]
No endpoint value of the Fourier-series representative is required: essential extrema are obtained as one-sided limits from \(0<t<1\).

**2. Exact fiber extrema.** For every \(0<r<1\) and \(|z|=1\),
\[
\operatorname{Re}\frac1{1-rz}
=\frac{1-r\operatorname{Re}z}{1-2r\operatorname{Re}z+r^2}
\ge\frac1{1+r},\qquad
\left|\frac1{1-rz}\right|\le\frac1{1-r}.
\]
The first expression is strictly increasing in \(\operatorname{Re}z\); equality in the lower inequality holds at \(z=-1\) and in the upper inequality at \(z=1\). Since \(r_j\le r_j^t\le1\) and every \(a_j\) is strictly positive,
\[
L\le \operatorname{Re}\sum_j\frac{a_jr_j^t}{1-r_jz}
\le\left|\sum_j\frac{a_jr_j^t}{1-r_jz}\right|\le U.
\]
For \(z=-1\) the lower value is approached as \(t\uparrow1\), while for \(z=1\) the upper value is approached as \(t\downarrow0\). Each neighborhood of these boundary points has positive torus measure. Hence the *essential* infimum and supremum of the modulus are exactly \(L\) and \(U\); multiplying by \(4\pi^2/\alpha\) proves the formulas for \(A_g,B_g\). In particular \(0<A_g\le B_g<\infty\).

**3. Global conditioning optimum.** Let \(h(r)=(1+r)/(r(1-r))\) and \(c=(1+\sqrt2)^2=3+2\sqrt2\). Then
\[
\frac UL=\sum_{j=1}^Nq_j h(r_j),\qquad
h(r)-c=c\frac{(r-r_*)^2}{r(1-r)},\quad r_*=\sqrt2-1.
\]
The last identity follows by expanding the quadratic numerator; it is exact on \(0<r<1\). All summands of the defect are nonnegative. Therefore \(U/L=c(1+\mathcal D)\), establishing the exact condition-number identity and its sharp universal lower bound. Equality holds precisely when every \(r_j=r_*\), corresponding to the single effective height \(w_*\). For any \(\delta>0\), \(r(1-r)\le1/4\) implies that each excluded summand in \(\mathcal D\) is at least \(4\delta^2q_j\). Summing proves the stated stability estimate.

## Verification

The standalone, standard-library-only script `check_critical_cauchy.py` checks the exact closed formulas for positive mixtures with one through six poles across randomized lattice scales; verifies sampled Zak-fiber bounds and sharp boundary limits; checks the scalar square-defect identity and global optimum; and compares its Zak expression with truncated direct rational-function sums at interior fiber points. Replaying the embedded script gives `CRITICAL_CAUCHY_FRAME_CHECKS_PASS 6062`. These 6062 checks are finite computational corroboration. The universal theorem is established by the explicit inequalities and factorization in the proof, not by the computation.

For example, with \(\alpha=1\) and a single pole at \(w=\log(1+\sqrt2)/(2\pi)\), the exact condition-number ratio is \((1+\sqrt2)^4\). A positive two-pole mixture at different heights necessarily has a strictly larger ratio.

## Relationship to prior work

Belov, Kulikov and Lyubarskii (2021 preprint; 2022 publication) proved that **every** positive Cauchy (Herglotz) mixture has a Gabor frame on **all** rectangular lattices of density at least one. That is a qualitative frame-set theorem, not an exact formula for the optimal mixed-window frame bounds or their best attainable condition number. Belov, Kulikov and Lyubarskii (2022 preprint on the single Cauchy kernel) explicitly computed critical-density optimal bounds **when there is just one pole**; that particular single-pole computation is prior work. The finding here is the uniform all-positive-mixture sharp extrema and the global no-mixing-improvement/rigidity identity; it does not claim the Zak criterion or the single-pole bound as new. General Zak-frame theory supplies the functional-analytic reduction but does not itself optimize the positive mixture over pole locations and weights.

The novelty assessment is provisional: an older special-function, Wiener–Hopf, positive-real-kernel, or Zak-transform treatment may contain an equivalent mixed-pole bound or the resulting universal optimum. Numerical computations and absence of search matches are not evidence of independence from such work.

## Limitations

The universal barrier depends crucially on positive residues and poles entirely on the same side of the real axis; cancellation can break the pointwise lower bound. The result is confined to rectangular **critical-density** lattices and describes only the extremal frame bounds, not the full spectral density or canonical dual windows. The \(q_j\)-weighted rigidity statement measures the effective contributions to the *lower* bound; it does not directly constrain the unweighted empirical pole distribution. It supplies no lower bound on physical time-frequency localization of the window, and does not claim global optimization outside the specified positive Cauchy class. Historical priority remains subject to independent literature review; no independent mathematical audit has been performed.

## References

1. Y. Belov, A. Kulikov, Y. Lyubarskii, *Gabor frames for rational functions*, arXiv:2103.08959, first publicly posted 2021-03-16; Inventiones mathematicae 231 (2023), 431–466, DOI 10.1007/s00222-022-01151-8. Relevant: Herglotz frame-set Theorem 1.1 and critical-fiber discussion.
2. Y. Belov, A. Kulikov, Y. Lyubarskii, *Gabor frame operator for the Cauchy kernel*, arXiv:2212.08915, first publicly posted 2022-12-17. Relevant: explicit single-pole Zak transform and optimal critical-density bounds in the introduction.
3. K. Gröchenig, *Foundations of Time-Frequency Analysis*, Birkhäuser (2001), Chapter 8. Relevant: critical Zak-transform frame criterion.
