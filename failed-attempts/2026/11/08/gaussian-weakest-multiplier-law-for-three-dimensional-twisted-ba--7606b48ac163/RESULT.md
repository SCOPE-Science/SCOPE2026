# Gaussian weakest-multiplier law for three-dimensional twisted baker periodic points

## Finding
For the three-dimensional twisted baker map defined below, let \(\mathcal R_n\) be its isolated fixed points of the \(n\)-th iterate with an entirely real return-Jacobian spectrum. Sample \(x\) uniformly from \(\mathcal R_n\) and put
\[
\chi_n(x)=\min_{\lambda\in\operatorname{spec}(DF^n(x))}|\lambda|^{1/n}.
\]
Then, as \(n\to\infty\),
\[
\boxed{\sqrt n\left(\frac13-\log_2\chi_n(x)\right)\ \Longrightarrow\ -\min(Z_0,Z_1,Z_2),}
\]
where \(Z\) is centered Gaussian on \(Z_0+Z_1+Z_2=0\) with covariance
\[
\boxed{\operatorname{Cov}(Z_i,Z_j)=\frac13\mathbf 1_{\{i=j\}}-\frac19.}
\]
In particular, the average weakest expansion has the sharp correction
\[
\boxed{\frac1{|\mathcal R_n|}\sum_{x\in\mathcal R_n}\log_2\chi_n(x)
=\frac13-\frac{\sqrt3}{2\sqrt{\pi n}}+o(n^{-1/2}).}
\]
The theorem counts fixed points of iterates (possibly with smaller least period), not only primitive cycles.

## Assumptions and scope
On \(X=[-1,1]\times[0,1]^2\), define the piecewise-affine map
\[
F(x_1,x_2,x_3)=\begin{cases}
(1+2x_1,x_2,x_3),&x_1<0,\\
(1-2x_3,x_1,x_2),&x_1\ge0.
\end{cases}
\]
The nonisolated fixed face \(N=\{x_1=-1\}\) is excluded. By the symbolic coding of Saiki–Takahasi–Yorke, every word of length \(n\) with at least one right symbol corresponds to exactly one isolated point fixed by \(F^n\). No periodic orbit crosses the switching hyperplane. The real-eigenvalue criterion, verified in the cited exact residue law, is precisely that the number of right symbols is divisible by three. Thus \(\mathcal R_n\) is nonempty for \(n\ge3\); no probabilistic claim is made for \(n<3\).

## Proof
**1. Exact eigenvalue-to-occupation reduction.** The two branch Jacobians are
\[
L=\begin{pmatrix}2&0&0\\0&1&0\\0&0&1\end{pmatrix},\qquad
R=\begin{pmatrix}0&0&-2\\1&0&0\\0&1&0\end{pmatrix}.
\]
For a periodic itinerary \(a_1\ldots a_n\in\{L,R\}^n\), put \(r_0=0\) and \(r_j=r_{j-1}+\mathbf1_{\{a_j=R\}}\pmod3\). If \(r_n=0\), the signed monomial matrix \(DF^n\) is diagonal. Define its residue occupation counts
\[
N_j=\#\{1\le k\le n:r_k=j\},\quad j=0,1,2.
\]
Tracing an input coordinate through the signed cyclic permutations shows that the diagonal moduli are exactly \(2^{N_0},2^{N_2},2^{N_1}\): every step multiplies precisely the strand whose post-step cyclic residue is its designated residue by two. Hence \(N_0+N_1+N_2=n\) and
\[
\log_2\chi_n=\frac1n\min\{N_0,N_1,N_2\}.
\]
Each right/left word occurs once, with the all-left word excluded. Uniform counting on \(\mathcal R_n\) is therefore the law of independent fair increments \(a_j\in\{0,1\}\), conditioned on \(r_n=0\) and on at least one increment being one.

