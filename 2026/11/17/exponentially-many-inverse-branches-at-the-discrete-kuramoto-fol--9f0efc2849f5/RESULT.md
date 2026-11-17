# Exponentially many inverse branches at the discrete Kuramoto folding threshold

## Finding

Consider the finite, attractive, zero-phase-lag, all-to-all discrete Kuramoto phase map
\[
F_{K,\omega}(\theta)_i=\theta_i+\omega_i+\frac K N\sum_{j=1}^N\sin(\theta_j-\theta_i)\pmod{2\pi},
\qquad 1\le i\le N.
\]
For **every** integer \(N\ge2\), coupling \(K>1\), and frequency vector \(\omega\in\mathbb R^N\), the fiber over the uncoupled-output target \([\omega]\in\mathbb T^N\) contains at least
\[
\boxed{2^N-1}
\]
distinct states. All these states have explicit formulas and collapse onto the synchronized input as \(K\downarrow1\). More strongly, for each fixed \(N\), there is a finite set of exceptional coupling strengths \(E_N\subset(1,\infty)\) such that, whenever \(K\notin E_N\), an open neighborhood of \([\omega]\) consists entirely of targets with **at least \(2^N-1\) distinct preimages**. In particular, this robust multiplicity holds for all \(K>1\) sufficiently close to one.

This gives an explicit all-dimensional, exponentially growing **lower bound**, not an exact count of the full inverse fiber. The qualitative threshold between invertibility and noninvertibility at \(K=1\) is prior work; the contribution is the quantitative combinatorial multiplicity and its open-target persistence.

## Assumptions and scope

Here \(\mathbb T^N=(\mathbb R/2\pi\mathbb Z)^N\); frequency components may differ arbitrarily. No phase-lag term is present. Let \(d=d(K)\in(0,\pi)\) be the unique positive solution of
\[
\boxed{d=K\sin d}.
\]
For each nonempty proper subset \(S\subsetneq\{1,\ldots,N\}\), set \(m=|S|\) and define the real lift
\[
\theta_i^S=\begin{cases}
\frac{N-m}{N}d,& i\in S,\\[3pt]
-\frac mN d,&i\notin S.
\end{cases}
\]
Also define \(\theta^{\varnothing}=0\). Every component of every constructed lift belongs to \((-\pi,\pi)\); these lifts therefore give distinct torus states. The sets \(S=\{1,\ldots,N\}\) and \(S=\varnothing\) are not counted separately, since both would give the zero state under the natural convention.

For the open-target statement one possible finite exceptional set is obtained as follows. Define
\[
q(d)=\frac{\sin(d)/d-\cos d}{1-\cos d},\qquad 0<d<\pi,
\]
and set
\[
E_N=\left\{\frac d{\sin d}:0<d<\pi,\quad
q(d)\in\left\{\frac mN,1-\frac mN:1\le m\le N-1\right\}\right\}.
\]
The theorem permits this set to contain extraneous parameters: it is a sufficient exceptional set, not asserted to be minimal.

## Proof

