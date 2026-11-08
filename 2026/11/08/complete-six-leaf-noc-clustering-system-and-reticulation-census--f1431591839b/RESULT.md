# Complete six-leaf NOC clustering-system and reticulation census

## Finding

Fix a labeled set \(X\) of six elements. Let \(\mathcal C\) be a clustering system, meaning a family of nonempty subsets containing \(X\) and each singleton of \(X\). Two sets *overlap* when they intersect but neither contains the other. The system is *not-overlap-covered* (NOC) when every \(C\in\mathcal C\) has a point outside every member that overlaps \(C\). Write \(\mathcal H(\mathcal C)\) for the inclusion Hasse diagram, with arcs directed from strict supersets to their immediate strict subsets. Let \(r(\mathcal C)\) count Hasse vertices with at least two parents, and let \(q_{n,k}\) count NOC clustering systems on a fixed labeled \(n\)-element set with \(r(\mathcal C)=k\).

**Exact finite census.** For \(n=6\), the complete distribution is
\[
(q_{6,0},q_{6,1},q_{6,2},q_{6,3},q_{6,4})
=(2752,79076,1037235,4511390,4023915),
\]
with \(q_{6,k}=0\) for all other \(k\). In particular,
\[
q_6=\sum_{k\ge0}q_{6,k}=9{,}654{,}368.
\]
By the known NOC-to-network bijection, these are also the exact numbers of leaf-label-preserving isomorphism classes of **strong-phylogenetic normal networks** with six leaves and the indicated number of reticulation vertices.

The reproducibility table additionally gives \(q_2=1\), \(q_3=7\), \(q_4=210\), and \(q_5=23{,}746\), with complete reticulation distributions in `counts.tsv`. These smaller entries are crosschecks, not additional independent general theorems.

## Assumptions and scope

All leaf labels are distinct and fixed, and set families are not identified under permutations of \(X\). A reticulation vertex is any Hasse-diagram vertex having **at least two** immediate strict supersets; no binary indegree/outdegree restriction is imposed. Counts refer to *clustering systems*, not arbitrary networks realizing the same clusters. The transfer to canonical strong-phylogenetic normal networks uses the bijection of Lindeberg and Hellmuth, Corollary 11, and the definition of \(q_{n,k}\) in their concluding section. No count is asserted for \(n\ge7\).

## Proof

The exact integers have a finite exhaustive computational proof, with two separately implemented exhaustive searches. We establish that both programs enumerate precisely the required mathematical objects, without pruning any admissible family; the source code and exact output checks form part of this proof.

**1. Exhaustive parameterization.** For \(n\) leaves, precisely \(2^n-n-2\) subsets can be optional clusters: those of size between two and \(n-1\) inclusive. For six leaves there are \(56\) such subsets. Every clustering system is uniquely determined by a Boolean include/exclude choice for each of these optional subsets, together with the mandatory singletons and \(X\). Each optional cluster is represented as a bit mask, so no labeled family is counted more than once.

**2. Exact NOC test.** For an optional selected cluster \(C\), define
\[
W_{\mathcal A}(C)=C\mathbin{\setminus}
 \bigcup_{\substack{D\in\mathcal A\\D\text{ overlaps }C}} D,
\]
where \(\mathcal A\) is the currently selected family of optional clusters. The mandatory singletons and \(X\) overlap no cluster, so the full clustering system is NOC if and only if \(W_{\mathcal A}(C)\ne\emptyset\) for every optional selected \(C\). When adding a new optional set \(S\), the witness sets change by the exact rule
\[
W_{\mathcal A\cup\{S\}}(C)
=\begin{cases} W_{\mathcal A}(C)\setminus S,& C\text{ overlaps }S,\\
W_{\mathcal A}(C),&\text{otherwise},\end{cases}
\]
and the new set's witnesses are \(S\setminus\bigcup_{C\in\mathcal A,\ C\text{ overlaps } S}C\). A witness set can only shrink under further additions. Therefore, any branch whose selected family violates NOC can safely be discarded forever. Conversely, each NOC family has only NOC subfamilies, so the unique include/exclude path to that family is never pruned. This proves completeness of the incremental search, including its branch pruning.

**3. Exact reticulation statistic.** At each accepted leaf, append the six mandatory singleton masks and the full mask. For each cluster \(C\), the number of parents is computed by checking every selected proper superset \(D\supsetneq C\) and retaining \(D\) exactly when no selected \(E\) satisfies \(C\subsetneq E\subsetneq D\). This is the definition of a Hasse cover, so counting clusters with two or more such parents gives precisely \(r(\mathcal C)\). There is no truncation of the possible reticulation range: the histogram vector dynamically expands whenever necessary.

