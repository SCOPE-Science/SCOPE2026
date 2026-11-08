# A sharp completed-step positivity ceiling for fifth-order Radau IIA on finite Markov generators

## Finding
Let \(Q\) be any finite conservative continuous-time Markov-chain generator, meaning \(Q\mathbf 1=0\) and \(Q_{ij}\geq0\) for \(i\ne j\). Set \(\Lambda=\max_i(-Q_{ii})\). For the three-stage, fifth-order Radau IIA completed-step map
\[
\mathcal T_h(Q)=R(hQ),\qquad R(z)=\frac{60+24z+3z^2}{60-36z+9z^2-z^3},
\]
there is an **exact, sharp, dimension-independent positivity ceiling** \(\tau_*=1.703416266987\ldots\): every such map is entrywise nonnegative and row-stochastic whenever \(h\Lambda\leq\tau_*\). Conversely, for every \(t>\tau_*\) there exists a finite pure-birth generator with maximum departure rate one for which \(R(tQ)\) contains a strictly negative entry. Thus the common guarantee over arbitrary finite Markov generators holds exactly on \([0,\tau_*]\). The exceptional case \(\Lambda=0\) gives \(Q=0\) and is safe for every step.

The threshold is algebraic: let \(\rho\) be the unique real root of
\[
p(x)=x^3-9x^2+36x-60,
\]
let \(s=9-\rho\), and set
\[
\boxed{\tau_* =\frac{60/\rho-\rho^2}{3\rho-9}}.
\]
The three-state pure-birth chain \(1\to2\to3\) (the last state absorbing, both rates one) has a striking, **reentrant** completed-step positivity set \([0,\eta_1]\cup[\eta_2,\infty)\), where \(\eta_1=4.808412580708\ldots\) and \(\eta_2=17.728541157989\ldots\) are the two positive roots of
\[
q(t)=t^4-16t^3-48t^2+240t+1200.
\]
In particular, at \(t=5\) its \((1,2)\) transition is \(-105/13924\), whereas the entire matrix is nonnegative again for \(t\geq\eta_2\). This finite-state return does not restore the universal guarantee.

