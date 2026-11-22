# Global escape and recurrence rigidity in the odd negative secant model

## Finding
Let \(d\ge3\) be any **odd integer**, let \(c>0\), and consider the exact polynomial map
\[
T_{c,d}(x,y)=\bigl(y+c(x+y)^d,\ y+2c(x+y)^d\bigr).
\]
For \(s=x+y\) and \(z=y-x\), define the two nonempty closed-sided escape cones
\[
\mathcal C_+=\{s>0,\ |z|\le c|s|^d\},\qquad
\mathcal C_-=\{s<0,\ |z|\le c|s|^d\}.
\]
**Global classification.** For every real initial condition, exactly one of the following alternatives holds:

1. Its forward orbit converges to \((0,0)\).
2. Its forward orbit eventually belongs to \(\mathcal C_+\), remains there, and escapes to infinity along the positive \((1,2)\) ray.
3. Its forward orbit eventually belongs to \(\mathcal C_-\), remains there, and escapes to infinity along the negative \((1,2)\) ray.

For an escaping orbit, write \(s_n=x_n+y_n\) and \(r_n=|s_n|\). There is a uniquely defined \(H=H(x_0,y_0)>0\) such that
\[
\frac{(x_n,y_n)}{s_n}\longrightarrow\left(\frac13,\frac23\right),
\qquad
H=\lim_{n\to\infty}\frac{\log r_n}{d^n},
\qquad
r_n=(3c)^{-1/(d-1)}\exp\bigl(Hd^n+o(1)\bigr).
\]
The only nonwandering point of \(T_{c,d}\) is the origin. Consequently \(\delta_{(0,0)}\) is its **unique invariant Borel probability measure** (without a moment or compact-support assumption). In particular, there are no nonzero periodic orbits or other bounded recurrent orbits.

## Assumptions and scope
The phase space is the entire real plane, forward time is the integer \(n\ge0\), and \(d\) ranges over all odd integers at least three. The parameter \(c\) is an arbitrary positive real number. The theorem concerns the negative-coefficient branch \(a=-c<0\) of the model \(T_{a,d}=(y-a(x+y)^d,\ y-2a(x+y)^d)\) introduced in the cited source. It makes no assertion about the untruncated secant method, even degrees, or the positive-coefficient odd branch. The two escape cones have disjoint sign and each contains an open set, so both alternatives occur.

The attracting set \(\{(x,y):T_{c,d}^n(x,y)\to0\}\) was previously identified as the global stable manifold of the origin. That identification is not claimed as new. The new content is the exhaustive fate of its complement, the explicit finite-entry escape channels and sharp height, and the global absence of any other recurrent or stationary probability dynamics.

