# Exact weak-selection clock for a two-sex Volterra map near its neutral continuum

## Finding

A four-parameter two-sex Volterra quadratic stochastic map has a neutral curve of fixed states when its heredity determinant vanishes. Near this balance, the entire slow evolution is described by a **single explicit logarithmic clock** on the inverse-determinant time scale. This statement concerns the *time scale and transition profile*, not the already known global convergence classification.

Fix \(a,b,c\in(0,1)\) with \(ac<b\). For \(\varepsilon\ne0\) sufficiently small, set \(d_\varepsilon=(ac+\varepsilon)/b\in(0,1)\), and iterate
\[
 x_{n+1}=x_n-a x_n(1-y_n)+b y_n(1-x_n),\qquad
 y_{n+1}=y_n+d_\varepsilon x_n(1-y_n)-c y_n(1-x_n).
\]
Let \(z_0=(x_0,y_0)\in[0,1]^2\setminus\{(0,0),(1,1)\}\) be independent of \(\varepsilon\). Define
\[
 R(t)=a+(b-a)t,\quad X(t)=\frac{bt}{R(t)},\quad
 Q(t)=t+\frac{ct}{R(t)},\quad
 H_0=y_0+\frac cb x_0.
\]
The strictly increasing function \(Q:[0,1]\to[0,1+c/b]\) gives a unique \(t_0\in(0,1)\) with \(Q(t_0)=H_0\). Define
\[
 G(t)=(a+c)\log t-\left(b+\frac{ac}{b}\right)\log(1-t)
       -\frac{c(b-a)}b\log R(t),\qquad 0<t<1.
\]
Then \(G\) is a strictly increasing bijection from \((0,1)\) onto \(\mathbb R\). Put \(\sigma=\operatorname{sgn}\varepsilon\) and define the explicit slow profile \(t_\sigma(\tau)\) by
\[
 G(t_\sigma(\tau))=G(t_0)+\sigma\tau,\qquad \tau\ge0.
\]
For every finite \(T>0\), there is \(K_T<\infty\) such that, for all sufficiently small \(|\varepsilon|\),
\[
\sup_{0\le \tau\le T}\left|y_{\lfloor\tau/|\varepsilon|\rfloor}
+\frac cb x_{\lfloor\tau/|\varepsilon|\rfloor}
-Q(t_\sigma(\tau))\right|\le K_T|\varepsilon|.
\]
Moreover, for every \(0<\delta<T\), possibly increasing \(K_T\),
\[
\sup_{\delta\le\tau\le T}\left\|
\begin{pmatrix}x_{\lfloor\tau/|\varepsilon|\rfloor}\\y_{\lfloor\tau/|\varepsilon|\rfloor}\end{pmatrix}
-\begin{pmatrix}X(t_\sigma(\tau))\\t_\sigma(\tau)\end{pmatrix}
\right\|\le K_T|\varepsilon|.
\]
If \(z_0=(X(t_0),t_0)\) lies on the neutral fixed curve, the last estimate holds already for \(\delta=0\).

This yields a **sharp inverse-determinant scale** for passage between any two distinct interior neutral states. The limiting rescaled time from \(t=p\) to \(t=q\), in the appropriate direction, is \(|G(q)-G(p)|\). The slow profile has explicit endpoint exponents:
\[
1-t_+(\tau)\asymp e^{-\tau/(b+ac/b)},\qquad
 t_-(\tau)\asymp e^{-\tau/(a+c)}\qquad(\tau\to\infty).
\]
The two exponents agree with the small-determinant expansions of the actual fixed-point Perron multipliers.

## Assumptions and scope

All coefficients are **strictly interior**: \(0<a,b,c<1\), \(ac<b\), and \(d_\varepsilon\in(0,1)\). The perturbation changes only \(d\), while \(a,b,c\) and the initial condition remain fixed. The limit \(\varepsilon\to0\) is one-sided or two-sided with the sign \(\sigma\) fixed. Norms on \(\mathbb R^2\) are arbitrary but fixed. The constants in the estimates may depend on these fixed coefficients, the initial state and \(T\), not on \(\varepsilon\). No claim of a uniform-in-\(T\) error estimate is made. The initial two corners are stationary for all parameters and are excluded from the logarithmic profile.

## Proof

**1. Exact neutral projection and transverse contraction.** Set \(H(x,y)=y+(c/b)x\). Direct expansion gives the *exact* drift identity
\[
H(F_\varepsilon(x,y))-H(x,y)=\frac\varepsilon b x(1-y).
\]
At \(\varepsilon=0\), each chord \(H=h\) is invariant and has a unique equilibrium \(\Gamma(h)=(X(t),t)\), where \(Q(t)=h\). Indeed, neutral fixed points satisfy \(a x(1-y)=b y(1-x)\), whose solution is \(x=X(y)\), and
\[
Q'(t)=1+\frac{ac}{R(t)^2}>0.
\]
On a chord the first-coordinate map \(f_h\) has exact derivative
\[
f_h'(x)=(1-a)(1-y)+(1-b)y-\bigl[(1-x)c+x(ac/b)\bigr],
\qquad y=h-(c/b)x.
\]
Each bracketed convex combination lies strictly between zero and one. Thus throughout every chord
\[
|f_h'(x)|\le q_*:=\max\bigl\{1-\min(a,b),\ c,\ ac/b\bigr\}<1.
\]
The neutral equilibrium first coordinate \(\xi(h)\) is uniformly Lipschitz because \(Q'(t)\ge1\) and \(X'(t)=ab/R(t)^2\) is bounded.

