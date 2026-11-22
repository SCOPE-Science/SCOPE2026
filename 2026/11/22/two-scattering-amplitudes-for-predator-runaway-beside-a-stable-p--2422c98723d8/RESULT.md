# Two scattering amplitudes for predator runaway beside a stable prey-only state

## Finding

In the semi-discrete prey-refuge predator–prey family of Hong and Zhang, a nonempty parameter chamber open in the five free parameters at fixed conversion parameter has **both** a locally exponentially attracting prey-only state and an open set of strictly positive trajectories with unbounded predator population and superexponentially vanishing prey. On every trajectory in an explicit forward-invariant escape wedge, two positive finite asymptotic amplitudes exist and determine the full leading and subleading escape clocks.

More precisely, let
\[
F(x,y)=\left(x\exp\left(1-\frac{x}{\gamma}-\frac{ay}{H+x}\right),\;y\exp\left(\frac{ax+\xi}{H+x}-\delta\right)\right),
\]
where \(a=1-c\) and \(H=1+\alpha\xi\). Assume the strict conditions in the next section. Define
\[
s=\frac{\xi}{H}-\delta>0,\qquad k=\xi-aH>0,\qquad x_* =\frac{\xi-\delta H}{\delta-a},\qquad
P(x)=\frac{ax+\xi}{H+x}-\delta.
\]
For any \(0<\varepsilon<x_*\) and \(Y>(H+\varepsilon)/a\), the wedge
\[
W_{\varepsilon,Y}=\{(x,y):0<x<\varepsilon,\ y>Y\}
\]
is forward invariant. For each \((x_0,y_0)\) therein, the two limits
\[
L=\lim_{n\to\infty}y_ne^{-sn}\in(0,\infty),\qquad
K=\lim_{n\to\infty}x_n\exp\!\left(\frac{aL(e^{sn}-1)}{H(e^s-1)}-n\right)\in(0,\infty)
\]
exist. In particular, putting \(C=aL/[H(e^s-1)]\),
\[
\boxed{\;y_n\sim Le^{sn},\qquad x_n\sim K\exp\!\left(n-C(e^{sn}-1)\right).\;}
\]
The function \(L\) is continuous and nonconstant in the initial state on the wedge. The prey-only fixed point \((\gamma,0)\) is a hyperbolic sink, the unique positive equilibrium is a hyperbolic saddle, and there exist disjoint nonempty open sets of positive initial data, one attracted to the prey-only equilibrium and one escaping to infinity. These two outcomes are not asserted to exhaust all positive trajectories.

## Assumptions and scope

Work with the authors' discrete recurrence (their Equation (2)) on \((0,\infty)^2\) at the explicit parameter slice \(\beta=1\). Let \(\alpha>1\), \(\xi>0\), \(0<c<1\), \(a=1-c\), \(H=1+\alpha\xi\), and suppose
\[
\boxed{\quad a<\delta<\frac{\xi}{H},\qquad \gamma>\frac{\xi-\delta H}{\delta-a}.\quad}
\]
These strict conditions form a nonempty open chamber in the five-dimensional slice \(\beta=1\), not an open region in all six original parameters: for example,
\[
(\alpha,\xi,c,\delta,\gamma)=\left(\frac65,2,\frac12,\frac{11}{20},4\right),
\]
for which \(H=17/5\), \(k=3/10\), \(s=13/340\), \(x_*=13/5\), and \(y_*=21/5\). The recurrence is defined and remains strictly positive at every finite iterate. The theorem is about the stated positive parameter chamber, not about all parameter choices or all initial data.

## Proof

**Step 1: decreasing predator growth with prey and the equilibria.** The logarithmic per-step predator growth function satisfies the exact identity
\[
P(x)=s-\frac{kx}{H(H+x)},\qquad P'(x)=-\frac{k}{(H+x)^2}<0.
\]
The assumptions imply \(P(0)=s>0\), \(P(x_*)=0\), and \(P(\gamma)<0\). Any positive equilibrium must have \(x=x_*\) and
\[
y=y_*:=\frac{H+x_*}{a}\left(1-\frac{x_*}{\gamma}\right)>0.
\]
There are also the boundary equilibria \((0,0)\) and \((\gamma,0)\). The Jacobian of \(F\) at the prey-only state has multipliers \(0\) and \(e^{P(\gamma)}\in(0,1)\). Consequently \((\gamma,0)\) has a relative open attraction basin in the strictly positive quadrant.

