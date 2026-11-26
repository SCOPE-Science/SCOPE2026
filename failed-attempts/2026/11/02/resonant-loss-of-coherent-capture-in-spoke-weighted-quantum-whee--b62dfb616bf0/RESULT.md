# Resonant loss of coherent capture in spoke-weighted quantum wheels

## Finding

Let a wheel have \(n\ge5\) rim sites \(0,1,\ldots,n-1\), labeled cyclically, and one hub \(h\). Fix rim hopping \(J>0\) and identical hub--rim hopping \(g>0\); put \(a=g/J\). Consider a single excitation with coherent Hamiltonian \(H_0=J A_a\), where \(A_a\) has unit rim-edge weights, weight \(a\) on each spoke, and zero diagonal. Choose two distinct rim absorbers at sites \(0,d\), with \(1\le d\le \lfloor n/2\rfloor\), and arbitrary strictly positive absorber rates.

Put
\[
 m_{n,d}=\left\lfloor\frac{\gcd(n,2d)-1}{2}\right\rfloor,\qquad
 c_k=2\cos\frac{2\pi k}{n},\qquad
 a_k^2=\frac{c_k(c_k-2)}{n}
\]
for integers \(\lfloor n/4\rfloor<k\le\lfloor n/2\rfloor\). All these \(a_k\) are positive and pairwise distinct. Define \(\delta_{n,d}(a)\) to be \(1\) precisely when \(a=a_k\) for one of these indices and \(\exp(2\pi i k d/n)\ne-1\); otherwise let it be \(0\).

**Exact two-rim capture law.** The dark (nonabsorbing) subspace dimension and the bright (eventually absorbed) subspace dimension are
\[
 \boxed{\dim\mathcal D_{0,d}=m_{n,d}+\delta_{n,d}(a),\qquad
 \dim\mathcal K_{0,d}=n+1-m_{n,d}-\delta_{n,d}(a).}
\]
For any initial density matrix \(\rho\), its eventual capture probability is \(\operatorname{tr}(\Pi_{\mathcal K_{0,d}}\rho)\). Consequently, for the maximally mixed initial excitation \(I/(n+1)\), it is exactly \((n+1-m_{n,d}-\delta_{n,d}(a))/(n+1)\), independently of both strictly positive loss rates.

**Resonant blackout of perfect pair capture.** For every resonance associated with an index \(k<n/2\), no two rim sites yield full eventual capture of *every* initial state: every placement leaves at least one dark mode. Away from resonances, two rim absorbers yield full capture precisely when \(\gcd(n,2d)\le2\). For even \(n\), at the endpoint resonance \(k=n/2\), full capture remains possible (for instance at spacing \(d=1\)). If one absorber instead occupies the hub and the other any rim site, the bright dimension is always \(2+\lfloor n/2\rfloor\), independent of all positive spoke weights and loss rates.

For example, when \(n=12\) and \(g=J/2\), the negative radial eigenvalue coincides with the \(k=4\) rim eigenvalue \(-1\). The accessible dimensions for rim-pair distances \(d=1,\ldots,6\) are respectively \(12,11,10,11,12,7\), one below the corresponding generic values \(13,12,11,12,13,8\). In particular, adjacent absorbers lose perfect capture at this *single exact coupling*.

## Assumptions and scope

The graph is finite and simple, the single-excitation Hamiltonian uses **adjacency hopping**, all spokes have identical real positive weights, and there are no additional diagonal energies, magnetic fluxes, losses, dephasing, or coherent interactions. The generator on the graph subspace is
\[
 H_{\mathrm{eff}}=J A_a-i\gamma_0|0\rangle\langle0|-i\gamma_d|d\rangle\langle d|,
 \qquad\gamma_0,\gamma_d>0.
\]
The time evolution of its unnormalized graph density matrix is \(\rho(t)=e^{-itH_{\mathrm{eff}}}\rho(0)e^{itH_{\mathrm{eff}}^\dagger}\). Its lost trace is the absorbed probability. Distances are measured in rim edges, not through the hub. All equalities hold for every allowed real \(a>0\), including exact resonances.

## Proof

