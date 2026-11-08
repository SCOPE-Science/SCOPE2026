# Exact periodicity of a missing three-sumfree seed progression

## Finding

Consider the strict greedy three-sumfree sequence initialized with the three positive integers \(1,2,h\): every subsequent term is the smallest larger integer that is not the sum of **three distinct** earlier terms. For every integer \(k\ge2\) put
\[
 h=6k+5,\qquad m=5h-1=30k+24.
\]
Define finite subsets of the positive integers
\[
 \begin{aligned}
 C_k={}&\{1,2\}\cup\bigcup_{j=0}^{k}\{h+6j,h+6j+1,h+6j+2\}
 \cup\{2h+1,2h+6\},\\
 B_k={}&\{6h+6j-1:1\le j\le k+1\}\\
 &\cup\{6h+6j:0\le j\le k\}
 \cup\{6h+6j+1:-1\le j\le k-1\}.
 \end{aligned}
\]
Then the **entire infinite greedy sequence**, as a set of terms, is exactly
\[
 \boxed{S_{1,2,6k+5}=C_k\cup\bigcup_{q\ge0}(B_k+qm).}
\]
The least eventual period of its characteristic sequence is **exactly** \(m=5h-1\). Each eventual block has \(3k+3\) terms, so the natural density exists and is
\[
 \boxed{\delta(S_{1,2,6k+5})=\frac{3k+3}{30k+24}=\frac{h+1}{2(5h-1)}.}
\]
These assertions hold simultaneously for every integer \(k\ge2\), without an upper parameter cutoff. They do not claim periodicity for other residue classes of \(h\).

## Assumptions and scope

All sets contain **positive integers**, and all greedy exclusions use sums of three pairwise distinct **previous** terms; representations with repeated terms are not forbidden. The initial terms are forced to be exactly \(1,2,h\), even if an initial term could have been represented by earlier ones (not relevant for this seed). The notation \(B_k+qm\) means \(\{b+qm:b\in B_k\}\). Intervals below are inclusive integer intervals, with empty intervals omitted.

For proof bookkeeping write an integer as \(6u+r\), where \(r\in\{0,1,2,3,4,5\}\), and put \(M=m/6=5k+4\). The finite set \(C_k\) has the following exact \(u\)-coordinate slices:

| residue \(r\) | \(u\) with \(6u+r\in C_k\) |
|---|---|
| 0 | \([k+1,2k+1]\) |
| 1 | \(\{0\}\cup[k+1,2k+1]\) |
| 2 | \(\{0\}\) |
| 3 | empty |
| 4 | \(\{2k+2\}\) |
| 5 | \([k,2k+1]\) |

The set \(B_k\) has slices \([6k+5,7k+5]\) for \(r=0,5\), \([6k+4,7k+4]\) for \(r=1\), and none otherwise. Consequently its residues \(R=B_k\bmod m\) have slices \([k+1,2k+1]\) for \(r=0,5\), and \([k,2k]\) for \(r=1\).

## Proof

**1. Restricted interval arithmetic.** For any nonempty integer interval \([a,b]\), the sums of two distinct elements fill \([2a+1,2b-1]\), and the sums of three distinct elements fill \([3a+3,3b-3]\), whenever the interval contains enough elements. For sums from different disjoint residue-slices, ordinary integer-interval addition applies. A triple of summands with coordinate residues \(r_1,r_2,r_3\) has residue \(r_1+r_2+r_3\bmod6\) and \(u\)-coordinate equal to the sum of the coordinate values plus \(\lfloor(r_1+r_2+r_3)/6\rfloor\).

Write \(3^{\wedge}C_k\) for the set of sums of three **distinct** elements of \(C_k\), \(2^{\wedge}C_k\) for distinct pairs, and \(P_k=2^{\wedge}C_k+B_k\). Applying these interval rules to the six slices above gives the following **exact** coordinate slices. Each displayed interval includes both endpoints.

