# A unique reset-rate optimum and resonant divergence for discrete-time qubit phase sensing

## Finding

**Theorem (stationary phase information under Bernoulli resets).** Prepare a qubit in \(\lvert+\rangle=(\lvert0\rangle+\lvert1\rangle)/\sqrt2\). At each discrete tick reset it to \(\lvert+\rangle\) with probability \(r\in(0,1)\); otherwise apply \(U_\theta=\exp(-i\theta\sigma_z/2)\). These choices are independent between ticks. Only a single qubit at stationarity is observed, without its reset-history record. For unknown gate angle \(\theta\in(0,\pi]\), let \(\mathcal F_\theta(r)\) be the symmetric-logarithmic-derivative quantum Fisher information of the resulting stationary density matrix for estimating \(\theta\), with \(r\) regarded as a known control.

Set \(q=1-r\), \(c=\cos\theta\), and \(\mathcal D=1-2qc+q^2\). Then
\[
\mathcal F_\theta(r)=\frac{q(1-q)^2(1+q)\big[(1+c)-(1+3c)q+2q^2\big]}{2\mathcal D^3}.
\]
For each fixed \(\theta\in(0,\pi]\), there is **exactly one** global maximizer \(r_*(\theta)\in(0,1)\). For \(0<\theta<\pi\), put \(u=\tan(\theta/2)>0\), \(w=u^2\), and \(t=r/(2-r)\). Its unique optimizer is \(r_*=2t_*/(1+t_*)\), where \(t_*\in(0,1)\) is the unique root of
\[
P_w(t)=2\big[t^5-(w+2)t^4-2wt^3+2w(w+1)t^2-3w^2t+w^2\big]=0.
\]
Near the gate resonance \(\theta\downarrow0\), the optimizer and maximal information obey the sharp limits
\[
\lim_{\theta\downarrow0}\frac{r_*(\theta)}{\theta}=\sqrt{\frac{1+\sqrt3}{2}},\qquad
\lim_{\theta\downarrow0}\theta^2\max_{0<r<1}\mathcal F_\theta(r)=\frac{2\sqrt3}{9}.
\]
At the opposite endpoint \(\theta=\pi\), the unique optimum is \(r_*=2/3\) and \(\max\mathcal F_\pi=1/64\). The optimum crosses \(r_*=2/3\) at the unique interior phase \(\theta=2\arctan(1/\sqrt2)\): it lies below \(2/3\) at smaller angles and above \(2/3\) at larger angles below \(\pi\).

## Assumptions and scope

The Hilbert space is \(\mathbb C^2\). Reset events replace the entire qubit state by the stated pure state; they do not merely projectively measure the qubit. One update is exactly one reset or one phase gate. Reset probability \(r\) is fixed independently of \(\theta\) when taking its statistical derivative. The stationary ensemble exists uniquely because \(r>0\), and phase information is assessed from its density operator alone (not from observing the reset clock, elapsed waiting time, or measurement records). Fisher information is expressed in units of inverse squared dimensionless gate angle. Results cover all \(\theta\in(0,\pi]\); symmetry gives the corresponding statements for \(\theta\in[\pi,2\pi)\) by replacing \(\theta\) by \(2\pi-\theta\). Exact resonances \(\theta\in2\pi\mathbb Z\) are excluded from the smooth full-rank calculation.

## Proof

**1. Stationary Bloch signal.** Write \(q=1-r\). The reset channel is \(\rho\mapsto r\lvert+\rangle\langle+\rvert+qU_\theta\rho U_\theta^\dagger\). As a trace-norm contraction on differences with factor \(q<1\), it has a unique stationary state. Its geometric-age representation is
\[
\rho_*(\theta,r)=r\sum_{n=0}^{\infty}q^nU_\theta^n\lvert+\rangle\langle+\rvert U_\theta^{-n}
=\frac12\begin{pmatrix}1&\overline{z}\\z&1\end{pmatrix},\qquad
z=\frac{r}{1-qe^{i\theta}}.
\]
For \(0<\theta\le\pi\), the state has full rank because \(1-|z|^2=2q(1-\cos\theta)/\mathcal D>0\).

**2. Quantum Fisher information.** The full-rank qubit Bloch formula is
\[
\mathcal F_\theta=|\partial_\theta z|^2+
\frac{[\operatorname{Re}(\overline z\partial_\theta z)]^2}{1-|z|^2}.
\]
Here \(\partial_\theta z=ir q e^{i\theta}/(1-qe^{i\theta})^2\), so \(|\partial_\theta z|^2=r^2q^2/\mathcal D^2\) and \(\operatorname{Re}(\overline z\partial_\theta z)=-r^2q\sin\theta/\mathcal D^2\). Therefore
\[
\mathcal F_\theta=\frac{r^2q^2}{\mathcal D^2}+
\frac{r^4q(1+\cos\theta)}{2\mathcal D^3},
\]
which simplifies to the displayed rational formula. This derivation is specific to estimating the gate phase, not the reset probability.

