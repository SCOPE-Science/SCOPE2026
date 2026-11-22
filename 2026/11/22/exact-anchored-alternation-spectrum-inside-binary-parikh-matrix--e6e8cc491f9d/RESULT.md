# Exact anchored-alternation spectrum inside binary Parikh-matrix classes

## Finding

For integers \(A\ge1\), \(B\ge0\), and \(0\le C\le AB\), let \(\mathcal L_{A,B,C}\) be the set of binary words with precisely \(A\) letters \(a\), \(B\) letters \(b\), and \(C\) scattered occurrences of \(ab\). For a word \(w\), let \(J(w)\) be the largest integer \(j\ge0\) such that the alternating word \(a(ba)^j\) is a scattered subsequence of \(w\). The longest alternating scattered subsequence beginning and ending with \(a\) therefore has length \(2J(w)+1\).

Write \(N_{A,B,C,j}=|\{w\in\mathcal L_{A,B,C}:J(w)=j\}|\). The following **exact full distribution** holds for every \(A\ge1\):

\[
\sum_{B,C,j\ge0}N_{A,B,C,j}\,u^B z^C v^j
=\frac{1}{(1-u)(1-uz^A)}\prod_{i=1}^{A-1}
\left(1+\frac{vuz^i}{1-uz^i}\right).
\tag{1}
\]

In particular, summing over \(C\),
\[
\sum_{C\ge0}N_{A,B,C,j}
=\binom{A-1}{j}\binom{B+1}{j+1},
\tag{2}
\]
with the convention that out-of-range binomial coefficients vanish. This simultaneously counts avoidance of every anchored odd alternating pattern: the number avoiding scattered \(a(ba)^r\), \(r\ge1\), is \(\sum_{j=0}^{r-1}N_{A,B,C,j}\).

For the stable low-area regime \(0\le C<A\) and \(B\ge C\), the conditional distribution of \(J\) in \(\mathcal L_{A,B,C}\) is **exactly** the distribution of the number \(D(\lambda)\) of distinct part sizes of a uniformly selected integer partition \(\lambda\) of \(C\). Consequently, denoting its counting function by \(p_j(C)\) and the unrestricted partition number by \(p(C)\),
\[
N_{A,B,C,j}=p_j(C),\qquad
\Pr\{a(ba)^r\not\preceq W\}=
\frac{\sum_{j=0}^{r-1}p_j(C)}{p(C)}.
\tag{3}
\]
Here \(W\) is uniform in \(\mathcal L_{A,B,C}\), and \(\preceq\) means scattered-subsequence containment. The sharp support in this stable regime is \(J=0\) if \(C=0\), and for \(C\ge1\) all and only integers \(1\le J\le\lfloor(\sqrt{8C+1}-1)/2\rfloor\) occur. For every fixed integer \(r\ge2\), as \(C\to\infty\) through this regime,
\[
\log \Pr\{a(ba)^r\not\preceq W\}
=-\pi\sqrt{2C/3}+O_r(\log C).
\tag{4}
\]
The expected anchored-alternation index is exactly
\[
\mathbb E J(W)=\frac{1}{p(C)}\sum_{k=1}^{C}p(C-k)
\sim\frac{\sqrt{6C}}{\pi}.
\tag{5}
\]
The empty partition has \(D=0\), \(p(0)=1\); (4) is stated only for \(r\ge2\) and \(C\to\infty\).

For example, in any stable class with \(C=10\), the exact counts for \(J=1,2,3,4\) are \(4,22,15,1\), respectively, among \(p(10)=42\) representatives. Thus the scattered pattern \(ababa\) is absent in exactly four of those forty-two words.

## Assumptions and scope

