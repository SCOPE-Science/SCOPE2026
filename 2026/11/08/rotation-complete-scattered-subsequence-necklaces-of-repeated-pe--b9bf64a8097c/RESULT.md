# Rotation-complete scattered-subsequence necklaces of repeated permutation words

## Finding

Fix an integer \(q\ge2\), an integer \(k\ge1\), and a linear host word
\[
W_{q,k}=(0\,1\,\cdots\,(q-1))^k.
\]
For each \(h\ge1\), write \(R_{q,k}(h)\) for the number of distinct cyclic-rotation classes (necklaces) of length \(h\) for which **every** rotation is a *scattered subsequence* of this **fixed linear host**. This is not a question about factors, subsequences of rotated hosts, or multiplicity of embeddings.

For a representative \(u=(u_0,\dots,u_{h-1})\), define its cyclic weak-descent number
\[
c(u)=\sum_{i=0}^{h-1}\mathbf1_{u_i\ge u_{(i+1)\bmod h}}.
\]
A nonconstant necklace satisfies the all-rotations condition if and only if \(c(u)\le k-1\). For a constant necklace, the condition is \(h\le k\).

Let \(M_q(z)\) be the \(q\)-by-\(q\) matrix whose \((a,b)\) entry is \(z\) if \(a\ge b\) and \(1\) otherwise, and write \(\varphi\) for Euler's totient. Then, for every \(h\ge1\),
\[
\boxed{R_{q,k}(h)=q\mathbf1_{h=k}+\frac1h\sum_{d\mid h}\varphi(d)
  \sum_{j=0}^{k-1}[z^j]\operatorname{tr}(M_q(z^d)^{h/d}).}
\]
The formula is integral, nonnegative, and exact for every alphabet size, repetition count, and word length.

For \(k\ge2\), the maximal realizable length is \(q(k-1)\). There is exactly one maximal necklace, represented by \((0\,1\,\cdots\,(q-1))^{k-1}\), except when \((q,k)=(2,2)\); in that exceptional case the maximal length is two and the three necklaces are \([00]\), \([11]\), and \([01]\). For \(k=1\) the maximal length is one, with \(q\) constant necklaces.

The first two lengths below the maximum exhibit a simple, sharp defect enumeration. For \(q\ge3\), \(k\ge3\), and \(d=k-1\),
\[
\begin{aligned}
R_{q,k}(qd)&=1,\\
R_{q,k}(qd-1)&=q,\\
R_{q,k}(qd-2)&=\binom q2+\left\lfloor\frac{d-1}{2}\right\rfloor q^2+\mathbf1_{2\mid d}\binom{q+1}{2}.
\end{aligned}
\]
Thus the full spectrum has a uniform finite transfer formula, and its top three layers admit closed structural classifications.

## Assumptions and scope

The alphabet is labeled and totally ordered, and every symbol occurs exactly once per repeated block. The host \(W_{q,k}\) has length \(qk\) and is **linear**, not circular. A query of length \(h\) is accepted only if each of its (possibly coinciding) \(h\) cyclic rotations can be obtained by deleting arbitrary positions from the same host. Distinct necklaces, not placements of their representatives, are counted. Empty words are excluded. The inequalities in \(c(u)\) are weak, so equality counts as a descent. The coefficient operation \([z^j]\) extracts the exact coefficient of a polynomial, with \(j\) a nonnegative integer.

## Proof

**1. Greedy copies and weak descents.** Greedily embedding any nonempty word \(v=(v_0,\ldots,v_{h-1})\) in the infinite periodic extension of the block uses the first block for \(v_0\). Since every block is the strictly increasing permutation, its next symbol fits in the current block exactly when it is strictly greater than its predecessor; otherwise a fresh block must be entered. The minimum number of blocks required is therefore
\[
1+\sum_{i=0}^{h-2}\mathbf1_{v_i\ge v_{i+1}}.
\]
The greedy algorithm is optimal because the earliest possible occurrence never disadvantages a later match. Consequently \(v\) occurs in \(W_{q,k}\) exactly when this block count is at most \(k\).

For a cyclic word \(u\), cutting just after an edge with weak descent omits one of the \(c(u)\) counted edges, leaving \(c(u)-1\) linear weak descents. Cutting after an ascent omits none, leaving \(c(u)\). Every nonconstant circular word has at least one ascent: an all-weakly-decreasing cycle would force every letter to be equal. Thus the *largest* minimum-block count among rotations of a nonconstant word is \(1+c(u)\), proving the threshold \(c(u)\le k-1\). For a constant word, every cut omits one weak descent and its block requirement is \(h\), proving the different constant threshold.

**2. Transfer-matrix and orbit count.** The trace polynomial
\[
T_{q,h}(z)=\operatorname{tr}(M_q(z)^h)
=\sum_{u\in\Sigma_q^h}z^{c(u)}
\]
sums over all length-\(h\) sequences with a marked position, with the closing cyclic edge included. To apply Burnside's lemma to the position-rotation action of the cyclic group of order \(h\), consider a rotation having exactly \(d\) repeated blocks, each of length \(h/d\). There are \(\varphi(d)\) rotations with that repetition number. A fixed word is a \(d\)-fold repetition of a smaller word, and its cyclic weak-descent statistic is \(d\) times that of the shorter word. Accordingly the fixed-point weight polynomial is \(T_{q,h/d}(z^d)\). Keeping only terms of degree at most \(k-1\) before the Burnside average counts necklaces satisfying the nonconstant criterion together with all constant necklaces of length less than \(k\). Precisely at \(h=k\), the \(q\) constant necklaces meet the subsequence criterion but have cyclic weak-descent count \(k\), so they must be added once. For \(h>k\) they are correctly excluded. This proves the displayed formula.

