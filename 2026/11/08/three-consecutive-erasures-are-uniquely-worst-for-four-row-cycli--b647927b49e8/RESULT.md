# Three consecutive erasures are uniquely worst for four-row cyclic harmonic frames

## Finding
For every integer \(N\ge 7\), let \(\omega=\exp(2\pi i/N)\) and consider the Parseval frame in \(\mathbb C^4\)
\[
\varphi_j=N^{-1/2}(1,\omega^j,\omega^{2j},\omega^{3j})^{\mathsf T},\qquad j\in\mathbb Z/N\mathbb Z.
\]
If \(E\subset\mathbb Z/N\mathbb Z\) has exactly three elements, define the retained frame operator \(S_E=\sum_{j\notin E}\varphi_j\varphi_j^*\). Put
\[
r_d=\frac{\sin(4\pi d/N)}{\sin(\pi d/N)},\quad a_N=r_1,\quad b_N=r_2,\quad
\beta_N=\frac{b_N+\sqrt{b_N^2+8a_N^2}}2.
\]
Then the sharp universal lower retained-frame bound is
\[
\boxed{\ \lambda_{\min}(S_E)\ge 1-\frac{4+\beta_N}{N}>0\ }.
\]
Equality holds **if and only if** \(E=\{k,k+1,k+2\}\pmod N\) for some \(k\). Hence precisely \(N\) distinct erasure masks are worst, including the exceptional orders \(N=7,8,9\). Here \(\lambda_{\min}\) is the smallest eigenvalue of the Hermitian operator; no asymptotic approximation is involved.

## Assumptions and scope
Only the four consecutive Fourier characters indexed \(0,1,2,3\), an arbitrary cyclic order \(N\ge7\), unit frame normalization \(N^{-1/2}\), and exactly three erased column coefficients are considered. Distinct erasure positions are required. Complex Hilbert-space inner products use the usual conjugate transpose. For evaluating \(r_d\) on signed column differences, the actual integer difference in \(\{1,\dots,N-1\}\), rather than its shortest cyclic representative, is used; the signs matter in the Gram matrix. Circular distance is used only for absolute-value comparisons.

## Proof
**1. Fourier reduction.** Character orthogonality gives \(\sum_{j=0}^{N-1}\varphi_j\varphi_j^*=I_4\). Writing \(\Phi_E\) for the four-by-three matrix of erased columns, \(S_E=I_4-\Phi_E\Phi_E^*\), and the three nonzero eigenvalues of \(\Phi_E\Phi_E^*\) equal those of \(\Phi_E^*\Phi_E\). If the erased positions are \(e_1<e_2<e_3\), a diagonal unitary phase change reduces \(N\Phi_E^*\Phi_E\) to \(4I_3+B_E\), where \(B_E\) is real symmetric, diagonal zero, and the off-diagonal entries for positions \(e_i<e_j\) are \(r_{e_j-e_i}\). Indeed
\[
\sum_{m=0}^3\omega^{md}=e^{3\pi i d/N}\frac{\sin(4\pi d/N)}{\sin(\pi d/N)}.
\]
Consequently \(\lambda_{\min}(S_E)=1-(4+\lambda_{\max}(B_E))/N\).

**2. The consecutive candidate.** For \(E=\{0,1,2\}\), the symmetric off-diagonal matrix is
\[
B_*=\begin{pmatrix}0&a_N&b_N\\a_N&0&a_N\\b_N&a_N&0\end{pmatrix}.
\]
Its eigenvalues are \(-b_N\) and the two roots of \(x^2-b_Nx-2a_N^2=0\). For every \(N\ge7\), \(a_N>0\) and the larger root \(\beta_N\) exceeds \(-b_N\), so \(\lambda_{\max}(B_*)=\beta_N\). Cyclic translation conjugates the Gram matrix unitarily, so every consecutive triple has the same value.

**3. Circular sidelobe domination for \(N\ge10\).** Since
\[
r_d=4\cos(\pi d/N)\cos(2\pi d/N),
\]
\(r_1>r_2>0\). Furthermore, for each circular distance \(2\le d\le\lfloor N/2\rfloor\), \(|r_d|\le r_2\). At \(N=10\) this follows directly by checking distances \(2,3,4,5\): \(r_2=1\), \(|r_3|<1\), \(|r_4|=1\), \(r_5=0\). For \(N\ge11\), set \(t=\pi d/N\). On \(2\pi/N\le t\le\pi/4\), the positive product \(4\cos t\cos2t\) decreases, so its value is at most \(r_2\). On \(\pi/4\le t\le\pi/2\), calculus gives \(|4\cos t\cos2t|\le8/(3\sqrt6)<6/5\). Finally \(r_2\ge r_2(11)>6/5\), because \(2\pi/11<3\pi/16\), \(4\pi/11<3\pi/8\), \(\cos(3\pi/16)>4/5\), and \(\cos(3\pi/8)>3/8\).

