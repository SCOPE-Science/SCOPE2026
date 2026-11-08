# Perfect-square survival under Hamming-sphere absorption on a quantum hypercube

## Finding
Let \(Q_d\) be the binary \(d\)-cube, \(d\ge 2\), and let one excitation start at the all-zero vertex. Fix an integer shell radius \(1\le r\le d\). Every vertex of Hamming weight \(r\) carries a strictly positive, possibly unequal irreversible capture rate; all other vertices have zero capture rate. For uniform nonzero real nearest-neighbor hopping, define \(p_{d,r}\) as the infinite-time probability of never being captured. Then
\[
p_{d,r}=2^{-d}\sum_{k=0}^{d}\binom dk\,\mathbf 1_{\{K_r(k;d)=0\}},\qquad
K_r(k;d)=\sum_{j=0}^{r}(-1)^j\binom kj\binom{d-k}{r-j}.
\]
Binomial coefficients outside their natural ranges are zero. This formula is independent of all positive capture rates and the nonzero hopping magnitude.

In particular, monitoring **every vertex exactly two edges from the initial site** gives
\[
p_{d,2}=\begin{cases}
\displaystyle \frac{2}{2^d}\binom{d}{(d-\sqrt d)/2},&d\ge4\text{ a perfect square},\\[4pt]
0,&d\ge2\text{ not a perfect square}.
\end{cases}
\]
On square dimensions \(d=s^2\to\infty\),
\[
p_{s^2,2}\sim\sqrt{\frac{8}{\pi e}}\,\frac1s.
\]
Thus an entire nonempty shell of absorbers may leave permanent survival in infinitely many dimensions, while all other dimensions are completely absorbing from the specified initial state. This is a statement about asymptotic capture **probability**, not mean capture time.

## Assumptions and scope
The vertex set is \(\{0,1\}^d\), with Hamming weight \(|x|\), and \(|0\rangle\) denotes the basis vector at the origin. Let \(A\) be the adjacency matrix of \(Q_d\), let \(J\in\mathbb R\setminus\{0\}\), and let \(\gamma_x>0\) be arbitrary real rates for \(|x|=r\). Put
\[
\Gamma=\sum_{|x|=r}\gamma_x|x\rangle\langle x|,\qquad
H_{\mathrm{eff}}=JA-\frac{i}{2}\Gamma,\qquad
p_{d,r}=\lim_{t\to\infty}\|e^{-itH_{\mathrm{eff}}}|0\rangle\|^2.
\]
The unnormalized no-jump state is used; its squared norm is the unabsorbed probability for independent irreversible local loss channels. The model does not include dephasing, coherent onsite disorder, time-dependent loss rates, or periodic measurements.

## Proof
**1. What survives dissipation.** Write \(M=-iJA-\Gamma/2\). Since \(M+M^*=-\Gamma\le0\), \(e^{tM}\) is a contraction. If \(Mv=\lambda v\) with \(\operatorname{Re}\lambda=0\), then
\[
2\operatorname{Re}\lambda\,\|v\|^2=\langle v,(M+M^*)v\rangle=-\langle v,\Gamma v\rangle=0.
\]
Thus \(\Gamma v=0\), and \(v\) is also an eigenvector of \(A\). Conversely, each adjacency eigenvector in \(\ker\Gamma\) is undamped. Their direct sum
\[
\mathcal D=\bigoplus_{\mu\in\operatorname{spec}A}\big(\ker(A-\mu I)\cap\ker\Gamma\big)
\]
is reducing for \(A\) and \(\Gamma\), hence for \(M\). On its orthogonal complement all eigenvalues of \(M\) have strictly negative real part. In finite dimension, the complementary evolution decays to zero; no nontrivial Jordan block can persist on the imaginary axis for a contraction semigroup. Therefore
\[
p_{d,r}=\|P_{\mathcal D}|0\rangle\|^2.
\]
Positivity of every \(\gamma_x\) makes \(\ker\Gamma\) precisely the vectors vanishing at *all* weight-\(r\) sites, so the answer depends only on the absorber support.

**2. The only modes visible at the origin.** For \(z\in\{0,1\}^d\), the normalized Walsh character \(\chi_z(x)=2^{-d/2}(-1)^{z\cdot x}\) has adjacency eigenvalue \(d-2|z|\). Let \(P_k\) be the orthogonal projection onto the Walsh eigenspace of weight \(k\), where \(0\le k\le d\). One has
\[
\|P_k|0\rangle\|^2=2^{-d}\binom dk.
\]
The permutation group of coordinates preserves \(A\), the entire absorbing shell, and therefore \(\mathcal D\). Each eigenspace of weight \(k\) has a *one-dimensional* permutation-invariant line, spanned by \(P_k|0\rangle\). Consequently the orthogonal dark projection of this vector is either the entire vector or zero: an invariant projection has no intermediate image inside a one-dimensional invariant line.

