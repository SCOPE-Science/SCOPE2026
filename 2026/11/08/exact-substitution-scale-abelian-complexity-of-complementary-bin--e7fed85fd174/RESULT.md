# Exact substitution-scale Abelian complexity of complementary binary morphic words

## Finding

Fix an integer \(b\ge 3\). Define the length-\(b\) binary morphism
\[
\varphi_b(0)=0^{b-1}1,\qquad \varphi_b(1)=1^{b-1}0,
\]
and let \(\mathbf w_b=\varphi_b^\omega(0)\) be its one-sided fixed point, indexed from zero. Write \(\mathcal F_n(\mathbf w_b)\) for its distinct contiguous factors of length \(n\), and let
\[
\rho_b(n)=\#\bigl\{\lvert u\rvert_1:u\in\mathcal F_n(\mathbf w_b)\bigr\}
\]
be its Abelian factor complexity. Then for every integer \(k\ge0\),
\[
\boxed{\rho_b(b^k)=2\sum_{j=0}^k(b-2)^j-(b-2)^k+1.}
\]
Equivalently,
\[
\boxed{\rho_3(3^k)=2k+2,\qquad
\rho_b(b^k)=\frac{(b-1)(b-2)^k+b-5}{b-3}\quad(b\ge4).}
\]
In fact, letting \(L=b^k\), \(D=(b-2)^k\), \(H=\sum_{j=0}^k(b-2)^j\), and \(M=2H-D\), the exact set of one-counts of length-\(L\) factors is the full integer interval
\[
\boxed{\left\{\frac{L-M}{2},\frac{L-M}{2}+1,\ldots,\frac{L+M}{2}\right\}.}
\]
The endpoints are attained by factors crossing complementary substitution blocks. For \(k\ge1\), an explicit crossing offset is
\[
r_k=1+\frac{(b-2)(b^k-1)}{b-1}\qquad(0<r_k<b^k).
\]
Consequently the maximal difference in numbers of ones among equal-length factors of length \(b^k\) is exactly \(M=\rho_b(b^k)-1\). For \(b\ge4\), the complexity grows like \(\frac{b-1}{b-3}(b-2)^k\), or equivalently a power \(L^{\log_b(b-2)}\); for \(b=3\) it grows logarithmically with \(L\).

## Assumptions and scope

The base \(b\) is any integer at least three, without any primality assumption. The factor length is exactly a substitution length \(b^k\), and \(k\) is any nonnegative integer. The count \(\lvert u\rvert_1\) is the number of occurrences of the letter \(1\) in a finite factor \(u\). In a binary alphabet, Abelian equivalence is precisely equality of these counts at fixed length.

