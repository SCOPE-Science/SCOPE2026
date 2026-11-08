# Exact collision-dark spectrum and Hamming-distance capture on Boolean hypercubes

## Finding

Let \(d\ge 2\), \(n=2^d\), and let \(Q_d\) be the graph with vertex set \(V=\mathbb F_2^d\), with an edge whenever two vertices differ in exactly one coordinate. Two identical, noninteracting bosons evolve with uniform nonzero real hopping \(J\) and are irreversibly removed when they occupy the same vertex. The collision-loss rates \(\gamma_x\) may be arbitrary and unequal, provided \(\gamma_x>0\) for every \(x\in V\).

The *complete* nondecaying subspace \(\mathcal D\) has dimension

\[
\boxed{\dim \mathcal D=2^{d-1}(2^d-d-1).}
\]

Its orthogonal complement has dimension \(2^{d-1}(d+2)\). The orthogonal projection onto \(\mathcal D\) is constructed explicitly below by deleting one collision-bright vector from every joint total-momentum/energy sector. For any initial normalized two-boson density operator \(\rho\), the eventual removal probability is exactly

\[
\eta(\rho)=1-\operatorname{Tr}(P_{\mathcal D}\rho).
\]

For an initial normalized symmetric state with the two particles at distinct vertices \(x,y\), at Hamming distance \(s=|x+y|\in\{1,\ldots,d\}\), this specializes to the closed binomial-tail formula

\[
\boxed{\eta_d(s)=\frac{2}{2^d\binom ds}\sum_{j=s}^{d}\binom dj.}
\]

The probability is strictly decreasing in \(s\): in particular \(\eta_d(1)=2(2^d-1)/(d2^d)\) and \(\eta_d(d)=2^{1-d}\). A uniformly chosen distinct-vertex pair has average removal probability \(d/(2^d-1)\), whereas an initially doubly occupied site is removed with probability one. All statements concern ultimate removal, not finite-time decay rates.

## Assumptions and scope

Use the normalized bosonic Hilbert space \(\mathcal H_+=\operatorname{Sym}^2(\mathbb C^{V})\) with position basis \(|x,y\rangle_+=(|x\rangle\otimes|y\rangle+|y\rangle\otimes|x\rangle)/\sqrt2\) for \(x\ne y\), and \(|x,x\rangle=|x\rangle\otimes|x\rangle\). Write \(A_d\) for the usual adjacency operator of \(Q_d\). The Hermitian hopping Hamiltonian is

\[
H=J(A_d\otimes I+I\otimes A_d)|_{\mathcal H_+},\qquad J\in\mathbb R\setminus\{0\}.
\]

The no-jump effective Hamiltonian is \(H_{\mathrm{eff}}=H-i\Gamma/2\), with \(\Gamma=\sum_{x\in V}\gamma_x|x,x\rangle\langle x,x|\) and strictly positive \(\gamma_x\). No on-site disorder, particle-particle interaction, time-dependent coupling, or finite-time loss bound is assumed.

The *dark* subspace is the largest subspace invariant under \(H\) on which every diagonal amplitude \(\langle x,x|\psi\rangle\) vanishes. Since \(H\) is Hermitian, it is the orthogonal sum over energies of the collision-zero kernels inside each energy eigenspace.

## Proof

**1. Decay criterion.** For any eigenvector of \(H_{\mathrm{eff}}\) with real eigenvalue, taking the imaginary part of its own expectation gives \(\langle\psi|\Gamma|\psi\rangle=0\), so positivity forces \(\langle x,x|\psi\rangle=0\) for every \(x\), and \(H\psi\) is an eigenvector. Conversely every eigenvector of \(H\) killed by \(\Gamma\) is nondecaying. The span of these vectors is reducing for both \(H\) and \(\Gamma\); all eigenvalues of the finite-dimensional generator on its orthogonal complement have strictly negative imaginary parts. Jordan blocks on that complement do not obstruct decay, because polynomial factors are dominated by strict exponential decay. Thus the long-time norm-squared of a pure state equals its squared projection onto \(\mathcal D\), and the density-operator formula follows by linearity. This also proves independence from the positive values of the individual \(\gamma_x\).

