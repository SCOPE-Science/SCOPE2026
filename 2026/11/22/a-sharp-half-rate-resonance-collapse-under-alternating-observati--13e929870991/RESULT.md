# A sharp half-rate resonance collapse under alternating observation clocks

## Finding

**Theorem (exact two-phase clock classification).** For a structure-preserving constant-input leaky integrate-and-fire neuron with reset-to-threshold time \(T_c>0\), take the periodic opportunity set
\[
\mathcal T_{a,b}=\{kP,\ kP+a:k\in\mathbb Z\},\qquad P=a+b,\quad a,b>0.
\]
Let \(t_1\in\mathcal T_{a,b}\) be any firing time and define all subsequent firing times by the threshold-and-reset rule. Write uniquely
\[
T_c=qP+r,\qquad q\in\mathbb Z_{\ge0},\quad 0\le r<P.
\]
For every initial firing phase, the limiting physical-time firing frequency \(\nu=\lim_{n\to\infty}n/(t_n-t_1)\) exists, is independent of that phase, and equals
\[
\nu=\begin{cases}
1/(qP),&r=0\quad(q\ge1),\\[2pt]
2/((2q+1)P),&0<r\le\min\{a,b\},\\[2pt]
1/((q+1)P),&\min\{a,b\}<r<P.
\end{cases}
\]
The spike phases are periodic from the first spike or after at most one phase change. In the middle regime they alternate forever, with successive physical interspike intervals \(qP+a\) and \(qP+b\). In the last regime they are eventually confined to one of the two phases, with constant interspike interval \((q+1)P\). In particular, when \(T_c=P/2\), the exactly uniform clock \(a=b=P/2\) gives \(\nu=2/P\), while **every** nonzero alternating perturbation \(a\ne b\), however small, gives \(\nu=1/P\). This exact halving is discontinuous at zero clock jitter.

For fixed \(P\) and \(0<r\le P/2\), the high-frequency regime exists exactly on the closed parameter interval \(r\le a\le P-r\). Its complement has the lower frequency. Against the uniform clock with the same two opportunities per period, an alternating clock never has a higher asymptotic firing rate; its rate is strictly smaller exactly when \(\min\{a,b\}<r\le P/2\).

## Assumptions and scope

Fix \(\tau_m>0\), a reset voltage \(V_r\), threshold \(V_{th}\), and constant equilibrium voltage \(V_\infty>V_{th}>V_r\). Define the classical travel time
\[
T_c=\tau_m\log\!\left(\frac{V_\infty-V_r}{V_\infty-V_{th}}\right)>0.
\]
The subthreshold dynamics are the structure-preserving Hilger lift of the continuous membrane law, not a forward Euler transcription. Firing is allowed only at points of \(\mathcal T_{a,b}\), and each firing resets the voltage to \(V_r\) at that same point. There is no extra refractory interval, network coupling, noise, or time-varying drive. The theorem concerns all \(a,b,T_c>0\), both possible first-firing phases, and the asymptotic physical-time event frequency. The first firing time from an arbitrary subthreshold initial voltage is not part of the frequency formula.

## Proof

By the forward-projection firing theorem of Kaymakçalan and Selçuk, once a firing has occurred, the exact event recursion is
\[
t_{n+1}=\Pi_{\mathcal T_{a,b}}^+(t_n+T_c),\qquad \Pi_{\mathcal T}^+(u)=\min\{s\in\mathcal T:s\ge u\}.
\]
Set the two phases to \(0\) and \(a\) modulo \(P\). If \(r=0\), the next event is precisely \(qP\) later from either phase. Since \(T_c>0\), here \(q\ge1\), giving the first displayed case.

Suppose \(0<r<P\). The two possible forward projections are, for every integer \(k\),
\[
\begin{aligned}
t_n=kP&\implies t_{n+1}=\begin{cases}(k+q)P+a,&r\le a,\\(k+q+1)P,&r>a;\end{cases}\\
t_n=kP+a&\implies t_{n+1}=\begin{cases}(k+q+1)P,&r\le b,\\(k+q+1)P+a,&r>b.\end{cases}
\end{aligned}
\]
This calculation includes equality at the phase boundaries because the forward projection permits firing exactly at a threshold-crossing opportunity.

