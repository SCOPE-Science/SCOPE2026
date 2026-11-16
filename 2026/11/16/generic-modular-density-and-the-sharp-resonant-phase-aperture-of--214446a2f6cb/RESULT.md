# Generic modular density and the sharp resonant phase aperture of an exponential trinomial

## Finding

Let \(\alpha>\beta>0\) with \(\alpha/\beta\notin\mathbb Q\), and let \(a,b\in\mathbb C\setminus\{0\}\). The zeros of
\[
F(z)=1-ae^{\alpha z}-be^{\beta z}
\]
have the following two complementary modular distribution laws.

**Generic periods.** If \(L>0\) and
\[
\frac{2\pi}{L}\notin\mathbb Q\alpha+\mathbb Q\beta,
\]
then, for every nonempty open arc \(J\subset\mathbb R/L\mathbb Z\), the number of *distinct* zeros \(z\) of \(F\) satisfying \(0<\operatorname{Im}z\le T\) and \(\operatorname{Im}z\bmod L\in J\) obeys
\[
\liminf_{T\to\infty}\frac{N_J(T)}T>0.
\]
In particular their imaginary parts are dense modulo \(L\). The excluded periods form a countable subset of \((0,\infty)\); hence the assertion holds for all but countably many \(L\).

**A resonant period.** Write \(q=\beta/\alpha\), \(\kappa=|b|\,|a|^{-q}\), and \(L_0=2\pi/\alpha\). For \(-1\le c\le1\) set
\[
 u_q(c)=\frac{-(2q-1)c+\sqrt{(2q-1)^2c^2+4q(1-q)}}{2(1-q)},
 \qquad H_q(c)=\frac{\sqrt{1+u_q(c)^2-2c\,u_q(c)}}{u_q(c)^q}.
\]
Then the **exact closure** of the residues of all zeros, expressed in the angular coordinate \(\phi=\arg(a)+\alpha\operatorname{Im}z\pmod{2\pi}\), is
\[
\boxed{\mathcal A=\{\phi\pmod{2\pi}:H_q(\cos\phi)\le\kappa\}.}
\]
The function \(H_q\) is continuous and strictly decreasing on \([-1,1]\), with \(H_q(1)=0\) and
\[
H_q(-1)=K_q:=q^{-q}(1-q)^{q-1}.
\]
Thus, when \(0<\kappa<K_q\), the closure is exactly one proper closed arc
\[
\mathcal A=\{\phi:|\operatorname{Arg}(e^{i\phi})|\le\Theta_q(\kappa)\},
\qquad \Theta_q(\kappa)=\arccos\bigl(H_q^{-1}(\kappa)\bigr)\in(0,\pi).
\]
For \(\kappa\ge K_q\), the closure is the entire circle. Every open arc meeting the *interior* of \(\mathcal A\) contains residues of a positive lower linear density of distinct zeros, measured as above with period \(L_0\). As \(\kappa\uparrow K_q\) from below, the missing angular half-width satisfies the sharp square-root law
\[
\boxed{\pi-\Theta_q(\kappa)=\sqrt{\frac{2(K_q-\kappa)}{K_q q(1-q)}}\,(1+o(1)).}
\]
The offset \(\arg(a)\) is essential: the displayed symmetric arc is in the coordinate \(\arg(a)+\alpha\operatorname{Im}z\), not necessarily centered at zero in the raw height coordinate.

## Assumptions and scope

The parameters \(\alpha,\beta\) are positive real frequencies in the strict order \(\alpha>\beta\), with irrational ratio. Both complex coefficients are nonzero. Zeros are counted without multiplicity; repeated zeros cause no exception. Every modular residue is taken on the corresponding quotient circle, and statements about closures are topological closures, not assertions that each boundary residue is attained by an exact zero. No rational independence with the additional constant \(1\) is assumed. In the generic part, \(L\) can be any positive length outside the stated countable set, while the resonant part concerns the specific natural period \(2\pi/\alpha\). The exponent normalization of \(F\) is obtained from a general three-term sum by dividing by its nonzero constant term and shifting all exponents by their smallest exponent.

## Proof

**1. A zero-transfer lemma.** Consider any model function
\[
G(w)=1-Ue^{\alpha w}-Ve^{\beta w},\qquad U,V\in\mathbb C\setminus\{0\},\quad U+V=1.
\]
It is not identically zero and has an isolated zero at \(w=0\). Select an arbitrarily small disk \(D=\{|w|<r\}\) with no zeros on its boundary. If \((a e^{\alpha x+i\alpha t},b e^{\beta x+i\beta t})\) is sufficiently close to \((U,V)\), then
\[
F(x+it+w)=1-ae^{\alpha x+i\alpha t}e^{\alpha w}-be^{\beta x+i\beta t}e^{\beta w}
\]
is uniformly close to \(G(w)\) on \(\partial D\), and Rouché's theorem gives a zero of \(F\) in \(x+it+D\). This remains valid for a multiple model zero: only nonvanishing on \(\partial D\) is required. By taking \(r\) as small as desired, the imaginary coordinate of the transferred zero can be made arbitrarily close to \(t\).

