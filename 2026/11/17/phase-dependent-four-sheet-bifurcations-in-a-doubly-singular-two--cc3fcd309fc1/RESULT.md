# Phase-dependent four-sheet bifurcations in a doubly singular two-phase implicit recurrence

## Finding
Consider a scalar, periodically non-autonomous implicit recurrence with coefficient period two:
\[
F_0(x_n,x_{n+1};a,b)=x_{n+1}^2+a x_{n+1}-x_n=0,\qquad
F_1(x_n,x_{n+1};a,b)=2x_{n+1}^2+b x_{n+1}-x_n=0.
\]
All states and parameters are real. Starting at phase \(j\), a **two-step successor** of a prescribed initial state \(x\) is a real terminal state \(z\) for which both successive implicit relations hold in order. Distinct terminal states give distinct successors; the intervening state is uniquely determined by \(z\). Let \(N_j\) be the greatest number of distinct real successors over *regular* initial states (targets that are not critical values of the two-step polynomial).

For every \(a,b\in\mathbb R\), the exact classification is
\[
N_0=\begin{cases}4&b^2>4a,\\2&b^2\le4a,\end{cases}\qquad
N_1=\begin{cases}4&a^2>b,\\2&a^2\le b.\end{cases}
\]
When four sheets exist, their complete open target windows are
\[
\begin{aligned}
\mathcal W_0&=\left(-\frac{a^2}{4},-\frac{a^2}{4}+\frac{(b^2-4a)^2}{64}\right), & b^2>4a,\\
\mathcal W_1&=\left(-\frac{b^2}{8},-\frac{b^2}{8}+\frac{(a^2-b)^2}{8}\right), & a^2>b.
\end{aligned}
\]
Every regular target in \(\mathcal W_j\) has exactly four real successors, and no target outside its closure has four. At the caustic equality \(b^2=4a\), respectively \(a^2=b\), the corresponding four-sheet window collapses to a single quartic critical point. The inequalities have no hidden small-parameter restriction.

All four phase-ordered valence pairs \((2,2),(4,2),(2,4),(4,4)\) occur arbitrarily near \((a,b)=(0,0)\). At that simultaneous forward singularity the two-step maps are \(x=4z^4\) and \(x=2z^4\); the inverse near the singular target has the *optimal* local Hölder exponent \(1/4\).

There is also a sharper orbit-based distinction. For \(a=-\varepsilon\), \(b=\varepsilon\) and every \(0<\varepsilon<1/16\), the phase-labelled stationary orbit \(x_{2m}=x_{2m+1}=0\) has exactly four two-step successors from phase zero and exactly two from phase one. At both phases the unique Floquet multiplier of this regular orbit is \(-\varepsilon^{-2}\). Therefore equal cyclic Floquet spectra do not determine global two-step branching, even arbitrarily close to simultaneous failure of forward regularity.

## Assumptions and scope
No positivity constraint is imposed: the state space is the whole real line, parameters \(a,b\) are arbitrary real numbers, and phases are retained as part of the non-autonomous system. A **regular target** is a real number not attained at a real critical point of the relevant two-step polynomial. The maximum \(N_j\) is taken over all such targets, without insisting that the corresponding transition is part of a periodic orbit. The local orbit and its Floquet multiplier are discussed only where the next-state derivatives do not vanish, namely \(ab\ne0\). The phase-labelled two-step state \((0,0)\) is not asserted to have least state-period two; its forcing phase has period two.

## Proof
Put \(h_0(t)=t^2+at\) and \(h_1(t)=2t^2+bt\). The original implicit equations read \(x_n=h_{n\bmod2}(x_{n+1})\). Consequently the two-step inverse-relation polynomials are
\[
H_0(z)=h_0(h_1(z)),\qquad H_1(z)=h_1(h_0(z)).
\]
Their exact completed-square forms are
\[
\begin{aligned}
H_0(z)&=\left[2\left(z+\frac b4\right)^2-\frac{b^2-4a}{8}\right]^2-\frac{a^2}{4},\\
H_1(z)&=2\left[\left(z+\frac a2\right)^2-\frac{a^2-b}{4}\right]^2-\frac{b^2}{8}.
\end{aligned}
\]
For a positive number \(c\), the real quartic \((A u^2-c)^2-d\), with \(A>0\), has two nondegenerate local minima and one central local maximum; exactly four simple inverse images occur for levels strictly between the minimum \(-d\) and maximum \(c^2-d\). If \(c=0\) there is one quartic stationary point and at most two simple real inverse images. If \(c<0\), the quartic is strictly increasing as a function of \(u^2\) and again has at most two simple real inverse images. Applying these observations to each completed-square form proves the two necessary-and-sufficient criteria and the stated window widths. The outer levels have no further four-preimage windows because the quartics are strictly increasing outside their outer minima.

