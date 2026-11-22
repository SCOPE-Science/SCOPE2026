# Minimum allele-loss-resilient mating supports under two sporophytic self-incompatibility rules

## Finding

Consider a collection of distinct heterozygous diploid plant genotypes at one self-incompatibility locus, with exactly \(k\ge 2\) available S-alleles and all \(k\) represented. A collection is *one-allele-loss-resilient* if, after eliminating every genotype containing any prescribed one S-allele, two remaining genotype types can still form at least one compatible directed pollen-to-stigma cross. The original collection must survive this test for **every** choice of deleted allele.

Under a strict common dominance hierarchy in pollen and codominance in the stigma (DOMCOD), the minimum number of genotype types is

\[
N_{\mathrm{DOMCOD}}(k)=
\begin{cases}
\infty,&2\le k\le 3,\\
5,&k=4,\\
4,&k=5,\\
\lceil k/2\rceil,&k\ge 6.
\end{cases}
\]

If both pollen and stigma express both S-alleles codominantly (COD), the corresponding minimum is

\[
N_{\mathrm{COD}}(k)=
\begin{cases}
\infty,&2\le k\le 4,\\
5,&k=5,\\
\lceil k/2\rceil,&k\ge 6.
\end{cases}
\]

Infinity means no choice of distinct heterozygote genotypes works, even when all possible genotypes are present. For \(k=4\), there are exactly three DOMCOD minimum collections; for \(k=5\), the COD minimum collections are exactly the twelve labeled five-cycles when genotypes are viewed as edges between allele labels. Thus pollen dominance enables resilience with four S-alleles and saves one genotype type with five S-alleles, but this minimum-support advantage vanishes from six alleles onward.

## Assumptions and scope

Fix an integer \(k\ge 2\) and S-allele labels \([k]=\{1,\ldots,k\}\), totally ordered so that smaller labels dominate larger labels in **pollen**. A genotype type is an unordered pair \(\{i,j\}\subseteq[k]\) with \(i\ne j\). A cohort \(E\) is a set (not a multiset) of such pairs, with \(\bigcup_{e\in E}e=[k]\). Every genotype type has at least one reproductively capable individual; its frequency is immaterial to the existential compatibility question.

For DOMCOD, a donor genotype \(e\) expresses its smallest S-allele in pollen, while the stigma of genotype \(f\) expresses both alleles. By definition, pollen from \(e\) is accepted by the stigma of \(f\) exactly when \(\min(e)\notin f\). Thus this crossing relation can be directed, and at least **one** of the two possible directions is sufficient. For COD, both alleles are expressed in both tissues, so the cross is permitted exactly when \(e\cap f=\varnothing\). These definitions idealize standard SSIcod and SSIdomcod expression patterns; no environmental or stochastic fertilization model is assumed.

For each deleted allele \(v\), let \(E-v=\{e\in E:v\notin e\}\). Resilience means for each \(v\in[k]\) there exist **distinct** \(e,f\in E-v\) such that the donor \(e\) is compatible with recipient \(f\) under the applicable rule. The deletion removes all genotypes carrying \(v\), not merely one plant. This is a worst-case *genotype-support* condition, not a statement about post-deletion allele-frequency equilibrium, dispersal, pollen quantity, or population persistence. Label order is fixed independently of genotype deployment.

## Proof

**1. Universal coverage lower bound and the small-alphabet obstruction.** Every genotype contains two allele labels, so covering all \(k\) labels needs at least \(\lceil k/2\rceil\) genotypes under either rule. When \(k\le3\), deleting an allele leaves at most two allele labels and hence at most one distinct heterozygous genotype type. Two distinct surviving compatible types are impossible. When \(k=4\), COD is also impossible: deleting any allele leaves only three possible labels, whereas two codominantly compatible diploid genotypes must be disjoint and therefore use four distinct labels.

