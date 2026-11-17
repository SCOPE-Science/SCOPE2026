# Sharp single-site amplification thresholds in globally attracting competition cascades

## Finding

**Theorem.** For every integer \(n\ge2\) and parameters \(d,b>0\), consider the directed generalized Lotka–Volterra competition cascade
\[
\dot x_i=x_i(d+b-dx_i-bx_{i+1})\quad(1\le i<n),\qquad
\dot x_n=d x_n(1-x_n).
\]
Every strictly positive initial state exists globally and converges to the unique positive equilibrium \({\bf1}=(1,\ldots,1)\). Its Jacobian at that equilibrium is Hurwitz with all eigenvalues equal to \(-d\).

For the normalized first-order deviation from a positive pulse of size \(\varepsilon\) in **one species only**, define
\[
R_{n,j}(t)=\lim_{\varepsilon\downarrow0}\frac{\|x(t;{\bf1}+\varepsilon e_j)-{\bf1}\|_2}{\varepsilon}\qquad(1\le j\le n).
\]
All limits exist, and, setting \(F_j(v)=\sum_{r=0}^{j-1}v^{2r}/(r!)^2\), one has the exact identity
\[
R_{n,j}(t)^2=e^{-2dt}F_j(bt).
\]
Put
\[
\gamma_n=\max_{v>0}\frac{\log F_n(v)}{2v},\qquad \kappa_n=\frac1{\gamma_n},\qquad
\rho_n=\sec\!\left(\frac{\pi}{n+1}\right).
\]
Then the following is a sharp all-time, all-species classification:

1. Some initially increased *single* species creates a Euclidean deviation exceeding its starting size at a later positive time **if and only if** \(b/d>\kappa_n\). The terminal species \(j=n\) is always an optimal single-site choice; no other site can exceed its response at the same positive time.
2. At \(b/d=\kappa_n\), the terminal response touches but does not cross one at some strictly positive time. For every \(b/d\le\kappa_n\), all such single-site responses remain at most one at all positive times. All of them contract immediately after the pulse, regardless of \(b/d\).
3. The full linear semigroup admits amplification of *some* (possibly sign-changing) perturbation if and only if \(b/d>\rho_n\), and the two thresholds are strictly separated for every \(n\):
\[
1<\rho_n<\kappa_n.
\]
4. The single-site threshold decreases strictly with the number of species and obeys the sharp dimension law
\[
\boxed{\lim_{n\to\infty}\frac{n(\kappa_n-1)}{\log n}=\frac14},\qquad
\rho_n-1=\frac{\pi^2}{2(n+1)^2}+O(n^{-4}).
\]
For two species, writing \(u\in(1/2,1)\) for the unique nonzero root of \((1-u)e^{2u}=1\), the threshold is exactly
\[
\kappa_2=\frac{e^u}{\sqrt u}=2.485267512660\ldots.
\]
These are statements about infinitesimal perturbations in the stated Euclidean coordinates; the finite-size nonlinear response is not asserted to exceed its original amplitude for arbitrary \(\varepsilon\).

## Assumptions and scope

Every \(x_i(0)>0\); the last compartment has only logistic self-regulation, and each earlier compartment is inhibited by its immediate successor. Parameters \(d,b\) are homogeneous and strictly positive. Time is continuous and no noise, forcing, or migration is included. The norm \(\|\cdot\|_2\) refers to species coordinates with compatible units. A single-site pulse is a *positive perturbation from coexistence*, not an arbitrary initial population in a positive cone. The comparison with full reactivity concerns unconstrained signed tangent perturbations.

## Proof

**Global nonlinear behavior.** Positivity is forward invariant. Each coordinate satisfies \(\dot x_i\le x_i(d+b-dx_i)\), hence all positive solutions are global and bounded. The terminal logistic equation gives \(x_n(t)\to1\). Suppose by backward induction that \(x_{i+1}(t)\to1\). Write \(r_i(t)=d+b-bx_{i+1}(t)\to d\), so \(\dot x_i=x_i(r_i(t)-dx_i)\). Its reciprocal \(z_i=1/x_i\) satisfies the exact linear equation \(\dot z_i=-r_i(t)z_i+d\). Since eventually \(r_i(t)>d/2\), variation of constants implies \(z_i(t)\to1\), and therefore \(x_i(t)\to1\). Backward induction proves global convergence. Setting derivatives to zero backward from the terminal species shows \({\bf1}\) is the only positive equilibrium.

