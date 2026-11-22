# Cubic proliferation and asymptotically universal repulsion of antipodal two-cycles in a quadratic memristor sine map

## Finding
Consider the real planar map
\[
F_{a,b}(x,q)=\left(a\sin\big(\pi x(1+b-bq^2)\big),\ q+x\right),\qquad a,b>0.
\]
Let \(N_b(a)\) count its distinct primitive period-two orbits of the antipodal form \(\{(x,q),(-x,-q)\}\). Let \(R_b(a)\) count those among them whose two-step derivative has both eigenvalues of modulus strictly larger than one. Then, for every fixed \(b>0\),
\[
\boxed{N_b(a)=\frac b4a^3-(1+b)a+O_b(1)\quad (a\to\infty),}
\]
and
\[
\boxed{\lim_{a\to\infty}\frac{R_b(a)}{N_b(a)}=1.}
\]
Here \(O_b(1)\) means a quantity bounded independently of \(a\) once \(b\) is fixed. Every counted orbit is a genuine primitive period-two orbit; the theorem does not assert that every period-two orbit is antipodal or that these orbits are attracting.

## Assumptions and scope
The state space is the full real plane \(\mathbb R^2\), not a circle quotient or a finite-precision grid. The two real parameters satisfy \(a>0\) and \(b>0\); the limit is taken with \(b\) fixed. The first coordinate is a sine with angular frequency \(\pi\), and the memory state accumulates the *current* first coordinate as \(q\mapsto q+x\). The map is the quadratic-charge specialization of the sine internal-perturbation construction with \(M(q)=q^2-1\); all assertions concern this explicitly written recurrence. A periodic orbit is counted once as a two-point set. For a repelling two-cycle, both eigenvalues of \(D(F_{a,b}^{\circ2})\) at either cycle point must have modulus greater than one.

## Proof
**1. Exact symmetry reduction.** Let \(S(x,q)=(-x,-q)\). Since \(1+b-bq^2\) is even in \(q\) and sine is odd, \(F_{a,b}S=SF_{a,b}\). Therefore a nontrivial antipodal two-cycle is equivalent to a nonzero solution of \(F_{a,b}(x,q)=(-x,-q)\). Its second coordinate forces \(q=-x/2\). The first coordinate then becomes
\[
\sin\Phi_b(x)=-\frac xa,\qquad
\Phi_b(x)=\pi\left((1+b)x-\frac b4x^3\right).
\]
The sine bound gives \(|x|\le a\). Sign symmetry pairs the roots \(x\) and \(-x\), so **each root** in \(0<x\le a\) gives **exactly one** distinct primitive antipodal two-cycle, with points \((x,-x/2)\) and \((-x,x/2)\). The root \(x=0\) is excluded: it lies on the equilibrium line.

**2. Exact congruence representation.** Define \(\alpha_a(x)=\arcsin(x/a)\) for \(0\le x\le a\). The sine equation is equivalent to either
\[
\Phi_b(x)+\alpha_a(x)\in2\pi\mathbb Z
\quad\text{or}\quad
\Phi_b(x)-\alpha_a(x)\in\pi+2\pi\mathbb Z.
\]
For \(0<x<a\) the two families do not overlap. At \(x=a\) they can coincide, contributing at most one duplicate to a count; the first family includes the spurious root \(x=0\).

**3. Bounded-error counting.** Fix a constant \(L>\max\{1,\sqrt{4(1+b)/(3b)}\}\), depending only on \(b\). Since \(\Phi_b\) is a fixed cubic and \(\alpha_a\in[0,\pi/2]\), both congruence families have \(O_b(1)\) roots on \([0,L]\) as \(a\to\infty\): for sufficiently large \(a\), both \(\Phi_b+\alpha_a\) and \(\Phi_b-\alpha_a\) are strictly concave on \((0,L]\), and their ranges on this fixed interval stay bounded. (Indeed their second derivatives are respectively \(-3\pi bx/2+x/(a^2-x^2)^{3/2}\) and \(-3\pi bx/2-x/(a^2-x^2)^{3/2}\).)

