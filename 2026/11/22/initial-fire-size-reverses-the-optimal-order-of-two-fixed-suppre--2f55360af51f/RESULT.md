# Initial fire size reverses the optimal order of two fixed suppression episodes

## Finding
For a finite-capacity continuous-time birth–death–suppression process with states \(0,1,2\), state \(0\) absorbing, consider two prescribed suppression intensities \(h>\ell\geq0\) and their respective positive durations \(u,v\). Compare schedule \(HL\) (intensity \(h\) for duration \(u\), followed by intensity \(\ell\) for duration \(v\)) with \(LH\) (the same two episodes in reverse order). For an initial probability \(\alpha\) of state \(1\) and \(1-\alpha\) of state \(2\), write \(E_{HL}\) and \(E_{LH}\) for the probabilities of extinction by the common final time \(u+v\).

Let \(\lambda>0\) be the transition rate \(1\to2\), \(m>0\) the natural rate \(1\to0\), and \(d>0\) the natural rate \(2\to1\). The suppression intensity \(s\) adds the **same absolute rate** \(s\) to each downward transition; there are no upward transitions from state \(2\). Then, for a strictly positive explicit factor \(K\),

\[
E_{HL}-E_{LH}=K\bigl[\alpha\lambda-(1-\alpha)(d-m)\bigr].
\]

Consequently, if \(d>m\), the two orders tie **for every** \(h,\ell,u,v\) exactly at
\[
\alpha_* = \frac{d-m}{d-m+\lambda},
\]
and \(HL\) gives greater extinction probability for \(\alpha>\alpha_*\), whereas \(LH\) does for \(\alpha<\alpha_*\). If \(d=m\), \(HL\) is better for every \(\alpha>0\) and ties when \(\alpha=0\); if \(d<m\), \(HL\) is better for every \(\alpha\in[0,1]\). In the natural per-unit loss case \(d=2m\), the sharp initial-mixture boundary is \(\alpha_*=m/(m+\lambda)\). Thus, starting with **one** active site favors strong suppression first, while starting with **two** favors it last, at every pair of positive episode durations.

The two-active-site capacity is minimal for this phenomenon: with a single active state and the same additive suppression hazard, the extinction probability depends only on the integrated intensity and never on its chronological order.

## Assumptions and scope
- Time is continuous; \(0\) is absorbing and \(1,2\) are the only transient states. No re-ignition is permitted after state \(0\).
- The only upward transition is \(1\to2\) at rate \(\lambda>0\). At state \(2\), additional births are excluded by a hard two-active-site capacity.
- Natural downward rates are \(m>0\) from \(1\) and \(d>0\) from \(2\). A suppression rate \(s\geq0\) is added equally to both *total downward intensities*, rather than per active unit.
- For both schedules the same two intensities \(h>\ell\geq0\) are used for the same respective durations \(u,v>0\). Only the ordering changes. The initial distribution, including \(\alpha\in[0,1]\), is the same.
- The endpoint metric is extinction by time \(u+v\), not final burn footprint, expected total spread, or indefinite-horizon eventual extinction.

## Proof
Use row-vector probabilities on transient states \(1,2\). The transient subgenerator during a constant suppression interval of intensity \(s\) is
\[
Q_s=\begin{pmatrix}-(\lambda+m+s)&\lambda\\ d+s&-(d+s)\end{pmatrix}.
\]
The two remaining-active probabilities are \(S_{HL}=p^\top e^{uQ_h}e^{vQ_\ell}\mathbf 1\) and \(S_{LH}=p^\top e^{vQ_\ell}e^{uQ_h}\mathbf 1\), where \(p^\top=(\alpha,1-\alpha)\) and \(\mathbf 1=(1,1)^\top\). Extinction probabilities are \(E_{HL}=1-S_{HL}\), \(E_{LH}=1-S_{LH}\).

