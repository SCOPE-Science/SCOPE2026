# Poisson freezing thresholds for multicolor three-site plurality on cyclic rings

## Finding

Let a finite cyclic ring of \(n\ge3\) sites use an alphabet of \(q\ge3\) colors. At each synchronous update a site takes the most frequent of its left, own, and right colors, retaining its own color when all three are different. Write \(F\) for the global map and define the first fixation time \(T(x)=\min\{t\ge0:F^{t+1}(x)=F^t(x)\}\), with \(T(x)=\infty\) if the orbit never fixes. Then:

1. The indicator \(e_i(t)=\mathbf1\{F^{t+1}(x)_i\ne F^t(x)_i\}\) satisfies exactly, for every configuration, site and nonnegative time,
   \[e_i(t+1)=e_{i-1}(t)e_i(t)e_{i+1}(t).\]
   Equivalently, \(e_i(t)=1\) precisely when the initial cyclic word of length \(2t+3\) centered at \(i\) alternates between exactly two different colors.
2. Every orbit reaches a fixed point except the \(q(q-1)\) initially alternating configurations on even rings, which make \(q(q-1)/2\) primitive temporal two-cycles. Among orbits that do fix, the sharp worst-case fixation time is \(\lfloor(n-1)/2\rfloor\) for odd \(n\) and \((n-2)/2\) for even \(n\).
3. Let the initial colors be independent uniform colors in \(\{1,\dots,q_n\}\) with \(q_n\to\infty\), \(n\to\infty\), and fix an integer \(t\ge0\). Set
   \[\lambda_n=\frac{n(q_n-1)}{q_n^{2t+2}}.\]
   If \(\lambda_n\to\lambda\in[0,\infty)\), then the number of initially alternating cyclic windows of length \(2t+3\) converges in distribution to a Poisson random variable of mean \(\lambda\), so
   \[\Pr\{T\le t\}\longrightarrow e^{-\lambda}.\]
   If \(\lambda_n\to\infty\), the same probability tends to zero. Thus for each fixed \(t\), the critical palette size is \(q_n\asymp n^{1/(2t+1)}\): whenever \(q_n/n^{1/(2t+1)}\to c\in(0,\infty)\),
   \[\Pr\{T\le t\}\longrightarrow \exp\big(-c^{-(2t+1)}\big).\]
   In that critical window, \(T\) is asymptotically concentrated on the two values \(t\) and \(t+1\), with limiting respective probabilities \(\exp(-c^{-(2t+1)})\) and \(1-\exp(-c^{-(2t+1)})\).

## Assumptions and scope

Sites are indexed modulo \(n\), with simultaneous deterministic updates and the incumbent-preserving rule on a three-distinct-color local tie. A color is not given any preferred order. The alphabet is fixed within each system but may vary with \(n\) in the asymptotic theorem. The random initial colors are independent and exactly uniform; no distributional assertion is made for other initial laws. Fixation means entry into a true fixed point, rather than entry into any periodic orbit. Therefore \(T=\infty\) on the alternating two-cycles; the probability of this exceptional event is \((q_n-1)/q_n^{n-1}\), and it vanishes in the claimed scaling regimes.

## Proof

**Local erosion identity.** Write \(a,b,c,d,h\) for five consecutive colors at time \(s\). The center changes exactly when \(b=d\ne c\), and then it becomes \(b\). If this happens, the left neighbor switches from \(b\) to \(c\) precisely when \(a=c\), and the right neighbor switches from \(b\) to \(c\) precisely when \(h=c\); a neighbor not satisfying its condition remains \(b\). Therefore both neighbors at time \(s+1\) equal \(c\) precisely when \(a=c=h\). Thus the center changes again precisely when \(a=c=h\) and \(b=d\ne c\), which says that the center and both neighbors all changed at time \(s\). If the center did not change at time \(s\), neither can it change next: for both updated neighbors to agree on a color different from its unchanged color \(c\), they would already have had to agree on that color at time \(s\), contradicting its failure to change. This proves \(e_i(s+1)=e_{i-1}(s)e_i(s)e_{i+1}(s)\). Repeated Boolean conjunction gives
\[e_i(t)=\prod_{j=-t}^{t}e_{i+j}(0).\]
Now \(e_j(0)=1\) iff the original letters at \(j-1,j,j+1\) are alternating. Conjunction over consecutive \(j\) is equivalent to an alternating cyclic word of length \(2t+3\). This argument remains valid if the word wraps around the ring.

**Complete recurrent classification and sharp clocks.** Flipping sites can never be created; their set undergoes erosion by one site on both sides each update. An arbitrarily long alternating cyclic window forces the entire ring to alternate two colors, which is possible only for even \(n\). In that case the whole configuration interchanges the two colors every update, and there are exactly \(q(q-1)\) such labeled states. Otherwise some finite \(t\) has no flippers and the system is fixed. For odd \(n\), no alternating window of length \(n+2\) exists, which yields fixation by \(\lfloor(n-1)/2\rfloor\); for even \(n\), an alternating window of length \(n+1\) forces the exceptional global checkerboard, so every other orbit fixes by \((n-2)/2\). These bounds are attained, respectively, by a length-\(n\) alternating cyclic word on an odd ring, and by an alternating run of length \(n-1\) followed by a third color on an even ring. An alternating window of length \(2t+3\) exists exactly up to one update before the asserted maximum.

