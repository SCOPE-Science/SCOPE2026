# Exact parity-selected exceptional points in two-particle tandem exclusion

## Finding

Consider the tandem exclusion process (TEP), with the consecutive-site moves \(110\to101\) at rate \(\alpha>0\) and \(101\to011\) at rate \(\beta>0\). For each \(N\ge5\) and exactly two particles on the periodic ring \(\mathbb Z/N\mathbb Z\), restrict the generator to the nonfrozen configurations. Its complete spectrum is

\[
\lambda_{k,\pm}=-\frac{\alpha+\beta}{2}\pm\frac12\sqrt{(\alpha-\beta)^2+4\alpha\beta e^{2\pi i k/N}},\qquad k=0,1,\ldots,N-1.
\]

The restricted generator is nondiagonalizable **if and only if** the ring length \(N\) is even and

\[
\frac{\beta}{\alpha}\in\{3-2\sqrt2,\;3+2\sqrt2\}.
\]

At either ratio it has exactly one nontrivial Jordan block, of size two, at eigenvalue \(-(\alpha+\beta)/2\). At every other strictly positive rate pair the restricted generator is diagonalizable over \(\mathbb C\). Odd ring lengths have no exceptional point.

There is a direct observable signature. Set \(A_j=\{j,j+1\}\), \(B_j=\{j,j+2\}\), and, for an even ring started at \(A_0\), let

\[
F(t)=\sum_{j=0}^{N-1}(-1)^j\Pr_{A_0}(\eta_t=A_j),
\]

where the sum ranges over adjacent-pair positions and the initial state is \(A_0\). Define \(S=\alpha+\beta\) and \(\Delta^2=(\alpha-\beta)^2-4\alpha\beta\). Then

\[
F(t)=e^{-St/2}\left(\cosh(\Delta t/2)+\frac{\beta-\alpha}{\Delta}\sinh(\Delta t/2)\right),
\]

under the continuous extension at \(\Delta=0\), namely

\[
F(t)=e^{-St/2}\left(1+\frac{\beta-\alpha}{2}t\right).
\]

The staggered signal changes sign infinitely often **exactly** on the open rate-ratio interval \(3-2\sqrt2<\beta/\alpha<3+2\sqrt2\). Otherwise it has at most one sign change. In particular, equal rates yield \(F(t)=e^{-\alpha t}\cos(\alpha t)\), whereas the stationary weights of the active class are uniform. This temporal distinction is not the clustering transition of the stationary spatial measure.

## Assumptions and scope

The ring sites are indexed by \(\mathbb Z/N\mathbb Z\), with \(N\ge5\) and exactly two indistinguishable exclusion particles. Every triple is interpreted cyclically. Only moves \(110\to101\) and \(101\to011\) occur, with constant, strictly positive rates \(\alpha\) and \(\beta\), respectively. The theorem concerns the backward continuous-time Markov generator on the nonfrozen sector. A pair with no interparticle separation of one or two sites in either cyclic direction is frozen and is excluded, not incorrectly assigned the same relaxation modes. The initial condition for the observable is \(A_0\) and the observable requires even \(N\). The eigenvalues count algebraic multiplicities.

## Proof

**1. Exact active configuration graph.** With exactly two particles, a move is possible precisely when they occupy sites \(j,j+1\) or \(j,j+2\) for some \(j\). Since \(N\ge5\), the \(2N\) labeled configurations \(A_j\) and \(B_j\) are all distinct, and every other two-particle configuration contains neither movable triple and is absorbing. A local triple check gives the only permitted moves

\[
A_j\xrightarrow{\alpha}B_j\xrightarrow{\beta}A_{j+1},\qquad j\pmod N.
\]

Hence the active restriction is an irreducible directed \(2N\)-cycle with alternating rates. The diagonal of the row-sum-zero backward generator is the negative departure rate.

**2. Fourier reduction.** Translation by one site commutes with the generator. Writing \(f(A_j)=u e^{i\theta j}\) and \(f(B_j)=v e^{i\theta j}\), where \(\theta=2\pi k/N\), gives the exact block

\[
Q_k=\begin{pmatrix}-\alpha&\alpha\\\beta e^{i\theta}&-\beta\end{pmatrix}.
\]

The characteristic equation is \(\lambda^2+(\alpha+\beta)\lambda+\alpha\beta(1-e^{i\theta})=0\), giving the displayed spectrum. This diagonalizes the translation action, not necessarily the individual \(2\times2\) blocks.

