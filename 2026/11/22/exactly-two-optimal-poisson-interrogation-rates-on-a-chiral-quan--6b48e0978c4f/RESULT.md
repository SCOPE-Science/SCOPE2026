# Two equally optimal Poisson interrogation rates for first detection on a chiral quantum triangle

## Finding

A chiral quantum triangle, probed at exponential intervals and actively re-prepared after each failure, has **two distinct and exactly equally optimal positive interrogation rates** for mean time to first detection in one flux orientation. Reversing the flux while leaving the preparation and detector fixed gives a unique optimum. The two-rate degeneracy is governed by the exact symmetry \(r\mapsto6/r\) in unit hopping. That symmetry holds in both orientations, but only in one orientation does the optimum occur away from its fixed point.

The optimal forward rates and corresponding mean are
\[
r_\pm=\frac{3+2\sqrt3\ \pm\sqrt{12\sqrt3-3}}2,
\qquad T_+(r_\pm)=3+2\sqrt3.
\]
They are approximately \(1.1234606571\) and \(5.3406409581\), with exact product six. In the reverse orientation the unique optimal rate is \(\sqrt6\), with mean time \(27/(6+4\sqrt6)\).

The one-attempt success probabilities used below coincide with stationary site occupations also tabulated for the same flux-threaded triangle with unconditional Poisson resetting [6,7]. The result here is the classification of the optima for **elapsed first-detection time**, not a new calculation of a stationary population imbalance.

## Assumptions and scope

In the orthonormal basis \(|0\rangle,|1\rangle,|2\rangle\), with unit hopping and \(\hbar=1\), take
\[
H_+=\begin{pmatrix}0&-i&-1\\i&0&1\\-1&1&0\end{pmatrix},
\qquad H_-=\overline{H_+}.
\]
These matrices are Hermitian. At the start of each attempt the state is \(|0\rangle\). After an independently chosen wait \(\tau\) of density \(r e^{-r\tau}\), during which the state evolves under the selected Hamiltonian, make the ideal binary measurement with success projector \(P=|2\rangle\langle2|\). Stop on success. On failure, **actively re-prepare \(|0\rangle\)** at zero time cost independently of the no-click state, and start a new attempt. The objective is expected total elapsed time, with no reset overhead. With hopping magnitude \(J>0\), rates above are multiplied by \(J\) and times divided by \(J\).

## Proof

**The one-attempt law.** The cubic identity \(H_+^3=3H_+\) and matrix entries \((H_+)_{20}=-1\), \((H_+^2)_{20}=i\) give
\[
\langle2|e^{-iH_+t}|0\rangle
=i\left(\frac{\sin(\sqrt3t)}{\sqrt3}+\frac{\cos(\sqrt3t)-1}{3}\right).
\]
Conjugating the Hamiltonian changes the sign of the cosine-minus-one part of this amplitude. Squaring and using the elementary Laplace transforms of sine and cosine at frequencies \(\sqrt3,2\sqrt3\) gives
\[
p_\pm(r)=r\int_0^\infty e^{-rt}|\langle2|e^{-iH_\pm t}|0\rangle|^2\,dt
=\frac{2(r^2\mp3r+6)}{(r^2+3)(r^2+12)}.
\]
Here \(p_+\) uses the minus sign in its numerator, and both probabilities are positive on \(r>0\).

The same integral is the stationary occupation of site 2 for an unconditional reset process of rate \(r\) with reset state \(|0\rangle\) [6]. Indeed the state is the unitary evolution since the last reset, and in stationarity the time since that reset is exponential of rate \(r\). For the flux convention of [7], \(D^*H_+D\) with \(D=\operatorname{diag}(1,i,i)\) is their \(\Phi=-\pi/2\) matrix at unit hopping; conjugation gives their \(\Phi=\pi/2\) case up to a site gauge. The diagonal gauge leaves preparation and site projectors unchanged. Their individual population formula for \(p_2\) therefore gives exactly the displayed \(p_\pm(r)\).

**Elapsed first-detection time.** The attempts are independent and identically distributed as pairs of duration and success indicator. For the first attempt the expected duration is \(1/r\), and the expected residual time after a failure is again \(T_\pm(r)\). The mean is finite: summing means of the trial durations weighted by the probabilities that the previous trials all failed gives a geometric series, since each duration is independent of the previous failures. Thus \(T_\pm=1/r+(1-p_\pm)T_\pm\), or \(T_\pm=1/(rp_\pm)\). No independence of duration and success within a trial is assumed.

