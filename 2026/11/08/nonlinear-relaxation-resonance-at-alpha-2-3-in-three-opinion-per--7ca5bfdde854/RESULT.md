# Nonlinear relaxation resonance at \(\alpha=2/3\) in three-opinion persuasion–polarization dynamics

## Finding
Consider the three-opinion version of the iterative persuasion–polarization (IPP) mean-field model of Cao and Reed, with persuasion probability \(0<\alpha<1\) and repulsion probability \(\beta=1-\alpha\). Let \(a(t),b(t),c(t)\) be the fractions holding opinions \(-1,0,1\), respectively, summing to one. There are three vertex equilibria and exactly one equilibrium with more than one positive component:
\[
(a_*,b_*,c_*)=\left(\frac{1-\alpha}{2-\alpha},\frac{\alpha}{2-\alpha},\frac{1-\alpha}{2-\alpha}\right).
\]
Every nonvertex initial probability vector converges to this interior equilibrium; the three vertices themselves remain fixed.

The relaxation has a **sharp nonlinear resonance** that is absent from the three special persuasion parameters studied in the initiating paper. Set
\[
\kappa=2-\alpha,\quad \lambda=\frac{\alpha(1-\alpha)}{2-\alpha},\quad
x(t)=b(t)-b_*,\quad d(t)=c(t)-a(t).
\]
For every nonvertex initial condition with \(d(0)\ne0\), the finite, nonzero limit
\[
D=\lim_{t\to\infty}e^{\lambda t}d(t)
=d(0)\exp\left(-\beta\int_0^\infty x(s)\,ds\right)
\]
exists. The middle-opinion deviation then satisfies the following *sharp leading limits*:
\[
\begin{array}{ll}
0<\alpha<2/3: &\displaystyle \lim_{t\to\infty}e^{2\lambda t}x(t)
=-\frac{\alpha D^2}{2(\beta-2\lambda)}<0,\\[6pt]
\alpha=2/3: &\displaystyle \lim_{t\to\infty}\frac{e^{\beta t}x(t)}{t}=-\frac{\alpha D^2}{2}<0,\\[6pt]
2/3<\alpha<1: &\displaystyle \lim_{t\to\infty}e^{\beta t}x(t)=C,
\end{array}
\]
where, in the third case, the absolutely convergent integral gives
\[
C=x(0)+\int_0^\infty e^{\beta s}\left(\frac{\kappa}{2}x(s)^2-\frac{\alpha}{2}d(s)^2\right)ds.
\]
In the last regime, the ordinary exponential rate \(\beta\) is sharp whenever \(C\ne0\); such data form a nonempty relatively open set, including asymmetric data. If \(C=0\), the asserted limit remains valid but the leading rate can be faster. In the first two regimes every initially asymmetric trajectory eventually approaches the middle-opinion equilibrium **from below**, independently of the sign or size of its initial middle-opinion deviation.

## Assumptions and scope
Here \(a,b,c\ge0\), \(a+b+c=1\), \(0<\alpha<1\), and time has the normalization of equation (3.2) in Cao and Reed, arXiv:2408.00148v1 (unit mean-field rate). A *vertex* is \((1,0,0)\), \((0,1,0)\), or \((0,0,1)\). The long-time asymptotic rate statements concerning \(D\) assume \(c(0)\ne a(0)\). No claim is made about finite-population random fixation, higher-dimensional opinion alphabets, or the endpoint parameters \(\alpha=0\) and \(\alpha=1\).

## Proof
**1. Exact reduction.** Substituting three opinions into the published IPP equation (3.2), with \(\beta=1-\alpha\), gives
\[
\dot a=c(\beta b-\alpha a),\qquad
\dot b=2\alpha ac-\beta b(a+c),\qquad
\dot c=a(\beta b-\alpha c).
\tag{1}
\]
The sum of the three derivatives is zero. Every face of the probability simplex is inward-pointing except at its vertices: for example, at \(a=0\) with \(b,c>0\), \(\dot a=\beta bc>0\); at \(b=0\) with \(a,c>0\), \(\dot b=2\alpha ac>0\), and similarly at \(c=0\). Thus every nonvertex solution has all three coordinates strictly positive for each \(t>0\). The vector field is polynomial and preserves the compact simplex, so solutions exist uniquely for all positive times.

