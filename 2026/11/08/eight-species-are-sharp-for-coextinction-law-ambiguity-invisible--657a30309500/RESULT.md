# Eight species are sharp for coextinction-law ambiguity invisible to mean and variance

## Finding

In the connected, simple bipartite model of plants and pollinators with no isolated species, the number of plants retaining at least one living pollinator can have identical mean and variance curves in two networks, yet different full probability laws. **Eight total species are necessary and sufficient** for this phenomenon. More precisely, among connected networks with exactly eight total species there are **exactly five** unordered pairs of nonisomorphic, part-respecting network classes with this property: four with four plants and four pollinators and one with five plants and three pollinators.

Here and throughout, a *moment twin* means two networks with the same numbers of plants and pollinators and identical mean and variance functions for every extinction probability \(q\in(0,1)\), but different probability laws for at least one such \(q\).

An explicit connected four-plant, four-pollinator moment-twin pair has respective plant-partner sets
\[
\mathcal A=(\{a,b\},\{a,c\},\{b,c\},\{a,b,c,d\}),\qquad
\mathcal B=(\{a,b\},\{a,c\},\{a,d\},\{a,b,c,d\}).
\]
For \(Y\), the number of plants with at least one surviving partner, these networks satisfy
\[
\mathbb E[Y_{\mathcal A}]=\mathbb E[Y_{\mathcal B}]
=4-3q^2-q^4,
\quad
\mathbb E[(Y_{\mathcal A})_2]=\mathbb E[(Y_{\mathcal B})_2]
=12-18q^2+6q^3,
\]
where \((Y)_2=Y(Y-1)\). Nevertheless,
\[
\Pr(Y_{\mathcal B}=4)-\Pr(Y_{\mathcal A}=4)=q^3(1-q)>0.
\]
The largest invisible all-plants-served probability gap for this witness is \(27/256\), attained at \(q=3/4\).

## Assumptions and scope

Let \(G\) be a finite simple connected bipartite graph with a distinguished plant part \(P\) of size \(p\ge1\) and pollinator part \(M\) of size \(m\ge1\). Every plant and pollinator has positive degree. Pollinators disappear independently, with common probability \(q\in(0,1)\). A plant is counted as functionally served if it retains at least one pollinator neighbor. Define \(Y_G(q)\) to be the number of served plants. This is an instantaneous, one-sided topological service-loss model: there is no pollinator rewiring, graded interaction strength, intrinsic plant mortality or feedback cascade. Network isomorphisms must preserve the two guilds; their individual labels are immaterial.

For every plant \(i\), write \(S_i\subseteq M\) for its nonempty set of pollinator partners, \(d_i=|S_i|\), and \(u_{ij}=|S_i\cup S_j|\). Two compared networks always have equal \(p\) and \(m\). An *entire-law difference* means a difference in some \(\Pr(Y=k)\) for some \(q\in(0,1)\).

## Proof

**Moment reduction.** Let \(I_i\) be the indicator that plant \(i\) is served. Because its pollinator partners disappear independently, \(\Pr(I_i=0)=q^{d_i}\); two plants are simultaneously unserved with probability \(q^{u_{ij}}\). Consequently,
\[
\mathbb E Y=p-\sum_iq^{d_i},
\]
\[
\mathbb E (Y)_2=p(p-1)-2(p-1)\sum_iq^{d_i}
+2\sum_{i<j}q^{u_{ij}},
\qquad
\operatorname{Var}(Y)=\mathbb E(Y)_2+\mathbb EY-(\mathbb EY)^2.
\]
Since powers of \(q\) have independent coefficients, equality of complete mean and variance curves is equivalent to equality of the multisets of plant degrees and unordered plant-pair union sizes. No assumption about higher-order partner-set unions follows from these two profiles.

**Lower bound, small plant part.** Because every pollinator serves at least one plant, \(Y=0\) precisely when every pollinator has disappeared, so \(\Pr(Y=0)=q^m\), independent of network topology. When \(p\le3\), normalization, the first two moments and this zero-service probability uniquely determine the probabilities of every other possible value of \(Y\): for the at most three unknown masses at \(1,2,3\), the coefficient matrix with rows \((1,1,1)\), \((1,2,3)\), \((1,4,9)\) is nonsingular (with unused values omitted). Hence no two networks with at most three plants can be moment twins.

**Lower bound, small pollinator part.** For \(m=1\), the entire law is immediate. For \(m=2\), if precisely one pollinator survives, the served-plant count equals its degree (as a pollinator) and the two single-survivor configurations each occur with probability \(q(1-q)\). The both-survive and both-extinct counts are the fixed values \(p\) and \(0\). The mean and second-moment functions determine the sum and sum of squares of the two pollinator degrees, hence their unordered pair and the entire law. Thus \(m\le2\) cannot support moment twins for any \(p\).

**Remaining case below eight total species.** The only not-yet-covered possibility with \(p+m\le7\) is \((p,m)=(4,3)\). Every such graph is represented by four nonzero masks from \(\{1,\ldots,7\}\) whose bitwise union is \(7\). There are exactly \(7^4-3\cdot3^4+3=2161\) such labelled matrices. Sorting masks and minimizing over all six pollinator permutations gives exactly 42 guild-preserving isomorphism classes. Exact enumeration of their degree/pair-union signatures and, independently, direct enumeration of all pollinator-survival subsets proves that every class sharing a moment signature also shares the whole service-count law. The certificate `verify.py` exhausts all 2,161 labelled matrices without using graph isomorphism as a shortcut and rechecks the 42-class quotient. Therefore no graph with fewer than eight total species is a counterexample.

