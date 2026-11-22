# Sharp scattered-triple spectra inside binary Parikh-matrix classes

## Finding

For any integers \(a,b\geq1\) and \(0\leq t\leq ab\), let \(\mathcal F_{a,b,t}\) be the set of binary words with exactly \(a\) zeros, \(b\) ones, and \(t\) positional scattered occurrences of `01`. Let \(T(w)\) count positional scattered occurrences of `010`. Write
\[
t=bq+r,\quad 0\leq r<b;\qquad t=ak+s,\quad0\leq s<a.
\]
Then the **exact endpoints** of the scattered-triple spectrum within the entire class are
\[
\boxed{\min_{w\in\mathcal F_{a,b,t}}T(w)=s(a-s),}
\qquad
\boxed{\max_{w\in\mathcal F_{a,b,t}}T(w)=at-(b-r)q^2-r(q+1)^2.}
\tag{1}
\]
Each endpoint has exactly one attaining word, even when the endpoints coincide. More strongly, the full joint distribution before fixing \(b,t\) is the coefficient-wise identity
\[
\boxed{\sum_{\substack{w\in\{0,1\}^*\\|w|_0=a}}
 u^{|w|_1}z^{\binom{w}{01}}v^{\binom{w}{010}}
 =\prod_{j=0}^{a}\frac1{1-uz^jv^{j(a-j)}}.}
\tag{2}
\]
Here the coefficients of \(u^b z^t v^h\) count exactly the words with \(T(w)=h\). In particular, every member of a fixed class satisfies the parity constraint
\[
T(w)\equiv(a-1)t\pmod 2.
\tag{3}
\]
For \(a=2h\), \(b=2k\), and \(t=ab/2\), the two extreme values are \(0\) and \(bh^2\), respectively. Thus the same complete two-binomial data can conceal arbitrarily large differences in the `010` three-subsequence count.

## Assumptions and scope

All words are finite, linear and over \(\{0,1\}\). The notation \(\binom{w}{p}\) counts distinct **position selections** forming pattern \(p\), not merely distinct pattern strings and not contiguous-factor occurrences. The parameters \(a,b\) are positive and \(t\) ranges over every integer from \(0\) through \(ab\); every such fiber is nonempty. Quotients and remainders in (1) are the ordinary Euclidean quotients. Equation (2) is interpreted as a formal series in \(u\) whose coefficients are polynomials in \(z,v\); no analytic convergence is needed. A fiber fixes the complete binary two-binomial/Parikh-matrix data. The uniqueness assertion refers to literal words, not equivalence under reversal or complementation.

## Proof

**1. Gap bijection and the exact series.** Every word with exactly \(a\) zeros has a unique expression
\[
w=1^{m_0}0\,1^{m_1}0\cdots0\,1^{m_{a-1}}0\,1^{m_a},\qquad m_j\geq0.
\]
A one in gap \(j\) has exactly \(j\) zeros before it and \(a-j\) after it. Counting occurrences by their selected one therefore gives
\[
|w|_1=\sum_{j=0}^{a}m_j,\quad
\binom{w}{01}=\sum_{j=0}^{a}jm_j,\quad
T(w)=\sum_{j=0}^{a}j(a-j)m_j.
\tag{4}
\]
The gap multiplicities vary independently over all nonnegative integers. Taking the ordinary geometric series for each gap proves (2), with exactly one contribution per word.

**2. A bounded-partition formulation.** List the number of preceding zeros for each one, in source order, as the nondecreasing sequence
\[
0\leq x_1\leq\cdots\leq x_b\leq a.
\]
Conversely every such sequence determines exactly one word by the gap encoding. The fixed two-binomial condition is \(\sum_{i=1}^{b}x_i=t\). Moreover
\[
T(w)=\sum_i x_i(a-x_i)=at-\sum_i x_i^2.
\tag{5}
\]
This simultaneously proves nonemptiness of all fibers: writing \(t=ak+s\), one may take \(k\) parts equal to \(a\), one additional part \(s\) if \(s>0\), and all others zero.

**3. Unique maximum of the triple count.** To minimize \(\sum_i x_i^2\), suppose two entries differ by at least two. Increasing the smaller by one and decreasing the larger by one preserves their total and the bounds, but strictly decreases the squared sum by \(2(x_{\rm large}-x_{\rm small}-1)>0\). Sorting the modified entries changes neither constraint nor objective. Iterating forces all values to differ by at most one; the sum then uniquely determines the multiset as \(b-r\) copies of \(q\) and \(r\) copies of \(q+1\). Conversely no balancing move is possible in that configuration, which is the unique minimizer by the strict improvement argument. Equation (5) gives the right-hand bound of (1), uniquely attained by its one nondecreasing sequence.

