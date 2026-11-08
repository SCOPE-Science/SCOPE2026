# Exact Abelian-power phase spectra for distinct-run periodic words

## Finding

Fix an integer \(q\ge3\), distinct letters \(c_0,\ldots,c_{q-1}\), and positive run lengths \(a_0,\ldots,a_{q-1}\). Put
\[
P=c_0^{a_0}c_1^{a_1}\cdots c_{q-1}^{a_{q-1}},\qquad L=\sum_{i=0}^{q-1}a_i,\qquad X=P^\omega.
\]
For integers \(p\ge1\) and \(e\ge2\), call a phase \(s\in\{0,\ldots,L-1\}\) *qualifying* when the length-\(ep\) factor of \(X\) starting at \(s\) splits into \(e\) consecutive blocks of length \(p\) having identical Parikh vectors. Let \(N(p,e)\) count these phases and let \(D(p,e)\) count distinct length-\(ep\) words thereby obtained (not distinct decompositions or phases).

Write \(r=p\bmod L\), with \(0\le r<L\); for \(r>0\), let \(t=\min\{r,L-r\}\). Then, simultaneously for every choice of the parameters,
\[
N(p,e)=\begin{cases}
L,&r=0,\\
\displaystyle\sum_{i=0}^{q-1}\max\{0,a_i-et+1\},&1\le r<L,
\end{cases}
\qquad
D(p,e)=\begin{cases}
\displaystyle\sum_{i=0}^{q-1}\mathbf1_{\{a_i\ge ep\}},&ep<L,\\
N(p,e),&ep\ge L.
\end{cases}
\]
The formula comes with an exact *phase classification*. If \(0<r\le L/2\), phase \(s\) qualifies if and only if the \(er\) consecutive symbols beginning at \(s\) are all one letter. If \(L/2<r<L\), the condition instead is that the \(e(L-r)\) consecutive symbols ending immediately before \(s\) are all one letter. All positions are interpreted modulo \(L\).

Consequently, for \(r>0\), an Abelian \(e\)-power of period \(p\) exists if and only if \(e\min(r,L-r)\le\max_i a_i\). Its exact phase count and its exact distinct-factor count depend only on the multiset of run lengths, not their cyclic ordering. These are *fixed-period* statements; arbitrary-length existence follows by applying the formulas separately at each period.

## Assumptions and scope

A factor is contiguous, not scattered. A Parikh vector lists the count of each letter in a finite word. An Abelian \(e\)-power is a concatenation of \(e\) equal-length blocks with equal Parikh vectors; the blocks need not be identical strings. The host is right-infinite and purely periodic, but a starting phase is always reduced modulo its primitive period \(L\). The letters in different runs are **pairwise distinct**, each appears in just one contiguous run per period, and \(q\ge3\). These hypotheses are essential: the binary word \((0^2 1^2)^\omega\) has Abelian squares of block length \(2\) at two phases although the displayed nonzero-residue formula would return zero.

## Proof

**Adjacent-arc rigidity lemma.** Partition a circle of length \(L\), carrying exactly one nonempty contiguous run of each of at least three different letters, into two consecutive arcs \(A,B\) of a common length \(t\), with \(2t\le L\), and possibly a complementary arc \(C\). If \(A\) and \(B\) have equal Parikh vectors, they are both monochromatic, in the same letter.

Indeed, every letter appearing in \(A\) also appears in \(B\). Its unique circular run must therefore cross either the common boundary between \(A\) and \(B\), or the other way around the circle across \(C\); the latter is possible only when the run covers all of \(C\). At most one letter's run can cross the common boundary, and at most one different letter's run can cover all of \(C\). If both types were present, every point of \(A\cup B\) would belong to one of those two letters, because a third letter would have to appear in both arcs without either of these two crossing options. Every point of \(C\), if any, would belong to the outer-crossing letter. That would exclude a required third positive run, a contradiction. Thus only one letter appears in \(A\cup B\), proving the lemma (including the case of empty \(C\)).

**Period reduction.** Any factor of length \(p=mL+r\), where \(0\le r<L\), consists, in terms of letter counts, of \(m\) complete circular periods plus a residual arc of length \(r\). Therefore \(e\) consecutive length-\(p\) blocks have equal Parikh vectors precisely when their \(e\) residual arcs do. The residual arcs begin at phases \(s+jr\pmod L\), for \(j=0,\ldots,e-1\). If \(r=0\), all phases qualify.

**Short residual arcs.** Suppose \(0<r\le L/2\). The residual arcs are consecutive length-\(r\) arcs modulo \(L\). Apply the rigidity lemma to each consecutive pair. Their Parikh vectors are all equal exactly when the first \(er\) symbols from phase \(s\) form a monochromatic circular interval. This conclusion remains valid if that interval wraps several times around the circle: such an interval cannot be monochromatic when it exceeds the length of the unique run of its letter.

