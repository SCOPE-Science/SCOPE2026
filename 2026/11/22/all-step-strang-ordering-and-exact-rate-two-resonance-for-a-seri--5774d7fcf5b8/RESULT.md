# All-step Strang ordering and exact rate-two resonance for a serial Markov reaction chain

## Finding

Consider the irreversible chain \(0\xrightarrow{a}1\xrightarrow{b}2\), with positive rates \(a,b\). One exact Strang step of duration \(h>0\) uses the half-step/full-step/half-step composition of the individual transition semigroups. Denote by \(S_A(h)\) the composition with transition \(0\to1\) on the outside and by \(S_B(h)\) the opposite composition. Then, in worst-initial-state total variation from the exact semigroup \(P(h)\),

\[
\sup_{p\in\Delta_2}\operatorname{TV}(pS_A(h),pP(h))
<\sup_{p\in\Delta_2}\operatorname{TV}(pS_B(h),pP(h))
\quad\Longleftrightarrow\quad a>b.
\]

For \(a=b\), the two errors coincide. Thus the transition with the *larger rate* belongs in the two outer half-steps, for every positive step size; the slower transition belongs in the middle. The preferred composition is exact, for **every** \(h\ge0\) and **every** initial probability distribution, exactly at the strict rate ratio \(\max(a,b)/\min(a,b)=2\). Specifically, \(S_A(h)=P(h)\) for every \(h\) if and only if \(a=2b\), and \(S_B(h)=P(h)\) for every \(h\) if and only if \(b=2a\). In fact, for any fixed positive \(h\), the same rate conditions characterize exactness.

A stronger sign classification holds at *every* positive step: the terminal-state error of \(S_A\) has the sign of \(a-2b\), and that of \(S_B\) has the sign of \(b-2a\). The arithmetic mean of their terminal-state probabilities is always strictly smaller than the true one.

## Assumptions and scope

Let \(A\) and \(B\) be the row-conservative continuous-time Markov generators

\[
A=\begin{pmatrix}-a&a&0\\0&0&0\\0&0&0\end{pmatrix},\qquad
B=\begin{pmatrix}0&0&0\\0&-b&b\\0&0&0\end{pmatrix},\qquad a,b>0.
\]

For row probability vectors and every \(h\ge0\), define

\[
P(h)=e^{h(A+B)},\quad
S_A(h)=e^{hA/2}e^{hB}e^{hA/2},\quad
S_B(h)=e^{hB/2}e^{hA}e^{hB/2}.
\]

The probability simplex \(\Delta_2\) comprises all triples of nonnegative numbers summing to one. Total variation of two probability rows is half their \(\ell^1\) distance. There is one *single* Strang step; no claim about arbitrary multi-step adaptive schedules or general reaction graphs is implied. All operators preserve nonnegativity and total mass.

## Proof

**Reduction to the terminal probability.** Start at state \(0\). The exact probability of reaching state \(2\) by time \(h\) is the CDF of two independent exponential waiting times \(X\sim\operatorname{Exp}(a)\), \(Y\sim\operatorname{Exp}(b)\):

\[
T=\Pr(X+Y\le h)
=\begin{cases}
1-e^{-ah}-\dfrac{a(e^{-ah}-e^{-bh})}{b-a},&a\ne b,\\
1-(1+ah)e^{-ah},&a=b.
\end{cases}
\]

The two split compositions give

\[
T_A=(1-e^{-ah/2})(1-e^{-bh}),\qquad
T_B=(1-e^{-ah})(1-e^{-bh/2}).
\]

For either approximation and the exact flow, the state-\(0\) survival probability is \(e^{-ah}\). Therefore the initial-state-\(0\) row differences have the form \((0,-d,d)\), where \(d=T_A-T\) or \(d=T_B-T\). Starting from states \(1\) or \(2\) gives identical exact and split rows. Thus, for every initial distribution \(p=(p_0,p_1,p_2)\),

\[
\operatorname{TV}(pS_A,pP)=p_0|T_A-T|,\qquad
\operatorname{TV}(pS_B,pP)=p_0|T_B-T|.
\]

**Universal midpoint inequality.** In fact, for any independent nonnegative waiting times with strictly decreasing positive densities \(f,g\), their CDFs \(F,G\) satisfy

\[
\Pr(X+Y\le h)>\tfrac12\{F(h/2)G(h)+F(h)G(h/2)\},\quad h>0.
\]

To prove this, integrate \(f(u)g(v)\) over the square \([0,h]^2\). The desired difference vanishes pointwise in both same-side subsquares \([0,h/2]^2\) and \([h/2,h]^2\). In each cross subsquare, the triangular region \(u+v<h\) contributes plus one half of the density, and its complement contributes minus one half. Reflect the latter through \((u,v)\mapsto(h-v,h-u)\), a unit-Jacobian involution within that cross subsquare. Every point \((u,v)\) in the lower triangle satisfies \(u<h-v\) and \(v<h-u\), so \(f(u)g(v)>f(h-v)g(h-u)\). Integrating proves the strict inequality. The exponential densities meet these hypotheses, whence

\[
T>\frac{T_A+T_B}{2}.
\]

On the other hand, with \(r=e^{-ah/2}\), \(s=e^{-bh/2}\),

