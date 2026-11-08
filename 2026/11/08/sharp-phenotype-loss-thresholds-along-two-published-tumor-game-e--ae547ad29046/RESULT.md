# Sharp phenotype-loss thresholds along two published tumor-game environment paths

## Finding

Consider the deterministic four-phenotype replicator equation from the January 2026 tumor-heterogeneity model of Rodrigues, with coordinates ordered as proliferative (P), invasive (I), resistant (R), and cooperative (C). Form two one-parameter environmental paths by linear interpolation between its published baseline matrix and, respectively, its published acidic and buffered matrices. Along **each complete path**, there is a unique globally attracting equilibrium for every strictly positive initial phenotype vector. It has four positive components up to one sharp threshold, after which precisely one component vanishes: P in the acidic path, R in the buffered path. The threshold parameters are the unique roots in \((0,1)\) of

\[
 g_a(t)=t^3-2t^2+234t-60=0,\qquad
 g_b(t)=41t^3-712t^2+3201t-2520=0.
\]

Numerically they are \(t_a=0.256901888893311\ldots\) and \(t_b=0.994745404575664\ldots\). In particular, the buffered scenario retains a positive limiting R fraction until more than \(99.47\%\) of the way along this interpolation; the acidic scenario loses P after about \(25.69\%\). These are mathematical interpolation fractions, not calibrated pH concentrations.

At the published endpoint matrices, the limiting states are exactly

\[
 p_a(1)=\frac{1}{677}(0,250,232,195),\qquad
 p_b(1)=\frac{1}{334}(100,49,0,185).
\]

For any interior initial state and any \(t\) strictly above its corresponding threshold, the extinct phenotype's positive abundance decreases at the exact logarithmic asymptotic rate

\[
 \lim_{s\to\infty}\frac{\log x_j(s)}{s}=-\Delta_j(t),
\]

where \(s\) is dynamical time, \(j=P\) or \(R\), and the positive invasion loss is

\[
 \Delta_P(t)=\frac{g_a(t)}{5(875-188t-10t^2)},\qquad
 \Delta_R(t)=\frac{g_b(t)}{100(515-184t+3t^2)}.
\]

At the published endpoints the extinction exponents are respectively \(173/3385\) and \(1/3340\), showing a particularly small resistant-phenotype decay rate in the buffered case.

## Assumptions and scope

Let \(\Sigma=\{x\in\mathbb R^4:x_i\ge0,\sum_i x_i=1\}\). For an environmental parameter \(t\in[0,1]\) and dynamical time \(s\ge0\), study

\[
 \frac{dx_i}{ds}=x_i\big((A(t)x)_i-x^{\mathsf T}A(t)x\big),\qquad x(0)\in\operatorname{int}\Sigma.
\]

The payoff matrices, reproduced exactly as decimal rationals from the motivating paper, are

\[
 A_0=\begin{pmatrix}.90&.90&.95&.92\\1.05&.85&.95&.92\\1.02&1.00&.75&.92\\1.03&1.04&1.00&.80\end{pmatrix},
\]
\[
 A_a=\begin{pmatrix}.88&.85&.90&.88\\1.10&.88&1.00&.90\\1.05&1.05&.80&.92\\1.00&1.02&.95&.78\end{pmatrix},
\qquad
 A_b=\begin{pmatrix}.92&.90&.95&.93\\1.00&.85&.90&.90\\.95&.95&.75&.90\\1.05&1.05&1.00&.82\end{pmatrix}.
\]

The acidic and buffered paths are \(A_a(t)=(1-t)A_0+tA_a\) and \(A_b(t)=(1-t)A_0+tA_b\). These line segments are an explicit mathematical experiment between the paper's already defined scenarios, not a claimed mechanistic conversion between \(t\) and environmental pH. All conclusions concern the deterministic replicator, not the paper's stochastic or spatial models. Boundary initial states need not approach the full-support attractor because absent strategies cannot reappear.

## Proof

