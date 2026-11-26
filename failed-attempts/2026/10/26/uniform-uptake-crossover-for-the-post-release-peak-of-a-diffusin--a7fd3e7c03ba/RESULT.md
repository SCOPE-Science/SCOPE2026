# Uniform uptake crossover for the post-release peak of a diffusing point-source pulse

## Finding

A finite-duration constant point release in an infinite homogeneous three-dimensional diffusion medium produces an observation peak *after* release ends. More precisely, the familiar three-dimensional diffusion kernel with a nonnegative first-order removal rate has a unique post-release peak. A new uniform asymptotic formula resolves its lag as the release duration becomes long, even when the removal rate varies with duration.

Fix an observation distance \(r>0\), effective diffusivity \(D^*>0\), and extracellular volume fraction \(\alpha>0\). Set \(a=r^2/(4D^*)\) and \(p=3/2\). For a release duration \(T>0\) and a spatially homogeneous first-order removal rate \(k\geq0\), write \(t_*(T,k)=T+\delta(T,k)\) for the unique concentration-peak time. Put
\[
B_T=\log(T/a)+\log p + kT/p.
\]
**Uniform peak-lag theorem.** As \(T/a\to\infty\), uniformly for *all* \(k\geq0\), including arbitrary \(k=k(T)\),
\[
\boxed{\delta(T,k)=\frac{a}{p\{B_T+\log B_T+O(\log B_T/B_T+a/T)\}}.}
\]
The constants in this assertion are independent of \(k\), for fixed \(a,p\). The asymptotic is meaningful once \(T/a\) is sufficiently large that \(B_T>1\). In particular, zero removal gives \(\delta\sim 2a/[3\log(T/a)]\), whereas fixed positive removal gives \(\delta\sim a/(kT)\). If \(k(T)T/[p\log(T/a)]\to c\in[0,\infty)\), then \(\delta\sim a/[p(1+c)\log(T/a)]\). This identifies the sharp logarithmic-to-inverse-duration crossover at \(kT\asymp\log(T/a)\).

## Assumptions and scope

The setting is the infinite space \(\mathbb R^3\), initially at zero concentration, with a point source of constant strength \(Q>0\) during \(0<t<T\) and no source afterward. The medium has constant diffusivity \(D^*>0\), uniform extracellular fraction \(\alpha>0\), and spatially homogeneous irreversible first-order loss \(k\ge0\). At any observation point of radial separation \(r>0\), concentration is the causal convolution
\[
C_T(t)=\frac{Q}{\alpha(4\pi D^*)^{3/2}}
\int_{\max\{0,t-T\}}^{t}s^{-3/2}\exp(-a/s-ks)\,ds,
\qquad a=\frac{r^2}{4D^*}.
\]
The integrand is understood to vanish at \(s=0\). Peak timing is independent of \(Q\) and \(\alpha\), although peak *height* is not. This is a controlled idealization, not a theorem for finite tissue, anisotropic transport, concentration-dependent uptake, adsorption with memory, or cellular microstructure.

## Proof

