# Near-top matrix-power fibers and concentration in niltriangular algebras

## Finding

Let \(m\ge2\), let \(k=\mathbb F_q\) be an arbitrary finite field, and let \(J=N_{m+2}(k)\) be the associative algebra of strictly upper-triangular matrices. Put
\[
H=\frac{m(m-1)}2,\qquad K=H+m-1=\frac{m^2+m-2}2.
\]
Every \(m\)-th power lies in the three-dimensional ideal \(J^m=\operatorname{span}_k\{E_{1,m+1},E_{2,m+2},E_{1,m+2}\}\). For every target \(Z=A E_{1,m+1}+B E_{2,m+2}+C E_{1,m+2}\) in this ideal, its prescribed-root count \(F_m(Z)=|\{X\in J:X^m=Z\}|\) is exactly
\[
F_m(Z)=q^K\begin{cases}
(q-1)^{m-1},&(A,B)\ne(0,0),\\
(q-1)^{m-1}((m-1)q+1),&A=B=0,\ C\ne0,\\
q^{m+2}-(q-1)^m(q^2+mq+1),&Z=0.
\end{cases}
\]
Targets outside \(J^m\) have no roots. These three displayed positive fiber sizes are strictly increasing, and the power map \(J\to J^m\) is surjective, for every characteristic.

If \(X\) is uniform in \(J\), then, conditioned on \(X^m\ne0\), the probability that \(X^m\) lies in the one-dimensional center \(kE_{1,m+2}\) is
\[
\frac{(m-1)q+1}{mq+q^2+1}=1-\frac{q(q+1)}{mq+q^2+1}.
\]
For each fixed \(q\), the latter tends to one, with failure probability asymptotic to \((q+1)/m\) as \(m\to\infty\). This conditional concentration is a phenomenon across growing niltriangular dimensions, not a claim about the unconditional power law.

For characteristic \(p\) and \(m=p^t\) with \(t\ge1\), the identical three fiber formulas count the \(m\)-th roots of every \(I+Z\in I+J^m\) in the unitriangular group \(UT_{m+2}(k)\), because \((I+X)^{p^t}=I+X^{p^t}\).

## Assumptions and scope

Here \(q\ge2\) is any prime power and \(m\ge2\) is an integer. Matrix units are indexed from 1. A zero coefficient has its literal meaning in \(k\); no parity, characteristic, or lower bound on \(q\) is imposed. The root count is for **all** of \(J\), not only full-index or invertible shifts. In the group interpretation the extra hypothesis \(m=p^t\) is necessary. No group power assertion is made for other exponents.

## Proof

Write \(a_i=X_{i,i+1}\) for \(1\le i\le m+1\) and \(b_j=X_{j,j+2}\) for \(1\le j\le m\). Each path contributing to \(X^m\) has \(m\) strictly increasing steps across at most \(m+1\) positions. Thus all higher superdiagonals of \(X\) are irrelevant. There are exactly \(H\) freely choosable entries beyond the first two superdiagonals, contributing \(q^H\) to each fiber.

For \(P=\prod_{i=2}^m a_i\), the only possibly nonzero coordinates of \(X^m\) are
\[
A=a_1P,\qquad B=a_{m+1}P,\qquad
C=\sum_{j=1}^{m}b_j\prod_{i\in\{1,\ldots,m+1\}\setminus\{j,j+1\}}a_i.
\]
For fixed \(a=(a_1,\ldots,a_{m+1})\), the final coordinate is a linear functional in the \(m\) independent \(b_j\). If at least one coefficient is nonzero, every specified \(C\) has exactly \(q^{m-1}\) choices of \(b\); otherwise \(C=0\) has \(q^m\) choices and nonzero \(C\) has none.

If \(P\ne0\), then the \(m-1\) internal entries \(a_2,\ldots,a_m\) are nonzero. For prescribed \((A,B)\ne(0,0)\), these entries have \((q-1)^{m-1}\) assignments, and \(a_1=A/P\), \(a_{m+1}=B/P\) are forced. At least one coefficient of the \(b\)-functional is nonzero. Multiplication by \(q^{H+m-1}=q^K\) proves the first case. If instead \(P\ne0\) and \(A=B=0\), both endpoints vanish and every coefficient of the \(b\)-functional vanishes.

Suppose \(P=0\), so \(A=B=0\). A coefficient of the \(b\)-functional is nonzero if and only if the set of indices with \(a_i=0\) is contained in one adjacent pair \(\{j,j+1\}\). Under \(P=0\), this happens in exactly two disjoint ways: exactly one internal zero (\(m-1\) possible positions), or exactly two adjacent zeros (\(m\) possible pairs). The number of such \(a\)-assignments is therefore
\[
N_1=(m-1)(q-1)^m+m(q-1)^{m-1}=(q-1)^{m-1}((m-1)q+1).
\]
These are precisely the first-diagonal assignments permitting nonzero \(C\) when \(A=B=0\), proving the second case.

