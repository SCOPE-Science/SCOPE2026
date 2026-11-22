# A sharp two–three–four cluster threshold for single-Poisson approximation on the circle

## Finding

Let \(m\ge2\) be an integer, \(0<r<1\), and let the mean-one circle Poisson kernel be
\[
P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}.
\]
For the equal-mass mixture of \(m\) regularly spaced components, write
\[
F_{m,r}(\theta)=\frac1m\sum_{j=0}^{m-1}P_r(\theta-2\pi j/m)
=P_{r^m}(m\theta).
\]
Choose one Poisson component \(P_s(\theta-\phi)\), with \(0\le s<1\) and \(\phi\in\mathbb R/(2\pi\mathbb Z)\), to minimize the **population integrated squared error**
\[
E_{m,r}(s,\phi)=\frac1{2\pi}\int_0^{2\pi}|F_{m,r}(\theta)-P_s(\theta-\phi)|^2\,d\theta.
\]
The following phase classification is global, not merely stationary:

1. **Two components:** If \(0<r\le 1/\sqrt2\), the unique fitted density is uniform (\(s=0\)). If \(1/\sqrt2<r<1\), the unique fitted radius is \(s=\sqrt{t}\), where
   \[
   t=\frac{\sqrt2\,r-1}{\sqrt2\,r-r^2},
   \]
   and its two optimal directions are \(\phi=0,\pi\). Writing \(\delta=r^2-1/2\downarrow0\), the onset is continuous:
   \[
   s^2=2\delta+O(\delta^2),\qquad
   \min_{s,\phi}E_{2,r}(s,\phi)-E_{2,r}(0,0)=-4\delta^2+O(\delta^3).
   \]
2. **Three components:** Put
   \[
   u_c=\frac{3\sqrt6}{8},\quad r_c=\left(\frac{3\sqrt6}{8}\right)^{1/3},\quad s_c=\sqrt{\frac23}.
   \]
   For \(r<r_c\), the unique fitted density is uniform. At \(r=r_c\), both the uniform density and the three fitted kernels with radius \(s_c\) and directions \(\phi=2\pi j/3\) are global minimizers, and there are no others. For \(r>r_c\), the optimal fitted radius is unique, belongs to \((0,1)\), and occurs at precisely those three directions. It is the **larger** solution \(s\in(0,1)\) of
   \[
   \frac{1-r^3s^3}{\sqrt{s}(1-s^2)}=\sqrt{3r^3}.
   \]
   The transition is discontinuous: as \(r\downarrow r_c\) from above, the optimal radius tends to \(s_c>0\). With \(\eta=r^3-u_c\downarrow0\), its squared-error improvement has the sharp first-order law
   \[
   \min_{s,\phi}E_{3,r}(s,\phi)-E_{3,r}(0,0)
   =-\frac{32\sqrt6}{9}\,\eta+O(\eta^2).
   \]
3. **Four or more components:** For every \(m\ge4\) and every \(0<r<1\), the **uniform density is the unique** best-fitting single Poisson density; no positive concentration of a single component improves the integrated squared error.

At \(s=0\), all direction labels represent the same uniform density. Whenever \(s>0\) is optimal, the displayed source directions are exhaustive modulo \(2\pi\).

## Assumptions and scope

All errors and inner products are in \(L^2(\mathbb T,d\theta/(2\pi))\); the Poisson kernel is normalized to have mean one, not to integrate to one against unnormalized Lebesgue measure. The target has equal component weights, a common radius strictly inside the disk, and exact rotational symmetry. In the uniform-fit regime the exact irreducible squared error is \(2r^{2m}/(1-r^{2m})\), because \(\|F_{m,r}-1\|_2^2=2r^{2m}/(1-r^{2m})\). The fitted family permits the uniform endpoint \(s=0\). The loss is population integrated squared error, not likelihood, Hellinger, or Wasserstein distance. At the omitted endpoint \(r=1\), the target is not an \(L^2\) function; no statement about that boundary is asserted.

The primary harmonic-analysis aspect is the exact Fourier-mode selection under compression of an \(m\)-fold cyclic Poisson orbit to one Poisson kernel.

## Proof

