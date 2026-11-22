# Two nested reversal-count fluctuation thresholds for finite-interval run-and-tumble escape

## Finding

For a one-dimensional run-and-tumble particle launched to the right, the conditional **number of velocity reversals before exiting an absorbing interval** has two distinct, strictly ordered spatial thresholds. Write \(s=x/L\in(0,1)\) for the starting fraction of the interval and \(\ell=\lambda L/v>0\) for the reversal rate measured per ballistic crossing time. Set \(N\) equal to the number of reversals strictly before first exit, and write \(R\) and \(B\) for exiting at \(L\) (right) and \(0\) (left), respectively. Define

\[
\Delta_m(s,\ell)=\mathbb E[N\mid B]-\mathbb E[N\mid R],\qquad
\Delta_V(s,\ell)=\operatorname{Var}(N\mid B)-\operatorname{Var}(N\mid R).
\]

Both differences are strictly increasing in \(s\). For every \(\ell>0\), \(\Delta_V\) has exactly one zero \(s_V(\ell)\in(0,1)\), with \(\Delta_V<0\) below and \(\Delta_V>0\) above that zero. Meanwhile \(\Delta_m>0\) for every interior \(s\) when \(0<\ell\le\sqrt3\). When \(\ell>\sqrt3\), \(\Delta_m\) has exactly one zero \(s_m(\ell)\), and the thresholds are **strictly nested**:

\[
0<s_m(\ell)<s_V(\ell)<1.
\]

Thus conditional reversal-count variances can reverse their ordering even at rates for which the conditional reversal-count means never do. For \(\ell>\sqrt3\) a nonempty interval of starting positions has \(\mathbb E[N\mid B]>\mathbb E[N\mid R]\) yet \(\operatorname{Var}(N\mid B)<\operatorname{Var}(N\mid R)\).

There is also a sharp high-reversal boundary layer:

\[
\begin{aligned}
s_m(\ell)&=\frac12-\frac1{2\ell}-\frac2{\ell^3}+O(\ell^{-4}),\\
s_V(\ell)&=\frac12-\frac1{2\ell}+\frac{10}{\ell^3}+O(\ell^{-4}),\\
s_V(\ell)-s_m(\ell)&=\frac{12}{\ell^3}+O(\ell^{-4}).
\end{aligned}
\]

At weak reversals, the variance threshold has the nontrivial limit \(s_V(\ell)\to 1/(1+\sqrt3)\) as \(\ell\downarrow0\).

## Assumptions and scope

Fix \(L,v,\lambda>0\). The particle moves on \((0,L)\) with velocity \(+v\) or \(-v\), independently reversing velocity at the jump times of a homogeneous Poisson process of rate \(\lambda\), with no translational Brownian noise. It starts at \(0<x<L\) with velocity \(+v\). The first arrival at either endpoint terminates the path immediately; endpoints do not hold or reflect the particle. The elapsed stopping time and reversal count are almost surely finite, and both exit-side probabilities are positive. Counts exclude any event after absorption. The rate \(\lambda\) is the actual rate of sign flips, not the twice-as-large relaxation-rate convention sometimes used for a telegraph equation.

For compactness let \(q=\ell s\) and \(h=\ell(1-s)\), so \(q+h=\ell\). The exact differences are

\[
\boxed{\Delta_m=1+\frac13\left(\frac{q^2(q+3)}{q+1}-h^2\right)}
\]

and

\[
\boxed{\Delta_V=\frac2{45}\left[\frac{q^4(q^2+6q+15)}{(q+1)^2}-h^4+15\left(\frac{q^2(q+3)}{q+1}-h^2\right)\right].}
\]

For the **entire marked count law**, define \(F_R(z)=\mathbb E[z^N\mathbf1_R]\) and \(F_B(z)=\mathbb E[z^N\mathbf1_B]\), initially for real \(0\le z\le1\). Put \(w=\sqrt{1-z^2}\) and interpret removable singularities at \(w=0\) by continuity. Then

\[
\boxed{F_R(z)=\frac{\cosh(qw)+\sinh(qw)/w}{\cosh(\ell w)+\sinh(\ell w)/w},\quad
F_B(z)=\frac{z\sinh(hw)/w}{\cosh(\ell w)+\sinh(\ell w)/w}.}
\]

In particular \(\Pr(R)=(1+q)/(1+\ell)\) and \(\Pr(B)=h/(1+\ell)\), and conditional counts are even on \(R\) and odd on \(B\).

## Proof

**Absorption and analytic moments.** From either interior position and either velocity, the particle reaches the boundary currently ahead within \(L/v\) unless it reverses first. The chance of no reversal throughout that passage is at least \(e^{-\ell}>0\). Applying the strong Markov property after successive reversals therefore bounds the number of reversals before absorption by a geometric tail. This guarantees finite moments of every order, justifies derivatives of the PGFs at \(z=1\), and excludes spurious nonabsorbing boundary solutions.

