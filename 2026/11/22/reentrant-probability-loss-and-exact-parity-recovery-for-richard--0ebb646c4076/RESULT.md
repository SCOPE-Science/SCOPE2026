# Reentrant probability loss and exact parity recovery for Richardson-extrapolated backward Euler on two-state chains

## Finding
Consider the active second-order Richardson extrapolation of backward Euler,
\[
T_h=2(I-\tfrac12hQ)^{-2}-(I-hQ)^{-1},
\]
for an irreducible two-state continuous-time Markov generator
\[
Q=\begin{pmatrix}-a&a\\ b&-b\end{pmatrix},\qquad a,b>0.
\]
Put \(s=a+b\), \(m=\min(a,b)/s\), \(z=sh\), \(z_0=2+2\sqrt2\), and
\[
r(z)=\frac{2}{(1+z/2)^2}-\frac1{1+z}.
\]
Let \(z_*\) be the unique positive root of \(z^3-10z^2-20z-8=0\), and set \(c=-r(z_*)>0\). Numerically \(z_*=11.7587236921259\ldots\), \(c=0.0361173373065\ldots\). For every integer \(n\ge1\), the following is a complete entrywise-positivity and embeddability classification of the fixed-step propagator \(T_h^n\):

1. Every even \(n\) gives a nonnegative, row-stochastic \(T_h^n\) for every \(h>0\) and every \(a,b>0\). For odd \(n\), write
   \[
   m_n=\frac{c^n}{1+c^n}.
   \]
   If \(m\ge m_n\), all steps are nonnegative; at equality, exactly \(z=z_*\) has a zero diagonal. If \(0<m<m_n\), there are exactly two step parameters \(z_{n,-}<z_*<z_{n,+}\), uniquely determined by
   \[
   r(z_{n,\pm})=-\left(\frac{m}{1-m}\right)^{1/n},
   \]
   and \(T_h^n\) is entrywise nonnegative **if and only if** \(z\notin(z_{n,-},z_{n,+})\). The lower endpoint exceeds \(z_0\); in the open excluded interval exactly the diagonal corresponding to minority stationary mass is negative.
2. The one-step threshold is \(m_1=0.0348583466429\ldots\), equivalently a larger-to-smaller transition-rate ratio of \(1/c=27.6875338709\ldots\). For \(m=m_1-\delta\), the two forbidden interval endpoints satisfy
   \[
   z_{1,\pm}=z_*\pm (1+c)\sqrt{\frac{2}{r''(z_*)}}\,\sqrt\delta+O(\delta),\qquad\delta\downarrow0,
   \]
   with positive leading coefficient \(75.5167836541\ldots\). More generally, the coefficient for odd \(n\) is
   \[
   K_n=\sqrt{\frac{2c^{1-n}(1+c^n)^2}{n\,r''(z_*)}}.
   \]
3. When \(z<z_0\), every power \(T_h^n\) is the time-one transition matrix of a finite-rate two-state Markov generator. At \(z=z_0\), every positive power is singular and hence not so embeddable. For \(z>z_0\), every odd power has negative determinant and is not embeddable, **even if it is entrywise nonnegative**; every even power is embeddable. Thus a single non-Markov one-step matrix can have a perfectly Markov and embeddable two-step propagator.

All statements refer to the active (not passive) extrapolation, with identical \(h\) and \(Q\) at each repeat.

