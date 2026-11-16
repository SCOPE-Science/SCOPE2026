# Drift-induced recovery and exact temporal resonances in cyclic Fourier sampling

## Finding
Let \(N\ge4\) be even, \(-1<\delta<1\), and \(\tau>0\). Write \(S f(j)=f(j+1)\) on \(\mathbb Z/N\mathbb Z\), set
\[
L_\delta=I-\frac{1+\delta}{2}S-\frac{1-\delta}{2}S^{-1},\qquad P f=(f(0),f(2),\ldots,f(N-2)),
\]
and observe the two snapshots \(\mathcal T_{N,\delta,\tau}f=(Pf,P e^{-\tau L_\delta}f)\). The complete complex signal is recoverable from these observations precisely when
\[
\boxed{\ N\equiv2\pmod4\quad\text{or}\quad(4\mid N,\ \delta\ne0,\ \delta\tau\notin\pi\mathbb Z).\ }
\]
In all other cases the measurement map has **exactly one complex dimension of kernel**. Thus a nonzero drift removes the persistent Fourier blind spot on a four-divisible cycle except at the discrete *temporal resonance* delays \(\tau=m\pi/|\delta|\), for positive integers \(m\).

For \(4\mid N\), let \(A_N(\delta,\tau)\) be the smallest eigenvalue of \(\mathcal T_{N,\delta,\tau}^*\mathcal T_{N,\delta,\tau}\). As \(\delta\to0\) through nonzero real values,
\[
\boxed{\ \lim_{\delta\to0}\frac{\max_{\tau>0}A_N(\delta,\tau)}{\delta^2}
=\frac{\tau_*^2}{e^{2\tau_*}+1}=0.12070751969725028\ldots\ },
\]
where \(\tau_*=1+e^{-2\tau_*}=1.108857552878572\ldots\) is the unique positive solution. Every maximizing delay converges to \(\tau_*\). The constant and limiting delay are independent of the four-divisible cycle length.

## Assumptions and scope
All signal and observation norms use unweighted complex Euclidean counting measure, and times are real. The parameter \(\delta\) encodes the imbalance of two strictly positive directed nearest-neighbor jump rates; \(\delta=0\) is the reversible normalized cycle heat operator. We consider the full signal space, exactly every other vertex, and exactly two times \(0\) and \(\tau\). The lower bound is the **squared** least singular value, and the maximization is over all positive delays. Four-divisible sizes \(N\ge4\) are fixed when taking the small-drift limit.

## Proof
**Fourier fibers and nullity.** The normalized Fourier characters \(u_k(j)=N^{-1/2}e^{2\pi i k j/N}\) diagonalize \(L_\delta\), with eigenvalues
\[
\lambda_k=1-\cos\theta_k-i\delta\sin\theta_k,\qquad \theta_k=2\pi k/N.
\]
Characters \(u_k\) and \(u_{k+N/2}\) agree on the even vertices. Unitary Fourier transformation of both observation channels therefore splits the measurement map into \(N/2\) orthogonal blocks
\[
Q_k=\frac1{\sqrt2}\begin{pmatrix}1&1\\z_k&z_{k+N/2}\end{pmatrix},\qquad z_k=e^{-\tau\lambda_k}.
\]
The factor \(1/\sqrt2\) follows from the two-to-one spatial downsampling. The determinant vanishes exactly when \(z_k=z_{k+N/2}\). Since \(\lambda_{k+N/2}=2-\lambda_k\), equality of magnitudes forces \(\cos\theta_k=0\). Such a character exists among the representatives \(0\le k<N/2\) exactly when \(4\mid N\), and then its index is \(k=N/4\), the **only** such block. There the entries are \(e^{-\tau}e^{\pm i\delta\tau}\), so equality occurs precisely at \(\sin(\delta\tau)=0\). A singular block has rank one, proving the complete injectivity and exact nullity classification.

**Sharp smallest singular value at the critical alias.** For \(4\mid N\), denote by \(a(\delta,\tau)\) the lower eigenvalue of \(Q_{N/4}^*Q_{N/4}\). Its trace is \(1+e^{-2\tau}\) and determinant is \(e^{-2\tau}\sin^2(\delta\tau)\), hence
\[
a(\delta,\tau)=\frac{1+e^{-2\tau}-\sqrt{(1+e^{-2\tau})^2-4e^{-2\tau}\sin^2(\delta\tau)}}2.
\]
For \(\delta=0\), all other Fourier blocks are invertible at every positive time because their cosine is nonzero. Consequently, for any compact \(\tau\)-interval inside \((0,\infty)\), these other blocks retain a uniform positive lower singular value for sufficiently small \(|\delta|\). On that compact interval the global least eigenvalue therefore equals \(a(\delta,\tau)\) when \(\delta\) is sufficiently small. Taylor expansion, uniformly on compact intervals, yields
\[
\frac{A_N(\delta,\tau)}{\delta^2}\longrightarrow h(\tau)=\frac{\tau^2}{e^{2\tau}+1}.
\]