**2. Fourier/eigenenergy sectors.** For \(p\in\mathbb F_2^d\), set \(\chi_p(x)=(-1)^{p\cdot x}\) and \(|p\rangle=2^{-d/2}\sum_x\chi_p(x)|x\rangle\). The single-particle energy is \(J(d-2|p|)\). The diagonal translations of the two-particle system have total momentum \(k=p+q\in\mathbb F_2^d\). For \(k=0\), the only symmetric Fourier pairs are \(|p,p\rangle\); at energy \(2J(d-2r)\), with \(|p|=r\), their number is \(M_{0,r}=\binom dr\) for \(0\le r\le d\).

For \(k\ne0\), write \(t=|k|\). The symmetric pair indexed by the unordered orbit \(\{p,p+k\}\) has energy

\[
E_{k,r}=J(2d-2t-4r),\quad r=|p\setminus\operatorname{supp}(k)|\in\{0,\ldots,d-t\},
\]

and the number of such unordered pairs is \(M_{k,r}=2^{t-1}\binom{d-t}{r}\). Every pair in one \((k,r)\) block has exactly the same collision diagonal, proportional to \(\chi_k(x)\); it is nonzero. The restriction of diagonal observation to each block therefore has rank exactly one. In coincident-energy blocks with distinct total momenta, the diagonal characters are linearly independent, so no additional cross-block cancellation is possible.

**3. Complete projector and dimension.** Define \(b_{0,r}=M_{0,r}^{-1/2}\sum_{|p|=r}|p,p\rangle\). For \(k\ne0\), choose one representative \(p\) from each orbit \(p\leftrightarrow p+k\) with the stated outside-support weight \(r\), and put

\[
b_{k,r}=M_{k,r}^{-1/2}\sum_{p\in R_{k,r}}|p,p+k\rangle_+.
\]

All these vectors are orthonormal. Each is the unique normalized collision-visible direction within its \((k,r)\) block. Consequently the full projector is

\[
P_{\mathcal D}=I_{\mathcal H_+}-\sum_{r=0}^d|b_{0,r}\rangle\langle b_{0,r}|-\sum_{k\ne0}\sum_{r=0}^{d-|k|}|b_{k,r}\rangle\langle b_{k,r}|.
\]

There are \(d-|k|+1\) such vectors at each total momentum \(k\). Summing their ranks gives

\[
\dim\mathcal D^\perp=\sum_{k\in\mathbb F_2^d}(d-|k|+1)=2^{d-1}(d+2).
\]

Since \(\dim\mathcal H_+=2^{d-1}(2^d+1)\), subtracting yields the stated dimension.

**4. Hamming-distance capture.** Fix \(x\ne y\), let \(z=x+y\), and write \(s=|z|\). For \(m\ge s\), define the binary Krawtchouk coefficient

\[
K_r^{(m)}(s)=[u^r](1-u)^s(1+u)^{m-s}.
\]

The standard Walsh orthogonality identity, proved by applying row orthogonality to the symmetric restriction of the \(2^m\)-character matrix, is

\[
\sum_{r=0}^m\frac{K_r^{(m)}(s)^2}{\binom mr}=\frac{2^m}{\binom ms}.
\]

The square of the overlap of \(|x,y\rangle_+\) with the \((0,r)\) bright vector is \(2^{1-2d}K_r^{(d)}(s)^2/\binom dr\). Its sum over \(r\) is \(2/[2^d\binom ds]\). For \(k\ne0\), the sum over an orbit of Fourier signs vanishes unless \(\operatorname{supp}(k)\cap\operatorname{supp}(z)=\varnothing\). For such \(k\), with \(t=|k|\), the squared \((k,r)\) bright overlap is

\[
\frac{2^{t+1}}{2^{2d}}\frac{K_r^{(d-t)}(s)^2}{\binom{d-t}r}.
\]

Summing over \(r\) gives \(2/[2^d\binom{d-t}s]\). For each \(t\) there are \(\binom{d-s}t\) total momenta disjoint from \(\operatorname{supp}(z)\), including \(k=0\) when \(t=0\). It follows that

\[
\eta_d(s)=\frac{2}{2^d}\sum_{t=0}^{d-s}\frac{\binom{d-s}t}{\binom{d-t}s}
=\frac{2}{2^d\binom ds}\sum_{t=0}^{d-s}\binom dt
=\frac{2}{2^d\binom ds}\sum_{j=s}^{d}\binom dj.
\]

The middle equality uses \(\binom{d-s}t/\binom{d-t}s=\binom dt/\binom ds\). To see strict monotonicity, divide the last binomial tail by its leading term:

