# Opposite Hopf criticalities in a triadic SIS–opinion model

## Finding

An exactly specified three-community, purely triadic susceptible–infected–susceptible (SIS) epidemic coupled to risk-responsive opinions supports **both** supercritical and subcritical endemic Hopf transitions, despite a locally exponentially stable disease-free state. The transition type has the following exact sign classification.

Take the homogeneous synchronous dynamics
\[
\dot x=x[-d_0-d_1 y+q x(1-x)],\qquad \dot y=x-y,
\]
where \(x\in[0,1]\) is infection prevalence, \(y\in[0,1]\) is shifted perceived severity, and \(d_0,d_1,q>0\). For \(0<s<1/2\) and \(0<\omega^2<s/(1-2s)\), set
\[
q=\frac1{s(1-2s)},\quad
 d_1=\frac{1+\omega^2}{s},\quad
 d_0=\frac{s}{1-2s}-\omega^2.
\]
Then the upper positive equilibrium \((s,s)\) has simple eigenvalues \(\pm i\omega\). In the explicitly defined canonical coordinates in the proof, its first Lyapunov coefficient is
\[
\boxed{\ell_1=\frac{4s-1-2(1-2s)\omega^2}{8s(1-2s)^2\omega^2}.}
\]
Thus the cubic Hopf coefficient can be positive or negative within the admissible biological parameter domain, and vanishes on the internal sign-change curve. The zero-coefficient case is not asserted to be a generalized Hopf bifurcation.

Two exact nondegenerate transverse examples, varying \(q\) with \(d_0,d_1\) fixed, are:

* **Supercritical:** \((d_0,d_1,q,s,\omega)=(1/4,5,8,1/4,1/2)\). Here \(\ell_1=-2\) and \(d\operatorname{tr}J/dq=1/8\); for sufficiently small \(q-8>0\) an orbitally attracting small-amplitude positive endemic cycle exists on the synchronous set.
* **Subcritical:** \((d_0,d_1,q,s,\omega)=(3/4,15/4,9,1/3,1/2)\). Here \(\ell_1=9/4\) and \(d\operatorname{tr}J/dq=-7/9\); for sufficiently small \(q-9>0\) an orbitally repelling positive endemic cycle surrounds the locally attracting upper endemic equilibrium on the synchronous set.

Both nondegenerate transition types persist after introducing sufficiently small **strictly positive pairwise transmission**, with a nearby adjusted triadic transmission coefficient. At the supercritical example the disease-free state is simultaneously locally exponentially stable, so the system has a disease-free attractor and an attracting endemic oscillation on the same synchronous state space.

## Assumptions and scope

Consider three communities in the higher-order SIS–opinion equations of Samadi, Caiza, Gracy and Paré. Let the pairwise infection matrix \(A=0\) initially. For each distinct triple \(\{i,j,k\}=\{1,2,3\}\), put \(b_{ijk}=b_{ikj}=1/2\) and all remaining entries of \(B_i\) equal to zero, so infection of \(i\) is driven by a genuine two-other-community triadic exposure, with \(x^\top B_i x=x_jx_k\). Choose common rate parameters \(\gamma^{\min}=d_0\), \(\gamma_i=d_0+d_1\), \(\beta_{i2}=\beta_2^{\min}=q\), and \(\beta_{i1}=\beta_1^{\min}=0\). Let the unsigned opinion Laplacian be that of any symmetric graph (for example, the unit-weight triangle). The model's shifted opinion is \(y=o_i+1/2\). The exact synchronous manifold \(x_i=x,\ o_i=y-1/2\) reduces to the displayed planar ODE.

All asserted Hopf cycles are **relative to this invariant synchronous manifold**, not necessarily stable to arbitrary asymmetric community perturbations. Since each equilibrium has \(s<1/2\), the relevant vector field is smooth in a neighborhood where each opinion is negative, away from the model's sign-switching surfaces. Rates and states remain in their admissible domains for sufficiently small Hopf cycles.

For persistence with positive pairwise transmission, choose \(A\) as the unit-row-sum complete three-node graph (off-diagonal entries \(1/2\)), let \(\beta_{i1}=\beta_1^{\min}=\varepsilon>0\), and keep other choices. Its synchronous reduction becomes \(\dot x=x[-d_0-d_1y+(1-x)(\varepsilon+q x)]\), \(\dot y=x-y\). The pairwise perturbation is asserted only for sufficiently small \(\varepsilon\), not for arbitrary pairwise intensity.

## Proof

**1. Exact equilibrium geometry.** The disease-free equilibrium is \((0,0)\), with Jacobian \(\left(\begin{smallmatrix}-d_0&0\\1&-1\end{smallmatrix}\right)\), so it is exponentially stable for every \(d_0>0\) at zero pairwise transmission. A positive equilibrium has \(y=x=s\) and
\[
g(s)=-d_0-d_1s+q s(1-s)=0.
\]
The parameterization in the finding solves this equation and the trace-zero condition. The second positive root is
\[
s_{-}=s-(1-2s)\omega^2\in(0,s).
\]
Indeed \(g(u)=-q(u-s_-)(u-s)\). Thus the Hopf state is the upper endemic equilibrium, while the lower equilibrium is a saddle. These conclusions use only \(0<s<1/2\) and \(0<\omega^2<s/(1-2s)\).