\[
T_A-T_B=(1-r)(1-s)(s-r).
\]

Its sign is the sign of \(a-b\). If \(a>b\), the larger approximation \(T_A\) is strictly nearer to \(T\) than \(T_B\), because \(T\) lies strictly above their arithmetic midpoint; the reverse applies if \(a<b\). This establishes strict optimal order for all \(h>0\), including possible overshoot of the better approximation.

**Exactness and bias signs.** Write \(\operatorname{sinhc}(z)=\sinh(z)/z\), continuously set to one at zero. Direct subtraction of the preceding exponential expressions and hyperbolic rearrangement yield

\[
T_A-T=bh\,e^{-(a+b)h/2}\left[
\operatorname{sinhc}\left(\frac{(a-b)h}{2}\right)
-\operatorname{sinhc}\left(\frac{bh}{2}\right)\right],
\]

\[
T_B-T=ah\,e^{-(a+b)h/2}\left[
\operatorname{sinhc}\left(\frac{(b-a)h}{2}\right)
-\operatorname{sinhc}\left(\frac{ah}{2}\right)\right].
\]

The even function \(\operatorname{sinhc}\) is strictly increasing in the absolute value of its argument on positive values: differentiation gives numerator \(z\cosh z-\sinh z>0\) for \(z>0\), as its derivative is \(z\sinh z>0\). Consequently the first signed error is zero exactly when \(|a-b|=b\), which for \(a,b>0\) means \(a=2b\); its sign equals that of \(a-2b\). Similarly the second signed error vanishes exactly at \(b=2a\), and its sign equals that of \(b-2a\). Because only the initial-state-\(0\) row can differ, these identities establish exactness of the entire stochastic matrix, not just one observable.

**Size of the ordering effect.** When \(a>2b\) is held fixed and \(h\to\infty\), direct exponential comparison gives

\[
|T_A-T|\sim\frac{b}{a-b}e^{-bh},\qquad
|T_B-T|\sim e^{-bh/2},\quad
\frac{|T_B-T|}{|T_A-T|}\sim\frac{a-b}{b}e^{bh/2}.
\]

At \(a=2b\), \(T_A=T\) exactly instead of merely asymptotically. These statements follow from the displayed closed forms and do not presume that large steps are accurate for arbitrary generators.

## Verification

A standalone Python 3 program, `verify.py`, uses 65-digit decimal arithmetic and explicitly multiplies the two stochastic substep matrices. It checks both terminal-probability formulas, the hyperbolic bias formulas, strict midpoint and best-order inequalities, and the \(2:1\) exactness cases. Running `python verify.py` completed **3,937** comparison cases successfully, including twelve exactness cases. These are independent numerical consistency checks; universal claims rest on the analytic proof above, not on finite enumeration.

## Relationship to prior work

Engblom's 2014/2015 study of stochastic jump kinetics introduces exact split generators, analyzes strong convergence, and writes down the second-order Strang half/full/half composition; its examples and estimates are not an all-step total-variation comparison of the two orders on a serial irreversible three-state chain. Lukassen and Kiehl (publicly available 2018 abstract) analyze reaction splitting and stiffness/order reduction, but the accessible abstract does not disclose an exact \(2:1\) serial-chain resonance; the inaccessible full text remains a priority risk. Mitra, Diddens and Heuer (2026) compare the two Strang orientations for a three-state reaction/diffusion model with reversible transitions and derive particular error comparisons and modified reaction probabilities. Their model and reported comparison do not give the present two irreversible transitions, exact all-step rate ordering, strict two-rate signed-error classification, or the exact resonance. Related indexed Markov splitting results address other topologies, state dimensions, or extrapolated methods. These scientific distinctions are subject to independent publication-priority checking.

## Limitations

The theorem concerns one exact split step, precisely two consecutive irreversible transitions, positive constant rates, and total-variation error for probability distributions. It makes no universal assertion about reversible chains, coupled chemistry/diffusion, different observables, weak vs strong pathwise error, multiple composed steps, or computational cost. The \(2:1\) exactness is particular to this serial generator structure. Historical priority is not independently verified; a closely relevant 2018 paper was accessible only by its abstract.

## References

1. S. Engblom, *Strong convergence for split-step methods in stochastic jump kinetics*, arXiv:1412.6292 (first posted 19 December 2014), SIAM Journal on Numerical Analysis 53 (2015), 2655–2676. https://arxiv.org/abs/1412.6292
2. A. A. Lukassen and M. Kiehl, *Operator splitting for stiff chemical reaction systems*, Proceedings in Applied Mathematics and Mechanics 18 (2018), e201800026; public abstract dated 17 December 2018. https://doi.org/10.1002/pamm.201800026
3. S. Mitra, D. Diddens and A. Heuer, *Improving operator splitting and effective reaction probability for a reactive-step based molecular dynamics workflow*, Journal of Mathematical Chemistry 64 (2026), article 24, published 21 April 2026. https://doi.org/10.1007/s10910-026-01780-x
4. A. Chevallier and S. Engblom, *Pathwise error bounds in multiscale variable splitting methods for spatial stochastic kinetics*, arXiv:1607.00805 (first posted 4 July 2016). https://arxiv.org/abs/1607.00805