The word \(\mathbf w_b\) can also be defined by \(\mathbf w_b(n)\equiv\#\{\text{base-}b\text{ digits of }n\text{ equal to }b-1\}\pmod2\), with leading zeroes ignored. Thus the result concerns a natural digit-automatic family, not arbitrary substitutions chosen separately for each length.

## Proof

**1. Substitution blocks and their signed sums.** Define \(A_k=\varphi_b^k(0)\), of length \(L_k=b^k\). The image of \(1\) is the bitwise complement \(\overline{A_k}\). Let \(\epsilon(0)=1\), \(\epsilon(1)=-1\), and put
\[
F_k(r)=\sum_{j=0}^{r-1}\epsilon(A_k(j)),\qquad 0\le r\le b^k.
\]
The total signed sum is
\[
D_k=F_k(b^k)=(b-2)^k,
\]
since every application of \(\varphi_b\) multiplies the signed sum by \(b-2\). Set \(c=b-2\), \(H_k=\max_r F_k(r)\), and \(m_k=\min_r F_k(r)\).

The block recurrence \(A_k=A_{k-1}^{\,b-1}\overline{A_{k-1}}\) yields, for \(0\le r\le b^{k-1}\),
\[
F_k(d b^{k-1}+r)=
\begin{cases}
dD_{k-1}+F_{k-1}(r),&0\le d\le b-2,\\
(b-1)D_{k-1}-F_{k-1}(r),&d=b-1.
\end{cases}
\]
The endpoint overlaps in this representation agree, so taking maxima and minima is legitimate. Therefore
\[
H_k=\max\{cD_{k-1}+H_{k-1},\ (b-1)D_{k-1}-m_{k-1}\},
\]
\[
m_k=\min\{m_{k-1},\ (b-1)D_{k-1}-H_{k-1}\},
\]
with \(H_0=1\), \(m_0=0\), and \(D_0=1\).

**2. Exact prefix extrema.** We claim
\[
H_k=\sum_{j=0}^k c^j,\qquad
m_k=\begin{cases}\min(0,2-k),&b=3,\\0,&b\ge4.\end{cases}
\]
For \(b=3\), \(c=D_k=1\). Substituting the displayed expressions into the two extrema recurrences gives \(H_k=k+1\) and \(m_k=\min(0,2-k)\) by induction: the candidate \(1+H_{k-1}=k+1\) dominates \(2-m_{k-1}\).

For \(b\ge4\), \(c\ge2\). Assume \(m_{k-1}=0\) and \(H_{k-1}=\sum_{j=0}^{k-1}c^j\). Then
\[
D_{k-1}\le H_{k-1}\le\frac{c}{c-1}D_{k-1}\le(b-1)D_{k-1}.
\]
Thus the first candidate dominates in the maximum recurrence, while the minimum stays zero. Hence \(H_k=cD_{k-1}+H_{k-1}=\sum_{j=0}^k c^j\). This proves both formulas for all bases and levels.

Moreover, at every level a maximizing prefix can be chosen inside the \((b-2)\)-th zero block (zero-indexed), followed by a maximizing prefix at the preceding level. Starting with \(r_0=1\), the resulting offsets satisfy \(r_k=(b-2)b^{k-1}+r_{k-1}\), giving the explicit value in the finding. For \(k\ge1\), it is strictly between zero and \(b^k\).

**3. All factor imbalances.** Fix \(k\ge1\) and write \(L=b^k\), \(D=D_k\). Every length-\(L\) factor begins at a position \(qL+r\), where \(0\le r<L\); it is the suffix of one \(k\)-block followed by the prefix of the next. If the parent letters are \(x,y\in\{0,1\}\), its signed sum is exactly
\[
\begin{cases}
(-1)^xD,&x=y,\\
(-1)^x(D-2F_k(r)),&x\ne y.
\end{cases}
\]
The fixed point contains all four binary adjacent pairs: \(00,01\) occur within \(\varphi_b(0)\), while \(11,10\) occur within \(\varphi_b(1)\), and both letters occur in the fixed point. Consequently every indicated parent-pair and offset combination really occurs in a factor of the fixed point.

The signed magnitude of a length-\(L\) factor is thus at most
\[
\max\{D,\ 2H_k-D,\ D-2m_k\}.
\]
From the extrema formulas, \(H_k\ge D\) and \(H_k+m_k\ge D\), so this maximum equals \(M=2H_k-D\). Taking \(r=r_k\), where \(F_k(r_k)=H_k\), and the parent pairs \(01\) and \(10\), produces both signed sums \(-M\) and \(M\). Therefore the minimum and maximum possible one-counts are exactly \((L-M)/2\) and \((L+M)/2\).

As a length-\(L\) window moves forward by one position, its one-count changes by an element of \(\{-1,0,1\}\). Since windows attaining both endpoints exist, every integer between them is attained by some intervening window. This proves that the set of one-counts is precisely the stated full interval, and its cardinality is \(M+1\). At \(k=0\), the two single-letter factors give complexity two, agreeing with the same formula. Substituting the geometric sum proves all closed forms and growth statements. \(\square\)

## Verification

The accompanying standalone `verify.py` generates the finite substitution blocks directly, inspects all windows of substitution length across each of the four ordered pairs of blocks, and compares their complete sets of one-counts with the claimed integer intervals. It independently checks the prefix-maximum construction. The tested cases comprise \(3\le b\le9\) and all \(k\ge0\) for which \(b^k\le12000\), giving \(42\) base/level pairs. It reports `VERIFY_OK tested_base_level_pairs 42` and `EXTREMAL_PREFIX_OK`.

This finite verification is diagnostic only. The unrestricted theorem is proved by the exact recurrences and the factor-intermediate-value argument above.

## Relationship to prior work

Popoli, Shallit and Stipulanti study additive and Abelian complexity of automatic sequences, including explicit examples of bounded and unbounded behavior; over a binary alphabet these two notions coincide. Their paper does not supply the present all-base substitution-scale formula for the complementary morphisms. Rigo, Stipulanti and Whiteland give an effective method for Parikh-collinear morphisms, but the present incidence matrix is \(\left(\begin{smallmatrix}b-1&1\\1&b-1\end{smallmatrix}\right)\), with eigenvalues \(b\) and \(b-2\), hence rank two for \(b\ge3\), outside that theorem's hypotheses. Chen and Wen obtain ultimately periodic Abelian complexity for a different, larger-alphabet generalized Thue–Morse substitution. Blanchet-Sadri, Seita and Wise give a general algorithm for binary uniform morphic words; an algorithm for any fixed instance does not itself state the closed formula uniform in \(b\) and \(k\). The final two papers merit further bibliographic comparison because their relevant full texts were not accessible during the present examination.

## Limitations

The theorem makes no claim about \(\rho_b(n)\) at lengths other than powers of \(b\), nor about independent proof verification. The formula is proved only for integer bases \(b\ge3\). Novelty is qualified by the possibility of a less directly indexed equivalent formulation, especially in the literature on general binary uniform substitutions and substitution balance. An independent scientific review has not been performed.

## References

1. P. Popoli, J. Shallit, M. Stipulanti, *Additive word complexity and Walnut*, arXiv:2410.02409v1, first submitted 2024-10-03, https://arxiv.org/html/2410.02409v1.
2. M. Rigo, M. Stipulanti, M. A. Whiteland, *Automatic Abelian Complexities of Parikh-Collinear Fixed Points*, arXiv:2405.18032v1, first submitted 2024-05-28, https://arxiv.org/html/2405.18032v1.
3. J. Chen, Z.-X. Wen, *On the abelian complexity of generalized Thue-Morse sequences*, arXiv:1809.06554v1, first submitted 2018-09-18, https://arxiv.org/html/1809.06554v2.
4. F. Blanchet-Sadri, D. Seita, D. Wise, *Computing abelian complexity of binary uniform morphic words*, Theoretical Computer Science 640 (2016), 41–51, https://doi.org/10.1016/j.tcs.2016.05.046.
5. M. A. Whiteland, *Asymptotic Abelian Complexities of Certain Morphic Binary Words*, Journal of Automata, Languages and Combinatorics 24 (2019), 89–114, https://doi.org/10.25596/jalc-2019-089.
