# Sharp five-state positivity onset and topology-dependent recovery for the implicit Taylor method

## Finding

Consider the one-stage, second-order implicit Taylor update applied to a unit-rate continuous-time Markov generator \(Q\):
\[
T_Q(h)=\bigl(I-hQ+\tfrac12h^2Q^2\bigr)^{-1},\qquad h\ge0.
\]
Two canonical generator families are considered: the unit directed cycle \(C_n=P_n-I_n\), where \(P_n\) advances every state one place modulo \(n\), and the unit pure-birth generator \(B_n\), with transitions \(i\to i+1\) of rate one for \(i<n-1\) and state \(n-1\) absorbing. In each family, for **every** integer \(n\ge1\), \(T_Q(h)\) exists for all \(h\ge0\), and \(T_Q(h)\mathbf1=\mathbf1\). It is entrywise nonnegative at **every** step size if and only if \(n\le4\). For every \(n\ge5\), it has a negative entry at every sufficiently small positive step size, but it becomes nonnegative for all sufficiently large step sizes (depending on \(n\)).

For \(n=5\), the complete, exact positivity sets differ by topology:
\[
T_{C_5}(h)\ge0\quad\Longleftrightarrow\quad
h=0\ \text{or}\ h\ge\rho_C,
\qquad \rho_C=\sqrt{1+\frac2{\sqrt5}}-1
=0.376381920471\ldots;
\]
\[
T_{B_5}(h)\ge0\quad\Longleftrightarrow\quad
h=0\ \text{or}\ h\ge\rho_B,
\]
where \(\rho_B=0.496605762665\ldots\) is the unique positive solution of
\[
h^2(h+2)(h+6)=4.
\]
In particular, \(\rho_C<\rho_B\); at the same positive step \(h=2/5\), the five-cycle has a nonnegative numerical transition, whereas the five-state absorbing birth chain does not. All nonzero entries allowed by the graph become strictly positive above their respective five-state thresholds.

## Assumptions and scope

- States are ordered \(0,\ldots,n-1\). We use **row generators** and entrywise inequalities; choosing the column convention transposes every matrix and leaves all claims unchanged.
- The directed cycle has generator \(C_n=P_n-I_n\), with \((P_n)_{i,i+1\pmod n}=1\); for \(n=1\), \(C_1=0\). The birth generator has \((B_n)_{i,i}=-1\) and \((B_n)_{i,i+1}=1\) for \(i<n-1\), and a zero final row.
- The result concerns the **one-stage implicit Taylor** map \(y_{k+1}=y_k+hQy_{k+1}-\frac12h^2Q^2y_{k+1}\), not the explicit Taylor polynomial, Crank–Nicolson, Gauss, or Radau methods. There is no claim for arbitrary Markov generators, nonunit birth rates, or nonlinear operators.
- A nonnegative, row-sum-one matrix is a stochastic numerical transition. A row-sum-one matrix with negative entries is not. Positivity is a property of the **endpoint numerical matrix**, not of internal stages or a norm.

## Proof

**1. Well-defined mass-conserving update.** Put \(r(z)=(1-z+z^2/2)^{-1}\). Its poles are \(1\pm i\). The spectra of \(B_n\) and \(C_n\) are contained in \(\{z:\Re z\le0\}\), so \(T_Q(h)=r(hQ)\) exists for every \(h\ge0\). Since \(Q\mathbf1=0\) and \(r(0)=1\), \(T_Q(h)\mathbf1=\mathbf1\).

**2. Five states are necessary for small-step negativity.** At the origin,
\[
r(z)=1+z+\tfrac12z^2+0z^3-\tfrac14z^4+O(z^5).
\]
For a directed cycle with \(n\ge5\), the entry from state \(0\) to state \(4\) has no contribution of order less than four. At fourth order, its coefficient is the coefficient of \(P_n^4\) in \(-\frac14h^4(P_n-I_n)^4\), namely \(-\frac14h^4\). Therefore
\[
(T_{C_n}(h))_{0,4}=-\tfrac14h^4+O(h^5)<0
\]
for all sufficiently small \(h>0\). For \(B_5\), the same expansion holds for the transition \(0\to4\), since all paths to state \(4\) require four advances. For \(B_n\) with \(n\ge6\), the transient-to-transient entry \(0\to4\) has the same expansion. This is an analytic asymptotic sign argument for every fixed \(n\), not a finite enumeration.