**3. The exact shell-zero criterion.** At any vertex \(x\) with \(|x|=r\), direct character summation and binomial double counting give
\[
(P_k|0\rangle)(x)=\frac1{2^d}\sum_{|z|=k}(-1)^{z\cdot x}
=\frac1{2^d}\frac{\binom dk}{\binom dr}K_r(k;d).
\]
Thus the invariant weight-\(k\) eigenvector is dark exactly when \(K_r(k;d)=0\). Summing its initial squared weights gives the announced formula for every \(1\le r\le d\).

**4. The perfect-square case.** For the second shell,
\[
K_2(k;d)=\binom{d-k}{2}-k(d-k)+\binom k2
=\frac{(d-2k)^2-d}{2}.
\]
An integer \(k\in\{0,\ldots,d\}\) is a zero exactly when \(d=s^2\), for a positive integer \(s\), and \(k=(d\pm s)/2\). Since \(s\) and \(s^2\) have the same parity, both roots are integers; for \(d\ge4\) they are distinct and in range. The two binomial weights coincide. This proves the exact dichotomy. Finally the local central binomial estimate with standardized displacement \(s/\sqrt d=1\) gives
\[
2^{-s^2}\binom{s^2}{(s^2-s)/2}\sim\sqrt{\frac{2}{\pi s^2}}e^{-1/2},
\]
which yields the stated asymptotic coefficient.

## Verification
Two standalone numerical programs accompany the proof and are independently runnable with Python, NumPy and SciPy.

- `verify_fourier.py` computes a *full* Fourier-eigenspace shell-restriction nullspace without using the Krawtchouk formula, then compares it against the formula for all 35 pairs \((d,r)\) with \(2\le d\le8\) and \(1\le r\le d\). It also checks the polynomial square criterion for 498 dimensions \(2\le d<500\).
- `verify_dynamics.py` exponentiates the non-Hermitian generator on the full \(2^d\)-vertex state space, using nonuniform randomly generated positive absorption rates and both signs of hopping. All 15 cases with \(2\le d\le6\) agree at the selected long times with the exact prediction to the stated numerical tolerance; it also verifies norm monotonicity at two times.

Execute each in the same directory as `python verify_fourier.py` and `python verify_dynamics.py`, respectively. The infinite-time statement and all-dimension classification rest on the proof, not on these finite checks or extrapolation from finite-time exponentials.

## Relationship to prior work
Moore and Russell [1] study continuous-time coherent quantum walks and mixing on hypercubes, but not shell-supported irreversible loss. Krovi and Brun [2] establish general symmetry/degeneracy mechanisms for infinite quantum hitting times, including a continuous-time discussion, but do not calculate the exact capture law for an entire prescribed Hamming shell. Feinsilver and Kocik [3] establish the symmetric Krawtchouk/Hadamard spectral relation, which is used here as known algebra rather than claimed new. The new contribution is the exact nonuniform-rate shell-loss survival law and its dimension-arithmetic second-shell classification, not the underlying Walsh spectrum, Krawtchouk identities, or the general dark-state principle. This is a mathematically explicit specialization of established spectral machinery; no claim is made that all ingredients or general dark-state methods are new.

## Limitations
The source-based originality assessment is provisional: a differently indexed spectral/detection paper could contain an equivalent special case. A general dark-subspace statement plus known Krawtchouk identities supplies a route to deriving the result, but the inspected sources do not themselves report the exact shell-loss law or the perfect-square trapping dichotomy. The result addresses eventual survival from the single specified corner, not the full dark-subspace dimension or arbitrary initial states. The proof does not give characteristic decay times or survival rates at finite time, and it does not cover arbitrary partial shell detection or spatially varying hopping amplitudes.

## References
1. C. Moore and A. Russell, *Quantum Walks on the Hypercube*, arXiv:quant-ph/0104137v1 (first public 2001-04-29), https://arxiv.org/abs/quant-ph/0104137.
2. H. Krovi and T. A. Brun, *Quantum walks with infinite hitting times*, arXiv:quant-ph/0606094v1 (first public 2006-06-10), https://arxiv.org/abs/quant-ph/0606094.
3. P. Feinsilver and J. Kocik, *Krawtchouk matrices from classical and quantum random walks*, arXiv:quant-ph/0702173v1 (first public 2007-02-16), https://arxiv.org/abs/quant-ph/0702173.
