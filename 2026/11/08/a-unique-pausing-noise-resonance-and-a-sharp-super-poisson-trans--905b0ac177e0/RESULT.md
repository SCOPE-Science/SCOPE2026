# A unique pausing-noise resonance and a sharp super-Poisson transition in a two-site exclusion process

## Finding

For a two-site totally asymmetric exclusion process whose particles independently alternate between active and paused modes, with unit entry, hopping and exit rates, let \(p>0\) be the pausing rate and \(q>0\) the unpausing rate. The stationary exit count \(N(t)\) has mean current \(J(p,q)\) and long-time Fano factor \(F(p,q)=\lim_{t\to\infty}\operatorname{Var}[N(t)]/\mathbb E[N(t)]\). Then:

1. \(J\) is strictly decreasing in \(p\), and \(F\) is strictly decreasing in \(q\) for fixed positive \(p\).
2. For **every** \(q>0\), \(p\mapsto F(p,q)\) has exactly one critical point \(p_*(q)>0\), which is its strict global maximum. The endpoint values are \(F(0,q)=9/25\) and \(\lim_{p\to\infty}F(p,q)=1/2\), with the second approached from above.
3. There is a unique \(q_c\in(0.33645,0.33646)\) such that \(\max_{p>0}F(p,q)>1\) precisely for \(0<q<q_c\), equals 1 at \(q_c\), and is less than 1 for \(q>q_c\). Numerically \(q_c\simeq0.3364557959167649\).
4. The maximizing rate obeys the sharp asymptotic laws
\[
 p_*(q)\sim\tau q\quad(q\downarrow0),\qquad
 p_*(q)\sim4q^2\quad(q\to\infty),
\]
where \(\tau=1.001802622284\ldots\) is the unique positive root of \(63\tau^4+285\tau^3+150\tau^2-300\tau-200=0\). Moreover
\[
 \max_{p>0}F(p,q)\sim\frac{4\tau(9\tau^2+30\tau+20)}{q(7\tau^2+15\tau+10)^2}
 \sim\frac{0.230468969852}{q}\quad(q\downarrow0),
\]
\[
 \max_{p>0}F(p,q)=\frac12+\frac{1+o(1)}{16q^2}\quad(q\to\infty).
\]

By comparison, the corresponding **one-site** exclusion model has
\[
 F_1(p,q)=\frac{p^2+2pq+2p+2q^2}{(p+2q)^2},\qquad
 \partial_pF_1=\frac{2\{p(q-1)+2q\}}{(p+2q)^3}.
\]
For \(q\geq1\) the one-site Fano factor is strictly increasing and has no interior maximum. Thus two sites are the smallest possible lattice length for a pausing-noise peak at *every* unpausing rate in this model.

## Assumptions and scope

The state space is \(\{0,A,P\}^2\), with \(0\) an empty site and \(A,P\) active and paused particles. Entry \((0,y)\to(A,y)\) occurs at rate 1; hopping \((A,0)\to(0,A)\) at rate 1; exit \((x,A)\to(x,0)\) at rate 1 and adds one count; independently at each occupied site \(A\to P\) occurs at rate \(p\) and \(P\to A\) at rate \(q\). All clocks are independent, waiting times exponential; both boundary rates and the active hopping rate are exactly 1. Each \(p,q>0\) gives an irreducible finite-state Markov chain, with a stationary exit point process. No finite-time Fano or non-unit-rate claim is asserted.

## Proof