At the interior equilibrium, abbreviate \(r=1-x_*/\gamma\in(0,1)\). The Jacobian is
\[
J_* =\begin{pmatrix}
 r\left(1+\frac{x_*}{H+x_*}\right)&-\frac{ax_*}{H+x_*}\\
 -\frac{ky_*}{(H+x_*)^2}&1
\end{pmatrix}.
\]
Writing \(A=J_{11}>0\) and \(B=J_{12}J_{21}=r x_*k/(H+x_*)^2>0\), its characteristic polynomial is
\[
\chi(t)=t^2-(1+A)t+(A-B).
\]
Because \(\alpha>1\) gives \(0<k<\xi<H\), we have \(B<A\). Thus \(\chi(0)>0\) and \(\chi(1)=-B<0\), proving one eigenvalue lies strictly between zero and one and the other strictly above one. The positive equilibrium is therefore a hyperbolic saddle. The origin is a source with multipliers \(e\) and \(e^s\).

**Step 2: an explicit invariant escape wedge.** Fix \(0<\varepsilon<x_*\) and \(Y>(H+\varepsilon)/a\). Put
\[
q=e^{P(\varepsilon)}>1,\qquad
\vartheta=\exp\left(1-\frac{aY}{H+\varepsilon}\right)\in(0,1).
\]
For every point in \(W_{\varepsilon,Y}\), the prey multiplier is no more than \(\vartheta\) and the predator multiplier at least \(q\). Hence the wedge is strictly invariant, with \(x_n\le x_0\vartheta^n\) and \(y_n\ge y_0q^n\). Summing the stronger inequality
\[
\log\frac{x_{j+1}}{x_j}\le 1-\frac{ay_0q^j}{H+\varepsilon}
\]
gives
\[
0<x_n\le x_0\exp\!\left(n-\frac{ay_0}{H+\varepsilon}\frac{q^n-1}{q-1}\right).
\]
Thus for every finite \(r>0\), \(\sum_{n\ge0}e^{rn}x_n<\infty\). In particular, \(x_n\to0\) superexponentially and \(y_n\to\infty\).

**Step 3: the first positive scattering amplitude.** Define \(d_j=kx_j/[H(H+x_j)]\). The predator equation gives, by exact telescoping,
\[
y_n=y_0\exp\left(sn-\sum_{j=0}^{n-1}d_j\right).
\]
Since \(\sum d_j<\infty\),
\[
L=y_0\exp\left(-\sum_{j=0}^{\infty}\frac{kx_j}{H(H+x_j)}\right)\in(0,\infty).
\]
Furthermore \(y_n=Le^{sn}\exp(R_n)\), where \(R_n=\sum_{j=n}^{\infty}d_j\downarrow0\). This proves the first asymptotic.

The convergence is sufficiently fast to have the stronger summability
\[
\sum_{n=0}^{\infty}|y_n-Le^{sn}|<\infty.
\]
Indeed \(0\le R_n\le\sum_jd_j<\infty\), so \(e^{R_n}-1\le e^{R_0}R_n\), and by rearranging nonnegative series,
\[
\sum_{n\ge0}e^{sn}R_n
=\sum_{j\ge0}d_j\sum_{n=0}^{j}e^{sn}
\le\frac{e^s}{e^s-1}\sum_{j\ge0}e^{sj}d_j<\infty.
\]
(The last step uses the superexponential prey bound.) We also obtain \(\sum x_ny_n<\infty\), because \(y_n\le y_0e^{sn}\).

**Step 4: the second positive scattering amplitude.** Let
\[
E_j=\frac{y_j}{H+x_j}-\frac{Le^{sj}}H.
\]
The two summability statements above imply \(\sum_{j\ge0}|E_j|<\infty\), since
\[
|E_j|\le\frac{|y_j-Le^{sj}|}{H}+\frac{y_jx_j}{H(H+x_j)}.
\]
Taking logarithms of the prey recurrence and adding/subtracting the exactly summable geometric forcing gives
\[
\begin{aligned}
\log x_n
&=\log x_0+n-\frac1\gamma\sum_{j<n}x_j-a\sum_{j<n}\frac{y_j}{H+x_j}\\
&=n-\frac{aL}{H}\frac{e^{sn}-1}{e^s-1}
+\log x_0-\frac1\gamma\sum_{j<n}x_j-a\sum_{j<n}E_j.
\end{aligned}
\]
The last three terms converge to a finite real number \(\log K\), where explicitly
\[
K=x_0\exp\left(-\frac1\gamma\sum_{j=0}^{\infty}x_j-a\sum_{j=0}^{\infty}E_j\right)\in(0,\infty).
\]
This proves the second asymptotic, including the order-\(n\) exponent term and the initial-state-dependent constant.