**Backward transfer problem.** For an exit-mark generating function, let \(f_+(x,z)\) and \(f_-(x,z)\) be its values at current velocities \(+v\) and \(-v\). First-step analysis yields

\[
v\partial_x f_++\lambda(zf_--f_+)=0,\qquad
-v\partial_x f_-+\lambda(zf_+-f_-)=0.
\]

Thus \(\partial_x(f_+,f_-)^{\mathsf T}=M(f_+,f_-)^{\mathsf T}\), where

\[
M=\frac\lambda v\begin{pmatrix}1&-z\\z&-1\end{pmatrix},\qquad
M^2=\left(\frac\lambda v\right)^2(1-z^2)I.
\]

The physically correct outgoing boundary data for \(F_R\) are \(f_-(0,z)=0\) and \(f_+(L,z)=1\); those for \(F_B\) are \(f_-(0,z)=1\) and \(f_+(L,z)=0\). Propagating with

\[
e^{Mx}=I\cosh\left(\frac{\lambda x}{v}w\right)+\frac{M}{(\lambda/v)w}\sinh\left(\frac{\lambda x}{v}w\right)
\]

and evaluating the initial \(+v\) component gives exactly the two boxed generating functions. The boundary-value problem is unique because every trajectory absorbs almost surely.

**Moments.** Set \(y=1-z^2\). The denominator and the two numerators are expanded using

\[
\cosh(a\sqrt y)+\frac{\sinh(a\sqrt y)}{\sqrt y}
=1+a+\left(\frac{a^2}{2}+\frac{a^3}{6}\right)y
+\left(\frac{a^4}{24}+\frac{a^5}{120}\right)y^2+O(y^3),
\]

\[
\frac{\sinh(a\sqrt y)}{\sqrt y}=a+\frac{a^3}{6}y+\frac{a^5}{120}y^2+O(y^3).
\]

Since \(y=-2(z-1)-(z-1)^2\), differentiating the normalized PGFs \(F_R(z)/F_R(1)\) and \(F_B(z)/F_B(1)\) gives

\[
\begin{aligned}
\mathbb E[N\mid R]&=\frac{\ell^2}{3}\left(\frac{\ell+3}{\ell+1}-\frac{s^2(\ell s+3)}{1+\ell s}\right),\\
\mathbb E[N\mid B]&=1+\frac{\ell^2}{3}\left(\frac{\ell+3}{\ell+1}-(1-s)^2\right).
\end{aligned}
\]

For either side \(E\), the conditional variance is \(G_E''(1)+G_E'(1)-G_E'(1)^2\), where \(G_E(z)=F_E(z)/F_E(1)\). Subtracting the two conditional variances and simplifying the rational expressions gives the boxed formula for \(\Delta_V\); the second-order series identity is also verified exactly by the supplied script.

**Exactly one crossing and its sharp onset.** Introduce the two increasing functions of \(q>0\),

\[
A(q)=\frac{q^2(q+3)}{q+1},\qquad
B(q)=\frac{q^4(q^2+6q+15)}{(q+1)^2}.
\]

Both are strictly increasing by the explicit positive derivatives

\[
A'(q)=\frac{2q(q^2+3q+3)}{(q+1)^2}>0,\qquad
B'(q)=\frac{4q^3(q^3+6q^2+15q+15)}{(q+1)^3}>0.
\] Since \(q=\ell s\) strictly increases and \(h=\ell(1-s)\) strictly decreases with \(s\), the expressions \(\Delta_m=1+(A(q)-h^2)/3\) and \(\Delta_V=2(B(q)-h^4+15(A(q)-h^2))/45\) are strictly increasing. Their boundary limits are

\[
\begin{aligned}
\Delta_m(0+,\ell)&=1-\ell^2/3,&\Delta_m(1-,\ell)&=1+A(\ell)/3>0,\\
\Delta_V(0+,\ell)&=-2(\ell^4+15\ell^2)/45<0,&\Delta_V(1-,\ell)&=2(B(\ell)+15A(\ell))/45>0.
\end{aligned}
\]

Continuity and strict monotonicity now prove the existence, uniqueness, signs and \(\sqrt3\) onset described in the finding.

**Strict nesting.** At any mean-crossing position, the equality \(\Delta_m=0\) says \(h^2=A(q)+3\). Substituting this into the variance difference gives the exact, strictly negative expression

\[
\left.\Delta_V\right|_{\Delta_m=0}
=-\frac{4(4q^3+12q^2+18q+9)}{15(q+1)^2}<0.
\]

Because \(\Delta_V\) strictly increases and ends positive, its unique zero lies strictly to the right of the unique mean zero.

