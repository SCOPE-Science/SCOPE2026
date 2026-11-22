# Sharp rate balancing for Crank–Nicolson positivity on a bidirected star

## Finding
Let \(m\ge2\) be an integer. Consider the continuous-time Markov chain with one hub \(0\) and \(m\) interchangeable leaves, hub-to-each-leaf rate \(a>0\), and each-leaf-to-hub rate \(b>0\). For its generator \(Q\) in row convention, define the completed Crank–Nicolson step
\[
C_h=(I-hQ/2)^{-1}(I+hQ/2),\qquad h\ge0.
\]
The exact positivity horizon \(H_m(a,b):=\sup\{h\ge0:C_h\text{ is entrywise nonnegative}\}\) has a **unique global maximum as the return rate \(b>0\) varies with \(m,a\) fixed**:
\[
\boxed{b_*=\frac{m^2}{2m-1}a,\qquad \max_{b>0}H_m(a,b)=\frac{2(2m-1)}{ma(m-1)}.}
\]
At \(b=b_*\), the hub diagonal and all leaf diagonals of \(C_h\) become zero simultaneously at the sharp boundary. Below this rate, the hub is the unique limiting site; above it, all leaves are the limiting sites. In comparison, the symmetric choice \(b=a\) has horizon \(2/[(m-1)a]\), so rate balancing increases the largest nonnegative timestep by the exact factor \(2-1/m\), tending to two as \(m\to\infty\).

