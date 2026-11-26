# An exact arithmetic Riesz-spectrum trichotomy on an unbounded translational tile

## Finding

There is an explicit unbounded measurable set \(\Omega\subset\mathbb R\), of Lebesgue measure one, which is a fundamental domain for integer translations, with the following sharp property. For each real \(\alpha\), consider the *indexed* exponential family
\[
\mathcal E_\alpha=\{e^{2\pi i(2n)x}:n\in\mathbb Z\}\ \cup\ \{e^{2\pi i(2n+\alpha)x}:n\in\mathbb Z\}
\quad\text{in }L^2(\Omega).
\]
If \(\alpha=a/b\) is expressed in lowest terms, with \(b>0\), then:

1. If \(a\) is odd, \(\mathcal E_\alpha\) is a Riesz basis with the **exact** squared synthesis bounds
\[
A_\alpha=1-\cos\!\left(\frac{\pi}{2b}\right),\qquad
B_\alpha=1+\cos\!\left(\frac{\pi}{2b}\right).
\]
2. If \(a\) is even, the family is incomplete and has a nontrivial synthesis kernel.
3. If \(\alpha\) is irrational, the family is complete and Bessel, but it is not a frame (and has no positive lower Riesz bound).

For odd \(a\), the ratio of sharp squared bounds is
\[
\frac{B_\alpha}{A_\alpha}=\cot^2\!\left(\frac{\pi}{4b}\right).
\]
Thus \(\alpha=1\) gives an orthonormal basis, while arbitrarily small irrational perturbations of the second frequency coset destroy the frame property. The rational perturbations \(\alpha=1+1/b\) for even positive \(b\) retain bases, but their squared-bound ratios grow as \(16b^2/\pi^2\).

## Assumptions and scope

For \(j\ge0\) define
\[
E_j=\left[1-2^{-(j+1)},\ 1-2^{-(j+2)}\right),
\quad m_0=0,\quad m_{2k-1}=k,\quad m_{2k}=-k\quad(k\ge1).
\]
The intervals \(E_j\) are disjoint, each has positive length, and their union is \([1/2,1)\). The sequence \((m_j)_{j\ge0}\) lists each integer exactly once. Set
\[
\Omega=[0,1/2)\ \cup\ \bigcup_{j\ge0}(E_j+m_j).
\]
The union is disjoint up to boundaries, as translations preserve the disjoint residues modulo one. Its reduction modulo \(\mathbb Z\) is a measure-preserving bijection almost everywhere onto \([0,1)\); consequently \(|\Omega|=1\), and integer translates of \(\Omega\) tile \(\mathbb R\) at multiplicity one. The set is unbounded in both directions.

The exponential family is indexed by two copies of \(\mathbb Z\). If the cosets collide, repeated elements count separately, making any Riesz-basis claim false. Norms use unnormalized Lebesgue measure. The Fourier convention is \(e_\lambda(x)=e^{2\pi i\lambda x}\). “Sharp bounds” refer to the best constants in the squared synthesis inequalities for finite coefficient sequences, then by completion.

## Proof

**Two-channel unitary fiberization.** Write \(J_j=E_j-1/2\), which partition \([0,1/2)\). For \(t\in J_j\) the only points of \(\Omega\) congruent modulo \(1/2\) to \(t\) are \(t\) and \(t+1/2+m_j\). Translation provides a unitary map
\[
U:L^2(\Omega)\longrightarrow L^2\!\left([0,1/2);\mathbb C^2\right),
\quad Uf(t)=\bigl(f(t),f(t+1/2+m_j)\bigr)\ (t\in J_j).
\]
For finite sequences \((c_n)\) and \((d_n)\), let
\[
C(t)=\sum_n c_ne^{4\pi int},\qquad D(t)=\sum_n d_ne^{4\pi int}.
\]
The Fourier basis on \([0,1/2)\) has squared norm \(1/2\); hence
\[
\sum_n(|c_n|^2+|d_n|^2)=2\int_0^{1/2}(|C(t)|^2+|D(t)|^2)\,dt.
\]
At each \(t\in J_j\), synthesis is multiplication by the matrix
\[
M_j(t)=\begin{pmatrix}
1&e^{2\pi i\alpha t}\\
1&e^{2\pi i\alpha(t+1/2+m_j)}
\end{pmatrix}.
\]
The two eigenvalues of the normalized Gram matrix \(\frac12M_j(t)^*M_j(t)\) are
\[
1\pm\left|\cos\left(\pi\alpha(m_j+1/2)\right)\right|.
\]
Because each \(J_j\) has *positive* measure, the exact best global synthesis bounds (the lower one may be zero) are
\[
1-\rho(\alpha)\quad\text{and}\quad 1+\rho(\alpha),\qquad
\rho(\alpha)=\sup_{m\in\mathbb Z}\left|\cos\left(\pi\alpha(m+1/2)\right)\right|.
\]
Sharpness follows by selecting unit-norm measurable eigenvectors on any one \(J_j\), and approximating these coefficient functions in \(L^2([0,1/2))^2\) by finite Fourier polynomials. Every fiber matrix has norm at most two, proving Bessel boundedness for all \(\alpha\).

