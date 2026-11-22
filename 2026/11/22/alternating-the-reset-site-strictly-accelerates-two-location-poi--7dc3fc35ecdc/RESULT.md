# Alternating the reset site strictly accelerates two-location Poisson search

## Finding
For any reset-free search mechanism with two possible restart states and independent Poisson interruption at rate \(r>0\), let \(a=\mathbb E[e^{-r S_A}]\) and \(b=\mathbb E[e^{-r S_B}]\) be its two single-attempt success probabilities, with \(0<a,b<1\). The exponential of an infinite hitting time is interpreted as zero. At every interruption, let the reset state switch from \(A\) to \(B\), or conversely, with probability \(c\in[0,1]\); otherwise keep the previous reset state. Draw the initial restart state uniformly. With independent fresh search paths and reset clocks after each interruption, the mean completion time is exactly
\[
M(c)=\frac{a+b-2ab+4c(1-a)(1-b)}{2r[ab+c(a+b-2ab)]}.
\]
Its entire response to serial reset-site anticorrelation satisfies
\[
\frac{dM}{dc}=-\frac{(a-b)^2}{2r[ab+c(a+b-2ab)]^2}.
\]
Consequently deterministic alternation \(c=1\) minimizes the mean over this entire symmetric two-site Markov family; freezing the site \(c=0\) maximizes it. Both are unique unless \(a=b\), when all protocols have the same mean. The iid two-site choice is \(c=1/2\), and the exact improvement from iid to alternation is
\[
M(1/2)-M(1)=\frac{(a-b)^2}{2r(a+b)(a+b-ab)}.
\]
Importantly, every protocol has the same *unconditioned one-step reset-location marginal*: one-half at each site. The effect is entirely due to correlations between successive proposed locations, not to a change in the marginal location distribution or reset-clock intensity.

For Brownian motion with generator \(D\partial_x^2\) on a ring of circumference \(L>0\), with a perfectly absorbing point at \(0\), and restart sites \(x_A,x_B\in(0,L)\),
\[
a=\frac{\cosh[(L/2-x_A)\sqrt{r/D}]}{\cosh[(L/2)\sqrt{r/D}]},\qquad
b=\frac{\cosh[(L/2-x_B)\sqrt{r/D}]}{\cosh[(L/2)\sqrt{r/D}]}.
\]
Thus alternation is strictly better than iid for every fixed \(r>0\) exactly when \(x_B\notin\{x_A,L-x_A\}\); equality occurs for coincident or target-reflected restart positions.

## Assumptions and scope
Let \(S_A,S_B\in[0,\infty]\) be the first target-arrival times during uninterrupted attempts, started at the indicated restart states. The law of the search path is renewed independently after every interruption and depends only on that state. Each interruption clock is exponential with rate \(r\), independent of search and of site selections. If arrival occurs before the interruption, the process finishes; otherwise an instantaneous relocation is made according to
\[
P_c=\begin{pmatrix}1-c&c\\c&1-c\end{pmatrix}.
\]
The initial state is chosen with probabilities \((1/2,1/2)\). The symmetric transition matrix preserves this marginal at each *pre-generated* reset index; this must not be confused with the reset-site distribution conditioned on survival. No travel time, positional memory across interruptions, or target detection during a relocation is included. We require the two success probabilities strictly between zero and one; those bounds hold at both non-target Brownian ring sites. All optimization statements fix \(r\) and the two restart sites, and vary only \(c\).

