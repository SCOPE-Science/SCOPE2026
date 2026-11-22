# A second-order inverse-sheet signature across eight sine-memristor maps

## Finding

Consider the eight real planar maps listed below, introduced as single- and multiple-perturbation sine maps by Yihyis, He, Tang, and Wang [1]. Write every map as
\[
F_j(x,q)=\bigl(a\sin H_j(x,q),\ q+x\bigr),\qquad j=1,\ldots,8,
\]
where \(a>0\), \(\omega>0\), \(b>0\), and the sinusoidal-memristance offset \(c\in\mathbb R\) is fixed. Define
\[
Q(q)=q^2-1,\quad A(q)=|q|-1,\quad S(q)=\sin(\pi q)+c,
\quad E(q)=e^{-\cos(\pi q)}-1.
\]
The eight phase functions, with parentheses reproduced literally from Tables 1 and 2 of [1], are
\[
\begin{aligned}
H_1&=\omega x(1-bQ(q)),&H_2&=\omega x(1-bA(q)),\\
H_3&=\omega x(1-bS(q)),&H_4&=\omega x(1-bE(q)),\\
H_5&=\omega x(1-bQ(q)-bA(q)),&
H_6&=\omega\bigl(x-bE(q)-bxA(q)\bigr),\\
H_7&=\omega x(1-bQ(q)-bE(q)),&
H_8&=\omega x(1-bQ(q)-bE(q)-bA(q)).
\end{aligned}
\]
**Important scope detail:** In the displayed Model 6 of Table 2, the exponential term is \(-bE(q)\), *without* an accompanying factor \(x\); the theorem uses that displayed formula. The general multi-perturbation template elsewhere in [1] uses a different placement, which is not substituted here.

For each target \((u,v)\in\mathbb R^2\) and cutoff \(R>0\), count *distinct* one-step inverse states in the natural bounded-current window:
\[
N_j(R;u,v)=\#\{(x,q)\in\mathbb R^2:\ |x|\le R,\ F_j(x,q)=(u,v)\}.
\]
Define \(\kappa(u)=1\) for \(|u|<a\) and \(\kappa(u)=1/2\) for \(|u|=a\). **Theorem.** For every fixed admissible choice of parameters and target \(|u|\le a\), as \(R\to\infty\),
\[
\boxed{\begin{aligned}
N_1&=\frac{2\kappa\omega b}{\pi}R^3+O(R),\\
N_2&=\frac{2\kappa\omega b}{\pi}R^2+O(R),\\
N_3&=\frac{2\kappa\omega b}{\pi}R^2+O(R),\\
N_4&=\frac{\kappa\omega b(e-e^{-1})}{\pi}R^2+O(R),\\
N_5&=\frac{2\kappa\omega b}{\pi}R^3+\frac{2\kappa\omega b}{\pi}R^2+O(R),\\
N_6&=\frac{2\kappa\omega b}{\pi}R^2+O(R),\\
N_7&=\frac{2\kappa\omega b}{\pi}R^3+O(R),\\
N_8&=\frac{2\kappa\omega b}{\pi}R^3+\frac{2\kappa\omega b}{\pi}R^2+O(R).
\end{aligned}}
\]
All errors may depend on the fixed parameters and target; they are not claimed to be uniform as \(b\to0\). If \(|u|>a\), all eight counts vanish identically. In contrast, at \(b=0\), all eight maps have the common linear law
\[
N_j(R;u,v)=\frac{2\kappa(u)\omega}{\pi}R+O(1),\qquad |u|\le a.
\]
Every target in \([-a,a]\times\mathbb R\) has countably infinitely many full-plane preimages for every fixed \(b\ge0\). For \(|u|<a\), infinitely many of its preimages are regular (the two-dimensional Jacobian is nonsingular). For \(|u|=a\), every preimage is critical.

The **new distinguishing effect** is the positive \(R^2\) correction in Models 5 and 8: within the cubic-growth family, it occurs exactly when absolute-charge memory accompanies quadratic-charge memory. The exponential addition in Model 7 produces no \(R^2\) term. Among the quadratic-growth single-memristor models, the absolute and sinusoidal choices have exactly equal leading coefficients, while the exponential choice has the larger coefficient by the factor \((e-e^{-1})/2>1\). The Model 1 cubic law is included as a baseline; a separate earlier calculation already derives its sharper two-term count [2].

## Assumptions and scope

All states and targets are real, without a positivity restriction or imposed absorbing domain. The cutoff measures the absolute current-like coordinate \(x\); once the target's second coordinate \(v=q+x\) is fixed, this is also an equivalent bounded window on initial charge \(q\). Neither a finite orbit simulation nor cryptographic security is involved. Each \(O(\cdot)\) refers to fixed \(a,\omega,b,c,u,v\), with \(b>0\) except in the separately stated zero-coupling law. The square-root and nonsmooth singularities sometimes associated with numerical implementations are not added to the displayed maps.

A regular inverse state is one where \(\det DF_j(x,q)\ne0\); for the two maps containing \(|q|\), the usual Jacobian is considered only away from the kink \(q=0\). Kink states are counted as inverse states, but not called regular.

