# A first fractional-packing gap for paired-chord deletion on ordered matchings

## Finding

For perfect matchings on ordered endpoints, the zero-error code capacities for deletion of one *unknown entire pair* are

\[
(A_1,A_2,A_3,A_4)=(1,1,3,7).
\]

The corresponding numbers of optimal, labeled codebooks are \((1,3,1,278)\), and the fractional shadow-packing optima are \((1,1,3,15/2)\). Hence four pairs are the first instance where this natural linear-programming relaxation has a strictly nonintegral optimum. At four pairs, exactly \(136\) optimal codebooks are fixed by reversal of the endpoint order, so there are \(207\) reversal classes.

## Assumptions and scope

For each \(m\in\{1,2,3,4\}\), the source space \(\mathcal M_m\) is the set of *all* perfect matchings of the ordered set \(\{0,\ldots,2m-1\}\). A pair is represented by \((a,b)\) with \(a<b\), and pairs are listed in increasing order of their first endpoint. A channel use selects one matched pair and deletes *both* its endpoints. The surviving vertices are renumbered from zero in increasing order. The resulting distinct matchings form a set \(D(M)\), where equal received outcomes are counted only once. Thus \(D(M)\subseteq\mathcal M_{m-1}\), with \(\mathcal M_0\) consisting of the empty matching.