**Step 1: existence, uniqueness, and localization.** Write \(h(s)=s^{-p}\exp(-a/s-ks)\) for \(s>0\), with \(p=3/2\). Its logarithmic derivative is
\[
\frac{h'(s)}{h(s)}=\frac{a}{s^2}-\frac{p}{s}-k.
\]
Thus \(h\) increases on \((0,m)\) and decreases on \((m,\infty)\), for the unique mode \(m=2a/[p+\sqrt{p^2+4ak}]>0\). For \(0<t<T\), \(C_T'(t)\) is a positive multiple of \(h(t)>0\). For \(t>T\), \(C_T'(t)\) is a positive multiple of \(h(t)-h(t-T)\). With \(d=t-T\), the difference is positive if \(T+d\le m\) and negative if \(d\ge m\). In the remaining interval \(\max\{0,m-T\}<d<m\), \(h(d)\) strictly increases whereas \(h(T+d)\) strictly decreases, and their values cross exactly once. Consequently \(t_*=T+\delta\) is the unique global maximizer and \(0<\delta<m\), \(t_*>m\). In particular, \(\max\{T,m\}<t_*<T+m\).

**Step 2: exact peak equation.** The positive equality \(h(\delta)=h(T+\delta)\), with \(\delta\in(0,m)\), is equivalent to
\[
\frac a\delta-\frac a{T+\delta}
=p\log(1+T/\delta)+kT.\tag{1}
\]
Set \(z=a/(p\delta)\) and \(B_T=\log(T/a)+\log p+kT/p\). Since \(m\le a/p\), we have \(z>1\). Rearranging (1) exactly yields
\[
z-\log z=B_T+E_T(z),\quad
E_T(z)=\log\left(1+\frac{a}{pTz}\right)+\frac{a}{p[T+a/(pz)]}.\tag{2}
\]
For all \(z\ge1\), \(k\ge0\), and \(T>0\),
\[
0<E_T(z)\le\frac{2a}{pT}.\tag{3}
\]
Notice that the removal parameter has disappeared from the error bound.

**Step 3: inversion with a uniform remainder.** Let \(B=B_T\). By (2)–(3), \(z-\log z=B+O(a/T)\), where the implied constant is universal for fixed \(p\) and independent of \(k\). Since \(B\ge\log(T/a)+\log p\to\infty\), the relevant solution satisfies \(z>1\), grows without bound, and obeys \(z\ge B\). The strictly increasing map \(x\mapsto x-\log x\) on \((1,\infty)\) has inverse
\[
(x-\log x)^{-1}(B)=B+\log B+O(\log B/B).\tag{4}
\]
Indeed, substituting \(x=B+\log B\) gives \(x-\log x=B-\log(1+\log B/B)=B+O(\log B/B)\); the derivative \(1-1/x\) is at least \(1/2\) for sufficiently large \(B\), so the mean-value theorem bounds the inverse error. The perturbation \(O(a/T)\) from (3) changes the inverse by at most a uniform \(O(a/T)\). Equation (2) therefore yields
\[
z=B+\log B+O(\log B/B+a/T).
\]
Using \(\delta=a/(pz)\) gives the boxed formula. Since \(kT/p\) competes with \(\log(T/a)\) inside \(B\), the three stated regimes follow directly. This establishes the theorem for every nonnegative sequence \(k=k(T)\), not merely for fixed \(k\).

**Step 4: finite-duration monotonicity (context).** For fixed \(k\), implicit differentiation of \(h(\delta)=h(T+\delta)\), with \(h'(\delta)>0>h'(T+\delta)\), gives
\[
\frac{\partial\delta}{\partial T}=
\frac{h'(T+\delta)}{h'(\delta)-h'(T+\delta)}\in(-1,0).
\]
Thus the lag decreases strictly as duration increases, while the absolute peak time moves later at speed in \((0,1)\). This qualitative result is included for interpretation, not asserted to be new.

## Verification

The accompanying pure-Python `verification.py` independently solves the exact log-ratio equation by bisection and checks the peak bracket, the sign equation, duration monotonicity, and the long-duration regimes over specified positive grids. Run `python verification.py` with a current Python 3 interpreter. These finite computations illustrate but do not establish the uniform, infinite-range theorem; its proof is Steps 1–3 above. The equations can also be checked by substituting the Gaussian fundamental solution into the linear diffusion-with-loss equation and applying a rectangular temporal convolution.

## Relationship to prior work

Remmers et al. (1997, DOI below) calculated concentration curves for a three-second glycine iontophoresis pulse; their Fig. 7 and associated text describe concentration peaking *after* the pulse at greater observation distances. Their model ignores first-order loss and reports no large-duration uniform lag crossover. Syková and Nicholson (2008), especially their Eq. (13) and Eq. (14), give the classical constant point-source concentration response with and without first-order loss, for a nonzero extracellular volume fraction. Linear superposition of their step response reproduces the finite-duration convolution above. The source formulas are therefore acknowledged, not presented as new. An earlier quantitative peak-timing result for the physically different Glover–Balmer stream-depletion setting uses the identical loss-free kernel and establishes a unique peak, strict timing brackets and duration monotonicity; those qualitative consequences are likewise not the new contribution here. The asserted addition is the **sharp two-term uniform lag inversion across all nonnegative loss rates**, including the turnover from inverse-logarithmic to inverse-duration scaling.

## Limitations

No mathematical uniqueness of the asymptotic formula in all literature is claimed. The 1997 source was read for its diffusion curves and discussion, and the 2008 review's explicit diffusion equations were read through accessible indexed sections, but the full 2008 article was not exhaustively inspected, leaving a literature-coverage risk. A general asymptotic inverse-function result may subsume the algebraic inversion, and long-duration peak timing could have been derived in diffusion studies under different vocabulary. The result is not a statistical estimation formula and does not determine a loss rate from one observation. Uniformity refers to \(k\ge0\) at fixed \(a,p\), not to spatially variable loss or a simultaneous \(r\to0\) singular limit. The earliest verified exact public online date for the Remmers source is 2006-03-27 in the article's open online archive; its print issue appeared in 1997, but the inspected bibliographic record did not provide an exact original print day.

## References

- J. E. Remmers, S. A. Schultz, J. Wallace, R. Takeda and A. Haji, “A Modified Coaxial Compound Micropipette for Extracellular Iontophoresis and Intracellular Recording: Fabrication, Performance and Theory,” *Japanese Journal of Pharmacology* 75 (1997), 161–169. DOI: 10.1254/jjp.75.161. Open article and PDF: https://www.jstage.jst.go.jp/article/jphs1951/75/2/75_2_161/_pdf . Archive posting date 2006-03-27: https://www.jstage.jst.go.jp/browse/jjp/75/2/_contents/-char/ja .
- E. Syková and C. Nicholson, “Diffusion in Brain Extracellular Space,” *Physiological Reviews* 88 (2008), 1277–1340, especially Eqs. (13)–(14). DOI: 10.1152/physrev.00027.2007. Published online 2008-10-01. https://pmc.ncbi.nlm.nih.gov/articles/PMC2785730/ .
