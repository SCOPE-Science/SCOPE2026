# Exact rational census of inclusion-minimal super domination on paths

## Finding

For each integer \(n\geq 1\), let \(a_n\) be the number of inclusion-minimal super-dominating vertex sets of the labelled path \(P_n\). Put \(a_0=1\) as a formal empty-path boundary convention. Then the exact ordinary generating function is

\[
\sum_{n\geq0}a_n z^n=
\frac{1+z+2z^2+2z^3+z^5-2z^6-2z^7-2z^8-z^9+z^{10}+z^{11}}
{1-z^3-z^4-2z^5-2z^6-z^7+z^8+2z^9+z^{10}}.
\]

Equivalently, for every integer \(n\geq12\),

\[
a_n=a_{n-3}+a_{n-4}+2a_{n-5}+2a_{n-6}+a_{n-7}-a_{n-8}-2a_{n-9}-a_{n-10},
\]

with \((a_0,a_1,\ldots,a_{11})=(1,1,2,3,2,6,7,10,16,21,32,47)\). Thus, for instance, \((a_{12},\ldots,a_{20})=(67,99,142,206,302,438,637,925,1342)\).

## Assumptions and scope

The path \(P_n\) has vertex set \(\{1,2,\ldots,n\}\) and edges \(\{\{i,i+1\}:1\leq i<n\}\), and is treated as a labelled graph. For any finite simple graph \(G=(V,E)\), a vertex set \(S\subseteq V\) is *super dominating* if for every \(v\in V\setminus S\) there is an adjacent \(u\in S\) with \(N(u)\cap(V\setminus S)=\{v\}\). It is *inclusion-minimal* if deleting any one of its vertices destroys super domination. This is a minimal-by-inclusion condition, not a minimum-cardinality requirement.

For \(T=V\setminus S\), say that \(T\) is *open irredundant* if each \(v\in T\) has a neighbour \(u\in V\setminus T\) with \(N(u)\cap T=\{v\}\). Since this condition survives deletion from \(T\), a set \(S\) is inclusion-minimal super dominating if and only if \(T\) is an inclusion-maximal open-irredundant set. This equivalence follows directly from the quantifiers and does not rely on any unproved graph parameter identity.

## Proof

Encode \(T\) by a word \(t_1\ldots t_n\) in \(\{0,1\}^n\), with \(t_i=1\) exactly when \(i\in T\). Write \(\bot\) for a position outside the path. A selected position \(i\), with \(t_i=1\), has a private neighbouring witness if and only if at least one of the following holds:

\[
(t_{i-1}=0\ \mathrm{and}\ t_{i-2}\in\{0,\bot\})
\quad\mathrm{or}\quad
(t_{i+1}=0\ \mathrm{and}\ t_{i+2}\in\{0,\bot\}).
\]

Both neighbouring and second-neighbouring positions outside the path are interpreted as \(\bot\); an out-of-path neighbour itself is never equal to zero. Hence admissibility of the current word is a radius-two condition. For a zero position \(i\), maximality means that switching \(t_i\) from zero to one makes the new word inadmissible. Only the witness status of positions at distance at most two from \(i\) can change. Consequently both admissibility and maximality at a central position are decided by the nine entries from offset minus four through plus four.

Here is an exact finite-state construction, fully specified by the companion standalone script `verify_path_census.py`. Start with eight copies of \(\bot\). Each step appends a bit from \(\{0,1\}\) to the current eight-symbol suffix and accepts the resulting nine-symbol window exactly when its central position satisfies the preceding local admissibility and maximality tests. Retain only the last eight symbols. After all \(n\) ordinary positions have been appended, append four \(\bot\) symbols using the same test. The number of surviving suffix paths is precisely \(a_n\). Early and late \(\bot\) symbols implement both boundaries, including \(n=0\) and \(n=1\).

Let \(D_n(s)\) denote the number of accepted prefixes after \(n\) bit appends that end in eight-symbol state \(s\), starting from \(\bot^8\). The single-bit extension is a fixed integer linear operator \(A\) on suffix-state vectors, so \(D_{n+1}=AD_n\). Define

\[
Q(z)=1-z^3-z^4-2z^5-2z^6-z^7+z^8+2z^9+z^{10}.
\]

An exhaustive exact-integer state calculation establishes that the vector

\[
D_{18}-D_{15}-D_{14}-2D_{13}-2D_{12}-D_{11}+D_{10}+2D_9+D_8
\]