**4. Arithmetic and independent replay.** `noc_incremental.cpp` follows the witness-update rule above and examines optional sets in decreasing cardinality order; it returns the distribution in the statement after accepting exactly \(9{,}654{,}368\) families. `noc_direct.cpp` enumerates optional sets in increasing bit-mask order and **recomputes the entire NOC condition from scratch** at every inclusion step. It uses an independently coded Hasse-cover check and returns the identical five histogram entries. `verify.py` compiles and runs both searches for every \(2\le n\le6\), compares every histogram entry with `counts.tsv`, and additionally performs a naive Python family enumeration for \(2\le n\le4\). All three implementations agree where their domains overlap. Since the searches consider every possible clustering system, the computed integers are exhaustive, rather than estimates or partial samples.

**5. Network interpretation.** Lindeberg and Hellmuth proved that each NOC clustering system corresponds uniquely to a strong-phylogenetic normal network with its labeled leaf set and with its Hasse diagram as canonical realization. Their specified reticulation refinement counts vertices with at least two Hasse parents. Therefore the enumerated \(q_{6,k}\) are exactly the corresponding leaf-labeled network isomorphism-class counts. This equivalence, including the existence and uniqueness theorem, is *prior work*, not a new proof here.

## Verification

From a directory containing all supplied sources, run `python3 verify.py`. It requires a C++17 compiler (`g++`) and Python 3.10 or later, and uses only the standard Python library. It recompiles both implementations in a temporary directory, enumerates all admissible families for each \(n=2,3,4,5,6\), checks `counts.tsv`, independently checks small orders in Python, and prints `VERIFY_OK` only if every assertion succeeds. On the actual package sources the replay printed `CPP_CENSUS_OK` for all ten C++/order combinations and ended with `VERIFY_OK 2 independent full six-leaf enumerators; naive small-n control`.

The direct n=6 program visited \(60{,}009{,}613\) recursion states; the incremental implementation visited \(45{,}312{,}598\) states and rejected \(26{,}003{,}863\) infeasible inclusion branches. These are search statistics, not unproven assumptions. Replaying the supplied code rederives the histograms independently of those reported values.

## Relationship to prior work

Lindeberg and Hellmuth introduced the NOC definition, identified its equivalence with inclusion-visibility, proved the exact NOC/normal-network correspondence, and explicitly defined the natural enumerative parameters \(q_n\) and \(q_{n,k}\) in Section 5 of arXiv:2609.13336. They invited enumeration of these parameters but did not list the six-leaf counts above. The new contribution here is the **exact complete six-leaf reticulation distribution**, rather than the NOC characterization or the construction of the Hasse realization.

The previously published equality classification of extremal NOC set systems counts only families with the **maximum possible number of clusters**, giving \(n!/2\) families in that sparse sublayer (\(360\) when \(n=6\)); it does not enumerate the other millions of valid families or their reticulation profile. Published enumerations of *binary* tree-child and normal networks, such as those of Fuchs, Gittenberger, and Mansouri, concern an additional binary degree restriction and thus do not cover the unrestricted NOC/Hasse family here. Searches also considered the aliases *strict compatibility*, *inclusion visibility*, *regular normal network*, *strong-phylogenetic normal network*, and the exact displayed numbers. No source located gave these exact values or an implication forcing them.

## Limitations

This is a finite, fully specified computational census, not a formula or asymptotic for arbitrary \(n\). The correctness of the exact integers depends on the completeness argument and replayable implementations. Two programs provide crosschecking but are not independent mathematical certification. Values for binary network conventions should not be identified with the values here. Priority remains provisional because unindexed or inaccessible relevant work may exist, and no independent mathematical audit has been performed.

## References

1. A. Lindeberg and M. Hellmuth, *NOC NOC, who's there? Clustering systems of tree-child and normal networks*, arXiv:2609.13336, originally public 2026-09-11. https://arxiv.org/abs/2609.13336
2. M. Fuchs, B. Gittenberger, and E. Y. Mansouri, *Counting phylogenetic networks with few reticulation vertices: exact enumeration and corrections*, 2021. See https://arxiv.org/abs/2006.15784 for the binary counting framework.
3. *Equality cases for the quadratic NOC bound*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/9/19/SCOPE-extremal-noc-set-systems--3ab59462c5be (extremal sublayer only).