**Arithmetic evaluation.** If \(\alpha=a/b\) is reduced and \(a\) odd, then the odd integers \(a(2m+1)\) run through all odd residue classes modulo \(2b\). No such residue is divisible by \(2b\), and the closest one to a multiple of \(2b\) has distance one. Therefore
\[
\rho(a/b)=\cos\!\left(\frac{\pi}{2b}\right)<1.
\]
If \(a\) is even, coprimality forces \(b\) odd; choose \(m=(b-1)/2\) to obtain \(a(m+1/2)/b=a/2\in\mathbb Z\), so \(\rho(a/b)=1\), with an *exact singular fiber* on the interval \(J_j\) corresponding to this \(m\). If \(\alpha\notin\mathbb Q\), the sequence \(\alpha(m+1/2)\) modulo one is dense by irrational-rotation density. None is an integer, but the supremum of the absolute cosine is one. In this case every fiber matrix is invertible, with no uniform inverse bound.

**Basis, completeness and frame statements.** When \(\rho(\alpha)<1\), multiplication by \(M_j(t)\) on the direct-integral fibers has an essentially bounded inverse. Composing it with the two Fourier-series isomorphisms gives boundedly invertible synthesis, so the family is a Riesz basis with the computed sharp bounds. If \(a\) is even, the positive-measure singular fiber gives a nonzero element in the orthogonal complement of the synthesis range (and a nonzero coefficient kernel), hence incompleteness. If \(\alpha\) is irrational, all fibers are invertible almost everywhere, so the adjoint multiplication operator has zero kernel and the synthesis range is dense. Its lower synthesis bound vanishes by the preceding sharpness argument, and the same fiber eigenvalues show that the adjoint also has no positive lower bound: the complete Bessel family is not a frame. This also establishes the asserted trichotomy without assuming that a complete Bessel family is automatically a basis.

**Discontinuous stability and asymptotics.** At \(\alpha=1\), the frequency family is precisely all integer exponentials, an orthonormal basis for this integer-translation fundamental domain. Irrational numbers arbitrarily close to one have no lower frame bound. With \(b\) even, \(\alpha=1+1/b=(b+1)/b\) has odd reduced numerator and
\[
\frac{B_\alpha}{A_\alpha}
=\cot^2\!\left(\frac{\pi}{4b}\right)
\sim \frac{16b^2}{\pi^2}\qquad (b\to\infty,\ 2\mid b).
\]
The failure of uniform frequency stability is consistent with the fact that changing \(\lambda\) by a tiny amount need not change \(e^{2\pi i\lambda x}\) uniformly or in an operator-small manner on an unbounded domain.

## Verification

The independent-of-proof consistency program `CHECK.py` uses only the Python standard library. It reconstructs sample Gram eigenvalues of the two-by-two fiber matrices, tests the exact odd/even numerator rule across rational parameters, checks finite segments of the explicit partition, and finds near-resonances for illustrative irrational parameters. Its run printed `TWO_COSET_UNBOUNDED_TILE_CHECKS_PASSED 3049`. These finite calculations are checks only: the infinite trichotomy relies on the analytic fiberization, elementary modular arithmetic and irrational-rotation density proved above. Reproduce with `python CHECK.py`.

## Relationship to prior work

Cabrelli and Carbajal (2017/2018), particularly their fiber criterion and Examples 2.6, 2.7 and 3.3, analyze unbounded multi-tiles and countable translated partitions. Their results provide the relevant general structure, but their examples neither specify this half-integer all-height tile nor classify every two-coset offset by numerator parity and sharp constants. Frederick and Mayeli (2022) connect exponential Riesz bases of tiling sets to indicator-window Gabor Riesz bases; the current result concerns explicit exponential spectra and does not claim that qualitative transfer as new. Asipchuk and Drezels (2022) treat interval unions and give sufficient exact-gap conditions, not the present all-parameter trichotomy for a fixed two-sided unbounded tile. A publicly available calculation for two bounded separated unit intervals obtains exact two-coset bounds controlled by just two translation heights; its bounded finite-height problem does not imply the arithmetic classification on the infinite set of *all* heights.

The basic fiber matrix calculation itself is established methodology. The claim here is its exact arithmetic consequence on a fixed natural unbounded tile: complete-but-nonframe irrational offsets, an even-numerator incompleteness obstruction, odd-numerator sharp bounds, and arbitrarily small nonframe detuning from an orthogonal basis. An equivalent special construction under another normalization could remain unrecognized in earlier specialized literature.

## Limitations

The theorem concerns this explicitly constructed set and the prescribed two-coset frequency family; it is not a classification of all spectra of arbitrary unbounded tiles. It does not assert that *every* small perturbation of the integer Fourier basis loses the frame property; odd-numerator rational offsets are stable. It does not classify stability under independently perturbed individual frequencies. The mathematical verification is same-method analytic plus supplemental finite tests, not independent expert certification. Historical priority is best-knowledge rather than exhaustive.

## References

1. C. Cabrelli and D. Carbajal, *Riesz Bases of Exponentials on Unbounded Multi-tiles*, arXiv:1701.07042v1, first public 2017-01-24; *Proc. Amer. Math. Soc.* 146 (2018), 1991–2004. https://arxiv.org/abs/1701.07042
2. C. Frederick and A. Mayeli, *A characterization of Gabor Riesz bases with separable time-frequency shifts*, arXiv:2202.06343v1, first public 2022-02-13. https://arxiv.org/abs/2202.06343
3. O. Asipchuk and V. Drezels, *Examples of exponential bases on unions of intervals*, arXiv:2211.03821v1, first public 2022-11-07. https://arxiv.org/abs/2211.03821
4. C. Frederick and K. Yacoubou Djima, *Examples of Riesz Bases of Exponentials for Multi-tiling Domains and Their Duals*, *La Matematica* 3 (2024), 108–123; published online 2023-11-20. https://doi.org/10.1007/s44007-023-00078-7