**Rare alternating defects and critical scaling.** Fix \(t\) and put \(L=2t+3\). Let \(I_j\) indicate that the length-\(L\) cyclic window starting at \(j\) alternates two distinct colors. It is specified by a first color and a distinct second color, so
\[p=\Pr(I_j=1)=\frac{q(q-1)}{q^L}=\frac{q-1}{q^{L-1}},\qquad\mathbb E\big[\sum_j I_j\big]=np=\lambda_n.\]
For \(n>2L\), two windows displaced by \(1\le s\le L-2\) overlap on at least two sites; both must use the same alternating pair and \(\Pr(I_j=I_{j+s}=1)=p q^{-s}\). Windows sharing only one site are independent (the color of that shared site does not change either window's success probability), as are disjoint windows. Consequently \(\operatorname{Var}(\sum_j I_j)\le\lambda_n+C_L\lambda_n/q\) for an absolute constant depending only on \(L\), and the probability of zero windows tends to zero if \(\lambda_n\to\infty\) by Chebyshev. If \(\lambda_n\to0\), the union bound proves the zero-window probability tends to one.

When \(\lambda_n\to\lambda\in(0,\infty)\), divide the ring into consecutive blocks of length \(b_n=\lfloor\sqrt n\rfloor\), discarding possible alternating-window starts near block boundaries. The expected number of discarded windows is \(O(\lambda_n L/b_n)=o(1)\). The remaining window-hit events belonging to distinct blocks depend on disjoint sets of initial colors and hence are independent. A block contains at most one hit except with probability bounded by \(O(b_n^2p^2+b_np/q)\), by the just-computed pairwise overlaps. Summing over all blocks, the probability of any multiple-hit block is \(O(nb_np^2+\lambda_n/q)=o(1)\). Each block has hit probability \(O(b_np)=o(1)\), and the sum of these probabilities tends to \(\lambda\). The elementary law of small numbers therefore gives a Poisson\((\lambda)\) limit for total window hits. The same conclusion for \(\lambda=0\) follows from the union bound. As \(T\le t\) iff there are no such windows, its stated limit follows.

If \(q_n\sim c n^{1/(2t+1)}\), then \(\lambda_n\to c^{-(2t+1)}\). At the previous deadline \(t-1\), when \(t\ge1\), the expected window count diverges, so \(\Pr(T\le t-1)\to0\). At deadline \(t+1\), its expected window count tends to zero, so \(\Pr(T\le t+1)\to1\). For \(t=0\), \(T\ge0\) for all finite fixation times and the same upper concentration applies. This establishes the two-point clock law.

## Verification

The standalone `verify.py` enumerates all \(q^n\) initial states for \(q\in\{2,3,4\}\) and \(3\le n\le8\), checking the erosion identity across multiple steps, the exact alternating-window characterization, the complete recurrent-state classification, and sharp fixation cutoffs. A separate test checks the one-step erosion relation on every one of the \(5^7=78{,}125\) length-seven, five-color input words. All cases passed; `CHECKS.txt` contains the actual outputs. The analytic proof, not the finite checks, establishes the unbounded and stochastic claims.

## Relationship to prior work

Classical radius-one majority studies use a binary alphabet; the known binary alternating-run clock has a Poisson extreme-value window when the *time* grows logarithmically with ring length. The present claim instead concerns incumbent-tie plurality with an unbounded alphabet and exhibits an infinite hierarchy of *palette-size* thresholds at each fixed update time. The distinction is not merely a color-name replacement: a third local color enables genuine three-way ties, and the probability of two-color alternating defects depends on \(q\). Nakar and Ron address synchronous binary majority configurations, and Kaaser, Mallmann-Trenn and Natale address binary graph majority convergence. Lemoy, Mozeika and Seki study binary majority under thermal noise, a different stochastic mechanism. Publicly indexed binary ring entry-time results give no explicit moving-alphabet limit. These comparisons do not establish absolute historical novelty.

## Limitations

The statement is for exactly three sites per local vote, deterministic synchronous updates and incumbent retention in a three-way tie. The uniform random initial law is essential to the displayed critical constant. The Poisson statement assumes \(q_n\to\infty\), not fixed alphabets; fixed alphabet windows exhibit nonvanishing cluster effects. No rate of convergence is asserted outside the fixed-time limits. No independent external audit or definitive historical-priority certification has been performed.

## References

- R. Lemoy, A. Mozeika and S. Seki, *Transfer matrix analysis of one-dimensional majority cellular automata with thermal noise*, arXiv:1311.4388, initially public 18 November 2013. https://arxiv.org/abs/1311.4388
- D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519, initially public 14 August 2015. https://arxiv.org/pdf/1508.03519
- Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, arXiv:2205.08972, initially public 18 May 2022. https://arxiv.org/pdf/2205.08972
