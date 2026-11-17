# Exact radius-four flag-rank sphere volumes over finite fields

## Finding

For every prime power \(q\) and every integer \(n\ge 4\), let \(\mathrm U(n,\mathbb F_q)\) be the upper triangular matrices. For \(M\in\mathrm U(n,\mathbb F_q)\), write \(M_{[i]}\) for the submatrix in rows \(1,\ldots,i\) and columns \(i,\ldots,n\), and put
\[
\operatorname{fr}(M)=\sum_{i=1}^{n}\operatorname{rank}_{\mathbb F_q}M_{[i]}.
\]
The number \(s_q(n,4)\) of matrices of flag-rank weight exactly four is
\[
\boxed{\displaystyle
s_q(n,4)=\sum_{r=1}^{4}\binom{3}{r-1}\binom{n-3}{r}(q-1)^r(q^2+q-1)^{4-r}
+(n-2)q^3(q-1)^2(q+1).}
\]
Here \(\binom{m}{r}=0\) for \(0\le m<r\). In particular, for every fixed \(n\ge4\),
\[
s_q(n,4)=(n-3)q^7+O_n(q^6)\quad\text{as prime powers }q\longrightarrow\infty.
\]
The exact radius-four ball volume is consequently \(b_q(n,4)=b_q(n,3)+s_q(n,4)\), where \(b_q(n,3)\) is the established radius-three volume given in the first reference. Thus the formula supplies a concrete sphere-packing input for any flag-rank code of minimum distance at least nine; it is not an existence assertion for a perfect code.

## Assumptions and scope

The field is an arbitrary finite field \(\mathbb F_q\), including nonprime fields; no characteristic restriction is used. Indices run from \(1\) to \(n\). The weight sums ordinary matrix ranks over the same field. The sphere is centered at the zero matrix, but translation invariance yields the same count at every center. The main formula is asserted for integers \(n\ge4\), not merely for the enumerated small cases. We use the abbreviations \(u=q-1\) and \(t=q^2+q-1\) below.

## Proof

**1. Active cuts and separated runs.** Call cut \(i\) active if \(\operatorname{rank}M_{[i]}>0\). A nonzero entry \(M_{a,b}\) with \(a\le b\) belongs to all cut submatrices \(M_{[i]}\) for \(a\le i\le b\). Consequently an inactive cut forces to zero every entry that crosses it. The matrix decomposes into upper triangular principal blocks on the maximal consecutive runs of active cuts, with all remaining entries zero. The flag-rank weight is the sum of the weights of those blocks.

If the weight is four, there can be at most four active cuts. A run of one active cut has rank profile \((1)\); a run of two has profile \((1,1)\), since its cut matrices have only one row or one column. A run of three has profile \((1,1,1)\) or \((1,2,1)\), because its first and last cut matrices have rank one and its middle cut has rank at most two. Therefore all weight-four matrices fall into exactly two disjoint classes: four active cuts, all of rank one; or exactly three consecutive active cuts with rank profile \((1,2,1)\). One or two active cuts cannot carry weight four, and any three nonconsecutive active cuts have total weight three.