**1. Existence and uniqueness of the nonzero separation.** The quotient \(\sin d/d\) decreases strictly from one to zero as \(d\) increases from zero to \(\pi\). Indeed its derivative has numerator \(d\cos d-\sin d<0\), since \((\sin d-d\cos d)'=d\sin d>0\). Thus \(\sin d/d=1/K\) has exactly one solution in \((0,\pi)\) for each \(K>1\), and \(d(K)\downarrow0\) as \(K\downarrow1\).

**2. All Boolean two-cluster partitions are preimages.** If \(i\in S\), exactly \(N-m\) terms in the coupling sum have phase difference \(-d\); otherwise exactly \(m\) terms have phase difference \(+d\). Therefore the real (unreduced) update is, for \(i\in S\),
\[
\theta_i^S+\omega_i+\frac K N\sum_j\sin(\theta_j^S-\theta_i^S)
=\omega_i+\frac{N-m}{N}(d-K\sin d)=\omega_i,
\]
and, for \(i\notin S\),
\[
\theta_i^S+\omega_i+\frac K N\sum_j\sin(\theta_j^S-\theta_i^S)
=\omega_i-\frac mN(d-K\sin d)=\omega_i.
\]
The zero state also maps to \(\omega\). Every nonempty proper subset is recovered exactly from the **positive-coordinate indices** of its lift; hence these \(2^N-2\) states and zero are pairwise distinct modulo \(2\pi\). This proves the lower bound. Moreover,
\[
\sum_i\theta_i^S=0,\qquad
\|\theta^S\|_2^2=\frac{m(N-m)}N d^2.
\]
From \(K=d/\sin d=1+d^2/6+O(d^4)\) follows
\[
\|\theta^S\|_2^2=\frac{6m(N-m)}N(K-1)+O_N((K-1)^2),
\]
so all constructed states coalesce with zero when \(K\downarrow1\) at fixed \(N\).

**3. Exact regularity criterion.** At any phase state the Jacobian of the real lift is the identity minus the symmetric weighted graph Laplacian with off-diagonal weights \(K\cos(\theta_j-\theta_i)/N\). For the two-cluster state of size \(m\), write \(t=m/N\). Its complete real spectrum is
\[
\begin{aligned}
&1 &&\text{(global phase direction)},\\
&1-K\cos d &&\text{(relative cluster direction)},\\
&1-K[t+(1-t)\cos d] &&\text{(multiplicity \(m-1\))},\\
&1-K[(1-t)+t\cos d] &&\text{(multiplicity \(N-m-1\))}.
\end{aligned}
\]
Modes with zero multiplicity are simply omitted. The relative-cluster eigenvalue is strictly positive, because \(1-d\cot d>0\). Using \(K=d/\sin d\), the two possible remaining zero-eigenvalue conditions become respectively \(t=q(d)\) and \(1-t=q(d)\). Thus the stated \(E_N\) contains all possible singular parameters of the nonzero constructed preimages. At zero, the Jacobian has eigenvalues \(1\) and \(1-K\) (the latter \(N-1\) times), and is invertible whenever \(K>1\).

**4. The exceptional set is finite and stays away from one.** The apparent singularity of \(q\) at zero is removable; its even Taylor expansion starts
\[
q(d)=\frac23-\frac{d^2}{90}+O(d^4),
\]
and \(q(\pi)=1/2\). Hence \(q\) extends analytically to a neighborhood of the compact interval \([0,\pi]\) and is not constant. For each fixed fraction \(m/N\) or \(1-m/N\), the analytic equation \(q(d)=m/N\) or \(q(d)=1-m/N\) has finitely many solutions in \((0,\pi)\): otherwise compactness would produce a zero accumulation point, contradicting the identity theorem. This proves \(E_N\) is finite. At small positive \(d\), the displayed expansion excludes every fixed listed fraction, including \(2/3\) at the endpoint. Consequently \(E_N\) does not approach \(K=1\).

**5. Open-target persistence.** Fix \(K\notin E_N\). Each of the constructed \(2^N-1\) preimages is a regular point of the smooth torus map. Choose disjoint neighborhoods of these finitely many preimages. The inverse function theorem gives an open neighborhood of their common image \([\omega]\) for each neighborhood. Their finite intersection is a nonempty open set of targets admitting one distinct preimage in every chosen neighborhood. Therefore every target there has at least \(2^N-1\) preimages. This completes the proof.

## Verification

The companion `verify.py` reproduces exact local eigenvalue expansions symbolically; independently evaluates the full \(N\)-oscillator map on 2,505 explicit constructed lifts for several dimensions, couplings, and heterogeneous frequencies; and compares 21 exact predicted Jacobian spectra against direct numerical eigenvalues. It reports `VERIFY_OK` on success. None of these finite tests substitutes for the analytic quantifiers above.

## Relationship to prior work

Gade and Gupta (first publicly posted September 19, 2026) formulate the same discrete-time globally coupled phase map with general lag \(\beta\), investigate the continuum limit, incoherent-state stability, synchronization, and a Frobenius–Perron description. The present theorem uses the \(\beta=0\) specialization and addresses finite-dimensional **inverse multiplicity**, not the continuum synchronization threshold.

Maistrenko, Vasylenko, Maistrenko and Mosekilde (2008), Section 3, **already state that the discrete Kuramoto dynamics are invertible for \(0<K\le1\) and become noninvertible for \(K>1\)**. Neither that qualitative boundary nor mere existence of multiple preimages is new. The theorem here quantifies how many pairwise distinct preimages a single canonical target has for **all** \(N\) and all \(K>1\), and proves open-target robustness away from finitely many explicitly defined exceptional strengths.

Kalmár-Nagy, Horváth and Vincze (2025) study phase-space geometry for small globally coupled networks and tile the three-oscillator torus. Only its abstract was accessible for this comparison; overlapping full-text results remain a residual priority risk. Existing generalized convergence and synchronization theorems concern forward orbits, not the inverse-fiber count.

## Limitations

The result gives a constructive **lower bound**, not the exact total number of preimages. The particular count applies to the attractive, zero-phase-lag, all-to-all phase update; no analogous bound is proved for arbitrary phase lags, sparse graphs, or different nonlinear coupling kernels. The finite set \(E_N\) is a sufficient exclusion for the open-target statement and need not be minimal. The existence of many one-step inverse branches alone says nothing about multistep chaotic behavior or the stability of those preimages as forward states. Historical priority and independent validation remain open.

## References

1. P. M. Gade and S. Gupta, *Discrete-time Kuramoto model with phase lag: Linear stability analysis and onset of synchronization*, arXiv:2609.22715v1 (publicly posted 2026-09-19), https://arxiv.org/abs/2609.22715.
2. V. Maistrenko, A. Vasylenko, Yu. Maistrenko, and E. Mosekilde, *Phase Chaos and Multistability in the Discrete Kuramoto Model*, Nonlinear Oscillations **11** (2008), 229–241, https://doi.org/10.1007/s11072-008-0026-4; open text https://www.imath.kiev.ua/~nosc/admin/private/published_files/601/NOSC6012008111999.pdf.
3. T. Kalmár-Nagy, D. A. Horváth, and B. Vincze, *Synchronization in Small, Fully Coupled Systems of Discrete-Time Kuramoto Oscillators*, International Journal of Bifurcation and Chaos **35** (2025), 2530032, https://doi.org/10.1142/S0218127425300320.