**1. A uniform dissipativity certificate.** Put
\[
 B=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\\-1&-1&-1\end{pmatrix},
\qquad H(A)=B^{\mathsf T}\frac{A+A^{\mathsf T}}2B.
\]

For \(A_0,A_a,A_b\), the leading principal minors of \(H\), in order, are respectively

\[
 \left(-\frac14,\frac{451}{10000},-\frac{47263}{4000000}\right),\quad
 \left(-\frac{11}{50},\frac{1447}{40000},-\frac{32387}{4000000}\right),\quad
 \left(-\frac6{25},\frac{1167}{40000},-\frac{911}{160000}\right).
\]

By Sylvester's criterion, every endpoint form is strictly negative definite. Since \(H\) depends linearly on \(A\), every intermediate path matrix satisfies \(v^{\mathsf T}A(t)v<0\) for all nonzero vectors \(v\) whose coordinates sum to zero. For fixed \(t\) there is a constant \(c_t>0\) such that \(v^{\mathsf T}A(t)v\le-c_t\|v\|_2^2\) on this tangent space.

**2. Candidate equilibria and a single crossing.** Equalize the four payoffs and impose total mass one. Along the acidic path the four-coordinate algebraic candidate has common denominator
\[
 D_a(t)=34t^3-186t^2+2173t-13870<0
\]
with numerators, in P,I,R,C order,
\[
 20g_a(t),\quad-10(t+2)(2t^2-37t+180),\quad-2(3t^3+113t^2+1196t+1260),\quad5(8t^3-50t^2+189t-1310).
\]
Along the buffered path the common denominator is
\[
 D_b(t)=31t^3-1382t^2+7871t-13870<0
\]
with numerators
\[
 -5(2t^3-115t^2+313t+240),\quad5(9t^3-193t^2+687t-720),\quad g_b(t),\quad-5(9t^3+56t^2-560t+1310).
\]
All three nontarget coordinates are strictly positive throughout \([0,1]\); this follows directly from bounding their displayed polynomials. The first target coordinate has the sign opposite to \(g_a(t)\), the second target coordinate has the sign opposite to \(g_b(t)\). Both cubics are strictly increasing on \([0,1]\): \(g_a'(t)=3t^2-4t+234>0\), \(g_b'(t)=123t^2-1424t+3201>0\). Each starts negative and ends positive, giving exactly one crossing at \(t_a\) or \(t_b\). Before the crossing, the positive full-support candidate has equal payoffs and is a Nash equilibrium.

**3. The correct boundary branches.** On and after the acidic threshold, set P to zero and use the exact normalized face equilibrium
\[
 p_a(t)=\frac{1}{10t^2+188t-875}\begin{pmatrix}0\\-10(2t^2-t+24)\\2(5t^2-31t-90)\\5(4t^2+48t-91)\end{pmatrix}.
\]
On and after the buffered threshold, set R to zero and use
\[
 p_b(t)=\frac{1}{3t^2-184t+515}\begin{pmatrix}3t^2+37t+60\\7t^2-138t+180\\0\\-(7t^2+83t-275)\end{pmatrix}.
\]
All their three supported components are strictly positive on \([0,1]\) and sum to one. Direct multiplication shows equality of payoffs on the respective faces. The excluded phenotype's fitness minus the common resident fitness is
\[
 (A_a(t)p_a(t))_P-(A_a(t)p_a(t))_I
 =\frac{g_a(t)}{5(10t^2+188t-875)},
\]
\[
 (A_b(t)p_b(t))_R-(A_b(t)p_b(t))_P
 =-\frac{g_b(t)}{100(3t^2-184t+515)}.
\]
Both are nonpositive exactly at and after their threshold. Therefore each boundary candidate is a Nash equilibrium throughout its stated regime. The displayed positive loss formulas are their negatives in the strict regime.

**4. Unique equilibrium selected by every interior trajectory.** A Nash equilibrium \(p\) satisfies \((x-p)^{\mathsf T}A(t)p\le0\) for every \(x\in\Sigma\). If \(p,q\) were two Nash equilibria, these two inequalities would imply \((p-q)^{\mathsf T}A(t)(p-q)\ge0\), contradicting strict tangent negativity unless \(p=q\). Thus the candidate identified above is the unique Nash equilibrium.