## Proof

**1. Reduction and an elementary level-counting lemma.** Fix the observed output \((u,v)\). The second equation forces \(q=v-x\), so the inverse problem becomes
\[
\sin h_j(x)=u/a,\qquad h_j(x)=H_j(x,v-x),\quad |x|\le R.
\]
The phase set solving \(\sin t=u/a\) has asymptotic point density \(\kappa(u)/\pi\): two interlaced arithmetic progressions of spacing \(2\pi\) when \(|u|<a\), and one such progression at an extremum. On each interval where a continuous phase \(h\) is strictly monotone, the count of these levels is
\[
\frac{\kappa(u)}{\pi}|h(\text{right})-h(\text{left})|+O(1).
\]
If \(K_h(R)\) is the number of monotonicity intervals of \(h\) on \([-R,R]\), joining the intervals and removing any double-counting at their common endpoints gives
\[
\boxed{N_j(R;u,v)=\frac{\kappa(u)}{\pi}\operatorname{Var}_{[-R,R]}(h_j)+O(K_{h_j}(R)).}\tag{1}
\]
Here \(\operatorname{Var}\) is the ordinary one-dimensional total variation. The estimate remains true at phase extrema, where inverse roots are counted once rather than with multiplicity.

**2. The four phases involving quadratic memory.** Put \(m(q)=Q(q)+\eta_A A(q)+\eta_E E(q)\), where \((\eta_A,\eta_E)\in\{(0,0),(1,0),(0,1),(1,1)\}\) corresponds to Models 1, 5, 7, and 8. With \(q=v-x\), the phase is
\[
h(x)=\omega x[1-bm(v-x)]
=\omega\bigl[-bx^3+2bvx^2+O(|x|)\bigr]
 -\omega b\eta_A x|v-x|.
\]
The \(O(|x|)\) term includes bounded periodic exponential memory. Its derivative grows at most linearly, while the derivative of the cubic term has leading part \(-3\omega bx^2\). Therefore the phase is strictly decreasing on both sufficiently distant tails. It has only finitely many turning or kink points in the remaining compact interval (each smooth piece is analytic), hence \(K_h(R)=O(1)\) and
\[
\operatorname{Var}_{[-R,R]}(h)=h(-R)-h(R)+O(1).
\]
For \(R>|v|\), the identity
\[
(-R)|v+R|-(R)|v-R|=-2R^2
\]
shows that adding \(A\) contributes **exactly** \(2\omega bR^2\) to \(h(-R)-h(R)\). Meanwhile the quadratic-charge part contributes \(2\omega bR^3+O(R)\): its target-dependent \(x^2\) term is even and cancels between endpoints. Bounded periodic exponential terms contribute at most \(O(R)\). Thus
\[
\operatorname{Var}_{[-R,R]}(h)
=2\omega bR^3+2\omega b\eta_A R^2+O(R),
\]
and (1) yields precisely the four cubic laws. In particular the \(R^2\) coefficient is independent of \(v\), \(c\), and exponential memory.

**3. Absolute-charge memory and the literal mixed Model 6.** For Model 2,
\[
h_2(x)=\omega x(1+b-b|v-x|).
\]
For Model 6,
\[
h_6(x)=h_2(x)-\omega bE(v-x).
\]
The last term is bounded with bounded derivative. On both tails, the derivative of \(h_2\) equals \(-2\omega b|x|+O(1)\), so both phases eventually decrease strictly, and have \(K_h(R)=O(1)\). Their endpoint phase differences equal \(2\omega bR^2+O(R)\). Applying (1) gives the Model 2 and 6 laws. The bounded additive exponential perturbation in the displayed Model 6 cannot change the quadratic leading count.