**Limit laws for the two thresholds.** At small \(\ell\), expanding the variance difference yields \(\Delta_V=(2\ell^2/3)(3s^2-(1-s)^2)+O(\ell^3)\) uniformly on \([0,1]\). Its unique positive root tends to \(1/(1+\sqrt3)\). At large \(\ell\), substitute \(s=1/2-1/(2\ell)+c/\ell^3\) into each difference. The mean difference has leading term \((2c+4)/(3\ell)\); the variance difference has leading term \((2c/45-4/9)\ell\). Their unique zeros therefore have \(c=-2\) and \(c=10\), respectively. Standard smooth implicit expansions of the explicit rational equations, with positive derivatives near these zeros, control the stated \(O(\ell^{-4})\) errors.

## Verification

Run \(`python check.py`\) in an environment with Python, SymPy, NumPy and SciPy installed. The standalone script recomputes both conditional moment differences from the power series, checks their exact symbolic agreement with the claimed rational functions, certifies positive derivative numerators and the nesting substitution, checks both large-rate asymptotics, independently evaluates the two-sided boundary transfer matrix at multiple parameter points, and solves the two threshold equations numerically. A successful local run reported 250 transfer-matrix and root checks in addition to the exact symbolic identities. This finite diagnostic set does not constitute proof over continuous parameters; the preceding algebra and monotonicity argument do.

For \(\ell=3\), the two roots are approximately \(s_m=0.288675134595\) and \(s_V=0.415547505294\). The script uses outgoing-velocity rather than both-velocity Dirichlet boundary conditions, avoiding an overdetermined telegraph boundary-value problem.

## Relationship to prior work

Guéneau and Touzo [1] examine splitting probabilities, hard-wall/absorbing duality and time-dependent exit probabilities for a one-dimensional run-and-tumble particle. Angelani [2] develops generic boundary escape conditions and mean first-exit times. Park, Singh and Fai [3] calculate exit-side probabilities and conditional mean **elapsed time** in a related telegraph representation. Cinque [4,5] derives telegraph distributions conditioned on fixed-time reversal counts and the one-sided first-passage maximum, rather than the reversal count accumulated up to two-sided absorption. Marchione and Orsingher [6] derive the correct outgoing-direction Dirichlet exit problem and unmarked splitting and mean first-exit times for the same interval telegraph dynamics; their results coincide with the specialization of the present equations at \(z=1\), but do not supply the marked-count threshold classification.

Those sources provide important transfer and first-passage context but the inspected statements do not give the paired conditional reversal-count **variance and mean ordering phase diagram**, the distinct sharp onset \(\sqrt3\), their strict spatial nesting, or the cubic-scale separation. Exact one-point first-passage results can in principle yield count transforms by a rate-changing identity; mere nonappearance of identical expressions does not rule out an implicit derivation. Literature beyond the examined sources could contain a stronger general theorem. The status is self-reviewed, not independently validated or priority-certified.

## Limitations

The theorem requires a uniform Poisson reversal rate, symmetric speeds of equal magnitude, a specified initial rightward orientation, and immediately absorbing endpoints. It is not a claim about first-passage **time** variance, spatially dependent reversal rates, sticky/reactive walls, or a freely randomized initial velocity. It proves conditional marked-count laws and their crossings, not novel formulas for classical unmarked exit probabilities. The independent scientific audit and exhaustive publication-priority comparison remain open.

## References

[1] M. Guéneau and L. Touzo, *Relating absorbing and hard wall boundary conditions for a one-dimensional run-and-tumble particle* (first arXiv posting 2023-12-20), https://arxiv.org/abs/2312.13200 .

[2] L. Angelani, *One-dimensional run-and-tumble motions with generic boundary conditions*, Journal of Physics A **56** (2023) 455003, https://doi.org/10.1088/1751-8121/ad009e ; open full text: https://iris.cnr.it/retrieve/e1d78abe-8685-4eff-936b-9bcad8ad4c0f/prod_489129-doc_203607.pdf .

[3] S. Park, P. Singh and T. Fai, *Coarse-grained Stochastic Model of Myosin-Driven Vesicles into Dendritic Spines* (2022), https://pmc.ncbi.nlm.nih.gov/articles/PMC9603279/ .

[4] F. Cinque, *The Negative Reflection Principle and the Joint Distribution of the Telegraph Process and its Maximum* (2020 first preprint; 2022 revised PDF), https://arxiv.org/abs/2011.00342 .

[5] F. Cinque, *A Note on the Conditional Probabilities of the Telegraph Process* (2022), https://arxiv.org/abs/2202.01904 .

[6] M. M. Marchione and E. Orsingher, *Dirichlet problems and exit distributions for the telegraph process and its planar extensions* (first arXiv posting 2026-05-06), https://arxiv.org/abs/2605.05430 .
