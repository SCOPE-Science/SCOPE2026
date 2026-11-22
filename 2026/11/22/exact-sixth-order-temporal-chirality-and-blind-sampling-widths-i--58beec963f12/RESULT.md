# Exact sixth-order temporal chirality and blind sampling widths in cyclic switching diffusion

## Finding

A Brownian displacement with a three-state cyclically switching diffusivity has exactly ordinary Brownian mean-square displacement and orientation-insensitive two-time squared-increment covariances, but an explicit three-window sixth-order statistic detects hidden circulation orientation when the ordered diffusivity labels are known. The statistic has an infinite, universal set of exactly blind observation widths, even when the microscopic cycle is irreversible.

Let \(\alpha,\beta>0\), let \(d_1,d_2,d_3>0\), and introduce
\[
c=\frac32(\alpha+\beta),\qquad
b=\frac{\sqrt3}{2}(\alpha-\beta),\qquad
\lambda=-c+ib,\qquad
V=(d_1-d_2)(d_2-d_3)(d_3-d_1).
\]
For \(h>0\) and \(u,v\geq0\), define the three disjoint squared increments
\[
Y_1=(X_h-X_0)^2,\quad
Y_2=(X_{2h+u}-X_{h+u})^2,\quad
Y_3=(X_{3h+u+v}-X_{2h+u+v})^2,
\]
and let \(M_h(u,v)=\mathbb E[Y_1Y_2Y_3]\). Then the *chronological gap-order contrast* \(\Delta_h(u,v)=M_h(u,v)-M_h(v,u)\) is
\[
\boxed{\displaystyle
\Delta_h(u,v)=\frac{16V}{3\sqrt3}\,e^{-c(u+v+h)}
\left|\frac{e^{\lambda h}-1}{\lambda}\right|^2
\frac{\sin(bh)}{b}\sin\bigl(b(u-v)\bigr).}
\]
The ratio \(\sin(bh)/b\) is defined by continuity as \(h\) when \(b=0\).

If \(\alpha\ne\beta\) and the three diffusivities are pairwise distinct, the statistic \(\Delta_h(u,v)\) is identically zero for *every* pair \(u,v\geq0\) precisely at the positive sampling widths
\[
\boxed{\displaystyle
h_n=\frac{2n\pi}{\sqrt3\,|\alpha-\beta|},\qquad n=1,2,\ldots.}
\]
At every other positive width, it is nonzero for generic unequal gaps and changes sign under reversal \(\alpha\leftrightarrow\beta\) with the ordered diffusivity triple held fixed. This is a classification of the specified statistic, not a claim that all observations at the exceptional widths become time-reversible.

## Assumptions and scope

The environment \(S_t\in\{1,2,3\}\) is the stationary continuous-time Markov chain whose transition rate from state \(i\) to \(i+1\pmod3\) is \(\alpha\) and to \(i-1\pmod3\) is \(\beta\). Its stationary distribution is uniform. An independent standard one-dimensional Brownian motion \(W_t\) drives
\[
X_t=\int_0^t\sqrt{2d_{S_s}}\,dW_s,\qquad X_0=0.
\]
All expectations are for the stationary environment and independent Brownian noise. There is no position drift or confining potential, and intervals defining the \(Y_j\) are disjoint (endpoints may touch). Rates and diffusivities are finite and strictly positive; gap lengths may vanish.

For all \(t\geq0\),
\[
\mathbb E[X_t]=0,\qquad
\mathbb E[X_t^2]=2\bar d\,t,\qquad
\bar d=(d_1+d_2+d_3)/3.
\]
All disjoint *linear* displacement increments have zero covariance. More strongly, the stationary two-time diffusivity covariance is
\[
\operatorname{Cov}(d_{S_0},d_{S_t})=
\frac13\sum_{i=1}^3(d_i-\bar d)^2e^{-ct}\cos(bt),
\]
which is unchanged by \(\alpha\leftrightarrow\beta\). Thus second moments of disjoint squared increments, obtained by integrating this covariance, cannot determine the hidden direction of circulation.