**4. Periodic sinusoidal and exponential memory.** Take \(M=S\) or \(M=E\), and put \(q=v-x\). Direct differentiation gives
\[
h'(x)=\omega\bigl[1-bM(q)+bxM'(q)\bigr].
\]
As \(M\) and \(M'\) are bounded, the inequality \(\bigl||X+Y|-|Y|\bigr|\le|X|\) yields
\[
\operatorname{Var}_{[-R,R]}(h)
=\omega b\int_{-R}^R|x|\,|M'(v-x)|\,dx+O(R).
\]
The absolute derivative \(|M'|\) is periodic with period \(2\) and a bounded zero-mean primitive after subtracting its mean \(\mu_M\). Integration by parts separately on the two half-intervals gives
\[
\int_{-R}^R|x|\,|M'(v-x)|\,dx
=\mu_M R^2+O(R).
\]
For sinusoidal memory,
\[
\mu_S=\frac12\int_0^2\pi|\cos(\pi q)|\,dq=2.
\]
For exponential memory, using monotonicity between consecutive integer arguments,
\[
\mu_E=\frac12\int_0^2\pi e^{-\cos(\pi q)}|\sin(\pi q)|\,dq=e-e^{-1}.
\]
It remains to control the error in (1). Both periodic derivatives \(M'\) have only finitely many **simple** zeros per period. Away from small fixed neighborhoods of these zeros, the term \(bxM'(v-x)\) controls the sign of \(h'\) on distant tails. Within each such neighborhood, differentiating \(h'\) gives
\[
h''(x)=\omega b\bigl(2M'(v-x)-xM''(v-x)\bigr),
\]
whose sign is fixed for sufficiently large \(|x|\) since \(M''\) has fixed nonzero sign there. Each neighborhood therefore contains at most one zero of \(h'\), and there are \(O(R)\) such neighborhoods in \([-R,R]\). The bounded center contains finitely many zeros by analyticity. Thus \(K_h(R)=O(R)\), and (1) gives exactly the Model 3 and Model 4 laws.

**5. Zero coupling, image, and regularity.** At \(b=0\), every phase is \(\omega x\), and its sine-level lattice gives the common linear formula with \(O(1)\) error. For \(b>0\), every positive leading coefficient above implies infinitely many distinct inverse states for every target \(|u|\le a\); the range of the first coordinate cannot extend beyond \([-a,a]\), so the exact image is \([-a,a]\times\mathbb R\). For each fixed target, the zero sets are discrete on every compact input interval (on the two analytic sides of the possible absolute-value kink), and hence the infinite fibers are countable.

For \(|u|<a\), differentiating \(F_j\) and taking its determinant along \(q=v-x\) gives, away from kink points,
\[
\det DF_j(x,v-x)=a\cos(h_j(x))\,h'_j(x).
\]
At interior inverse levels the cosine factor is nonzero; singular inverse states therefore lie among the \(O(R)\) phase-critical points, while the total count grows at least quadratically. Infinitely many inverses are consequently regular. At \(|u|=a\), the cosine vanishes at every inverse, so all smooth inverse states are singular; nonsmooth kink states are not regular by definition. This completes the theorem.

## Verification

The companion `verify.py` differentiates all eight displayed phase formulas numerically against centered differences at nonsingular test points; verifies the exact periodic mean-variation constants by integration; and directly counts phase-level crossings after splitting into numerical monotonicity intervals for four growing windows. It tests the new positive quadratic correction by comparing Models 5 with 1 and 8 with 7. On execution with Python, SciPy, and the standard library, it prints `VERIFY_OK`. All infinite-count and remainder bounds are proved above; the numerical tests are diagnostics only, and no root-search mesh is invoked as an exhaustion argument.

## Relationship to prior work

The source study [1] introduces and compares the eight maps using chaotic attractor diagrams, bifurcation plots, Lyapunov exponents, and a pseudo-random sequence generator. Its complete sections on single and mixed perturbations and Tables 1–2 supply the exact formulas but do not analyze inverse fibers, finite-window predecessor counts, or the second-order distinction between mixed-memory architectures. A separate existing calculation [2] gives a sharper two-term inverse count and a small-coupling crossover for Model 1 alone; that isolated cubic case is **background**, not the new contribution. The new result determines the remaining seven architectures simultaneously and exposes the \(R^2\) mixed-model invariant.

Classical noninvertible-map theory [3] provides the vocabulary of inverse-image multiplicity and critical curves; the total-variation level-counting principle is elementary. A related quantitative inverse-valence result [4] counts predecessors of a **different** cosine-flux Chialvo map in a positive quadrant, with linear rather than quadratic or cubic growth. Another result [5] finds bounded finite multiplicity for a coupled polynomial Gumowski–Mira network. Neither system has the phase functions or absolute-charge mixed-memory term in this theorem. This is an explicitly model-specific extension, not a claim that counting crossings by variation is itself new.

## Limitations

The theorem studies **one-step real inverse-image geometry**, not forward entropy, attractor basins, unpredictable orbits, cryptographic resistance, or finite-precision security. Large-memory predecessors may be far from experimentally bounded states. The results are asymptotic for fixed positive \(b\), not uniform as \(b\to0\), and do not quantify all lower-order terms. The printed Model 6 equation is treated literally, not silently changed to match a different general template. Historical priority outside the inspected source and indexed literature remains open to independent review.

## References

1. W. A. Yihyis, S. He, Z. Tang, and H. Wang, *A Class of Discrete Memristor Chaotic Maps Based on the Internal Perturbation*, **Symmetry** 15 (2023), 1574, first public 2023-08-12, https://doi.org/10.3390/sym15081574 ; full open text: https://www.mdpi.com/2073-8994/15/8/1574 .
2. *Universal inverse-sheet crossover and two-term branch law in a quadratic-memristor sine map*, earlier model-specific calculation; exact Model 1 theorem is acknowledged as established background, rather than reasserted as a new priority claim.
3. C. Mira, *Noninvertible maps*, **Scholarpedia** 2(9):2328 (2007), https://doi.org/10.4249/scholarpedia.2328 (general background).
4. *Singular zero-to-infinite inverse-valence transition in a cosine-flux Chialvo map*, quantitative related-map result, available at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-singular-zero-to-infinite-inverse-valence-transition-in-a-cosine--8b96b0ec53ba .
5. *Exact inverse-sheet and observation-window transitions in coupled Gumowski–Mira rings*, quantitative related-map result, available at https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-inverse-sheet-and-observation-window-transitions-in-couple--370a893f822a .
