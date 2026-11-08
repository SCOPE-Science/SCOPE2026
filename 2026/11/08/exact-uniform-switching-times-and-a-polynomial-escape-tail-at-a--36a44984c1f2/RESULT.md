# Exact uniform switching times and a polynomial escape tail at a negative-doubling critical hole

## Finding
Let \(T\) be the negative-doubling interval map
\[
T(x)=\begin{cases}1-2x,&0\leq x<1/2,\\2-2x,&1/2<x\leq1,\end{cases}
\]
with any value at \(1/2\), and let the open hole be \(H=(2/5,3/5)\). Give \(X_0\) uniform Lebesgue distribution on \([0,1]\), put \(X_j=T^j(X_0)\), and let \(E_n=\{X_j\notin H:0\leq j<n\}\) for every integer \(n\geq1\). Endpoint ambiguities have zero Lebesgue probability.

**Theorem.** For every integer \(n\geq1\),
\[
\mathbb P(E_n)=\frac{4(n+1)}{5\,2^n}.
\]
Partition the safe set, modulo endpoints, into four equal open intervals \(I_0=(0,1/5)\), \(I_1=(1/5,2/5)\), \(I_2=(3/5,4/5)\), and \(I_3=(4/5,1)\). Define \(J_n\) to be the first time \(j\in\{0,\ldots,n-1\}\) at which \(X_j\in I_1\cup I_2\), or \(J_n=n\) if there is none. Then **the conditioned switching time is exactly uniform**:
\[
\mathbb P(J_n=j\mid E_n)=\frac1{n+1},\qquad j=0,\ldots,n.
\]
In particular the rescaled switching time \(J_n/n\), conditional on \(E_n\), converges in distribution to uniform measure on \([0,1]\). The one-step conditional escape probability after observing \(n\) safe positions is \(n/[2(n+1)]\), tending to \(1/2\) with a nonzero reciprocal-time correction.

Write \(\nu_{\mathrm{out}}=(\delta_0+\delta_1)/2\), \(\nu_{\mathrm{in}}=(\delta_{1/3}+\delta_{2/3})/2\). For every fixed \(0\leq\theta<1\), the conditional law of \(X_{\lfloor\theta n\rfloor}\) given \(E_n\) converges weakly to
\[
(1-\theta)\nu_{\mathrm{out}}+\theta\nu_{\mathrm{in}}.
\]
At the terminal observed time, a boundary-layer effect occurs: the conditional distribution of \(X_{n-1}\) is *exactly* a mixture of the uniform laws on \(I_0,I_1,I_2,I_3\) with masses
\[
\frac{(1,n,n,1)}{2(n+1)}.
\]
It converges in total variation to the uniform law \(\nu_*\) on \(I_1\cup I_2\), with exact total-variation distance \(1/(n+1)\). Hence its terminal limit is nonatomic, unlike the limit at any fixed fraction \(\theta<1\) of the observation horizon.

At the other natural symmetric zero-entropy boundary \(H=(1/3,2/3)\), the corresponding exact survival probability is instead
\[
\mathbb P(E_n)=\frac4{3\,2^n},\qquad n\geq1,
\]
and the terminal conditional distribution is uniform on \((0,1/3)\cup(2/3,1)\) for every \(n\). Thus these two distinguished holes have the same exponential escape rate \(\log2\), but only the \((2/5,3/5)\) hole has a linear-in-time escape prefactor and a uniform conditioned switching time.

## Assumptions and scope
The map is defined on \([0,1]\), with piecewise affine branches as displayed; the hole is open. All probability statements use ordinary Lebesgue initial data, not the maximal-entropy measure on the survivor set. Safe-cell endpoints and their preimages have zero Lebesgue measure, so arbitrary endpoint conventions do not affect the results. The integer horizon \(n\) counts observations at times \(0,\ldots,n-1\), including the initial position.

## Proof
**1. Exact Markov partition.** With cells ordered \(I_0,I_1,I_2,I_3\), the only positive-length safe-cell transitions are
\[
I_0\to I_2,I_3,\quad I_1\to I_1,\quad I_2\to I_2,\quad I_3\to I_0,I_1.
\]
Indeed, the images of the four whole cells are respectively \((3/5,1)\), \((1/5,3/5)\), \((2/5,4/5)\), and \((0,2/5)\). Every indicated branch covers the full destination cell with slope magnitude \(2\), and the other image portions fall in the hole. The adjacency matrix is therefore
\[
A=\begin{pmatrix}0&0&1&1\\0&1&0&0\\0&0&1&0\\1&1&0&0\end{pmatrix}.
\]
Every admissible \(n\)-cell path represents a disjoint (up to endpoints) initial interval of length \(1/[5\,2^{n-1}]\). This follows inductively from the full-branch property and needs no statistical independence assumption.

**2. Switching paths.** The two outer cells \(I_0,I_3\) alternate deterministically if the orbit stays in the outer pair. At each transition an outer path can instead enter exactly one of the two inner cells, after which surviving paths remain in that inner cell. For an \(n\)-cell path there are exactly two choices for each switching time \(j=0,1,\ldots,n\): two paths start in the inner pair when \(j=0\); for \(1\leq j<n\), there are two possible outer starting cells and one allowed path for the specified switch; and for \(j=n\), two paths never switch. Thus there are \(2(n+1)\) equal-length admissible paths, proving both the survival probability and exact uniform switching-time law. The conditional next-step survival ratio is \(\mathbb P(E_{n+1})/\mathbb P(E_n)=(n+2)/[2(n+1)]\); subtraction from one gives the stated escape probability.

