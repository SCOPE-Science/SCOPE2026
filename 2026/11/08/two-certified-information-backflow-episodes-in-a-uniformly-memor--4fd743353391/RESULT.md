# Two certified information-backflow episodes in a uniformly memory-reset qubit

## Finding
For the continuous-time uniform-history Poisson-reset qubit specified below, there are **two disjoint intervals of increasing state distinguishability despite a constant, strictly positive reset rate**. In units with Bohr frequency one and reset rate \(r=1/3\), the trace distance \(D(t)\) between the evolved equatorial antipodes obeys the certified strict bounds
\[
D(15/2)<19/500,\quad D(10)>111/1000,\quad
D(14)<7/200,\quad D(16)>9/200.
\]
Consequently the Breuer–Laine–Piilo (BLP) information-backflow functional for this evolution satisfies
\[
\mathcal N_{\mathrm{BLP}}>83/1000,
\]
and the dynamical family is not positive-divisible. The two revivals, and positivity of their total information-backflow contribution, persist on an open interval of reset-rate values containing \(1/3\) (with the frequency and observation times fixed).

## Assumptions and scope
The Hilbert space is \(\mathbb C^2\), \(\hbar=1\), and \(H=\operatorname{diag}(1/2,-1/2)\). Between resets the state evolves by \(\rho\mapsto e^{-iH\Delta t}\rho e^{iH\Delta t}\). Reset events form a Poisson process of intensity \(r>0\). At a reset at physical time \(t>0\), one time \(u\) is sampled uniformly in \([0,t]\), and the actual state from the same trajectory at \(u\) is restored. This is history resetting, not resetting to a fixed initial state. The tested initial states are
\[
\rho_\pm(0)=\tfrac12\begin{pmatrix}1&\pm1\\ \pm1&1\end{pmatrix}.
\]
The channel is the expectation over reset histories. Here \(D(t)=\tfrac12\|\rho_+(t)-\rho_-(t)\|_1\). The BLP functional is the supremum over initial state pairs of the integral of the positive part of their trace-distance time derivative, with time running over \([0,\infty)\). No claim is made about an optimal rate, the complete set of revival windows, or the size of this functional beyond the stated lower bound.

## Proof
Write \(f(t)\) for the coherence multiplier of the upper-right density-matrix entry. Conditioning on the history-reset mechanism gives the Volterra equation
\[
f'(t)=-(r+i)f(t)+\frac r t\int_0^t f(u)\,du,\qquad f(0)=1.
\]
Differentiation gives \(tf''+[1+(r+i)t]f'+if=0\), while the Volterra equation fixes \(f'(0)=-i\). The regular solution is the confluent hypergeometric function
\[
f(t)={}_1F_1\!\left(\frac{i}{r+i};1;-(r+i)t\right).
\]
This is the known exact solution of the uniform-history model [1], here also recovered from the scalar differential equation. For \(r=1/3\) its parameters are \(a=(9+3i)/10\), \(z_t=-(1/3+i)t\), and
\[
f(t)=\sum_{n=0}^\infty T_n(t),\quad T_0(t)=1,\quad
T_{n+1}(t)=T_n(t)\frac{(n+a)z_t}{(n+1)^2}.
\]
For all four tested times, \(|z_t|<17\) and \(|a|<1\). With \(P_{80}=\sum_{n=0}^{80}T_n\), the tail is bounded by
\[
|f(t)-P_{80}(t)|\le\varepsilon_t:=
\left(|\Re T_{80}|+|\Im T_{80}|\right)
\frac{17/81}{1-17/82}.
\]
Indeed the modulus of each successive-term ratio is at most \(17/(n+1)\) for \(n\ge80\). Every real and imaginary component of each \(T_n\), hence every bound on \(|P_{80}|^2\), is an *exact rational number*. In particular, setting
\[
E_t=2\left(|\Re P_{80}|+|\Im P_{80}|\right)\varepsilon_t+\varepsilon_t^2,
\]
one has \(|\,|f(t)|^2-|P_{80}(t)|^2\,|\le E_t\). Exact rational comparisons, reproduced by the included verifier, give
\[
\begin{aligned}
|f(15/2)|^2&<(19/500)^2,\\
|f(10)|^2&>(111/1000)^2,\\
|f(14)|^2&<(7/200)^2,\\
|f(16)|^2&>(9/200)^2.
\end{aligned}
\]
Under the channel, \(\rho_+(t)-\rho_-(t)\) has off-diagonal entries \(f(t)\) and its complex conjugate and vanishing diagonal entries. Its eigenvalues are \(\pm|f(t)|\), so \(D(t)=|f(t)|\). The two disjoint intervals \([15/2,10]\) and \([14,16]\) therefore contain positive trace-distance variation, of total size strictly larger than
\[
(111/1000-19/500)+(9/200-7/200)=83/1000.
\]
Analyticity of \(f\) and absolute continuity of \(|f|\) ensure positive-derivative subintervals. Positive trace-preserving intermediate maps contract the trace distance of any pair of states, so these increases disprove positive divisibility. Finally, the exact solution depends continuously on \(r>0\); strict inequalities persist in an open neighbourhood of \(r=1/3\).

## Verification
Run `python3 verify.py` with Python 3. The checker uses only exact `fractions.Fraction` arithmetic; no numerical special-function library or external data are needed. It computes the four rational partial sums, rational tail bounds, and the four strict squared-distance inequalities. A successful replay prints `PASS` and the stated backflow lower bound. Its finite calculation certifies four inequalities of an analytically defined entire function; it does not enumerate all revival intervals or optimize over all initial states.

## Relationship to prior work
De Mauro, Kulkarni and Majumdar [1] introduced this continuous-time uniform-history quantum-reset protocol and derived the exact hypergeometric coherence multiplier. Their qubit section concerns polarization relaxation and long-time algebraic/logarithmic oscillations; the exact multiplier and asymptotic decay are prior work, not claimed anew here. The present claim uses that multiplier to establish **two strict trace-distance revivals** and a **certified positive lower bound for operational information backflow**, which are not stated in that source. Carollo and Wald [2] study non-divisibility and state-distinguishability revival for a different, discrete-time family reset to a reference state, including generalized negative effective reset probabilities; their result does not yield the four inequalities for the positive-rate uniform-history model. Classical preferential-relocation limit theory [3] and previous exact operational-clock results likewise do not state these finite-time trace-distance inequalities. Exact hypergeometric formulas permit the signs to be computed in principle, so this claim is a new certified qualitative comparison, **not** an independently discovered channel solution.

## Limitations
The finding proves existence of at least two distinct information-backflow episodes for one physical rate and an open neighbourhood, not the complete rate phase diagram or the precise BLP supremum. The distinction from prior exact solutions is the rigorously certified sign pattern and its information-theoretic consequence; unpublished analyses or a more general hypergeometric modulus theorem might subsume it. No independent audit has been performed.

## References
1. G. de Mauro, M. Kulkarni and S. N. Majumdar, *Quantum resetting with memory*, arXiv:2608.02297v1, first submitted 3 August 2026, https://arxiv.org/abs/2608.02297 .
2. F. Carollo and S. Wald, *Stochastic resetting induces quantum non-Markovianity*, arXiv:2601.13367v1, 19 January 2026, https://arxiv.org/abs/2601.13367 .
3. C. Mailler and G. Uribe Bravo, *Random walks with preferential relocations and fading memory: a study through random recursive trees*, arXiv:1810.02735v1, 5 October 2018, https://arxiv.org/abs/1810.02735 .
