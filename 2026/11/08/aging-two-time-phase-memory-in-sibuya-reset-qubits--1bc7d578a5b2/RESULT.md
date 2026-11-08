# Aging two-time phase memory in Sibuya-reset qubits

## Finding

An age-dependent reset qubit can lose all ensemble one-time transverse coherence yet retain order-one, phase-locked, trajectory-level coherence between observations separated by a fraction of the sample age. Fix \(0<\gamma<1\), a gate \(U=e^{-i\theta\sigma_z/2}\) with \(z=e^{i\theta}\ne1\), and reset to \(|+\rangle=(|0\rangle+|1\rangle)/\sqrt2\). If \(Q_t=z^{A_t}\) is the complex transverse Bloch phase along the reset trajectory, and if integers \(k_t/t\to u\in(0,\infty)\), then
\[
 z^{-k_t}\mathbb E[Q_{t+k_t}\overline{Q_t}]
 \longrightarrow H_\gamma(u)=I_{1/(1+u)}(\gamma,1-\gamma)
 =\frac{\sin(\pi\gamma)}{\pi}\int_0^{1/(1+u)}s^{\gamma-1}(1-s)^{-\gamma}\,ds.
\]
Here \(I_x(a,b)\) denotes the regularized incomplete Beta function. In particular \(H_{1/2}(1)=1/2\), so macroscopic-lag phase memory is nonzero. Meanwhile \(\mathbb E Q_t\to0\). For every fixed integer \(k\ge1\), the undemodulated correlation tends to \(z^k\).

## Assumptions and scope

Time is discrete and starts at \(t=0\) in the reset state. After \(a\) consecutive unitary steps, the next operation is a reset occupying that step with probability \(r_a=\gamma/(a+1)\), and otherwise a gate occupying that step. All such choices are conditionally independent given the elapsed-age state. A reset sets the state to \(|+\rangle\) and the age to zero, whereas a gate increments the age. The reset intervals are independent with the same Sibuya distribution. The qubit's trajectory-level signal is the expectation of \(\sigma_x+i\sigma_y\) in its pure state on each realized reset/gate history, not the result of two invasive measurements on one quantum copy.

Write \(A_t\in\{0,\ldots,t\}\) for the age and \(Q_t=\langle\sigma_x\rangle_t+i\langle\sigma_y\rangle_t=z^{A_t}\). The \(\mathbb E\) averages *classical reset histories*. The claim fixes \(\gamma,z\) while \(t\to\infty\). The frequency \(z\) may be any nontrivial unit complex number, including a nontrivial root of unity. The phase correction \(z^{-k_t}\) is necessary because \(z^{k_t}\) need not converge.

## Proof

**1. Explicit renewal probabilities.** Define the rising factorial \((a)_0=1\) and \((a)_n=\prod_{j=0}^{n-1}(a+j)\) for integer \(n\ge1\). If \(L\) is the number of operations between consecutive resets, its survival probabilities and masses are
\[
 s_n=\Pr(L>n)=\frac{(1-\gamma)_n}{n!},\qquad
 p_j=\Pr(L=j)=\frac{\gamma(1-\gamma)_{j-1}}{j!}\quad(j\ge1).
\]
The probability-generating function of \(p_j\) is \(1-(1-w)^\gamma\). The renewal-event probability \(v_n\) (with \(v_0=1\)) therefore has generating function \((1-w)^{-\gamma}\), giving \(v_n=(\gamma)_n/n!\). Consequently
\[
 \Pr(A_t=a)=v_{t-a}s_a,\qquad 0\le a\le t.
\]
The equalities are identities of nonnegative probabilities, so the age mass sums to one.

**2. One-time coherence vanishes.** Set \(m_n(z)=\mathbb E Q_n=\sum_{a=0}^n v_{n-a}s_a z^a\). Denote the nonnegative summand coefficient by \(b_{n,a}=v_{n-a}s_a\). For \(0\le a<n\),
\[
 \frac{b_{n,a+1}}{b_{n,a}}=
 \frac{(n-a)(a+1-\gamma)}{(n-a-1+\gamma)(a+1)}.
\]
Its difference from one has the sign of \(a+1-\gamma(n+1)\). Thus the coefficient sequence first decreases and then increases, with total variation at most \(2(v_n+s_n)\). Since \(z\ne1\), the geometric partial sums \(\sum_{a=0}^jz^a\) are bounded by \(2/|1-z|\). Discrete summation by parts shows
\[
 |m_n(z)|\le\frac{C}{|1-z|}(v_n+s_n)
 =O_z(n^{\gamma-1}+n^{-\gamma})\longrightarrow0.
\]
This also implies \(\sup_{n\ge\delta t}|m_n(z)|\to0\) for each fixed \(\delta>0\).

**3. Exact two-time decomposition.** Let \(C_{t,k}=\mathbb E[Q_{t+k}\overline{Q_t}]\) for integers \(t\ge0,k\ge1\). Histories without any reset between times \(t\) and \(t+k\) contribute \(z^kH_{t,k}\), where
\[
 H_{t,k}=\sum_{a=0}^t v_{t-a}s_{a+k}
 =\Pr(\text{no reset at times }t+1,\dots,t+k).
\]
If the *first* reset after \(t\) occurs at step \(t+j\), then before that reset the age was \(a\), its joint probability is \(v_{t-a}p_{a+j}\), and subsequent reset/gate dynamics from that reset has mean coherence \(m_{k-j}(z)\). Therefore the exact identity is
\[
 C_{t,k}=z^kH_{t,k}
 +\sum_{a=0}^t v_{t-a}\bar z^{a}
 \sum_{j=1}^k p_{a+j}\,m_{k-j}(z).
 \tag{1}
\]
This conditional-first-reset formula also holds at finite \(t,k\), without approximations.