**3. The macroscopic conditional profile.** Conditioned on survival, every switching time \(j\in\{0,\ldots,n\}\) has equal probability, and for each \(j\) the two paths are paired by the reflection \(x\mapsto1-x\). If switching occurs after \(t=\lfloor\theta n\rfloor\), the orbit at time \(t\) remains in one of two outer branches for at least \(j-t\) further steps. Inverse-branch contraction shows its distance from the outer two-cycle \(\{0,1\}\) is at most \((1/5)2^{-(j-t-1)}\) when \(j>t\), with a harmless adjustment for \(j=t+1\). If switching occurs no later than \(t\), the orbit at time \(t\) must survive inside \(I_1\) or \(I_2\) for the remaining \(n-1-t\) steps. Inverse contraction around the branch fixed points \(1/3\) and \(2/3\) bounds the distance from the corresponding point by a constant times \(2^{-(n-1-t)}\). For any fixed \(\theta<1\), away from a vanishing fraction of switching times near \(t\), these errors vanish uniformly. The reflection pairs ensure equal weights within either two-point set. Since \(\mathbb P(J_n\leq t\mid E_n)=(t+1)/(n+1)\to\theta\), weak convergence to the asserted convex combination follows, including \(\theta=0\).

**4. Terminal boundary layer.** The exact path counts ending in the four cells are the entries of \(\mathbf1^\top A^{n-1}\):
\[
\mathbf1^\top A^{n-1}=(1,n,n,1),\qquad n\geq1.
\]
For a fixed terminal cell, the affine full-branch images of all its admissible path cylinders are uniformly distributed on that entire cell. Normalizing the counts gives the displayed terminal masses. Since each cell supports an absolutely continuous uniform law and the two inner cells have limiting masses \(1/2\) each, total variation against \(\nu_*\) is precisely \(1/(n+1)\). This also proves the boundary-layer distinction without exchanging the limits \(n\to\infty\) and \(t/n\to1\).

**5. Comparison hole.** For \(H=(1/3,2/3)\), the safe intervals \(K_0=(0,1/3)\), \(K_1=(2/3,1)\) have the sole full-cell transitions \(K_0\to K_1\) and \(K_1\to K_0\). Thus there are exactly two length-\(n\) paths, each of initial length \(1/[3\,2^{n-1}]\). Their terminal images are the two full safe intervals, proving both comparison claims. At \(H=(2/5,3/5)\), the characteristic polynomial of \(A\) is \((\lambda-1)^3(\lambda+1)\) with a size-two Jordan block at \(\lambda=1\). That nonsemisimple component accounts for the polynomial prefactor despite both graphs having spectral radius one.

## Verification
Run `python3 verify_escape.py` with Python 3. The standalone program independently forms iterated exact-rational inverse-image interval unions for each hole, rather than obtaining their lengths from the path-count formula. For every horizon from 1 to 25 it verifies the two stated survival probabilities. It separately verifies the four-state matrix identities, all switching-time counts, the two-state comparison, and the exact terminal total-variation formula. The finite checks corroborate but do not replace the all-horizon path proof.

## Relationship to prior work
Ding, Steiner and Sun develop symbolic survivor spaces and Hausdorff-dimension devil's staircases for the negative-doubling map with a hole. Their paper gives the map convention and establishes the qualitative open-system setting, not the exact Lebesgue-conditioned path law above. Glendinning and Sidorov study hole thresholds for the *positive* doubling map; their entropy and survivor-set classifications do not imply this negative-doubling conditional law. General transfer-operator and escape-rate results for open expanding maps explain why transition matrices matter but do not determine the displayed coefficients or conditioned switching-time distribution without the specific four-cell computation. Existing periodic-orbit zeta classifications for symmetric negative-doubling holes concern recurrent orbit counts, whereas the present theorem counts transient cylinders and their Lebesgue weights. In particular, a zeta function alone cannot determine the number of entrance paths or their distribution over switching times.

## Limitations
The theorem covers exactly the two displayed rational symmetric holes and Lebesgue initial data. It does not claim a full parameter-neighborhood classification of escape tails or any analogous result for the positive doubling map. The convergence at \(t/n\to\theta<1\) is weak, not total variation, whereas the terminal distribution does converge in total variation to an absolutely continuous law. Zero-measure exceptional endpoint orbits are excluded from probabilistic statements. Novelty is assessed against the explicitly inspected literature and records, not certified as exhaustive historical priority; independent review is outstanding.

## References
1. Y. Ding, W. Steiner, Y. Sun, *Open dynamical systems in topologically expansive decreasing Lorenz maps*, arXiv:2610.03327v1 (first posted 2026-10-02), https://arxiv.org/abs/2610.03327.
2. P. Glendinning, N. Sidorov, *The doubling map with asymmetrical holes*, Ergodic Theory Dynam. Systems **35** (2015), 1208–1228, arXiv:1302.2486, https://arxiv.org/abs/1302.2486.
3. C. Bose, G. Froyland, C. González-Tokman, R. Murray, *Ulam's Method for Lasota–Yorke Maps with Holes*, SIAM J. Appl. Dyn. Syst. (2014), https://doi.org/10.1137/130917533.
4. M. Demers, P. Wright, L.-S. Young, *Entropy, Lyapunov Exponents and Escape Rates in Open Systems*, arXiv:1107.2609, https://arxiv.org/abs/1107.2609.
