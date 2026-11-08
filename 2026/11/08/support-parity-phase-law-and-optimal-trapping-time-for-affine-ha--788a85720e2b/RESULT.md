# Support-parity phase law and optimal trapping time for affine halfcube detectors

## Finding

Let \(d\ge1\), let \(a\in\{0,1\}^d\setminus\{0\}\) have Hamming weight \(w\), and let \(b\in\{0,1\}\). On the continuous-time quantum walk on the binary hypercube \(Q_d\), attach equally strong absorbers to the affine parity hyperplane
\[
T_{a,b}=\{v\in\{0,1\}^d:a\cdot v=b\pmod 2\}.
\]
This detector occupies exactly half the vertices, independently of \(w\). The coherent Hamiltonian is the unweighted adjacency operator \(A_d\); the absorbing no-jump Hamiltonian is \(H_\kappa=A_d-i\kappa P_{T_{a,b}}\), with \(\kappa>0\). Start from any computational-basis vertex \(x\notin T_{a,b}\). Put \(\sigma_j=|w-2j|\), \(p_j=2^{-w}\binom{w}{j}\), and
\[
M_{\sigma,\kappa}=\begin{pmatrix}-\kappa&-i\sigma\\-i\sigma&0\end{pmatrix},\qquad
f_{\sigma,\kappa}(t)=\left\|e^{tM_{\sigma,\kappa}}\binom{0}{1}\right\|^2.
\]
The exact surviving norm, for **every** \(t\ge0\), is
\[
\boxed{\left\|e^{-itH_\kappa}|x\rangle\right\|^2=\sum_{j=0}^wp_jf_{\sigma_j,\kappa}(t).}
\]
Consequently the eventual probability of *never* being absorbed is
\[
\boxed{q_w=\begin{cases}0,&w\text{ odd},\\2^{-w}\binom{w}{w/2},&w\text{ even}.\end{cases}}
\]
The complete dark-subspace dimension is \(0\) for odd \(w\), and \(2^{d-w-1}\binom{w}{w/2}\) for even \(w\). Thus detectors of identical cardinality undergo an exact perfect-versus-incomplete capture transition depending solely on the parity of the support size \(w\).

Define the strictly positive finite quantities
\[
\eta_w=1-q_w,\qquad R_w=2^{-w}\sum_{\substack{0\le j\le w\\w\ne2j}}\frac{\binom{w}{j}}{(w-2j)^2}.
\]
The absorption-time distribution is defective when \(w\) is even. Conditioned on absorption occurring, its mean is exactly
\[
\boxed{\mathbb E(\tau\mid\tau<\infty)=\frac1\kappa+\frac{\kappa R_w}{2\eta_w}.}
\]
It has the **unique** global optimum over all \(\kappa>0\):
\[
\boxed{\kappa_w^*=\sqrt{\frac{2\eta_w}{R_w}},\qquad
\min_{\kappa>0}\mathbb E(\tau\mid\tau<\infty)=\sqrt{\frac{2R_w}{\eta_w}}.}
\]
Along the odd and even support subsequences, respectively, the sharp asymptotic constants are
\[
\begin{aligned}
\kappa_w^*&\sim \frac{2^{5/4}}{\pi^{3/4}}w^{1/4},
&\min\mathbb E\tau_{\rm conditional}&\sim\frac{\pi^{3/4}}{2^{1/4}}w^{-1/4}
&& (w\text{ odd}),\\
\kappa_w^*&\sim \frac{\sqrt3\,2^{5/4}}{\pi^{3/4}}w^{1/4},
&\min\mathbb E\tau_{\rm conditional}&\sim\frac{\pi^{3/4}}{\sqrt3\,2^{1/4}}w^{-1/4}
&& (w\text{ even}).
\end{aligned}
\]
The optimization is conditional on successful capture, so the even-support optimum **does not** erase its positive dark-state survival probability.

## Assumptions and scope

Vertices are bit vectors in \(\mathbb F_2^d\); an edge flips precisely one bit. All edges have coherent hopping amplitude one, all trapping vertices have equal amplitude-loss parameter \(\kappa>0\), and no other site disorder, dephasing, recombination, or interactions are present. The initial state is localized at one vertex outside the detector. The usual quantum-jump realization has physical probability-loss rate \(2\kappa\) per unit probability at a detector site. All formulae hold for every integer \(d\ge w\ge1\), both affine parities \(b\), all choices of the \(w\) support coordinates, and all \(t\ge0\). The limit \(w\to\infty\) allows \(d\ge w\) to vary arbitrarily. The conditional mean is taken only over trajectories that eventually get absorbed.