## Assumptions and scope
All matrices are finite and real. Generators may be reducible or directed; no reversibility, sparsity, symmetry, or irreducibility is imposed. The generator convention is \(Q_{ij}\geq0\) off diagonal and rows summing to zero. The step \(h\geq0\) acts on \(u'=Qu\), and \(R(hQ)\) is a matrix rational function using the above exact numerator and denominator. The claim concerns **completed-step, linear, componentwise nonnegativity** and stochasticity, not nonnegative Runge–Kutta internal stages, nonlinear SSP properties, or backward error.

For the sharpness statement a separate finite witness may be selected for each \(t>\tau_*\); the witness dimension is not uniformly bounded as \(t\downarrow\tau_*\). The result does not assert that every generator fails beyond the ceiling.

## Proof
**1. Poles and the exact threshold.** The denominator is \(-p(z)\). Since
\[
p'(x)=3(x-3)^2+9>0,
\]
there is precisely one real pole \(\rho\), and rational evaluations give
\[
3.6378<\rho<3.6379.
\]
The other poles are \(\xi,\overline\xi\), with \(\xi=\alpha+i\beta\), \(\beta>0\),
\[
\alpha=(9-\rho)/2>0,\qquad |\xi|^2=60/\rho,
\qquad \beta^2=60/\rho-(9-\rho)^2/4>0.
\]
The closest pole to the real point \(-t\) is the real pole precisely for \(0\leq t\leq\tau_*\), since
\[
|t+\xi|^2-(t+\rho)^2=60/\rho-\rho^2-(3\rho-9)t.
\]
The real-pole/complex-pole distance equality is the displayed formula for \(\tau_*\).

**2. A rigorous residue margin.** Write \(N(z)=60+24z+3z^2\). Partial fractions are
\[
R(z)=\frac{A_0}{\rho-z}+\frac{A_1}{\xi-z}+\frac{\overline{A_1}}{\overline\xi-z},\qquad A_0=\frac{N(\rho)}{p'(\rho)},\quad A_1=\frac{N(\xi)}{p'(\xi)}.
\]
We have the *strict* inequality \(A_0>2|A_1|\). Here is an exact check that avoids numerical residue comparison. Put \(r=\rho\), \(S=9-r\), \(P=60/r\), and
\[
\begin{aligned}
N_0&=3(r^2+8r+20),&D_0&=3r^2-18r+36,\\
N_c&=9(P^2+8PS+20S^2+24P+160S+400),&
D_c&=(r^2-rS+P)(4P-S^2).
\end{aligned}
\]
The identities \(|N(\xi)|^2=N_c\) and \(|p'(\xi)|^2=D_c\) imply
\[
A_0^2-4|A_1|^2=\frac{N_0^2D_c-4N_cD_0^2}{D_0^2D_c}.
\]
Modulo \(r^3-9r^2+36r-60=0\), the numerator multiplied by \(r^2\) reduces **exactly** to
\[
F(r)=22429872r^2-385471872r+1121843520.
\]
On the rational isolating interval above, \(F\) is decreasing and \(F(3.6379)>0\); every denominator is positive. Hence \(A_0^2>4|A_1|^2\), and \(A_0>0\), establishing the margin. The supplementary verifier reproduces the polynomial congruence and exact rational endpoint inequalities.

**3. Uniform positivity.** For \(k\geq0\), the Taylor coefficient at \(-t\) is
\[
c_k(t):=\frac{R^{(k)}(-t)}{k!}=\frac{A_0}{(t+\rho)^{k+1}}+2\operatorname{Re}\frac{A_1}{(t+\xi)^{k+1}}.
\]
For \(0\leq t\leq\tau_*\), the real pole is no more distant than the complex pair, so
\[
c_k(t)\geq\frac{A_0-2|A_1|}{(t+\rho)^{k+1}}>0
\quad\text{for every integer }k\geq0.
\]
For \(\Lambda>0\), normalize \(\widehat Q=Q/\Lambda\) and set \(P=I+\widehat Q\). The matrix \(P\) is nonnegative and row-stochastic. For \(t=h\Lambda\), the Taylor series converges in the infinity operator norm, because its nearest pole is farther than \(t\) from \(-t\), giving
\[
R(hQ)=R(-tI+tP)=\sum_{k=0}^{\infty}c_k(t)t^kP^k.
\]
The scalar coefficients are positive and sum to \(R(0)=1\). This is a convex combination of stochastic matrices, proving entrywise nonnegativity and row sums one.

**4. Sharpness for every larger timestep.** If \(t>\tau_*\), then \(|t+\xi|<t+\rho\). Write \(\theta=\arg(t+\xi)\in(0,\pi/2)\), \(\phi=\arg A_1\). The coefficient formula becomes a dominant oscillation:
\[
c_k(t)=\frac{2|A_1|}{|t+\xi|^{k+1}}\cos(\phi-(k+1)\theta)+\frac{A_0}{(t+\rho)^{k+1}}.
\]
For irrational \(\theta/(2\pi)\), the phases are dense; for rational \(\theta/(2\pi)\), their nonconstant finite cycle has mean zero and a strictly negative value. In either case infinitely many cosine values are bounded below some negative constant along a subsequence. The real-pole term decays geometrically faster, hence \(c_k(t)<0\) for infinitely many positive integers \(k\).

Fix such a \(k\). In the pure-birth chain of \(k+2\) states, let states \(1,\ldots,k+1\) each jump right at rate one and the last state absorb. Its uniformization matrix \(P=I+Q\) shifts each transient state deterministically. The \((1,k+1)\) entry of \(P^j\) equals one for \(j=k\) and zero otherwise, so
\[
(R(tQ))_{1,k+1}=t^k c_k(t)<0.
\]
This proves sharpness for every \(t>\tau_*\), not merely failure along a sequence of timesteps.

**5. Three-state reentrance.** For the generator
\[
Q_3=\begin{pmatrix}-1&1&0\\0&-1&1\\0&0&0\end{pmatrix},
\]
functional calculus for its Jordan block shows
\[
R(tQ_3)=\begin{pmatrix}
R(-t)&tR'(-t)&1-R(-t)-tR'(-t)\\
0&R(-t)&1-R(-t)\\0&0&1
\end{pmatrix}.
\]
Direct exact differentiation gives
\[
R'(-t)=\frac{3q(t)}{(t^3+9t^2+36t+60)^2},
\]
while the potentially remaining entry is always positive for \(t>0\):
\[
1-R(-t)-tR'(-t)=\frac{t^2(t^4+12t^3+198t^2+960t+1800)}{(t^3+9t^2+36t+60)^2}>0.
\]
Also \(0<R(-t)<1\) for \(t>0\). Descartes' rule allows at most two positive roots of \(q\); signs \(q(0)>0\), \(q(5)<0\), \(q(18)>0\) force exactly two. Thus the full claimed union of closed timestep intervals follows. At \(t=5\) the exact negative entry is \(-105/13924\).

## Verification
Run `python verify.py` after installing the declared dependency in `requirements.txt`. It checks the fifth-order series, cubic pole bracket and monotonicity, positive residue margin by polynomial remainder, exact pole tie, three-state entry identities and rational counterexample, and Taylor coefficients and a pure-birth witness at timestep two. It outputs `VERIFY_OK 22 first_negative_coefficient_at_h2 11 negative_entry -5772440991/3213750657762304`. The infinite-dimensional-uniform quantifiers in the theorem follow from the analytical Taylor-series/oscillatory-pole proof, not from the finite tests.

## Relationship to prior work
The Padé stability map of fifth-order Radau IIA is classical; see Hairer and Wanner (1999). Van de Griend and Kraaijevanger (1986) developed the general absolute-monotonicity theory of rational stability functions. Lóczi and Ketcheson (first available preprint dated March 26, 2013; journal 2014) develop exact radius and pole-dominance methods for families of rational functions, giving the key general conceptual implication between absolute monotonicity and linear positivity; their family (4.1) **contains this very Radau function at parameter \(a=-1/60\)**, and their pole-distance formula (Section 4.2) already implies the bound \(R(\cdot)\leq\tau_*\). That upper bound, and the general matrix-positivity interpretation, are credited as known. Their inspected theorem and proof do not give the equality \(R(\cdot)=\tau_*\) for this fixed parameter, nor its sharp all-timestep pure-birth witnesses or its three-state phase diagram. The present contribution is the exact \([2/3]\) residue-domination argument proving equality with the established pole bound, a sharp Markov-generator statement with explicit all-dimension pure-birth converse for **each** timestep above the threshold, and the three-state reentrant phase diagram. General SSP conclusions do not automatically hold for stages or nonlinear problems. Earlier Padé positivity-smoothing approaches (Wade et al., 2004) address different compositions and nonnegative semidiscrete heat updates.

## Limitations
The result concerns finite conservative generators, uniform departure-rate bounds, the fixed three-stage Radau IIA rational update, and the completed step only. No claim of internal-stage or nonlinear positivity is made. The chain dimensions witnessing arbitrary near-threshold failures can be arbitrarily large; no bound on the first failing dimension is proved. The formula relies on exact algebraic inequalities; published general theory supplies methods that might allow an equivalent specialization not explicitly indexed. The 1986 primary full text could not be inspected through accessible channels; its general contributions are acknowledged without asserting that its entire content was excluded.

## References
- E. Hairer and G. Wanner, *Stiff differential equations solved by Radau methods*, J. Comput. Appl. Math. 111 (1999), 93–111, https://doi.org/10.1016/S0377-0427(99)00134-X.
- J. A. van de Griend and J. F. B. M. Kraaijevanger, *Absolute monotonicity of rational functions occurring in the numerical solution of initial value problems*, Numer. Math. 49 (1986), 413–424, https://geodesic.mathdoc.fr/item/NUMA_1986__49_133121/.
- L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, first public arXiv version March 26, 2013, https://arxiv.org/abs/1303.6651; LMS J. Comput. Math. 17 (2014), 159–205, https://doi.org/10.1112/S1461157013000326.
- I. Higueras, *Strong stability for additive Runge–Kutta methods*, SIAM J. Numer. Anal. 44 (2006), 1735–1758, https://doi.org/10.1137/040612968.
- B. A. Wade et al., *Smoothing with positivity-preserving Padé schemes for parabolic problems with nonsmooth data*, first published September 29, 2004, https://doi.org/10.1002/num.20039.
