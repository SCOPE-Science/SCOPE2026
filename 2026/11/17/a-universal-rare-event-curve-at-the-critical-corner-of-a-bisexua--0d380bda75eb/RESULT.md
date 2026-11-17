# A universal rare-event curve at the critical corner of a bisexual quadratic map

## Finding

Fix \(0<a,b<1\), set \(q=1-b\) and \(U=\min\{1,a/q\}\), and iterate the quadratic stochastic population map
\[
(X_{n+1},Y_{n+1})=\bigl(X_n+a(1-X_n)Y_n,\;Y_n[X_n+b(1-X_n)]\bigr).
\]
Let \((X_0,Y_0)\) be uniformly distributed on the unit square. For every continuous compactly supported function \(F:[0,\infty)^2\to\mathbb R\),
\[
\boxed{\lim_{n\to\infty}n\,\mathbb E\left[F\bigl(qn(1-X_n),\,anY_n\bigr)\right]
=\frac Ua\int_{-\infty}^{\infty}
F\left(\frac{t}{e^t-1},\frac{te^t}{e^t-1}\right)\,dt.}
\]
Both fractions take their continuous value \(1\) at \(t=0\). Equivalently, the finite measures \(n\) times the laws of the rescaled transient populations converge *vaguely* to a measure supported on the explicit curve parameterized above, with constant \(t\)-intensity \(U/a\). The limiting measure is locally finite but not finite.

There is an exact, readily observable conditional formulation. Define the conserved signed offset
\[
D=X_0+\frac aqY_0-1
\]
and put \(T_n=qnD\). For every fixed \(K>0\),
\[
\mathbb P\{|T_n|\le K\}=\frac{2KU}{an}+o(n^{-1}).
\]
Conditionally on \(|T_n|\le K\), the triple
\[
\bigl(T_n,qn(1-X_n),anY_n\bigr)
\]
converges in law to \(\bigl(T,f(T),f(T)+T\bigr)\), where \(T\) is uniform on \([-K,K]\) and \(f(t)=t/(e^t-1)\). In particular, the two transient populations retain a strongly dependent, nonlinear universal profile within a probability-\(n^{-1}\) critical strip of starting states.

## Assumptions and scope

The parameters \(a,b\) are fixed strictly between zero and one. The initial coordinates are independent uniform random variables on \([0,1]\), equivalently normalized Lebesgue measure on the square. The time index \(n\) is an integer tending to infinity. The weak conditional law holds for any fixed finite \(K>0\). The vague limit tests only compactly supported continuous functions, not functions with an unrestricted tail. The primary object is the discrete-time dynamics and its transient critical-layer selection, rather than a random perturbation of the map.

For context, the map has an equilibrium on either boundary \(Y=0\) or \(X=1\). Their intersection \((1,0)\) is nonhyperbolic. A single invariant line passes through each initial point, and the long-term equilibrium changes boundary precisely as the signed invariant \(D\) changes sign. Those qualitative features were already established in the originating work.

## Proof

**1. Invariant and exact scalar dynamics.** Put \(u_n=1-X_n\), \(d=D\). Direct subtraction gives
\[
X_{n+1}-X_n=au_nY_n,
\qquad Y_{n+1}-Y_n=-qu_nY_n,
\]
hence \(d=X_n+(a/q)Y_n-1\) is invariant, and
\[
Y_n=\frac qa(u_n+d),\qquad
u_{n+1}=u_n\,[1-q(u_n+d)]. \tag{1}
\]
The square is forward invariant: \(X_n\) increases in \([0,1]\) and \(Y_n\) decreases in \([0,1]\). In particular \(q(u_n+d)=aY_n\in[0,a]\). There is no singularity in the following reciprocal estimates as long as the starting point lies in the interior.

**2. Uniform near-critical transient profile.** Fix \(K>0\) and a compact initial interval \(\varepsilon\le u_0\le U-\varepsilon\) with \(\varepsilon>0\). Write \(d=t/(qn)\) where \(|t|\le K\), and for the first \(n\) steps define \(h_j=1/(nu_j)\). Equation (1) yields the *exact* difference equation
\[
h_{j+1}-h_j=\frac{t h_j+q}{n\,[1-t/n-qu_j]},
\qquad h_0=\frac1{nu_0}. \tag{2}
\]
The denominator is \(1-aY_j\ge1-a>0\), and the numerator is nonnegative. The upper bound
\[
0\le h_{j+1}-h_j\le\frac{Kh_j+q}{n(1-a)}
\]
gives \(\max_{j\le n}h_j=O_{a,K,\varepsilon}(1)\) by discrete Gronwall.

