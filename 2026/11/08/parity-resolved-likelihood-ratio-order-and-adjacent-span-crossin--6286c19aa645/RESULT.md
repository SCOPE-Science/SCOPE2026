# Parity-resolved likelihood-ratio order and adjacent-span crossing for random chord degrees

## Finding

In a uniformly random chord diagram with \(n\ge3\) chords, condition on the distinguished chord containing endpoint \(1\) having \(a\) endpoints on its shorter open circular arc, where \(0\le a\le n-1\). Let \(K_{n,a}\) count other chords crossing the distinguished chord. Then the following exact assertions hold.

1. For \(b=2n-2-a\), its full probability law is
   \[
   p_{n,a}(k):=\Pr(K_{n,a}=k)=
   \frac{\binom{a}{k}\binom{b}{k}k!\,(a-k-1)!!\,(b-k-1)!!}{(2n-3)!!},
   \]
   where \(0\le k\le a\), \(k\equiv a\pmod2\); other probabilities vanish, and \((-1)!!=1\).
2. For every \(0\le a\le n-3\), the distribution at span \(a+2\) strictly dominates that at span \(a\) in likelihood-ratio order (and hence strictly in the usual stochastic order). On their common support,
   \[
   \frac{p_{n,a+2}(k)}{p_{n,a}(k)}=
   \frac{(a+1)(a+2)}{b(b-1)}\frac{b-k}{a+2-k},
   \]
   which increases with \(k\), and the larger-span distribution additionally assigns positive mass to \(k=a+2\).
3. For every \(1\le a\le n-2\), the distributions at the **adjacent** spans \(a\) and \(a+1\) are incomparable in ordinary first-order stochastic order. The lone initial boundary is \(K_{n,0}=0\) and \(K_{n,1}=1\) almost surely.

Thus conditioning on increasing chord length produces two strict likelihood-ratio chains, one per parity, but the distributions across each adjacent pair of positive spans cross. This happens despite the strictly increasing conditional means
\[
\mathbb E K_{n,a}=\frac{a(2n-2-a)}{2n-3}\qquad (0\le a\le n-1).
\]

## Assumptions and scope

A chord diagram is a uniformly chosen perfect matching on \(2n\) labeled endpoints in cyclic order. Two chords cross precisely when their endpoints alternate. Fixing a distinguished chord is equivalent by cyclic symmetry to conditioning that endpoint \(1\) is paired to endpoint \(a+2\), with \(a\le n-1\). Its two remaining endpoint blocks have sizes \(a\) and \(b=2n-2-a\); the other \(2n-2\) endpoints form a uniform perfect matching. The event that a marked chord has shorter-arc length \(a\) gives the same conditional crossing law by reflection symmetry. Stochastic order means nonnegative comparison of all upper-tail probabilities; likelihood-ratio order means nondecreasing larger-to-smaller probability ratio across the ordered union of supports (allowing a larger top endpoint).

## Proof

**Exact matching count.** If exactly \(k\) chords cross the distinguished chord, choose \(k\) endpoints from its smaller block and \(k\) from the larger block, then pair these chosen endpoints bijectively in \(k!\) ways. The remaining \(a-k\) and \(b-k\) endpoints must be paired internally within their respective blocks, possible if and only if \(a-k\) and \(b-k\) are even, in \((a-k-1)!!(b-k-1)!!\) ways. There are \((2n-3)!!\) equally likely remaining matchings, giving the stated law with its exact support. Also, each potential cross-block pair is present with probability \(1/(2n-3)\); summing over \(ab\) possibilities proves the mean formula. The mean difference between consecutive lengths is \((b-a-1)/(2n-3)>0\) for \(a\le n-2\).

**The same-parity comparison.** Let \(0\le a\le n-3\), so \(b=2n-2-a>a+2\). The probabilities for lengths \(a\) and \(a+2\) have common values of \(k\) congruent to \(a\) modulo \(2\), from the minimum up to \(a\). Canceling the factorial form of the mass formula gives the exact ratio above. As \(k\) increases, \((b-k)/(a+2-k)\) increases strictly because its derivative is \((b-a-2)/(a+2-k)^2>0\). The larger-span law has one additional positive atom at \(a+2\), which extends the likelihood ratio to \(+\infty\). Thus its likelihood ratio is nondecreasing on the union of supports, with strict inequality in stochastic order (for instance at threshold \(a+1\)). Repeating the comparison proves the two parity-restricted chains.