The words are finite, linear (not cyclic), over the ordered two-symbol alphabet \(\{a,b\}\). A scattered occurrence selects strictly increasing positions, not necessarily consecutive ones. Letter counts and the count of scattered \(ab\)-pairs are fixed, and words are counted as distinct strings, not by position embeddings. The parameter \(A\) is at least one, so \(a\) itself is present and \(J\ge0\) is defined. No assertion about the longest *unanchored* alternating subsequence is made. Formula (1) is a formal-power-series identity in \(u,z,v\), or a rational identity over \(\mathbb Q(z,v)[[u]]\).

## Proof

**Step 1 (unique gap representation).** Every word with \(A\ge1\) copies of \(a\) is written uniquely as
\[
w=b^{x_0}ab^{x_1}a\cdots ab^{x_A},\qquad x_i\in\mathbb Z_{\ge0}.
\]
It has \(B=\sum_{i=0}^{A}x_i\) and \(C=\sum_{i=0}^{A}i x_i\), because each \(b\) in gap \(i\) has precisely \(i\) earlier copies of \(a\).

**Step 2 (anchored alternating subsequences).** Let \(S(w)=\{i:1\le i\le A-1,\ x_i>0\}\). If \(i_1<\cdots<i_j\) belong to \(S(w)\), choose one \(b\) in each indicated gap; choose an \(a\) before the first chosen \(b\), between successive chosen gaps, and after the last one. This realizes \(a(ba)^j\). Conversely, in any occurrence of \(a(ba)^j\), its \(j\) chosen \(b\)'s must lie in *distinct* interior gaps: the intervening \(a\)'s prohibit the same gap, and the leading/trailing \(a\)'s prohibit gaps \(0\) and \(A\). Therefore \(J(w)=|S(w)|\) exactly. This proves the stated maximum-length interpretation and the exact avoidance criterion.

**Step 3 (trivariate counting).** Gap \(0\) contributes \(1/(1-u)\), and gap \(A\) contributes \(1/(1-uz^A)\). Every interior gap \(i\) contributes \(1\) if empty and \(v\sum_{t\ge1}(uz^i)^t=vuz^i/(1-uz^i)\) if occupied. The product gives (1); uniqueness in Step 1 prevents overcounting.

**Step 4 (fixed-composition total).** If exactly \(j\) of the \(A-1\) interior gaps are occupied, their index set has \(\binom{A-1}{j}\) choices. For each set, write the \(j\) positive occupancies as one plus a nonnegative integer. Along with the two nonnegative end-gap occupancies, the remaining \(B-j\) letters distribute among \(j+2\) labeled gaps in \(\binom{B+1}{j+1}\) ways. This proves (2), including \(j>B\), for which both sides vanish.

**Step 5 (stable partition bijection).** Suppose \(C<A\) and \(B\ge C\). The equation \(C=\sum i x_i\) forces \(x_A=0\). The positive-size gap occupancies \(x_i\), \(i\ge1\), are precisely the multiplicities of part size \(i\) in a partition of \(C\). Conversely, every partition of \(C\) has total number of parts at most \(C\le B\); placing the unused \(B-\sum_{i\ge1}x_i\) letters into gap \(0\) reconstructs exactly one word. Because all part sizes are at most \(C<A\), the number of distinct part sizes equals \(J\). This proves (3). To obtain the exact support, each partition with \(j\) distinct positive part sizes has area at least \(1+2+\cdots+j=j(j+1)/2\). Conversely, whenever \(C\ge j(j+1)/2\), the partition with parts \(1,2,\ldots,j-1,C-j(j-1)/2\) has exactly \(j\) distinct positive sizes. This gives every and only the claimed values.

**Step 6 (asymptotic rarity and mean).** For fixed \(r\ge2\), there is at least one partition of \(C\) with at most \(r-1\) distinct part sizes for \(C\ge1\) (the all-ones partition), while the number of such partitions is at most \(\sum_{j=1}^{r-1} C^{2j}=C^{O(r)}\): specify at most \(j\) part sizes and their multiplicities, each in \(\{1,\ldots,C\}\). The Hardy–Ramanujan asymptotic \(p(C)\sim(4C\sqrt3)^{-1}\exp(\pi\sqrt{2C/3})\) proves (4).