**Global optimization without a hidden time-escape.** For every \(\tau>0\), the unit antisymmetric vector supported on the critical Fourier pair gives the exact Rayleigh quotient \(e^{-2\tau}\sin^2(\delta\tau)\). Thus, for all real \(\delta\),
\[
0\le\frac{A_N(\delta,\tau)}{\delta^2}\le\tau^2e^{-2\tau}\qquad(\delta\ne0).
\]
The right side tends to zero both as \(\tau\downarrow0\) and \(\tau\to\infty\). At each nonzero \(\delta\), \(A_N(\delta,\tau)\) is continuous, positive for some times and tends to zero at both time endpoints, hence achieves a maximum. The compact-uniform convergence and the common endpoint envelope show that maxima converge to \(\max h\), and every limit point of maximizing delays maximizes \(h\). Differentiating gives \(h'(\tau)=0\) exactly when \(\tau=1+e^{-2\tau}\). The difference of the two sides is strictly increasing, giving one positive solution; \(h\) vanishes at both endpoints, so this solution is the unique global maximizer. This proves the sharp asymptotic, the universal constant and convergence of all maximizing delays. \(\square\)

## Verification
The standalone `CHECK.py` constructs the full \(N\times N\) directed semigroup and compares its two-snapshot Gram eigenvalues against all Fourier fibers for eight even sizes, four drifts and four times (128 comparisons), checks eight critical resonant/nonresonant cases, and tests six small-drift optimization quantities. With Python 3, NumPy and SciPy, execute `python CHECK.py`; observed output is `CHECK_OK direct_gram_comparisons=128 resonant_checks=8 small_drift_checks=6 total=142`. These finite computations corroborate normalization and representative cases; the proof above covers all even sizes, times and permitted real drifts.

## Relationship to prior work
The September 2026 graph Paley–Wiener dynamical-sampling preprint of Cabrelli, Cordero, Bulai, Saliani and Molter motivates graph Fourier frame recovery but its accessible abstract treats undirected normalized-Laplacian dynamics and path examples, not the directed cyclic resonance set. The closest exact undirected-cycle result, *Arithmetic blind spots and an optimal two-time heat-sampling delay on cycles*, proves the irreversible obstruction when \(4\mid N\) for symmetric diffusion; that obstruction is deliberately the \(\delta=0\) boundary here. A second exact result on the integer line establishes the same universal optimization function \(h\) for a **reversible** heat flow with a spectral notch, but does not identify directed phase resonances or recovery at critical spatial aliases. The numerical constant is not claimed original on its own. General polyphase dynamical-sampling criteria predate these exact results; the contribution is the all-cycle drift/delay singular-set classification and the quantitative, sharp restoration of stability near reversibility.

## Limitations
The drift is spatially homogeneous and the directed generator is normal; arbitrary directed graphs, nonuniform observation sets, other temporal samplers and nonnormal perturbations are not covered. The quadratic stability law is for each fixed four-divisible cycle as drift tends to zero, not a joint limit in size and drift. The full text of the plausible 2026 graph preprint was not accessible; novelty remains a best-knowledge comparison rather than a certified priority determination. No independent audit has been performed.

## References
- C. Cabrelli, E. Cordero, I. M. Bulai, S. Saliani and U. Molter, *Dynamical Sampling in Graph Paley–Wiener Spaces*, arXiv:2609.25472 (first posted 2026-09-21), https://arxiv.org/abs/2609.25472.
- *Arithmetic blind spots and an optimal two-time heat-sampling delay on cycles*, published-finding corpus, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-arithmetic-blind-spots-and-an-optimal-two-time-heat-sampling-del--36b6900e59dd.
- *Exact two-time diffusion frame bounds and optimal blind-spot scaling on the integer line*, published-finding corpus, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-two-time-diffusion-frame-bounds-and-optimal-blind-spot-sca--60ea36e5831d.
- A. Aldroubi, J. Davis and I. Krishtal, *Exact Reconstruction of Spatially Undersampled Signals in Evolutionary Systems*, arXiv:1312.3203 (2013), https://arxiv.org/abs/1312.3203.