**Witness and gap.** Both displayed networks are connected (their fourth plant meets every pollinator); the first three plant-partner sets have sizes \(2,2,2\) and pairwise unions of size \(3\), while the fourth has size \(4\). Thus the moment reduction gives identical moment curves. In \(\mathcal A\), the first three partner sets have triple union size \(3\), whereas in \(\mathcal B\) the triple union size is \(4\). Inclusion-exclusion for all plants being served yields
\[
\Pr(Y_{\mathcal A}=4)=1-3q^2+2q^3,\qquad
\Pr(Y_{\mathcal B}=4)=1-3q^2+3q^3-q^4.
\]
The gap is \(q^3(1-q)\), strictly positive in the domain, with its unique maximum at \(q=3/4\). Their pollinator-degree multisets differ, so they cannot be isomorphic by a guild-preserving bijection.

**Entire connected eight-vertex exception layer.** The small-part arguments leave only \((p,m)=(4,4)\) and \((5,3)\) at total size eight. Canonical row-mask enumeration under all pollinator permutations produces respectively \(150\) and \(76\) connected isomorphism classes. For each class the exact first-two-moment polynomial signature is compared, and every moment-equivalent pair is tested against its full Bernoulli-mixture probability law. There are exactly four different-law pairs in the first case and exactly one in the second. The five unordered pairs, given as pairs of sorted bit-mask tuples with least-significant bit denoting pollinator \(a\), are:

| Plant/pollinator counts | First graph | Second graph |
|---|---|---|
| \((4,4)\) | `(1,7,7,14)` | `(1,7,11,13)` |
| \((4,4)\) | `(3,5,6,15)` | `(3,5,9,15)` |
| \((4,4)\) | `(3,5,7,14)` | `(3,5,11,13)` |
| \((4,4)\) | `(3,5,11,13)` | `(3,7,7,12)` |
| \((5,3)\) | `(1,3,3,3,6)` | `(1,3,3,5,5)` |

The independent certificate `crosscheck.py` generates every labelled binary incidence matrix (not only row multisets), reduces by guild-preserving isomorphisms, computes moment coefficients directly from extinction outcomes rather than degree/union formulas, and reproduces the same class counts and five-pair census.

## Verification

Run `python3 verify.py` and `python3 crosscheck.py` with standard Python 3. Both must print `PASS`. All arithmetic in the certificates is integer except the exact rational check at \(q=1/2\), performed with Python `fractions.Fraction`. The first certificate checks 2,161 labelled four-by-three networks, the exact 42-class quotient, 150 connected four-by-four classes, 76 connected five-by-three classes, every equal-moment class pair, and the explicit witness. The second independently checks all labelled binary incidence matrices in the two eight-vertex cases and obtains the same five pairs. The proof's finite cutoff uses exhaustive enumeration of each complete stated search domain, not statistical sampling.

## Relationship to prior work

The species-dependence rule is the standard topological last-partner-loss approximation considered in the pollination-network robustness literature, including Memmott, Waser and Price (2004). Campbell et al. (2012) investigated vulnerable mutualistic-network topology with a dynamic Boolean model. Vieira, Cianciaruso and Almeida-Neto (2013) simulated coextinction impacts on phylogenetic and functional diversity, while Vieira and Almeida-Neto (2014) introduced a stochastic model with interactions weighted beyond the last-partner-loss approximation. These sources motivate the dependence structure, but the present claim is an exact *moment-to-full-law identifiability threshold and first exceptional connected-layer classification*. No published result is claimed for these formulas merely by rephrasing a general coextinction model.

## Limitations

The conclusion is a finite-graph theorem for uniform independent pollinator extinction and binary last-partner plant service; it does not cover heterogeneous extinction probabilities, probabilistic dependence on partner abundance, coextinction feedback, network adaptation, or measured ecosystem productivity. Moment twins need not have the same pollinator-degree distribution, and the theorem does not say that mean/variance alone reconstructs a general network. The finite census is reproducible but has not received an independent external scientific audit. Historical originality beyond the directly inspected literature is provisional; especially, some relevant original papers were available only by abstract during literature examination.

## References

1. Memmott, J., Waser, N. M., and Price, M. V. (2004). *Tolerance of pollination networks to species extinctions*. Proceedings of the Royal Society B **271**, 2605–2611. https://doi.org/10.1098/rspb.2004.2909 (public 2004-12-22).
2. Campbell, C., Yang, S., Shea, K., and Albert, R. (2012). *Topology of plant-pollinator networks that are vulnerable to collapse from species extinction*. Physical Review E **86**, 021924. https://doi.org/10.1103/PhysRevE.86.021924.
3. Vieira, M. C., Cianciaruso, M. V., and Almeida-Neto, M. (2013). *Plant-pollinator coextinctions and the loss of plant functional and phylogenetic diversity*. PLOS ONE **8**, e81242. https://doi.org/10.1371/journal.pone.0081242.
4. Vieira, M. C., and Almeida-Neto, M. (2014). *A simple stochastic model for complex coextinctions in mutualistic networks: robustness decreases with connectance*. Ecology Letters **18**, 144–152. First published 2014-11-28. https://doi.org/10.1111/ele.12394.