There are \(q^{m+1}\) total assignments to \(a\), and exactly \(q^2(q-1)^{m-1}\) with \(P\ne0\). Of the latter, exactly \((q-1)^{m-1}\) have \(A=B=0\); all have zero \(b\)-functional. Thus the number of \(a\)-assignments with \(A=B=0\) and zero \(b\)-functional is
\[
N_0=q^{m+1}-(q^2-1)(q-1)^{m-1}-N_1.
\]
The zero-target fiber has \(q^H(q^mN_0+q^{m-1}N_1)\) members. Substituting the value of \(N_1\) and simplifying gives the asserted third case.

For strictness of the three positive values, the middle-to-first ratio is \((m-1)q+1>1\). The difference between the zero and middle counts simplifies to
\[
q^{K+2}\left(q^m-(q-1)^{m-1}(q+m-1)\right)>0;
\]
the inequality is strict by the binomial theorem applied to \(q=(q-1)+1\), since \(m\ge2\). All three fibers are positive, hence the image is exactly \(J^m\).

There are \(q^3-q\) targets with \((A,B)\ne(0,0)\), and \(q-1\) nonzero central targets. Dividing their respective weighted counts gives the displayed conditional concentration formula. Its asymptotic follows by division by \(m\). In characteristic \(p\), the binomial theorem and the commutativity of \(I\) with \(X\) give the final group claim when \(m=p^t\).

## Verification

An executable Python checker accompanies this statement as `check_power_fibers.py`, together with its recorded output `checker_output.txt`. It constructs genuine matrix products over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\), compares every prescribed target against the closed formula for small \(m\), and independently enumerates the relevant first-two-diagonal variables at larger \(m\). The program also verifies the support-pattern lemma. The finite tests are checks, not a substitute for the proof above. Example: for \(m=4,q=2\) the generic, nonzero-central, and zero fiber sizes are respectively \(512\), \(3584\), and \(26112\), totaling \(2^{15}\) roots over all eight targets.

## Relationship to prior work

Bier (2012) determines power verbal subgroups and sharp width thresholds for unitriangular groups; at dimension \(m+2\) and exponent \(m=p^t\), surjectivity of the power map is consistent with her theorem. Sosnovsky (first posted January 31, 2012) treats verbal width in triangular matrix groups. Dolfi–Singh–Yadav (first posted 2019) studies the size and conjugacy classes of power images and explicitly recalls the \(n=p+2\) surjectivity boundary. These results do not state prescribed-root multiplicities or the conditional concentration law proved here. Ekhad–Zeilberger (1995) counts solutions to \(X^2=0\) for triangular matrices in arbitrary dimensions; that is a zero-target enumeration, rather than the three-stratum nonzero-target law here.

The \(m=3\) specialization recovers an existing finite-field cubic-power fiber calculation for \(N_5(k)\). This is explicitly a strict infinite-parameter extension: the new content is simultaneous exactness for every exponent and size \(m+2\), including the conditional \(m\to\infty\) central-concentration law. No claim is made that the \(m=3\) case itself is new.

## Limitations

This theorem concerns the near-top exponent \(m=n-2\), not arbitrary power maps in arbitrary matrix dimension. It does not establish statistical independence or general formulas for \(n\ge m+3\). Its novelty assessment relies on searched mathematical literature and an index of published research records, not on exhaustive coverage of all historical mathematics. The existence of an equivalent older prescribed-fiber count cannot be conclusively excluded.

## References

- A. Bier, *The Width of Verbal Subgroups in the Group of Unitriangular Matrices Over a Field*, International Journal of Algebra and Computation 22 (2012), 1250019, https://doi.org/10.1142/S0218196712500191 . Accessible full-text transcription: https://www.academia.edu/88269862/The_Width_of_Verbal_Subgroups_in_the_Group_of_Unitriangular_Matrices_Over_a_Field .
- Yu. V. Sosnovsky, *On the Width of Verbal Subgroups of the Groups of Triangular Matrices over a Field of Arbitrary Characteristic*, arXiv:1201.6513, first posted January 31, 2012, https://arxiv.org/abs/1201.6513 .
- S. Dolfi, A. Singh, M. K. Yadav, *p-Power conjugacy classes in U(n,q) and T(n,q)*, arXiv:1905.04244, first posted May 10, 2019, https://arxiv.org/abs/1905.04244 .
- S. B. Ekhad and D. Zeilberger, *An Explicit Formula for the Number of Solutions of X^2=0 in Triangular Matrices over a Finite Field*, arXiv:math/9512224, first posted December 19, 1995, https://arxiv.org/abs/math/9512224 .