## Assumptions and scope
The process has exactly two states, fixed positive transition rates \(a,b\), row-vector probability convention \(p'(t)=p(t)Q\), and a fixed positive timestep \(h\). The numerical update is multiplication by \(T_h\) on the right, so its entries must be nonnegative to preserve every initial probability vector. No external projection, clipping, or renormalization is applied. \(n\) is any positive integer, not a continuous interpolation parameter. A matrix is Markov-embeddable here if it equals \(e^G\) for some finite real two-state continuous-time Markov generator \(G\); equivalently an interval-scaled generator is permitted. The \(h\to0\) endpoint is the identity but is outside the strict positive-step classification.

## Proof
Define the stationary rank-one projection
\[
\Pi=\frac1s\begin{pmatrix}b&a\\ b&a\end{pmatrix}.
\]
Then \(Q=-s(I-\Pi)\), \(\Pi^2=\Pi\), and \(\Pi(I-\Pi)=0\). Resolvents therefore obey
\[
(I-hQ)^{-1}=\Pi+\frac{I-\Pi}{1+z},\qquad
(I-\tfrac12hQ)^{-2}=\Pi+\frac{I-\Pi}{(1+z/2)^2},
\]
so, exactly and without approximation,
\[
T_h=\Pi+r(z)(I-\Pi),\qquad T_h^n=\Pi+r(z)^n(I-\Pi).
\]
Its off-diagonal entries are \((1-r(z)^n)\pi_j\), with \(\pi=(b/s,a/s)\), and its diagonal entries are \(\pi_i+(1-\pi_i)r(z)^n\). In particular \(T_h^n\) is nonnegative exactly when
\[
-\frac{m}{1-m}\le r(z)^n\le1.
\]
(The upper bound also follows from \(|r(z)|<1\) for \(z>0\).) To establish that bound directly, note that \(r(z)>-1/(1+z)>-1\), while the derivative analysis below gives \(r(z)<1\) for \(z>0\).

After simplification,
\[
r(z)=-\frac{z^2-4z-4}{(z+1)(z+2)^2},\qquad
r'(z)=\frac{z^3-10z^2-20z-8}{(z+1)^2(z+2)^3}.
\]
The numerator of \(r'\) has one sign change, one positive real zero by Descartes' rule and the intermediate value theorem, and changes from negative to positive there. Hence \(r\) decreases strictly from \(r(0)=1\) to its unique negative minimum \(-c\) at \(z_*\), then increases strictly to \(0\) from below. Its only positive zero is \(z_0=2+2\sqrt2\). Thus \(-c\le r(z)<1\), and \(0<c<1\).

If \(n\) is even, \(0\le r(z)^n<1\), proving stochasticity for every rate ratio and step. For odd \(n\), \(r(z)^n\) is negative exactly when \(z>z_0\), and its global minimum is \(-c^n\). Comparing with the diagonal criterion gives the threshold \(m_n=c^n/(1+c^n)\). Below threshold the horizontal level \(-[m/(1-m)]^{1/n}\) intersects the strictly decreasing and then strictly increasing portions of \(r\) exactly once each. This proves both unique endpoints, the exact forbidden interval, and the absence of any further intervals. At the threshold the two roots coalesce at \(z_*\).

Because \(r''(z_*)>0\), Taylor's theorem gives
\[
r(z)=-c+\tfrac12r''(z_*)(z-z_*)^2+O(|z-z_*|^3).
\]
For fixed odd \(n\), the endpoint level as \(m=m_n-\delta\) is
\[
-\left(\frac{m}{1-m}\right)^{1/n}=-c+\frac{c^{1-n}(1+c^n)^2}{n}\delta+O(\delta^2).
\]
Equating and solving on the two monotone branches yields \(z_{n,\pm}=z_*\pm K_n\sqrt\delta+O(\delta)\), including the stated \(n=1\) coefficient. Positivity of \(r''(z_*)\) follows from the strict derivative sign crossing, or directly from \(r''(z_*)=F'(z_*)/[(z_*+1)^2(z_*+2)^3]>0\) for \(F(z)=z^3-10z^2-20z-8\) (its unique positive root is a simple root).

Finally, \(\det T_h^n=r(z)^n\). A real matrix exponential always has strictly positive determinant, so singular and negative-determinant cases are not embeddable. For \(0<r(z)^n<1\), set \(\gamma=-\log(r(z)^n)>0\), giving
\[
T_h^n=\exp\bigl[-\gamma(I-\Pi)\bigr].
\]
Since \(-\gamma(I-\Pi)\) has nonnegative off-diagonal entries and zero row sums, it is a legitimate finite-rate Markov generator. This also shows why even powers recover continuous-time embeddability away from the unique singular step.

For a rational counterexample, choose \((a,b)=(99,1)\), \(h=3/25\), so \(z=12\), \(r(12)=-23/637\), and the first diagonal of \(T_h\) equals \(-82/3185\). Every entry of \(T_h^2\) is nevertheless nonnegative. With balanced rates \(a=b=1\) and \(z=12\), \(T_h\) is nonnegative but its negative determinant excludes embeddability.

## Verification
Run `python3 verify.py` (standard library only) from the containing directory. The verifier independently constructs the two resolvents by exact rational \(2\times2\) inversion rather than reusing the closed-form matrix, checks 3,360 rational power identities and row sums, and tests even-power nonnegativity and the odd-power criterion. It separately brackets the cubic minimum, root crossings, signed regions and the square-root cusp. The direct rational counterexample can be checked from the displayed fractions. The 3,360 finite cases support the proof but are not claimed to prove the universal statement.

## Relationship to prior work
Zlatev, Dimov, Faragó and Havasi [1, Chapter 4, equations (4.14) and (4.18)] give active Richardson extrapolation for the \(\theta\)-method and its scalar stability function; the backward Euler case used here is their \(\theta=1\) specialization. Their analysis concerns scalar A-/L-stability and not stochastic-matrix positivity. Baake and Sumner [2, Sections 1–2] give the general equal-input matrix algebra and nonnegativity criterion, which subsume the elementary projection reduction used in this proof. Their results are acknowledged as algebraic background, not a claim of novelty. The more recent version [3] describes further equal-input Markov-flow structure, likewise not the specific extrapolated scheme, its sharp minimum, or its iteration-parity windows. Bayleyegn, Faragó and Havasi [4] study consistency and convergence of classical extrapolation with explicit one-step methods, not entrywise Markov preservation. Quezada de Luna and Ketcheson [7, Sections 5–7.1] use implicit-Euler extrapolation in flux-limited maximum-principle schemes and explicitly distinguish the positivity of internal stages from that of the uncorrected completed update. Their algorithm requires a limiter for guaranteed positivity, so it does not give an unconditional classification of the unmodified two-state extrapolation step. The distinct available mathematical results on extrapolation and stochasticity for longer chains [5–6] establish different graph-dependent phase boundaries; they do not state or imply the present rate-imbalance classification for an irreducible two-state generator without an additional, nontrivial global scalar extremization and power analysis.

The point of the present theorem is the **complete sharp combination**: one-step rate-imbalance threshold, precisely one forbidden step window, square-root endpoint law, exact parity recovery, and embeddability distinction. Generic equal-input formulas and the scalar stability function are existing tools, not original subclaims.

## Limitations
This theorem only concerns two states, time-homogeneous generators, repeated equal-size active extrapolation steps, and the property of preserving every initial probability vector. It says nothing about a nonautonomous generator, higher-dimensional state spaces, passive Richardson extrapolation, variable-step composition, weak error, or preservation of stochastic ordering. When an even power is stochastic, one-step intermediate states obtained from a nonpositive \(T_h\) can still be negative: the recovery statement concerns only the completed block. The embeddability assertion is for exact finite-rate two-state generators; it does not rule out an approximation by singular limits at \(z=z_0\). The originality comparison does not establish exhaustive historical priority; published work not inspected in full may contain an equivalent special case. The proof is analytic, with finite computational tests used only as supplemental checks.

## References
[1] Z. Zlatev, I. Dimov, I. Faragó and Á. Havasi, *Richardson Extrapolation: Practical Aspects and Applications*, De Gruyter (published 7 November 2017), Chapter 4, DOI: 10.1515/9783110533002. Author manuscript: https://real.mtak.hu/72180/1/Practical_Aspects_of_the_Richardson_Extrapolation_final_submitted_u.pdf

[2] M. Baake and J. Sumner, *On equal-input and monotone Markov matrices*, first public preprint 22 July 2020, arXiv:2007.11433; *Advances in Applied Probability* 54 (2022), 460–492, DOI: 10.1017/apr.2021.39.

[3] M. Baake and J. Sumner, *On the algebra of equal-input matrices in time-inhomogeneous Markov flows*, first public preprint 17 April 2024, arXiv:2404.11222; *Documenta Mathematica* 30 (2025), 455–474, DOI: 10.4171/DM/997. Lawful open full text: https://content.ems.press/assets/public/full-texts/serials/dm/30/2/14298671/online/10.4171-dm-997.pdf

[4] T. Bayleyegn, I. Faragó and Á. Havasi, *On the Consistency and Convergence of Classical Richardson Extrapolation as Applied to Explicit One-Step Methods*, *Mathematical Modelling and Analysis* 28 (2023), 42–52, DOI: 10.3846/mma.2023.16283. Open full text: https://journals.vilniustech.lt/index.php/MMA/article/download/16283/11455

[5] *Richardson acceleration creates a sharp positivity barrier for backward Euler* (2026), research record 2026/10/4/SCOPE-richardson-acceleration-creates-a-sharp-positivity-barrier-for-b--c9c2b9f6d7e1. The scalar nonnegativity cutoff is prior knowledge.

[6] *Re-entrant positivity of Richardson-extrapolated backward Euler on five-state pure-birth chains* (2026), research record 2026/10/13/SCOPE-re-entrant-positivity-of-richardson-extrapolated-backward-euler--c08f9b38b493. The five-state absorbing-chain phenomenon is prior knowledge.

[7] M. Quezada de Luna and D. I. Ketcheson, *Maximum principle preserving space and time flux limiting for diagonally implicit Runge–Kutta discretizations of scalar convection–diffusion equations*, first public preprint 17 September 2021, arXiv:2109.08272, Sections 5–7.1. Lawful full text: https://arxiv.org/html/2109.08272v1