**Stationary full-counting equations.** Order the nine states lexicographically with \(0,A,P\) represented by \(0,1,2\). Let \(Q\) have columns as source states and transitions as above, so \(\mathbf1^\top Q=0\), and let \(C\) contain just the off-diagonal **counted exit** transitions. The tilted generator is \(Q(s)=Q+(e^s-1)C\). The uniquely normalized stationary vector \(\pi\) and auxiliary vector \(h\) solve
\[
 Q\pi=0,\quad\mathbf1^\top\pi=1,\quad
 Qh=J\pi-C\pi,\quad\mathbf1^\top h=0,\quad
 J=\mathbf1^\top C\pi.
\]
Twice differentiating the dominant eigenvalue of \(Q(s)\) at zero gives the exact formula
\[
 F=1+\frac{2\mathbf1^\top Ch}{J}.
\]
The nine-state linear systems yield
\[
 J=\frac{q(p+2q+2)(2p^2+4pq+p+2q^2+2q)}{P},\qquad F=\frac{A}{P^2},
\]
where the positive polynomial \(P\) is
\[
\begin{aligned}
P={}&4p^4+(20q+12)p^3+(38q^2+40q+7)p^2\\
&+(32q^3+47q^2+15q)p+10q^2(q+1)^2,
\end{aligned}
\]
and \(A=\sum_{k=0}^8a_k(q)p^k\), with coefficients
\[
\begin{aligned}
a_8={}&8,\\
a_7={}&80q+56,\\
a_6={}&336q^2+464q+158,\\
a_5={}&792q^3+1576q^2+1060q+220,\\
a_4={}&1164q^4+2912q^3+2836q^2+1172q+145,\\
a_3={}&1104q^5+3220q^4+3918q^3+2364q^2+620q+36,\\
a_2={}&664q^6+2168q^5+2989q^4+2210q^3+845q^2+120q,\\
a_1={}&232q^7+836q^6+1220q^5+940q^4+404q^3+80q^2,\\
a_0={}&36q^4(q+1)^4.
\end{aligned}
\]
All coefficients are independently generated from the nine-state generator by `verify.py`, not assumed from a numerical fit.

**Current and unpausing monotonicity.** With \(P>0\) for positive rates, direct exact polynomial expansion of the derivative numerator of \(J\) with respect to \(p\) has strictly negative nonzero coefficients. Likewise every nonzero coefficient of
\[
 U_q=(\partial_qA)P^2-A\partial_q(P^2)
\]
is negative; thus \(\partial_pJ<0\) and \(\partial_qF<0\) for all \(p,q>0\). These finite exact-arithmetic sign certificates are reconstructed in the accompanying script.

**Global uniqueness.** Set \(U_p=(\partial_pA)P^2-A\partial_p(P^2)\), a polynomial of degree 14 in \(p\). Its coefficients at \(p^0,p^1,p^2\) are strictly positive for positive \(q\), while the coefficient of \(p^{14}\) is \(-128\). For exponents \(k=3,4,\ldots,13\), the \(p^k\)-coefficient, viewed as a polynomial in \(q\), has exactly one positive zero, with positive leading coefficient and negative constant. Exact Descartes sign checks and rational evaluations isolate these eleven zeros in the consecutive intervals (shown in increasing \(k\) order)
\[
\begin{gathered}
(0.081,0.082),(0.332,0.333),(0.616,0.617),
(0.881,0.882),\\
(1.114,1.115),(1.328,1.329),(1.545,1.546),
(1.802,1.803),\\
(2.167,2.168),(2.835,2.836),(4.761,4.762).
\end{gathered}
\]
Because these intervals are strictly ordered, for each fixed \(q>0\), the coefficients of \(U_p\), in ascending powers of \(p\), consist of an initial nonempty positive block followed by a nonempty negative block. The polynomial therefore has **exactly one positive root** by Descartes' rule and its signs at 0 and infinity. That root is the unique strict global maximizer of \(F\). Direct formulas give \(\partial_pF(0,q)>0\), \(F(0,q)=9/25\), \(F\to1/2\), and \(\lim_{p\to\infty}p(F-1/2)=1/2\).

**Super-Poisson threshold.** Define \(M(q)=F(p_*(q),q)\). The strict \(q\)-monotonicity of \(F\) makes \(M\) continuous and strictly decreasing: use the maximizing \(p\) at the larger of two \(q\)-values. The inequality \(F(0.36467,0.33645)>1\) is an exact rational evaluation. At \(q=0.33646\), the exact integer/rational polynomial \(P^2-A\) in \(p\) has no positive roots by a Sturm-chain count and is positive at \(p=0\); hence \(F(p,0.33646)<1\) for all \(p\geq0\). The intermediate-value theorem and strictness give one and only one \(q_c\) in this bracket.

