# Permutation-block bases for one-point-extension rank in coloured finite orders

## Finding

Let \(q\ge 1\) and let \(\Sigma\) be a fixed, named alphabet of exactly \(q\) colours. Regard a finite strictly ordered structure with disjoint exhaustive unary colours as a word \(w\in\Sigma^*\); a coloured induced suborder is a scattered subsequence. Let \(\operatorname{rk}(w)\) be the Kubiś–Shelah one-point-extension rank of the empty marked structure relative to the hereditary class of these words.

Define the finite recursive word families
\[
\mathcal E_0=\{\varepsilon\},\qquad
\mathcal E_{t+1}=\{u\pi v:u,v\in\mathcal E_t,\ \pi\text{ a permutation of all }q\text{ colours}\}.
\]
Here a permutation is a length-\(q\) word containing each named colour once. For every integer \(t\ge 0\),
\[
\boxed{\operatorname{rk}(w)\ge t\quad\Longleftrightarrow\quad
\exists e\in\mathcal E_t\ \text{such that }e\text{ is a scattered subsequence of }w.}
\]
The \(\mathcal E_t\) are *exactly* the minimum-order rank-\(t\) hosts: they have common length
\[
\boxed{N_t=q(2^t-1),\qquad |\mathcal E_t|=(q!)^{2^t-1}.}
\]
Each has exactly \(2^t-1\) occurrences of every named colour; their mutual non-embeddability at the same length makes \(\mathcal E_t\) the exact minimal induced-suborder basis of the rank-at-least-\(t\) class. Consequently the maximum rank of any \(n\)-point \(q\)-coloured order is
\[
\boxed{\left\lfloor\log_2(1+n/q)\right\rfloor.}
\]
In particular, there are \(128\) minimum \(14\)-point hosts at rank \(3\) on two named colours, and \(216\) minimum \(9\)-point hosts at rank \(2\) on three named colours.

## Assumptions and scope

The ambient class includes the empty structure and words omitting some colours, so it is hereditary; the *palette*, not the colours occurring in one host, is fixed. Embeddings preserve order and every named unary predicate. A marked substructure \(F\subseteq w\) consists of selected positions, with induced colour/order. Rank is defined by the successor recursion: \(\operatorname{rk}_{w}(F)\ge0\) always, and \(\operatorname{rk}_{w}(F)\ge k+1\) if, for **each** one-point extension type \(F\cup\{a\}\) permitted by the ambient class, **some** realization in \(w\setminus F\) has relative rank at least \(k\). For finite hosts the rank is finite. There are exactly \(q(|F|+1)\) possible extension types: choose one of the gaps determined by the marked points and one named colour.

For a finite word \(g\), define its interval rank \(R(g)\) recursively by
\[
R(g)=\begin{cases}
0,&\text{if at least one colour of }\Sigma\text{ is absent from }g,\\[2pt]
1+\displaystyle\min_{c\in\Sigma}\ \max_{j:g_j=c}\ \min\bigl(R(g_{<j}),R(g_{>j})\bigr),&\text{otherwise}.
\end{cases}
\]
The maximum is over positions with colour \(c\); the second case has nonempty such sets. If the marked positions of \(F\) cut \(w\) into the \(|F|+1\) (possibly empty) unmarked gap words \(g_0,\ldots,g_{|F|}\), then
\[
\boxed{\operatorname{rk}_{w}(F)=\min_{0\le i\le|F|}R(g_i).}
\]
This identity is a component of the theorem and computes ranks for *every* marked induced substructure, not only the empty one.

## Proof

**1. Relative-rank decomposition.** We induct simultaneously on the finite depth \(k\). At depth zero the rank lower bound holds for every marked structure, as does \(R(g)\ge0\). Assume the claimed equivalence at depth \(k\). A one-point extension type over \(F\) specifies exactly a marked gap \(i\) and a colour \(c\). If a position \(j\) of that colour is chosen inside \(g_i\), it splits that gap into the prefix \((g_i)_{<j}\) and suffix \((g_i)_{>j}\). The other gap words are unchanged. Thus the relative rank after realizing the extension is at least \(k\) precisely when both resulting subgap words have rank at least \(k\) and the other old gaps do as well. Requiring this for every pair \((i,c)\) gives precisely \(R(g_i)\ge k+1\) for all \(i\). To see the equivalence explicitly, if all old gaps have rank at least \(k+1\), they each also have rank at least \(k\), and every extension type is independently realizable with both split subgaps at least \(k\). Conversely, if every extension type can be so realized, fix an old gap and colour; its qualifying realization forces that gap to satisfy the depth-\(k+1\) recurrence. The induction therefore proves \(\operatorname{rk}_{w}(F)=\min_iR(g_i)\); for \(F=\varnothing\) there is a single gap \(w\), so \(\operatorname{rk}(w)=R(w)\).

**2. Monotonicity.** If \(a\) is a scattered subsequence of \(b\), then \(R(a)\le R(b)\). This follows directly by induction on the rank depth: for each colour, any witness pivot in \(a\) corresponds to one in \(b\), with superwords on both sides; the induction preserves both required lower bounds. It also follows from the one-point-extension game by transferring witnessing realizations along the embedding.

**3. Basis equivalence.** We induct on \(t\). At \(t=0\), the empty word is a scattered subsequence of every word and all ranks are at least zero. Assume the statement at \(t\). If \(R(w)\ge t+1\), then, for every colour \(c\), there is a position \(j_c\) of that colour such that \(R(w_{<j_c})\ge t\) and \(R(w_{>j_c})\ge t\). These \(q\) pivot positions are pairwise distinct. Let \(a\) and \(b\) be their leftmost and rightmost positions. The prefix before \(a\) has rank at least \(t\), as does the suffix after \(b\). The induction hypothesis places a member \(u\in\mathcal E_t\) in the prefix and a member \(v\in\mathcal E_t\) in the suffix. Reading the \(q\) distinct pivot positions in their order produces a permutation word \(\pi\), between \(u\) and \(v\). Hence \(u\pi v\in\mathcal E_{t+1}\) embeds in \(w\).