**1. Capture is orthogonal projection onto a spectral bright space.** Write \(\Gamma=\gamma_0|0\rangle\langle0|+\gamma_d|d\rangle\langle d|\), and let \(\mathcal K=\operatorname{span}\{A_a^r|0\rangle,A_a^r|d\rangle:r\ge0\}\). Because \(A_a\) is real symmetric, \(\mathcal D=\mathcal K^\perp\) is invariant under \(A_a\), and all vectors in \(\mathcal D\) have zero amplitudes at both absorbers. Thus \(\Gamma\) annihilates \(\mathcal D\), and the effective generator is block diagonal on \(\mathcal D\oplus\mathcal K\). An eigenvector in \(\mathcal K\) of \(H_{\mathrm{eff}}\) with real eigenvalue would satisfy \(\langle v,\Gamma v\rangle=0\) by taking imaginary parts; hence it would be an eigenvector of \(A_a\) orthogonal to both absorber sites, and so belong to \(\mathcal D\), a contradiction. Every eigenvalue of the finite bright block therefore has strictly negative imaginary part. Its evolution decays to zero, while \(\mathcal D\) evolves unitarily. Hence the surviving trace tends to \(\operatorname{tr}(\Pi_{\mathcal D}\rho)\), proving the absorption law and rate independence. This argument does not assume that the dissipative block is diagonalizable.

**2. Exact spectral decomposition.** Set \(|u\rangle=n^{-1/2}\sum_{j=0}^{n-1}|j\rangle\). The radial subspace spanned by \(|u\rangle,|h\rangle\) has matrix
\[
 \begin{pmatrix}2&a\sqrt n\\ a\sqrt n&0\end{pmatrix},
\]
whose distinct eigenvalues are \(\lambda_\pm=1\pm\sqrt{1+na^2}\). The perpendicular rim Fourier sector has eigenvalues \(c_k\), \(1\le k\le\lfloor n/2\rfloor\). For \(k<n/2\), each Fourier eigenspace has dimension \(2\), with conjugate characters \(j\mapsto e^{\pm2\pi i kj/n}\); for even \(n\) and \(k=n/2\), it has dimension \(1\). These Fourier eigenvalues are distinct as \(k\) increases. Also \(\lambda_+>2\), so it never collides with a rim eigenvalue. The strictly negative, decreasing \(\lambda_-\) equals \(c_k\) exactly at the displayed positive coupling \(a=a_k\), and only for \(c_k<0\). Thus at most one Fourier eigenvalue collides for any fixed spoke coupling.

**3. Nonresonant absorber rank.** By the spectral theorem and polynomial interpolation at the distinct eigenvalues, the dimension of \(\mathcal K\) is the sum, over distinct eigenvalues, of the ranks of the projections of \(|0\rangle,|d\rangle\) to their eigenspaces. At the two radial eigenvalues each contributes rank \(1\), because its rim component is a nonzero constant. At a two-dimensional Fourier eigenspace the two probes have evaluation matrix proportional to
\[
 \begin{pmatrix}1&1\\ e^{i\theta_k}&e^{-i\theta_k}\end{pmatrix},\qquad\theta_k=2\pi kd/n,
\]
whose rank is \(1\) exactly when \(\sin\theta_k=0\), and otherwise \(2\). The even-cycle highest mode is intrinsically one-dimensional. Hence the total dark dimension is the number of indices \(1\le k<n/2\) satisfying \(n\mid2kd\). Writing \(q=\gcd(n,2d)\), these indices are the multiples of \(n/q\) strictly below \(n/2\); their number is exactly \(\lfloor(q-1)/2\rfloor=m_{n,d}\).

**4. Resonant rank loss.** At \(a=a_k\), the negative radial eigenspace merges with exactly one Fourier eigenspace. In a basis consisting of the two Fourier characters and one radial mode, the two absorber-site restrictions are, up to nonzero column scalings,
\[
 \begin{pmatrix}1&1&1\\ e^{i\theta_k}&e^{-i\theta_k}&1\end{pmatrix}.
\]
For \(k=n/2\) (even \(n\)), remove one redundant Fourier column. The merged restriction has rank \(1\) when \(e^{i\theta_k}=1\) and rank \(2\) otherwise. Before collision the separate radial and Fourier eigenspaces would contribute total probe rank \(1+2\) if \(\sin\theta_k\ne0\), or \(1+1\) otherwise. Consequently precisely one extra dark mode appears except when \(e^{i\theta_k}=-1\), in which case the rank is unchanged. This is exactly \(\delta_{n,d}(a)\), proving the dimension formula.

**5. Universal resonant obstruction and hub placement.** If \(n\) is odd, \(e^{2\pi i kd/n}=-1\) is impossible, so every resonance produces a dark mode. If \(n=2s\) is even and a pair has no generic dark mode, then \(\gcd(s,d)=1\). For \(k<s\), the equation \(e^{2\pi i kd/n}=-1\) would imply \(kd\equiv s\pmod{2s}\), hence \(s\mid k\), a contradiction. Thus no rim pair has full capture at an interior resonance. For \(k=s\), the phase equals \((-1)^d\), so \(d=1\) retains full capture. Finally, for a hub/rim pair, the hub detects both radial eigenvectors and the rim detects one direction of every Fourier eigenspace. At a radial--Fourier collision these remain two independent detector directions, so the contribution is unchanged. There are \(2\) radial and \(\lfloor n/2\rfloor\) Fourier spectral values, yielding the claimed hub--rim rank.

