# The signed finite-section law for compact Cesàro self-commutators

## Finding
Let \(0<t<1\), let \(C_t\) be the generalized Cesàro operator on \(\ell^2(\mathbb N_0)\), and put \(H_t=C_t^*C_t-C_tC_t^*\). For the projection \(P_N\) onto the first \(N\) coordinates, let \(N_-(N,t)\) and \(N_+(N,t)\) count the strictly negative and strictly positive eigenvalues, with multiplicity, of the **compression of the infinite self-commutator** \(P_NH_tP_N\) on \(P_N\ell^2\). Then
\[
\lim_{N\to\infty}\frac{N_-(N,t)}N=\frac{\arccos t}{\pi},\qquad
\lim_{N\to\infty}\frac{N_+(N,t)}N=1-\frac{\arccos t}{\pi}.
\]
In particular, for every \(0<t<1\), the trace-class self-adjoint operator \(H_t\) has infinitely many strictly positive and infinitely many strictly negative eigenvalues. At \(t=0\), \(H_0=0\); nevertheless \(H_t\to0\) in trace norm as \(t\downarrow0\), while the negative finite-section fraction tends to \(1/2\) after the large-section limit.

## Assumptions and scope
The Hilbert space is complex \(\ell^2(\mathbb N_0)\). The matrix is
\[
(C_t)_{nj}=\begin{cases}t^{n-j}/(n+1),&0\le j\le n,\\0,&j>n.\end{cases}
\]
Every limit in \(N\) holds for each **fixed** \(t\in(0,1)\). The two limits \(t\downarrow0\) and \(N\to\infty\) are not interchanged. The finite matrices are principal compressions of \(H_t\), **not** the self-commutators of truncated \(C_t\) matrices. Primary classification: 47B37 (operators on sequence spaces).

## Proof
**1. Trace class and exact kernel.** Since
\[
\|C_t\|_{\mathcal S_2}^2=\sum_{n=0}^\infty\frac{1-t^{2(n+1)}}{(n+1)^2(1-t^2)}<\infty,
\]
\(H_t\) is self-adjoint and trace class. For \(j=i+k\), \(i,k\ge0\), set \(m=i+1\) and \(q=t^2\). Matrix multiplication gives exactly
\[
(H_t)_{i,i+k}=t^k\left[\sum_{\ell=0}^\infty\frac{q^\ell}{(m+k+\ell)^2}-\frac{1-q^m}{m(m+k)(1-q)}\right].\tag{1}
\]
The other entries are determined by real symmetry. Define \(A_0=(1-q)^{-1}\) and \(A_1=q(1-q)^{-2}\). For fixed \(k\), expanding the summands in (1) at large \(m\) yields
\[
\lim_{i\to\infty}[(i+1)(i+k+1)]^{3/2}(H_t)_{i,i+k}
=b_k:=-t^k(kA_0+2A_1).\tag{2}
\]

**2. Uniform Toeplitz approximation on remote blocks.** For \(s=m+k\), let
\[
\Delta_s=\sum_{\ell\ge0}q^\ell\left(s^{-2}-(s+\ell)^{-2}\right),\qquad 0\le\Delta_s\le2A_1s^{-3}.
\]
An exact rearrangement of (1) is
\[
 t^{-k}(H_t)_{i,i+k}=-\frac{A_0k}{ms^2}-\Delta_s+\frac{A_0q^m}{ms}.
\]
After multiplication by \((ms)^{3/2}\), its three terms are bounded respectively by \(A_0k\), \(2A_1\), and \(A_0q^m\sqrt{ms}\). On the indices \(i,j\ge\lfloor\varepsilon N\rfloor\), \(i,j<N\), for every fixed \(0<\varepsilon<1\), the last quantity is bounded uniformly by \(C_{t,\varepsilon}q^{\lfloor\varepsilon N\rfloor}(N+1)\to0\). Thus the full scaled matrix has an exponentially summable off-diagonal majorant of the form \(C_t(k+1)t^k\). Using (2) for each fixed \(k\) and then cutting off the summable tails proves **operator-norm** convergence
\[
\left\|D_{N,\varepsilon}\bigl(P_{[\varepsilon N,N)}H_tP_{[\varepsilon N,N)}\bigr)D_{N,\varepsilon}
-T_{N-\lfloor\varepsilon N\rfloor}(b)\right\|\longrightarrow0,\tag{3}
\]
where \(D_{N,\varepsilon}\) is diagonal with entries \((j+1)^{3/2}\), and \(T_L(b)=(b_{|i-j|})_{0\le i,j<L}\). Positive diagonal congruence preserves the numbers of positive and negative eigenvalues.

