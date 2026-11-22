# Exact shattering of fixed-block convex equivalence relations on finite chains

## Finding

Fix a labeled linearly ordered set \([n]=\{1,\ldots,n\}\), where \(n\ge1\), and an integer \(b\) with \(1\le b\le n\). A convex equivalence relation is one whose equivalence classes are intervals of the given order. Let \(\mathcal E_{n,b}\) be the concept family of **only** those convex equivalence relations with **exactly** \(b\) nonempty blocks, with Boolean queries \(q_{ij}\) asking whether \(i\sim j\) for \(1\le i<j\le n\).

Write \(m=n-1\) for the number of possible adjacent cut sites and \(c=b-1\) for the compulsory number of cuts. Associate \(q_{ij}\) to the nonempty integer interval of cut sites \(I_{ij}=[i,j-1]\cap\mathbb Z\subseteq[m]\). For a support \(S\) of distinct queries, write \(\mathcal I(S)=\{I_{ij}:q_{ij}\in S\}\), its union \(U(S)\), and the minimum piercing number \(\tau(S)\), meaning the smallest number of cut sites that meet every interval of \(\mathcal I(S)\). Set \(\tau(\varnothing)=0\), \(U(\varnothing)=\varnothing\). A *private site* of \(I\in\mathcal I(S)\) belongs to \(I\) but to no other member of \(\mathcal I(S)\).

**Complete support criterion.** A support \(S\) is VC-shattered by the exact-\(b\)-block concept family if and only if all three conditions hold:

1. Every member of \(\mathcal I(S)\) has a private site.
2. \(\tau(S)\le c\).
3. \(m-|U(S)|\ge c\).

**Sharp all-parameter dimension law.** For every admissible \(n,b\),
\[
\boxed{\operatorname{VCdim}(\mathcal E_{n,b})=\min\left\{2(b-1),\left\lfloor\frac{n-1}{2}\right\rfloor,n-b\right\}.}
\]
Equivalently, the dimension is \(\min\{2c,\lfloor m/2\rfloor,m-c\}\). These three bounds arise, respectively, from a limited number of compulsory cuts, from simultaneous private-site and shared-cut demands, and from leaving room for an all-positive response. All three constraints are attained simultaneously by explicit disjoint overlapping-pair gadgets and singleton intervals. The full support criterion is effective: private sites, union size, and the minimum interval piercing number can be computed by finite scans, with the latter determined greedily by increasing right endpoints.

## Assumptions and scope

The underlying order and the elements of \([n]\) are fixed and labeled. Each hypothesis has exactly \(b\) convex equivalence classes (equivalently exactly \(c=b-1\) cut sites, with no block-size constraint). Hypotheses give answer one when the queried pair lies in the same block and zero otherwise. Supports consist of distinct unordered pairs, and shattering means realizing all \(2^{|S|}\) binary traces. Empty supports are counted as shattered, also when the family is a singleton. No assertion is made for nonconvex partitions, variable block counts, additional prescribed block sizes, or adaptive shattering.

## Proof

**1. Cut-set encoding.** A convex equivalence relation with exactly \(b\) blocks corresponds bijectively to a set \(C\subseteq[m]\) of precisely \(c\) cut sites. The answer on \(q_{ij}\) is zero if and only if \(C\cap I_{ij}\ne\varnothing\). Hence shattering is equivalent to realizing every prescribed subfamily \(N\subseteq\mathcal I(S)\) as the set of support intervals hit by some \(c\)-element set of cut sites.

**2. Necessity of the three conditions.** If exactly one query \(I\) has answer zero and all other support queries have answer one, a cut site hits \(I\) and no other support interval; therefore \(I\) has a private site. If all queries have answer zero, the witnessing cut set has size \(c\) and hits every support interval, so \(\tau(S)\le c\). If all queries have answer one, the entire \(c\)-element cut set lies outside \(U(S)\), hence \(m-|U(S)|\ge c\).