## Proof

**1. Reduction to the active coordinates.** By permuting bits and flipping one supported bit, write \(Q_d=Q_w\square Q_{d-w}\), with detector projection \(P_{T_{a,b}}=P_{\rm even}\otimes I\). The no-jump generator factors as
\[
-iH_\kappa=(-iA_w-\kappa P_{\rm even})\otimes I+I\otimes(-iA_{d-w}).
\]
Its two tensor factors commute, and the second is unitary. For a localized initial state, the survival norm depends only on \(w\), not on \(d\), the remaining coordinates, or the choice of affine hyperplane orientation. The first factor begins on an odd-parity vertex.

**2. Singular-mode decomposition and exact time law.** In the even/odd bipartition of \(Q_w\), its adjacency operator has block form
\[
A_w=\begin{pmatrix}0&B\\B^*&0\end{pmatrix},
\]
while the loss operator is \(\kappa\operatorname{diag}(I,0)\). An initial odd vertex has a spectral measure for \(B^*B\) equal to the spectral measure of \(A_w^2\) at that vertex. The Walsh functions \(2^{-w/2}(-1)^{s\cdot x}\) diagonalize \(A_w\), with eigenvalues \(w-2|s|\). Their squared moduli are all \(2^{-w}\), so the spectral measure of \(B^*B\) puts mass \(p_j\) at \(\sigma_j^2\). Every singular mode reduces to \(M_{\sigma_j,\kappa}\) with initial vector \((0,1)^\mathsf T\). Summing squared norms proves the first boxed identity.

An entirely scalar expression is available. For \(\sigma>0\) put \(\Delta=\sqrt{\kappa^2-4\sigma^2}\), taking either complex square-root branch, and define
\[
\begin{aligned}
F_{\sigma,\kappa}(t)=e^{-\kappa t}\bigg(&\left|\cosh(\Delta t/2)+(\kappa/\Delta)\sinh(\Delta t/2)\right|^2\\
&+\left|(2\sigma/\Delta)\sinh(\Delta t/2)\right|^2\bigg).
\end{aligned}
\]
Then \(f_{\sigma,\kappa}=F_{\sigma,\kappa}\). At \(\Delta=0\) interpret this by its continuous limit: \(f_{\sigma,\kappa}(t)=e^{-\kappa t}[(1+\kappa t/2)^2+\sigma^2t^2]\). At \(\sigma=0\), \(f_{0,\kappa}(t)=1\). For \(\sigma>0\), both eigenvalues of \(M_{\sigma,\kappa}\) have strictly negative real parts, so \(f_{\sigma,\kappa}(t)\to0\).

**3. Dark dimension and absorption probability.** Zero singular modes are exactly the odd-vertex vectors in \(\ker B\). The eigenvalues of \(A_w\) are \(w-2j\) with multiplicity \(\binom{w}{j}\). For odd \(w\), \(A_w\) is nonsingular. For even \(w\), \(\dim\ker A_w=\binom{w}{w/2}\); since \(B\) is square, \(\dim\ker B=\frac12\binom{w}{w/2}\). Taking the tensor product with the complete \(Q_{d-w}\) factor gives the dark dimension stated above. In the initial localized state, the kernel weight is precisely the zero-spectral mass \(q_w\), establishing the capture law.

**4. Exact conditional mean and unique optimum.** For a nonzero singular value \(\sigma\), let \(z(t)=e^{tM_{\sigma,\kappa}}(0,1)^\mathsf T\). Solving the two-state Lyapunov equation
\[
M_{\sigma,\kappa}^*X+XM_{\sigma,\kappa}=-I
\]
shows \(\int_0^\infty\|z(t)\|^2dt=X_{22}=1/\kappa+\kappa/(2\sigma^2)\). Equivalently, this follows by integrating the coupled populations and coherence. The total finite-time survival excess above \(q_w\) integrates to \(\eta_w/\kappa+\kappa R_w/2\). Dividing by the success probability \(\eta_w>0\) gives the conditional mean. The resulting function \(1/\kappa+c\kappa\), with \(c>0\), has its unique strict minimum at the stated \(\kappa_w^*\).