For any positive initial vector, define relative entropy on the equilibrium's support:
\[
 V(x)=\sum_{i:p_i>0}p_i\log\frac{p_i}{x_i}\ge0.
\]
Finite-time positivity follows from the replicator equation. Direct differentiation gives
\[
 \frac{dV}{ds}=(x-p)^{\mathsf T}A(t)(x-p)+(x-p)^{\mathsf T}A(t)p
 \le-c_t\|x-p\|_2^2.
\]
The simplex is compact and the vector field is bounded and Lipschitz, so \(\|x(s)-p\|_2^2\) is uniformly continuous. Its finite time integral and Barbalat's lemma imply \(x(s)\to p\). This rules out any other interior limiting behavior for every \(t\in[0,1]\), including both threshold values.

**5. Sharp extinction exponents.** Above threshold, for the missing phenotype \(j\), its initially positive fraction satisfies
\[
 \frac{d}{ds}\log x_j(s)=(A(t)x(s))_j-x(s)^{\mathsf T}A(t)x(s).
\]
By the proved convergence, the right side tends to \((A(t)p)_j-p^{\mathsf T}A(t)p=-\Delta_j(t)<0\). Cesàro averaging gives the claimed exact logarithmic extinction exponent. Substituting \(t=1\) in the face formulas yields the two endpoint states and \(\Delta_P(1)=173/3385\), \(\Delta_R(1)=1/3340\).

## Verification

The accompanying standalone `verify.py` reads no external files. It checks all payoff matrices, exact signs of the symmetric tangent-form principal minors, the full equilibrium's missing-coordinate formulas, normalized face formulas, face payoff equalities, invasion gaps, uniqueness of a root in each open unit interval, and endpoint extinction exponents using rational symbolic algebra. An independent numerical integration of the deterministic replicator from \((.2,.3,.3,.2)\), to dynamical time \(10^4\), approached the predicted three endpoint compositions. Computation confirms the displayed algebra but does not replace the global convergence proof.

## Relationship to prior work

The three environmental matrices and the four-phenotype replicator dynamics are taken from Rodrigues (January 22, 2026). That paper reports numerical coexistence and scenario comparisons, but the inspected body and Appendix A do not supply a sharp one-parameter phenotype-loss classification between its own matrices, the exact boundary compositions, or the terminal invasion exponents. The interpolation paths and their quantitative thresholds are the new model-specific conclusions.

Strictly stable population games and relative-entropy Lyapunov arguments are classical, especially the stable-games theory of Hofbauer and Sandholm. No novelty is claimed for the abstract convergence method; the exact conditional-negativity certificates and complete ecological phase diagram for the published three matrices are the particular application. Classical theory alone does not determine these model-specific thresholds without the payoff calculations.

## Limitations

The matrices are phenomenological illustrative numerical matrices rather than experimentally calibrated payoffs. Linearly interpolating matrix entries is a mathematical choice, not a published pH dose–response model. Extinction is asymptotic, never finite-time for strictly positive starts. At the threshold the excluded fitness advantage is exactly zero, so the strictly positive exponential-rate statement does not apply; convergence itself still holds. Different boundary initial supports and non-replicator stochastic perturbations are outside scope. Mathematical dominance of a phenotype is not a prediction for a clinical tumor.

## References

1. J. A. Rodrigues, *Modeling Tumor Phenotypic Heterogeneity with Multi-Strategy Evolutionary Games*, Preprints.org 202601.1761.v1, posted January 22, 2026. https://www.preprints.org/manuscript/202601.1761
2. J. Hofbauer and W. H. Sandholm, *Stable Games*, working paper (2006), available at https://discovery.ucl.ac.uk/id/eprint/14466/
3. J. Hofbauer and K. Sigmund, *Evolutionary Games and Population Dynamics*, Cambridge University Press (1998), for classical replicator equations and stability terminology.
