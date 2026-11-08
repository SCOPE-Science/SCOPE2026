# Exact dyadic projector convolution support and a sharp positive fiber bound

## Finding

Let \(k\ge2\), \(R_k=\mathbb Z/2^k\mathbb Z\), and let \(\mathcal P_k\) be all rank-one idempotents in \(M_2(R_k)\). The ordered additive convolution
\[
 r_k(S)=(\mathbf1_{\mathcal P_k}*\mathbf1_{\mathcal P_k})(S)
 =\#\{(P,Q)\in\mathcal P_k^2:P+Q=S\}
\]
has a precise arithmetic support obstruction. It vanishes unless \(\operatorname{tr}S=2\); for matrices of trace \(2\), write \(S=I_2+A\) with \(\operatorname{tr}A=0\). If \(A\ne0\), put \(j=\min\{v_2(A_{11}),v_2(A_{12}),v_2(A_{21}),v_2(A_{22})\}\in\{0,\ldots,k-1\}\), with valuations truncated at \(k\). For \(j\ge1\), let \(B=A/2^j\) modulo \(2^{k-j}\). Then
\[
 \boxed{\;r_k(S)=0\iff
 1\le j<k\ \text{and}\ B\equiv I_2\pmod2\;}
\]
within the trace-two hyperplane. The target \(S=I_2\), for which \(A=0\), is always represented.

The trace-two hyperplane has \(8^k\) matrices. Exactly
\[
 Z_k=\sum_{j=1}^{k-1}8^{k-j-1}=\frac{8^{k-1}-1}{7}
\]
of them are not two-projector sums. Consequently
\[
 \boxed{|\mathcal P_k+\mathcal P_k|=\frac{55\cdot8^{k-1}+1}{7},\qquad
 \lim_{k\to\infty}\frac{|\mathcal P_k+\mathcal P_k|}{8^k}=\frac{55}{56}.}
\]
Every represented trace-two target has at least \(2^{k+1}\) ordered representations, and this is sharp:
\[
 \boxed{\min_{r_k(S)>0}r_k(S)=2^{k+1}.}
\]
The exact positive fibers on the non-scalar Fourier-compatible strata are given in the proof; no assertion of a complete numerical convolution histogram is made.

## Assumptions and scope

An idempotent of rank one means a matrix \(P\) satisfying \(P^2=P\), \(\operatorname{tr}P=1\), \(\det P=0\). For \(2\times2\) matrices over \(R_k\), trace one and determinant zero already imply idempotency by Cayley–Hamilton. These matrices are precisely the local free-rank-one projectors, and every idempotent whose reduction modulo two has rank one belongs to this set. Let \(\mathbb F_2=R_k/(2)\). All congruences involving \(A/2^j\) mean its uniquely determined reduction modulo \(2^{k-j}\), not a division by a unit.

For \(S\) of trace \(2\), \(A=S-I_2\) is traceless. If \(A\) is not divisible by two, its reduction \(\bar A\) is either the scalar matrix \(I_2\) or a non-scalar traceless matrix. If \(A\) is nonzero and divisible by two, the primitive reduction \(\bar B\) defined above is nonzero and traceless, and its only scalar possibility is \(I_2\).

## Proof

**Step 1: a trace pairing reduces the two-projector problem.** The rank-one projectors have the smooth affine parametrization
\[
 P=\begin{pmatrix}a&b\\c&1-a\end{pmatrix},\qquad a(1-a)=bc.
\]
Modulo two there are six such projectors. The derivative of the defining equation with respect to \(a\) is \(1-2a\), a unit at every point; hence each solution at depth \(m\) lifts to exactly four solutions at depth \(m+1\). Thus \(|\mathcal P_k|=6\cdot4^{k-1}=3\cdot2^{2k-1}\).