**3. Birth chains, including the exact five-state boundary.** Let
\[
D=h^2+2h+2>0.
\]
For a transient starting state, the transition to another transient state at forward distance \(j\) equals \(b_j(h)=h^jr^{(j)}(-h)/j!\). Direct differentiation gives
\[
\begin{aligned}
b_0&=2/D,\\
b_1&=4h(h+1)/D^2,\\
b_2&=2h^2(3h^2+6h+2)/D^3,\\
b_3&=8h^4(h+1)(h+2)/D^4,\\
b_4&=2h^4(5h^4+20h^3+20h^2-4)/D^5.
\end{aligned}
\]
Every transient-to-absorbing coefficient is one minus the sum of the remaining transient coefficients, by row-sum preservation. For one, two, three, or four forward jumps to absorption these are, respectively,
\[
\begin{aligned}
a_1&=h(h+2)/D,\\
a_2&=h^2(h^2+4h+2)/D^2,\\
a_3&=h^4(h^2+6h+6)/D^3,\\
a_4&=h^4\bigl(h^4+8h^3+12h^2-4\bigr)/D^4.
\end{aligned}
\]
For \(n\le4\), all reachable transient entries use \(b_0,b_1,b_2\), and all absorption entries use \(a_1,a_2,a_3\): each is nonnegative for every \(h\ge0\). All entries below the upper diagonal are identically zero. For \(B_5\), the only potentially negative entry is \((0,4)\), which is exactly \(a_4\). Its numerator is \(h^4[q_B(h)]\), where
\[
q_B(h)=h^2(h+2)(h+6)-4.
\]
Since \(q_B(0)=-4\), \(q_B\) is strictly increasing on \((0,\infty)\), and \(q_B(h)\to+\infty\), it has precisely one positive root \(\rho_B\). This proves the complete \(B_5\) classification, including the zero step.

**4. Cycles of up to five states.** Circulant symmetry reduces positivity to the first row. Symbolic inversion gives the following first-row numerators \(N_{n,j}\), with a common positive denominator \(H_n\) for each \(n\). Multiplication by \(H_n\) is exact; all displayed polynomials apart from \(N_{5,4}\) have nonnegative coefficients.

For \(n=2\):
\[
H_2=2h^2+2h+1,\quad
(N_{2,0},N_{2,1})=(h^2+h+1,\ h(h+1)).
\]
For \(n=3\):
\[
\begin{aligned}
H_3&=9h^4+18h^3+18h^2+12h+4,\\
(N_{3,0},N_{3,1},N_{3,2})&=
(3h^4+6h^3+8h^2+8h+4,\ h(3h^3+6h^2+8h+4),\ h^2(3h^2+6h+2)).
\end{aligned}
\]
For \(n=4\):
\[
\begin{aligned}
H_4&=2(h+1)(h^2+1)(2h^2+2h+1),\\
(N_{4,0},N_{4,1},N_{4,2},N_{4,3})&=
(h^5+2h^4+3h^3+5h^2+4h+2,\\
&\qquad h(h^4+2h^3+4h^2+4h+2),\\
&\qquad h^2(h^3+2h^2+3h+1),\ h^4(h+2)).
\end{aligned}
\]
For \(n=5\):
\[
H_5=25h^8+100h^7+200h^6+300h^5+360h^4+320h^3+200h^2+80h+16,
\]
\[
\begin{aligned}
N_{5,0}&=5h^8+20h^7+40h^6+80h^5+136h^4+160h^3+128h^2+64h+16,\\
N_{5,1}&=h(5h^7+20h^6+50h^5+100h^4+136h^3+120h^2+64h+16),\\
N_{5,2}&=h^2(5h^6+20h^5+50h^4+80h^3+76h^2+40h+8),\\
N_{5,3}&=h^4(5h^4+20h^3+40h^2+40h+16),\\
N_{5,4}&=h^4(5h^4+20h^3+20h^2-4).
\end{aligned}
\]
Thus \(C_n\) is positive for all \(h\ge0\) when \(n\le4\). The only exceptional \(C_5\) entry is the forward-four entry, and its sign is that of
\[
q_C(h)=5h^2(h+2)^2-4.
\]
This polynomial is strictly increasing for \(h>0\) and has the unique positive root \(\rho_C=\sqrt{1+2/\sqrt5}-1\). The difference
\[
q_C(h)-q_B(h)=4h^2(h+1)(h+2)>0\quad(h>0)
\]
proves \(\rho_C<\rho_B\), while direct substitution \(h=2/5\) places it strictly between the two roots.