**2. Spectrum.** At a positive equilibrium, the Jacobian is
\[
J=\begin{pmatrix}s q(1-2s)&-s d_1\\1&-1\end{pmatrix}.
\]
At the stated parameterization this is \(\left(\begin{smallmatrix}1&-(1+\omega^2)\\1&-1\end{smallmatrix}\right)\), with trace zero and determinant \(\omega^2>0\). Therefore its simple eigenvalues are \(\pm i\omega\). The lower equilibrium has determinant \(-s_-g'(s_-)<0\).

**3. Exact first Lyapunov coefficient.** Define
\[
X=x-s,\qquad Y=\frac{s d_1(y-s)-(x-s)}{\omega}.
\]
A direct polynomial expansion yields the **exact** canonical system at the Hopf parameter:
\[
\dot X=-\omega Y+F(X,Y),\quad
\dot Y=\omega X-\frac{F(X,Y)}{\omega},\quad
F=-q s X^2-\frac{\omega}{s}XY-qX^3.
\]
For \(\dot X=-\omega Y+f\) and \(\dot Y=\omega X+h\), the standard planar Hopf coefficient is
\[
\ell_1=\frac{f_{XXX}+f_{XYY}+h_{XXY}+h_{YYY}}{16}
+\frac{f_{XY}(f_{XX}+f_{YY})-h_{XY}(h_{XX}+h_{YY})-f_{XX}h_{XX}+f_{YY}h_{YY}}{16\omega},
\]
with all derivatives evaluated at \((0,0)\). Substitution of \(f=F\), \(h=-F/\omega\) gives precisely the boxed expression. This coefficient is tied to the explicitly defined real canonical coordinates; normalization changes can rescale its magnitude but not its sign.

**4. Transverse crossings and cycle sides.** With \(d_0,d_1\) fixed and \(q\) varying, the upper equilibrium solves \(g(s(q),q)=0\); since \(g_s=-\omega^2/s<0\), it extends smoothly. Its trace \(T(q)=s(q)q(1-2s(q))-1\) has derivative at the Hopf point
\[
\frac{dT}{dq}=s(1-2s)+\frac{s(1-s)(1-4s)}{(1-2s)\omega^2}.
\]
For the first exact example this is \(1/8>0\), and \(\ell_1=-2\); the nondegenerate supercritical Hopf theorem gives a stable cycle for \(q>8\) near 8. In the second example it is \(-7/9<0\), while \(\ell_1=9/4>0\); the nondegenerate subcritical Hopf theorem gives a repelling cycle for \(q>9\) near 9. Since \(s<1/2\) strictly, the small cycles remain inside the domain and within one smooth opinion-sign region. The disease-free state stays exponentially stable for both cases.

**5. Positive pairwise robustness.** Adding \(\varepsilon x(1-x)\) to the prevalence equation is a smooth perturbation. Both examples have a simple endemic branch (nonzero determinant), a nonzero derivative of the trace with respect to \(q\), and nonzero \(\ell_1\). By the implicit-function theorem and continuity of the Hopf coefficients, a nearby nondegenerate Hopf point with the same sign exists for every sufficiently small positive \(\varepsilon\). The disease-free eigenvalues become \(\varepsilon-d_0\) and \(-1\); hence sufficiently small positive \(\varepsilon<d_0\) retains local disease-free stability.

## Verification

Run `python CHECK.py` with Python 3 and SymPy. The code symbolically reconstructs the stationary and Jacobian identities, transforms the cubic field into canonical coordinates, differentiates its exact first Lyapunov formula, verifies both rational parameter witnesses and their crossing speeds, and checks an admissible point of sign reversal. The theorem about small periodic orbits uses the classical analytic nondegenerate Hopf theorem; symbolic identities and numerical experiments do not by themselves prove that theorem.

## Relationship to prior work

Samadi et al. introduce the higher-order SIS–opinion system, prove its synchronous invariance, and provide healthy/endemic stability and bistability statements under sign conditions on the endemic Jacobian's trace. The present finding treats an explicit admissible **trace-zero** transition, determines both possible nonlinear Hopf signs, and establishes nearby cycles. It is not a restatement of an endemic-equilibrium stability criterion. Behaviorally induced epidemic cycles are known in different SIS–behavior models, notably Frieswijk et al. (2022) and Juher et al. (2020); the general possibility of oscillations is **not** claimed as new. The model-specific exact opposite-criticality formula and positive-pairwise persistence are the claims assessed here.

## Limitations

The results are local near the two stated Hopf parameter points and apply to synchronous solutions. They do not prove globally attracting oscillations, asymptotic stability transverse to synchrony, stochastic outbreak cycles, or a nondegenerate generalized-Hopf point at \(\ell_1=0\). In the examples the baseline transmission is purely triadic, but the claimed Hopf types survive small positive pairwise rates. Literature search and record comparisons do not certify exhaustive novelty; accessible earlier work on behavior-induced cycles is a meaningful contextual boundary.

## References

1. S. Samadi, J. I. Caiza, S. Gracy, and P. E. Paré, *A Networked SIS Epidemic–Opinion Model with Higher-Order Interactions*, arXiv:2608.31032, first posted 2026-08-31. https://arxiv.org/html/2608.31032
2. K. Frieswijk, L. Zino, M. Ye, A. Rizzo, and M. Cao, *A mean-field analysis of a network behavioural-epidemic model*, arXiv:2203.04016 (2022). https://arxiv.org/abs/2203.04016
3. D. Juher, D. Rojas, and J. Saldaña, *Robustness of behaviorally induced oscillations in epidemic models under a low rate of imported cases*, Phys. Rev. E 102, 052301 (2020). https://doi.org/10.1103/PhysRevE.102.052301
