# A two-step normal form and exact many-letter noncontingency algebra on finite bicliques

## Finding

Fix any integer \(k\geq 2\), let \(C=\{0,1\}^k\) and \(q=|C|=2^k\). Over the class of all finite, **irreflexive complete bipartite** Kripke frames \(K_{m,n}\) with \(m,n\geq2\), allow arbitrary valuations of \(k\) proposition letters and arbitrary Boolean combinations and nestings of the sole modal operator \(\Delta\) (noncontingency, or knowing whether). The numbers of pointed semantic types distinguishable at modal depths zero, one and two are, respectively,
\[
 r_0=q,\qquad r_1=q(2^q-q),\qquad
 r_2=q+q\,2^{q-1}(2^q-q-1).
\]
These depth-two types are **complete**: no formula of greater depth separates any more pointed models. The exact numbers of formulas up to equivalence across **all** such pointed models are therefore \(2^{r_0}\), \(2^{r_1}\), and \(2^{r_2}\) at depths zero, one and at least two. The depth-two threshold is sharp for every \(k\geq1\), and a common witnessing frame of minimum coordinatewise size is \(K_{q,q}\): varying valuations on this fixed frame realizes every pointed semantic type, whereas no \(K_{m,n}\) with either side smaller than \(q\) realizes them all.

For two letters, \(q=4\) and the exact pointed-type profile is \(4,48,356,356,\ldots\), so there are \(2^{356}\) formula meanings. The one-letter boundary case also follows from the proof and has pointed-type profile \(2,4,6,6,\ldots\); the many-letter classification for \(k\geq2\), rather than this boundary case, is the claim of extension.

## Assumptions and scope

A frame has two nonempty vertex sides \(L,R\), accessibility exactly between different sides, no within-side edges or loops, and side sizes at least two. These minimum sizes place no restriction on how many different propositional truth vectors are used in a valuation: both sides may be monochromatic. For every pointed model \((M,w)\), let \(c\in C\) be the atomic truth vector at \(w\); let \(S\subseteq C\) be the nonempty set of vectors realized on the side of \(w\), and \(T\subseteq C\) the nonempty set realized on the opposite side. Necessarily \(c\in S\). The multiplicities of colors are not recorded.

The language has the \(k\) Boolean-valued propositional letters, truth-functional negation, conjunction (and hence all finite Boolean operations), with
\[
 M,w\models\Delta\varphi\quad\Longleftrightarrow\quad
 \forall u,v\,(wRu\wedge wRv\Rightarrow (M,u\models\varphi\iff M,v\models\varphi)).
\]
Modal depth counts nested occurrences of \(\Delta\). Two formulas are equivalent when they agree at every designated world of every valuation on every frame in the stated class; the counts do not concern syntactic formulas, pointed-model isomorphisms, or the ordinary necessity language.

For nonempty \(U\subseteq C\) define the *homogeneity descriptor*
\[
 [U]=\begin{cases}*,&|U|=1,\\ U,&|U|\geq2,\end{cases}
\]
where \(*\) is a formal symbol different from every subset. Define the normal form
\[
 \nu(c,S,T)=\begin{cases}
 (c,*,*),&|T|=1,\\
 (c,T,[S]),&|T|\geq2.
 \end{cases}
\]
All displayed descriptors are realized by finite models in the class.

## Proof

**1. Colors and the first modal layer.** Every Boolean formula with no modal operators is a function \(f:C\to\{0,1\}\), and every such function is definable as a Boolean combination of the \(k\) atomic letters. Thus depth zero distinguishes exactly \(q\) colors.

At a world with opposite-side color support \(T\), \(\Delta f\) holds iff \(f\) is constant on \(T\). If \(|T|=1\), every depth-one modal atom \(\Delta f\) is true. If \(|T|\geq2\), for each \(a\in C\) let \(\chi_a\) be the Boolean minterm identifying color \(a\). Then
\[
 \neg\Delta\chi_a\quad\Longleftrightarrow\quad a\in T\qquad(|T|\geq2).
\]
The complete first-layer theory is therefore exactly \((c,[T])\). There are \(1+(2^q-q-1)=2^q-q\) possible successor descriptors for each current color, giving \(r_1=q(2^q-q)\). Its Boolean-definable characteristic formulas can be constructed from \(\chi_c\) and the finite family \(\Delta\chi_a\).