For \(S=I_2+A\), with \(\operatorname{tr}A=0\), a rank-one projector \(P\) yields a rank-one projector \(Q=S-P\) if and only if \(\det Q=0\), because \(\operatorname{tr}Q=1\). The two-by-two determinant polarization identity and \(\operatorname{adj}(A)=-A\) give
\[
 \det(I_2+A-P)=\det A+\operatorname{tr}(AP).
\]
Therefore
\[
 r_k(I_2+A)=\#\{P\in\mathcal P_k:\operatorname{tr}(AP)=-\det A\}. \tag{1}
\]

**Step 2: exact mod-two trace-pairing lemma.** Let \(C\) be a non-scalar matrix over \(\mathbb F_2\) and \(f_C(P)=\operatorname{tr}(CP)\) on the six rank-one projectors. A solution \(P\) is called regular when \(f_C\) has a nonzero differential on the two-dimensional projector variety there. Conjugating \(P\) to \(\operatorname{diag}(1,0)\) shows that this differential is nonzero precisely when \(C\) does not commute with \(P\).

When \(\operatorname{tr}C=0\), the matrix is a non-scalar Jordan block, so no rank-one projector commutes with it. If \(\det C=0\), there are four projectors with \(f_C(P)=0\), and if \(\det C=1\), there are two. The complementary fibers each have the remaining two and four projectors, respectively. In particular, for \(\operatorname{tr}C=0\), the fiber \(f_C(P)=-\det C\) consists of four regular solutions.

When \(\operatorname{tr}C=1\), there are three projectors in the fiber \(f_C(P)=0\). At least two of them are regular. Indeed, if \(\det C=0\), \(C\) is similar to \(\operatorname{diag}(0,1)\) and exactly one of those three solutions commutes with \(C\); if \(\det C=1\), its quadratic characteristic polynomial is irreducible and all three are regular. Every regular solution lifts through each dyadic digit with exactly two choices, by one nonzero linear condition on the two tangent directions.

**Step 3: primitive targets.** If \(A\not\equiv0\pmod2\) and \(\bar A\ne I_2\), (1) has exactly four regular solutions modulo two. Each lifts to \(2^{k-1}\) solutions, so
\[
 r_k(I_2+A)=2^{k+1}. \tag{2}
\]
If \(\bar A=I_2\), write \(A=I_2+2C\), where \(C\) is defined modulo \(2^{k-1}\). Since \(\operatorname{tr}A=0\), the trace of \(C\) is \(-1\) modulo \(2^{k-1}\). The determinant identity yields
\[
 \operatorname{tr}(AP)+\det A=2\bigl(\operatorname{tr}(CP)+2\det C\bigr),
\]
so equation (1) reduces to \(\operatorname{tr}(CP)=-2\det C\pmod{2^{k-1}}\). Because \(\bar C\) has trace one, the lemma gives at least two regular mod-two projectors satisfying this equation; each has \(2^{k-2}\) lifts at modulus \(2^{k-1}\), and each of these lifts to four projectors over \(R_k\). Therefore
\[
 r_k(I_2+A)\ge2^{k+1}. \tag{3}
\]
This lower bound remains valid for \(k=2\).

**Step 4: divisible targets.** If \(A=0\), every \(P\in\mathcal P_k\) produces \(Q=I_2-P\), so \(r_k(I_2)=3\cdot2^{2k-1}\). Otherwise write \(A=2^jB\) with \(1\le j<k\) and \(B\) primitive modulo \(2^{k-j}\). The identity \(\det A=2^{2j}\det B\) makes (1) equivalent to
\[
 \operatorname{tr}(BP)=-2^j\det B\pmod{2^{k-j}}. \tag{4}
\]
If \(\bar B=I_2\), its left side is \(\operatorname{tr}\bar P=1\) while its right side is zero, proving nonrepresentation. If \(\bar B\) is non-scalar, the lemma gives exactly four regular solutions to (4) modulo two when \(\det\bar B=0\) and exactly two when \(\det\bar B=1\). Each lifts to \(2^{k-j-1}\) solutions modulo \(2^{k-j}\), and every projector there has \(4^j\) lifts to \(R_k\). Hence
\[
 r_k(I_2+A)=\begin{cases}
 2^{k+j+1},&\det\bar B=0,\\
 2^{k+j},&\det\bar B=1,
 \end{cases} \tag{5}
\]
when \(\bar B\) is non-scalar. Together with (2) and (3), this proves the exact zero criterion and the lower bound. Equality in the lower bound is attained by every primitive non-scalar target in (2).

