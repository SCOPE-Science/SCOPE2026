# A sharp unimodal–trimodal–bimodal transition in a two-state run-and-tumble particle

## Finding
Consider the one-dimensional two-orientation velocity-jump process with rightward speed \(v_+(x)=2-\tanh(ux)\), leftward speed \(v_-(x)=2+\tanh(ux)\), and orientation-switching rates \(\gamma_\pm(x)=1\pm\tanh(3ux)\), where \(u>0\). Its normalized, smooth, even stationary position density \(p_u\) has this **complete phase diagram**:

- For \(0<u\le 25/4\), its only local maximum is at the origin; it is strictly decreasing on \((0,\infty)\), though at \(u=25/4\) the derivative vanishes at one additional positive point without changing sign.
- For \(25/4<u<7\), it has **exactly three strict local maxima**, at \(0\) and at \(\pm x_+(u)\), separated by the two strict local minima \(\pm x_-(u)\).
- For \(u\ge7\), it has exactly two strict local maxima at \(\pm x_+(u)\); the origin is a strict local minimum, with a vanishing quadratic term at \(u=7\).

For \(25/4<u<7\), let \(z_-(u)<z_+(u)\) be the two roots in \((0,1)\) of
\[
u(1+2z-3z^2)=7+5z.
\]
Then \(x_\pm(u)=u^{-1}\operatorname{arctanh}\sqrt{z_\pm(u)}\). For \(u\ge7\), only the larger positive root remains (at \(u=7\), the other root is zero). In particular, at \(u=13/2\), the two positive squared-hyperbolic-tangent coordinates are exactly \(1/13\) and \(1/3\):
\[
x_- =\frac2{13}\operatorname{arctanh}\frac1{\sqrt{13}},\qquad
x_+ =\frac2{13}\operatorname{arctanh}\frac1{\sqrt3}.
\]

More generally, for the saturating-rate family \(v_\pm(x)=v_0\mp v_1\tanh(ux)\), \(\gamma_\pm(x)=\gamma_0\pm\gamma_1\tanh(gx)\), with \(v_0>v_1>0\), \(\gamma_0\ge\gamma_1>0\), \(u>0\) and \(0\le g\le u\), the stationary density has **at most two local maxima**. Thus a tumbling gradient steeper than the speed gradient is necessary for trimodality within this positive-parameter family, and the stated \(g=3u\) subfamily shows it is possible.

## Assumptions and scope
The process is on the entire real line, without translational diffusion. In orientation \(+\), it moves deterministically to the right at \(v_+(x)>0\); in orientation \(-\), it moves to the left at \(v_-(x)>0\). Orientation changes are independent conditional-rate jumps at the displayed \(\gamma_\pm(x)\). For the sharp phase diagram, the speed scales and switching amplitudes are fixed as stated, while \(u>0\) varies and the tumbling spatial gradient is \(g=3u\). Rates remain positive at every finite position and velocities are bounded between \(1\) and \(3\). A *mode* means a local maximum of the marginal stationary position density, not a maximum of either orientation-resolved density.

## Proof
**Stationarity and normalization.** A stationary zero-current solution of the coupled transport equations must have
\[
p_\pm(x)=\frac{C}{v_\pm(x)}e^{I(x)},\qquad
I'(x)=\frac{\gamma_-(x)}{v_-(x)}-\frac{\gamma_+(x)}{v_+(x)}.
\]
Indeed \(v_+p_+=v_-p_-=Ce^{I}\), so both stationary forward equations vanish. With the stated parameters, writing \(z=\tanh^2(ux)\), elementary triple-angle and partial-fraction identities give the explicitly normalized-at-zero expression
\[
\frac{p_u(x)}{p_u(0)}=
\frac4{4-z}(1-z)^{1/u}(1+3z)^{-4/(13u)}
\left(\frac{4-z}{4}\right)^{-9/(13u)}.
\]
This is positive, smooth and even. As \(|x|\to\infty\), \(1-z\sim4e^{-2u|x|}\), and the remaining factors approach positive constants. Hence \(p_u(x)\asymp e^{-2|x|}\), so a finite normalizer exists and the displayed solution defines a stationary probability density.