**2. Recovering the reverse side at depth two.** Suppose \(|T|\geq2\). Choose any \(a\in T\). The Boolean minterm \(\chi_a\) is not constant on \(T\). For any \(b\in C\), at every opposite-side world \(u\), the formula \(\Delta\chi_b\) has a single common truth value \(h_b\), because every such \(u\) has the *same* successor support \(S\); moreover \(h_b=1\) exactly when \(\chi_b\) is constant on \(S\). Consequently at the original world,
\[
 \Delta(\chi_a\wedge\Delta\chi_b)\quad\Longleftrightarrow\quad h_b=0.
\]
Indeed, if \(h_b=0\), the inner conjunction is false everywhere on \(T\), whereas if \(h_b=1\), it varies as \(\chi_a\), which is nonconstant on \(T\). The collection of these depth-two truth values detects \([S]\) exactly: when \(|S|=1\), they are all false; when \(|S|\geq2\), the formula is true precisely for \(b\in S\). Thus depth two separates all different \(\nu(c,S,T)\) with \(|T|\geq2\).

If \(|T|=1\), all opposite-side worlds have the same atomic color and see the same support \(S\), and hence satisfy the same formulas by structural induction. Every \(\Delta\psi\) is therefore true at the original world, for *all* formulas \(\psi\). Only the local atomic color \(c\) remains observable. This proves precisely the first branch of \(\nu\).

**3. Arbitrary nesting cannot add distinctions.** Consider any two pointed models with the same \(\nu\). For \(|T|=1\), every modal atom at the current point is true, regardless of the inner formula, as above. For \(|T|\geq2\), the sets of successor \(\nu\)-types are determined solely by the descriptor:
\[
 \left\{\nu(d,T,S):d\in T\right\}.
\]
If \(|S|=1\), all these successors have descriptor \((d,*,*)\); if \(|S|\geq2\), each has descriptor \((d,S,[T])\). The latter data are uniquely determined by the current \((c,T,[S])\), including the singleton branch \([T]\) when necessary. Therefore, assuming a subformula has the same truth value on corresponding \(\nu\)-types, its homogeneity or non-homogeneity among successors is also equal. Boolean induction now shows **every** formula has constant truth on each \(\nu\)-class. Step 2 proves that distinct classes are separated by depth-two formulas. Hence the normal form is exact and stable at depth two.

**4. Exact counting and all formula meanings.** For each of the \(q\) current colors, there is one descriptor \((c,*,*)\). For every non-singleton \(T\), of which there are \(2^q-q-1\), there are \(1+(2^{q-1}-1)=2^{q-1}\) choices for \([S]\), since a non-singleton \(S\) must contain the designated color \(c\). Thus
\[
 r_2=q+q(2^q-q-1)2^{q-1}.
\]
All classes are mutually distinguishable by finitely many depth-at-most-two formulas. Because there are finitely many classes, a finite conjunction of separators (using negations as needed) isolates any one class. Taking disjunctions produces every subset of the \(r_2\) classes at depth at most two, proving the formula-algebra cardinality \(2^{r_2}\). The analogous argument at depths zero and one gives \(2^{r_0}\) and \(2^{r_1}\).

**5. Sharpness and least common frame.** For \(q\geq2\), fix a current color \(c\), choose \(d\ne c\), and choose a non-singleton opposite support \(T\). The two configurations \(S=\{c\}\) and \(S=\{c,d\}\) agree at depth one but are distinguished by step 2 at depth two; thus the threshold is sharp. Any descriptor can be realized on \(K_{q,q}\): assign colors to its two sides so that their supports are exactly \(S,T\), repeating colors when needed to fill \(q\) vertices, and designate a vertex of color \(c\). Conversely the descriptor \((c,C,C)\) occurs and requires at least \(q\) distinct colors in both sides simultaneously, hence at least \(q\) vertices on each side. The fixed frame \(K_{q,q}\) is therefore coordinatewise minimal for realizing the full pointed-theory spectrum, as claimed.

## Verification

