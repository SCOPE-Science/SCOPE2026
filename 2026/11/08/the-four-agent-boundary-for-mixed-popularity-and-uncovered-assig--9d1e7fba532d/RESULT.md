# The four-agent boundary for mixed popularity and uncovered assignment refinements

## Finding
In complete strict one-sided house assignment with the same number of agents and houses, the support of every mixed-popular lottery belongs to each of the Bordes, Gillies, and McKelvey uncovered sets whenever there are at most three agents. With four agents, **every** mixed-popular lottery still has support in the McKelvey uncovered set, but separate four-agent profiles admit mixed-popular lotteries assigning positive probability to Bordes-covered and Gillies-covered assignments. Consequently four is the sharp first size for failure of the Bordes and Gillies support inclusions. The question of McKelvey support inclusion for five or more agents is not resolved here.

## Assumptions and scope
Let \(n\in\{2,3,4\}\), let \(N=\{1,\ldots,n\}\), and let \(H\) be an \(n\)-element house set. Every agent has a complete strict order on \(H\). An assignment \(a\) is a bijection from agents to houses, and \(\mathcal A\) is the set of all \(n!\) assignments. For assignments \(a,b\), define their integer majority margin
\[
M_{ab}=\sum_{i\in N}\left(\mathbf1\{a(i)\succ_i b(i)\}-\mathbf1\{b(i)\succ_i a(i)\}\right).
\]
Thus \(M\) is skew-symmetric, with ties contributing zero. A lottery \(p\) on \(\mathcal A\) is **mixed popular** when \(p_a\ge0\), \(\sum_a p_a=1\), and \(\sum_a p_aM_{ab}\ge0\) for every deterministic assignment \(b\), equivalently \(Mp\le0\). (Testing all deterministic \(b\) is equivalent to testing all lotteries.)

An assignment \(c\) **Bordes-covers** \(b\) when \(M_{cb}>0\) and for every assignment \(d\), \(M_{bd}>0\) implies \(M_{cd}>0\). It **Gillies-covers** \(b\) when \(M_{cb}>0\) and for every \(d\), \(M_{dc}>0\) implies \(M_{db}>0\). It **McKelvey-covers** \(b\) when both conditions hold. In each case the uncovered set consists of assignments with no such covering predecessor. These strict-majority definitions apply even when the number of voters is even and some margins vanish. With a single agent, there is only one assignment, so every covering relation is empty and the claimed support inclusion holds trivially.

## Proof
**Finite rational certificate for the universal claims.** Fix \(n\) and a profile. For one of the three covering variants, write \(c\in\{0,1\}^{n!}\) for the indicator of covered assignments. It suffices to exhibit a coordinatewise nonnegative rational vector \(y\) such that
\[
\sum_a y_aM_{ab}\ge c_b\qquad\text{for every assignment }b.
\]
Indeed, if \(p\) is mixed popular, nonnegativity of \(p\) gives
\[
0\le \sum_b c_bp_b\le y^{\mathsf T}Mp=-p^{\mathsf T}My\le0.
\]
Hence every covered assignment has lottery mass zero. For every possible strict profile with \(n=2,3\), the accompanying compressed data provide such a nonnegative rational \(y\) for all three covering variants. They also provide such a \(y\) for the McKelvey variant for every profile with \(n=4\). The accompanying exact-arithmetic verifier independently builds \(M\), constructs covering relations from the definitions, and verifies every coordinate of each rational inequality; it does not trust the certificates' stated profile counts or use a floating-point optimization engine.

For completeness of the profile search, any house relabeling preserves majority margins, covering, and mixed popularity. We may therefore fix agent one's order as \((0,1,\ldots,n-1)\). Every other agent's order ranges independently over all \(n!\) permutations, for \((n!)^{n-1}\) normalized profiles: precisely \(2\), \(36\), and \(13{,}824\) profiles for the respective market sizes. The verifier exhausts these profiles. This proves all universal statements above, rather than extrapolating from sampled experiments.