## Assumptions and scope
The \((m+1)\times(m+1)\) generator has \(Q_{0i}=a\), \(Q_{i0}=b\), \(Q_{00}=-ma\), \(Q_{ii}=-b\) for \(1\le i\le m\), and all other off-diagonal entries zero. Row probability vectors evolve as \(p'(t)=p(t)Q\). Both rates are strictly positive; the result covers all real positive \(a,b\) and all integer \(m\ge2\). Positivity means entrywise nonnegativity of the completed step, equivalently preservation of nonnegative row vectors. No statement about positivity of internal stage representations or about other Runge–Kutta integrators is made.

Put \(s=h/2\), and introduce
\[
B=b\bigl[b+(m-2)a\bigr]>0,
\quad s_L=\frac{ma+\sqrt{m^2a^2+4B}}{2B},
\quad s_H=\begin{cases}(ma-b)^{-1},&b<ma,\\ +\infty,&b\ge ma.\end{cases}
\]
The complete sharp law is
\[
\boxed{C_h\ge0\quad\Longleftrightarrow\quad 0\le h\le H_m(a,b)=2\min\{s_H,s_L\}.}
\]

## Proof
Write \(R_s=(I-sQ)^{-1}\). The inverse \(R_s\) is a strictly positive row-stochastic matrix whenever \(s>0\), because \(I-sQ\) is an irreducible nonsingular \(M\)-matrix. Moreover, the Cayley identity gives \(C_h=2R_s-I\). Thus all off-diagonal entries of \(C_h\) are positive for \(h>0\), while nonnegativity of the diagonal entries is necessary and sufficient for the entire matrix to be nonnegative.

The leaf block of \(I-sQ\) is \((1+sb)I_m\). Its scalar Schur complement at the hub is \(1+sma/(1+sb)\), giving, with \(T=1+s(b+ma)\),
\[
(R_s)_{00}=\frac{1+sb}{T},\qquad
(R_s)_{ii}=\frac1{1+sb}+\frac{s^2ab}{(1+sb)T}\quad(1\le i\le m).
\]
Consequently the only distinct diagonal signs in the Crank–Nicolson matrix are
\[
(C_h)_{00}=\frac{1+s(b-ma)}{T},
\qquad
(C_h)_{ii}=\frac{1+mas-b[b+(m-2)a]s^2}{(1+sb)T}.
\]
All denominators are positive. The hub numerator is nonnegative through \(s_H\), and the leaf numerator is a strictly concave quadratic in \(s\) with precisely one positive zero \(s_L\). This proves the exact positivity interval.

When \(b<ma\), substitute \(s=s_H=1/(ma-b)\) into the leaf diagonal to obtain the exact identity
\[
(C_{2s_H})_{ii}=\frac{am^2-(2m-1)b}{am^2}.
\]
Therefore the hub crosses first for \(b<b_*:=am^2/(2m-1)\), the leaf crosses first for \(b>b_*\), and the two cross simultaneously at \(b=b_*\). Here \(0<b_*<ma\); for \(b\ge ma\), the hub never becomes negative and leaves still have a finite crossing.

To prove global optimality in \(b\), observe that on \(0<b<ma\) the hub crossing \(s_H=1/(ma-b)\) increases strictly with \(b\). The leaf crossing \(s_L\) decreases strictly with \(b\), since for any fixed \(s>0\) its numerator
\[
F(s,b)=1+mas-b[b+(m-2)a]s^2
\]
strictly decreases in \(b\), is initially positive, and has exactly one positive zero. Hence \(\min\{s_H,s_L\}\) increases strictly until \(b_*\) and decreases strictly afterward (including \(b\ge ma\)), proving uniqueness. Substituting \(b=b_*\) into \(s_H\) gives
\[
H_m(a,b_*)=\frac{2(2m-1)}{ma(m-1)}.
\]
At \(b=a<b_*\), \(H_m(a,a)=2/[(m-1)a]\). Division gives the exact improvement factor \((2m-1)/m\), as claimed.

## Verification
The standalone file `verify.py` uses symbolic algebra to check the hub and leaf resolvent identities, the crossing equality, and the simultaneous-boundary law. It then uses exact rational inverses to test stochasticity, off-diagonal strict positivity and complete diagonal sign classification across integer leaf counts \(2\) through \(11\), with 20 seeded positive rational-rate triples each. Additional rational and high-precision checks straddle the three return-rate regimes. The script reports 1,513 passed finite assertions. These computations supplement rather than establish the all-real theorem.

## Relationship to prior work
The classical Runge–Kutta positivity and absolute-monotonicity framework is prior work; in particular, the general completed-trapezoidal positivity-radius analysis is not new. Fekete, Ketcheson and Lóczi (arXiv:1610.00228, publicly posted October 2, 2016) study sharp positivity of explicit Runge–Kutta steps on convective semidiscretizations; they do not classify the implicit midpoint step of this reversible hub–leaf chain. Higueras and Roldán (2007) study positivity of implicit Runge–Kutta implementations and stage predictors, but not this rate-optimization problem.

Two open numerical research records already establish (i) the general diagonal-resolvent criterion for completed Crank–Nicolson Markov steps and (ii) a sharp hub-controlled positivity threshold for *symmetric weighted-star generators*, whose two edge directions necessarily have equal rates. Those principles are explicitly prior and not claimed here. The present result instead fixes every outward hub rate and optimizes a **separate, unequal** inward return rate, obtaining an exact hub-to-leaf limiting-site switch and a unique sharp rate-design rule. The symmetric-star result is recovered only on the line \(b=a\); the general resolvent law does not itself give the maximizing rate or the switch formula.

## Limitations
The family has homogeneous rates within each direction (all outward rates equal, all inward rates equal), not arbitrary independently varying edge rates. The optimized safe timestep is not an optimal time-discretization error, mixing time, stability margin, or prescribed-stationary-law solution. In exact arithmetic, each boundary transition has zero diagonal entries; roundoff can perturb that sign. General spectral and M-matrix methods furnish parts of the proof, and a specialized unindexed formula could affect publication priority. Independent mathematical validation has not been performed.

## References
1. I. Fekete, D. I. Ketcheson, L. Lóczi, *Positivity for convective semi-discretizations*, arXiv:1610.00228, first public version October 2, 2016. https://arxiv.org/abs/1610.00228
2. I. Higueras and T. Roldán, *Numerical positivity for Runge–Kutta methods*, Proceedings of XX CEDYA / X CMA, Sevilla, September 24–28, 2007. https://idus.us.es/server/api/core/bitstreams/7fb8681b-bb0e-41c1-832b-4f0cfdfdf643/content
3. Z. Horváth, *Positivity of Runge–Kutta and diagonally split Runge–Kutta methods*, Appl. Numer. Math. 28 (1998), 309–326. DOI:10.1016/S0168-9274(98)00050-6.
4. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*, open research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a
5. *Sharp positivity horizon and homogenization extremum for weighted-star Crank–Nicolson steps*, open research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-positivity-horizon-and-homogenization-extremum-for-weighte--2ba13f6aa0a6
