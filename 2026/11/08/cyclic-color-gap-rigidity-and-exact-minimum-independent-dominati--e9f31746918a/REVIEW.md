# Scientific assessment of cyclic color-gap rigidity

## Correctness — PASS

The statement is quantified for all integers \(n\ge6\), \(q\ge3\), on the labelled *direct product* \(C_n\times K_q\). The proof's three-window inequality gives the sharp scalar lower bound and an explicit gap/color construction attains it. For minimum independent dominating sets the sum of all nonnegative window excesses is at most two. Any full occupied layer would create excess at least one in each of three windows, so no minimum set has a full layer; partial layers of size strictly between one and \(q\) are excluded separately by independence and domination. The remaining singleton layers form monochromatic positive runs of length at least two with a differently colored run on each side of every empty layer. The number of empty layers is forced to be \(k=\lfloor n/3\rfloor\); cyclic weak-composition counting and a proper-coloring trace yield the claimed exact formula. The boundary \(k=2\) is explicitly handled. Direct graph-based exhaustive tests on seven cases and \(786909\) tested vertex subsets corroborate every count; they do not replace the proof.

## Originality — PASS, with residual risk

Kuenzel and Rall (arXiv:2203.12397, Proposition 6) already give \(i(C_n\times K_q)=\lceil2n/3\rceil\); the earlier arXiv:1901.03218 provides the general layer-size characterization. Bakal and Mane (arXiv:2506.11865, Lemma 3.1 and Theorem 4.2) give a related three-layer domination argument and the scalar domination optimum. Jahari and Alikhani (arXiv:1808.07369) define the independent-domination polynomial and count other graph families. These known theorems overlap substantially with the proof's ingredients, and are acknowledged without claiming novelty for the minimum value or basic layer lemma. Neither the inspected full accessible accounts nor the targeted searches and comparison records supply the exact minimum-set multiplicity for every \(n\ge6\), \(q\ge3\), or classify all those extremizers as colored cyclic gaps. The risk of an unindexed equivalent enumeration, or an unstated direct specialization of the general weak-partition scheme, remains material but not presently decisive.

## Mathematical value — PASS

The precise count of optimum independent dominating sets is a natural next invariant after the published optimum cardinality for these graph products. It is not an arbitrary parameter slice: the theorem treats every sufficiently large cycle and every nontrivial clique factor with \(q\ge3\) and identifies the natural boundary where all optimal layers become singleton/empty. Its bijective classification exposes a change from a graph-product domination problem to a proper-coloring problem on a compressed cycle, explaining exponential numbers of extremizers and the three distinct residue-class factors in the exact formula. It does not claim the complete independent-domination polynomial, a classification of nonminimum maximal independent sets, or a general product-graph principle.

## Checked literature and limitations

The accessible article contents inspected were Kuenzel–Rall arXiv:2203.12397 (definitions, Section 3, Lemma 4, four weak-partition conditions, Table 1, Proposition 6 and proof); Kuenzel–Rall arXiv:1901.03218 (Section 3 and Lemma 9); Bakal–Mane arXiv:2506.11865 (Sections 3–4, Lemmas 3.1–3.2 and the scalar results); and Jahari–Alikhani arXiv:1808.07369 (definition and the independent-domination-polynomial families). A separate article on reconfiguration of minimum independent dominating sets of ordinary paths and cycles, arXiv:2303.08190, concerns different graphs. Further synonym searches used maximal independent sets, tensor/categorical product, chromatic-polynomial enumeration and optimum multiplicity; no directly covering statement was found. Negative search results are not a proof of historical novelty.

The statement excludes \(q=2\), small cycles, and symmetry-quotient counts. Publication priority remains provisional pending external specialist comparison. Finite experiments cannot replace the unrestricted proof.

Self-review: passed. Independent audit: not yet performed.