## Proof
**1. Exact coordinates and a strict Lyapunov function.** Introduce \(s=x+y\), \(z=y-x\), and \(w=c s^d\). Direct substitution gives the *global* polynomial recurrence
\[
s'=s+z+3w,\qquad z'=w.
\]
Set \(V(s)=c s^{d+1}/(d+1)\), a convex differentiable function on \(\mathbb R\) because \(d\) is odd, and define
\[
L(s,z)=V(s)-z^2.
\]
Its exact one-step difference is
\[
\begin{aligned}
L(s',z')-L(s,z)
&=\underbrace{V(s')-V(s)-V'(s)(s'-s)}_{B_V(s',s)\ge0}
 +2w^2+wz+z^2\\
&=B_V(s',s)+\left(z+\frac w2\right)^2+\frac74w^2.
\end{aligned}
\]
The Bregman term is nonnegative by convexity. The two squares vanish together only when \(s=z=0\). Thus \(L\) **strictly increases at every nonzero point**, for all parameter values in the stated domain.

**2. Escape versus convergence.** If \(L(s_n,z_n)\) is bounded above along a forward orbit, summing the preceding identity gives
\[
\sum_{n\ge0}\left[\left(z_n+\frac{c s_n^d}{2}\right)^2+\frac74c^2s_n^{2d}\right]<\infty.
\]
Hence \(s_n\to0\) and \(z_n\to0\), implying \((x_n,y_n)\to0\). More generally, if a forward orbit has a bounded subsequence, the values of the continuous function \(L\) on that subsequence are bounded above. Monotonicity of \(L\) then bounds \(L\) on *every* forward iterate, and the same summation proves convergence to zero. The contrapositive proves that every orbit not converging to the origin satisfies
\[
\|(x_n,y_n)\|\longrightarrow\infty.
\]
This excludes bounded aperiodic motion as well as nontrivial periodic motion; it is stronger than merely knowing the geometry of the origin's basin.

**3. Explicit absorbing escape cones.** If \(s\ne0\) and \(|z|\le c|s|^d\), multiplication of \(s'=s+z+3c s^d\) by the sign of \(s\) yields
\[
\operatorname{sgn}(s)s'\ge |s|+2c|s|^d>|s|.
\]
Also \(|z'|=c|s|^d\le c|s'|^d\). Thus each \(\mathcal C_\pm\) is forward invariant, its sign cannot change, and the magnitudes of the successive sum coordinates strictly increase. The inequality \(r_{n+1}\ge r_n+2c r_n^d\) forces \(r_n\to\infty\).

For an orbit that escapes, \(|s_n|\) and \(|s_{n-1}|\) cannot decrease indefinitely; otherwise both would be bounded, and so would \(z_n=c s_{n-1}^d\), contradicting the escape conclusion of Step 2. At arbitrarily late indices there is therefore an \(n\) with \(|s_n|\ge |s_{n-1}|\), and \(s_n\ne0\) since the orbit escapes. The exact recurrence \(z_n=c s_{n-1}^d\) gives \(|z_n|\le c|s_n|^d\). Hence every escaping orbit enters exactly one of the two cones in finite time and stays in it.

**4. Sharp two-ray superexponential escape.** After one additional iteration in a cone the successive \(s_n\) have the same sign. Put \(r_n=|s_n|\). For all sufficiently large \(n\),
\[
r_{n+1}=r_n+3cr_n^d+cr_{n-1}^d
=3cr_n^d(1+e_n),\qquad
e_n=\frac{r_n+cr_{n-1}^d}{3cr_n^d}>0.
\]
Since \(r_n\ge3cr_{n-1}^d\), we have the **actual all-degree bound**
\[
0<e_n\le\frac{4}{9c}r_n^{1-d}\longrightarrow0.
\]
Let \(W_n=\log r_n+\log(3c)/(d-1)\). Then
\[
W_{n+1}=dW_n+\log(1+e_n).
\]
It follows by a convergent geometric series of increments that \(d^{-n}W_n\to H\). Moreover, for sufficiently large \(n\), \(W_n>0\), all corrections are positive, and hence \(H>0\). The exact tail identity
\[
Hd^n-W_n=\sum_{k=n}^\infty d^{n-k-1}\log(1+e_k)\longrightarrow0
\]
follows from \(e_k\to0\), giving the claimed multiplicative constant. Finally \(z_n=c s_{n-1}^d\) has the same eventual sign as \(s_n\), and \(z_n/s_n\to1/3\) by the preceding recurrence. Since \(x_n=(s_n-z_n)/2\) and \(y_n=(s_n+z_n)/2\), their normalized ratio tends to \((1/3,2/3)\).

**5. Nonwandering and invariant probabilities.** At every nonzero point \(p\), continuity of \(L\) and the strict increment gives an open neighborhood \(U\ni p\) and \(\eta>0\) with \(L(Tq)-L(q)>\eta\) for all \(q\in U\), while the oscillation of \(L\) on \(U\) is smaller than \(\eta\). Since \(L\) never decreases, \(T^n(U)\cap U=\varnothing\) for every \(n\ge1\). Thus every nonzero point is wandering; the origin is fixed. By Poincaré recurrence, every invariant Borel probability assigns mass zero to such a wandering neighborhood. A countable subcover of \(\mathbb R^2\setminus\{0\}\) shows its entire mass is at the origin. The point mass at the fixed origin is invariant, proving uniqueness.

## Verification
Run `python verify_secant.py` with Python 3. It evaluates the exact conjugacy and Lyapunov inequality using rational arithmetic at 441 parameter/phase triples with odd degrees 3, 5 and 7 and positive rational parameters, verifies invariance of the two cones on 222 qualifying triples, and checks 48 exact coordinate transformations on representative trajectories. All checks passed on the packaged script. These tests corroborate, but cannot replace, the convexity, cone, and infinite-time arguments above.

## Relationship to prior work
Fontich, Garijo and Jarque introduced this exact truncated secant model and proved that for odd degree and negative coefficient its origin basin equals an unbounded stable manifold (Theorem A(c) and Section 6). Their result does **not state** that all orbits outside the stable manifold escape, that the map is globally free of nonzero recurrence, that its only invariant probability is the origin mass, or the two signed ray and superexponential-height asymptotics established above. A same-model published result for **even degrees** gives a one-ray escape classification and related sharp growth estimates; because it assumes even degree, it does not imply this odd-degree negative-sign classification. The companion work on homoclinic intersections takes the opposite, **positive** coefficient in odd degree and describes chaotic invariant dynamics instead of the gradient-like negative branch.

## Limitations
The global alternative applies only to the exact polynomial model, not to higher-order perturbations or to the untruncated rational secant map. The stable manifold is not parametrized explicitly here. The positive height \(H\) is defined by an orbit limit, not an elementary formula in the initial data; no uniform entrance-time bound is claimed. The analytical Lyapunov and escape proofs hold in all odd degrees, while the accompanying finite tests sample only three. An unindexed mathematically equivalent treatment may exist; independent external mathematical review has not been carried out.

## References
1. E. Fontich, A. Garijo, X. Jarque, *On the basin of attraction of a critical three-cycle of a model for the secant map*, arXiv:2405.08791v1 (first posted 2024-05-14), https://arxiv.org/abs/2405.08791; Discrete and Continuous Dynamical Systems 45 (2025), 1045–1078, https://doi.org/10.3934/dcds.2024122. In particular Theorem A(c) and Section 6.
2. E. Fontich, A. Garijo, X. Jarque, *Chaotic dynamics at the boundary of a basin of attraction via non-transversal intersections for a non-global smooth diffeomorphism*, arXiv:2405.08812v1 (2024-05-14), https://arxiv.org/abs/2405.08812; Journal of Nonlinear Science 34 (2024), 102, https://doi.org/10.1007/s00332-024-10079-7. Opposite coefficient in odd degree.
3. *Universal escape direction and exact superexponential scale for an even-degree secant model*, published 2026-10-11, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-universal-escape-direction-and-exact-superexponential-scale-for--329ac93ba819/RESULT.md. Even-degree result, disjoint parameter domain.