| \(r\) | \(3^{\wedge}C_k\): \(u\) ranges | \(P_k\): \(u\) range |
|---|---|---|
| 0 | \([2k+2,6k+4]\) | \([7k+6,11k+8]\) |
| 1 | \([2k+2,6k+3]\) | \([7k+5,11k+7]\) |
| 2 | \([k+1,6k+5]\) | \([6k+6,11k+10]\) |
| 3 | \([k+1,6k+5]\) | \([6k+5,11k+9]\) |
| 4 | \([k+1,2k+1]\cup[2k+3,6k+5]\) | \([6k+4,11k+9]\) |
| 5 | \([2k+2,6k+4]\) | \([7k+6,11k+8]\) |

No extrapolation from numerical samples is involved: the endpoints follow by adding the finitely many affine interval endpoints, with \(q\)-element selections in one interval ranging from \(qa+q(q-1)/2\) to \(qb-q(q-1)/2\). The standalone symbolic verifier enumerates every residue-slice choice, checks all affine order and overlap comparisons **for all integers \(k\ge2\)**, and reproduces this table.

**2. The full finite initial partition.** The largest sum of three distinct elements of \(C_k\) is \(6h+4\), and the greatest relevant base endpoint is
\[
 E=11h+3=(6h+4)+m.
\]
At each residue \(r\), restrict the preceding table to the integer interval \(h<n\le E\). In this interval, the prescribed sequence contributes exactly the entries from \(C_k\), \(B_k\), and the portion of \(B_k+m\) below \(E\). These entries and \(3^{\wedge}C_k\cup P_k\) partition the entire interval without overlap: after the common lower coordinate \(u=k+1\), their successive intervals meet at consecutive integers. For instance, at residue \(0\) these intervals, alternating between admitted and forbidden, are
\[
 \begin{aligned}
 &[k+1,2k+1],\ [2k+2,6k+4],\ [6k+5,7k+5],\\
 &[7k+6,11k+8],\ \{11k+9\};
 \end{aligned}
\]
for residue \(1\) they are \([k+1,2k+1]\), \([2k+2,6k+3]\), \([6k+4,7k+4]\), \([7k+5,11k+7]\), \([11k+8,11k+9]\); residue \(2\) and residue \(3\) consist entirely of forbidden entries; at residue \(4\) only \(u=2k+2\) is admitted; residue \(5\) has the same alternating pattern as residue \(0\), without its final admitted singleton. The symbolic verifier checks all six partitions exactly for the whole parameter range.

Hence every excluded \(n\) with \(h<n\le E\) is a sum of three distinct prescribed entries, while no prescribed term in that interval is represented by a triple of \(C_k\), or by two elements of \(C_k\) plus one from \(B_k\).

**3. No periodic term becomes a forbidden triple.** Work modulo \(m\) and retain the residue slices \(R=B_k\bmod m\). For each target residue \(r\in\{0,1,5\}\), its permitted \(u\)-coordinates lie in \([k+1,2k+1]\) when \(r=0,5\), or \([k,2k]\) when \(r=1\). Exact interval calculations for the three types of prospective triple with at least one periodic summand yield:

| triple type | \(u\)-interval at \(r=0\) | at \(r=1\) | at \(r=5\) |
|---|---|---|---|
| \(2^{\wedge}C_k+R\) | \([2k+2,6k+4]\) | \([2k+1,6k+3]\) | \([2k+2,6k+4]\) |
| \(C_k+R+R\) | \([2k+3,6k+4]\) | \([2k+2,6k+3]\) | \([2k+3,6k+4]\) |
| \(R+R+R\) | \([3k+3,6k+3]\) | \([3k+2,6k+2]\) | \([3k+3,6k+3]\) |

In the last two rows, repeated residue representatives were **allowed**, making these upper bounds stronger than necessary for exclusion. Each possible triple lies strictly above the indicated target interval \(R\), but strictly below its translate \(R+M\). Thus none is congruent modulo \(m=6M\) to any member of \(R\). Every prescribed periodic term is therefore free of triples containing at least one periodic summand. A triple entirely from \(C_k\) is at most \(6h+4\); beyond this limit it cannot reach a periodic term, and below it the finite partition in step 2 rules out collisions. The initial finite terms are likewise protected by step 2 (or by positivity for the seeds).

