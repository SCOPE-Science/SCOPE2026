# Exactly two optimal Poisson interrogation rates on a chiral quantum triangle

## Finding

An ideal projective search on a three-vertex chiral quantum ring, with explicit re-preparation after each failed probe, has **two distinct and exactly equally optimal positive Poisson interrogation rates**. Reversing the magnetic circulation while leaving the preparation site and detector fixed produces instead exactly one global optimum. The degeneracy is exact, rather than a numerical coincidence.

Take unit hopping strength and define the positive probe rate \(r\). For the orientation specified below, the probability of detecting the target in one independently prepared exponential-duration attempt is
\[
p_+(r)=\frac{2(r^2-3r+6)}{(r^2+3)(r^2+12)}.
\]
The first-success mean time is \(T_+(r)=1/[r p_+(r)]\). Its **only** global minimizers are
\[
\boxed{r_\pm=\frac{3+2\sqrt3\ \pm\sqrt{12\sqrt3-3}}2},\qquad
\boxed{T_+(r_\pm)=3+2\sqrt3}.
\]
Numerically, \(r_-\approx1.1234606571\) and \(r_+\approx5.3406409581\). The two optimal rates have the simple exact product \(r_-r_+=6\).

Under reversed magnetic circulation,
\[
p_-(r)=\frac{2(r^2+3r+6)}{(r^2+3)(r^2+12)},
\]
and the unique global optimum is
\[
\boxed{r=\sqrt6},\qquad
\boxed{T_-(\sqrt6)=\frac{27}{6+4\sqrt6}}.
\]
These claims concern the same three-site device, source, target and cost criterion; only the complex hopping orientation is reversed.

## Assumptions and scope

The Hilbert space is \(\mathbb C^3\), in the ordered orthonormal site basis \(|0\rangle,|1\rangle,|2\rangle\). In units with \(\hbar=1\) and hopping magnitude one, choose
\[
H_+=\begin{pmatrix}0&-i&-1\\i&0&1\\-1&1&0\end{pmatrix},\qquad H_-=\overline{H_+}.
\]
Both are Hermitian. The cyclic product of the three hopping entries is nonreal, so the hopping has nontrivial magnetic circulation. The particle starts in \(|0\rangle\) and is detected by the ideal binary projector \(P=|2\rangle\langle2|\), with failure projector \(I-P\).

For each attempt, draw \(\tau\) independently with density \(r e^{-r\tau}\) for \(\tau>0\). Unitary evolution under the selected, time-independent Hamiltonian runs until the probe at time \(\tau\). On a successful probe stop. After a failure, **actively re-prepare the exact state \(|0\rangle\)**, independently of the post-measurement no-click state, at zero time cost; draw a fresh interval and repeat. These explicit resets are a physical assumption and must not be confused with the measurement-only protocol that lets the projected failure state evolve.

All waiting intervals are independent and identically distributed, quantum evolution is coherent between probes, detector success is perfect, resetting has no time or resource overhead, and the objective is expected total physical time to the first successful probe. The theorem does not assert experimental realizability of the zero-overhead re-preparation assumption. For hopping magnitude \(J>0\), the displayed rates multiply by \(J\) and displayed mean times divide by \(J\).

## Proof

**1. Exact transition amplitude.** Direct matrix multiplication gives \(H_+^3=3H_+\), \((H_+)_{20}=-1\), and \((H_+^2)_{20}=i\). Therefore
\[
e^{-iH_+t}=I-i\frac{\sin(\sqrt3t)}{\sqrt3}H_+
+\frac{\cos(\sqrt3t)-1}{3}H_+^2
\]
and hence
\[
\langle2|e^{-iH_+t}|0\rangle
=i\left[\frac{\sin(\sqrt3t)}{\sqrt3}+\frac{\cos(\sqrt3t)-1}{3}\right].
\]
Conjugating the hopping matrix flips the sign of the mixed sine–cosine contribution to the transition probability; its purely even terms are unchanged.

**2. Poisson-averaged success probability.** The success probability of one attempt is the integral
\[
p_\pm(r)=r\int_0^\infty e^{-rt}\bigl|\langle2|e^{-iH_\pm t}|0\rangle\bigr|^2dt.
\]
Expand the square of the preceding two-frequency amplitude. The elementary Laplace identities
\[
r\int_0^\infty e^{-rt}\cos(\omega t)dt=\frac{r^2}{r^2+\omega^2},\qquad
r\int_0^\infty e^{-rt}\sin(\omega t)dt=\frac{r\omega}{r^2+\omega^2}
\]
for \(\omega=\sqrt3,2\sqrt3\) yield precisely the two rational formulas for \(p_+(r)\) and \(p_-(r)\) stated above. They are strictly between zero and one at every positive rate; in particular, each attempt has a positive success probability.

**3. Renewal reduction.** Let \(T\) be the elapsed time until first success. By restarting both the state and the waiting clock after every failure, every trial is independent and statistically identical. The expected duration of one trial is \(1/r\). Conditioning on its success indicator gives the exact renewal identity
\[
\mathbb ET=\frac1r+(1-p_\pm(r))\mathbb ET,
\qquad\text{so}\qquad \mathbb ET=\frac{1}{rp_\pm(r)}.
\]
The identity does not assume independence between success and trial duration; only the fresh trial after a failure is independent.

