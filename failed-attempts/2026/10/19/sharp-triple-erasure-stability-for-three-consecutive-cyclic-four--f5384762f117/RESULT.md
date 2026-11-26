# Sharp triple-erasure stability for three consecutive cyclic Fourier characters

## Finding
For every integer \(N\ge6\), put \(\omega=\exp(2\pi i/N)\) and consider the Parseval frame of \(N\) vectors in \(\mathbb C^3\)
\[
\varphi_j=N^{-1/2}(1,\omega^j,\omega^{2j})^{\mathsf T},\quad j\in\mathbb Z_N.
\]
Delete **exactly three distinct labelled measurements** \(E\subset\mathbb Z_N\), \(|E|=3\). Write \(A(E)\) for the optimal squared lower frame bound of the retained family \(\{\varphi_j:j\notin E\}\), equivalently the smallest eigenvalue of its frame operator. Set
\[
 a_N=1+2\cos(2\pi/N),\qquad b_N=1+2\cos(4\pi/N),
 \qquad L_N=3+\frac{b_N+\sqrt{b_N^2+8a_N^2}}2.
\]
The exact worst-retained-frame bound is
\[
\boxed{\min_{|E|=3}A(E)=1-\frac{L_N}{N}>0.}
\]
**Exactly \(N\) erasure masks attain equality:** the cyclic translates \(E=\{j,j+1,j+2\}\). Every nonconsecutive three-set yields a strictly larger retained lower bound. Moreover,
\[
 L_N=9-\frac{16\pi^2}{N^2}+O(N^{-4}),\qquad
 \min_{|E|=3}A(E)=1-\frac9N+\frac{16\pi^2}{N^3}+O(N^{-5})
\]
as \(N\to\infty\) through integers. The boundary \(N=5\) is excluded: every three-erasure pattern then leaves fewer than three measurements, hence lower frame bound zero.

## Assumptions and scope
All frequency indices are \(0,1,2\), all time/measurement indices are elements of \(\mathbb Z_N\), and all frame vectors use exactly the normalization \(N^{-1/2}\). A cyclicly consecutive triple means \(\{j,j+1,j+2\}\) modulo \(N\). Erasure masks are unordered three-element subsets of *distinct* measurement labels. We optimize the squared lower analysis-frame bound after deletion, **not** the upper retained frame bound, arbitrary reconstruction-dual errors, or the condition number. The statement is restricted to this three-frequency harmonic Parseval frame and exactly three erasures; it is not a universal Gabor-frame assertion.

## Proof
**1. Fourier Gram reduction.** Fourier-character orthogonality for \(N\ge3\) gives \(\sum_j\varphi_j\varphi_j^*=I_3\). For a deleted triple \(E\), the retained frame operator is \(S_E=I_3-\sum_{j\in E}\varphi_j\varphi_j^*\). The nonzero eigenvalues of its rank-at-most-three subtraction are those of the deleted-column Gram matrix, divided by \(N\). Rephase each unnormalized deleted vector \(v_j=(1,\omega^j,\omega^{2j})^{\mathsf T}\) by \(\omega^{-j}\). This yields the real symmetric Gram matrix \(C_E\), with diagonal entries \(3\) and off-diagonal entries
\[
 k_N(j-k)=1+2\cos(2\pi(j-k)/N).
\]
Therefore \(A(E)=1-\lambda_{\max}(C_E)/N\). The surviving vectors have positive lower bound when \(N\ge6\): at least three of the remaining \(N-3\) sample sites are distinct, and their three-column Vandermonde matrix in the character indices \(0,1,2\) is nonsingular.

**2. Consecutive-triple eigenvalues.** For \(E=\{j,j+1,j+2\}\), the real Gram matrix is, after relabeling,
\[
 C_0=\begin{pmatrix}3&a_N&b_N\\a_N&3&a_N\\b_N&a_N&3\end{pmatrix}.
\]
The vector \((1,0,-1)^{\mathsf T}\) has eigenvalue \(3-b_N\). The other two eigenvalues are \(3+(b_N\pm\sqrt{b_N^2+8a_N^2})/2\). For \(N\ge6\), \(a_N>0\), \(b_N\ge0\); thus the top eigenvalue is exactly \(L_N\).

**3. Strict universal bound for \(N\ge8\).** Here \(\theta=2\pi/N\le\pi/4\), and \(a_N>b_N\ge1\). Among the cyclic distances \(d\in\{2,\ldots,\lfloor N/2\rfloor\}\), the function \(1+2\cos(d\theta)\) decreases from at most \(b_N\) to at least \(-1\). Consequently every nonadjacent pair has \(|k_N(d)|\le b_N\), whereas every adjacent pair has \(|k_N(1)|=a_N\). In every three-point subset some pair is nonadjacent; relabel it as the \((1,3)\) pair. Then the entrywise nonnegative matrix \(|C_E|\) is bounded by \(C_0\). The variational and Perron inequalities yield
\[
 \lambda_{\max}(C_E)\le\rho(|C_E|)\le\rho(C_0)=L_N.
\]
The positive matrix \(C_0\) is irreducible. If \(E\) is not a consecutive triple, it has at most one adjacent pair whereas \(C_0\) has two. At least one of the displayed entrywise inequalities is then strict, so Perron monotonicity gives \(\lambda_{\max}(C_E)<L_N\). Consecutive triples achieve equality.