\[
\frac{\sum_{j=s}^d\binom dj}{\binom ds}=
1+\sum_{r=1}^{d-s}\prod_{i=1}^r\frac{d-s-i+1}{s+i}.
\]

Every positive product strictly decreases upon increasing \(s\), and the number of products does not increase. Finally \(\sum_{x<y}\eta_d(|x+y|)=\operatorname{Tr}(I-P_{\mathcal D})-2^d=2^{d-1}d\), because each diagonal basis state has capture probability one. Dividing by \(\binom{2^d}2\) gives the mean \(d/(2^d-1)\).

## Verification

The accompanying `check_observability_exact.py` constructs the full bosonic symmetric-coordinate Hamiltonian as an integer matrix, without employing Fourier block counting. It takes the exact finite-field rank of the stacked observability matrix \([D;DH;\ldots;DH^{2d}]\), for \(d=1,2,3,4\), obtaining observed dimensions \(3,8,20,48\) and dark dimensions \(0,2,16,88\). This is a finite diagnostic, not a substitute for the proof for arbitrary \(d\).

The separately implemented `check_spectral_numeric.py` constructs the two-particle Hamiltonian in an orthonormal bosonic position basis, diagonalizes its complete energy sectors, forms the collision-null projector and checks every Hamming-distance capture probability for \(d=1,2,3,4\). All tests pass at numerical tolerance \(10^{-8}\). The projector is Hermitian and idempotent in those tests. These numerical checks corroborate the exact proof and do not certify untested graph dimensions.

## Relationship to prior work

Moore and Russell (arXiv:quant-ph/0104137, originally posted 2001-04-29) analyze one-particle hypercube continuous-time quantum walks using Walsh characters and determine mixing times; in their Section 3 they obtain the one-particle energies. Those characters are an input here, but their work does not impose simultaneous two-particle collision loss or evaluate its dark dimension and Hamming-distance capture law. Krovi and Brun (arXiv:quant-ph/0606094, originally posted 2006-06-10) establish the symmetry/degeneracy mechanism behind infinite-hitting-time subspaces for quantum walks, including continuous time. This is a conceptual antecedent, not an evaluation for two bosons with a detector covering every diagonal pair configuration.

Štefaňák, Kiss, Jex, and Mohring (arXiv:0705.1985, originally posted 2007-05-14) study the *meeting* probability of two coined discrete-time walkers on an infinite line; their fixed-time meeting observable and graph differ from continuous irreversible collision absorption on finite hypercubes. Gamble et al. (arXiv:1002.3003, originally posted 2010-02-16) construct the noninteracting two-boson graph Hamiltonian and examine graph-isomorphism witnesses on strongly regular graphs, but not the collision detector or this Hamming-distance formula. The exact family-specific spectral rank and binomial-tail capture law are the stated contribution, not the underlying Walsh diagonalization, bosonic symmetrization, or general notion of dark states.

## Limitations

The result requires *all* diagonal loss rates to be strictly positive; if some are zero, the dark space can enlarge. Arbitrary variation of hopping rates, interactions, dephasing, discrete-time measurement protocols, and quantitative decay times are outside the result. The primary-literature comparison supports only provisional originality: unindexed equivalent collision-detection computations remain possible. The finite independent tests cover dimensions through four; the proof supplies the quantifiers for all \(d\ge2\). No independent scientific audit or experimental validation is claimed.

## References

1. C. Moore and A. Russell, *Quantum Walks on the Hypercube*, arXiv:quant-ph/0104137 (first public preprint 2001-04-29), https://arxiv.org/abs/quant-ph/0104137.
2. H. Krovi and T. A. Brun, *Quantum walks with infinite hitting times*, arXiv:quant-ph/0606094 (first public preprint 2006-06-10), https://arxiv.org/abs/quant-ph/0606094.
3. M. Štefaňák, T. Kiss, I. Jex, and B. Mohring, *The meeting problem in the quantum random walk*, arXiv:0705.1985 (first public preprint 2007-05-14), https://arxiv.org/abs/0705.1985.
4. J. K. Gamble, M. Friesen, D. Zhou, R. Joynt, and S. N. Coppersmith, *Two-particle quantum walks applied to the graph isomorphism problem*, arXiv:1002.3003 (first public preprint 2010-02-16), https://arxiv.org/abs/1002.3003.