**2. Uniform shadowing on the slow time scale.** Write \(h_n=H(x_n,y_n)\) and \(e_n=x_n-\xi(h_n)\). The first-coordinate formula of \(F_\varepsilon\) does not involve \(d_\varepsilon\); consequently, \(x_{n+1}=f_{h_n}(x_n)\), and the preceding contraction and \(|h_{n+1}-h_n|\le |\varepsilon|/b\) give
\[
|e_n|\le q_*^n|e_0|+C|\varepsilon|.
\]
Since \(y_n=h_n-(c/b)x_n\), the difference from \(\Gamma(h_n)\) is also bounded by \(C(q_*^n+|\varepsilon|)\). In particular, with the globally Lipschitz function \(g(h)=\xi(h)[1-\eta(h)]/b\) and \(\eta(h)=Q^{-1}(h)\),
\[
h_{n+1}=h_n+\varepsilon g(h_n)
+O\bigl(|\varepsilon|q_*^n+\varepsilon^2\bigr).
\]
The error bound is uniform on the full square. For the ODE \(\dot h=\sigma g(h)\), \(h(0)=H_0\), comparison with the Euler scheme and discrete Gronwall, using \(\sum_{n\ge0}q_*^n<\infty\), gives
\[
\max_{0\le n\le T/|\varepsilon|}|h_n-h(n|\varepsilon|)|\le C_T|\varepsilon|.
\]
Interpolation over intervals of length \(|\varepsilon|\) accounts for the floor. Combining with the transverse bound proves both asserted estimates, including the initial-layer exception and its absence when \(e_0=0\).

**3. Explicit integration.** Put \(h=Q(t)\). Since \(\xi(Q(t))=bt/R(t)\),
\[
\frac{dt}{d\tau}=\sigma\frac{t(1-t)R(t)}{R(t)^2+ac}.
\]
Partial fractions give
\[
\frac{R(t)^2+ac}{t(1-t)R(t)}
=\frac{a+c}{t}+\frac{b+ac/b}{1-t}
 -\frac{c(b-a)^2}{bR(t)}=G'(t)>0.
\]
Integration proves the exact inverse-function formula. Both logarithmic divergences imply \(G:(0,1)\to\mathbb R\) is bijective and give the two endpoint exponentials. Finally, at \(\varepsilon=-s<0\), the Jacobian at \((0,0)\) has characteristic polynomial evaluated at one equal to \(s\), with derivative at one tending to \(a+c\); its Perron root is \(1-s/(a+c)+O(s^2)\). For \(\varepsilon=s>0\), the Jacobian at \((1,1)\) analogously has Perron root \(1-s/(b+ac/b)+O(s^2)\). These equal the endpoint rates in slow time. This completes the proof.

## Verification

Run `python verify.py` in the directory containing this document. The checker symbolically verifies the exact drift, derivative and primitive identities, and tests representative positive/negative near-neutral trajectories at three scales. Its finite integrations are corroborative; the global quantifiers and \(O(|\varepsilon|)\) estimates follow from the proof above, not from sampling.

## Relationship to prior work

The four-parameter two-type Volterra operator and its fixed points were introduced and studied previously. Castanos, Jamilov and Rozikov (2018) proved convergence for five subfamilies. Rasulov (2026), **Lemma 8(2)**, already establishes convergence for the two-type discrete restriction across the coefficient regimes, including neutral conserved chords; therefore global convergence and neutral fixed-curve existence are **not** claimed as contributions here. The result proved here is the *quantitative near-neutral double-scaling law* \(n|\varepsilon|=O(1)\), with an explicit full-passage clock \(G\), a uniform \(O(|\varepsilon|)\) error away from the fast initial layer, and exact matching to endpoint spectral rates. Generic fast–slow shadowing theory motivates the method but does not supply this map-specific clock or the quantitative statement without additional calculation.

## Limitations

The proof varies the single heredity coefficient \(d\) around an interior neutral parameter triple. It does not cover simultaneous multi-parameter degeneration, coefficients on the boundary of the parameter cube, a perturbation that vanishes with \(n\) nonuniformly, finite-population randomness, or errors uniform over arbitrarily long slow times. The initial fast layer prevents a state-space estimate at slow time zero unless the initial state is already on the neutral curve. Earlier general slow-fast theory may subsume the qualitative limit mechanism; historical priority of the explicit clock remains provisional. Independent validation has not been performed.

## References

- Rasulov Xaydar Raupovich, “Analytical solutions of one class of Volterra quadratic stochastic operators of a two-sex population with continuous time,” arXiv:2610.06895 (first public September 28, 2026), especially Lemma 8 and Section 6.
- O. Castanos, U. U. Jamilov and U. A. Rozikov, “On Volterra quadratic stochastic operators of a two-sex population on \(S^1\times S^1\),” arXiv:1808.01812 (2018); DOI:10.29229/uzmj.2018-3-4.
- U. A. Rozikov and U. U. Zhamilov, “Volterra quadratic stochastic operators of a two-sex population,” Ukrainian Mathematical Journal (2011), DOI:10.1007/s11253-011-0568-y (abstract consulted; full text not accessed).
- N. N. Ganikhodjaev and U. U. Jamilov, “Contracting Quadratic Operators of Bisexual Population” (2015), concerning sufficient conditions for Banach contraction.