**Step 5: continuity, nonconstancy and open coexistence of outcomes.** On every compact subset of the open wedge, the superexponential estimate has uniform constants; hence the series defining \(L\) and \(K\) converge locally uniformly, so both limits depend continuously on the initial state. For fixed \(x_0\in(0,\varepsilon)\), the geometric bound gives \(\sum x_n\le x_0/(1-\vartheta)\), uniformly for all \(y_0>Y\). Thus
\[
L\ge y_0\exp\left(-\frac{kx_0}{H^2(1-\vartheta)}\right),
\]
which tends to infinity with \(y_0\). Thus \(L\) is nonconstant. Finally, the wedge is an open set of strictly positive runaway data, whereas the hyperbolic prey-only sink attracts a distinct relative open set of strictly positive data. For each fixed \(x_0>0\), sufficiently large \(y_0\) also sends the first iterate into the wedge, since \(x_1\to0\) and \(y_1=y_0e^{P(x_0)}\to\infty\) as \(y_0\to\infty\). This finishes the proof.

## Verification

The standalone file `verify.py` checks the strict rational parameter witness, exactly reconstructs the interior fixed point, compares algebraic Jacobian identities and evaluates the two logarithmic amplitudes with high-precision orbit iteration. It prints `REFUGE_ESCAPE_VERIFY_OK` when its assertions pass. These calculations are independent diagnostics; the infinite-time assertions follow from Steps 2–5, not from finite numerical iteration.

For the witness, the admissible choice \(\varepsilon=1\), \(Y=10\) has \(P(1)=1/55>0\), so one may take \(q=e^{1/55}\) and \(\vartheta=e^{-3/22}\). Starting at \((x_0,y_0)=(1/4,10)\), the numerical limits are \(L\approx9.84562775756377\) and \(\log K\approx-1.32704685670356\), solely as reproducibility cross-checks.

## Relationship to prior work

Hong and Zhang (2023, DOI `10.3390/math11061399`) introduce the semi-discrete model (Equation (2)), analyze its boundary/interior fixed points, and establish local Neimark–Sacker bifurcation conditions. Those facts and the recurrence itself are prior work. Their inspected analysis does not contain an invariant escape wedge, coexistence of a prey-only sink with unbounded predator orbits, or the two exact asymptotic amplitudes of this theorem.

Parshad, Wickramsooriya, Antwi-Fordjour and Banerjee (arXiv:2208.00153v1, 2022, Sections 2.3–2.4) already prove infinite-time predator explosion for a related **continuous-time**, **no-refuge** functional-response model in a high-additional-food regime. That establishes explosion as a known qualitative phenomenon; it does not imply the discrete-time result above, its simultaneous prey-only sink, or its double-exponential prey clock. Ghosh, Sahoo and Poria (2017, DOI `10.1016/j.chaos.2017.01.010`) analyze the related **continuous-time** refuge model, including equilibria and limit cycles, not the present discrete scattering constants.

Other 2023–2026 discrete refuge and food-supplement models investigate different recurrence laws or local bifurcations. The nontrivial difference here is an open parameter region within the specified slice exhibiting opposite outcomes with a pair of complete, initial-state-dependent escape amplitudes in the original published map, rather than merely the generic possibility of prey extinction or predator overgrowth.

## Limitations

The proof works only on the slice \(\beta=1\), under the strict open parameter inequalities and in the explicit wedge for the asymptotic formulas. It does not classify the entire boundary between the finite-sink basin and runaway orbits, all other invariant sets, or the effect of density-dependent predator competition. The runaway is an **infinite-generation** limit; all finite iterates are positive and finite. The model lacks predator self-limitation, so large densities need not be ecologically realistic. The phase-space evidence establishes no independent peer review, priority guarantee or uniqueness among unpublished mathematical work. Earlier or unindexed equivalent formulations remain a residual publication-priority risk.

## References

1. B. Hong and C. Zhang, “Neimark–Sacker Bifurcation of a Discrete-Time Predator–Prey Model with Prey Refuge Effect,” *Mathematics* **11** (2023), 1399; first publicly published 2023-03-14. DOI: https://doi.org/10.3390/math11061399 ; full text: https://www.mdpi.com/2227-7390/11/6/1399 .
2. R. D. Parshad, S. Wickramsooriya, K. Antwi-Fordjour, A. Banerjee, “Additional food causes predator ‘explosion’—unless the predators compete,” arXiv:2208.00153v1 (2022-07-30), https://arxiv.org/html/2208.00153v1 .
3. J. Ghosh, B. Sahoo and S. Poria, “Prey-predator dynamics with prey refuge providing additional food to predator,” *Chaos, Solitons & Fractals* **96** (2017), 110–119. DOI: https://doi.org/10.1016/j.chaos.2017.01.010 .
