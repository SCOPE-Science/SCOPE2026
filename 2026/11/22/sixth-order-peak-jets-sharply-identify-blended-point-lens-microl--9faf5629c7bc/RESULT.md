# Sixth-order peak jets sharply identify blended point-lens microlensing across arbitrarily many passbands

## Finding

Consider a point-source, point-lens microlensing event, observed in any fixed finite number \(m\geq1\) of photometric passbands, with independent unknown positive source and blend fluxes in each band. If its (noise-free) intensity curves are analytic near their common maximum, **all parameters are uniquely determined by the derivatives at the maximum through order six in just one passband, together with the peak value and curvature in the others.** This requires neither a measured pre-event baseline nor known source/blend colors.

The order six is **sharp** on the open parameter domain: derivatives through order five in *every* passband leave a continuous one-parameter family of distinct physically positive parameter choices, regardless of how many passbands are available. The first baseline- and amplitude-independent dimensionless peak-shape invariant is

\[
R=\frac{F''(t_0)F^{(6)}(t_0)}{F^{(4)}(t_0)^2}
=\frac{20}{9}\left(1+\frac{1}{(u_0^2+2)^2}\right),
\qquad \frac{20}{9}<R<\frac{25}{9}.
\]

Here \(u_0>0\) is the minimum lens-source separation in Einstein-radius units. Consequently the exact impact parameter is

\[
u_0=\sqrt{\sqrt{\frac{20}{9R-20}}-2}.
\]

The strict interval above is a necessary shape constraint for every such exact curve. It is not, by itself, a sufficient test of an arbitrary full light curve, and the result does not assert good statistical conditioning in noisy data.

## Assumptions and scope

Let \(m\in\mathbb N\) be arbitrary. Each passband \(j\in\{1,\dots,m\}\) records the *flux* (not logarithmic magnitudes)

\[
F_j(t)=B_j+S_j A\left(\sqrt{u_0^2+\frac{(t-t_0)^2}{T^2}}\right),
\quad
A(u)=\frac{u^2+2}{u\sqrt{u^2+4}},
\]

with \(u_0>0\), \(T>0\), \(S_j>0\), and \(B_j>0\). The blend fluxes \(B_j\) and unlensed source fluxes \(S_j\) are unconstrained across passbands; only \(t_0,u_0,T\) are shared. No parallax, finite-source, binary-lens, variable-blend, extinction-variation, or photometric noise terms are included. Time has a fixed known physical unit. The single maximum \(t_0\) is observable as the common maximizer of the complete analytic curves; its location is counted as part of the jet data. The \(k\)-jet means \(F_j^{(r)}(t_0)\) for all integers \(0\le r\le k\). The minimality statement concerns the open domain where every blend \(B_j\) is strictly positive; it need not hold with externally known source or baseline fluxes.

## Proof

