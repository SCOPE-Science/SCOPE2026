# Positive polar-paint accumulation and an algebraic active tail

## Finding

For the one-dimensional diffusive run-and-tumble model, let the first visit to each point permanently deposit a color equal to the current orientation. Starting with positive orientation, the expected excess length of positive over negative paint is strictly increasing in both elapsed time and nonnegative propulsion speed, despite its definition as a difference of two growing observables.

For every \(D>0\), \(\alpha>0\), and \(v\ge0\), its finite limiting value is
\[
\Delta_v(\infty)=\frac{2\sqrt{\alpha D+v^2}}{\alpha}.
\]
For each fixed \(v>0\), the gap has the sharp power-law asymptotic
\[
\Delta_v(\infty)-\Delta_v(t)\sim
\frac{2v^2}{\sqrt\pi\,\alpha^{3/2}\sqrt{\alpha D+v^2}}\,t^{-1/2}
\qquad(t\to\infty).
\]
For the passive endpoint \(v=0\), the known exact formula, included to exhibit the boundary, is
\[
\Delta_0(t)=2\sqrt{\frac D\alpha}\,\operatorname{erf}(\sqrt{\alpha t}),
\quad
\Delta_0(\infty)-\Delta_0(t)
\sim\frac{2\sqrt D}{\sqrt\pi\,\alpha}\,\frac{e^{-\alpha t}}{\sqrt t}.
\]
Thus any fixed positive propulsion produces an algebraically persistent polar-paint imbalance, whereas the passive model has an exponentially decaying memory. The passive identity itself is not claimed as new.

## Assumptions and scope

Let \(B_t\) be standard Brownian motion, independent of a continuous-time two-state chain \(S_t\in\{+1,-1\}\), flipping in either direction with intensity \(\alpha/2>0\). Start at \(X_0=0\), \(S_0=+1\), and set
\[
X_t=v\int_0^t S_u\,du+\sqrt{2D}B_t,\qquad D>0,\quad v\ge0.
\]
For each \(x\in\mathbb R\), define \(\tau_x=\inf\{t\ge0:X_t=x\}\) and the color \(S_{\tau_x}\) when the point is first reached. Define the finite-time color-excess expectation
\[
\Delta_v(t)=\int_{\mathbb R}\mathbb E_{0,+}\big[S_{\tau_x}\mathbf1_{\{\tau_x\le t\}}\big]dx.
\]
The integral exists because its absolute value is bounded by the mean range, which is finite at fixed time. Brownian nondegeneracy makes the color at first passage well-defined and the expected paint excess continuous in time. The sign convention is that the initially chosen orientation is positive; flipping that initial orientation reverses the signed excess. Strict monotonicity in \(v\) means \(\Delta_{v_2}(t)>\Delta_{v_1}(t)\) for every \(t>0\) and \(0\le v_1<v_2\), under otherwise identical parameters.

## Proof

**1. Backward first-passage representation.** For \(s>0\), take the Laplace transform of first-hit orientation on the negative half-line, starting a distance \(y>0\) from the target:
\[
h_\pm(y;s)=\mathbb E_{y,\pm}[e^{-s\tau_0}S_{\tau_0}].
\]
The bounded decaying solution satisfies the two backward equations
\[
D h_\pm''\pm v h_\pm'+\tfrac\alpha2(h_\mp-h_\pm)-s h_\pm=0,
\quad h_\pm(0;s)=\pm1,\quad h_\pm(\infty;s)=0.
\]
For targets to the right of the initial point, reflection changes the initial sign and the sign of the hit color. Thus integrating the transformed signed visits over both spatial half-lines gives
\[
F_v(s):=s\int_0^\infty e^{-st}\Delta_v(t)dt
=\int_0^\infty [h_+(y;s)-h_-(y;s)]dy.
\]
The decaying ansatz \(e^{-ky}\) yields two strictly positive spatial exponents \(k_1>k_2\) from
\[
D^2k^4-\{2D(s+\alpha/2)+v^2\}k^2+s(s+\alpha)=0.
\]
The associated eigenvectors can be taken as \((1,q_i)\), where \(q_i=-[Dk_i^2+v k_i-s-\alpha/2]/(\alpha/2)\). Enforcing the boundary data gives coefficients \(c_1=(-1-q_2)/(q_1-q_2)\) and \(c_2=(q_1+1)/(q_1-q_2)\). Consequently
\[
F_v(s)=\sum_{i=1}^2\frac{c_i(1-q_i)}{k_i}.
\]
Use \(Dk_1k_2=\sqrt{s(s+\alpha)}\) and
\[
D(k_1+k_2)=\sqrt{v^2+D(\sqrt s+\sqrt{s+\alpha})^2}.
\]
Simplifying the two-mode expression gives the exact transform
\[
\boxed{F_v(s)=\frac{2\sqrt{v^2+D(\sqrt s+\sqrt{s+\alpha})^2}}
{\sqrt{s+\alpha}(\sqrt s+\sqrt{s+\alpha})}}.
\]
These equations use the backward generator, so the state sign at the *first hitting instant*, rather than the state at the observation time, is correctly preserved.