**4. The exceptional order \(N=7\).** Write \(a=k_7(1)\), \(b=k_7(2)\), \(c=k_7(3)\), and \(d=-c\). Then \(a>2\), \(0<b<1\), \(c<0\), and the seventh-root identity \(a+b+c=2\) gives \(d=a+b-2>b\) and \(0<d<a\). A nonconsecutive triple has at most one adjacent pair, so Gershgorin's bound is \(\lambda_{\max}(C_E)\le3+a+d\). For the consecutive triple, the all-ones Rayleigh quotient gives
\[
 L_7\ge3+(4a+2b)/3>3+a+d,
\]
because \(\bigl((4a+2b)/3\bigr)-(a+d)=(6-2a-b)/3>0\). Indeed \(a<1+\sqrt2<5/2\) since \(2\pi/7>\pi/4\), and \(b<1\) since \(4\pi/7>\pi/2\), yielding \(2a+b<6\). Thus only consecutive triples maximize.

**5. The exceptional order \(N=6\).** Up to rotations and reversals, the cyclic gap types of three-point subsets are \((1,1,4)\), \((1,2,3)\), and \((2,2,2)\). Since \(k_6(1)=2\), \(k_6(2)=0\), and \(k_6(3)=-1\), their Gram top eigenvalues are respectively \(3+2\sqrt2\), \(3+\sqrt5\), and \(3\). The unique largest type is the consecutive triple, with six distinct rotations.

**6. Asymptotics.** Expanding the elementary trigonometric formula gives \(a_N=3-4\pi^2/N^2+O(N^{-4})\) and \(b_N=3-16\pi^2/N^2+O(N^{-4})\). Inserting them in the explicit positive-root formula gives \(L_N=9-16\pi^2/N^2+O(N^{-4})\). Division by \(N\) finishes the claimed expansion. This completes the proof of the global minimum and all equality cases for every \(N\ge6\).

## Verification
The accompanying standard-library Python file `checker.py` independently reconstructs every deleted Gram matrix from \(k_N\), obtains its largest eigenvalue by a stable closed cubic-root formula, compares all \(\binom N3\) erasure masks for each \(6\le N\le36\), verifies the sharp constant and counts exactly \(N\) attaining masks, and separately checks the two small-order gap classifications. Running `python3 checker.py` prints a `VERIFY_OK` summary on success. The complete infinite-family conclusion follows from the preceding analytic proof, not from finite enumeration.

## Relationship to prior work
Salanevich and Strachan (arXiv:2509.01325v1, first public 2025-09-01) study adversarial coefficient erasures and stability for finite structured frames, especially Gabor frames and mutually unbiased bases. Their estimates do not provide the exact three-erasure spectral constant or equality classification for the three-character harmonic frame here.

The published *Exact adversarial-erasure spectra for two-character cyclic harmonic frames* treats **two** character rows (arbitrary erasure count); it explicitly excludes three or more rows. The published *Sharp Riesz conditioning for consecutive triples on finite cycles* optimizes the **smallest** condition number over three selected Fourier columns, preferring near-equilateral placements; our result maximizes a **different** eigenvalue over three deleted columns, with a consecutive worst placement. The published *Exact three-frequency Fourier projection norm on every cyclic group* evaluates an endpoint \(\ell^1/\ell^\infty\) operator norm, rather than a finite \(\ell^2\) Gram spectral extremum. Full public scientific statements of all three were inspected to compare mathematical implications, not merely title similarity.

## Limitations
The closed form is restricted to three consecutive Fourier frequencies and erasure cardinality three. The proof does not derive worst deletion patterns for larger frequency bands, longer erasure masks, or arbitrary Fourier row sets, nor does it assert near-optimal *condition numbers*. The elementary extremal inequality could have an unindexed equivalent in discrete spectral-concentration or rearrangement literature; bibliographic priority remains subject to independent specialist assessment. Computational tests are finite and do not constitute the proof.

## References
1. P. Salanevich and N. Q. D. Strachan, *Robustness to noise and erasures of Gabor frames in finite dimensions*, arXiv:2509.01325v1 (first public 2025-09-01), specifically introduction, Sections 1 and 5.
2. *Exact adversarial-erasure spectra for two-character cyclic harmonic frames*, published mathematical finding, `2026/10/11/SCOPE-exact-adversarial-erasure-spectra-for-two-character-cyclic-harmo--e1e03f96b6f0`, `RESULT.md`.
3. *Sharp Riesz conditioning for consecutive triples on finite cycles*, published mathematical finding, `2026/10/11/SCOPE-sharp-riesz-conditioning-for-consecutive-triples-on-finite-cycle--1200745c9cae`, `RESULT.md`.
4. *Exact three-frequency Fourier projection norm on every cyclic group*, published mathematical finding, `2026/10/4/SCOPE-exact-three-frequency-fourier-projection-norm-on-every-cyclic-gr--b176a6018242`, `RESULT.md`.
5. J. J. Benedetto and M. Fickus, *Finite normalized tight frames*, Advances in Computational Mathematics 18 (2003), 357–385 (general finite-frame context; not an exact fixed-cardinality erasure theorem).