**Step 1: aliasing and exact error.** For \(0\le a<1\), absolute convergence gives
\[
P_a(\theta)=1+2\sum_{n\ge1}a^n\cos(n\theta).
\]
Averaging its rotations by the \(m\)-th roots of unity annihilates all modes not divisible by \(m\), proving the asserted formula for \(F_{m,r}\). Parseval and the geometric series show
\[
\|P_s\|_2^2=1+\frac{2s^2}{1-s^2},\qquad
\langle F_{m,r},P_s(\cdot-\phi)\rangle
=1+2\sum_{\ell\ge1}(rs)^{m\ell}\cos(m\ell\phi).
\]
For every \(s>0\), each term in the latter series has strictly positive amplitude. Its unique maximizing phases are \(m\phi\in2\pi\mathbb Z\), because the first term already forces strict inequality at every other phase. Consequently, the difference from the uniform-fit error at the best angle is exactly
\[
\Delta_{m,r}(s):=\min_\phi E_{m,r}(s,\phi)-E_{m,r}(0,0)
=2g_{m,r}(s),\quad
g_{m,r}(s)=\frac{s^2}{1-s^2}-\frac{2(rs)^m}{1-(rs)^m}.
\tag{1}
\]
This reduction preserves the complete global optimization, including \(s=0\). For fixed \(r<1\), \(g_{m,r}(0)=0\), \(g_{m,r}(s)\to+\infty\) as \(s\uparrow1\), hence a minimizer exists.

**Step 2: the four-component barrier.** For \(m\ge4\), \((rs)^m\le s^4\), and \(x/(1-x)\) increases on \([0,1)\). For every \(0<s<1\), therefore,
\[
g_{m,r}(s)\ge\frac{s^2}{1-s^2}-\frac{2s^4}{1-s^4}
=\frac{s^2}{1+s^2}>0.
\]
Thus \(s=0\) is the unique minimizer for every \(m\ge4\).

**Step 3: the two-source continuous bifurcation.** Put \(u=r^2\) and \(t=s^2\). Equation (1) becomes \(g=t/(1-t)-2ut/(1-ut)\), and
\[
\partial_t g=\frac1{(1-t)^2}-\frac{2u}{(1-ut)^2}.
\]
The strictly increasing function \((1-ut)/(1-t)\) starts at one and diverges as \(t\uparrow1\). Hence, if \(u\le1/2\), the objective is strictly increasing on \((0,1)\). If \(u>1/2\), there is exactly one interior stationary point, a global minimum, obtained by setting \((1-ut)/(1-t)=\sqrt{2u}\). Solving gives the displayed \(t\), with \(\sqrt{2u}=\sqrt2\,r\). Expansion at \(u=1/2+\delta\) yields \(t=2\delta+O(\delta^2)\); substitution into (1) yields \(2g=-4\delta^2+O(\delta^3)\).

**Step 4: the three-source first-order transition.** Put \(u=r^3\). Elementary positive-denominator rearrangement gives, for \(s>0\),
\[
g_{3,r}(s)<0\ \Longleftrightarrow\ 1<u(2s-s^3).
\tag{2}
\]
On \([0,1]\), the function \(h(s)=2s-s^3\) has a unique maximum at \(s_c=\sqrt{2/3}\), with \(h(s_c)=4\sqrt{2/3}/3\). Its reciprocal is precisely \(u_c=3\sqrt6/8\). Therefore (2) proves uniform global optimality below \(u_c\), exactly two types of global minimizer at \(u_c\), and strict superiority of a nonuniform fit above \(u_c\).