## Proof
For a fresh attempt from state \(i\in\{A,B\}\), let \(E\) be its independent rate-\(r\) interruption time and write \(p_i=\mathbb E[e^{-rS_i}]\). Conditioning on \(S_i\), the probability that target arrival precedes interruption is \(p_i\). By integrating the attempt-survival function,
\[
\mathbb E[\min(S_i,E)]=\int_0^\infty e^{-rt}\Pr(S_i>t)\,dt=\frac{1-p_i}{r}.
\]
The identity also holds with positive mass at \(S_i=\infty\). Let \(T_i\) be the full mean remaining time starting a fresh attempt at state \(i\). Renewal at the first interruption gives
\[
\begin{aligned}
T_A&=\frac{1-a}{r}+(1-a)[(1-c)T_A+cT_B],\\
T_B&=\frac{1-b}{r}+(1-b)[cT_A+(1-c)T_B].
\end{aligned}
\]
The coefficient matrix is
\[
K_c=\begin{pmatrix}a+c(1-a)&-c(1-a)\\-c(1-b)&b+c(1-b)\end{pmatrix}.
\]
Its determinant is \(\Delta_c=ab+c(a+b-2ab)>0\). Inverting it (or applying Cramer's rule) to the two renewal equations and averaging \(T_A,T_B\) with weights one-half yields exactly the stated rational formula for \(M(c)\). Differentiation simplifies to the negative square in the finding. The denominator is strictly positive for all \(0\le c\le1\), so the optimum, strictness and boundary cases follow without local-optimizer assumptions. At \(c=1/2\), the formula reduces algebraically to \((2-a-b)/[r(a+b)]\), the established iid-location renewal result, and subtraction at \(c=1\) gives the displayed gain.

For the Brownian ring, cutting it at the absorbing point identifies the complement with an interval \((0,L)\) whose endpoints are both absorbing. The discounted probability \(u(x)=\mathbb E_x[e^{-rS}]\) solves \(Du''=ru\) with \(u(0)=u(L)=1\). Its unique bounded solution is \(u(x)=\cosh[(L/2-x)\sqrt{r/D}]/\cosh[(L/2)\sqrt{r/D}]\). Because \(\cosh\) is strictly increasing on nonnegative arguments, \(u(x_A)=u(x_B)\) precisely when \(|L/2-x_A|=|L/2-x_B|\), equivalent to \(x_B=x_A\) or \(x_B=L-x_A\). This proves the ring strictness criterion.

## Verification
Run \(\texttt{python verify.py}\) with Python 3, SymPy and NumPy installed. It checks the rational inversion, exact derivative and iid-gain identities symbolically; compares them with 120 exact rational cases; and, in 20 independent comparisons, solves a killed continuous-time random-walk generator on a finite cycle with two reset phases rather than relying on the renewal formula. A Brownian ring example with \(L=D=1\), \(r=4\), \(x_A=0.2\), and \(x_B=0.47\) gives means approximately \(0.105247\), \(0.102742\) and \(0.101382\) for \(c=0\), \(1/2\), and \(1\), respectively. These numerical checks supplement but do not replace the exact proof.

## Relationship to prior work
Julián-Salgado, Castro-Villarreal, Dagdug and Boyer (2026), §§II and IV–VI, give the full two-reset-location Brownian-ring analysis when successive site draws are independent. Their Eq. (27) is recovered here at \(c=1/2\), so that case and the ring hitting transform are credited, not claimed as new. Their explicitly iid site assumption does not determine the mean of the correlated protocols \(c\ne1/2\). Méndez, Flaquer-Galmés and Campos (2024), §§II and VI–VIII, similarly analyze independent random spatial reset locations on the line. Discrete resetting treatments with a single fixed reset node are further background. The assessed extension is the *global order over temporal reset-site correlations at identical site marginals*, quantified by the negative-square derivative and strict ring classification. An unindexed equivalent two-state Markov-renewal theorem remains possible.

## Limitations
The theorem concerns *mean* target-arrival time, not stochastic ordering of the entire distribution, fixed-start-phase optimization, reset-rate optimization, or optimality across arbitrary non-Markov or asymmetrically weighted selection schemes. The marginal equality is unconditional by proposed reset index, not conditioned on particles still surviving to that index. The no-travel-time and independent-attempt assumptions matter. The universal renewal identity is exact, while its literature priority remains subject to further independent examination.

## References
1. P. Julián-Salgado, P. Castro-Villarreal, L. Dagdug and D. Boyer, *Mirror transitions in diffusion with stochastic resetting confined on a ring*, arXiv:2605.08414v1, first public 2026-05-08, https://arxiv.org/abs/2605.08414 . Full text inspected: §§II, IV–VI, VII and Appendix A.
2. V. Méndez, R. Flaquer-Galmés and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, Physical Review E **109**, 044134 (2024), arXiv:2401.01125, https://doi.org/10.1103/PhysRevE.109.044134 . Authors' lawful open full text inspected: https://webs.uab.cat/vmendez/wp-content/uploads/sites/97/2024/04/128.pdf .
3. *Discrete space-time resetting model: application to first-passage and transmission statistics*, Journal of Physics A (2022), https://doi.org/10.1088/1751-8121/ac9765 . Online text inspected for its fixed-site reset model.