A zero-error code \(\mathcal C\subseteq\mathcal M_m\) requires \(D(M)\cap D(M')=\varnothing\) for all distinct \(M,M'\in\mathcal C\). This is unique decoding of a *single received outcome*, not reconstruction from an entire deletion deck. Define \(A_m\) to be the maximum code cardinality and \(N_m\) to be the number of different maximum codebooks on these fixed labels. Define the fractional packing value

\[
P_m=\max\left\{\sum_{M\in\mathcal M_m}x_M:\;x_M\ge0,\quad
\sum_{M:N\in D(M)}x_M\le1\ \text{for every }N\in\mathcal M_{m-1}\right\}.
\]

Reversal maps the vertex \(j\) to \(2m-1-j\) and is applied to every pair, hence to every codebook. Only that two-element symmetry group is counted; no cyclic identification or arbitrary relabeling is allowed.

## Proof

**Exact incidence recurrence.** Perfect matchings are generated without omission or duplication by pairing the least unpaired vertex with each possible larger partner and recursively pairing the remaining vertices. This enumerates respectively \(1,3,15,105\) sources at orders \(m=1,2,3,4\). Each channel output is produced by deleting each one of the source's \(m\) pairs, renumbering survivors in order, and deduplicating the resulting outputs. There are respectively \(1,1,3,15\) possible output matchings.

Associate to a source \(M\) the binary mask of its distinct outputs. For any set \(U\) of still-available output types, let \(F(U)\) be the maximum size of a family with shadows contained in \(U\) and mutually disjoint, and let \(G(U)\) count the maximizing families. Choose the least output \(r\in U\). Partition every admissible family according as \(r\) is unused, or as \(r\) belongs to the shadow of its unique chosen source \(M\). The former branch has universe \(U\setminus\{r\}\); the latter branches over every source with \(r\in D(M)\subseteq U\), and have universe \(U\setminus D(M)\) and a single additional selected source. Set \(F(\varnothing)=0\), \(G(\varnothing)=1\); maximize among these mutually exclusive branches and sum their counts only for branches achieving the maximum. The partition is exhaustive and disjoint because each admissible code has pairwise disjoint shadows. This proves by induction that the recurrence yields *both* exact optimum and exact equality count, with no sampling or floating-point approximation. Evaluating on the complete output universe for \(m=1,2,3,4\) yields the stated \((A_m)\) and \((N_m)\). A separate maximal-clique enumeration on the graph linking sources with disjoint shadows returns the same numbers.

**Direct sharp certificates at four pairs.** The enclosed `CERTIFICATES.json` and `verify.py` fix a deterministic source ordering by the least-partner recursion, with zero-based indices. The seven source indices

`[0,23,50,52,78,87,104]`

have pairwise disjoint shadows. Their complete matched-pair descriptions are in the certificate and checked against that canonical enumeration. Therefore \(A_4\ge7\).

For the fractional optimum, use source weights in integer *half-units* with nonzero entries

`{0:2,17:2,31:2,52:2,65:2,87:1,88:1,94:1,104:2}`.

The sum of these integers is \(15\). Directly checking all \(15\) output constraints shows that each output receives at most \(2\) half-units. Hence these weights are a feasible fractional source packing of value \(15/2\).

For the matching dual fractional cover, order the \(15\) outputs by the same recursive enumeration. Assign the following nonnegative integer half-unit weights:

`[2,1,1,1,0,0,1,2,1,0,1,1,1,1,2]`.

Their sum is \(15\), and for *every one* of the \(105\) sources the sum of these integers over its distinct outputs is at least \(2\). Therefore every feasible fractional source packing has value at most \(15/2\). Consequently \(P_4=15/2\), and integral codes have at most \(\lfloor15/2\rfloor=7\) members. The seven-word witness proves \(A_4=7\). For \(m\le3\), the displayed integer code maxima already equal the number of possible received outputs, which is a universal fractional upper bound; hence \(P_1=P_2=1\) and \(P_3=3\).

**Equality and reversal.** The exact subset recurrence counts \(278\) seven-member codes. For each such code the checker applies the involution \(j\mapsto7-j\) to every endpoint; precisely \(136\) equality cases are fixed. A two-element group has singleton or two-element orbits, so Burnside's lemma gives \((278+136)/2=207\) orbits.

## Verification

`verify.py` is a standalone Python standard-library checker. Run it in the same directory as `CERTIFICATES.json` with `python3 verify.py`; its final line is `VERIFY_OK`. It reconstructs all perfect matchings by two separately coded generators, computes all deletion shadows by both direct increasing-renumbering and an independent partner-involution implementation, and compares the two incidence structures. It evaluates the subset dynamic program and a separate Bron–Kerbosch maximal-clique enumeration at every claimed order. At four pairs it independently tests every source and output inequality of the primal and dual exact rational certificates, the concrete seven-source code, equality counts and reversal-orbit counts. All arithmetic is integral. The full finite domain, not a random sample, is checked. The output counts \((1,1,3,15)\) and source counts \((1,3,15,105)\) are also independently reproduced.

## Relationship to prior work

Pilaud and Rué analyze the same ordered chord-diagram/matching objects under crossing statistics, but not deletion-shadow coding or the precise four-pair incidence packing problem [1]. Gabrys and collaborators analyze a standardized permutation-deletion channel and general code constructions, but deleting one permutation entry is not removing an entire paired chord [2]. Sala, Gabrys and Dolecek's *Deletions in Multipermutations* addresses a related deletion channel on repeated-symbol words [3]; only its abstract was accessible during this comparison, and the full text was not assessed for possible equivalent results. Exact matching of the domain and channel is essential: neither a generic deletion coding bound nor a crossing enumeration implies the stated \(7\)-codeword optimum, \(15/2\) fractional value and \(278\)-codebook count without an additional substantive reduction or computation.

## Limitations

The claim is restricted to at most four pairs on *linearly ordered* endpoints, with exactly one whole matched pair removed. It does not determine the capacities for larger orders or for arbitrary two-position deletion. A code correcting one erasure does not necessarily correct multiple erasures. The multiplicity \(278\) counts labeled codebooks, not equivalence under arbitrary vertex permutations. The fractional gap is an *integrality* gap: its floor still equals the integer optimum at four pairs. The inaccessible full text of [3] and potentially unindexed earlier finite enumerations remain priority risks. No external or independent mathematical audit is claimed.

## References

1. V. Pilaud and J. Rué, *Analytic Combinatorics of Chord and Hyperchord Diagrams with k Crossings*, arXiv:1307.6440 (first public version, 2013-07-24), https://arxiv.org/abs/1307.6440.
2. E. Gabrys et al., *Single-deletion-correcting codes over permutations*, ISIT 2014, DOI:10.1109/ISIT.2014.6875337, https://yaakobi.net.technion.ac.il/files/2015/04/40_Single_Deletion_Permutations_ISIT14.pdf.
3. F. Sala, R. Gabrys and L. Dolecek, *Deletions in Multipermutations*, ISIT 2014, DOI:10.1109/ISIT.2014.6875338. Full article text not inspected; only abstract and bibliographic material were accessible.