**4. Macroscopic persistence.** The standard Gamma-ratio asymptotics yield
\[
 v_n\sim\frac{n^{\gamma-1}}{\Gamma(\gamma)},\qquad
 s_n\sim\frac{n^{-\gamma}}{\Gamma(1-\gamma)}.
\]
For \(k_t/t\to u>0\), the sum for \(H_{t,k_t}\) is a Riemann sum; its endpoint singularity at \(a=t\) is integrable because \(\gamma>0\). More formally, for \(\eta>0\), ordinary uniform Gamma-ratio bounds handle \(a/t\le1-\eta\), while the upper block \(a/t\ge1-\eta\) contributes at most \(C\eta^{\gamma}\). Thus
\[
 H_{t,k_t}\longrightarrow
 \frac1{\Gamma(\gamma)\Gamma(1-\gamma)}
 \int_0^1(1-x)^{\gamma-1}(x+u)^{-\gamma}\,dx.
\]
Substitution \(s=(1-x)/(1+u)\) and Euler's reflection formula transform this into \(H_\gamma(u)\) displayed in the finding.

**5. Every path containing a reset has negligible residual phase.** Let \(R_{t,k}\) denote the double sum in (1). Fix \(0<\delta<u\). For first-reset steps \(j\le k-\lfloor\delta t\rfloor\), the modulus of their total contribution is at most \(\sup_{n\ge\lfloor\delta t\rfloor}|m_n(z)|\to0\). For the remaining first-reset times, the total probability is
\[
 H_{t,k-\lfloor\delta t\rfloor}-H_{t,k},
\]
which tends to \(H_\gamma(u-\delta)-H_\gamma(u)\). By continuity of the displayed incomplete Beta integral, this tends to zero as \(\delta\downarrow0\). Hence \(R_{t,k_t}\to0\). Multiplication of (1) by \(z^{-k_t}\), of modulus one, gives the theorem.

**6. Fixed lags.** For fixed \(k\), any reset between \(t+1\) and \(t+k\) is contained in the union of the events of a renewal at those times. Its probability is bounded by \(\sum_{j=1}^k v_{t+j}\to0\). Therefore the finite-lag product equals \(z^k\) with probability tending to one, and its expectation tends to \(z^k\).

## Verification

The accompanying `code/verify_aging_phase.py` independently computes small-horizon two-time correlations by an age Markov chain, compares them with the renewal decomposition (1), checks renewal normalization, and evaluates the predicted Beta persistence at larger finite horizons. It passed 1147 deterministic numerical assertions. These checks test normalizations and finite-time identities; they do not certify infinite-time asymptotics, which are proved above. Execute with `python -B code/verify_aging_phase.py` in an environment containing NumPy and SciPy.

## Relationship to prior work

Wald, Yao, Platini, Hooley and Carollo (2024) introduce precisely the age-dependent discrete-time reset protocol and study single-time stationary-state behavior and spatial/particle correlators; their non-Poissonian section does not state a two-time trajectory-phase aging formula. The later renewal-quantum-resetting classification (2026) develops Sibuya **one-time** coherence asymptotics and near-resonant scaling, not the present two-time macroscopic-lag correlation. Classical aged-renewal and generalized-arcsine results account for the persistence function, but a no-renewal event by itself does not determine the complete complex phase correlation: the vanishing of the first-reset contribution in (1) is essential. Allegrini and collaborators (2004) study the different two-state renewal telegraph observable that is piecewise constant between events. The contribution here is the exact quantum Bloch-phase two-time law, including cancellation of every reset-containing path and the contrast with one-time coherence.

## Limitations

The result applies to a complete-reset qubit with the exact Sibuya hazard, a fixed nonresonant phase, and trajectory-resolved noninvasive signal reconstruction. It does not establish a sequential-measurement quantum regression formula, generalize to arbitrary age hazards, control phase frequencies approaching one with time, or furnish a uniform finite-sample error. The incomplete Beta persistence is rooted in classical renewal theory, and wider literature may contain an equivalent general phase-observable specialization not found in the comparisons. The 2026 classification's detailed full manuscript was not available for full-text inspection; the accessible technical account explicitly discussed one-time coherences and left multi-time correlations beyond its stated results.

## References

1. S. Wald, L. H. Yao, T. Platini, C. Hooley and F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, first public preprint 2024-10-15, https://arxiv.org/abs/2410.11497 .
2. *Renewal resetting of quantum dynamics: a classification for complete resets, a reduction for jump channels, and critical time scales*, 2026, DOI 10.5281/zenodo.23580221, accessible specialist technical account at https://www.evidencepress.org/releases/renewal-quantum-resetting-equilibration/ .
3. P. Allegrini, G. Aquino, P. Grigolini, L. Palatella, A. Rosa and B. J. West, *Correlation function and generalized master equation of arbitrary age* (2004), https://arxiv.org/abs/cond-mat/0409600 .
4. *Universal behaviors of the multi-time correlation functions of random processes with renewal: the step noise case (the random velocity of a Lévy walk)* (2025), https://arxiv.org/abs/2510.11747 .
