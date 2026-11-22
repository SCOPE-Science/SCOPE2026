# Sharp edge-mode splitting in a three-periodic finite-section counterexample

## Finding
Let \(H\) be the bounded, selfadjoint discrete Schrödinger operator on \(\ell^2(\mathbb Z)\),
\[
(Hu)_j=u_{j-1}+v_j u_j+u_{j+1},\qquad
(v_{3j},v_{3j+1},v_{3j+2})=(2,\tfrac12,\tfrac12).
\]
Let \(H_N\) be its Dirichlet compression to indices \(-N,\ldots,N\). For \(N=3k+1\), \(k\to\infty\), there are exactly two eigenvalues in one fixed open interval about zero, one negative and one positive, and they satisfy
\[
\lambda_-(H_{3k+1})=-\frac3{10}4^{-k}+O(k16^{-k}),\qquad
\lambda_+(H_{3k+1})=\frac3{10}4^{-k}+O(k16^{-k}).
\]
All other eigenvalues stay a uniform positive distance from zero. Consequently, all sufficiently large such finite sections are invertible and
\[
\lim_{k\to\infty}4^{-k}\|H_{3k+1}^{-1}\|=\frac{10}{3}.
\]
Thus the bad boundary phases in this established periodic finite-section counterexample produce a *quantified, exponentially ill-conditioned* inverse, with an exact leading constant.

## Assumptions and scope
The potential and truncation are exactly as displayed, with real Hilbert space or complex Hilbert space \(\ell^2\). Every limit is along integers \(k\to\infty\). The two small eigenvalues are counted with algebraic multiplicity and are individually simple. This assertion does not concern arbitrary three-periodic potentials, or truncation sequences with other boundary phases. The primary classification is MSC2020 47B36 (Jacobi operators).

## Proof
Put \(q=2k+1\), so \(H_{3k+1}\) has size \(3q\). Relabel its indices \(0,\ldots,3q-1\), where the potential reads \(\tfrac12,2,\tfrac12,\tfrac12,2,\tfrac12,\ldots,\tfrac12,2,\tfrac12\). Delete the two endpoint rows/columns, obtaining a symmetric tridiagonal matrix \(K_q\) of order \(M=3q-2\), with diagonal \(2,\tfrac12,\tfrac12,\ldots,2\) and unit off-diagonals. The interior diagonal word is palindromic.

Let \(d_j\) be the determinant of its first \(j\) rows and columns at energy zero, with \(d_0=1\). The continuant recurrence \(d_j=v_jd_{j-1}-d_{j-2}\), using interior phases \(2,\tfrac12,\tfrac12\), gives by induction
\[
d_{3r}=(-2)^r,\qquad d_{3r+1}=2(-2)^r,\qquad d_{3r+2}=0
\]
for every index in range. In particular \(\det K_q=d_M=2(-2)^{q-1}=2^q\), since \(q\) is odd. The inverse continuant formula, for \(1\le i\le j\le M\), is
\[
(K_q^{-1})_{ij}=(-1)^{i+j}\frac{d_{i-1}d_{M-j}}{d_M}.
\]
It uses the reversed suffix minors, equal to prefix minors by palindrome symmetry. The three exact formulas imply \(\lvert (K_q^{-1})_{ij}\rvert\le 2\,2^{-(j-i)/3}\); by symmetry the same estimate holds for \(j<i\). Therefore \(\sup_q\|K_q^{-1}\|\le 2(1+2\sum_{r\ge1}2^{-r/3})<\infty\), by the Schur row/column bound. In particular, there exists an absolute \(\delta>0\) for which every \(K_q-EI\) is invertible for real \(\lvert E\rvert\le2\delta\), with inverses uniformly bounded.