**3. Exhaustive Jordan classification.** Distinct values of \(e^{i\theta}\) cannot share any generator eigenvalue: solve the characteristic equation for \(e^{i\theta}=1+[\lambda^2+(\alpha+\beta)\lambda]/(\alpha\beta)\). Thus all coincidences of eigenvalues must occur inside a Fourier block. Its discriminant can vanish only if \(e^{i\theta}\) is real and negative, since \(\alpha,\beta>0\). Therefore \(\theta=\pi\), available exactly when \(N\) is even, and the resulting condition is \((\alpha-\beta)^2=4\alpha\beta\), equivalent to \(\beta/\alpha=3\pm2\sqrt2\). At such a point \(Q_{N/2}+SI/2\) is a nonzero matrix with square zero, hence a single size-two Jordan block. All other blocks have distinct eigenvalues, proving both necessity and sufficiency, including algebraic multiplicities and uniqueness of the defect.

**4. Exact staggered time response and all sign regimes.** When \(N\) is even, the observable \(f(A_j)=(-1)^j\), \(f(B_j)=0\) belongs entirely to Fourier mode \(k=N/2\). Consequently \(F(t)=(e^{tQ_{N/2}}(1,0)^T)_1\). Writing \(J=Q_{N/2}+SI/2\), one has \(J^2=(\Delta^2/4)I\), so direct exponentiation yields the asserted hyperbolic formula and its \(\Delta=0\) limit. If \(\Delta^2<0\), writing \(\omega=\sqrt{-\Delta^2}>0\) turns the bracket into \(\cos(\omega t/2)+(\beta-\alpha)\sin(\omega t/2)/\omega\), a nonzero sinusoid with infinitely many zeros for \(t\ge0\). If \(\Delta^2>0\), the bracket is a linear combination of two real exponentials and thus has at most one real zero; if \(\Delta=0\), it is linear in \(t\) and likewise has at most one. Finally \(\Delta^2<0\) is exactly \(3-2\sqrt2<\beta/\alpha<3+2\sqrt2\). At equal rates, substitution yields the stated exponentially damped cosine. All rate and ring-size boundary cases have been accounted for under the assumptions.

## Verification

Run `python verify.py` with Python 3, NumPy and SciPy installed. The program constructs the *full* two-particle configuration generator directly from the cyclic three-site moves, independently of the Fourier formula; identifies the active and frozen configurations; compares the active generator spectrum with the stated branches; checks the local graph transitions; compares the exact staggered evolution with matrix exponentials; and checks the square-zero Jordan remainder at the two algebraic threshold ratios. It tests even and odd rings and both threshold directions. The finite tests are corroboration, not a replacement for the all-parameter Fourier argument.

## Relationship to prior work

Nguyen Ngoc, Nhung and Thi (2026), *Tandem Exclusion Process*, introduces the precise local transition rules, establishes the stationary Gibbs measure on the active sector and computes the stationary current and **spatial** transfer-matrix correlations. Its full publicly posted manuscript, including appendices, was examined. Its spatial transfer-matrix eigenvalues are distinct from the temporal Markov-generator spectrum treated here. The two-particle parity-selected non-Hermitian Jordan thresholds and staggered temporal response are not stated in that source. Related literature on non-Hermitian exceptional points includes Huang and Nelson's (2026) alternating-coupling SSH and ladder models, and prior oligomer exceptional-point studies. Those models have different generators and do not, on the inspected available material, give this stochastic two-particle classification or the measured response. The present proof also reduces the system to a standard alternating-rate directed cycle, so a broader published cyclic-Markov spectral theorem could subsume the eigenvalue component; that priority risk remains open. No claim is made that two-by-two discriminants or the abstract exceptional-point mechanism were first discovered here.

## Limitations

The theorem is confined to exactly two particles in the *nonfrozen* class, \(N\ge5\), strictly positive rates and periodic boundaries. In odd rings there is no \(\pi\)-staggered Fourier mode, not an assertion that other Fourier modes have no complex eigenvalues: indeed they generally do. On even rings, only the staggered observable has the stated overdamped/oscillatory rate-ratio transition; other wave numbers may display damped oscillations for all rates. The theorem neither establishes the full many-particle spectral gap nor proves any thermodynamic-limit dynamical phase transition. A general directed-cycle theorem could render the spectral formula a special case; the originality comparison has this explicit residual risk. No independent audit has been performed.

## References

1. N. P. Nguyen Ngoc, L. T. Nhung and H. A. Thi, *Tandem Exclusion Process*, first posted 2026-06-01 UTC, arXiv:2606.01568v1, https://arxiv.org/abs/2606.01568 ; author-posted complete text at https://www.researchgate.net/publication/405684325_Tandem_Exclusion_Process.
2. R. Huang and D. R. Nelson, *Banded non-Hermitian random matrices, neural networks, and eigenvalue degeneracies*, arXiv:2605.19072 (2026), https://arxiv.org/abs/2605.19072.
3. *Exceptional points in oligomer chains*, Communications Physics (2021), https://doi.org/10.1038/s42005-021-00757-3.