**Long residual arcs.** Suppose \(L/2<r<L\) and set \(t=L-r\). The complement, within a complete period, of the residual arc starting at \(s+jr\) is the length-\(t\) arc beginning at \(s-(j+1)t\). Equal residual Parikh vectors are equivalent to equal complementary-arc Parikh vectors, since each full circular period has the same counts. The \(e\) complementary arcs form a consecutive chain, in reverse order, from \(s-et\) to \(s\). The rigidity lemma therefore makes equality equivalent to a homogeneous interval of length \(et\) ending at phase \(s\).

**Phase enumeration.** A homogeneous interval of positive length \(et\) can be contained in the run of letter \(c_i\) at exactly \(\max\{0,a_i-et+1\}\) circular starting positions. These sets are disjoint across distinct letters. Summing proves the formula for \(N(p,e)\) and the existence criterion. The count depends only on the run-length multiset.

**Distinct-factor enumeration.** The period \(P\) is primitive: its unique circular run of each distinct letter rules out a smaller positive period. Hence any factors of \(X\) of length at least \(L\), starting at different phases modulo \(L\), are distinct. When \(ep\ge L\), distinct qualifying phases thus count distinct Abelian-power factors. If \(ep<L\), then \(p<L\) and any qualifying factor is monochromatic by the phase characterization; it appears as a distinct string if and only if some run has length at least \(ep\), once per qualifying letter. This proves the formula for \(D(p,e)\).

## Verification

Run `python3 verify.py` with Python's standard library. Its independent direct scan enumerates all period phases, partitions each length-\(ep\) factor, calculates Parikh vectors independently, and compares the resulting complete phase set, phase count, and distinct-factor count with both formulas and the phase characterization. It passed **74,112 exhaustive configurations** with \(q\in\{3,4,5\}\), every run length from \(1\) to \(4\), periods from \(1\) to \(L+2\), and exponents \(2,3,4,5\); it also passed **800** reproducible seeded configurations with up to eight letters, run lengths up to twelve, periods up to three periods plus seven, and exponents up to eight. It separately checks the two-letter counterexample. These finite computations only test the proof and do not establish its infinite quantifiers.

For example, take run lengths \((3,4,5)\), so \(L=12\). At \(p=2,e=2\), the phase count is \(0+1+2=3\), but only two distinct Abelian-square factors occur because both are monochromatic and the total factor length is four. At \(p=11,e=2\), the phase count and distinct-factor count are both nine. At \(p=12\), every one of the twelve phases qualifies for any exponent at least two.

## Relationship to prior work

Peltomäki and Whiteland, *Avoiding abelian powers cyclically* (2020), study cyclic Abelian-power avoidance. Their complement argument (Lemma 2.7) relates existence at complementary periods. The present result uses a sharper one-run-per-letter rigidity, giving the exact phase sets, counts, all exponents, and distinct-factor counts for this particular family. General existence or avoidance statements do not by themselves furnish this distribution.

Fici, Mignosi, and Shallit, *Abelian-Square-Rich Words* (2017), study quantities of distinct Abelian-square factors, notably in Thue--Morse and Sturmian families, rather than the complete periodic distinct-run phase distribution here. A related prior two-letter, two-run periodic classification for exponents at least three has an extra opposite-half-residue exception and does not imply the present \(q\ge3\) result: the alphabet and rigidity hypotheses differ. Earlier formulas for Parikh-vector complexity of individual factors of distinct-run periodic words do not determine equality of Parikh vectors across consecutive blocks, so they do not settle this counting problem.

## Limitations

The result is restricted to a pure period with each symbol in exactly one run, and to at least three distinct symbols. It gives no assertion for words where a symbol returns within the period, arbitrary periodic hosts, or more general Abelian repetitions with incomplete boundary blocks. Existence for block lengths divisible by \(L\) is automatic. The originality comparison is limited to the cited inspected sources, the searched mathematical records, and accessible related claims; an unindexed equivalent or an unnoticed specialization of a general theorem remains possible. Independent scientific validation has not been performed.

## References

- G. Fici, F. Mignosi, J. Shallit, *Abelian-Square-Rich Words*, arXiv:1701.00948, first posted 2017-01-04. https://arxiv.org/abs/1701.00948
- J. Peltomäki, M. A. Whiteland, *Avoiding abelian powers cyclically*, arXiv:2006.06307, first posted 2020-06-11. https://arxiv.org/abs/2006.06307
- G. Fici et al., *Abelian powers and repetitions in Sturmian words*, Theoretical Computer Science 635 (2016), 16--34. https://doi.org/10.1016/j.tcs.2016.04.039 (comparison with an aperiodic family)