On \([L,a)\), \(\Phi'_b(x)=\pi((1+b)-3bx^2/4)<0\). Hence \(\Phi_b-\alpha_a\) is strictly decreasing. The other phase \(\Phi_b+\alpha_a\) has derivative
\[
\Phi'_b(x)+\alpha'_a(x)
=\frac{1-h_a(x)}{\sqrt{a^2-x^2}},\quad
h_a(x)=\pi\left(\frac{3b}{4}x^2-(1+b)\right)\sqrt{a^2-x^2}.
\]
For large \(a\), \(h_a(L)>1\), \(h_a(a)=0\), and the derivative of \(h_a\) has the sign of
\[
x\left(\frac{3b}{2}a^2-\frac{9b}{4}x^2+(1+b)\right).
\]
This expression changes sign at most once; therefore \(h_a\) initially increases and ultimately decreases to zero, crossing level \(1\) only once on \([L,a)\). Thus \(\Phi_b+\alpha_a\) decreases and then rises on a terminal segment. Since \(\Phi_b\) is decreasing, its terminal rise is at most \(\alpha_a(a)-\alpha_a(x_*)\le\pi/2\), so this last segment contributes at most one further congruence root.

On their decreasing segments, counting levels spaced by \(2\pi\) introduces an error bounded independently of \(a\). Also the corrections \(\alpha_a\) shift phase endpoints by at most \(\pi/2\). Each congruence family therefore contributes
\[
\frac{\Phi_b(L)-\Phi_b(a)}{2\pi}+O_b(1)
=-\frac{\Phi_b(a)}{2\pi}+O_b(1).
\]
Removing \(x=0\) and any duplicate at \(x=a\) changes the count by at most two. Summing the two families gives
\[
N_b(a)=-\frac{\Phi_b(a)}\pi+O_b(1)
=\frac b4a^3-(1+b)a+O_b(1).
\]
In particular, \(N_b(a)\) is finite for each finite \(a>0\), and grows without bound.

**4. Repulsion for almost all symmetric cycles.** Fix \(0<c<1\) and increase \(L\), if necessary, until \(d(x)>c_0(x)>0\) for all \(x\ge L\), where
\[
c_0(x)=\frac b4x^2-(1+b),\qquad
d(x)=\frac{5b}{4}x^2-(1+b).
\]
On the compactly truncated range \(L\le x\le ca\), the sine equation implies
\[
|\cos\Phi_b(x)|=\sqrt{1-x^2/a^2}\ge\sqrt{1-c^2}.
\]
At the cycle point \((x,-x/2)\), the one-step Jacobian is
\[
J=\begin{pmatrix}
M((1+b)-bx^2/4)&M bx^2\\
1&1
\end{pmatrix},\quad M=a\pi\cos\Phi_b(x).
\]
At the antipodal point the Jacobian is the same, so the period-two derivative is \(J^2\). Set \(s=M c_0(x)\) and \(\gamma=d(x)/c_0(x)>1\). The characteristic polynomial of \(J\) is exactly
\[
P(\lambda)=\lambda^2-(1-s)\lambda-\gamma s.
\]
Uniformly for \(L\le x\le ca\), \(|s|\ge a\pi c_0(L)\sqrt{1-c^2}\to\infty\). If \(s>0\), \(P(1)=(1-\gamma)s<0\) and \(P(-1)=2-(1+\gamma)s<0\) for sufficiently large \(a\); one real eigenvalue exceeds \(1\) and the other is below \(-1\). If \(s<0\), put \(u=-s\). Then the trace is \(1+u>2\), the determinant is \(\gamma u>1\), and \(P(1)=(\gamma-1)u>0\); the eigenvalues are either a complex conjugate pair of modulus \(\sqrt{\gamma u}>1\), or two positive real roots both greater than \(1\). In either case \(J^2\) has both eigenvalues of modulus greater than one. Thus every antipodal two-cycle with \(L\le x\le ca\) is hyperbolically repelling once \(a\) is large enough.

Finally, the same level-counting argument on \([L,ca]\) (where both phases are eventually strictly decreasing) gives
\[
\#\{\text{antipodal two-cycles with }L\le x\le ca\}
=\frac b4c^3a^3+O_{b,c}(a).
\]
Dividing by \(N_b(a)=ba^3/4+O_b(a)\) shows \(\liminf_{a\to\infty} R_b(a)/N_b(a)\ge c^3\). Since this holds for every \(c<1\), and \(R_b(a)\le N_b(a)\), the limit equals one. \(\square\)

## Verification
The supplied `CHECKER.py` independently evaluates the symmetry reduction, the phase crossing counts on monotone branches for representative gains and couplings, and the Jacobian sign tests. These finite computations corroborate the algebra but are not used as an infinite proof. The mathematical proof above directly establishes the entire fixed-coupling limit and both eigenvalue moduli for all sufficiently large gains. Numerical root samplers can miss closely spaced roots near \(x=a\), so the reproducible checker counts congruence crossings rather than sampling the sine residual on a uniform grid.

## Relationship to prior work
The quadratic memristance \(M(q)=q^2-1\) and sine internal-perturbation formula come from Yihyis, He, Tang and Wang (2023). Their paper examines phase portraits, Lyapunov exponents and bifurcation plots for several memristive perturbations; the exact antipodal periodic-orbit census and hyperbolic-repulsion density are distinct from those numerical descriptors. Yi, Wang and Sun (2026) study a different modular-bias-sine update, so their bounded-modulus recurrence does not imply the statements for this unwrapped cubic-charge sine map. The antecedent sine-series internal-perturbation framework of Dong and collaborators (2021) is acknowledged; a complete original full-text comparison of that antecedent was unavailable. Ordinary sine-level crossing arguments are standard: the contribution is the precise cubic-minus-linear law and the asymptotic repulsion classification for this explicitly specified two-dimensional memory map.

## Limitations
The count covers **only** antipodal primitive period-two orbits, not all possible two-cycles. It does not bound the number of cycles of higher periods, prove topological chaos, or establish an invariant probability or cryptographic security. The asymptotic is for fixed positive \(b\), not a joint limit with \(b\to0\), and gives no optimal finite-gain threshold. Most counted large-gain cycles are repelling, not observable attractors. The originating article's embedded Table 1 was not independently available as machine-readable text; this statement is for the explicit recurrence above, including its stated charge update. Publication priority remains subject to independent literature verification.

## References
1. W. A. Yihyis, S. He, Z. Tang, H. Wang, *A Class of Discrete Memristor Chaotic Maps Based on the Internal Perturbation*, **Symmetry** 15 (2023), 1574, published 12 August 2023. https://doi.org/10.3390/sym15081574
2. S. Yi, H. Wang, K. Sun, *A modular-bias-sin chaotification method for enhanced discrete memristor chaotic maps*, **Chinese Physics B** 35 (2026), 070504. https://doi.org/10.1088/1674-1056/ae181e
3. C. Dong et al., *Chaotification of Sine-series maps based on the internal perturbation model*, **Results in Physics** 31 (2021), 105010. https://doi.org/10.1016/j.rinp.2021.105010