**3. Interval overlap lemma.** If every interval in a finite family of distinct nonempty integer intervals has a private site, no point belongs to three intervals of the family. To see this, no interval is contained in another, because the contained interval would lack a private site. If three intervals \(I_1,I_2,I_3\) share a point \(x\), list them by increasing left endpoint. Their right endpoints must then also increase strictly. The middle interval \(I_2\) is contained in \(I_1\cup I_3\): the left portion of \(I_2\) through \(x\) is in \(I_1\), and the right portion from \(x\) is in \(I_3\). Thus \(I_2\) has no private site, a contradiction. This argument remains valid for singleton intervals and intervals meeting at endpoints.

**4. Sufficiency with an exact cut budget.** Suppose the three conditions hold, and prescribe an arbitrary zero-labeled subfamily \(N\subseteq\mathcal I(S)\). Take a minimum piercing set \(P\) of \(N\), so \(|P|=\tau(N)\le\tau(S)\le c\). Remove any redundant sites of \(P\). Every remaining site meets at least one member of \(N\). If a site of \(P\) meets an interval not in \(N\), the overlap lemma implies it meets **exactly one** member \(I\) of \(N\), since three support intervals cannot contain the same point. Replace that site by a private site of \(I\). The replacement continues to hit \(I\), hits no support interval outside \(N\), and cannot destroy hits of other members of \(N\) (the original site met no other such member). Repeating gives a set \(P'\) of at most \(c\) cut sites meeting precisely the support intervals in \(N\). There are at least \(c\) sites outside \(U(S)\); add distinct sites from that complement until the cut set has exactly \(c\) elements. Such padding changes no response on \(S\). Thus every labeling occurs and the criterion is sufficient.

**5. Dimension upper bound.** Let \(s=|S|\) for a shattered support. The \(s\) private sites are distinct and lie in \(U(S)\), while the all-positive labeling reserves \(c\) sites outside this union. Hence \(s\le m-c\). Under the all-zero labeling, \(c\) cut sites must hit all \(s\) support intervals. By the overlap lemma each site hits at most two intervals; therefore \(s\le2c\). Let \(r\) count the cut sites in this all-zero witness that hit **two** support intervals. A site that hits two intervals is not private; also different two-interval sites are distinct. Since a cut site hits at most two intervals, \(s\le c+r\), and so \(r\ge\max\{0,s-c\}\). Therefore \(|U(S)|\ge s+r\), yielding
\[
m\ge c+|U(S)|\ge c+s+\max\{0,s-c\}\ge2s.
\]
It follows that \(s\le\lfloor m/2\rfloor\). This proves all three upper bounds without assuming a particular structure of a maximizing support.

**6. Sharp witnesses for every parameter.** Put \(s=\min\{2c,\lfloor m/2\rfloor,m-c\}\). If \(s=0\), the empty support attains the bound. If \(1\le s\le c\), take \(s\) distinct singleton intervals on cut sites; there are at least \(c\) sites outside their union because \(m\ge s+c\). Every subset of these intervals is hit with at most \(s\le c\) sites and then padded outside.

If \(s>c\), let \(r=s-c>0\) and \(u=2c-s\ge0\). Choose \(r\) mutually disjoint **three-site gadgets**, with the pair of support intervals \([a,a+1]\) and \([a+1,a+2]\) on each gadget, and additionally \(u\) disjoint singleton intervals. The gadgets and singleton intervals use \(3r+u=2s-c\) sites and produce \(2r+u=s\) queries. Because \(m\ge2s\), at least \(c\) sites remain outside their union. Each gadget can realize either, both, or neither negative query with at most one hit: use its left private endpoint, right private endpoint, shared middle site, or no site, respectively. A selected negative singleton uses one site. Thus all patterns use at most \(r+u=c\) cut sites and can be padded outside the union. These witnesses achieve \(s\) in every case, completing the dimension formula.

## Verification

The separate, dependency-free `checker.py` implements (i) the three-condition support test via a private-site scan and greedy right-endpoint piercing and (ii) a separate brute-force generator of every \(c\)-site cut set and its complete Boolean trace. It checks all supports for \(m\le5\), every support of size at most five for \(m=6\), independently computes the exact VC dimension through \(m=8\) using recursive trace-fiber splitting, and additionally makes deterministic cross-checks for \(7\le m\le10\). See `verification_output.txt` for the actual successful execution counts. The infinite-parameter result rests on the proof above, not on finite experimentation.

For instance, at \(m=8\), the VC dimensions as the compulsory number of cut sites ranges from zero to eight are \((0,2,4,4,4,3,2,1,0)\); at \(m=6\) they are \((0,2,3,3,2,1,0)\). These illustrate both the plateau caused by the total site budget and the loss of shattering as nearly all sites become compulsory cuts.

## Relationship to prior work

Chase and Freitag [1] provide the model-theoretic and learning-theoretic VC framework; the present finite pair-query family uses that framework but is not a theorem stated there. Blais, Ferreira Pinto and Harms [2] describe the VC dimension of unions of a bounded number of point intervals, a related but different *primal* incidence family; the present concepts are exact-size sets of cut sites and the query domain consists of **all cut-site intervals** (same-block pair queries).

The published *Exact shattering polynomial for convex equivalence relations on a finite chain* [3] treats the same pair-query representation but explicitly allows **every** cut-set cardinality, proving a private-site support criterion and dimension \(m\). Fixing the number of blocks is not a formal specialization of its theorem: the permitted concept family is instead one rank slice of the cut-set Boolean lattice, and its VC dimension is bounded by \(\lfloor m/2\rfloor\), with two additional conditions required for shattering. The published *Refinement-closed partition concepts: exact shattering supports, online dimension, and coloring quotients* [4] assumes downward refinement closure, which is destroyed by prescribing exactly \(b\) blocks. The published *Forest size profiles determine shattering by fixed-cardinality cuts* [5] concerns unrestricted two-block partitions with a prescribed *block size*, rather than interval blocks with a prescribed *block count*. These are statement-level distinctions, not title differences. No priority claim is made for the generic greedy interval piercing algorithm or for the standard private-site terminology.

## Limitations

The result classifies VC-shattered supports and exact VC dimensions; it does not compute the face polynomial or adaptive (Littlestone) dimension, determine orbit counts under order reversal, or solve arbitrary interval hypergraph variants with a different cut-budget rule. In particular, the theorem makes no statement about partitions into a fixed number of **nonconvex** blocks. Searches and relevant document inspections cannot rule out equivalent treatments under alternate terminology (fixed-size transversals, dual interval range spaces, and uniform-rank cuts); independent mathematical and historical audit has not been performed. The executable checker is finite verification only.

## References

[1] H. Chase and J. Freitag, *Model Theory and Machine Learning*, arXiv:1801.06566v1 (public 2018-01-19), https://arxiv.org/abs/1801.06566.

[2] E. Blais, R. Ferreira Pinto Jr., and N. Harms, *VC Dimension and Distribution-Free Sample-Based Testing*, arXiv:2012.03923v1 (public 2020-12-07), https://arxiv.org/abs/2012.03923.

[3] *Exact shattering polynomial for convex equivalence relations on a finite chain*, published scientific result, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-shattering-polynomial-for-convex-equivalence-relations-on--f0f3d770c003/RESULT.md.

[4] *Refinement-closed partition concepts: exact shattering supports, online dimension, and coloring quotients*, published scientific result, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-refinement-closed-partition-concepts-exact-shattering-supports-o--2203ea0ddc4a/RESULT.md.

[5] *Forest size profiles determine shattering by fixed-cardinality cuts*, published scientific result, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-forest-size-profiles-determine-shattering-by-fixed-cardinality-c--e71e3de9534e/RESULT.md.