If \(r\le\min\{a,b\}\), both arrows switch phase. Two successive steps therefore return to the original phase after exactly \((2q+1)P\) physical time, with the two positive gaps \(qP+a\) and \(qP+b\). Hence the frequency is \(2/((2q+1)P)\). If \(r>\min\{a,b\}\), at least one phase maps to itself. The other phase either also maps to itself or reaches the absorbing phase in one step. Every self-phase step advances exactly \((q+1)P\), establishing the final formula and the finite transient assertion.

For comparison, the uniform grid of spacing \(P/2\) has event frequency
\[
\nu_{\mathrm{uniform}}=\frac{2}{P\lceil 2T_c/P\rceil}.
\]
For \(0<r\le P/2\), this is \(2/((2q+1)P)\), while for \(P/2<r<P\), it is \(1/((q+1)P)\); at \(r=0\), it equals \(1/(qP)\). Since \(\min\{a,b\}\le P/2\), comparison with the exact classification gives the claimed strict loss criterion and the closed high-frequency interval \(r\le a\le P-r\). Finally, if \(T_c=P/2\), this interval reduces to the single point \(a=b=P/2\), producing the asserted factor-two jump. Every conclusion follows for all parameters claimed. \(\square\)

## Verification

The included `checker.py` is dependency-free Python using exact rational arithmetic. Execute `python checker.py` to compare the formula and phase-transition period with the actual forward-projection recursion on \(125000\) rational parameter triples, checking both initial phases, plus resonance/boundary examples. These finite checks supplement the complete analytic two-state proof and are not used as a proof for arbitrary real parameters.

For an exact resonant witness, choose \(P=1\), \(T_c=1/2\). At \(a=b=1/2\), the fire times are spaced by \(1/2\). At \(a=51/100\), \(b=49/100\), the phases eventually lock to \(51/100\) modulo \(1\) and subsequent spikes occur every \(1\) time unit. The same half-rate conclusion holds for every \(a\ne1/2\), regardless of perturbation size.

## Relationship to prior work

Kaymakçalan and Selçuk (2026) establish the structure-preserving membrane dynamics and the arbitrary-time-scale forward-projection recurrence. They give an explicit rate formula for the uniform grid \(h\mathbb Z\) and explicitly identify arithmetic spike structure on periodic time scales as an unaddressed problem. The present result takes their recurrence as a premise, does not claim it, and resolves the minimal nonuniform periodic clock through a sharp complete phase diagram.

Rotter and Diesmann (1999) develop exact propagation on a regular numerical grid; that work provides relevant numerical context but does not imply the alternating-opportunity result. Pakdaman (2001) studies periodic *input forcing* and phase rotation numbers, a different mechanism from periodic availability of threshold events. The abstract and publication record were available, but the complete paper could not be compared; priority risk from specialized earlier results remains.

## Limitations

The result does not cover more than two observation opportunities per period, stochastic jitter, network interactions, non-constant input, or event-insertion semantics where threshold times are allowed between observation points. The rate cliff is for the on-time-scale reset convention, not for an exact event-driven simulation that inserts continuous crossing times. The first-firing transient is immaterial to the rate and is not classified. Novelty is supported by inspected literature and mathematical comparison, not an exhaustive claim of worldwide priority. No independent validation has been performed.

## References

1. B. Kaymakçalan and B. İ. Selçuk, *Structure-Preserving Leaky Integrate-and-Fire Dynamics on Arbitrary Time Scales*, arXiv:2611.17219v1, first public 2026-11-12. https://arxiv.org/html/2611.17219v1
2. S. Rotter and M. Diesmann, *Exact digital simulation of time-invariant linear systems with applications to neuronal modeling*, Biological Cybernetics **81** (1999), 381–402. https://doi.org/10.1007/s004220050570 ; lawful PDF https://brainworks.biologie.uni-freiburg.de/1999/journal%20papers/RotterDiesmann99.pdf
3. K. Pakdaman, *Periodically forced leaky integrate-and-fire model*, Physical Review E **63** (2001), 041907. https://doi.org/10.1103/PhysRevE.63.041907
4. B. A. Moser and M. Lunglmayr, *On Leaky-Integrate-and Fire as Spike-Train-Quantization Operator on Dirac-Superimposed Continuous-Time Signals*, arXiv:2402.07954 (2024). https://arxiv.org/abs/2402.07954
