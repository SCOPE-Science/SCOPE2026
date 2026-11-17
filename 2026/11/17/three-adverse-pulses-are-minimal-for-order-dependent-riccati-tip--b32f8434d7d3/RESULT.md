# Three adverse pulses are minimal for order-dependent Riccati tipping

## Finding
Consider a system that normally relaxes to a stable state, but experiences finitely many adverse environmental phases. For the Riccati flow \(\dot x=q(t)-x^2\), the relative timing of **two** such phases cannot change the eventual recovery-versus-escape decision if both orders remain finite through the forcing window. In contrast, **three** adverse phases suffice, even when every phase by itself is harmless and every forced segment remains finite. This gives a sharp minimum number of phases for post-exposure, order-dependent tipping in this model.

The observable is terminal basin membership, **not equality of terminal states**. The same pulse list can produce different terminal values even at length two.

## Assumptions and scope
Fix the unforced coefficient \(q=1\), the pre-exposure equilibrium \(x(0)=1\), and the scalar initial-value problem
\[
\dot x=q(t)-x^2.
\]
An adverse pulse with strength \(a>0\) and duration \(\tau>0\) means that \(q=-a^2\) for that duration. Outside the finite pulse window, \(q=1\). Pulse strengths and durations travel together when phases are reordered. Each solution is understood up to its first finite-time pole. We compare orders only when **both solutions exist as finite real functions through the full pulse window**. No smooth interpolation of the input is assumed; piecewise-constant coefficients are part of the model.

After forcing ends, \(q=1\); the exact basin threshold is \(x=-1\). A terminal state \(x>-1\) exists forever and tends to \(+1\), \(x=-1\) stays at the unstable equilibrium, and \(x<-1\) blows up to \(-\infty\) in finite additional time. "Tipping" in this result means the last alternative, specifically **post-exposure escape**; no claim is made about formal rate-induced tipping without frozen-system bifurcation.