**Impulse response.** The Jacobian is \(J_n=-dI_n-bS_n\), where \((S_n)_{i,i+1}=1\) and \(S_n^n=0\). Smooth dependence on initial conditions gives the linear-response limit \(e^{tJ_n}e_j\). Directly from the finite nilpotent exponential,
\[
e^{tJ_n}e_j=e^{-dt}\sum_{r=0}^{j-1}\frac{(-bt)^r}{r!}e_{j-r},
\]
so orthogonality of coordinates yields the stated \(R_{n,j}\) formula. For every \(t>0\), \(F_n(bt)>F_j(bt)\) if \(j<n\), while \(R_{n,j}(0)=1\) and \(\partial_tR_{n,j}(0)=-d<0\). Consequently the terminal pulse is strictly dominant at all positive times despite *every* single pulse contracting initially.

**Sharp restricted threshold and tangency.** For fixed \(n\ge2\), define \(q_n(v)=\log F_n(v)/(2v)\) for \(v>0\). Since \(F_n(v)=1+v^2+O(v^4)\) as \(v\downarrow0\), we have \(q_n(v)\to0\) at zero. Since \(F_n\) is a polynomial, \(q_n(v)\to0\) also as \(v\to\infty\). It is positive, hence attains a positive maximum \(\gamma_n\) at some finite \(v_n>0\). Upon writing \(v=bt\),
\[
\log R_{n,n}(t)^2=\log F_n(v)-2(d/b)v=2v(q_n(v)-d/b).
\]
The exact crossing criterion is \(d/b<\gamma_n\), equivalent to \(b/d>\kappa_n\). At equality the response equals one at \(t=v_n/b>0\), with zero derivative there by Fermat's rule; for smaller couplings it stays strictly below one for \(t>0\). This proves the sharp threshold without assuming uniqueness of \(v_n\).

**Full reactivity and the strict mismatch.** The symmetric part of \(J_n\) is \(-dI_n-(b/2)(S_n+S_n^{\mathsf T})\). Diagonalizing the path adjacency matrix yields its largest eigenvalue \(-d+b\cos(\pi/(n+1))\). A time-independent real matrix has \(\|e^{tJ_n}\|_2\le1\) for all \(t\ge0\) exactly when its symmetric part is negative semidefinite: sufficiency follows by differentiating squared norm, and necessity from its top Rayleigh vector at time zero. Hence unrestricted amplification occurs exactly when \(b/d>\rho_n\).

At \(b/d=\rho_n\) all deviations have nonincreasing norm, and the terminal response has strictly negative initial derivative; therefore \(R_{n,n}(t)<1\) for **every** \(t>0\). A uniform small-time estimate (the initial derivative is \(-d\) for every coupling), uniform large-time decay on any compact coupling interval (each response is an exponential times a fixed-degree polynomial), and compactness of intermediate times show that \(R_{n,n}(t)<1\) still holds for a nonempty open coupling interval immediately above \(\rho_n\). Thus \(\kappa_n>\rho_n>1\) for finite \(n\).

**Monotonicity and the logarithmic dimension law.** The strict inequalities \(F_{n+1}(v)>F_n(v)\) for \(v>0\) imply \(\gamma_{n+1}>\gamma_n\), so \(\kappa_n\) decreases strictly. To compute its asymptotics put \(I_0(2v)=\sum_{j=0}^{\infty}v^{2j}/(j!)^2\). The integral representation \(I_0(2v)=(2\pi)^{-1}\int_{-\pi}^{\pi}e^{2v\cos\theta}\,d\theta\) and elementary Laplace estimation yield
\[
\log I_0(2v)=2v-\tfrac12\log(4\pi v)+O(v^{-1})\qquad(v\to\infty).
\]
For \(v=n-\sqrt n\), Stirling's formula uniformly on the \(\lfloor\sqrt n/5\rfloor\) integers with \(v-\sqrt v/5\le j\le v\) gives \(v^{2j}/(j!)^2\ge c e^{2v}/v\), with a fixed \(c>0\) and all those indices below \(n\) for large \(n\). Summing yields \(F_n(v)\ge c' e^{2v}/\sqrt n\). Consequently
\[
\gamma_n\ge1-\frac{\log n}{4n}+O(n^{-1}),
\]
and in particular \(\gamma_n\to1\).

Let \(v_n\) be any maximizer of \(q_n\). We claim \(v_n/n\to1\). For any \(\epsilon\in(0,1)\), convexity of \(\log I_0(2v)\) (a log moment-generating function) and its zero value at zero show that \(\log I_0(2v)/(2v)\) is nondecreasing. Thus whenever \(v\le(1-\epsilon)n\),
\[
q_n(v)\le\frac{\log I_0(2(1-\epsilon)n)}{2(1-\epsilon)n}
=1-\frac{\log n}{4(1-\epsilon)n}+O(n^{-1}),
\]
which is strictly smaller for large \(n\) than the preceding lower bound for \(\gamma_n\). For \(v\ge(1+\epsilon)n\), the terms of \(F_n\) increase through index \(n-1\), giving \(F_n(v)\le n[v^{n-1}/(n-1)!]^2\). Stirling and the strict inequality \((1+\log r)/r<1\) for \(r>1\) imply uniformly for such \(v\) that
\[
q_n(v)\le\sup_{r\ge1+\epsilon}\frac{1+\log r}{r}+o(1)<1.
\]
Both ranges are excluded by \(\gamma_n\to1\), proving \(v_n/n\to1\).