**3. Sharp uniqueness.** For \(0<\theta<\pi\), introduce \(u=\tan(\theta/2)\), \(w=u^2\), and \(t=(1-q)/(1+q)=r/(2-r)\). The information becomes
\[
\mathcal F_\theta=\frac{t^2(1-t)(1+w)^2[2t^2+w(1-t)]}{4(t^2+w)^3},\quad 0<t<1.
\]
Its derivative with respect to \(t\) is
\[
\partial_t\mathcal F_\theta=\frac{(1+w)^2tP_w(t)}{4(t^2+w)^4}.
\]
The positive change of variables \(x=t/(1-t)\) yields the polynomial identity
\[
(1+x)^5P_w\left(\frac{x}{1+x}\right)=2w^2+4w^2x+4wx^2-4w(w-2)x^3
-2(w^2-w+2)x^4-2(w+1)x^5.
\]
For every \(w>0\), its ascending-order coefficients have exactly one sign change: the first three are strictly positive, the last two strictly negative, and the fourth coefficient may have either sign or be zero. Descartes' rule of signs therefore allows **at most one** positive root, counted with multiplicity. The polynomial is positive at \(x=0\) and has negative leading coefficient, hence has exactly one positive root. The inverse transformation maps it bijectively to \(t\in(0,1)\). The derivative changes sign from positive to negative there, so this root is the unique global maximum. Endpoint information vanishes for \(w>0\).

**4. Resonant scaling and endpoint.** Put \(t=u y\) as \(u\downarrow0\). Dividing the polynomial identity by \(u^4\) (equivalently \(w^2\)) yields the nondegenerate leading equation \(-2y^4+2y^2+1=0\). For any two constants \(0<a_-<\sqrt{(1+\sqrt3)/2}<a_+\), evaluating \(P_w(a_\pm u)/u^4\) gives opposite signs for sufficiently small \(u>0\). By the already proved uniqueness, \(a_-u<t_*<a_+u\). Letting the constants approach the unique positive root yields \(t_*/u\to\sqrt{(1+\sqrt3)/2}\). Substituting the scaling into the exact information gives
\[
u^2\mathcal F_\theta(uy)=\frac{y^2(2y^2+1)}{4(1+y^2)^3}+o(1),
\]
whose unique maximum is \(\sqrt3/18\). Since \(\theta\sim2u\) and \(r=2t/(1+t)\), the two stated limits follow.

When \(\theta=\pi\), direct substitution yields \(\mathcal F_\pi=q^2(1-q)^2/(1+q)^4=t^2(1-t)^2/4\). Its unique optimum is \(t=1/2\), equivalent to \(r=2/3\), and its maximum is \(1/64\). For finite \(w\), \(P_w(1/2)=3(2w-1)/16\), which together with derivative uniqueness establishes the claimed crossover relative to \(r=2/3\).

## Verification

The accompanying executable `verify_qfi.py` uses exact symbolic algebra to check the phase/QFI transformations, the derivative polynomial and its positive-root polynomial, and the endpoint identities. Independently, it computes the symmetric logarithmic derivative directly from \(2\times2\) density matrices at 64 phase–reset pairs and compares its trace formula against the rational expression; it also verifies those stationary matrices against truncated geometric-age series. Further checks test root uniqueness at nine parameter points and the resonant scaling at three near-resonant points. On the recorded package, all 171 assertions/check groups passed. These finite checks are corroboration, not the proof of the universal claims; the global claims rest on the polynomial sign argument above.

To replay, run `python verify_qfi.py` with Python 3, NumPy and SymPy installed. No external files or paper text are required.

## Relationship to prior work

Wald, Yao, Platini, Hooley and Carollo (arXiv:2410.11497, first submitted 2024-10-15) give the discrete-time Bernoulli-reset stationary geometric mixture and identify gate-eigenphase resonances. Their paper does not present the stationary gate-phase quantum Fisher information or its globally optimal reset probability; the stationary-state expression alone does not state the quintic single-maximizer classification or the sharp phase-resonant information constant. Rose, Touchette, Lesanovsky and Garrahan (arXiv:1806.01298) derive general reset-resolvent stationary states for **continuous-time** quantum and classical dynamics; those results are not the discrete Bernoulli qubit optimization. Lambert and Sørensen (New J. Phys. 25, 081201, 2023) review the general quantum information geometry and metrological meaning of QFI. Li, Tong and Bao (arXiv:2610.31249, 2026) examine reset-enhanced dissipative metrology and give a general local reset-rate QFI response identity, in a different continuous-time open-system setting; this later work is a publication-priority comparison, not the motivating first-public source. None of the inspected statements directly supplies the exact global optimization classification here.

## Limitations

The Fisher information is for one stationary qubit snapshot per independent preparation, without accounting for the expected number of gate applications per preparation or other time and energy costs; therefore the near-resonant divergence is **not** a claim of unbounded information at fixed resource cost. A quantum Fisher bound is a local measurement-optimization quantity and does not imply a fixed, parameter-independent measurement attains it globally. The exactly resonant, rank-changing point \(\theta=0\) is excluded, and its QFI need not equal the limit from nonzero phases. The result covers ideal instantaneous complete resets, not partial resets, dephasing during gates, drifting reset probabilities or unknown reset rates. The global novelty comparison is best-knowledge and not a proof that an equivalent result is absent from all literature; the known geometric stationary state allows rederivation using standard qubit information geometry.

## References

1. S. Wald, L. H. Yao, T. Platini, C. Hooley, and F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497 (first submitted 2024-10-15), https://arxiv.org/abs/2410.11497. Section 2, especially equations (7) and (10); Section 5 and appendices.
2. D. C. Rose, H. Touchette, I. Lesanovsky, and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, Phys. Rev. E 98, 022129 (2018), arXiv:1806.01298, https://arxiv.org/abs/1806.01298.
3. J. Lambert and E. S. Sørensen, *From classical to quantum information geometry: a guide for physicists*, New J. Phys. 25, 081201 (2023), https://doi.org/10.1088/1367-2630/aceb14.
4. S. Li, Q. Tong, and R. Bao, *Reset-Enhanced Dissipative Quantum Metrology*, arXiv:2610.31249 (first submitted 2026-10-22), https://arxiv.org/abs/2610.31249. General comparison only; full text was not inspected.