Any interior equilibrium must satisfy \(\alpha a=\beta b=\alpha c\), yielding the stated unique interior equilibrium. The inward-face calculation rules out other nonvertex boundary equilibria; all vertices are equilibria.

**2. Entropy and global attraction.** Put \(a_*=c_*=\beta/\kappa\) and \(b_*=\alpha/\kappa\). On the simplex define the continuous relative entropy
\[
H(a,b,c)=a\log\frac{a}{a_*}+b\log\frac{b}{b_*}+c\log\frac{c}{c_*},
\]
with \(0\log0=0\). For positive coordinates, direct differentiation of (1), using \(\alpha a_*=\beta b_*=\alpha c_*\), gives
\[
\dot H=-c(\alpha a-\beta b)\log\frac{\alpha a}{\beta b}
-a(\alpha c-\beta b)\log\frac{\alpha c}{\beta b}\le0.
\tag{2}
\]
Both terms are nonpositive by \((u-v)(\log u-\log v)\ge0\), and equality in the interior holds only at the interior equilibrium. This is the usual detailed-balance relative-entropy mechanism; its general form is classical rather than claimed as new.

For a nonvertex trajectory the entropy is strictly decreasing whenever it is not at equilibrium and has a finite limit. Every omega-limit point belongs to an invariant set on which the entropy is constant. No nonvertex boundary point can belong to this invariant set, because its forward orbit immediately enters the interior and strictly decreases entropy. Thus only the interior equilibrium and possibly the three vertices remain. The vertices cannot be limits of an interior trajectory: near \((1,0,0)\), \(\dot a=c(\beta b-\alpha a)<0\), so an interior trajectory cannot approach \(a=1\); near \((0,0,1)\), symmetrically \(\dot c<0\); near \((0,1,0)\), \(\dot b=2\alpha ac-\beta b(a+c)<0\) because \(2ac\le(a+c)^2/2\). Therefore the omega-limit set is the single interior equilibrium, proving global convergence from every nonvertex state.

**3. Two exact normal coordinates.** Let \(x=b-b_*\) and \(d=c-a\). From (1), with \(ac=((1-b)^2-d^2)/4\), one obtains the *exact*, not truncated, system
\[
\dot x=-\beta x+\frac{\kappa}{2}x^2-\frac{\alpha}{2}d^2,
\qquad \dot d=-(\lambda+\beta x)d.
\tag{3}
\]
Its linear eigenvalues are \(-\beta\) and \(-\lambda\), both negative. Consequently a convergent nonvertex trajectory enters a neighborhood where standard differential inequalities for this hyperbolic sink yield exponential convergence. In particular \(x\) is integrable over \([0,\infty)\), and integrating the second equation in (3) proves the formula for \(D\). If \(d(0)\ne0\), then \(D\ne0\) and \(d(t)=D e^{-\lambda t}(1+o(1))\).

For clarity, the necessary quantitative bootstrap follows directly from variation of constants. Hyperbolicity first gives \(x,d=O(e^{-(\lambda-\varepsilon)t})\) for any sufficiently small \(\varepsilon>0\). The second equation implies the sharper \(d=O(e^{-\lambda t})\); inserting this and the first bound into the first equation gives, for each sufficiently small \(\varepsilon>0\),
\[
x(t)=O\big(e^{-(\min\{\beta,2\lambda\}-\varepsilon)t}\big).
\tag{4}
\]
If \(2\lambda\ge\beta\), estimate (4), with \(\varepsilon<\beta/2\), makes \(e^{\beta t}x(t)^2\) integrable. If \(2\lambda<\beta\), choose \(\varepsilon<\lambda\) in (4); then \(x(t)^2=o(e^{-2\lambda t})\), which is the comparison required for the slower squared-imbalance forcing. These are the separate remainder bounds used below.

**4. The sharp resonance.** The first equation in (3) has the exact variation-of-constants form
\[
x(t)=e^{-\beta t}x(0)+\int_0^t e^{-\beta(t-s)}
\left(\frac{\kappa}{2}x(s)^2-\frac{\alpha}{2}d(s)^2\right)ds.
\tag{5}
\]
If \(2\lambda<\beta\), the squared-imbalance forcing is asymptotic to \(-\alpha D^2e^{-2\lambda s}/2\), while the quadratic \(x^2\) and the homogeneous term are negligible after multiplication by \(e^{2\lambda t}\). Direct evaluation of the exponential convolution gives \(-\alpha D^2/[2(\beta-2\lambda)]\).