**2. Positive-measure decomposition and strict time monotonicity.** Write
\[
W(s)=\sqrt s+\sqrt{s+\alpha},\qquad
G(s)=W(s)^2=2s+\alpha+2\sqrt{s(s+\alpha)}.
\]
Both \(W\) and \(G\) are complete Bernstein functions. For \(W\), this follows from addition of shifted principal square roots. For \(G\), on the upper complex half-plane the quantity \(\sqrt{z(z+\alpha)}\) has argument \([\arg z+\arg(z+\alpha)]/2\in(0,\pi)\); hence it and \(2z+\alpha\) have positive imaginary part, while \(G\) is positive on the positive real axis. This is the standard Pick characterization of complete Bernstein functions. Their reciprocals, as well as \((G+u)^{-1/2}\) for each \(u\ge0\), are completely monotone on the positive axis.

The elementary identity \(\sqrt{1+a/b}=1+\int_0^a[2\sqrt b\sqrt{b+u}]^{-1}du\), with \(b>0\), yields
\[
F_v(s)=\frac{2\sqrt D}{\sqrt{s+\alpha}}\left[
1+\int_0^{v^2/D}\frac{du}{2W(s)\sqrt{G(s)+u}}
\right].
\]
Every factor in the integral is completely monotone, and products and positive mixtures preserve complete monotonicity. By Bernstein's representation theorem, \(F_v\) is the Laplace transform of a finite nonnegative measure \(\mu_v\). Since \(F_v(s)\to0\) as \(s\to\infty\), it has no atom at time zero. Since \(F_v(s)/s\) is the Laplace transform of the original continuous \(\Delta_v(t)\), transform uniqueness gives \(\Delta_v(t)=\mu_v([0,t])\).

The first term of the decomposition has the strictly positive inverse-Laplace density
\[
\frac{2\sqrt D}{\sqrt{\pi t}}e^{-\alpha t},\qquad t>0.
\]
Therefore \(\Delta_v(t)\) is strictly increasing for all positive times, not merely nondecreasing. Further, if \(v_2>v_1\), the difference \(F_{v_2}-F_{v_1}\) is the integral of a positive completely monotone kernel over the nonempty interval \((v_1^2/D,v_2^2/D)\). Its representing measure gives positive mass to every positive time interval: each reciprocal factor has an inverse-Laplace measure with support accumulating at zero (its large-\(s\) decay is algebraic, not exponential), and convolution with the displayed strictly positive baseline density produces positive mass on every \((0,t)\). Thus the excess is also strictly increasing in propulsion speed \(v\).

**3. Exact saturation and active tail.** Since \(\mu_v\) is finite, its total mass is \(F_v(0+)\); the closed transform gives
\[
\mu_v([0,\infty))=\frac{2\sqrt{\alpha D+v^2}}{\alpha}.
\]
Expand \(F_v\) in \(q=\sqrt s\) at zero, with \(D,\alpha,v\) fixed:
\[
F_v(s)=C_v-K_v\sqrt s+O(s),\quad
C_v=\frac{2\sqrt{\alpha D+v^2}}{\alpha},\quad
K_v=\frac{2v^2}{\alpha^{3/2}\sqrt{\alpha D+v^2}}.
\]
Let \(R_v(t)=C_v-\Delta_v(t)\). This is nonnegative and nonincreasing. By Fubini and integration of the cumulative measure,
\[
\int_0^\infty e^{-st}R_v(t)dt=\frac{C_v-F_v(s)}s.
\]
For every fixed \(v>0\), the right-hand side is asymptotic to \(K_v s^{-1/2}\). The monotone form of Karamata's Tauberian theorem then gives
\[
R_v(t)\sim\frac{K_v}{\Gamma(1/2)}t^{-1/2},
\]
which is the displayed sharp coefficient. No finite numerical extrapolation is used to establish this infinite-time limit.

