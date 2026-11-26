# Two-level Fourier conditioning under crossed checkerboard sensor jitter

## Finding
For all even integers \(M,N\ge2\) and all real \(\delta,\varepsilon\), a two-way stagger of the complete tensor Fourier grid has at most two distinct squared singular values, independent of the grid dimensions. With \(s=|\sin(\pi\delta)\sin(\pi\varepsilon)|\), the squared singular-value multiset contains \(MN/2\) copies of \(1-s\) and \(MN/2\) copies of \(1+s\). These levels are distinct for \(s>0\) and coincide at \(1\) with total multiplicity \(MN\) for \(s=0\). Thus, if \(s<1\),
\[
\kappa_2(A)=\sqrt{\frac{1+s}{1-s}},
\qquad \|A^{-1}\|_2=(1-s)^{-1/2}.
\]
At \(s=1\), the rank drops to exactly \(MN/2\). If \(\delta\) or \(\varepsilon\) is an integer, the operator remains unitary regardless of the other displacement. An explicit paired-frequency inverse follows from the proof.

## Assumptions and scope
The unknown is a complex trigonometric polynomial on the two-dimensional unit torus with the complete rectangle of frequencies \(\{0,\ldots,M-1\}\times\{0,\ldots,N-1\}\). The \(MN\) sample positions, taken modulo one, are
\[
x_{j,k}=\frac{j+\delta(-1)^k}{M},\qquad y_{j,k}=\frac{k+\varepsilon(-1)^j}{N},
\quad 0\le j<M,\;0\le k<N.
\]
The normalized coefficient-to-data matrix is
\[
 A_{(j,k),(m,n)}=\frac{1}{\sqrt{MN}}e^{2\pi i(mx_{j,k}+ny_{j,k})}.
\]
Both side lengths are positive even integers; the two real offsets are unrestricted. Singular values and condition number refer to the ordinary Euclidean coefficient and sample norms.

## Proof
Write \(u=(m,n)\) and \(v=(m',n')\), and put \(d=m'-m\), \(e=n'-n\). Direct multiplication and separation of the sums give
\[
(A^*A)_{u,v}=P_M(d,2\pi e\varepsilon/N)\,P_N(e,2\pi d\delta/M),
\]
where, for even \(L\),
\[
P_L(t,\theta)=\frac1L\sum_{a=0}^{L-1}e^{2\pi i ta/L}e^{i\theta(-1)^a}
=\mathbf1_{t\equiv0\pmod L}\cos\theta+i\mathbf1_{t\equiv L/2\pmod L}\sin\theta.
\]
The last identity is exact: use \(e^{i\theta(-1)^a}=\cos\theta+i(-1)^a\sin\theta\) and geometric orthogonality. Since the frequency indices are each taken in a single complete interval of length \(M\) or \(N\), an off-diagonal Gram entry can survive only if \(d\equiv M/2\pmod M\) **and** \(e\equiv N/2\pmod N\). If exactly one difference vanishes while the other is a half-period, the remaining sine factor vanishes. For the double half-period, the entry is real, with sign depending on the chosen representative difference, and absolute value
\[
|\sin(\pi\delta)\sin(\pi\varepsilon)|=s.
\]
Thus the Gram matrix is \(I+H\), where \(H\) is Hermitian, its only potentially nonzero entries pair each \((m,n)\) with \((m+M/2\pmod M,\;n+N/2\pmod N)\), and every such entry has modulus \(s\). The partner map is a fixed-point-free involution, giving exactly \(MN/2\) independent two-by-two blocks
\[
\begin{pmatrix}1&h\\\overline h&1\end{pmatrix},\qquad |h|=s.
\]
Their eigenvalues are \(1\pm s\). This proves the multiplicities, sharp frame bounds, invertibility, rank, and condition number, including \(s=0,1\), without asymptotics or perturbative assumptions.

For \(s<1\), the pairing matrix satisfies \(H^2=s^2I\), hence
\[
(A^*A)^{-1}=\frac{I-H}{1-s^2},\qquad A^{-1}=\frac{I-H}{1-s^2}A^*.
\]
The adjoint requires only four ordinary rectangular Fourier transforms: expanding each of the two factors \(e^{-2\pi i m\delta(-1)^k/M}\), \(e^{-2\pi i n\varepsilon(-1)^j/N}\) into cosine and parity-weighted sine produces the transforms of the input data multiplied by \(1,(-1)^j,(-1)^k,(-1)^{j+k}\). Their scalar frequency-dependent linear combination gives \(A^*\) exactly. Applying the paired correction costs \(O(MN)\) more, yielding \(O(MN\log(MN))\) arithmetic complexity with standard FFT implementations.

## Verification
The companion `checker.py` uses only the Python standard library. It builds the full complex matrix at several even rectangular sizes and offsets and compares every directly summed Gram entry with the explicit partner-only formula. It also checks the quadratic identity for the predicted off-diagonal part. These are finite diagnostics; the proof above establishes the all-size spectrum and its frame bounds.

## Relationship to prior work
Alberti, Housholder, Iosevich, Miller and Palsson study Fourier-ratio sampling and model independently displaced sensors through measurement-error bounds, rather than an exact eigenspectrum for structured two-coordinate jitter. Yu and Townsend give nonuniform DFT stability bounds for arbitrary one-dimensional perturbed grids. Austin and Trefethen study convergence of trigonometric interpolation and quadrature under one-dimensional perturbations. Chen, Lin and Zhang use periodic nonuniform sampling to estimate singular-value bounds; their Theorem 1.4 is an inverse-norm bound for one-dimensional shifted nodes. These results do not give the product-of-sines spectrum of the two-dimensional crossed pattern. The exact unitary cases and singular boundary provide benchmarks against general perturbation estimates.

## Limitations
The theorem concerns full rectangular Fourier bandwidth and precisely two-periodic crossed displacements. It does not cover arbitrary independently jittered nodes, incomplete Fourier sampling, odd side lengths, or nonlinear noisy recovery. The absence of a presently identified equivalent published theorem is not a proof of historical novelty. At the singular boundary, only the rank statement is made; inversion is impossible.

## References
- N. Alberti, C. Housholder, A. Iosevich, S. J. Miller and E. A. Palsson, *Fourier Ratio Bounds and Sensitivity to Sensor Placement*, arXiv:2611.19755v1 (first public 2026-11-15), https://arxiv.org/html/2611.19755v1.
- A. Yu and A. Townsend, *On the stability of unevenly spaced samples for interpolation and quadrature*, arXiv:2202.04722 (2022), https://arxiv.org/abs/2202.04722.
- A. P. Austin and L. N. Trefethen, *Trigonometric Interpolation and Quadrature in Perturbed Points*, arXiv:1612.04018 (2016), https://arxiv.org/abs/1612.04018.
- L. Chen, R. Lin and H. Zhang, *Smallest Singular Value Estimates for Nonuniform Fourier Matrices via Periodic Nonuniform Sampling*, arXiv:2608.21960v4 (2026), https://arxiv.org/abs/2608.21960v4.