If \(2\lambda=\beta\), multiply (5) by \(e^{\beta t}\), divide by \(t\), and use \(e^{\beta t}d(t)^2\to D^2\); the contribution from \(e^{\beta t}x^2\) is integrable and hence vanishes after division by \(t\). This gives the logarithm-free polynomial prefactor \(-\alpha D^2 t e^{-\beta t}/2\).

If \(2\lambda>\beta\), both nonlinear forcing terms in (5) are integrable with weight \(e^{\beta s}\), yielding the stated constant \(C\). Algebra gives
\[
\beta-2\lambda=\frac{(1-\alpha)(2-3\alpha)}{2-\alpha},
\]
so the unique resonance is \(\alpha=2/3\). Sharpness of the \(e^{-\beta t}\) rate above resonance is witnessed already on the invariant symmetry line \(d=0\): for any nonzero \(x(0)\) admissible in the interior, equation (3) reduces to \(\dot x=-\beta x+\kappa x^2/2\), whence
\[
\lim_{t\to\infty}e^{\beta t}x(t)
=\frac{x(0)}{1-\kappa x(0)/(2\beta)}\ne0.
\]
The limit \(C\) varies continuously with nearby initial conditions (via uniform exponential estimates), so nearby asymmetric initial data also have \(C\ne0\). This completes the proof.

## Verification
The accompanying `verify.py` checks the polynomial equations (1) and (3), mass conservation, the equilibrium identities, and the rate-order transition exactly over 3,816 rational-state/parameter cases; it additionally checks four numerical trajectories and the entropy identity at representative interior points. Run `python verify.py` in a Python environment with SciPy installed. The symbolic and finite checks are corroborative, not a proof of global asymptotics; that proof is given above.

## Relationship to prior work
Cao and Reed (arXiv:2408.00148v1, equation (3.2) and sections 3.1–3.3) derive the mean-field IPP flow and analyze the special cases \(\alpha=1\), \(\alpha=0\), and \(\alpha=1/2\). The uniform equilibrium at \(\alpha=1/2\) agrees with this theorem. The arbitrary-interior-parameter three-opinion coexistence law and the \(\alpha=2/3\) nonlinear relaxation resonance are not established in that accessible version. The 2025 journal record has the same title and an accessible abstract but not publicly accessible complete text in the inspected source, so its possible extra details remain a priority risk.

The entropy argument is an application of classical detailed-balance principles (Horn and Jackson, 1972), not a new entropy theorem. Mobilia's constrained three-species voter model has different reactions and a continuum of polarization equilibria; its fixed-point laws do not imply this theorem. The subsequent incremental voter model of Cao and Gong (2026) is another discrete-opinion model, with different persuasion probabilities and equilibrium structure. Related material was compared at the level accessible in the stated sources, not assumed equivalent on the basis of terminology.

## Limitations
This is a deterministic infinite-population mean-field theorem for exactly three opinions. It neither proves finite-population stochastic persistence nor provides a universal higher-alphabet equilibrium classification. The coefficient \(C\) in the upper regime can vanish for exceptional initial conditions; no universal nonzero lower bound is claimed there. Endpoint probabilities \(\alpha=0\) and \(\alpha=1\) exhibit different dynamics, and neither endpoint is covered. The result has not received independent external validation. The 2025 journal full text and any unindexed mathematically equivalent work are residual originality uncertainties.

## References
1. F. Cao and S. Reed, *The iterative persuasion-polarization opinion dynamics and its mean-field analysis*, arXiv:2408.00148v1, first public release 2024-07-31, https://arxiv.org/html/2408.00148 ; journal version, SIAM J. Appl. Math. 85 (2025), 1596–1620, https://doi.org/10.1137/24M1700661.
2. F. Horn and R. Jackson, *General mass action kinetics*, Arch. Rational Mech. Anal. 47 (1972), 81–116, https://doi.org/10.1007/BF00251225.
3. M. Mobilia, *Fixation and polarization in a three-species opinion dynamics model*, arXiv:1104.5147v2 (2011), https://arxiv.org/pdf/1104.5147.
4. F. Cao and X. Gong, *The incremental voter model: mean-field analysis and convergence to equilibrium*, arXiv:2605.28984 (2026), https://arxiv.org/abs/2605.28984 (abstract compared; different model).