A nonconsecutive three-element cyclic set contains at most one adjacent pair. Thus its absolute Gram off-diagonals, after a simultaneous permutation, are bounded by \((r_1,r_2,r_2)\), while the candidate's are \((r_1,r_1,r_2)\). For Hermitian \(B_E\), the Rayleigh principle gives \(\lambda_{\max}(B_E)\le\lambda_{\max}(|B_E|)\), where absolute value is entrywise. Entrywise Perron--Frobenius strict comparison of the two nonnegative irreducible symmetric matrices yields
\[
\lambda_{\max}(B_E)\le \lambda_{\max}(|B_E|)
\le \rho\!\begin{pmatrix}0&r_1&r_2\\r_1&0&r_2\\r_2&r_2&0\end{pmatrix}
<\rho(B_*)=\beta_N.
\]
Hence no nonconsecutive mask attains equality for \(N\ge10\).

**4. The exact small-order certificate for \(N=7,8,9\).** Write the three signed off-diagonal entries of \(B_E\) as \(x,y,z\), with \(s=x^2+y^2+z^2\). If its eigenvalues are \(\mu_1\ge\mu_2\ge\mu_3\), zero trace and \(\operatorname{tr}(B_E^2)=2s\) give \(\mu_1^2\le4s/3\). Every triple has a cyclic translate containing \(0\); inspect the finite pairs \(E=\{0,a,b\}\), \(1\le a<b<N\), excluding the consecutive triples. The included `check_four_row.py` uses **exact rational arithmetic**, Machin's arctangent identity with alternating-series rational bounds for \(\pi\), and cosine Taylor polynomials with certified remainder bounds. The following strict certificates hold for all those pairs:
\[
\begin{array}{c|c|c}
N&\text{every nonconsecutive }s\le&\beta_N>\\\hline
7&6.34&2.91\\
8&8.01&3.69\\
9&10&4.34
\end{array}
\]
In each row \(4s/3\) is strictly smaller than the square of the listed lower bound for \(\beta_N\). Hence \(\lambda_{\max}(B_E)<\beta_N\). The inequalities are exact rational certificates; floating-point enumeration is not the justification.

**5. Strict positive retained bound and equality count.** Since \(N\ge7\), at least four columns remain. Every four distinct columns form a nonsingular four-by-four Vandermonde matrix (their points \(\omega^j\) are distinct). Therefore \(S_E\) is positive definite for any three erasures, including a worst mask. There are exactly \(N\) distinct cyclic translates of a three-consecutive mask when \(N\ge7\). This proves every assertion.

## Verification
The standalone Python 3 program `check_four_row.py` uses only the standard library. Running `python3 check_four_row.py` supplies certified rational bounds at \(N=7,8,9\), as detailed above, and separately recomputes every three-position mask for each integer \(7\le N\le39\), totaling \(91{,}355\) direct numerical corroboration cases. It reports `FOUR_ROW_THREE_ERASURE_PASS` when all tests pass. The infinite-order proof is analytical; those finite numerical tests are not an infinite certificate.

## Relationship to prior work
Marshall and Waldron's harmonic-frame construction supplies the canonical consecutive Fourier-row setting; their principal theorems count frame equivalence classes, not adversarial three-erasure spectral extrema. Results on two-row harmonic-frame erasures concern a different eigenvalue kernel and do not imply the four-row constant. Batenkov, Diederichs, Goldman and Yomdin study singular values of Fourier--Vandermonde matrices with clustered nodes, but their general cluster estimates do not supply the sharp all-\(N\) worst-mask classification here. Uniform subframe-bound theorems address a different uniformity question. Numeric algorithms for the SVD of Fourier submatrices provide computational machinery, not a stated theorem optimizing over all three-column configurations; however, incomplete access to that source is a bibliographic limitation.

## Limitations
The result is specific to four consecutive Fourier rows and **exactly three** erasures. It does not assert optimality for other row sets, larger masks, arbitrary frame constructions, or every eigenvalue of the erased Gram matrix. The inequality and uniqueness claim are mathematical proofs, not independent external certification. Earlier equivalent results under different terminology remain a potential priority risk, particularly where full source text was unavailable.

## References
- S. Marshall and S. Waldron, *On the number of harmonic frames*, arXiv:1611.07121 (first public version 2016-11-22), DOI:10.1016/j.acha.2018.02.004.
- D. Batenkov, B. Diederichs, G. Goldman and Y. Yomdin, *The spectral properties of Vandermonde matrices with clustered nodes*, arXiv:1909.01927 (2019), DOI:10.1016/j.laa.2020.08.034.
- T. Cheng, X. Lv and Q. Sun, *Frames of uniform subframe bounds with applications to erasures*, Linear Algebra and its Applications (2018), DOI:10.1016/j.laa.2018.05.025.
- D. Dirckx, D. Huybrechs and R. Ongenae, *On the Computation of the SVD of Fourier Submatrices*, arXiv:2208.12583 (2022), DOI:10.1007/s10915-023-02171-z; full text not accessible in this comparison.