## Proof
**1. Exact pulse propagation.** Write \(x=z'/z\) where \(z''=qz\), with initial \(z(0)=z'(0)=1\). For a phase \(q=-a^2\), the pair \((z',z)^{\mathsf T}\) evolves under
\[
M_a(\tau)=\begin{pmatrix}
\cos(a\tau)&-a\sin(a\tau)\\
\sin(a\tau)/a&\cos(a\tau)
\end{pmatrix}.
\]
The output is the first coordinate divided by the second coordinate of the propagated pair. If the Riccati trajectory is finite through the pulse sequence, then \(z\) has no zero there; since \(z(0)=1\), the terminal denominator \(z>0\). Thus the sign of the terminal quantity \(x+1\) is exactly the sign of the bilinear numerator
\[
N(M)=(1,1)M(1,1)^{\mathsf T}.
\]
This positivity requirement matters: the projective matrix product alone must not be used after a preceding Riccati pole.

**2. Two phases.** Let \(A=M_a(\tau_a)\), \(B=M_b(\tau_b)\), \(s_a=\sin(a\tau_a)\), and \(s_b=\sin(b\tau_b)\). Direct multiplication gives
\[
BA-AB=\frac{a^2-b^2}{ab}s_as_b
\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
Since \((1,1)\operatorname{diag}(1,-1)(1,1)^{\mathsf T}=0\), one has **exactly** \(N(BA)=N(AB)\). Whenever both pulse orders remain finite through exposure, both final denominators are positive. Hence both end on the same side of \(-1\), or both end exactly at \(-1\). One phase admits no nontrivial ordering, proving that three is a lower bound for order-dependent post-exposure outcomes in this domain.

**3. Three phases and strict chronology effect.** Append \(C=M_c(\tau_c)\). Using the same commutator,
\[
\begin{aligned}
N(CBA)-N(CAB)
&=\frac{a^2-b^2}{ab}\sin(a\tau_a)\sin(b\tau_b)\\
&\quad\cdot(c+c^{-1})\sin(c\tau_c).
\end{aligned}
\]
The factor for the third phase generally fails to annihilate the diagonal commutator. In particular, it is strictly positive when \(a>b>0\) and all three pulse angles lie in \((0,\pi/2)\).

For a fully exact example choose \(a=2\), \(b=1/2\), \(c=1\) and
\[
\tau_a=\frac12\arctan\frac12,\qquad
\tau_b=2\arctan\frac12,\qquad
\tau_c=\arctan\frac12.
\]
Because all cosines are positive and all three tangents are \(1/2\), each transfer map reduces to the rational Möbius map
\[
R_a(x)=\frac{x-a/2}{1+x/(2a)}.
\]
Every displayed denominator below is positive. The two histories are
\[
1\xrightarrow{A}0\xrightarrow{B}-\frac14\xrightarrow{C}-\frac67>-1,
\]
\[
1\xrightarrow{B}\frac38\xrightarrow{A}-\frac47\xrightarrow{C}-\frac32<-1.
\]
Moreover the one-phase terminal values are \(0,3/8,1/3\), all greater than \(-1\). Each forced trajectory is strictly decreasing during its phase because \(\dot x=-a^2-x^2<0\), and positivity of the listed transfer denominators ensures no pole inside any phase (the phase angles all lie between zero and \(\pi/2\), and the scalar linearized solution cannot cross zero and return to positive in such a phase). The strict final inequalities and continuous dependence of finite-time solutions provide an open parameter neighborhood with the same contrasting outcomes. After the first history, the equation \(\dot x=1-x^2\) converges to \(+1\); after the second it diverges to \(-\infty\) in finite time. Thus three phases attain the proven lower bound.

## Verification
The standalone Python 3 script `check_riccati_pulses.py` uses exact rational arithmetic only. It checks 144 two-phase algebraic identities, 729 three-phase numerator identities, the exact terminal-state witness, and the individual pulse values. Its expected terminal line is `RICCATI_PULSE_EXACT_OK two_phase=144 triple_identity=729 three_phase_witness=1`. The script does **not** prove the universal result; that follows from the displayed symbolic matrix identity and the positivity argument. The analytic argument requires neither numerical integration nor an extrapolation from finite tests.

## Relationship to prior work
The broader threshold problem is motivated by Wieczorek, Xie, and Ashwin's framework for tipping, thresholds and edge states, and the scalar quadratic nonautonomous analysis of Longo, Núñez, Obaya, and Rasmussen. Their results do not, as inspected, state this exact two-phase chronological invariance plus a sharp three-phase reversal for finite adverse constant pulses. General Riccati/projective transfer representations are standard mathematical tools, not claimed as new here. The specific contribution is their structurally exact terminal-threshold cancellation and minimal pulse-count consequence. The definition here explicitly concerns temporary crossing of a frozen saddle-node regime, not tipping without a frozen-system bifurcation.

## Limitations
This is a scalar model with normal coefficient \(q=1\), negative constant pulse coefficients, and initial state \(+1\). The two-phase impossibility assumes both reordered solutions stay finite throughout the forced window; no ordering claim is made for configurations with blow-up **during** a pulse. The exact transfer method is specific to Riccati dynamics, not to general nonlinear population models. The sharp minimality statement applies to the specified terminal recovery/escape classification, not the transient trajectories themselves. The result is a self-review and has not undergone independent audit. Equivalent results in unindexed Riccati/SL(2) literature cannot be excluded completely.

## References
- S. Wieczorek, C. Xie, P. Ashwin, *Rate-Induced Tipping: Thresholds, Edge States and Connecting Orbits*, arXiv:2111.15497, first submitted 2021-11-30, https://arxiv.org/abs/2111.15497.
- I. P. Longo, C. Núñez, R. Obaya, M. Rasmussen, *Rate-induced tipping and saddle-node bifurcation for a class of quadratic differential equations with nonautonomous asymptotic dynamics*, arXiv:2110.02608, https://arxiv.org/abs/2110.02608, and SIAM J. Appl. Dyn. Syst. 20 (2021), 500–540, DOI:10.1137/20M1339003.