**4. Passive endpoint.** If \(v=0\), cancellation in the transform gives \(F_0(s)=2\sqrt D/\sqrt{s+\alpha}\). The inverse-Laplace density is the one displayed above. Its integral from zero to \(t\) is \(2\sqrt{D/\alpha}\operatorname{erf}(\sqrt{\alpha t})\). The standard complementary-error-function asymptotic proves the exponential tail. This exact passive formula was obtained in the source paper's journal Appendix B and is used here solely for comparison.

## Verification

The standalone `verify.py` requires only the Python standard library. Run `python verify.py` in the extracted directory. It reconstructs the two decaying roots and their boundary eigenvectors directly from the backward first-passage equations, without evaluating the closed transform inside that reconstruction, and compares the resulting integral with the theorem for a grid of diffusion, switching, propulsion and Laplace parameters. It additionally checks the passive transform and the small-frequency coefficient. The reproduced run completed 297 assertions/checks with maximal relative transform discrepancy below \(1.1\times10^{-14}\). Numerical consistency is auxiliary only; complete-monotonicity and the Tauberian step are mathematical arguments above.

## Relationship to prior work

Sezik, Britton, Touma and Pruessner derive the full state-dependent first-visit transform for the same diffusive run-and-tumble particle. Their preprint, first public in March 2026, gives the general transform in equation (24) and computes only the leading \(\sqrt t\) term of separately colored volumes in equation (25), with an unspecified order-one remainder. The subsequent journal version gives the exact *passive* color imbalance in Appendix B, equations (B8)–(B11). Accordingly, the model, general transform, leading explored-volume terms and the passive endpoint are prior results: the present statement is a further analytical consequence of the published transform, not an independent derivation of a new underlying process. Its distinct contributions are a positive-measure monotonicity mechanism, strict ordering in time and propulsion, the closed finite active saturation, and the sharp nonzero-propulsion algebraic approach coefficient.

Malakar and collaborators established backward first-passage equations and survival laws for related one-dimensional run-and-tumble dynamics with Brownian diffusion. Their approach motivates the independent verification but does not classify permanent first-visit orientation-paint excess. General complete Bernstein and Tauberian results are standard mathematical inputs. The central priority risk is that the parent general transform already encodes the answer algebraically; the present value lies in proving the qualitative sign/monotonicity and singular decay-class change, not in claiming a new transform method.

## Limitations

The result assumes a translation-invariant infinite line, independent Brownian forcing with strictly positive diffusivity, exponentially switching two-state orientation, and permanent first-hit paint. The tail statement holds with \(v>0\) fixed and is not uniform as \(v\downarrow0\). The effect is at the expected-volume level; it is not an almost-sure sign theorem for individual paint realizations. Neither a many-particle interacting extension nor a higher-dimensional classification is established. The parent transform is known; independent publication-priority assessment has not been performed.

## References

1. E. Sezik, C. Britton, A. Touma and G. Pruessner, *Run, Tumble and Paint*, arXiv:2603.24277, first posted 25 March 2026, https://arxiv.org/abs/2603.24277. Revised publication: *Journal of Physics A* **59** (2026) 285001, https://doi.org/10.1088/1751-8121/ae85eb.
2. K. Malakar et al., *Steady-state, relaxation and first-passage properties of a run-and-tumble particle in one-dimension*, arXiv:1711.08474, https://arxiv.org/abs/1711.08474.
3. R. L. Schilling, R. Song and Z. Vondraček, *Bernstein Functions: Theory and Applications*, 2nd ed., De Gruyter (2012), https://doi.org/10.1515/9783110269338.
4. Classical monotone Karamata Tauberian theorem; used only in the standard nonnegative monotone-function setting.