Run `python3 verify.py` (Python 3 standard library only). The symbolic checker explicitly enumerates every nonempty ordered support pair \((S,T)\) and each designated \(c\in S\), builds successor supports from the exact bipartite semantics, and refines the all-valuation pointed-type partition at successive modal depths. It verifies profiles \((2,4,6,6,6)\), \((3,15,51,51,51)\), and \((4,48,356,356,356)\) for alphabets of sizes two, three, and four, including the depth-two normal-form equivalence. The three-color computation is an additional abstraction test, not a separate number of Boolean propositional letters. A second routine independently enumerates every valuation on all \(K_{m,n}\) with \(1\leq m,n\leq3\), for two- and three-color alphabets, checks actual graph successor sets, and confirms the claimed partitions and their stable depth. Its outputs are recorded in `VERIFICATION.md`. These finite experiments corroborate the proof but cannot by themselves establish the all-\(k\) theorem.

## Relationship to prior work

The recent work of Wang and Zenger develops general proof theory of noncontingency using frame conditions. It supplies the semantics and motivation but its publicly accessible abstract does not state a finite biclique \(k\)-letter normal form, sharp depth-two collapse, or the exact formula-algebra counts; a complete paper text could not be inspected and remains an access-related priority risk.

Two closely relevant previously published quantitative classifications were inspected in full: *Exact pointed-theory spectrum and optimal tests for non-contingency stars* treats any number of letters but **terminal** successors and proves only depth-one collapse; *Ten knowing-whether types versus twenty-two necessity types on complete multipartite frames* treats arbitrary multipartite frames but **one** letter, proving ten noncontingency pointed types. The first does not include the mutually observing sides of a biclique, and the second does not cover the multiple-letter classification here. The known one-letter complete-graph six-type result applies to **irreflexive cliques**, not the many-letter complete bipartite family. The present exact many-letter two-sided normal form uses both established semantic ideas but its reverse-side detection and all-parameter count are not consequences of those published theorems as stated.

General results on noncontingency bisimulation and Boolean modal algebras supply methods, not the precise count. In particular this finding does **not** assert novelty of the standard fact that color multiplicities can be invisible or of Boolean partition refinement.

## Limitations

The frame class consists only of **finite irreflexive bicliques with both nonempty sides of size at least two**, the language contains \(\Delta\) but not ordinary \(\Box\), and valuations may use any \(k\) truth assignments independently at each world. The theorem is not about arbitrary multipartite graphs, added modalities, restricted valuation families, or actual truth-value multiplicities. The frame \(K_{q,q}\) is universal for *pointed types under varying valuations*, not a claim that one valuation realizes all types simultaneously. The one-letter boundary case is included for mathematical completeness, not independently asserted new. A recent preprint is only abstract-inspected, and an equivalent older modal/coalgebraic normal form may be unindexed. Independent mathematical and historical-priority audits are not performed.

## References

1. Yunsong Wang and Lukas Zenger, *Proof Theory for Non-Contingency Logic*, arXiv:2609.38975, first public September 30, 2026. https://arxiv.org/abs/2609.38975.
2. Lloyd Humberstone, *The Modal Logic of Agreement and Noncontingency*, Notre Dame Journal of Formal Logic 43 (2002), DOI:10.1305/ndjfl/1071509431. https://doi.org/10.1305/ndjfl/1071509431.
3. Jie Fan, Yanjing Wang and Hans van Ditmarsch, *Contingency and Knowing Whether*, Review of Symbolic Logic, DOI:10.1017/S1755020314000343.
4. *Exact pointed-theory spectrum and optimal tests for non-contingency stars* (2026), full published result at https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-pointed-theory-spectrum-and-optimal-tests-for-non-continge--f721419c88bd.
5. *Ten knowing-whether types versus twenty-two necessity types on complete multipartite frames* (2026), full published result at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-ten-knowing-whether-types-versus-twenty-two-necessity-types-on-c--9064d486ef99.
6. *A sharp depth-two collapse of one-variable non-contingency logic on irreflexive cliques* (2026), full published result at https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-a-sharp-depth-two-collapse-of-one-variable-non-contingency-logic--000da32ebd0d.
