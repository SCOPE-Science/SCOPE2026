# Cubic slowing at the invasion threshold of a cooperative-hunting refuge map

## Finding

For the discrete predator–prey recurrence of Jang and Yousef, tuning the predator reproduction number to one gives a nonhyperbolic predator-free equilibrium. At a further, explicitly specified cooperation threshold, the quadratic drift vanishes and a strictly negative cubic drift takes over. Consequently **the local rate of predator extinction changes from reciprocal time to reciprocal square-root time**, with a closed-form coefficient. The same cubic coefficient controls the small stable coexistence branch on the high-cooperation side.

Write \(K=\lambda-1\), and impose \(\lambda>1\), \(0<\gamma<1\), \(\beta\gamma K=1\). Define
\[
 c_*=\frac12+\frac{\lambda\gamma}{K},\qquad
 b=\frac13+\frac{\lambda\gamma}{K}
       +2\left(\frac{\lambda\gamma}{K}\right)^2>0.
\]
For each fixed \(0\le c<c_*\), all strictly positive initial conditions sufficiently close to \((K,0)\) converge to \((K,0)\) and satisfy
\[
 \lim_{n\to\infty}n y_n=\frac1{c_*-c},\qquad
 \lim_{n\to\infty}n(K-x_n)=\frac{\lambda\gamma}{c_*-c}.
\]
At **exactly** \(c=c_*\), all such initial conditions instead satisfy
\[
 \boxed{\lim_{n\to\infty}\sqrt n\,y_n=\frac1{\sqrt{2b}},\qquad
 \lim_{n\to\infty}\sqrt n\,(K-x_n)=\frac{\lambda\gamma}{\sqrt{2b}}.}
\]
There exists \(\delta_0>0\) such that, for \(0<\delta<\delta_0\), choosing \(c=c_*+\delta\) produces a locally asymptotically stable positive equilibrium \((x_\delta,y_\delta)\) with
\[
 y_\delta=\frac{\delta}{b}+O(\delta^2),\qquad
 x_\delta=K-\frac{\lambda\gamma}{b}\delta+O(\delta^2).
\]
These are **local** results. In particular they do not assert global predator extinction, uniqueness of all possible positive attractors, or a global basin classification.

## Assumptions and scope

The exact map is
\[
 \begin{aligned}
 x_{n+1}&=\frac{\lambda x_n}{1+x_n}
  \left[1-\gamma\bigl(1-e^{-y_n(1+c y_n)}\bigr)\right],\\
 y_{n+1}&=\beta\gamma x_n\bigl(1-e^{-y_n(1+c y_n)}\bigr),
 \end{aligned}
\]
with nonnegative densities, parameters \(\lambda>1\), \(0<\gamma<1\), \(\beta>0\), \(c\ge0\), and the exact critical invasion condition \(\beta\gamma(\lambda-1)=1\). No stochasticity or delayed recruitment is included. A strictly positive initial condition means \(x_0>0,y_0>0\); its required proximity to \((K,0)\) may depend on the parameters. The time index \(n\) counts discrete generations. The assertion of a positive branch is for cooperation levels immediately *above* \(c_*\), not arbitrary large cooperation.

## Proof

**1. Local spectrum.** Let \(P_c(y)=1-\exp[-y(1+cy)]\). With \(K=\lambda-1\) and \(\beta\gamma K=1\), the map is equivalently
\[
 F_c(x,y)=\left(\frac{\lambda x}{1+x}[1-\gamma P_c(y)],\ \frac{x}{K}P_c(y)\right).
\]
It fixes \((K,0)\), with Jacobian
\[
 DF_c(K,0)=\begin{pmatrix}1/\lambda&-\gamma K\\0&1\end{pmatrix}.
\]
The transverse multiplier is strictly between zero and one, while the center multiplier equals one. The smooth center-manifold theorem for maps supplies a local center graph \(x=K+h_c(y)\), tangent to the center eigendirection, together with an exponentially contracting stable foliation. Because \(y=0\) is invariant and is the local strong stable manifold, positive initial predator density projects onto the positive center branch. Exponential stable-fiber errors do not affect the polynomial asymptotics below.

**2. Taylor coefficients.** Direct expansion of the predation probability gives
\[
 P_c(y)=y+\left(c-\frac12\right)y^2
             +\left(\frac16-c\right)y^3+O(y^4).
\]
Writing \(h_c(y)=h_1y+h_2y^2+O(y^3)\) for the prey displacement from \(K\), the invariant-graph equation
\[
 K+h_c\left(\frac{K+h_c(y)}K P_c(y)\right)
 =\frac{\lambda[K+h_c(y)]}{1+K+h_c(y)}[1-\gamma P_c(y)]
\]
first yields \(h_1=-\lambda\gamma\), independent of \(c\). The reduced predator coordinate therefore obeys
\[
 y_{n+1}=y_n+(c-c_*)y_n^2+B(c)y_n^3+O(y_n^4).
\]
At \(c=c_*\), the quadratic invariance equation gives
\[
 h_2=-\frac{\gamma^2\lambda^2}{K};
\]
substitution in the cubic coefficient gives
\[
 \begin{aligned}
 B(c_*)&=\left(\frac16-c_*\right)
       +\frac{h_1}{K}\left(c_*-\frac12\right)
       +\frac{h_2}{K}\\
 &=-\left[\frac13+\frac{\lambda\gamma}K
       +2\left(\frac{\lambda\gamma}K\right)^2\right]=-b<0.
 \end{aligned}
\]
All expansions are in actual model coordinates, not a rescaled normal form. The positivity of \(b\) holds throughout the specified parameter range.