**3. Exact Toeplitz symbol and its signs.** The absolutely summable coefficients in (2) have continuous real symbol
\[
h_t(\theta)=b_0+2\sum_{k\ge1}b_k\cos(k\theta)
=\frac{2t(t-\cos\theta)}{(1-2t\cos\theta+t^2)^2}.\tag{4}
\]
This identity follows by summing \(\sum_{k\ge1}z^k\) and \(\sum_{k\ge1}kz^k\) with \(z=te^{i\theta}\), taking real parts, and simplifying. The denominator is strictly positive for \(t<1\); hence the symbol is negative exactly where \(\cos\theta>t\), positive exactly where \(\cos\theta<t\), and zero at only two circle points.

**4. Count signs.** For any continuous real Toeplitz symbol with absolutely summable Fourier coefficients and a zero set of measure zero, the fraction of positive/negative eigenvalues of its finite Toeplitz matrices converges to the corresponding sign-set measure. To see this directly here, approximate the symbol uniformly by a trigonometric polynomial of degree \(K\). A banded Toeplitz matrix differs from the periodic circulant with the same coefficients by a matrix of rank at most \(2K\); circulant eigenvalues are samples of that polynomial on an equally spaced grid. First take matrix length to infinity, then \(K\to\infty\), bounding uncertain signs by the measure where \(|h_t|\) is small. Since its zero set has measure zero, this proves
\[
\frac{N_-(T_L(b))}{L}\to\frac{|\{\theta\in[-\pi,\pi]:\cos\theta>t\}|}{2\pi}=\frac{\arccos t}{\pi},
\]
and the complementary positive fraction. Operator-norm convergence (3) preserves these proportions by the same spectral-gap-near-zero argument. Cauchy interlacing between the remote principal block and the full \(N\)-compression changes each sign count by at most \(\lfloor\varepsilon N\rfloor\). Letting \(N\to\infty\) and then \(\varepsilon\downarrow0\) proves the displayed two limits.

**5. Infinite inertia and the endpoint.** A compact self-adjoint operator with only finitely many negative (respectively positive) eigenvalues cannot have arbitrarily large-dimensional negative (respectively positive) definite subspaces. The divergent finite-section sign counts therefore force infinitely many eigenvalues of each sign. At \(t=0\), \(C_0\) is real diagonal and \(H_0=0\). The defining matrix implies \(\|C_t-C_0\|_{\mathcal S_2}\to0\) by dominated convergence; the trace-ideal product estimate yields \(\|H_t\|_{\mathcal S_1}\to0\). This completes the proof.

## Verification
The standalone `checker.py` reconstructs the exact infinite self-commutator compressions via a geometric-tail recurrence rather than confusing them with commutators of truncated operators. For \(t=0.2,0.5,0.8\), it compares the negative finite-section fractions to \(\arccos(t)/\pi\), checks remote scaled matrix entries against (2), and independently integrates (4) to reconstruct its Fourier coefficients. It passed 51 finite assertions. The count limits, exact rational/trigonometric simplification, and infinite-inertia conclusions follow from the analytic proof, not finite tests.

## Relationship to prior work
Generalized Cesàro operators and their compactness, eigenvalues and dynamics are studied by Curbera–Ricker and Albanese–Bonet–Ricker. The latter full-text treatment gives the same matrix and compactness framework, but does not study the signed finite-section distribution of the self-commutator. Existing Cesàro self-commutator work on the classical nondamped matrix and on additive shift/deformation parameters concerns different operator families; it neither yields formula (4) nor the exact \(\arccos(t)/\pi\) signature fraction. The relevant Toeplitz finite-section principle is classical and is used as a tool, not claimed new.

## Limitations
This theorem counts **signs of eigenvalues of principal compressions**, not their individual magnitudes or the asymptotic distribution after a universal rescaling; it does not assert an eigenvalue Weyl coefficient. The statement is for fixed \(0<t<1\); the corner limits \(t\to0\) and \(t\to1\) may not be uniform in section size. The prior-art comparison does not establish independent historical priority; unindexed spectral finite-section work is a residual risk.

## References
1. G. P. Curbera and W. J. Ricker, *Fine spectra and compactness of generalized Cesàro operators in Banach lattices*, arXiv:2302.08750 (first posted 2023-02-17). https://arxiv.org/abs/2302.08750
2. A. A. Albanese, J. Bonet, and W. J. Ricker, *Spectral properties of generalized Cesàro operators in sequence spaces*, arXiv:2305.04805 (first posted 2023-05-08), DOI:10.1007/s13398-023-01470-2. https://link.springer.com/article/10.1007/s13398-023-01470-2
3. G. Szegő, *On certain Hermitian forms associated with the Fourier series of a positive function* (classical Toeplitz eigenvalue-distribution principle); the finite-band circulant argument is supplied here to avoid relying on a black-box theorem.