**4. Two and only two globally minimizing forward rates.** Define \(Q_+(r)=r p_+(r)\), \(c=2/\sqrt3-1>0\), and \(s=3+2\sqrt3\). An exact factorization, valid for every \(r>0\), is
\[
\boxed{c-Q_+(r)=
\frac{c\bigl(r^2-sr+6\bigr)^2}{(r^2+3)(r^2+12)}\ge0.}
\]
The quadratic has exactly the two distinct positive roots
\[
r_\pm=\frac{s\pm\sqrt{s^2-24}}2
=\frac{3+2\sqrt3\pm\sqrt{12\sqrt3-3}}2.
\]
Equality in the displayed bound holds only at these two roots. Thus they are the complete set of global maximizers of \(Q_+\), equivalently the complete set of global minimizers of \(T_+=1/Q_+\). Since \(c^{-1}=3+2\sqrt3\), the forward minimum is as claimed. Also \(Q_+(r)\to0\) at both endpoints \(r\downarrow0\) and \(r\uparrow\infty\), confirming that no boundary optimum is overlooked.

**5. Uniqueness under flux reversal.** Define \(Q_-(r)=r p_-(r)\). Direct differentiation and exact factorization yield
\[
Q_-'(r)=
-\frac{2(r^2-6)(r^4+6r^3+9r^2+36r+36)}{(r^2+3)^2(r^2+12)^2}.
\]
Every coefficient of the quartic in the numerator is positive, so the quartic is strictly positive for \(r>0\). Therefore \(Q_-\) strictly increases for \(0<r<\sqrt6\), strictly decreases for \(r>\sqrt6\), and has its unique global maximum at \(\sqrt6\). Substitution gives \(Q_-(\sqrt6)=(6+4\sqrt6)/27\); taking the reciprocal proves the reverse minimum time.

## Verification

Run `python verify_chiral_probe.py` with Python 3, NumPy, SymPy and SciPy. The script independently reconstructs the three-site Hermitian Hamiltonians; verifies their cubic matrix equation, transition amplitude, Poisson Laplace transform, complete forward factorization and reverse derivative identity symbolically; and independently integrates transition probabilities obtained from full matrix exponentials for multiple rates and both flux orientations. It also tests the claimed bounds over a geometric sample of positive rates. The recorded output was `PASS: exact symbolic identities and 614 direct numerical assertions;` with both positive forward rates and the single reverse optimum printed. These finite tests diagnose implementation errors; the universal statements are proved algebraically above.

## Relationship to prior work

Yin and Barkai [1] established sharp quantum search restarts and nontrivial competing minima for repeatedly monitored quantum walks with deterministic interrogation spacing and restarting after specified measurement counts. Thus neither the idea of quantum restart nor the mere possibility of competing quantum optimization branches is new. Here the *waiting times themselves are exponential*, each unsuccessful projective probe is followed immediately by active source re-preparation, the three-site hopping carries magnetic circulation, and two distinct positive **Poisson rates** attain exactly the same global mean-detection minimum for one fixed Hamiltonian.

Kulkarni and Majumdar [2] studied Poisson-random projective measurement and an induced resetting effect without a separate classical re-preparation move. Their explicitly solved generic two-level protocols are not identical to the present three-dimensional failure-projector-plus-re-preparation protocol; in dimension three the no-click subspace is two-dimensional, and a failed measurement alone generally does not return the state to the source. Modak and Aravinda [3] study sharp quantum resetting in stroboscopically observed settings; the present rate optimization is a different exponential renewal problem.

Wang and coauthors [4] investigate the local detection and flux-dependent dark states of a directed quantum triangle with fixed-time probing. The model is close at the Hamiltonian and detector level, but the inspected results concern local monitoring at fixed sampling intervals rather than a full re-preparation after every exponential-duration probe. Finocchiaro and coauthors [5] study flux control and optimal transport under locally monitored chiral walks, again with stroboscopic rather than exponential measurement intervals. Their published setting does not provide the stated exact twin Poisson-rate maximizers or the flux-reversal uniqueness comparison.

Published mathematical findings on alternating-flux two-shot quantum detection, chiral quantum triangles with continuous absorbing sinks, and two-state Poisson detectors were also compared by their mathematical assumptions and conclusions; those results do not directly imply this claim because they have different monitoring/re-preparation operations or optimize different statistics. Similarity or a null database search alone is not a novelty guarantee: general spectral and renewal formulas may still implicitly yield the present specialization.

## Limitations

This is a mathematically idealized model: coherent three-site hopping, source \(|0\rangle\), target \(|2\rangle\), ideal projective interrogation and *instantaneous explicit re-preparation* following every failure. In particular, it is not a claim about passive projective monitoring without re-preparation, permanent Lindblad absorption, arbitrary flux or source/target choices, non-Poisson renewal clocks, imperfect detection, or reset costs. The equal optimum is an exact parameter-specific degeneracy and need not persist under generic perturbations. The proof establishes expected first-detection time, not variance, tails or constrained multi-objective optimality. Publication priority beyond the inspected literature remains open to independent expert assessment; no independent scientific audit has been performed.

## References

1. R. Yin and E. Barkai, “Restart expedites quantum walk hitting times,” arXiv:2205.01974, first public 2022-05-04; later *Physical Review Letters* 130 (2023), 050802. https://arxiv.org/abs/2205.01974 .
2. M. Kulkarni and S. N. Majumdar, “First detection probability in quantum resetting via random projective measurements,” arXiv:2305.15123, first public 2023-05-24. https://arxiv.org/abs/2305.15123 .
3. A. Modak and S. Aravinda, “Non-Hermitian description of sharp quantum resetting,” arXiv:2303.03790, first public 2023-03-07. https://arxiv.org/abs/2303.03790 .
4. Q. Wang and collaborators, “First Hitting Times on a Quantum Computer: Tracking vs. Local Monitoring, Topological Effects, and Dark States,” arXiv:2402.15843, first public 2024-02-24. https://arxiv.org/abs/2402.15843 .
5. S. Finocchiaro and collaborators, “Optimal quantum transport on a ring via locally monitored chiral quantum walks,” arXiv:2507.10669, first public 2025-07-14. https://arxiv.org/abs/2507.10669 .