If \(\alpha\ne\beta\), the environment dissipates at the positive stationary entropy-production rate \((\alpha-\beta)\log(\alpha/\beta)\). If \(\alpha=\beta\), the environment is reversible and the contrast vanishes. The contrast also vanishes if any two diffusivities coincide; this observable does not identify the hidden orientation in that degenerate case.

## Proof

**1. Matrix representation and two-time invisibility.** Let \(P\) be the cyclic permutation matrix with \(P_{12}=P_{23}=P_{31}=1\) and let
\[
Q=\alpha(P-I)+\beta(P^\mathsf T-I),\qquad A=\operatorname{diag}(d_1,d_2,d_3).
\]
As the chain starts uniformly, \(\mathbb E[d_{S_0}d_{S_t}]=\frac13\mathbf1^\mathsf T A e^{Qt}A\mathbf1\). The nonconstant Fourier eigenvalues of \(Q\) are \(\lambda\) and \(\bar\lambda\). Their conjugate contributions give the covariance above, which is even in \(b\).

**2. The antisymmetric three-time diffusivity moment.** Put
\[
F(s,t)=\frac13\mathbf1^\mathsf T A e^{Qs}A e^{Qt}A\mathbf1.
\]
Define \(J=\mathbf1\mathbf1^\mathsf T/3\), \(R=(P-P^\mathsf T)/\sqrt3\), and
\[
E_+=(I-J-iR)/2,\qquad E_-=(I-J+iR)/2.
\]
These projectors satisfy \(e^{Qt}=J+e^{\lambda t}E_++e^{\bar\lambda t}E_-\). Terms involving the stationary mode or two equal Fourier modes are invariant under exchanging \(s,t\). The coefficient of the mixed term is
\[
C=\frac13\mathbf1^\mathsf T A E_+ A E_- A\mathbf1,
\qquad \operatorname{Im}C=-\frac{V}{6\sqrt3}.
\]
The coefficient identity follows by multiplying the displayed three-by-three matrices; it can also be reconstructed symbolically by the included independent checker. Pairing the complex-conjugate mixed terms yields the all-parameter identity
\[
\boxed{F(s,t)-F(t,s)=\frac{2V}{3\sqrt3}
 e^{-c(s+t)}\sin\bigl(b(s-t)\bigr).}
\]
No limiting or small-time approximation enters this identity.

**3. Conditional Gaussian reduction.** Given the complete environment path, each nonoverlapping displacement increment is an independent centered Gaussian with variance twice the diffusivity integrated over its window. Hence
\[
M_h(u,v)=8\int_0^h\!\int_0^h\!\int_0^h
F(h+u+t-s,\ h+v+z-t)\,ds\,dt\,dz.
\]
Interchanging the gaps \(u,v\) and reversing the three integration variables maps the second triple product to the reversed ordering of the time arguments. Thus the contrast is eight times the triple integral of the antisymmetric kernel in Step 2.

**4. Exact integration.** In the antisymmetric kernel, represent the sine by the imaginary part of \(e^{ib(s-t)}\). With \(\lambda=-c+ib\), the three separated integrations factor; in particular the two end windows contribute conjugate factors, and the middle window contributes \(\int_0^h e^{-ibt}\,dt\). Algebraic evaluation gives
\[
\int_{[0,h]^3}\!e^{-c(2h+u+v+z-s)}
\sin\bigl(b(u-v+2t-s-z)\bigr)\,ds\,dt\,dz
=
 e^{-c(u+v+h)}
\left|\frac{e^{\lambda h}-1}{\lambda}\right|^2
\frac{\sin(bh)}b\sin\bigl(b(u-v)\bigr).
\]
Inserting the Step 2 coefficient and the Gaussian variance factor \(8\) proves the boxed formula. All integrals are over compact intervals of bounded continuous functions, so no exchange of improper limits is required.