**Four-agent failure of Bordes inclusion.** Label the houses \(0,1,2,3\), and specify each agent's ranking from best to worst by
\[
(0,1,2,3),\ (0,1,2,3),\ (0,1,3,2),\ (1,2,0,3).
\]
Assign equal lottery probability to the assignments (written as the ordered vector of houses received by agents)
\[
(0,2,3,1)\qquad\text{and}\qquad(2,0,1,3).
\]
The second assignment is Bordes-covered by \((1,0,3,2)\), yet receives lottery mass \(1/2\). Exact comparison against every one of the \(24\) deterministic assignments gives nonnegative majority-margin expectation. More specifically, multiplying all expectations by \(2\) gives the multiset of margins with multiplicities \(0:14,\ 2:8,\ 4:2\). Thus the displayed lottery is mixed popular, establishing the first failure.

**Four-agent failure of Gillies inclusion.** Take the rankings
\[
(0,1,2,3),\ (0,1,2,3),\ (0,2,1,3),\ (1,0,3,2).
\]
Assign uniform probability to the three assignments
\[
(0,2,3,1),\qquad(2,3,0,1),\qquad(3,0,2,1).
\]
Here \((0,1,2,3)\) Gillies-covers the first assignment, which nevertheless has mass \(1/3\). Multiplying its majority-margin expectations against all \(24\) assignments by \(3\) gives the nonnegative multiset \(0:10,\ 2:6,\ 4:6,\ 6:2\). Consequently the lottery is mixed popular. In both examples the covered positive-mass assignment is McKelvey-uncovered, consistent with the four-agent universal statement. Failure cannot occur earlier by the rational certificates, establishing sharpness.

## Verification
Run `python3 verify.py` from a directory containing `verify.py` and `cover_dual_certificates.json.gz`. Both files are included as standalone artifacts. The verifier uses only the Python standard library, rational certificates with integer numerators and denominators, and integer majority margins. It checks \(2\) normalized two-agent profiles for each variant, \(36\) normalized three-agent profiles for each variant, and \(13{,}824\) normalized four-agent profiles for McKelvey. Every certificate is checked coordinatewise against all \(n!\) assignment alternatives; the two four-agent counterexample lotteries are checked against all \(24\) opponents and their asserted covering witnesses. Its final output is `ALL EXACT CHECKS PASS`. Normalized enumeration represents all profiles by house-relabeling symmetry.

## Relationship to prior work
Brandt, Chen, Dong, Lederer and Schlenga (2026) develop majority-based assignment rules and explicitly pose whether the support of mixed-popular assignment lotteries is in the uncovered set. The present result resolves that support-inclusion question through four agents for McKelvey covering while revealing a sharp failure at four for the stronger Bordes and Gillies refinements.

Classical results on the essential set of a tournament and the McKelvey uncovered set often employ a **sign-only** majority game. These do not automatically apply to mixed popularity defined using **cardinal vote margins** \(M_{ab}\), whose magnitudes can differ for assignments. Earlier small-market stochastic-dominance results, rank-maximal assignment results, and unrestricted tournament uncovered-set computations also do not imply the stated exact lottery-support conclusions.

## Limitations
This is a finite, fully enumerated theorem for at most four agents, not an all-population answer; no assertion is made for the McKelvey case with five or more agents. The two uncovered-set refinement counterexamples do not imply that every mixed-popular lottery violates inclusion, only that some do. The mathematical proof relies on replayable finite integer certificates rather than a short classification of all possible preference configurations. Publication priority may be affected by unindexed earlier results or broader theorems not found in the accessible literature. Independent scientific audit has not been performed.

## References
1. F. Brandt, J. Chen, Y. Dong, P. Lederer and J. Schlenga, *Majoritarian Assignment Rules*, arXiv:2602.14816v1 (first public February 16, 2026), https://arxiv.org/abs/2602.14816.
2. J. Duggan, *Uncovered Sets*, working-paper exposition (2011), https://www.wallis.rochester.edu/assets/pdf/WallisPapers/wallis_63.pdf. See the distinctions between uncovered refinements, the essential set, and payoff conventions.
3. T. Kavitha, J. Mestre, M. Nasre, *Popular Mixed Matchings*, 2011 (referenced in Brandt et al.).
