# Exact two-shot detection from complementary fluxes on a monitored quantum triangle

## Finding

Consider local projective first detection at one vertex of a three-site quantum ring. Although each of the two fixed fluxes \(0\) and \(\pi/3\) has a permanent dark subspace, alternating them after each unsuccessful measurement eliminates all persistent dark states except at exact stroboscopic revivals. Moreover, this two-flux protocol has an analytically sharp universal worst-case two-probe detection probability and a sharp long-run survival-rate optimum.

For \(J>0\), \(\tau>0\), and
\[
 t(\tau)=\frac{5+4\cos(3J\tau)}9,\qquad
 c(\tau)=\frac{\sqrt{16t(\tau)+(1-t(\tau))^2}+1-t(\tau)}4,
\]
the maximal survival probability after two probes is exactly \(c(\tau)^2\), over all normalized initially off-target states. It is strictly less than one if and only if \(3J\tau\notin2\pi\mathbb Z\). Consequently, if \(N\) is the index of the first successful probe, every normalized off-target state obeys
\[
 \Pr(N>2n)\le c(\tau)^{2n}\quad(n\ge1),
\]
and eventual detection has probability one away from revivals, with finite detection-time moments of every order.

The best guaranteed two-probe detection probability and the attaining intervals are
\[
 \boxed{\max_{\tau>0}\min_{\|\psi\|=1,\,Q\psi=\psi}\Pr_\psi(N\le2)
   =\frac{64-4\sqrt{13}}{81}},
 \qquad \boxed{3J\tau\equiv\pi\pmod{2\pi}}.
\]
At precisely these intervals, \(\|C\|_{2\to2}=(2+\sqrt{13})/9\) and the two eigenvalues of the two-step surviving amplitude \(C\) are \((-1\pm2i\sqrt2)/9\). The resulting spectral radius \(1/3\) is globally minimal over all sampling intervals.

## Assumptions and scope

The Hilbert space is \(\mathcal H=\mathbb C^3\), with ordered site basis \(\{|0\rangle,|1\rangle,|2\rangle\}\) and cyclic hopping operator
\[
 T=|0\rangle\langle1|+|1\rangle\langle2|+|2\rangle\langle0|,\qquad
 H_\alpha=-J(e^{i\alpha}T+e^{-i\alpha}T^\dagger),\quad J>0.
\]
We set \(\hbar=1\). The target projector is \(P=|0\rangle\langle0|\), the no-click projector is \(Q=I-P\), and the starting pure state is an arbitrary unit vector satisfying \(Q\psi=\psi\). The first probe follows one interval of unitary evolution under \(H_0\); after a failure, the second follows \(H_{\pi/3}\), and the same two-step pattern is repeated on further failures. Every interval has identical duration \(\tau>0\). The projective measurements are ideal, with no decoherence, detector errors, or noise. Probabilities are unconditional: unsuccessful trajectories are not renormalized between applications of the no-click linear maps.

Let \(U_\alpha=e^{-iH_\alpha\tau}\), and restrict the no-click linear product to \(Q\mathcal H\):
\[
 C=\left.QU_{\pi/3}QU_0Q\right|_{Q\mathcal H}.
\]
By the Born rule, the exact survival probability after \(2n\) probes, for any \(n\ge1\), is \(\|C^n\psi\|^2\).

## Proof