**5. Complete blind-width classification.** For \(h>0\), \(\Re\lambda=-c<0\) implies \(e^{\lambda h}\ne1\), so the modulus-squared factor is strictly positive. Under \(\alpha\ne\beta\) and \(V\ne0\), the only factor that can make the contrast zero for *every* choice of gaps is \(\sin(bh)\). Its strictly positive zeros are exactly the displayed \(h_n\); at all other widths one can choose \(u,v\geq0\) with \(\sin(b(u-v))\ne0\). Swapping clockwise and counterclockwise rates negates \(b\), leaving all other factors invariant and reversing the contrast sign. This completes the proof.

## Verification

The included standalone `check.py` checks the critical symbolic identity \(\operatorname{Im}C=-V/(6\sqrt3)\) exactly with SymPy, compares the three-time formula against independent matrix exponentials, and compares the integrated sixth-order contrast against direct three-dimensional Gaussian quadrature of the original Markov kernel. It also evaluates degenerate cases and the first four exact blind widths. The run passed **66 assertions** with NumPy, SciPy and SymPy. These finite numerical comparisons are independent diagnostics; the complete global statements follow from the matrix and integral proof above.

To reproduce: `python check.py` (requires Python 3, NumPy, SciPy and SymPy). The script is fully embedded with this finding, with no network access, random seeds, external data or other project files required.

## Relationship to prior work

Grebenkov's 2019 *Time-averaged MSD for switching diffusion* supplies the general Markov-modulated diffusion propagator and multi-time framework and primarily analyzes two-state time-averaged MSD statistics; the present chain and six-order contrast use that framework. Ślęzak, Burnecki and Metzler's 2019 *Random coefficient autoregressive processes describe Brownian yet non-Gaussian diffusion in heterogeneous systems* develops the conditional-Gaussian heterogeneous-diffusion viewpoint. Lucente and collaborators' 2023 *Statistical Features of Systems driven by non-Gaussian Processes: Theory & Practice* discuss higher-order time-reversal signatures. Existing work on stroboscopic reversibility of biased Markov rings classifies exceptional sampling delays of the hidden chain; it does not itself calculate the time-integrated, three-window squared-displacement contrast. The new scope here is the explicit Vandermonde-dependent sixth-order contrast, its strict orientation dependence and its complete infinite blind-width lattice for integrated displacement observations.

## Limitations

The contrast determines the orientation only relative to a known ordered assignment of diffusivities to the three states; it does not identify an absolute clockwise direction from unlabelled mobility data. This is an exact result for a homogeneous three-state nearest-neighbor cycle and three disjoint windows of *equal* duration. It does not classify general hidden Markov environments, overlapping windows, arbitrary measurement nonlinearities, or the full observed path-law irreversibility at exceptional widths. As with any high-order statistical diagnostic, finite-sample errors may obscure its theoretically nonzero value. General published propagator and stroboscopic-reversibility results provide strong conceptual antecedents, and independent evaluation is needed before any publication-priority assertion.

## References

1. D. S. Grebenkov, *Time-averaged MSD for switching diffusion*, 2019, arXiv:1903.04783v1, first publicly submitted 2019-03-12, https://arxiv.org/abs/1903.04783 .
2. M. Ślęzak, K. Burnecki and R. Metzler, *Random coefficient autoregressive processes describe Brownian yet non-Gaussian diffusion in heterogeneous systems*, 2019, arXiv:1904.08737, https://arxiv.org/abs/1904.08737 .
3. D. Lucente et al., *Statistical Features of Systems driven by non-Gaussian Processes: Theory & Practice*, 2023, arXiv:2306.14558, https://arxiv.org/abs/2306.14558 .
4. *Crystallographic restriction on stroboscopic detailed-balance aliasing in biased Markov rings*, published mathematical note, 2026 (related spectral and sampled-chain boundary; not a derivation of the integrated sixth-order contrast).
