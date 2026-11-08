# Universal quadratic circular-cumulant cascade under a discrete Kuramoto phase kick

## Finding
Let an initial oscillator phase have the Poisson-kernel law \(P_a\), where \(|a|<1\), and let one deterministic kick be
\[
\theta' = \theta+\omega+\operatorname{Im}(H e^{-i\theta})\pmod{2\pi},
\qquad H\in\mathbb C,\quad \omega\in\mathbb R.
\]
Write \(M_m(H)=\mathbb E[e^{im\theta'}]\), with \(M_0=1\). Then, for every **fixed integer** \(m\ge 2\), as \(H\to0\),
\[
\boxed{M_m(H)-M_1(H)^m=
\frac{m}{8}(1-|a|^2)a^{m-2}e^{im\omega}H^2+O_m(|H|^3).}
\]
Define the exponential cumulants \(\mathcal K_m(H)=m![s^m]\log\bigl(\mathbb E[e^{s e^{i\theta'}}]\bigr)\). These differ by a factor \( (m-1)! \) from the convention \(m[s^m]\log F\) used in some circular-cumulant literature; nonvanishing is independent of this normalization. For the same fixed indices,
\[
\boxed{\mathcal K_m(H)=\frac{m(-1)^m}{8}(1-|a|^2)a^{m-2}e^{im\omega}H^2+O_m(|H|^3).}
\]
Consequently, when \(0<|a|<1\), all higher circular cumulants have **nonzero quadratic coefficients** in the same weak-kick limit. In particular, the exact second-moment deviation is
\[
M_2(H)-M_1(H)^2=\tfrac14(1-|a|^2)e^{2i\omega}H^2+O(|H|^3),
\]
so no nonzero sufficiently small kick preserves the Poisson-kernel (Ott–Antonsen) family, even on a single frequency fibre. This also applies to the self-consistent discrete Kuramoto update with \(H=KZe^{-i\beta}\), whenever \(Z\ne0\) and \(K\to0\).

## Assumptions and scope
The initial density is
\[
P_a(\theta)=\frac{1-|a|^2}{2\pi|e^{i\theta}-a|^2},\qquad |a|<1,\quad 0\le\theta<2\pi.
\]
The complex \(a\) and real \(\omega\) are held fixed while the complex kick \(H\) approaches zero along **any direction**. The asymptotic remainder is for each fixed moment or cumulant order; no bound uniform over all integer orders is asserted. The kick can be taken within \(|H|<1\) to ensure an orientation-preserving circle diffeomorphism. No assumption on the frequency distribution beyond the described conditional fibre enters the proof.

The original nonlinear discrete Kuramoto–Sakaguchi model uses \(H=KZe^{-i\beta}\), where \(Z\) is its complex order parameter and \(K>0\). Its phase lag \(\beta\) only rotates the nonzero quadratic obstruction by \(e^{-2i\beta}\). For a nonzero mean field, the second-cumulant obstruction holds on every conditional fibre with \(|a|<1\), for sufficiently small \(K>0\) at that fixed initial state. Frequency integration or long-time behavior is not assumed.

## Proof
Set \(W=e^{i\theta}\). Its Poisson-kernel moments are \(\mathbb E[W^k]=a^k\) and \(\mathbb E[W^{-k}]=\bar a^{\,k}\) for all integers \(k\ge0\). The kicked complex phase is exactly
\[
W'=e^{i\omega}W\exp\left(\tfrac12(HW^{-1}-\bar H W)\right).
\]
Because \(|W|=1\), Taylor expansion of the exponential has uniformly bounded remainders for each fixed moment order. For \(m\ge2\), integration of the quadratic Taylor polynomial gives
\[
\begin{aligned}
e^{-im\omega}M_m={}&a^m+\frac m2(Ha^{m-1}-\bar H a^{m+1})\\
&+\frac{m^2}{8}(H^2a^{m-2}-2|H|^2a^m+\bar H^2a^{m+2})+O_m(|H|^3).
\end{aligned}
\]
At the first moment, the sole negative power contributes the conjugate moment:
\[
\begin{aligned}
e^{-i\omega}M_1={}&a+\tfrac12(H-\bar H a^2)\\
&+\tfrac18(H^2\bar a-2|H|^2a+\bar H^2a^3)+O(|H|^3).
\end{aligned}
\]
Expand \(M_1^m\) by the binomial theorem. Terms of order zero and one cancel those of \(M_m\); the mixed term and the \(\bar H^2\) term cancel too. The remaining \(H^2\) coefficient is \(m(1-|a|^2)a^{m-2}/8\), proving the first boxed statement. This includes \(a=0\) with \(a^0=1\).

For the second boxed statement, let
\[
F_H(s)=\mathbb E[e^{sW'}]=\sum_{m=0}^\infty M_m(H)\frac{s^m}{m!},\qquad A=ae^{i\omega},\quad c=\frac{(1-|a|^2)H^2e^{2i\omega}}8.
\]
The proven moment deviations yield, for \(s\) on any fixed compact disk,
\[
F_H(s)-e^{sM_1(H)}
=c s^2\frac{e^{As}-1}{As}+O_s(|H|^3).
\]
The quotient is defined continuously at \(As=0\). This series summation is legitimate because the exponential Taylor estimates and the compact-\(s\) power series are absolutely convergent; alternatively differentiate only finitely many times at \(s=0\). As \(M_1(H)=A+O(|H|)\), the logarithm about \(s=0\) obeys
\[
\log F_H(s)-sM_1(H)=c s^2\frac{1-e^{-As}}{As}+O_s(|H|^3).
\]
Since \((1-e^{-As})/(As)=\sum_{j=0}^\infty(-1)^j(As)^j/(j+1)!\), the coefficient of \(s^m\), multiplied by \(m!\), is precisely \(m(-1)^mc A^{m-2}\). This establishes the full fixed-order cumulant formula.

Finally, for \(m=2\) the leading coefficient is nonzero whenever \(|a|<1\) and \(H\ne0\), so for each such \(a\) and any sufficiently small nonzero complex \(H\) the exact moment relation \(M_2=M_1^2\) is violated. At \(H=KZe^{-i\beta}\) and fixed \(Z\ne0\), the same conclusion holds as \(K\to0\); no phase lag can remove the nonzero modulus of the leading term.

## Verification
Execute \(\texttt{python3 verify.py}\) with the Python standard library. It independently reconstructs the quadratic moment coefficients with rational arithmetic, recursively reconstructs exponential cumulants without assuming their claimed coefficients, and checks both formulas at five rational Poisson parameters for indices two through twelve. It also integrates the exact nonlinear kicked phase by midpoint quadrature at complex Poisson parameters and complex kick directions. Expected output: \(\texttt{VERIFY\_OK}\) with counts of the exact and quadrature comparisons. The symbolic argument above, not the finite checks, proves the theorem for every fixed integer order.

## Relationship to prior work
Gade and Gupta [1] derive the exact discrete Kuramoto map and its linear incoherence threshold, and numerically observe failure of the Ott–Antonsen moment closure in their Section V. The **qualitative breakdown** is therefore prior work; the new assertion is its explicit single-step quadratic coefficient at every Fourier order and the resulting entire order-dependent cumulant profile. Gong, Toenjes and Pikovsky [2] show that their **different Möbius update** preserves Poisson kernels exactly, explaining why that result cannot imply closure for an additive sine kick. Goldobin and Dolmatova [3] establish the broad fact that a physically realizable non-Ott–Antonsen circular-cumulant sequence cannot terminate at finite nonzero order. That broad fact, and the use of circular cumulants, are not new; [3] does not present the displayed additive-kick-specific quadratic coefficient sequence. These are statement-level comparisons, not a claim of exhaustive historical priority.

## Limitations
This is a one-step local-in-kick calculation, not a time-uniform expansion, an invariant manifold construction, a nonlinear synchronization threshold, or a statement about finite particle-size fluctuations. Each asymptotic claim fixes the Fourier/cumulant order before taking the weak-field limit. At \(a=0\), only the second cumulant has a nonzero quadratic coefficient, so the all-orders simultaneous nonzero-coefficient statement requires \(0<|a|<1\). At \(|a|=1\), the Poisson density is not interior and the leading coefficient vanishes; this case is excluded. An independently checked priority assessment is outstanding.

## References
[1] P. M. Gade and S. Gupta, *Discrete-time Kuramoto model with phase lag: Linear stability analysis and onset of synchronization*, arXiv:2609.22715v1, first posted September 19, 2026, Sections II, III and V. https://arxiv.org/abs/2609.22715

[2] C. C. Gong, R. Toenjes and A. Pikovsky, *Coupled Möbius Maps as a Tool to Model Kuramoto Phase Synchronization*, arXiv:2001.07593, Appendix C. https://arxiv.org/abs/2001.07593

[3] D. S. Goldobin and A. V. Dolmatova, *Ott-Antonsen ansatz is the only admissible truncation of a circular cumulant series*, arXiv:1908.00230, Sections II and VI. https://arxiv.org/abs/1908.00230