It remains to prove that the superior positive-radius minimizer is unique. Differentiating (1), its positive stationary points satisfy
\[
R_u(s):=\frac{1-us^3}{\sqrt{s}(1-s^2)}=\sqrt{3u}.
\tag{3}
\]
The sign of \(R_u'(s)\) is the sign of
\[
Q_u(s)=-1+5s^2-5us^3+us^5,\qquad
Q'_u(s)=5s(2-3us+us^3)>0.
\]
The last inequality follows from \(0<u<1\) and \(2-3s+s^3=(1-s)^2(s+2)>0\) for \(0<s<1\). Since \(Q_u(0)=-1\) and \(Q_u(1)=4(1-u)>0\), \(R_u\) decreases to exactly one minimum and then increases to infinity, with \(R_u(s)\to\infty\) also as \(s\downarrow0\). Thus (3) has at most two roots. For \(u>u_c\), the existence of an \(s\) with \(g<0\), together with \(g(0)=0\), positivity immediately to the right of zero, and \(g(s)\to\infty\) at one, forces two stationary points. The first is a local maximum; the second (the larger root) is the *only* interior local minimum and hence the unique global minimizer. At \(u=u_c\), equality in (2) occurs only at \(s=s_c\), giving exactly the claimed coexistence.

For the first-order improvement, at \((u,s)=(u_c,s_c)\) one has \(u_c s_c^3=1/2\). The positive minimizer is nondegenerate: direct differentiation gives \(\partial_s^2g(u_c,s_c)=18\) (equivalently, the above derivative test gives \(Q_{u_c}(s_c)=1/6>0\)), so it continues smoothly for \(u>u_c\) close to criticality. The envelope derivative of (1) there is
\[
\left.\frac{\partial(2g)}{\partial u}\right|_{(u_c,s_c)}
=-\frac{4s_c^3}{(1-u_c s_c^3)^2}
=-\frac{32\sqrt6}{9}.
\]
Taylor's theorem proves the asserted linear improvement and \(s\to s_c\). This completes all cases.

## Verification

The accompanying standalone `checker.py` evaluates the exact Fourier error and independently approximates the defining circle integrals by periodic trapezoidal quadrature. It checks the three critical regimes, numerical global minima, angular optimality, the critical identities and the predicted one-sided scaling. These finite diagnostics are sanity checks; all quantifiers in the theorem are established by the preceding analytic proof, not by grid search. Running `python3 checker.py` requires only the Python standard library.

## Relationship to prior work

The Poisson (wrapped-Cauchy) family and its finite mixtures, including their Fourier or spherical-harmonic expansions and identifiability, are classical. Golzy and Markatou (arXiv:1803.04485, first posted 12 March 2018) analyze mixture identifiability and clustering; see their Sections 3–5 and Appendix A. Chaubey (arXiv:1601.05053, first posted 19 January 2016), in Sections 2–4, relates circular Poisson smoothing and Fourier-series density estimation. Baringhaus and Grübel (DOI 10.1007/s00362-023-01393-5, online 15 February 2023) discuss discrete mixture representations for spherical distributions and the wrapped-Cauchy Fourier expansion. Their established identities are used here, not claimed new.

The present result instead solves a different, explicit **one-component nonlinear \(L^2\) compression problem** for the entire equally spaced \(m\)-source orbit, with a sharp continuous transition for two sources, a coexisting first-order transition for three, and a no-fit-improvement theorem for four or more. The same-dimensional angular and radial fit is essential: a best centered/radial mixture fit is a different optimization problem. These literature comparisons support best-knowledge originality, not an exhaustive historical novelty guarantee.

## Limitations

Equal masses, a perfect regular orbit, a common radial parameter, and the population \(L^2\) criterion are essential to the claims. The theorem does not address arbitrary angular locations, unequal weights, finite-sample likelihood fitting, optimization over several fitted components, or the non-\(L^2\) boundary case \(r=1\). The exact classification does not infer that the mixture itself is uniform or that a statistical procedure cannot detect its harmonics; it describes only the optimal **single-Poisson \(L^2\) projection**. Historical priority remains open to independent specialist review.

## References

1. M. Golzy and M. Markatou, *Poisson Kernel-Based Clustering on the Sphere: Convergence Properties, Identifiability, and a Method of Sampling*, arXiv:1803.04485v1 (12 March 2018), https://arxiv.org/abs/1803.04485 .
2. Y. P. Chaubey, *Smooth Kernel Estimation of a Circular Density Function: A Connection to Orthogonal Polynomials on the Unit Circle*, arXiv:1601.05053v1 (19 January 2016), https://arxiv.org/abs/1601.05053 .
3. L. Baringhaus and R. Grübel, *Discrete mixture representations of spherical distributions*, *Statistical Papers* (online 15 February 2023), https://doi.org/10.1007/s00362-023-01393-5 .