**2. Complete \(k=4\) DOMCOD classification.** Write \(ij\) for the genotype \(\{i,j\}\). For three labels \(a<b<c\), one allowed directed DOMCOD cross exists among the selected genotypes if and only if genotype \(bc\) is present together with at least one of \(ab\) and \(ac\). Indeed, \(ab\) and \(ac\) share dominant pollen allele \(a\), which both respective stigmas contain, and a cross between either and \(bc\) is compatible because \(a\notin\{b,c\}\); without \(bc\), no two types can cross. Apply this criterion after deleting one allele from \([4]\). The remaining triples \(123,124,134,234\) force genotype edges \(23,24,34\) and the three additional conditions

\[
(12\in E\ \text{or}\ 13\in E),\qquad
(12\in E\ \text{or}\ 14\in E),\qquad
(13\in E\ \text{or}\ 14\in E).
\]

At least two of \(12,13,14\) are therefore needed, and any two suffice (the \(234\) condition is then already satisfied). Exactly three five-genotype minimizers result:

\[
E=\{23,24,34\}\cup A,\qquad A\in\bigl\{\{12,13\},\{12,14\},\{13,14\}\bigr\}.
\]

Each covers all four labels and passes every deletion test, proving \(N_{\mathrm{DOMCOD}}(4)=5\) and the asserted classification.

**3. The five-label dominance contrast.** Suppose a resilient \(k=5\) cohort had at most three genotypes. Every allele must occur in at least one of them. If any allele occurs in two or more, deleting it leaves at most one genotype, impossible. If every allele occurs in at most one, three genotypes use six distinct allele labels, also impossible on five labels. Thus four genotypes are necessary. The four-genotype path \(E=\{12,23,34,45\}\) is resilient under DOMCOD: deleting labels \(1,2,3,4,5\), respectively, leaves compatible ordered donor-recipient witnesses

\[
(23,34),\ (34,45),\ (12,45),\ (12,23),\ (12,23).
\]

For example, \(12\to23\) succeeds because pollen specificity \(1\) is absent from recipient \(23\); disjoint pairs automatically succeed in either model. This proves \(N_{\mathrm{DOMCOD}}(5)=4\).

For COD, view the cohort as a simple undirected graph with S-alleles as vertices and genotype types as edges. After deleting any vertex of a five-vertex graph, resilience means that the remaining four vertices contain two vertex-disjoint edges, i.e. a perfect matching. In graph terminology this is the standard **factor-critical** property; it is *not* a new graph-theoretic notion. Every vertex of such a graph has degree at least two: removing the sole neighbor of any vertex of degree at most one would leave an isolated vertex, precluding a perfect matching. Hence the graph has at least five edges by the degree sum. With exactly five edges all five degrees equal two, and the sole simple 2-regular graph on five vertices is a five-cycle. Conversely, deleting any vertex of a five-cycle leaves a four-vertex path with a perfect matching. There are \(5!/(2\cdot5)=12\) labeled five-cycles. This proves \(N_{\mathrm{COD}}(5)=5\) and the classification. The factor-critical observation is a known matching-theory reduction; the new question here is the contrast with the directed S-locus rule under the same allele-deletion requirement.

**4. All \(k\ge6\).** If \(k=2r\) is even with \(r\ge3\), take the \(r\) pairwise disjoint genotypes \(12,34,\ldots,(2r-1)(2r)\). Removing an S-allele eliminates exactly one genotype and leaves \(r-1\ge2\) disjoint genotypes that cross in both directions under either rule. If \(k=2r+1\) is odd with \(r\ge3\), use the same \(r\) disjoint genotypes on the first \(2r\) alleles and add \(1(2r+1)\). After deletion of label \(1\), at least \(r-1\ge2\) disjoint original genotypes remain; after deletion of any other allele, at least \(r-1\ge2\) disjoint original genotypes remain. Both constructions cover all allele labels and contain precisely \(\lceil k/2\rceil\) genotypes. They attain the universal lower bound, completing the proof for both schemes.