**4. Every remaining integer is forbidden.** Let \(T=6h+4\). By step 2, each \(T<n\le T+m=E\) not prescribed is represented by a triple, necessarily with at least one periodic term because any triple from \(C_k\) is at most \(T\). The proposed set is periodic in membership for all \(n>T\). For any larger excluded integer \(n\), \(n-m\) is also excluded and lies above \(T\). Inductively express \(n-m\) as a sum of three distinct prescribed terms containing a periodic term. Increase the **largest** periodic summand by \(m\); it remains prescribed and is larger than the other two summands, so distinctness is preserved. This yields a forbidden triple for \(n\).

Steps 2–4 show that the prescribed infinite set admits precisely those and only those entries chosen by the strict greedy rule, proving the exact formula.

**5. Least period and density.** The \(3(k+1)\) terms in each copy of \(B_k\) have successive gaps of at most \(5\), except between the last term \(7h\) and the first term of the next block \(11h-6\), where the gap is \(4h-6>5\). This uniquely largest gap occurs **once per \(m\)-block**. Therefore a shorter eventual additive period cannot exist: it would repeat that uniquely largest gap more than once inside an \(m\)-block. Since each block has \(3k+3\) terms, its density is the stated ratio.

## Verification

Run `python3 verify_symbolic.py`. It checks all five affine sumset tables, the modular noncollision inequalities, and the six base-interval partitions with affine inequalities valid for **all integer parameters \(k\ge2\)**; it does not impose a finite parameter cutoff. The exact rules for sums of distinct elements of consecutive integer intervals are the sole nontrivial reduction used by this symbolic checker.

Run `python3 verify_greedy.py`. This separate implementation constructs the greedy sequence directly with integer bitsets, compares all terms through \(12h\) for \(k=2,\ldots,400\), checks long intervals through \(100h\) for eight further parameter values, and independently enumerates distinct triples in the base interval for eleven smaller parameters. Those finite computations corroborate, but do not replace, the infinite symbolic proof.

## Relationship to prior work

Van Berkel and Bosma, *On \(t\)-sumfree sequences* (arXiv:2609.16843, first posted 15 September 2026), establish ultimate periodicity of a broad class \(S_{f,g,g+d}\) under \(g\ge\max(f+1,d-1)\), and certify many additional individual small triples. For the present family, \(f=1\), \(g=2\), \(d=h-2\), and \(2<h-3\); the stated uniform theorem is inapplicable for every \(h\ge17\). Even confirmations of individual small seeds do not imply this infinite formula or its least period.

Shtrezi, *The greedy 3-sumfree sequence \(S_{1,g,g+1}\)* (arXiv:2606.17447, first posted 13 June 2026), proves another infinite seed family. It intersects the present line only at \(g=2,h=3\), which is outside the claimed range. Earlier OEIS examples such as A026471 concern that different seed. Published findings on **two**-sumfree sequences involve a different forbidden sum length and likewise do not imply this three-sumfree result.

## Limitations

The explicit description concerns only initial triples \((1,2,6k+5)\) with \(k\ge2\), not all three-sumfree sequences or the global periodicity conjecture. An exhaustive priority search of all historical or unpublished results is impossible; some sections of the most directly relevant primary preprint were not fully accessible in this review, so historical priority remains qualified. The independent finite-program stress tests are not proofs of infinitely many parameter cases; the proof is the stated affine-interval argument and its exact symbolic verification.

## References

1. D. van Berkel and W. Bosma, *On \(t\)-sumfree sequences*, arXiv:2609.16843v1 (15 September 2026), https://arxiv.org/abs/2609.16843 . Primary MSC 11B50.
2. O. Shtrezi, *The greedy 3-sumfree sequence \(S_{1,g,g+1}\)*, arXiv:2606.17447v1 (13 June 2026), https://arxiv.org/abs/2606.17447 .
3. OEIS A026471, the strict greedy 3-sumfree sequence with initial entries \((1,2,3)\), https://oeis.org/A026471 .
4. D. van Berkel and W. Bosma, *Periodicity conjectures for all 2-sumfree sequences*, arXiv:2609.18522 (16 September 2026), https://arxiv.org/abs/2609.18522 .