**Step 5: count all holes.** For a fixed \(j\in\{1,\ldots,k-1\}\), the obstructed trace-zero matrices \(A\) satisfy \(A=2^j B\) with \(B\equiv I_2\pmod2\). The traceless matrix \(B\) has three free entries, each fixed modulo two; there are exactly \(8^{k-j-1}\) such values. Distinct \(j\)'s cannot overlap, because \(B\) is primitive. Summing these disjoint strata produces \(Z_k=(8^{k-1}-1)/7\). Subtraction from the \(8^k\) trace-two matrices proves the support formula and its \(55/56\) limiting density.

## Verification

The standalone standard-library checker `check.py` separately constructs all projectors and their complete ordered sum convolution for every modulus \(2^k\) with \(2\le k\le5\). At **every** trace-two target it verifies the support criterion, the pointwise formulas (2) and (5), the lower bound (3), the hole count, the total ordered-pair mass, and the sharp least positive fiber. Run `python3 check.py` from the package directory. The success marker is `DYADIC_PROJECTOR_CONVOLUTION_SUPPORT_PASS`. These finite checks are not a proof for unbounded \(k\); Steps 1–5 supply that proof.

## Relationship to prior work

De Seguins Pazzis [1] classifies linear combinations of two idempotents over arbitrary **fields**, including characteristic two, but its theorems do not address the higher dyadic congruence levels or count the holes in this convolution support. His companion paper [2] studies sums of idempotents over fields. Fan and Yang [3] study the different problem of decomposing a matrix over a local ring as a *unit plus one commuting idempotent*, not a pair of trace-one projectors. Hartwig and Putcha [4] previously classified sums/differences of two idempotents through Jordan and elementary-divisor data over fields, not the explicit dyadic local-ring convolution.

The standard field-level description is compatible with the fact that there are no holes at depth one. The new obstruction appears only at depths \(k\ge2\), and previous odd-prime projector convolution results do not cover this dyadic case. The comparison is bounded: an unlocated earlier local-ring two-idempotent decomposition or representation-density theorem could imply the present criterion.

## Limitations

The theorem concerns the rank-one idempotent orbit in \(M_2(\mathbb Z/2^k\mathbb Z)\), its ordinary **additive** convolution, and the trace-two hyperplane. It does not determine the full distribution of positive representation multiplicities in the primitive-scalar sector, an explicit closed fourth Fourier moment, the characteristic-two polynomial ring case, or higher matrix dimensions. Independent mathematical validation and exhaustive historical-priority verification have not been performed.

## References

1. C. de Seguins Pazzis, *On linear combinations of two idempotent matrices over an arbitrary field*, arXiv:0907.4436v1, first publicly posted 25 July 2009, https://arxiv.org/abs/0907.4436.
2. C. de Seguins Pazzis, *On sums of idempotent matrices over a field of positive characteristic*, arXiv:0907.5360v1, first publicly posted 30 July 2009, https://arxiv.org/abs/0907.5360.
3. L. Fan and X. Yang, *Strongly clean matrix rings over commutative rings*, arXiv:0803.2176v1, first publicly posted 14 March 2008, https://arxiv.org/abs/0803.2176.
4. R. E. Hartwig and M. S. Putcha, *When is a matrix a difference of two idempotents?*, *Linear and Multilinear Algebra* 26 (1990), 267–277, DOI:10.1080/03081089008817983; bibliographic abstract inspected, full manuscript unavailable.