**2. Cyclic-walk central limit calculation.** The residue process \(r_j\) is the irreducible aperiodic Markov chain on \(\mathbb Z_3\) with matrix \(P=(I+S)/2\), where \(S\) cyclically advances the residue. Its stationary distribution is \(\pi=(1/3,1/3,1/3)\). For \(g(j)=e_j-(1/3)\mathbf1\), the occupation vector satisfies
\[
(N_0,N_1,N_2)-\frac n3\mathbf1=\sum_{j=1}^n g(r_j).
\]
On the mean-zero subspace the two nontrivial eigenvalues of \(P\) are \(\lambda=(1+\omega)/2\) and \(\overline\lambda\), with \(\omega=e^{2\pi i/3}\) and \(|\lambda|=1/2\). Crucially,
\[
\operatorname{Re}\frac{\lambda}{1-\lambda}=0.
\]
The Green–Kubo covariance is \(\langle g,g^\top\rangle_\pi\) plus the symmetric forward/backward covariance series. The latter vanishes because the two Fourier eigenvalues of \(\sum_{k\ge1}P^k\) have purely imaginary values \(\lambda/(1-\lambda)\) and its conjugate. Consequently the asymptotic covariance is *exactly*
\[
\Sigma=\operatorname{diag}(\pi)-\pi\pi^\top=\frac13I-\frac19\mathbf1\mathbf1^\top.
\]
The finite-state Markov additive central limit theorem therefore gives
\[
\frac{(N_0,N_1,N_2)-(n/3)\mathbf1}{\sqrt n}\Longrightarrow\mathcal N(0,\Sigma).
\]
This limit remains valid after imposing \(r_n=0\). Indeed, for every fixed Fourier test vector \(t\), the corresponding tilted finite-state transition matrix \(P\operatorname{diag}(e^{it\cdot g(j)/\sqrt n})\) has a simple leading eigenvalue with expansion \(1-\tfrac1{2n}t^\top\Sigma t+o(n^{-1})\), and all other eigenvalues remain uniformly separated from the unit circle. Its \((0,0)\) matrix element, divided by \(P^n(0,0)\to1/3\), has the same limiting Gaussian characteristic function. Excluding the all-left word changes the conditional law by at most \(O(2^{-n})\), since \(P^n(0,0)\to1/3\). Therefore the displayed Gaussian limit also holds for uniform isolated real-spectrum iterate-fixed points.

**3. Weakest multiplier and its mean.** By Step 1 and the continuous-mapping theorem,
\[
\sqrt n\left(\frac13-\log_2\chi_n\right)=-\min_j\frac{N_j-n/3}{\sqrt n}\Longrightarrow-\min_jZ_j.
\]
The bridge occupancy vector has second moments bounded by \(Cn\): the stationary covariance series decays geometrically, and conditioning on \(r_n=0\) increases expectations of nonnegative variables by at most a fixed constant because \(P^n(0,0)\ge c>0\) for \(n\ge3\). Likewise initial-state correction is bounded by geometric mixing. Hence the scaled minima have bounded second moments and are uniformly integrable, so their means converge.

Let \(W_0,W_1,W_2\) be independent standard Gaussians. The representation \(Z_j=(W_j-\overline W)/\sqrt3\) has covariance \(\Sigma\), and hence
\[
\mathbb E[-\min_jZ_j]=\frac{\mathbb E\max_jW_j}{\sqrt3}
=\frac{\sqrt3}{2\sqrt\pi}.
\]
The last identity follows by integrating the maximum density \(3\phi(z)\Phi(z)^2\): integration by parts and symmetry yield \(\mathbb E\max_jW_j=3/(2\sqrt\pi)\). Multiplying the mean convergence by \(n^{-1/2}\) proves the stated sharp mean correction.

## Verification
The included standalone standard-library script `check_occupations.py` reconstructs signed integer Jacobian products for all eligible words of lengths \(3\) through \(11\), compares their diagonal entries to the residue occupation formula, and verifies the real-spectrum residue criterion in dimension three for all non-all-left words in those lengths. It also checks the explicit Markov matrix eigenvalue identities algebraically through rational matrix powers and reports deterministic finite counts. These finite checks are corroboration; the all-\(n\) theorem follows from the exact monomial structure and finite-state Markov limit proof above.

## Relationship to prior work
Saiki, Takahasi and Yorke, *The twisted baker map* (2022 preprint, 2023 journal), established coding, hyperbolicity, density of both spectral types, and a qualitative nonuniform expansion phenomenon. Their Theorem C concerns spatial equidistribution, not the distribution of multiplier magnitudes. The published *Exact real-spectrum residue law for the twisted baker map* determines exactly which residue classes have real eigenvalues and their counts, but does not give fine multiplier distributions or their Gaussian asymptotics. For the two-dimensional specialization, explicit full-derivative gap histograms are known; these do not imply the three-coordinate Gaussian bridge law because the residue chain and covariance geometry change in dimension three. Work on periodic distributions of heterochaos baker maps concerns a different family and a different notion of instability.

## Limitations
The result is specific to the three-dimensional twisted baker map, uniform counting over isolated fixed points of \(F^n\) with entirely real return-Jacobian spectrum, and their weakest return eigenvalue modulus. It does not describe least-period-only conditioning, the nonreal-spectrum class, invariant measures sampled by physical time, or general piecewise baker families. The limit theorem is a same-source-derived new calculation and still carries the possibility of an unindexed equivalent result. No independent mathematical audit is claimed.

## References
1. Y. Saiki, H. Takahasi and J. A. Yorke, *The twisted baker map*, arXiv:2202.04304, first public 9 February 2022, https://arxiv.org/abs/2202.04304; especially §§2.1–2.3 and Theorems A–C.
2. *Exact real-spectrum residue law for the twisted baker map*, research record of 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-real-spectrum-residue-law-for-the-twisted-baker-map--f1bd1c74fb3b .
3. H. Takahasi, *Distributions of periodic points for the Dyck shift and the heterochaos baker maps*, arXiv:2409.01261 (different map family).