The exact corner Green entries from the continuant formulas are
\[
(K_q^{-1})_{11}=(K_q^{-1})_{MM}=\frac12,\qquad
(K_q^{-1})_{1M}=2^{-q}.
\]
The first Green column has magnitudes \(2^{-r-1}\) at the \(r\)-th first and third sites of the interior triples (with the final first site included). Summing the geometric squares gives
\[
\|K_q^{-1}e_1\|^2=\frac23-\frac53 4^{-q}.
\]
Write the full matrix in endpoint/interior block form. For \(\lvert E\rvert<2\delta\), its eigenvalue equation reduces exactly to the two-by-two Schur matrix
\[
S_q(E)=\begin{pmatrix}h_q(E)&g_q(E)\\g_q(E)&h_q(E)\end{pmatrix},
\]
where
\[
h_q(E)=\frac12-E-\langle e_1,(K_q-EI)^{-1}e_1\rangle,
\qquad g_q(E)=-\langle e_1,(K_q-EI)^{-1}e_M\rangle.
\]
Reflection invariance of the interior gives the equal diagonal entries. The exact Green data imply
\[
h_q(0)=0,\quad g_q(0)=-2^{-q},\quad
h_q'(0)=-1-\|K_q^{-1}e_1\|^2=-\frac53(1-4^{-q}).
\]
Uniform resolvent bounds give \(h_q''(E)=O(1)\) in a smaller fixed interval. The tridiagonal inverse corner formula gives
\[
\langle e_1,(K_q-EI)^{-1}e_M\rangle
=\frac{1}{\det(K_q-EI)},
\]
for odd \(M\). Since \(\lvert\operatorname{tr}(K_q-EI)^{-1}\rvert=O(q)\) there, its logarithmic derivative is \(O(q)\), so
\[
g_q(E)=-2^{-q}+O(q2^{-q}\lvert E\rvert)
\]
uniformly for \(\lvert E\rvert=O(2^{-q})\). Therefore the two scalar Schur equations \(h_q(E)+g_q(E)=0\) and \(h_q(E)-g_q(E)=0\) have solutions
\[
E=\pm\frac35 2^{-q}+O(q4^{-q}).
\]
They exist and are unique inside a fixed small neighborhood of zero: indeed \(S_q'(E)=-I-B^*(K_q-EI)^{-2}B\prec0\), where \(B\) is the two-column endpoint-to-interior coupling. Each symmetry-channel eigenvalue of \(S_q(E)\) is strictly decreasing; the values of \(S_q(0)\) have opposite signs, and uniform negativity of \(S_q'(E)\) forces one crossing of each channel at distance \(O(2^{-q})\). The uniform gap of \(K_q\) excludes any other small eigenvalues by the Schur determinant identity. Since \(q=2k+1\), \(\frac35 2^{-q}=\frac3{10}4^{-k}\) and \(q4^{-q}=O(k16^{-k})\). The smallest absolute eigenvalue controls the inverse norm of the real symmetric finite section, completing the proof.

## Verification
The standalone file `checker.py` verifies the continuant identities, exact corner inverse entries, first-column norm identity and the magnitude of the two nearest eigenvalues in finite sections using high-precision decimal bisection of the symmetric tridiagonal characteristic recurrence. It is supplementary to the infinite-family proof above, not a substitute for it. Run `python checker.py` from a directory containing that file; no third-party modules are required.

## Relationship to prior work
Gabel, Gallaun, Großmann, Lindner and Ukena (arXiv:2110.09339, first made public 18 October 2021), Theorem 1.1 and Example 4.2, establish that the period-three potential \((2,\tfrac12,\tfrac12)\) gives an invertible full-line Schrödinger operator but defeats the symmetric finite-section method because of zero-energy half-line boundary modes. That qualitative instability, the potential, and the boundary phases are prior work. The claim here is the previously unidentified pair of exponentially small finite-section eigenvalues with the precise coefficient \(3/10\), uniform spectral separation of other modes, and the sharp inverse-norm coefficient \(10/3\). Lindner–Ukena (arXiv:2208.04015, 8 August 2022) proves related qualitative finite-section and half-line inversion results for *integer-valued* potentials; its hypotheses exclude this half-integral example. Haeming (arXiv:2208.01646, August 2022) develops bandwidth asymptotics for ergodic periodic approximations, a related but different spectral quantity.

## Limitations
This proof addresses only the exact noninteger three-periodic word and one symmetric residue class of finite sections. The asymptotic is not uniform over perturbations of the potential or boundary conditions. Earlier general transfer-matrix tunneling formulas might entail this special coefficient without naming the word; the historical-priority comparison cannot exclude unindexed specialized literature.

## References
1. F. Gabel, D. Gallaun, J. Großmann, M. Lindner, R. Ukena, *Finite Sections of Periodic Schrödinger Operators*, arXiv:2110.09339v2, https://arxiv.org/abs/2110.09339 (first public 18 October 2021), especially Theorem 1.1, Remark 1.2 and Example 4.2.
2. M. Lindner and R. Ukena, *Half-line compressions and finite sections of discrete Schrödinger operators with integer-valued potentials*, arXiv:2208.04015, https://arxiv.org/abs/2208.04015 (first public 8 August 2022).
3. L. Haeming, *On the Bandwidths of Periodic Approximations to Discrete Schrödinger Operators*, arXiv:2208.01646, https://arxiv.org/abs/2208.01646 (first public August 2022).