Conversely, suppose \(w\) contains \(u\pi v\in\mathcal E_{t+1}\). For any named colour \(c\), take the position representing \(c\) in the embedded central permutation \(\pi\). Its left context contains \(u\) and its right context contains \(v\). By induction and monotonicity, both contexts have interval rank at least \(t\). Such a witness exists for every \(c\), so the recurrence yields \(R(w)\ge t+1\). This completes the all-size equivalence.

**4. Exact extremizers and count.** Every element of \(\mathcal E_0\) has length zero; the recursion adds two words of length \(N_t\) and a central word of length \(q\), hence \(N_{t+1}=2N_t+q\). Thus \(N_t=q(2^t-1)\). The basis equivalence says no host shorter than \(N_t\) can have rank at least \(t\), and all \(\mathcal E_t\) hosts do. A minimum host of length \(N_t\) containing one of these words must equal that word, since an equal-length scattered subsequence is the whole word. At fixed length \(N_{t+1}\), the first \(N_t\) positions, central \(q\) positions and final \(N_t\) positions uniquely determine \(u,\pi,v\); therefore, with \(A_t=|\mathcal E_t|\), we have \(A_0=1\) and \(A_{t+1}=q!A_t^2\). Solving gives \(A_t=(q!)^{2^t-1}\). Each colour appears once in every central permutation and twice recursively on the flanks, so its multiplicity is \(2^t-1\). The rank-at-least-\(t\) family is upward closed under induced embeddings, and every one of its minimum-length members is in \(\mathcal E_t\); since every rank-at-least-\(t\) word contains one of these members, \(\mathcal E_t\) is its complete minimal induced-suborder basis. Finally, for each \(n\ge N_t\), extending a basis word by arbitrary coloured points yields a host of size \(n\) and rank at least \(t\); for \(n<N_{t+1}\), no rank \(t+1\) is possible. This gives the displayed floor-logarithm formula. \(\square\)

## Verification

`verify_colored_rank.py` implements the abstract one-point-extension game on **every marked subset** of each tested word independently from the substring recurrence. It checks all words through length \(10\) on one colour, through length \(9\) on two colours, and through length \(6\) on three colours (2,127 host words in total); enumerates minimum-size hosts and compares them to the grammar; tests the scattered-subsequence criterion across 69,029 cases; and checks 180 larger constructive examples. The successful terminal condition is `ALL_CHECKS_OK`. The enumeration provides finite corroboration only: all unbounded quantifiers are discharged by the proof, not by computation.

A straightforward substring dynamic program evaluates \(R(w)\) in \(O(n^3+qn^2)\) time and \(O(n^2+q)\) auxiliary space: compute shorter intervals first and scan each colour's potential pivots in each interval.

## Relationship to prior work

López-Callejas and Navarro-Castillo (arXiv:2604.14461, initially available 15 April 2026) define the underlying one-point-extension rank, prove the interval characterization and calculate the uncoloured finite-order case \(\lfloor\log_2(n+1)\rfloor\) (Section 6). The present result recovers that case when \(q=1\), but the palette-dependent recursive minimal basis and its \((q!)^{2^t-1}\) extremal multiplicity are not given by the uncoloured size-only theorem.

Mwesigye and Truss, *On Optimal Representatives of Finite Coloured Linear Orders* (first published 2 May 2018), study **two-sided** Ehrenfeucht–Fraïssé equivalence of pairs of coloured orders. Their shortest representatives for a fixed first-order equivalence theory solve a different minimization problem; neither their \(q^2+2q\) two-move result nor their three-move constructions imply the present **one-sided** extension rank. The shared interval and colour language is not an identification of these distinct games.

The recursive families are a natural complete induced-suborder obstruction/basis description for an upward-closed rank property, not merely an upper bound on word length. No claim is made that the related first-order equivalence literature exhausts all earlier work on one-point ranks.

## Limitations

All statements are for **finite** words and a **fixed nonempty finite palette** of *named* colours, including possible unused palette colours in the host. They do not describe countably infinite coloured orders, variable or unnamed colours, coloured posets, arbitrary ternary relations, or two-structure Ehrenfeucht–Fraïssé equivalence. The rank classification uses a finite family of potentially enormous size and does not promise polynomial-time listing of that family; the separate dynamic program computes rank without listing it. Independent mathematical verification and exhaustive historical priority review have not been performed. Some unindexed literature could contain equivalent formulations; originality is relative to the inspected sources and available searchable records.

## References

1. C. López-Callejas and J. Navarro-Castillo, *A rank function for Fraïssé classes and the rank property*, arXiv:2604.14461, first version 2026-04-15, https://arxiv.org/abs/2604.14461. Particularly Definition 2.3 and Section 6.
2. F. Mwesigye and J. K. Truss, *On Optimal Representatives of Finite Coloured Linear Orders*, *Order* 36 (2019), 107–117, online 2018-05-02, https://doi.org/10.1007/s11083-018-9458-3; lawful open text at https://eprints.whiterose.ac.uk/id/eprint/129275/.
3. W. Kubiś and S. Shelah, *Ranks on evolution systems* (2024), cited for the general rank framework in Reference 1; no unverified claim about its coverage of finite coloured words is used here.