The basic phase-approximation fact used below is Kronecker--Weyl equidistribution. For any positive \(h\) outside a countable exceptional set, the numbers \(1,h\alpha/(2\pi),h\beta/(2\pi)\) are rationally independent. Consequently the discrete orbit \(n\mapsto(e^{i\alpha nh},e^{i\beta nh})\) visits every open rectangle of the two-torus with a strictly positive limiting frequency. If \(2\pi/L\notin\mathbb Q\alpha+\mathbb Q\beta\), choose \(h\) additionally so that \(1,h\alpha/(2\pi),h\beta/(2\pi),h/L\) are rationally independent; then the same positive-frequency statement holds in the three-torus, with the last coordinate \(nh\bmod L\). In either case \(h\) can be arbitrarily large, so disks around distinct translates are disjoint.

**2. Torus-model zeros and existence of zeros of \(F\).** Put \(u=|a|e^{\alpha x}\). Then \(|b|e^{\beta x}=\kappa u^q\). For chosen phases \(\phi,\eta\), the model equation at \(w=0\) is
\[
1=u e^{i\phi}+\kappa u^q e^{i\eta}.
\]
For a prescribed \(\phi\), such a model exists if and only if some \(u>0\) satisfies
\[
\frac{|1-u e^{i\phi}|}{u^q}=\kappa.\tag{1}
\]
For \(\phi=0\), the continuous left side tends to \(+\infty\) at both ends \(u\downarrow0\) and \(u\uparrow\infty\), and vanishes at \(u=1\). Thus equation (1) has a solution for every \(\kappa>0\), and we may choose \(\eta\) accordingly. The irrationality of \(\alpha/\beta\), two-torus equidistribution and the zero-transfer lemma then supply actual zeros of \(F\), indeed infinitely many distinct ones. This avoids an appeal to a general entire-function factorization theorem.

**3. Generic modular density and a lower linear count.** Fix any existing zero \(z_0\) of \(F\) and an arbitrary nonempty open target arc \(J\subset\mathbb R/L\mathbb Z\). Choose \(r>0\) so that \(z_0\) is the only zero in the disk \(D(z_0,r)\), its boundary is zero-free, and \(2r\) is smaller than the length of a closed subarc strictly inside \(J\). Choose \(h>2r\) satisfying the three-torus independence condition from Step 1. There is a nonempty product of open phase neighborhoods in which the first two coordinates of \(nh\) make \(F(z+i nh)\) uniformly close to \(F(z)\) on \(\partial D(z_0,r)\), while the third coordinate forces \((\operatorname{Im}z_0+nh-r,\operatorname{Im}z_0+nh+r)\bmod L\subset J\). Kronecker--Weyl supplies a positive proportion \(\delta>0\) of integers \(n\ge1\) in that product set. Rouché gives a zero in every corresponding disk \(D(z_0+i nh,r)\), and these disks are pairwise disjoint. For all large \(T\), at least \(\delta T/(2h)\) such disks lie in \(0<\operatorname{Im}z\le T\). Hence \(\liminf N_J(T)/T\ge\delta/(2h)>0\). The rational span \(\mathbb Q\alpha+\mathbb Q\beta\) is countable, proving the co-countable assertion.

**4. Exact resonant closure.** If \(z=x+iy\) is an actual zero, then with \(u=|a|e^{\alpha x}\) and \(\phi=\arg(a)+\alpha y\) we have \(1=u e^{i\phi}+\kappa u^q e^{i\eta}\) for some \(\eta\). Thus equation (1) holds, which forces
\[
H_q(\cos\phi):=\min_{u>0}\frac{\sqrt{1+u^2-2u\cos\phi}}{u^q}\le\kappa.
\]
This closed inequality contains the phase of every actual zero and therefore its closure.

Conversely, if \(H_q(\cos\phi)\le\kappa\), the function \(u\mapsto|1-u e^{i\phi}|/u^q\) is continuous, tends to infinity at both endpoints of \((0,\infty)\), and attains every value not smaller than its minimum. Choose \(u>0\) satisfying (1), put \(x=\alpha^{-1}\log(u/|a|)\), and choose \(\eta\) so that the model equation holds. Density of the two-frequency torus orbit provides \(t_n\to+\infty\) with \(\arg(a)+\alpha t_n\to\phi\) and \(\arg(b)+\beta t_n\to\eta\) modulo \(2\pi\). The zero-transfer lemma gives actual zeros near \(x+i t_n\), with \(\arg(a)+\alpha\operatorname{Im}z_n\to\phi\). Hence every phase satisfying the inequality belongs to the closure, including its boundary.

For a nonempty open arc meeting the interior of this closure, choose a target interior phase and an associated model equation as above. Take a sufficiently small zero-isolating disk so transferred zeros remain in the target arc. Use an \(h\) with the two-frequency discrete orbit equidistributed, select a product of open phase neighborhoods of the model phases, and apply Rouché on disjoint disks of spacing \(h\). The same counting argument as Step 3 gives positive lower linear density of distinct zeros in that arc.