**3. Maximal length.** For a nonconstant circular word with \(c\) cyclic weak descents, cut after each weak descent. The resulting \(c\) consecutive arcs are nonempty strictly increasing strings, so each contains at most \(q\) letters and \(h\le qc\le q(k-1)\). If equality holds, each arc is precisely the full increasing alphabet block; the resulting unique necklace is \([(0\cdots(q-1))^{k-1}]\). Constant accepted words have length at most \(k\). For \(q,k\ge2\), the inequality \(q(k-1)\ge k\) is strict except for \(q=k=2\), and this explains the sole additional maximal constant necklaces in the exceptional case. When \(k=1\), the preceding threshold excludes nonconstant necklaces, leaving exactly the length-one constant words.

**4. The top-three defect layers.** Let \(q\ge3\), \(d=k-1\ge2\), and take length \(h=qd-r\) for \(r=0,1,2\). Then \(h>q(d-1)\), so every accepted nonconstant word has exactly \(d\) weak descents (at least \(d\) by the arc bound, at most \(d\) by acceptance). Its canonical decomposition at those weak descents consists of \(d\) strictly increasing nonempty arcs. Represent each arc by the subset of alphabet symbols it retains; the sum of its missing-symbol counts over all arcs is exactly \(r\).

Every such assignment of missing symbols with total \(r\le2\) produces the required weak descents between consecutive increasing arcs. Indeed, if an arc ended at symbol \(a\) and the next began at a strictly greater symbol \(b\), the first arc would have to miss every symbol above \(a\) and the next miss every symbol below \(b\). The combined number of omitted letters would be at least \((q-1-a)+b\ge q\), impossible when \(r\le2<q\). Thus all assigned arcs glue validly, and their cut-at-descent decomposition is unique. Counting accepted necklaces is exactly counting cyclic arrays of \(d\) increasing-symbol subsets with total deficit \(r\).

For \(r=0\) every arc is full, giving one class. For \(r=1\) there is a single deficient arc with a chosen missing symbol, giving \(q\) classes. For \(r=2\), either (i) one arc misses two distinct symbols, giving \(\binom q2\) cyclic classes, or (ii) two different arcs each miss one symbol. In case (ii), their cyclic separation modulo reversal of the choice of the two distinguished positions has \(\lfloor(d-1)/2\rfloor\) non-antipodal distances, each with \(q^2\) ordered symbol assignments. If \(d\) is even, the antipodal distance permits exchanging the two single-letter labels, giving \(\binom{q+1}{2}\) classes. Summing produces the claimed third formula. The decomposition proves these are exact formulas rather than extrapolations from finite data.

## Verification

The accompanying standard-library script `verify.py` reproduces the weighted trace and Burnside calculation without relying on a symbolic-algebra package. It independently enumerates all necklaces, all their cyclic rotations, and direct greedy/subsequence embeddings for eleven alphabet/repetition parameter pairs. Its finite checks cover 76 full length cases (up to one beyond the host length), compare the structural boundary formulas in 60 parameter cases, and check low-length/full-necklace and support identities over a further grid. Run from the extracted directory with `python3 verify.py`. The script prints a single `PASS` line if all assertions succeed. These tests corroborate the proof, but do not certify the infinitely many cases.

## Relationship to prior work

The 2022 study by Kosche, Koß, Manea and Pak investigates scattered matching under bounded ranges, including *circular host matching*, wherein one chooses a rotation of the host. Our condition instead fixes the host and requires **all rotations of an individual query** to occur, and our counted objects are cyclic classes of query words. The 2021 work of Fleischmann, Germann and Nowotka studies *scattered-factor universality* and related circular universality: a host universal for every query up to a fixed length is a different quantifier structure from counting partially allowed all-rotation query necklaces. The 2021 work of Hirakawa, Nakashima, Inenaga and Takeda counts Lyndon subsequences; a Lyndon string is a canonical representative of a primitive necklace, but occurrence of that representative alone does not imply that its other rotations also occur, and nonprimitive necklaces are included here. The present exact all-length transfer formula and sharp boundary layers are not stated in the inspected portions of these works. A potentially equivalent unindexed theorem cannot be excluded.

## Limitations

The result requires blocks that are full permutations of distinct letters in a fixed increasing order, not arbitrary repeated words or a host allowed to rotate. It counts **necklaces**, not individual accepted linear query words or their embedding multiplicities. The three simple boundary formulas require \(q\ge3\) and \(k\ge3\); the general transfer formula and longest-length statement handle the smaller cases. The mathematical derivation is self-contained, while the originality comparison is necessarily limited to the named and searched literature. No independent scientific audit has been performed.

## References

1. P. Fleischmann, S. Germann and D. Nowotka, *Scattered Factor Universality—The Power of the Remainder*, arXiv:2104.09063 (first public preprint April 19, 2021). https://arxiv.org/abs/2104.09063
2. M. Hirakawa, Y. Nakashima, S. Inenaga and M. Takeda, *Counting Lyndon Subsequences*, arXiv:2106.01190 (first public preprint June 2, 2021). https://arxiv.org/abs/2106.01190
3. A. Kosche, T. Koß, F. Manea and S. Pak, *Subsequences in Bounded Ranges: Matching and Analysis Problems*, arXiv:2207.09201 (first public preprint July 19, 2022). https://arxiv.org/abs/2207.09201