## Verification

The included standalone `checker.py` checks every candidate cohort of each size up to and including the first feasible size for allele alphabets \(2\) through \(6\) (or all sizes if infeasible), returning the exact minima and number of minimum-size cohorts; it also checks the three four-allele DOMCOD minimizers, all twelve five-allele COD five-cycles, and the explicit constructions for every \(k\) from \(7\) through \(60\). Invoke `python3 checker.py` using Python's standard library. The verifier reported **12,494 deterministic assertions passed** on the included file. These finite checks corroborate but do not replace the all-\(k\) proof above. See `VERIFICATION.md` for the replay scope.

## Relationship to prior work

Schierup, Vekemans and Christiansen (1997) explicitly defined and compared SSIcod, SSIdom and SSIdomcod systems and studied allele turnover and selection by stochastic simulations. The published abstract documents their SSIcod and SSIdomcod distinctions, but the full 1997 paper could not be examined through accessible channels here. Accordingly it cannot be pronounced wholly noncovering. Schoen and Busch (2009), whose full article's abstract, modeling assumptions, equations and conclusions were inspected, investigated frequency-dependent selection and the evolution of tissue-specific S-locus dominance, not the cardinality of a genotype collection robust to deleting all carriers of any allele. Thrall and colleagues (2014), whose open-access article, model and results were examined, used spatial simulations to study how allele richness and mating-system expression influence population persistence; it does not give the stated exact adversarial genotype-support threshold. The standard factor-critical graph framework covers the codominant five-label five-cycle subclaim as a known matching-theory instance; this part is included as a baseline, **not claimed as independently original**. The comparative four- and five-label DOMCOD thresholds, together with their reconciliation with the universal coverage bound, distinguish the stated cross-model support result. The literature coverage is necessarily qualified, not a proof of historical novelty.

## Limitations

This theorem is existential: one compatible directed cross survives every deletion. It does not ensure every surviving individual can mate, reciprocal compatibility, sufficient pollen, breeding success, stable allele frequencies, or population persistence. It assumes a single common strict pollen dominance ordering, completely codominant stigma expression, no heterozygote duplicates, and one entire S-allele type deleted at a time. Different biological dominance graphs, pollen recognition pathways, stochastic genotype extinction, more than one S-allele deletion, or mandatory genetic inheritance after mating require fresh analysis. Full text of the 1997 original and some older mate-availability work remained unavailable, leaving a residual priority risk despite the inspected later full texts and matching-theory comparison.

## References

1. M. H. Schierup, X. Vekemans and F. B. Christiansen. *Evolutionary Dynamics of Sporophytic Self-Incompatibility Alleles in Plants*. **Genetics** 147 (1997), 835–846. First published 1 October 1997. https://doi.org/10.1093/genetics/147.2.835
2. D. J. Schoen and J. W. Busch. *The Evolution of Dominance in Sporophytic Self-Incompatibility Systems. II. Mate Availability and Recombination*. **Evolution** 63 (2009), 2099–2113. First published 29 July 2009. https://doi.org/10.1111/j.1558-5646.2009.00686.x
3. P. H. Thrall, F. Encinas-Viso, S. E. Hoebee and A. G. Young. *Life History Mediates Mate Limitation and Population Viability in Self-Incompatible Plant Species*. **Ecology and Evolution** 4 (2014), 673–687. https://doi.org/10.1002/ece3.963
4. X. Vekemans, M. H. Schierup and F. B. Christiansen. *Mate Availability and Fecundity Selection in Multi-Allelic Self-Incompatibility Systems in Plants*. **Evolution** 52 (1998), 19–29. https://doi.org/10.1111/j.1558-5646.1998.tb05134.x
5. Factor-critical graph, standard matching-theory definition and five-cycle example: https://en.wikipedia.org/wiki/Factor-critical_graph (background only, not a novelty source).