**5. Sharp asymptotics.** Let \(Z_w=w-2J\) with \(J\sim\operatorname{Binomial}(w,1/2)\), so \(R_w=\mathbb E[\mathbf1_{Z_w\ne0}/Z_w^2]\). For every fixed integer \(z\) of the same parity as \(w\), the local central limit theorem yields \(\sqrt w\,\mathbb P(Z_w=z)\to\sqrt{2/\pi}\). The uniform bound \(\sup_{w,z}\sqrt w\,\mathbb P(Z_w=z)<\infty\) and the summability of reciprocal squares permit dominated convergence on each parity sublattice. Thus
\[
\lim_{\substack{w\to\infty\\w\text{ odd}}}\sqrt w R_w=\sqrt{2/\pi}\sum_{z\in2\mathbb Z+1}\frac1{z^2}=\frac{\pi^{3/2}}{2\sqrt2},
\]
\[
\lim_{\substack{w\to\infty\\w\text{ even}}}\sqrt w R_w=\sqrt{2/\pi}\sum_{z\in2\mathbb Z\setminus\{0\}}\frac1{z^2}=\frac{\pi^{3/2}}{6\sqrt2}.
\]
Since \(q_w\to0\), substituting these constants into the exact optimizer and minimum gives the displayed \(w^{1/4}\) and \(w^{-1/4}\) laws with their parity-dependent coefficients.

## Verification

The accompanying `verify.py` implements a separate direct-matrix calculation of survival norms on \(Q_w\) for \(1\le w\le7\) across several trapping strengths, times, and every untrapped starting vertex. It additionally checks a non-coordinate affine hyperplane in \(Q_5\), exact dark-rank predictions through \(w=10\), and Lyapunov mean-time identities through \(w=20\). It reports 1207 matrix/time comparisons and 220 Lyapunov comparisons, all passing. Finite numerical tests are corroboration, not a proof of the general or asymptotic assertions; those follow from the preceding spectral and local-limit arguments. Reproduce with `python verify.py` after installing the versions stated in `requirements.txt`.

## Relationship to prior work

Moore and Russell introduced and analyzed continuous-time quantum walks on the hypercube, whose bit-flip adjacency structure is the starting point here. Novo et al. (2015, first public version 2014) calculate one-vertex-trap quantum transport efficiencies on hypercubes using reduced invariant subspaces; their full text treats a **single** trapped site and does not evaluate a parity hyperplane, its all-time survival, its support-parity obstruction, or the optimal-loss scaling here. Novo, Mohseni and Omar (2016) study disorder and dephasing with a **single** hypercube trap rather than the homogeneous, multi-site halfcube detector. Le et al. (2018) describe general dark-space suppression principles without an evaluated halfcube parity-detector classification. Those papers supply relevant concepts, but their examined stated results do not imply this evaluated finite-time, conditional-time, and parity-asymptotic theorem without additional analysis. Existing one- and two-point hypercube capture projectors and Hamming-shell detector results concern different detector geometries and do not give the present time/optimization law.

## Limitations

The result requires equal hopping and equal absorption strengths across a complete affine parity hyperplane; arbitrary half-size detector sets, nonuniform loss, dephasing, onsite disorder, and interactions are not covered. For even \(w\), all conclusions about capture time are explicitly conditional on capture, and an uncaptured dark fraction remains forever. The theorem determines neither a global optimum over all half-size trap subsets nor a universal advantage for even-support detectors: the latter have lower conditional mean asymptotically but nonzero loss of capture probability. Historical priority beyond the sources inspected is not independently certified.

## References

1. C. Moore and A. Russell, *Quantum Walks on the Hypercube*, arXiv:quant-ph/0104137 (first posted 2001-04-29), https://arxiv.org/abs/quant-ph/0104137 .
2. L. Novo, S. Chakraborty, M. Mohseni, H. Neven and Y. Omar, *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, arXiv:1412.7209 (first posted 2014-12-22); Scientific Reports 5, 13304 (2015), https://pmc.ncbi.nlm.nih.gov/articles/PMC4557070/ .
3. L. Novo, M. Mohseni and Y. Omar, *Disorder-assisted quantum transport in suboptimal decoherence regimes*, Scientific Reports 6, 18142 (2016), https://pmc.ncbi.nlm.nih.gov/articles/PMC4698721/ .
4. T. P. Le, L. Donati, S. Severini and F. Caruso, *How to suppress dark states in quantum networks and bio-engineered structures*, arXiv:1707.07482 (2017), J. Phys. A 51, 365306 (2018), https://arxiv.org/abs/1707.07482 .