**Spectral reduction.** Put \(\omega=e^{2\pi i/3}\), and let \(|f_k\rangle=3^{-1/2}\sum_{j=0}^{2}\omega^{jk}|j\rangle\), for \(k=0,1,2\). Direct diagonalization gives \(H_\alpha|f_k\rangle=-2J\cos(\alpha+2\pi k/3)|f_k\rangle\). Set \(z=e^{3iJ\tau}\). Because the eigenvalues at flux zero are \((-2J,J,J)\), and at flux \(\pi/3\) are \((-J,2J,-J)\) in Fourier order, we have the *exact* unitary identities
\[
 U_0=e^{-iJ\tau}[I+(z-1)|f_0\rangle\langle f_0|],\qquad
 U_{\pi/3}=e^{iJ\tau}[I+(z^{-1}-1)|f_1\rangle\langle f_1|].
\]
Put \(v_k=\sqrt{3/2}\,Qf_k\) for \(k=0,1\), so \(\|v_k\|=1\) and \(|\langle v_0,v_1\rangle|=1/2\). Let \(P_k=|v_k\rangle\langle v_k|\) on \(Q\mathcal H\), and \(a=(1+2z)/3\), \(t=|a|^2=(5+4\cos(3J\tau))/9\). The two scalar global phases cancel, leaving
\[
 C=BA,\qquad A=I+(a-1)P_0,\qquad B=I+(\bar a-1)P_1.
\]
The two factors have singular values \(1,\sqrt t\), so \(\det(C^\dagger C)=t^2\). Using \(A A^\dagger=I+(t-1)P_0\), \(B^\dagger B=I+(t-1)P_1\), the cyclic trace identity yields
\[
 \operatorname{tr}(C^\dagger C)
 =\operatorname{tr}[(I+(t-1)P_1)(I+(t-1)P_0)]
 =2t+\frac{(1-t)^2}{4}.
\]
Thus the two singular values are
\[
 c_\pm(t)=\frac{\sqrt{16t+(1-t)^2}\pm(1-t)}4,
 \qquad \frac19\le t\le1,
\]
proving the claimed exact operator norm.

**Detection and optimality.** The derivative
\[
 c_+'(t)=\frac14\left(\frac{7+t}{\sqrt{1+14t+t^2}}-1\right)>0
\]
is strictly positive for \(t\ge0\), because \((7+t)^2-(1+14t+t^2)=48\). Therefore \(c_+(t)<1\) exactly when \(t<1\), equivalently \(z\ne1\). The operator-norm bound on \(C^n\) gives the geometric survival inequality and thus detection with probability one and all moments finite. If \(z=1\), both unitaries are scalar multiples of the identity; since the initial state is in \(Q\mathcal H\), every probe fails with probability one.

Since \(c_+\) is strictly increasing, its global minimum occurs at the least possible \(t=1/9\), namely \(z=-1\), which is equivalent to \(3J\tau\equiv\pi\pmod{2\pi}\). Substitution gives
\[
 \min_\tau\|C\|=\frac{2+\sqrt{13}}9,
 \qquad\max_\tau\min_{\|\psi\|=1}\Pr_\psi(N\le2)
 =1-\left(\frac{2+\sqrt{13}}9\right)^2
 =\frac{64-4\sqrt{13}}{81}.
\]
The minimizing initial states exist: they are right singular vectors corresponding to the largest singular value.

At \(z=-1\), one has \(A=I-4P_0/3\), \(B=I-4P_1/3\). Since \(\operatorname{tr}(P_0P_1)=1/4\), a direct trace calculation gives \(\operatorname{tr}C=-2/9\) and \(\det C=1/9\). The characteristic polynomial is \(\lambda^2+(2/9)\lambda+1/9\), with roots
\[
 \lambda_\pm=\frac{-1\pm2i\sqrt2}{9},\qquad |\lambda_\pm|=\frac13.
\]
At any interval, \(|\det C|=t\ge1/9\), hence \(\rho(C)\ge\sqrt{|\det C|}=\sqrt t\ge1/3\); the preceding eigenvalues prove equality at the same optimal times. By the finite-dimensional spectral-radius formula, \(\lim_{n\to\infty}\|C^n\|^{1/n}=\rho(C)\).

**Individual dark states.** At either fixed flux, \(Q U_\alpha Q|_{Q\mathcal H}\) is a rank-one modification of a scalar unitary with singular values \(1,\sqrt t\). The unit vector orthogonal to its rank-one projector is a genuine dark state, with survival norm one at every probe. At nonrevival intervals \(t<1\), the complementary component decays, so a particle initially at \(|1\rangle\) has eventual detection probability exactly \(1/2\) for either fixed flux. At revivals it has eventual detection probability zero. The alternating protocol removes the shared dark direction because \(|\langle v_0,v_1\rangle|=1/2\), rather than one.