## Verification

The accompanying standalone `checker.py` independently forms full Krylov matrices, using an exact diagonal similarity that replaces spoke weights \(a\) by rational entries \(1\) and \(a^2\) without changing their ranks. It checks 5,194 modular ranks over two different prime fields for seven positive rational values of \(a^2\), all \(5\le n\le37\), all rim-pair separations, and hub/rim pairs. It also checks 16 small ranks by exact rational Gaussian elimination, including the tuned resonances at \((n,a^2)=(6,1/2),(8,1),(12,1/4)\), and nine ranks in the exact quadratic field \(\mathbb Q(\sqrt5)\) at the irrational resonances with \(n=5\) and \(n=10\). Run `python checker.py` with Python 3 and no third-party packages. The included `checker_output.txt` records the checked outputs. The finite computations independently test the finite cases only; the five proof steps establish the theorem for all allowed parameters and all sizes.

## Relationship to prior work

Coherent excitation capture and trapping with complex absorbing potentials were studied by Mülken and coauthors (2007), and Agliari, Mülken and Blumen (2009) analyzed cycle trapping. Godsil (2010) developed graph controllability via adjacency walk matrices, and Novo and coauthors (2015) established the Krylov/invariant-subspace framework for transport; both are used here, not claimed as new. Two separately monitored sites correspond to a two-input controllability problem, not a single broadcast characteristic-vector input. Wong and Philipp (2016) showed that weighted edges can improve quantum search on linked cliques, a different Hamiltonian and outcome. Xu, Ide and Konno (2012) treated trapping on a cycle with one extra chord, using a graph Laplacian rather than the positive weighted-wheel adjacency model. Le and coauthors (2017) demonstrated general dark-state suppression by changing graph weights and topology, but not the exact two-rim weighted-wheel resonance and arithmetic exception proved here.

The distinctive result is the complete *spoke-weight parameter* and *rim-pair placement* classification, especially the one-dimensional loss of capture at isolated radial/Fourier eigenvalue collisions and the proof that an interior collision obstructs perfect two-rim capture at every placement. A previous exact coherent-cycle result gives the underlying arithmetic dark-mode count without a hub; this result does not claim novelty for that cycle count. None of the inspected sources establishes the weighted-wheel parameter formula as a stated theorem or a directly covering stronger result. An additional 2014 paper on general adjacency controllability could be inspected only at abstract level; its full text is a residual priority risk. Historical priority remains subject to broader independent examination.

## Limitations

This is an exact finite-network asymptotic-capture theorem: it says nothing quantitative about absorption times or the dynamical timescale near resonances. The limits \(t\to\infty\) and \(a\to a_k\) need not commute. Finite-time dynamics is continuous in \(a\), so the exact discontinuity in the eventual capture fraction should not be interpreted as finite-time instability. The result does not cover diagonal disorder, loss at extra sites, unequal spokes, non-Hermitian hopping, interacting excitations, or dephasing. Spectral priority beyond the inspected literature has not been independently audited.

## References

1. O. Mülken et al., *Survival Probabilities in Coherent Exciton Transfer with Trapping*, arXiv:0705.3700v1 (25 May 2007), https://arxiv.org/abs/0705.3700.
2. E. Agliari, O. Mülken, and A. Blumen, *Continuous-Time Quantum Walks and Trapping*, arXiv:0903.3288v1 (19 March 2009), https://arxiv.org/abs/0903.3288.
3. X.-P. Xu, Y. Ide, and N. Konno, *Symmetry and localization of quantum walk induced by extra link in cycles*, arXiv:1202.4208 (2012), https://arxiv.org/abs/1202.4208.
4. L. Novo et al., *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, Scientific Reports 5, 13304 (2015), https://doi.org/10.1038/srep13304.
5. T. G. Wong and P. Philipp, *Engineering the Success of Quantum Walk Search Using Weighted Graphs*, arXiv:1605.04862v1 (16 May 2016), https://arxiv.org/abs/1605.04862.
6. T. P. Le et al., *How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures*, arXiv:1707.07482v1 (24 July 2017), https://arxiv.org/abs/1707.07482.

7. C. Godsil, *Controllable Subsets in Graphs*, arXiv:1010.3231v1 (15 October 2010), https://arxiv.org/abs/1010.3231.
8. A. Farrugia and I. Sciriha, *Controllability of undirected graphs*, Linear Algebra and its Applications 454 (2014), 138–157; repository abstract, https://www.um.edu.mt/library/oar/handle/123456789/28166.