**Exact mode count.** Differentiating the stationary density for \(x>0\) and setting \(z=\tanh^2(ux)\) yields
\[
\frac{p_u'(x)}{p_u(x)}=
\frac{2\tanh(ux)}{(4-z)(1+3z)}
\bigl[u(1+2z-3z^2)-(7+5z)\bigr].
\]
All factors outside the square bracket are strictly positive. Thus the sign is that of \(u-U(z)\), where
\[
U(z)=\frac{7+5z}{(1-z)(1+3z)},\quad
U'(z)=\frac{3(5z-1)(z+3)}{(1+2z-3z^2)^2}.
\]
On \((0,1)\), \(U\) decreases strictly until \(z=1/5\) and increases strictly afterward. Its endpoint and minimum values are
\[
U(0)=7,\quad U(1/5)=25/4,\quad
\lim_{z\uparrow1}U(z)=+\infty.
\]
Therefore no positive derivative sign change occurs for \(u\le25/4\); two positive critical points with derivative signs negative–positive–negative occur for \(25/4<u<7\); and one positive critical point with derivative signs positive–negative occurs for \(u\ge7\). Evenness completes the mode count. At \(u=25/4\), the isolated double zero at \(z=1/5\) does not create an extremum. At \(u=7\), the zero at \(z=0\) gives a strict quartic minimum at the origin: the leading term of \(\log[p_u(x)/p_u(0)]\) is \((9u^3/8)x^4\) evaluated at \(u=7\). At \(u=13/2\), the critical polynomial factors exactly as \(-\tfrac12(13z-1)(3z-1)\), proving the stated locations.

**Why the relative spatial gradient matters.** In the general family, the stationary logarithmic derivative for \(x>0\) is
\[
\frac{p'(x)}{p(x)}=\frac{2\tanh(ux)}{v_0^2-v_1^2\tanh^2(ux)}
\left[uv_1^2\operatorname{sech}^2(ux)-\gamma_0v_1
-\gamma_1v_0\frac{\tanh(gx)}{\tanh(ux)}\right].
\]
When \(0<g\le u\), the ratio \(R(x)=\tanh(gx)/\tanh(ux)\) is nondecreasing because
\[
\frac{R'(x)}{R(x)}=2\left[\frac g{\sinh(2gx)}-\frac u{\sinh(2ux)}\right]\ge0;
\]
for fixed \(x>0\), \(a/\sinh(2ax)\) decreases with \(a>0\). For \(g=0\), the ratio is identically zero. Consequently the bracket is strictly decreasing for \(x>0\), permitting at most one positive derivative zero, and thus at most two modes. No assumption about the number of extrema is used in either argument.

## Verification
Run the included standard-library checker as `python3 check_modes.py`. It checks the exact rational polynomial and derivative identities, the two rational critical roots at \(u=13/2\), sign patterns on all three sides of the phase boundaries, and independent finite-difference and numerical-integration diagnostics. In the packaged run, all **60 assertions passed**. The exact computations can also be reproduced by directly multiplying the displayed polynomials; the finite numerical tests are diagnostics, not a proof of uniqueness or of the continuum classification.

For illustration, at \(u=13/2\) the two positive extremum positions are approximately \(0.043816776925899\) and \(0.101304453609601\). The relative stationary heights are \(p_u(x_-)/p_u(0)\approx0.999343155092512\) and \(p_u(x_+)/p_u(0)\approx1.001088504664840\). Their closeness emphasizes why an analytic sign count matters.

## Relationship to prior work
Jain and Chatterjee (2024) introduced precisely this saturating-rate family, derived the exact stationary solution (their equations (3)–(4), (7), and Appendix A), and wrote the implicit extrema equation (15). Their proposed unimodal/bimodal classification (16)–(17) explicitly assumes that there are at most two maxima, on the basis of special parameter choices. The sharp \(g=3u\) phase diagram shows that this additional assumption does not hold throughout the stated nonnegative-parameter model. In particular, their criterion reduces to a central-curvature boundary at \(u=7\), whereas a pair of side extrema already appears at \(u=25/4\). Their stationary formula and previously known special cases are fully credited; the contribution here is the exact global mode count, the additional trimodal phase and the structural gradient comparison.

The three-internal-state harmonic-trap run-and-tumble model of Basu and collaborators (2019) is not an equivalent formulation: its state space, confining mechanism, and stationary support differ. General spatially inhomogeneous velocity-jump asymptotics do not, merely by their formulation, establish this exact positive-density mode phase diagram.

## Limitations
The complete sharp transition is proved only on the specified one-parameter \(g=3u\) subfamily, while the no-trimodality statement covers the separate general region \(0\le g\le u\). A full six-parameter modality classification is not claimed. The result concerns smooth stationary marginal densities, not finite-time distributions, finite-sample inference, thermal diffusion, interacting particles, or experimental observation. Independent assessment of publication priority has not been performed.

## References
1. K. Jain and S. Chatterjee, *Run-and-tumble particle with saturating rates*, arXiv:2405.13521, first posted 2024-05-22; *Physical Review E* **110**, 064110 (2024). https://arxiv.org/abs/2405.13521; full-text https://arxiv.org/html/2405.13521v2
2. U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit and G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083 (2019). https://arxiv.org/abs/1910.10083
3. J. M. Newby and J. P. Keener, *An Asymptotic Analysis of the Spatially Inhomogeneous Velocity-Jump Process*, *Multiscale Modeling & Simulation* (2011), DOI:10.1137/10080676X. https://doi.org/10.1137/10080676X