For sufficiently small \(\varepsilon>0\), choosing \((a,b)=(\varepsilon,\varepsilon),(-\varepsilon,\varepsilon),(\varepsilon,-\varepsilon),(-\varepsilon,-\varepsilon)\) gives, respectively, the ordered valence pairs \((2,2),(4,2),(2,4),(4,4)\). At the origin the completed squares simplify to \(H_0(z)=4z^4\), \(H_1(z)=2z^4\). Their positive-target inverse branches are constant multiples of \(x^{1/4}\), which are locally Hölder of exponent \(1/4\) but of no larger exponent at zero.

For the exact phase-specific orbit witness, take \(a=-\varepsilon,b=\varepsilon\). From phase zero, the equation \(H_0(z)=0\) factors as \(h_1(z)(h_1(z)-\varepsilon)=0\), and its four distinct roots are
\[
z=0,\quad z=-\varepsilon/2,\quad
z=\frac{-\varepsilon\pm\sqrt{\varepsilon^2+8\varepsilon}}4.
\]
From phase one, \(H_1(z)=0\) factors as \(h_0(z)(2h_0(z)+\varepsilon)=0\). Its real roots are exactly \(z=0\) and \(z=\varepsilon\), since the other quadratic has discriminant \(\varepsilon^2-2\varepsilon<0\). The intermediate state is \(h_1(z)\) or \(h_0(z)\), respectively, so these root counts equal counts of distinct admissible two-step successor chains.

Along the zero orbit, \(D_1F_0=D_1F_1=-1\), whereas \(D_2F_0=a\), \(D_2F_1=b\). For \(ab\ne0\), the two local forward derivatives are \(1/a\) and \(1/b\), giving the same scalar cyclic multiplier \(M=1/(ab)\) regardless of the starting phase, hence \(M=-\varepsilon^{-2}\) in the witness. Nevertheless the global numbers of successors are different. For completeness, the cyclic orbit equations \(F_0(x_0,x_1)=F_1(x_1,x_0)=0\) have state Jacobian \(\begin{psmallmatrix}-1&a\\ b&-1\end{psmallmatrix}\), whose determinant is \(1-ab\). It is invertible at the double singularity, ensuring that the zero *phase-labelled orbit* stays locally unique even while forward branches coalesce. Finally, each step has quadratic next-state dependence; replacing either step by an affine relation makes the two-step return polynomial of degree at most two, so the four-sheet effect requires two nonlinear steps within this polynomial class.

## Verification
The accompanying `verify.py` checks both completed-square identities as identities in the exact rational polynomial ring \(\mathbb Q[z,a,b]\); it then verifies rational parameter representatives for all four valence regions, the exact four-versus-two witness factorization, the cyclic Jacobian determinant and its multiplier. Run `python3 verify.py` using only the Python standard library. These algebra checks supplement the elementary global root-count proof; sample parameters are not substituted for the universal argument.

## Relationship to prior work
Oliveira (2026, arXiv:2611.03336v1) develops cyclic Lyapunov–Schmidt reduction and cyclic invariance of regular periodic-orbit bifurcation data for implicit systems, assuming nonzero next-state Jacobians at the reference orbit; its motivation explicitly notes nonunique global forward branches. The present result concerns *global two-step inverse-sheet valence in a doubly forward-singular, phase-dependent minimal polynomial family*, not a new regular Lyapunov–Schmidt theorem.

Beardmore and Webster (2008) treat singular difference-algebraic equations via quasi-invariant manifolds and parameter-dependent local normal forms; these do not directly supply the displayed complete two-phase branch-count conditions. Buescu and Oliveira (arXiv:2611.12327v1, publicly posted 2026-11-09) study evolution-fold markers and their interactions with local periodic-orbit bifurcations; their discussion identifies simultaneous singularity of distinct steps as a further problem. That later paper is a comparison only, not the date-defining source of this result. Standard quartic double-well geometry is a classical ingredient, not itself claimed as new.

## Limitations
The classification is exact only for the displayed two-parameter, scalar, two-phase quadratic implicit relation. It counts admissible finite two-step successors, not persistent orbits, attractors, or invariant measures. The four-versus-two example has an unstable regular orbit. No genericity or normal-form universality for arbitrary smooth systems is asserted; conjugacy of global two-step branch structure is not inferred from local multiplier invariance. A wider historical literature on singular difference equations and compositions of quadratics could contain equivalent special cases, and priority needs independent assessment.

## References
1. H. M. Oliveira, “Lyapunov–Schmidt reduction for periodic orbits of implicit discrete dynamical systems,” arXiv:2611.03336v1 (first posted 2026-11-02), https://arxiv.org/abs/2611.03336.
2. R. Beardmore and K. Webster, “Normal forms, quasi-invariant manifolds, and bifurcations of nonlinear difference-algebraic equations,” *SIAM Journal on Mathematical Analysis* **40** (2008), 413–441, https://doi.org/10.1137/050638618.
3. J. Buescu and H. M. Oliveira, “Singular bifurcations in implicit discrete dynamical systems,” arXiv:2611.12327v1 (first posted 2026-11-09; comparison literature), https://arxiv.org/abs/2611.12327.