**Why only one orientation has a two-rate tie.** Write \(x=r+6/r\). The success rate per unit expected elapsed time \(Q_\pm(r)=rp_\pm(r)\) factors through this single coordinate:
\[
Q_\pm(r)=\frac{2(x\mp3)}{x^2+3},\qquad x\ge2\sqrt6.
\]
Indeed dividing numerator and denominator by \(r^2\) gives numerator \(2(x\mp3)\) and denominator \(x^2+3\). The map from \(r\) to \(x\) has exactly two positive preimages for each \(x>2\sqrt6\) (their product is six) and the single preimage \(\sqrt6\) at \(x=2\sqrt6\).

The derivative of \(2(x-3)/(x^2+3)\) is \(2(-x^2+6x+3)/(x^2+3)^2\). It is strictly positive up to \(x_*=3+2\sqrt3>2\sqrt6\) and strictly negative thereafter on the attainable interval. At the maximum, the derivative equation gives \(x_*^2+3=2x_*(x_*-3)\), hence \(Q_+=1/x_*\). Solving \(r^2-x_*r+6=0\) now gives exactly the two stated minimizers. On reversal the derivative of \(2(x+3)/(x^2+3)\) is \(2(3-x^2-6x)/(x^2+3)^2<0\) on the attainable interval. Its unique maximizing \(x\) is \(2\sqrt6\), and substitution yields \(Q_-(\sqrt6)=(6+4\sqrt6)/27\). This proves both complete global optimizations.

## Verification

`python verify_chiral_probe.py` with Python 3, SymPy, NumPy and SciPy checks the cubic matrix equation, transition amplitude, rational probabilities, and exact forward sharp-bound and reverse derivative identities that give the same optimizers. It also compares direct matrix-exponential integrals and samples positive rates. The finite numerical tests are diagnostics; the symmetry reduction and derivative signs prove the result for all positive rates.

## Relationship to prior work and limitations

Repeated measurements with periodic sharp restarting can exhibit competing extrema [1,3]; such protocols differ from independent exponential waits followed by immediate source re-preparation. In two-level measurements, a one-dimensional failure subspace can make resets automatic [2]; with three sites the failure projector here does not have that property. Chiral triangles and rings have been studied under fixed-time or stroboscopic local monitoring [4,5]. The stationary reset-state law [6] and explicit triangle populations [7] supply the same one-attempt statistic. In particular [7] optimizes \(|p_1-p_2|\), not \(rp_2\); its sharp optimizer is for a different objective. It is cited for the overlapping probabilities without making a chronological priority assertion. The contribution here is the exact count and locations of tied **mean-time** optima and the flux-reversal uniqueness, with a symmetry that explains the paired rates.

This result does not extend to passive no-click propagation, absorption, arbitrary flux or reset cost, or optimization of variance and tails. Instantaneous re-preparation is a model assumption. The reciprocal-rate symmetry and equality of the two rates' means are exact for this specified triangle and objective; generic perturbations need not preserve them. Priority beyond the inspected sources is not settled.

## References

1. R. Yin and E. Barkai, *Restart expedites quantum walk hitting times*, [arXiv:2205.01974](https://arxiv.org/abs/2205.01974).
2. M. Kulkarni and S. N. Majumdar, *First detection probability in quantum resetting via random projective measurements*, [arXiv:2305.15123](https://arxiv.org/abs/2305.15123).
3. A. Modak and R. Aravinda, *Non-Hermitian description of sharp quantum resetting*, [arXiv:2303.03790](https://arxiv.org/abs/2303.03790).
4. Q. Wang et al., *First Hitting Times on a Quantum Computer: Tracking vs. Local Monitoring, Topological Effects, and Dark States*, [arXiv:2402.15843](https://arxiv.org/abs/2402.15843).
5. S. Finocchiaro et al., *Optimal quantum transport on a ring via locally monitored chiral quantum walks*, [arXiv:2507.10669](https://arxiv.org/abs/2507.10669).
6. D. C. Rose et al., *Spectral properties of simple classical and quantum reset processes*, [arXiv:1806.01298](https://arxiv.org/abs/1806.01298), eqs. (59)–(61), (73)–(74).
7. *Sharp flux–reset optimization and a singular weak-flux population imbalance in a quantum triangle*, [Resultary, 2026-11-22](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-sharp-flux-reset-optimization-and-a-singular-weak-flux-populatio--848fc77e7b52), Proof §1.