**Maximizer scaling.** Substituting \(p=qt\) and taking \(q\downarrow0\), one obtains for every fixed \(t>0\)
\[
 \lim_{q\downarrow0}qF(qt,q)=\frac{4t(9t^2+30t+20)}{(7t^2+15t+10)^2}.
\]
The derivative has the opposite sign of \(63t^4+285t^3+150t^2-300t-200\), which has exactly one positive root by Descartes. Evaluating the *exact* \(U_p\) at \(p=q(\tau\pm\varepsilon)\) for arbitrary fixed small \(\varepsilon>0\) and using the established unique root traps \(p_*/q\to\tau\), giving the first pair of asymptotics. Likewise setting \(p=q^2t\) yields
\[
 \lim_{q\to\infty}q^2\{F(q^2t,q)-1/2\}=\frac{t-2}{2t^2},
\]
whose derivative changes sign only at \(t=4\). Exact derivative signs at \(t=4\pm\varepsilon\) trap the unique maximizer, proving \(p_*/q^2\to4\) and the second Fano asymptotic. All displayed limits are symbolic rational-function limits, not extrapolations from finite grids.

## Verification

Run `python verify.py` with Python 3, SymPy and NumPy. The script independently constructs all nine transitions, solves stationary and counting equations, verifies the exact \(J,F\) formulas, the sign coefficients of both monotonicity derivatives, eleven rational isolating intervals, the exact rational super-Poisson witness and Sturm root count, one-site formula, both limits and sixteen numerical tilted-eigenvalue comparisons. The printed PASS line is a reproducibility aid; the infinite-parameter claims rely on the exact polynomial identities and sign arguments above, not on sixteen tests.

## Relationship to prior work

The August 8, 2026 preprint by Thommen introduces an open pausing-TASEP low-frequency exit Fano factor, reporting nonmonotonic fluctuations in large systems (50–500 sites) and an approximate collective noise mechanism. The present **two-site exact solution, all-unpausing-rate uniqueness theorem, sharp Poisson crossing and asymptotic phase diagram** concern a different finite-size question, not a claim to have invented pausing or Fano counting. Keisers et al. develop finite-size current approximations and a mapping to dynamical defects; Wang et al. introduce pausing TASEP in transcription. The generic tilted-generator and stationary Poisson-equation methods are established tools, not novel claims. The formulas apply only to the explicitly normalized two-site model; generic ASEP current-fluctuation results need not imply the unique positive root or the threshold without specialized sign analysis.

## Limitations

The result concerns precisely two sites, unit boundary/hop rates, exponential independent internal-state switching, and stationary infinite-window counting. The critical threshold is tightly bracketed but no elementary radical formula is claimed. The exact finite-state algebra does not establish analogous behavior for arbitrary rate ratios or longer chains. Bibliographic comparison cannot certify absolute priority: in particular, unlocated specialized exact analyses or alternative matrix methods could imply the same special-case statements. No independent audit is claimed.

## References

- Quentin Thommen, *Low-frequency output fluctuations in an open exclusion process with particle pausing*, arXiv:2608.08074v1, first public 2026-08-08, https://arxiv.org/abs/2608.08074.
- Johannes Keisers, Lorenzo Vito Dal Zovo, Norbert Kern, Luca Ciandrini, *Biologically relevant finite-size effects in a driven lattice gas with particle pausing and dynamical defects*, arXiv:2406.16569v1, 2024-06-24, https://arxiv.org/abs/2406.16569.
- Jingkui Wang et al., *Minimal model of transcriptional elongation processes with pauses*, arXiv:1411.4978v1, 2014-11-18, https://arxiv.org/abs/1411.4978.