For a bound on the total nonlinear discretization error, use \(d\ge-K/(qn)\) in (1):
\[
u_{j+1}\le u_j(1+K/n-qu_j).
\]
Set \(v_j=e^{-Kj/n}u_j\). Since \(e^{-K/n}(1+K/n)\le1\), for \(n\) large enough one has
\[
v_{j+1}\le v_j\left(1-\frac{q}{1+K}v_j\right).
\]
(The displayed inequality follows by comparing the two coefficients; all factors remain nonnegative.) It follows that
\[
u_j\le\frac{e^K}{u_0^{-1}+qj/(1+K)},
\qquad \sum_{j=0}^{n-1}u_j=O_{a,K,\varepsilon}(\log(n+1)). \tag{3}
\]
Therefore, comparing (2) with forward Euler for \(H'(s)=tH(s)+q\), \(H(0)=0\), and using \(|t|\le K\), gives uniformly
\[
\max_{0\le j\le n}|h_j-H(j/n)|
=O_{a,K,\varepsilon}\!\left(\frac{1+\log n}{n}\right).
\]
Here \(H(1)=q(e^t-1)/t\), interpreted as \(q\) at \(t=0\); this is strictly positive and uniformly bounded away from zero for \(|t|\le K\). Thus
\[
qn u_n\longrightarrow f(t)=\frac{t}{e^t-1},
\qquad anY_n=qn u_n+t\longrightarrow f(t)+t
=\frac{te^t}{e^t-1} \tag{4}
\]
uniformly for \(|t|\le K\) and \(u_0\) in any fixed compact subinterval of \((0,U)\).

**3. Initial-square area and the limiting measure.** The affine change of variables \((X_0,Y_0)\mapsto(u_0,d)\) has unsigned Jacobian \(q/a\), and the unit square becomes
\[
0\le u_0\le1,\qquad 0\le u_0+d\le a/q. \tag{5}
\]
Using \(t=qn d\), exactly \(n\,dX_0dY_0=(1/a)\,du_0dt\). A compactly supported \(F\) has \(F(z_1,z_2)=0\) outside a sufficiently large compact set. Whenever its argument is in the support, the invariant identity
\[
anY_n-qn(1-X_n)=qn d=t
\]
forces \(|t|\le K_F\) for a constant depending only on that support. On this bounded \(t\)-range, the admissible intervals in (5) converge to \([0,U]\). Apply the uniform convergence (4) on \(\varepsilon\le u_0\le U-\varepsilon\). The discarded endpoint strips have arbitrarily small total \(n\)-weighted area (at most a constant times \(\varepsilon\)), because the Jacobian is exactly constant and \(|F|\) is bounded. Letting \(\varepsilon\downarrow0\) proves the displayed vague limit with coefficient \(U/a\).

The event \(|qnD|\le K\) corresponds to a literal strip in (5). Its area is \((1/a)\int_{-K}^K\!\ell_n(t)\,dt/n\), where \(\ell_n(t)\) is the length of the allowed \(u_0\)-interval and converges uniformly to \(U\). This proves the stated probability asymptotic. Conditional uniformity of \(t\) and the joint curve limit follow from the same argument using bounded continuous test functions on the compact range \(t\in[-K,K]\).

**4. The exactly critical fiber, as a cross-check.** If \(d=0\) and \(u_0\in(0,U)\), let \(z_j=1/(qu_j)\). Then \(z_j>1\) and (1) gives
\[
z_{j+1}=z_j+1+\frac1{z_j-1}.
\]
Consequently \(z_j=j+O(\log j)\). The series of differences of \(z_j-j-\log j\) is summable, because its summands are \(O(\log j/j^2)\). Thus there exists a finite initial-condition-dependent \(C\) such that
\[
\frac1{qu_j}=j+\log j+C+o(1).
\]
This finer pointwise result is consistent with the central value \(f(0)=1\) in (4), but is not necessary for the rare-event integration.

## Verification

A standalone numerical checker (`check.py`) evaluates the exact discrete map at finite generation, computes the critical-layer predicted quadrature, verifies the invariant, and checks the logarithmically corrected reciprocal recurrence. The script prints `BOXONOV_LAYER_CHECK_OK` on successful numerical tests. Numerical convergence is corroboration, not a substitute for the uniform analytic estimates in the proof. The only infinite-limit claims are those proved above.

## Relationship to prior work

Boxonov introduced this bisexual-population quadratic operator and identified its fixed points, invariant straight lines, and ultimate states (arXiv:2303.03884v1, §3, especially Eq. (3.6), Lemma 1 and Theorem 2). These prior results are essential and not claimed as new. The present statement treats the finite-generation distribution of the *two* minority coordinates when the starting population is sampled from the full square; it identifies a probability-\(n^{-1}\) critical strip and its exact two-coordinate limiting intensity.

Teixeira and collaborators studied critical scaling and inverse-generation relaxation in one-dimensional logistic-like maps (arXiv:1502.06437v1). Such scalar scaling is an acknowledged ingredient, but the inspected account does not assert the joint finite-generation pushforward-measure law, the explicit critical-curve support, or its geometric prefactor for this bisexual map. A general theorem on parabolic maps and absolutely continuous initial ensembles might subsume this special case; that remains a priority uncertainty rather than a uniqueness claim.

## Limitations

The result does not claim a rate for convergence of the full vague measure; the proof gives a uniform compact-interior bound only. It does not establish convergence in total variation of global rescaled distributions: the limiting measure has infinite mass. The result is not uniform as either model parameter approaches the boundary of its allowed interval and does not cover deterministic initial data concentrated on the critical fiber or an arbitrary nonsmooth initial distribution. Publication priority relative to unindexed general parabolic-map limit theorems is not independently certified.

## References

1. Z. S. Boxonov, *On dynamical systems of quadratic stochastic operators constructed for bisexual populations*, arXiv:2303.03884v1 (first publicly available 2023-03-07), https://arxiv.org/abs/2303.03884. See §3 and Theorem 2.
2. R. M. N. Teixeira, D. S. Rando, F. C. Geraldo, R. N. Costa Filho, J. A. de Oliveira and E. D. Leonel, *Convergence towards asymptotic state in 1-D mappings: a scaling investigation*, arXiv:1502.06437v1 (2015), https://arxiv.org/abs/1502.06437.