**Adjacent-span incomparability.** Suppose \(1\le a\le n-2\). The larger-span variable takes the value \(a+1\) with positive probability, whereas the smaller-span variable never exceeds \(a\). Consequently at threshold \(a+1\) the larger span has strictly greater upper-tail probability. For the reverse inequality at a lower threshold there are two cases. If \(a\) is odd, the smaller-span variable is at least \(1\) surely, whereas the even span \(a+1\) has \(p_{n,a+1}(0)>0\); at threshold \(1\) the smaller-span upper tail is strictly greater. If \(a\ge2\) is even, the matching-count formula gives \(p_{n,a+1}(1)=(a+1)p_{n,a}(0)>p_{n,a}(0)>0\). The smaller-span variable has even support and the larger-span variable odd support. At threshold \(2\), their upper tails are respectively \(1-p_{n,a}(0)\) and \(1-p_{n,a+1}(1)\), so the smaller-span upper tail is strictly greater. The two opposite tail inequalities prove stochastic incomparability in every case. At \(a=0\), the two distributions are the deterministic values \(0\) and \(1\).

The smallest nontrivial example has \(n=3\): \(K_{3,1}=1\) almost surely, while \(K_{3,2}\) equals \(0\) with probability \(1/3\) and \(2\) with probability \(2/3\).

## Verification

The standalone Python 3 checker `verify.py` evaluates all probabilities with exact rational arithmetic. It independently enumerates *every* perfect matching of the remaining endpoints for \(2\le n\le7\), checks all conditional masses against direct counts, then checks normalization, expected degree, all two-step likelihood ratios and upper-tail orders, and all adjacent-span crossings for \(3\le n\le41\). One execution passed 24,290 exact assertions. The finite checks support, but do not replace, the universal counting and comparison proofs above.

Reproduce from a directory containing `verify.py` with `python3 verify.py`; no external dependencies or data files are used.

## Relationship to prior work

Acan's 2013 dissertation, Chapter 3.1, and the 7 January 2015 arXiv version of *On a uniformly random chord diagram and its intersection graph*, Section 2, examine exactly the same conditional degree-versus-length model. They establish the conditional mean and variance of the number of internally matched points and then an asymptotic degree law. The mean formula here is therefore not a novel contribution. In the inspected sections, neither source states the complete conditional crossing-degree mass formula or the parity-specific likelihood-ratio ordering and sharp adjacent-span stochastic incomparability. The last two assertions are the claim of structural interest here and require comparing entire exact laws rather than moments alone.

Acan and Pittel's *Formation of a giant component in the intersection graph of a random chord diagram* (arXiv:1406.2867, 2014) concerns globally conditioned total crossing counts and component sizes, not conditional crossing degree at a given chord span. Its global crossing-count results do not imply the above two conditional stochastic comparisons.

## Limitations

The result concerns the uniform perfect-matching model conditioned on a single distinguished chord, not arbitrary dependent chord models or a simultaneously coupled family of chord diagrams. Likelihood-ratio comparisons are claimed only for same-parity spans differing by two or more, whereas consecutive positive spans are proved incomparable. It does not classify every comparison of nonconsecutive, opposite-parity spans. Historical derivability from exact matching enumerations remains possible; the inspected earlier literature addresses the conditional model and its low-order moments. A relevant 2013 dissertation is publicly available but gives no verified exact calendar day of initial public release; the explicitly dated primary public source used for dating is arXiv:1501.01489v1 of 7 January 2015.

## References

1. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1 (7 January 2015), Section 2. https://arxiv.org/abs/1501.01489
2. H. Acan, *An Enumerative-Probabilistic Study of Chord Diagrams*, PhD dissertation, Ohio State University (2013), Chapter 3.1. https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1373310487&disposition=inline
3. H. Acan and B. Pittel, *Formation of a giant component in the intersection graph of a random chord diagram*, arXiv:1406.2867v1 (11 June 2014), Introduction. https://arxiv.org/abs/1406.2867