For every real \(2\times2\) matrix \(Q_s\), Cayley–Hamilton gives \(e^{tQ_s}=a_s(t)I+b_s(t)Q_s\). Here the two eigenvalues are real and distinct, because the discriminant is
\[
\Delta_s^2=(\lambda+m-d)^2+4\lambda(d+s)>0.
\]
Writing \(r_\pm(s)=-(\lambda+m+d+2s)/2\pm\Delta_s/2\), the coefficient is
\[
b_s(t)=\frac{e^{r_+(s)t}-e^{r_-(s)t}}{\Delta_s}>0\qquad(t>0).
\]
The scalar-plus-generator representation yields the *exact* matrix-exponential swap identity
\[
e^{uQ_h}e^{vQ_\ell}-e^{vQ_\ell}e^{uQ_h}
=b_h(u)b_\ell(v)[Q_h,Q_\ell].
\]
Direct matrix multiplication, with \([Q_h,Q_\ell]=Q_hQ_\ell-Q_\ell Q_h\), gives
\[
[Q_h,Q_\ell]=(h-\ell)
\begin{pmatrix}-\lambda&0\\d-\lambda-m&\lambda\end{pmatrix}.
\]
In particular,
\[
[Q_h,Q_\ell]\mathbf1=(h-\ell)
\begin{pmatrix}-\lambda\\d-m\end{pmatrix}.
\]
Therefore
\[
S_{HL}-S_{LH}=(h-\ell)b_h(u)b_\ell(v)
\bigl[-\alpha\lambda+(1-\alpha)(d-m)\bigr].
\]
Negating this identity proves the displayed extinction-difference formula with
\[
K=(h-\ell)b_h(u)b_\ell(v)>0.
\]
Its bracket is affine and strictly increasing in \(\alpha\) whenever \(d\geq m\), and all the stated sign, equality and threshold cases follow directly; if \(d<m\), both terms in the bracket are nonpositive and at least one is negative for every \(\alpha\in[0,1]\).

When the capacity is only one active state, the transient subgenerator is the scalar \(-(m+s)\); both orders yield the same survival \(\exp[-m(u+v)-hu-\ell v]\), proving minimality under this class of models.

## Verification
The accompanying standalone `verify.py` checks the symbolic commutator and its projection on the survival vector; the discriminant identity; and 1,800 independently generated strictly positive-rate and positive-duration parameter sets using matrix exponentials and the analytic positive-factor formula. These checks test the implementation, not the infinite quantifiers proved above.

An exact parameter witness is \(\lambda=m=1\), \(d=2\), \(h=3\), \(\ell=0\), \(u=v=1\). The initial-state-conditioned survival differences are approximately \(-0.007741914776\) (initial state \(1\)) and \(+0.007741914776\) (initial state \(2\)); the exact symmetry of their signs follows from the proven formula, independently of numerical rounding. In this witness the mixture boundary is exactly \(\alpha_*=1/2\). Run `python verify.py` with NumPy, SciPy and SymPy installed to reproduce the diagnostics.

## Relationship to prior work
Hulsey, Alderson and Carlson (2023) formulate a birth–death–suppression model motivated by wildfire dynamics, with natural loss proportional to active firelets and suppression of fixed absolute intensity. Their work derives population and footprint distributions, principally for constant suppression. The later Hulsey–Alderson–Carlson study (2025) examines time-dependent resource allocations numerically, including finite-time nonabsorption and cumulative-footprint risk. Those analyses motivate the exact timing comparison here; they do **not** provide the two-active-site, same-exposure, all-duration initial-state switching identity in their inspected statements and relevant sections.

Ross and Pollett (2006) analyze a two-phase, state-triggered birth–death culling process, including discussion of finite population ceilings and constant culling effort. Their phase variable changes upon crossing *population thresholds*, rather than by swapping two externally fixed calendar episodes. Generic Cayley–Hamilton and finite-state Markov semigroup facts are used here as established mathematics; novelty is not claimed for those tools. The contribution assessed here is the size-conditioned, complete chronological ranking in this specific capped suppression model, including the sharp mixture boundary and minimality.

## Limitations
The model has a hard capacity of two burning units, no re-ignition after extinction, exponential transition clocks, fixed equal-additive suppression at each positive state, and prescribed nonadaptive periods. It is not a calibrated wildfire model. It does not claim that delayed suppression lowers the *burned footprint*, nor that delay is advisable in actual fire response. The finite-capacity case is intentionally a rigorous boundary example for finite-deadline extinction probability. Historical priority is provisional pending broader expert literature assessment.

## References
1. G. Hulsey, D. L. Alderson, J. Carlson, *Birth-death-suppression Markov process and wildfires*, arXiv:2307.11726 (first public version July 21, 2023), https://arxiv.org/abs/2307.11726; later *Physical Review E* **109**, 014110 (2024), https://doi.org/10.1103/PhysRevE.109.014110.
2. G. Hulsey, D. L. Alderson, J. Carlson, *Forecasting and decisions in the birth-death-suppression Markov model for wildfires*, *Physical Review E* **111**, 024318 (2025), https://doi.org/10.1103/PhysRevE.111.024318; author-hosted full text https://faculty.nps.edu/dlalders/docs/PhysRevE.111.024318.pdf.
3. J. V. Ross, P. K. Pollett, *Extinction times for a birth-death process with two phases*, *Mathematical Biosciences* **202** (2006), 310–322, https://doi.org/10.1016/j.mbs.2006.02.004; author-hosted manuscript https://people.smp.uq.edu.au/PhilipPollett/papers/BDP2/BDP2.pdf.