is identically zero at **every reachable eight-symbol state**. The check enumerates 111 states of \(D_{18}\), constructs the union of supports of all nine contributing vectors, and checks each coordinate, not just the sum of coordinates. Because \(A\) is fixed and linear, applying \(A\) repeatedly proves the same vector identity at every index \(n\geq18\). The four-\(\bot\) finishing procedure is a fixed linear functional, so the corresponding scalar identity holds for all \(n\geq18\). The script directly verifies that identity also for \(12\leq n\leq17\), and obtains the displayed first twelve values by exact enumeration of the same automaton. Multiplication of their generating series by \(Q(z)\) gives the numerator displayed above, and the identity proves all its later coefficients vanish. This establishes the theorem for every \(n\geq0\).

## Verification

Run `python3 verify_path_census.py` with Python 3 and no third-party libraries. The code prints `EXACT_INTEGER_VECTOR_RECURRENCE_PASS` after checking the all-state certificate; `RATIONAL_GENERATING_FUNCTION_COEFFICIENTS_PASS` after checking the numerator; and `VERIFY_OK` only after its remaining checks pass. In addition, a separately coded literal graph test exhaustively checks all \(2^n\) subsets for every \(0\leq n\leq15\), directly testing the super-domination condition and the failure of every single-vertex deletion. This independent finite computation corroborates the automaton; the **infinite** conclusion rests on the all-state recurrence identity and its linear propagation, not on bounded sampling. The script also checks the recurrence at \(19\leq n\leq74\) as an extra consistency test.

## Relationship to prior work

Alikhani and Ghanbari, *Super Coalition Number in Graphs* (first public version 15 July 2026), motivate the study of rigid super domination on paths and other standard graphs; their coalition-partition parameter is distinct from the exact count of inclusion-minimal super dominating sets computed here. Cockayne, Favaron, Finbow and Mynhardt (2008) establish general maximal open-irredundance criteria and bounds, but no exact all-orders path counting function was identified in the inspected material. The published eight-state recurrence for **all** super-dominating sets of forests was inspected in full; its cardinality polynomial counts a wider family but does not provide the inclusion-minimal filtering or the path-only series. The published inclusion-minimal census of labelled cycles was also inspected in full: its unweighted transfer denominator is the same as the denominator here, so the denominator itself is not independently claimed as a discovery. Its cyclic logarithmic-derivative formula does not state or imply the present **path boundary numerator** without a separate endpoint analysis. A subsequent preprint by Avella-Alaminos, Lemańska and Zuazua (first posted 17 November 2026, subsequently to the motivating 2026 paper) discusses extremal sizes of minimal super-dominating sets of paths and complementary irredundance, not the complete number of such sets.

## Limitations

The theorem counts minimal sets **without** recording their cardinalities, is limited to labelled paths and their formal empty boundary, and makes no corresponding universal claim for arbitrary trees. An earlier unlocated exact enumeration under equivalent terminology remains a possible historical-priority risk; a negative search is not a proof of novelty. The finite-state identity is an exact computational certificate: its reproducibility depends on executing and inspecting the bundled plain-Python checker. No independent mathematical audit is claimed.

## References

- S. Alikhani and N. Ghanbari, *Super Coalition Number in Graphs*, arXiv:2607.22686, initial posting 2026-07-15, https://arxiv.org/abs/2607.22686.
- E. J. Cockayne, O. Favaron, S. Finbow, C. M. Mynhardt, *Open irredundance and maximum degree in graphs*, Discrete Mathematics 308 (2008), 5358–5375, https://doi.org/10.1016/j.disc.2007.10.002.
- Published full super-domination polynomial for forests, *An explicit eight-state enumerator for all super-dominating sets of forests* (2026-10-12), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-an-explicit-eight-state-enumerator-for-all-super-dominating-sets--dcd6d20229b7.
- Published minimal super-domination census for labelled cycles, *Inclusion-minimal super domination on cycles: a five-gap census and sharp seven-period upper spectrum* (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-inclusion-minimal-super-domination-on-cycles-a-five-gap-census-a--16bec2bc3654.
- D. Avella-Alaminos, M. Lemańska and R. Zuazua, *Minimal super dominating sets of maximum cardinality*, arXiv:2611.23464, initial posting 2026-11-17 (subsequent comparison only), https://arxiv.org/abs/2611.23464.