Finally, \(F_n(v_n)\le I_0(2v_n)\) and the displayed Laplace asymptotic give
\[
1-\gamma_n\ge\frac{\log(4\pi v_n)}{4v_n}+O(v_n^{-2})
=\frac{\log n}{4n}(1+o(1)),
\]
while the Stirling lower bound gives the opposite asymptotic inequality. Hence \(1-\gamma_n\sim(\log n)/(4n)\), and since \(\kappa_n=1/\gamma_n\) the boxed limit follows. Taylor expansion of \(\sec(\pi/(n+1))\) gives the separate unrestricted threshold law.

**Two-species closed form.** For \(n=2\), the stationarity equation for \(q_2(v)=\log(1+v^2)/(2v)\) is \(2v^2/(1+v^2)=\log(1+v^2)\). With \(u=v^2/(1+v^2)\), this becomes \((1-u)e^{2u}=1\). Besides the endpoint solution \(u=0\), the logarithm of the left-hand side is strictly concave and crosses zero once in \((1/2,1)\). At this root \(\gamma_2=\sqrt{u(1-u)}\), whence \(\kappa_2=e^u/\sqrt u\), proving the displayed value.

## Verification

The standard-library Python script `verify.py` evaluates the finite exponential and threshold equations, locates candidate tangencies for nine dimensions, tests the strict gap against the known full-reactivity formula, and cross-checks the two-species equation. Run `python3 verify.py`; the last line is `VERIFY_OK ...`. Its finite numerical tests are not an exhaustive check of all parameters or a substitute for the preceding proof.

## Relationship to prior work

Márquez, Chaib De Mares and Riascos investigate transient and stationary differences of generalized Lotka–Volterra processes on directed networks, motivating a test that discriminates between disturbances of distinct spatial support. Mari and collaborators' generalized ecological reactivity framework examines the role of chosen outputs and focal species, but its initial-time Hermitian-matrix criterion does not give a threshold for a single-site initial input at *any later time*. The published study *Exact no-amplification window for an inhibitory feedback ring* gives the complete instantaneous/operator-norm window of a related linear chain, and its open-chain reactivity formula coincides with the unrestricted boundary \(\rho_n\) here; that boundary is prior mathematics, not claimed new. Existing finite Jordan-block peak studies optimize over all initial vectors at selected dimensions rather than an exact one-site, all-dimension onset with its logarithmic scaling. The new assertion is the separation of restricted pulse amplification and unrestricted growth, including \(\kappa_n\) and its sharp asymptotic.

## Limitations

These exact results apply to a homogeneous directed competition cascade. The norm depends on coordinate scaling and the restricted pulse is infinitesimal; they do not imply large finite ecological interventions must amplify, nor that reactivity is ecologically beneficial. The threshold is defined by a one-dimensional maximization, with a closed form stated only for \(n=2\); uniqueness of positive maximizing times for every \(n\) is not claimed. Earlier generic nonnormal-matrix or special-function work might contain an equivalent formula not located by the literature searches. Independent validation has not occurred.

## References

1. N. A. Márquez, M. Chaib De Mares and A. P. Riascos, *Dissimilarity measures for generalized Lotka-Volterra systems on networks*, arXiv:2511.12701v1 (first publicly posted 2025-11-16), https://arxiv.org/abs/2511.12701.
2. L. Mari, R. Casagrandi, A. Rinaldo and M. Gatto, *A generalized definition of reactivity for ecological systems and the problem of transient species dynamics*, Methods in Ecology and Evolution 8 (2017), 1574–1584, https://doi.org/10.1111/2041-210X.12805.
3. *Exact no-amplification window for an inhibitory feedback ring*, published result dated 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-no-amplification-window-for-an-inhibitory-feedback-ring--43e519971d5d.
4. *Certified finite-horizon transient-peak intervals for Hurwitz-stable \(T_n=-I+2N\)*, published result dated 2026-09-09, https://github.com/published-finding corpus/2026/tree/main/2026/9/9/SCOPE008.
5. *Sharp metric-conditioning phase transition for a four-stage positive cascade*, published result dated 2026-10-12, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-sharp-metric-conditioning-phase-transition-for-a-four-stage-posi--2d808ba1bdde.