**3. Local attraction and exact extinction clocks.** For \(c<c_*\), the reduced map is \(y\mapsto y-(c_*-c)y^2+O(y^3)\). Its small positive iterates decrease monotonically to zero, and
\[
 \frac1{y_{n+1}}-\frac1{y_n}=(c_*-c)+O(y_n).
\]
Cesàro summation yields \(n y_n\to1/(c_*-c)\). At \(c=c_*\), the reduced map is \(y\mapsto y-by^3+O(y^4)\); for small positive iterates,
\[
 \frac1{y_{n+1}^2}-\frac1{y_n^2}=2b+O(y_n).
\]
Again by summation, \(n y_n^2\to(2b)^{-1}\). Stable-fiber tracking transfers both limits from center-manifold trajectories to all sufficiently nearby strictly positive initial conditions. Since \(x_n=K-\lambda\gamma y_n+O(y_n^2)\) along the center graph and transverse errors are exponentially small, the asserted prey-deficit limits follow.

**4. Coexistence branch just beyond the threshold.** Vary \(c=c_*+\delta\) with \(\delta\) small. Uniform smoothness of the center-reduced map in \((y,\delta)\) gives
\[
 y_{n+1}-y_n=y_n^2\left[\delta-b y_n
                       +O(\delta y_n+y_n^2)\right].
\]
The implicit-function theorem applied to the bracket supplies a positive fixed point \(y_\delta=\delta/b+O(\delta^2)\) for \(\delta>0\) small. Its center multiplier is
\[
 1-\frac{\delta^2}{b}+O(\delta^3)<1
\]
and its transverse multiplier is \(1/\lambda+O(\delta)<1\), proving local asymptotic stability. The prey expansion follows from the graph. The boundary fixed point has a positive center drift \(\delta y^2+O(y^3)\), so it is not attracting from sufficiently small positive center states.

## Verification

The accompanying standard-library `verify.py` recomputes the center-graph invariance through quadratic order and the reduced cubic coefficient using exact rational truncated power series for 20 independent admissible parameter pairs. It also iterates the *original* nonlinear map for \(\lambda=3\), \(\gamma=1/4\), \(\beta=2\), and \(c\in\{1/2,7/8,9/10\}\), checking the predicted clock and nearby stable positive equilibrium. Run `python3 verify.py` in a directory containing this file; no third-party Python packages are required. These checks corroborate arithmetic but are not substitutes for the analytic center-manifold and asymptotic arguments.

For the representative critical parameters, \(c_*=7/8\) and \(b=95/96\), so
\[
 \sqrt n\,y_n\longrightarrow\sqrt{48/95}.
\]

## Relationship to prior work

Jang and Yousef, *Effects of prey refuge and predator cooperation on a predator–prey system* (2023), equation (2), establish the exact model. Their Proposition 2.3 and Theorem 2.4 give local hyperbolic invasion classifications and an existence bound with the **same cooperation threshold** \(2c_*=[\lambda(2\gamma+1)-1]/(\lambda-1)\). That threshold and their equilibrium nonexistence result are acknowledged prior facts, not claimed as new. Their analysis does not give the local nonhyperbolic extinction rates, the negative cubic coefficient, or the small stable branch slope at exact critical invasion. The present finding fills that rate-and-stability gap rather than rebranding an existing equilibrium-count result.

Related work on cooperative hunting, including earlier refuge-free variants cited by Jang and Yousef and the distinct delayed model of Peng and Jiang (2025), does not directly imply this model-specific critical time law. General center-manifold and parabolic-iteration tools are standard; the model-dependent cancellation, explicit coefficient, and transition statement are the contribution assessed here.

## Limitations

The results are local and concern a codimension-two condition. They do not establish global convergence, global uniqueness of coexistence states, or survival with positive probability under demographic stochasticity. The first-public date is the verified August 3, 2023 online publication date; receipt or editorial revisions are not used as priority dates. An earlier unindexed preprint or an uninspected equivalent could affect originality, which has not been independently audited. No numerical finite-run check is presented as proof of an infinite-time limit.

## References

1. S. R-J Jang and A. M. Yousef, “Effects of prey refuge and predator cooperation on a predator–prey system,” *Journal of Biological Dynamics* **17** (2023), 2242372; first published online 2023-08-03. https://doi.org/10.1080/17513758.2023.2242372 . See equation (2), Proposition 2.3 and Theorem 2.4.
2. C. Peng and J. Jiang, “Dynamical Regimes in a Delayed Predator–Prey Model with Predator Hunting Cooperation: Bifurcations, Stability, and Complex Dynamics,” *Modelling* **6** (2025), article 84. https://doi.org/10.3390/modelling6030084 . Different delayed continuous-time model, included to delimit model comparisons.