**2. Count the all-rank-one blocks.** Let \(F_j\) count upper triangular \(j\times j\) blocks with all \(j\) cuts of rank exactly one. We prove, for \(1\le j\le4\), that
\[
F_j=u\,t^{j-1}.
\]
Clearly \(F_1=q-1=u\). For a \(2\times2\) upper triangular block, if its superdiagonal entry is nonzero the diagonal entries are arbitrary, and otherwise both diagonal entries must be nonzero. Thus
\[
F_2=q^2(q-1)+(q-1)^2=u(q^2+q-1)=ut.
\]
For a \(3\times3\) upper triangular block, its middle \(2\times2\) cut matrix \(B\) must be nonzero of rank one. Among such \(B\), the number with its top row and last column both nonzero is \(q^2(q-1)\); with exactly one of these vectors zero it is \(q(q-1)\) in either case; with both zero it is \(q-1\). The two outside diagonal entries are arbitrary unless the adjoining top row or last column of \(B\) vanishes, in which case the corresponding diagonal entry must be nonzero. Hence
\[
F_3=q^4(q-1)+2q^2(q-1)^2+(q-1)^3=u(q^2+q-1)^2=ut^2.
\]
For a \(4\times4\) upper triangular block, write its central \(2\times2\) rectangle (rows \(1,2\), columns \(3,4\)) as \(B\). The second and third cut matrices must be nonzero rank-one matrices, so \(B\) has rank at most one. If \(B=0\), the remaining left and right triples of entries separately satisfy the two-cut conditions counted by \(F_2\), giving \(F_2^2\) choices. If \(B\) has rank one, the new left column of the second cut must belong to its column space and the new bottom row of the third cut must belong to its row space, giving \(q\) choices for each. The two outer diagonal entries have exactly the same nonvanishing requirements as in the \(F_3\) count. This gives \(q^2F_3\) choices. Therefore
\[
F_4=F_2^2+q^2F_3=u^2t^2+q^2ut^2=ut^3.
\]
The rank-one matrix count used above is \(\#\{B\in\mathbb F_q^{2\times2}:\operatorname{rank}B=1\}=(q^2-1)^2/(q-1)\), so these steps hold for every prime power, not only prime fields.

**3. Count the exceptional rank-two cut.** A \(3\times3\) block has rank profile \((1,2,1)\) precisely when its central \(2\times2\) cut matrix is invertible. The two outside diagonal entries are arbitrary because the first and last cut matrices are automatically nonzero. The number of these blocks is
\[
H_3=q^2\lvert\mathrm{GL}_2(\mathbb F_q)\rvert
=q^2(q^2-1)(q^2-q)=q^3(q-1)^2(q+1).
\]
They can occupy any of the \(n-2\) consecutive triples of cut indices, contributing \((n-2)H_3\) matrices.

**4. Place the four rank-one cuts.** Suppose the four active cuts form \(r\) ordered consecutive runs, of lengths \(j_1,\ldots,j_r\ge1\) summing to four. Their block contributions multiply to
\[
\prod_{a=1}^rF_{j_a}=u^r t^{4-r}.
\]
There are \(\binom{3}{r-1}\) ordered compositions of four into \(r\) positive parts. For each ordered composition there are \(\binom{n-3}{r}\) ways to place the runs inside \(1,\ldots,n\): reserve one inactive cut between consecutive runs and distribute the remaining inactive cuts among the two ends and the \(r-1\) internal gaps. Summing over \(1\le r\le4\), then adding the disjoint three-cut class from Step 3, proves the boxed formula. Its largest power in \(q\), for fixed \(n\ge4\), is the \(r=1\) term \((n-3)q^7\); all other terms have degree at most six. \(\square\)

## Verification

The standalone `checker.py` enumerates all upper triangular matrices over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\) in explicitly selected small dimensions; ranks are computed by field Gaussian elimination, independently of the proof's run decomposition. The extension field \(\mathbb F_4\) is represented as \(\mathbb F_2[t]/(t^2+t+1)\). The exhaustive counts include \(s_2(4,4)=173\), \(s_3(4,4)=3526\), \(s_2(5,4)=397\), and the dimension-three boundary counts \(24,432,2880,12000\) at field orders \(2,3,4,5\), respectively. These finite checks are consistency tests, not the proof for arbitrary dimension or field.

The independent `checker.c` uses binary row elimination on packed bit vectors and exhausts all upper triangular binary matrices through dimension six, confirming \(s_2(6,4)=711\). Its source code and execution commands are included with this result. The general proof is the preceding cut-rank classification and finite-field counts.

## Relationship to prior work

Alfarano, Mushrraf and Zullo (2026) introduced the explicit flag-rank sphere enumeration up to radius three (Section 3, Propositions 3.1–3.3), and their conclusion names arbitrary-radius sphere volumes as a natural open direction. The present formula is a radius-four enumeration for every dimension at least four and every prime-power field order. The earlier Alfarano–Neri–Zullo paper (2023 preprint, 2024 journal) develops the flag-rank metric and Singleton-like bounds but does not give this radius-four sphere count. The original Fourier–Nebe formulation supplies the metric framework, not this enumeration. The dimension-three boundary is already recoverable from earlier small-dimension counts and is not asserted as a new isolated result.

## Limitations

No expression for spheres of radius five or larger is proved here. The formula determines a packing volume but does not construct perfect codes, classify distance-nine codes or establish their existence. The evidence considered does not exclude an equivalent enumeration in other terminology or unindexed literature. Exhaustive tests cover only the indicated finite parameter sets; the unbounded claim relies on the written proof.

## References

1. G. N. Alfarano, U. Mushrraf, and F. Zullo, *On perfect flag-rank metric codes*, arXiv:2606.12934v1 (first public version, 2026-06-11). https://arxiv.org/abs/2606.12934
2. G. N. Alfarano, A. Neri, and F. Zullo, *Maximum Flag-Rank Distance Codes*, arXiv:2303.16653v1 (2023-03-29); Journal of Combinatorial Theory, Series A 207 (2024), 105908. https://arxiv.org/abs/2303.16653
3. G. Fourier and G. Nebe, *Degenerate flag varieties in network coding*, arXiv:2003.02002v1 (2020-03-04); Advances in Mathematics of Communications 17 (2023), 888–899. https://arxiv.org/abs/2003.02002