**5. Exact aperture and edge asymptotics.** For \(c\in[-1,1]\), minimize the square of the ratio in Step 4, namely
\[
R_q(u,c)^2=(1+u^2-2cu)u^{-2q}.
\]
Its derivative has the sign of
\[
(1-q)u^2+(2q-1)cu-q.
\]
Because \(0<q<1\), this quadratic has exactly one positive root, the stated \(u_q(c)\), and the squared ratio diverges as \(u\downarrow0\) or \(u\uparrow\infty\). Thus \(u_q(c)\) is the unique global minimizer, yielding the formula for \(H_q\). For any \(u>0\), the ratio strictly decreases with \(c\), so comparison at the minimizing \(u\) shows that \(H_q\) is strictly decreasing. At \(c=1\), choosing \(u=1\) gives \(H_q(1)=0\). At \(c=-1\), minimizing \((1+u)u^{-q}\) gives \(u=q/(1-q)\) and \(H_q(-1)=K_q\). The proper-arc/full-circle dichotomy follows.

The envelope derivative at \(c=-1\) is
\[
H_q'(-1)=-\frac{[q/(1-q)]^{1-q}}{1+q/(1-q)}=-K_q q(1-q).
\]
The implicit minimizer is analytic near \(c=-1\), so
\[
H_q(c)=K_q-K_q q(1-q)(c+1)+O_q((c+1)^2).
\]
Writing \(\Theta_q(\kappa)=\pi-\delta\) yields \(\cos\Theta=-1+\delta^2/2+O(\delta^4)\) and, on setting \(H_q(\cos\Theta)=\kappa\), the asserted square-root asymptotic.

## Verification

The standalone file `CHECK.py` runs finite diagnostics for the closed-form positive stationary root, strict sampled decrease of \(H_q\), endpoint values, inequality against test trial points, the near-edge square-root ratio, and the exact coalescent model at rational test values. Run `python3 CHECK.py`; the saved package reported `CHECK_OK q_samples=6 stationary_grid=1542 tangency_samples=4 asymptotic_sweeps=18`. These tests are not proofs for all real parameters. In particular, the infinitely many zeros and the positive-density assertions rely on the analytic Rouché and Kronecker--Weyl arguments in the preceding proof, not finite computation.

## Relationship to prior work

Podesta's April 15, 2026 paper [1] specifically poses density of imaginary zero heights modulo a period as an open question for rationally independent exponential frequencies. It analyzes an auxiliary phase function and states that the modular-density solution is left for another publication. The geometric feasibility condition from its Proposition 1 is closely related to the minimization in Step 5; no novelty is asserted for that underlying geometric possibility test. The distinct additional conclusions here concern **actual zero residues**: co-countably many full-density periods with positive linear visiting frequency, versus an exact sharp arc at a resonant period, including boundary approach and the square-root transition. Podesta's February 2026 article [2] studies density of **real** projections, not modular imaginary projections. Moreno's original main theorem [3], and the related projection results [4], [5], describe real or linear projections of zeros; those projection theorems do not directly give this circular-modular closure. The survey [6] gives broad vertical-strip and zero-counting theory, but does not state the paired generic-period and resonant-period conclusion.

## Limitations

The theorem is specific to three nonzero exponential terms with real frequencies and irrational positive ratio. It does not assert equidistribution of individual zero heights with respect to uniform angular measure, nor an explicit optimal positive density constant. The exact closure may include boundary phases not attained by a zero. The result is a self-review, not an independent audit or a historical priority guarantee. The original source's phase-feasibility propositions may yield some of the aperture formula after a nontrivial parameter elimination, and uncatalogued older almost-periodic divisor results may cover parts of the modular conclusion; no stronger historical novelty claim is made.

## References

1. J. J. Podesta, “A Function Used to Locate the Zeros of an Exponential Sum,” *Monatshefte für Mathematik* 210 (2026), 223–268, first public 15 April 2026, https://doi.org/10.1007/s00605-026-02174-6 .
2. J. J. Podesta, “When Do Zeros of an Exponential Sum have Real Parts that Form a Dense Set?,” *American Mathematical Monthly* (online 27 February 2026), https://doi.org/10.1080/00029890.2026.2624366 .
3. C. J. Moreno, “The zeros of exponential polynomials (I),” *Compositio Mathematica* 26 (1973), 69–78, https://www.numdam.org/item/CM_1973__26_1_69_0/ .
4. A. Mas and J. M. Sepulcre, “The projections of the zeros of exponential polynomials with complex frequencies,” *Colloquium Mathematicum* 158 (2019), 91–102, https://doi.org/10.4064/cm7412-5-2018 .
5. J. M. Sepulcre and T. Vidal, “On the non-isolation of the real projections of the zeros of exponential polynomials,” *Journal of Mathematical Analysis and Applications* 437 (2016), 513–525, https://doi.org/10.1016/j.jmaa.2016.01.014 .
6. J. Heittokangas, K. Ishizaki, K. Tohge and Z.-T. Wen, “Value distribution of exponential polynomials and their role in the theories of complex differential equations and oscillation theory,” *Bulletin of the London Mathematical Society* 55 (2023), 1–77, https://doi.org/10.1112/blms.12719 .