**1. Unique peak and analytic reduction.** Put \(v=u_0^2>0\), \(q=T^{-2}>0\), \(h(v)=v(v+4)\), and \(g(v)=(v+2)/\sqrt{h(v)}\). Then \(F_j(t_0+x)=B_j+S_jg(v+qx^2)\). Since \(g'(v)=-4/h(v)^{3/2}<0\), each curve has a unique global maximum at \(x=0\). Its odd peak derivatives vanish.

**2. Exact derivative identities.** Direct differentiation, with all denominators positive on \(v>0\), yields

\[
\begin{aligned}
g'(v)&=-\frac4{h(v)^{3/2}},\\
g''(v)&=\frac{12(v+2)}{h(v)^{5/2}},\\
g'''(v)&=-\frac{48(v^2+4v+5)}{h(v)^{7/2}}.
\end{aligned}
\]

Writing \(J_{r,j}=F_j^{(r)}(t_0)\), the Taylor coefficients of \(g(v+qx^2)\) give

\[
J_{2,j}=2S_jqg'(v),\quad
J_{4,j}=12S_jq^2g''(v),\quad
J_{6,j}=120S_jq^3g'''(v).
\]

In particular \(J_{2,j}<0\), \(J_{4,j}>0\), and \(J_{6,j}<0\). Eliminating \(S_j\) and \(q\) gives, *identically in every passband*,

\[
\frac{J_{2,j}J_{6,j}}{J_{4,j}^2}
=\frac53\frac{g'(v)g'''(v)}{g''(v)^2}
=\frac{20}{9}\frac{v^2+4v+5}{(v+2)^2}
=\frac{20}{9}\left(1+\frac1{(v+2)^2}\right).
\]

Its derivative with respect to \(v\) is \(-40/[9(v+2)^3]<0\), with endpoint limits \(25/9\) as \(v\downarrow0\) and \(20/9\) as \(v\to\infty\). Thus it maps \((0,\infty)\) bijectively to \((20/9,25/9)\), and the displayed inversion uniquely recovers \(u_0\).

**3. Exact recovery of every unknown.** With \(v\) known, any one band's second and fourth peak derivatives give

\[
q=-\frac{v(v+4)}{18(v+2)}\frac{J_{4,j}}{J_{2,j}},
\qquad
S_j=-\frac{J_{2,j}[v(v+4)]^{3/2}}{8q},
\qquad
B_j=J_{0,j}-S_j\frac{v+2}{\sqrt{v(v+4)}}.
\]

These expressions are forced by the curve and recover \(T=q^{-1/2}\), then every other band's \(S_k,B_k\) from its second derivative and peak value. They establish injectivity of the sixth-order peak jets and an explicit inverse. The reconstructions have \(q,S_j>0\) automatically for genuine model data; an arbitrary proposed jet needs the reconstructed \(B_j>0\) as an additional physical admissibility check.

**4. Sharp failure of all fifth-order multiband jets.** The quotient \(J_{4,j}/J_{2,j}=6qg''(v)/g'(v)\) is the *same* for every band. Fix the complete fifth jets of a parameter choice with every \(B_j,S_j>0\), and call this common quotient \(H<0\). For each \(v'\) sufficiently close to (but not equal to) \(v\), define

\[
\begin{aligned}
q'&=-\frac{v'(v'+4)}{18(v'+2)}H,\\
S_j'&=-\frac{J_{2,j}[v'(v'+4)]^{3/2}}{8q'},\\
B_j'&=J_{0,j}-S_j'\frac{v'+2}{\sqrt{v'(v'+4)}}.
\end{aligned}
\]

All quantities depend continuously on \(v'\), agree with the originals at \(v'=v\), and remain positive for sufficiently small perturbations. Each resulting distinct light curve has exactly the same zeroth, second, and fourth derivatives in *every* band. Its first, third, and fifth derivatives vanish as well. Hence the full fifth jets for any number of bands retain a one-dimensional ambiguity, even though there may be more scalar measurements than unknown parameters. This proves sharp minimality.

**5. Conditioning boundary.** The exact shape derivative satisfies \(dR/dv=-40/[9(v+2)^3]\). Thus the inverse sensitivity \(|dv/dR|=9(v+2)^3/40\) diverges for large impact parameter; formal identifiability does not imply stable finite-noise estimation.

## Verification

The standalone standard-library file `check_peak_jet.py` evaluates the derivative identities and recovery equations at exact-rational parameters represented with high-precision decimal radicals. It also constructs explicit, distinct positive-parameter multiband models with identical fifth jets and different sixth derivatives. A recorded execution completed 22,222 assertions without failure. This finite diagnostic checks arithmetic and implementation; the infinite-domain statement is proved analytically in the preceding section.

A checkable exact example is \(v=1\), \(q=1/4\), \(S=3\), \(B=5\), for which

\[
F(t_0)=5+\frac9{\sqrt5},\quad J_2=-\frac6{5\sqrt5},\quad
J_4=\frac{81}{25\sqrt5},\quad J_6=-\frac{108}{5\sqrt5},\quad
R=\frac{200}{81}.
\]

The recovery formulas return exactly \(u_0=1\), \(T=2\), \(S=3\), \(B=5\).

## Relationship to prior work

The point-source/point-lens magnification law is classical. Woźniak and Paczyński (1997) analyzed near-degeneracies caused by blending in practical finite-noise observations, particularly at large or small impact parameters. Han (1999) gave analytic relations for the biases in peak magnification and event duration when blending is ignored. Smith et al. (2007) studied realistic blended-event recovery with Monte Carlo simulations. Dominik (2008 preprint; 2009 journal) analyzed feature-based parameterization and noted that, in principle, a nonlocal slope at the half-maximum epoch distinguishes impact parameters, though weakly. Those results concern fitting, asymptotic shapes, or nonlocal light-curve features. The present precise question is which *local peak derivative order* first determines the full model with freely unknown affine flux levels in arbitrary bands. The inspected primary texts do not give this sharp sixth-order formula or the all-passband fifth-order ambiguity. This observation does not certify global publication priority; historical literature and mathematical equivalences remain potential sources of overlap.

## Limitations

The result is a deterministic structural-identifiability theorem, not a usable guarantee of stable inference. High-order derivative estimates amplify measurement noise, sparse cadence, and model misspecification; the inverse becomes extremely ill-conditioned for large \(u_0\). Allowing finite stellar disks, binary lenses, varying blend flux, parallax, or known cross-band spectral constraints changes the problem. Knowing the baseline or a source flux externally may reduce the required jet order. The invariant interval is necessary only for the stipulated exact model; it does not authenticate astrophysical microlensing against all alternatives.

## References

1. P. Woźniak and B. Paczyński, *Microlensing of Blended Stellar Images*, arXiv:astro-ph/9702194, publicly submitted 1997-02-21, https://arxiv.org/abs/astro-ph/9702194.
2. C. Han, *Analytic Relations between the Observed Gravitational Microlensing Parameters With and Without the Effect of Blending*, arXiv:astro-ph/9810401; *MNRAS* 309 (1999), 373–378, https://doi.org/10.1046/j.1365-8711.1999.02832.x.
3. M. C. Smith, P. Woźniak, S. Mao, and T. Sumi, *Blending in Gravitational Microlensing Experiments: Source Confusion and Related Systematics*, arXiv:0707.0550, 2007, https://arxiv.org/abs/0707.0550.
4. M. Dominik, *Parameter degeneracies and (un)predictability of gravitational microlensing events*, arXiv:0811.4173, publicly submitted 2008-11-25; *MNRAS* 393 (2009), 816–821, https://arxiv.org/abs/0811.4173.