## Verification

Run `python verify_twoflux.py` with NumPy, SymPy and SciPy installed. It reconstructs the full three-site Hamiltonians independently and compares the two-shot matrix with the analytically derived rank-one projector formula on 1001 distinct nonresonant intervals; checks its singular spectrum, exact optimal point, eigenvalues, fixed-flux dark survival and multi-cycle norm bounds; and performs exact SymPy identities in \(\mathbb Q(\sqrt3)\) at the optimum. The recorded check output was `PASS: exact symbolic identities and 1071 independent finite checks`.

The exact proof establishes the all-interval and all-initial-state assertions. The finite checks are reproducibility diagnostics, not substitutes for the universal proof.

## Relationship to prior work

Wang and coauthors [1] introduce precisely the directed three-site Hamiltonian, projective local detection and flux-dependent dark states for **static** flux choices; their Sections 3, 6, and appendices were inspected. The present theorem retains that model but changes the control protocol: the two different fluxes are alternated after each unsuccessful probe. Its worst-case two-probe norm, all-state dark-state elimination (outside revival times), optimal interrogation times and best spectral radius are not supplied by static-flux results.

Thiel and coauthors [2] characterize bright and dark subspaces for repeated projective measurements with a fixed Hamiltonian. Kessler and coauthors [3] analyze random probing times, again for a fixed unitary Hamiltonian between measurements. The perturbed-ring work [4] modifies spatial couplings rather than applying a deterministic two-flux temporal cycle. Liu and coauthors [5] analyze conditional periodic no-click measurements with a repeated fixed survival operator; they establish generic and Floquet dark states and discuss control, but do not switch the Hamiltonian between successive failures or calculate this particular two-shot minimax. The present exact two-matrix product is not a direct fixed-unitary specialization of those analyses. The fixed-flux dark-state concepts themselves are not claimed as novel.

## Limitations

The theorem assumes ideal coherent three-site evolution, a single measured vertex, equal positive sampling intervals and the prescribed two flux values with strict alternation. It does not claim optimality over arbitrary time-dependent flux schedules, other flux pairs, other graphs or adaptive measurement rules; the optimality is only over the common sampling interval within the defined two-flux protocol. The guaranteed two-shot probability and infinite-horizon spectral radius are different criteria, although their minimizers happen to coincide here. Research-record and public-text searches cannot establish absolute novelty; a broader unindexed periodically monitored quantum-process result may imply this specialization. There has been no independent scientific audit or experimental implementation of the alternating protocol.

## References

1. Q. Wang, S. Ren, R. Yin, K. Ziegler, E. Barkai and S. Tornow, “First Hitting Times on a Quantum Computer: Tracking vs. Local Monitoring, Topological Effects, and Dark States,” arXiv:2402.15843v1, first public February 24, 2024; later *Entropy* **26** (2024), 869. https://arxiv.org/abs/2402.15843 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC11508062/ .
2. S. Thiel, R. Mualem, D. Meidan, E. Barkai and D. A. Kessler, “Quantum total detection probability from repeated measurements I. The bright and dark states,” arXiv:1906.08112 (2019), https://arxiv.org/abs/1906.08112 .
3. D. A. Kessler, E. Barkai and K. Ziegler, “The first detection time of a quantum state under random probing,” arXiv:2012.01763 (2020), https://arxiv.org/abs/2012.01763 .
4. Q. Wang, R. Yin, K. Dou, M. Zhang and G. Song, “Quantum first detection of a quantum walker on a perturbed ring,” *Physical Review Research* **5** (2023), 013202. https://doi.org/10.1103/PhysRevResearch.5.013202 .
5. Q. Liu, K. Ziegler, D. A. Kessler and E. Barkai, “Driving quantum systems with periodic conditional measurements,” *Physical Review Research* **4** (2022), 023129. https://doi.org/10.1103/PhysRevResearch.4.023129 .