**4. Unique minimum of the triple count.** To maximize the squared sum, suppose two entries are strictly between the two extremes in the following sense: a smaller entry is positive and a larger entry is less than \(a\). Transfer one unit from the smaller to the larger. The sum of squares strictly increases by \(2(x_{\rm larger}-x_{\rm smaller}+1)>0\). Thus a maximizing multiset has at most one part strictly between \(0\) and \(a\), and all other parts belong to \(\{0,a\}\). The prescribed sum \(t=ak+s\) forces exactly \(k\) entries equal to \(a\), one entry equal to \(s\) if nonzero, and all remaining entries zero. This configuration is attainable and uniquely determined; it is the global maximum of the squared sum by repeatedly transferring mass to an extreme. Substituting in (5) yields \(T=s(a-s)\), proving the left-hand bound of (1) and the unique attaining word. The proof covers both remainder-zero and boundary fibers without requiring special exceptions.

**5. Parity and separation.** Since \(x_i^2\equiv x_i\pmod2\), (5) gives (3). Under the parameters stated after (3), the remainder of \(t\) upon division by \(a\) is zero, so the minimum is zero. The balanced multiset comprises \(b\) entries \(h\), so its triple count is \(b h(2h-h)=bh^2\). As \(h\) or \(b\) grows, the gap grows without bound while \(a,b,t\) and hence all subsequence counts of length at most two remain fixed within each pair of extremal words.

## Verification

Two standalone Python 3 programs use only the standard library. Run `python3 check_words.py` to directly enumerate positional `01` pairs and `010` triples in all fixed-composition binary words with \(1\leq a,b\leq7\). It checks every attainable fiber, both exact endpoints, the **unique** realization of each endpoint and the parity constraint: 12,854 literal words and 833 fibers. Run `python3 check_partition.py` for an independent coefficient calculation of (2) against nondecreasing-partition enumeration through \(1\leq a,b\leq10\): 100 parameter pairs and 3,125 fibers; it also checks the Gaussian-binomial normalization and uniqueness of both endpoint coefficients. Recorded outputs are `check_words_output.txt` and `check_partition_output.txt`. These are finite checks supporting the all-parameter proof, not a substitute for it.

For example, with \(a=b=4\) and \(t=8\), equation (1) gives spectrum endpoints \(0\) and \(16\), while the full attainable set is \(\{0,6,8,10,12,14,16\}\); this illustrates that the parity law is necessary but not a no-holes claim.

## Relationship to prior work

Fazekas, Huang and Mercaş (2026) study the same binary Parikh-matrix classes and characterize subsequence universality with existential and universal quantifiers, plus an additive approximation scheme for the probability that a designated subsequence occurs. Their available abstract does not state the exact *multiplicity* spectrum of `010`, its joint weighted generating series, or the sharp all-fiber endpoint formulas. The full paper was unavailable for inspection; a specialized result in its body remains a priority risk.

Richomme (2025) establishes a partition-lattice representation of binary two-binomial equivalence classes (in particular, Lemma 4.12), which is a classical representation used in the proof above rather than a novel contribution. Its inspected Sections 4–5 discuss the class lattice and fair-word/least-squares properties, not exact `010` frequency extremizers or the extra quadratic weight in (2). The least-squares problem there fits a straight line to bit positions, and is not the extremization of (5).

Three other directly relevant exact results were inspected: an internal-span distribution for binary Parikh classes that determines existence of `0 1^t 0` patterns but not their positional counts; an unconditional fixed-frequency distribution for `010` over **all** length-\(n\) words; and a maximum `010` count given fixed letter composition and **run number**. The present theorem instead keeps \(\binom{w}{01}\) fixed and resolves the complete joint weighted distribution and both uniquely realized endpoints. Marginalization of (2) in \(z\) recovers known unconditional distributions, but a marginal alone does not recover its refined coefficients. The partition encoding and strict-convexity moves are classical; no novelty is claimed for those tools by themselves.

## Limitations

The exact formulas concern the scattered triple `010` (and, by bit complementation, `101`) in binary two-binomial classes. They do not classify every *attainable* intermediate count by a short elementary rule, solve full three-binomial reconstruction, or extend the endpoint formulas to arbitrary patterns/alphabet sizes. Standard convexity makes the endpoint proof short; the mathematical contribution assessed is the motivated exact classwise weighted distribution and complete sharp classification rather than a new optimization technique. Priorities versus unindexed papers and the uninspected full text of the 2026 motivating paper remain uncertain. Self-review is not independent mathematical validation.

## References

1. Sz. Zs. Fazekas, X. Huang, R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717 (first public October 5, 2026), https://arxiv.org/abs/2610.06717.
2. G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159 (first public October 8, 2025), https://arxiv.org/abs/2510.07159.
3. *Exact sandwich-subsequence profiles within binary Parikh-matrix classes*, publicly available result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-sandwich-subsequence-profiles-within-binary-parikh-matrix--b40371a80999.
4. *Quadratic-gap partition law and sharp stabilization for scattered 010 occurrences*, publicly available result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-quadratic-gap-partition-law-and-sharp-stabilization-for-scattere--02da9ce01629.
5. *Sharp cubic run penalties for scattered alternating triples in binary words*, publicly available result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-cubic-run-penalties-for-scattered-alternating-triples-in-b--07237c25ca80.