**5. Eventual recovery at every fixed dimension.** For cycles, \(C_n\) has the simple eigenvalue zero and all other eigenvalues have negative real part. Since \(r(h\lambda)\to0\) as \(h\to\infty\) for every nonzero eigenvalue \(\lambda\),
\[
T_{C_n}(h)\longrightarrow\frac1n\mathbf1\mathbf1^{\mathsf T}.
\]
Every entry of the limit is positive, hence every entry is positive for all sufficiently large \(h\). For birth chains, the transient Jordan block gives \(b_j(h)=2(j+1)h^{-2}+O(h^{-3})>0\) for every fixed finite transient distance \(j\), while each transient-to-absorbing entry equals \(1-O(h^{-2})>0\). The absorbing diagonal equals one, and inaccessible entries are identically zero. This proves eventual positivity for all fixed finite birth chains.

## Verification

The standalone `checker.py` uses exact SymPy rational arithmetic. It confirms the Taylor coefficient, the circulant numerator/denominator identities for dimensions two through five, birth-chain coefficient identities through six states, row sums, both threshold polynomial identities, and exact rational examples on either side of the thresholds. A fresh run prints `PASS: 239 exact symbolic/rational assertions`. The accompanying `checker_output.txt` records its output. These checks verify finite formulas; the all-dimension onset and eventual-recovery conclusions are proved analytically in steps 2 and 5.

## Relationship to prior work

Gottlieb, Grant, Hu and Shu (arXiv:2102.11939, first public 2021-02-23) introduce the second-order implicit Taylor method and prove unconditional strong-stability preservation **under an additional backward-derivative condition**. A generic directed Markov generator does not satisfy the needed cone-positivity condition: for a three-state birth chain, the off-diagonal second-advance entry of \(-Q^2\) is negative. Consequently our five-state counterexamples do **not** contradict their conditional theorem. The present result instead gives graph-family-specific, necessary-and-sufficient positivity and recovery laws not supplied by that theorem.

Lóczi and Ketcheson (arXiv:1303.6651) analyze global absolute-monotonicity radii of rational functions. Here \(r^{(4)}(0)=-6<0\), so a generic positive-radius uniform monotonicity theorem does not certify this method; the exact low-dimensional directed-graph classifications are a more selective question. Gottlieb and Grant's arXiv:2412.15142 survey restates the conditional two-derivative SSP framework, not these graph-specific quartic thresholds. Related published positivity barriers for different Padé, Gauss and SDIRK maps concern **different stability functions** and do not imply the two threshold equations above.

## Limitations

The results are for unit-rate directed cycles and unit-rate acyclic pure-birth chains only; extending the exact five-state thresholds to arbitrary rates, arbitrary weighted graphs, or nonlinear problems is unproved. Negative numerical entries are not negative exact transition probabilities: \(e^{hQ}\) remains Markov-positive. These results do not refute the conditional SSP theorem, because its backward-derivative assumption fails on the example generators. The symbolic checker is not a formal proof assistant and does not certify infinitely many dimensions. Potential older specialist precedence outside the inspected literature is unresolved; no independent audit has been performed.

## References

1. S. Gottlieb, Z. J. Grant, J. Hu, R. Shu, *High order strong stability preserving multi-derivative implicit and IMEX Runge–Kutta methods with asymptotic preserving properties*, arXiv:2102.11939 (first public 2021-02-23), https://arxiv.org/abs/2102.11939, especially Sections 1, 2.2–2.4.
2. L. Lóczi, D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651 (2013), https://arxiv.org/abs/1303.6651, especially Section 1.
3. S. Gottlieb, Z. J. Grant, *A review of high order strong stability preserving two-derivative explicit, implicit, and IMEX methods*, arXiv:2412.15142 (2024), https://arxiv.org/abs/2412.15142, Sections 1–3.
