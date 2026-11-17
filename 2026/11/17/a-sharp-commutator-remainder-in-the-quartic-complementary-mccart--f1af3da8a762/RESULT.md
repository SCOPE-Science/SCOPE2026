# A sharp commutator remainder in the quartic complementary McCarthy inequality

## Finding
Let \(\mathcal H\) be an arbitrary complex Hilbert space and let \(A,B\geq0\) belong to the Schatten class \(\mathcal S_4(\mathcal H)\). Write \(\|\cdot\|_2\) for Hilbert–Schmidt norm and set
\[
\mathcal D_4(A,B)=\operatorname{Tr}(A+B)^4-\operatorname{Tr}A^4-\operatorname{Tr}B^4
-14\operatorname{Tr}\bigl[(A^{1/2}BA^{1/2})^2\bigr].
\]
The following is an **exact, dimension-independent identity**:
\[
\boxed{\mathcal D_4(A,B)=4\|A^{1/2}(A-B)B^{1/2}\|_2^2+6\|AB-BA\|_2^2.}
\]
Consequently the strengthened complementary McCarthy bound
\[
\mathcal D_4(A,B)\geq 6\|AB-BA\|_2^2
\]
has the **largest possible universal coefficient** \(6\), even if one restricts to finite-dimensional positive definite operators. The lower bound is an equality precisely when \(A^{1/2}(A-B)B^{1/2}=0\); there are noncommuting equality pairs.

The original complementary inequality \(\mathcal D_4(A,B)\geq0\) is an equality exactly when \(A\) and \(B\) commute and \(AB(A-B)=0\). Equivalently, their simultaneous eigenvalue pairs \((a,b)\) satisfy \(ab(a-b)=0\): each joint eigenspace has either equal positive values or at least one zero eigenvalue.

## Assumptions and scope
All products, powers and traces refer to operators on the **same** Hilbert space. The hypotheses are only positivity and Schatten-four membership; no invertibility, finite dimension, equal trace, commutation, or rank bound is assumed. Schatten Hölder guarantees \(AB-BA\in\mathcal S_2\) and \(A^{1/2}(A-B)B^{1/2}\in\mathcal S_2\), so every displayed quantity is finite. In particular \(A^{1/2}\in\mathcal S_8\), \(A-B\in\mathcal S_4\), and \(B^{1/2}\in\mathcal S_8\).

## Proof
For finite positive matrices, cyclicity of trace gives
\[
\operatorname{Tr}\bigl[(A^{1/2}BA^{1/2})^2\bigr]=\operatorname{Tr}(ABAB).
\]
Expanding the fourth power and grouping cyclic words yields
\[
\mathcal D_4(A,B)=4\operatorname{Tr}(A^3B+AB^3+A^2B^2-3ABAB).
\]
On the other hand, expanding the Hilbert–Schmidt norms gives the two exact relations
\[
\begin{aligned}
\|A^{1/2}(A-B)B^{1/2}\|_2^2
 &=\operatorname{Tr}(A^3B+AB^3-2A^2B^2),\\
\|AB-BA\|_2^2
 &=2\operatorname{Tr}(A^2B^2-ABAB).
\end{aligned}
\]
Multiplying these equalities by \(4\) and \(6\), respectively, and adding proves the boxed identity. Each summand is nonnegative.

For general positive \(A,B\in\mathcal S_4(\mathcal H)\), choose common finite-rank orthogonal compressions converging to both operators in \(\mathcal S_4\). These compressions are positive. Schatten Hölder makes every fourth-order mixed trace continuous under \(\mathcal S_4\)-convergence, so the finite-matrix polynomial identity passes to the limit. For the two norm terms, their squares agree with the polynomial trace expressions above and hence have the same limit; alternatively, fractional-power continuity and Hölder give convergence in \(\mathcal S_2\). This proves the identity on arbitrary \(\mathcal H\).

The coefficient \(6\) is sharp. On \(\mathbb C^2\), take the noncommuting rank-one projections
\[
P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
Q=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]
Since \(P(P-Q)Q=0\), the first squared norm vanishes, whereas \(\|PQ-QP\|_2^2=1/2\) and \(\mathcal D_4(P,Q)=3\). Thus any coefficient larger than \(6\) fails. Approximating \(P,Q\) by \(P+\varepsilon I,Q+\varepsilon I\) in dimension two shows sharpness among positive definite pairs as \(\varepsilon\downarrow0\).

The equality condition for the strengthened bound follows directly from the exact identity. For the unstrengthened bound, zero defect forces \([A,B]=0\), after which simultaneous diagonalization of the commuting positive compact operators reduces the remaining square to the sum of \(ab(a-b)^2\) over joint eigenvectors. It vanishes exactly when \(ab(a-b)=0\) on every joint eigenspace, equivalently \(AB(A-B)=0\).

## Verification
The supplied `verify_quartic.py` uses exact rational matrix arithmetic to check the trace-word identity and both nonnegative terms on 562 small Gram-matrix pairs, plus the two-dimensional noncommuting sharpness and a nonidentical commuting zero-defect witness. The observed result is `QUARTIC_MCCARTHY_REMAINDER_OK 564 rational_matrix_pairs`. An additional 200 independently generated complex positive-semidefinite matrix pairs were evaluated with numerical square roots and checked to relative tolerance. The infinite-dimensional statement follows from Schatten Hölder and the proof, **not** finite tests.

## Relationship to prior work
Teng Zhang, arXiv:2611.00459v1, Theorem 1.2, proves \(\mathcal D_p(A,B)\geq0\) for \(p\geq2\) (with its corresponding \(p\)-dependent coefficient) and provides a general proof through tracial joint spectral measures. At \(p=4\), its lower bound is exactly \(\mathcal D_4\geq0\). The present statement supplies the additional **sharp commutator remainder**, an explicit positive-square decomposition, noncommuting sharpness witnesses, and a zero-defect classification; those are not asserted by that theorem.

Audenaert's 2005 norm-compression work treats the underlying positive block-matrix inequalities for general exponents, providing older foundational coverage of the unstrengthened bound. The decomposition here does not claim the underlying McCarthy/Audenaert inequality as new. Li and Zhou, arXiv:2608.20937v1, concern the complementary inequality across exponent ranges and negative-exponent equality; this is a distinct quantitative fourth-order stability question. Published research-record results on other quartic Schatten identities or crossed-Heinz commutator estimates have different operators and deficits.

## Limitations
The theorem is specific to the fourth power; no assertion is made of analogous optimal coefficients for arbitrary real exponents. The improvement is an additive Schatten-two commutator term and does not imply an operator-order inequality. The sharp coefficient is attained by noncommuting semidefinite rank-one pairs; for strictly positive pairs it is sharp as a supremum, not asserted to be attained. Existing literature could contain the same elementary quartic identity under an unindexed equivalent expression; publication priority requires further independent human comparison.

## References
1. T. Zhang, *Clarkson–McCarthy type inequalities, part II: refinements, unitary orbits, unitarily invariant norms and ell_s–ell_s estimates*, arXiv:2611.00459v1 (first public 2026-10-30), Theorem 1.2 and Section 3.2. https://arxiv.org/html/2611.00459v1
2. K. M. R. Audenaert, *A Norm Compression Inequality for Block Partitioned Positive Semidefinite Matrices*, arXiv:math/0505680v1 (2005). https://arxiv.org/pdf/math/0505680
3. X. Li and B. Zhou, *A negative exponent range for Audenaert's complementary McCarthy trace inequality*, arXiv:2608.20937v1 (2026). https://arxiv.org/abs/2608.20937