For each positive integer \(k\le C\), removing one part of size \(k\) bijects partitions of \(C\) containing that size with partitions of \(C-k\). Summing indicator variables for distinct part sizes gives the exact expectation in (5). For its asymptotic, put \(h=C^{3/5}\). Uniformly for \(1\le k\le h\), the Hardy–Ramanujan formula gives \(p(C-k)/p(C)=\exp(-\pi k/\sqrt{6C})(1+o(1))\), as the quadratic expansion error is \(O(h^2/C^{3/2})=o(1)\). For \(k>h\), monotonicity of \(p\) bounds their total contribution by \(C p(C-\lfloor h\rfloor)/p(C)=C\exp(-\Omega(C^{1/10}))=o(1)\). Hence the main sum is asymptotic to the geometric sum \(1/(e^{\pi/\sqrt{6C}}-1)\sim\sqrt{6C}/\pi\).

All steps apply to arbitrary integer parameters in the stated domains; finite checks listed below are supplementary, not the proof of the infinite claims.

## Verification

Two separate Python scripts are included: `verify_direct.py` enumerates 3,424 literal words across 42 fixed \((A,B)\) cases, computes their longest anchored alternating scattered subsequences by greedy subsequence matching, compares the full joint \((C,J)\) distribution with an independently enumerated gap formula, and checks the fixed-composition totals. `verify_stable.py` checks the stable partition correspondence at each \(C=0,\ldots,35\) using an independent recursive enumeration of distinct part sizes and a finite-state coefficient calculation. Run using Python 3: `python3 verify_direct.py` and `python3 verify_stable.py`. Their recorded outputs are in `verification_output.txt`.

## Relationship to prior work

Fazekas, Huang and Mercaş (arXiv:2610.06717, first posted October 5, 2026), §§2, 3 and 5, introduce the exact binary Parikh-matrix class \(\mathcal L_{A,B,C}\), the partition model, a fixed-pattern universal/existential criterion, and a general additive approximation for fixed-pattern containment probabilities. Their Lemma 5.2 uses bounded alternating-run templates; Theorem 5.7 gives an approximation scheme but not the exact distribution (1), the fixed-composition coefficient (2), or the distinct-part-spectrum interpretation (3) and mean (5).

Richomme (arXiv:2510.07159, first posted October 8, 2025), §4.2, proves the underlying word–partition bijection and analyzes a partition-lattice structure. That bijection underlies Step 5, but the inspected claims concern the class/graph itself rather than the anchored alternating-subsequence statistic.

Related published records on scattered \(ab^t a\)-avoidance count interior-letter multiplicities or partition restrictions of a different kind, and records on fixed-length balanced patterns address different subsequences. These results are not statements of the joint spectrum in (1). An earlier equivalent of the statistic-to-partition identification cannot be ruled out by finite literature searches.

## Limitations

The theorem concerns only anchored odd alternating subsequences in binary words and does not classify general alternating subsequences, other alphabets, or arbitrary patterns. The partition-law and asymptotic parts require \(C<A\), \(B\ge C\), while the full generating function covers all \(A\ge1\), \(B\ge0\), \(C\ge0\). The constants in \(O_r(\log C)\) can depend on fixed \(r\); no uniform growing-\(r\) limit is asserted. The finite verification is not a proof of (1) for unbounded parameters. Historical-priority checks are not exhaustive.

## References

1. S. Z. Fazekas, X. Huang, R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717 (v1 first public October 5, 2026), https://arxiv.org/abs/2610.06717.
2. G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159 (v1 first public October 8, 2025), https://arxiv.org/abs/2510.07159.
3. G. H. Hardy and S. Ramanujan, *Asymptotic formulae in combinatory analysis*, Proc. London Math. Soc. (1918), partition asymptotic.
