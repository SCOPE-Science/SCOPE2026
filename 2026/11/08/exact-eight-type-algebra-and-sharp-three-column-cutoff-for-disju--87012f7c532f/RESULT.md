# Exact eight-type algebra and sharp three-column cutoff for disjunctive knowing-whether on two-row epistemic grids

## Finding
For every integer \(m\geq1\), let \(G_m\) be the two-agent \(\mathsf{S5}\) frame on \(\{0,1\}\times\{1,\ldots,m\}\), where the first agent identifies worlds in the same row and the second identifies worlds in the same column. Work in the Boolean language with one propositional letter \(p\) and one primitive bundled modality \(H\), interpreted by
\[
H\varphi:= (\Box_1\varphi\vee\Box_1\neg\varphi)\vee(\Box_2\varphi\vee\Box_2\neg\varphi).
\]
Two formulas are equivalent when they agree at every world for **every** valuation of \(p\) on \(G_m\). Let \(\mathcal A_m\) be the resulting formula Boolean algebra. Then
\[
|\mathcal A_m|=\begin{cases}4,&m=1,\\64,&m=2,\\256,&m\geq3.\end{cases}
\]
The number of distinct complete pointed formula theories is respectively \(2,6,8\). Every formula is equivalent on *all* these frames to one of \(H\)-depth at most two. Depth two is necessary as soon as \(m\geq2\), while depth zero suffices for \(m=1\). In particular, three is the sharp column threshold for stabilization of this formula algebra across the family.

## Assumptions and scope
The domain of \(G_m\) is finite and nonempty, with two rows and exactly \(m\) labelled columns. Agent 1's relation is equality of row coordinates and agent 2's is equality of column coordinates; both are reflexive equivalence relations. The language has arbitrary Boolean combinations, **one** propositional variable, and **only the single bundled operator** \(H\), not two separately available knowing-whether operators. Truth and equivalence are global over all \(2^{2m}\) valuations of \(p\) on that fixed frame. This is a statement about formula equivalence over a frame with varying valuations, not about the number of events generated under one fixed valuation.

Write a column's two truth bits as \(t\in\{0,1,2,3\}\), where bit \(r\in\{0,1\}\) is the truth value of \(p\) in row \(r\). For a valuation, let \(S\) be the nonempty set of column types occurring. Thus \(S\subseteq\{0,1,2,3\}\) and \(|S|\leq m\).

## Proof
**1. Support reduction (for every \(m\)).** A formula's truth at a world depends only on the column type \(t\), its row \(r\), and the support \(S\), not on the multiplicities or order of columns. Prove this by structural induction. It holds for \(p\) and Boolean operators. If the assertion holds for \(\varphi\), the row-equivalence class is uniform in \(\varphi\) precisely when all \(\varphi\)-values at \((S,u,r)\), for \(u\in S\), coincide. The column-equivalence class is uniform precisely when its two values at \((S,t,0)\) and \((S,t,1)\) coincide. These conditions are unaffected by repetition of identical column types. Every nonempty \(S\) of size at most \(m\) is realizable: list its types and duplicate one to fill the remaining columns. Hence formula equivalence on \(G_m\) is exactly agreement over
\[
\Omega_m=\{(S,t,r):\varnothing\ne S\subseteq\{0,1,2,3\},\ |S|\leq m,\ t\in S,\ r\in\{0,1\}\}.
\]
All these domains embed in the universal \(64\)-point test domain \(\Omega=\Omega_4\), since \(\sum_{S\ne\varnothing}2|S|=64\).

**2. Exact finite operator on the universal domain.** For \(X\subseteq\Omega\) define \(\widehat H(X)\) by
\[
(S,t,r)\in\widehat H(X)\ \Longleftrightarrow\
\bigl[\forall u\in S\ ((S,u,r)\in X\Leftrightarrow(S,t,r)\in X)\bigr]
\ \vee\
\bigl[((S,t,0)\in X)\Leftrightarrow((S,t,1)\in X)\bigr].
\]
This is exactly the semantics of \(H\) from step 1, including the cases \(|S|=1\). Let \(P\) be the set of all \((S,t,r)\) whose bit \(r\) in \(t\) is one. Set \(K=\widehat H(P)\), and consider the following five formulas, of respective depths \(0,1,2,2,2\):
\[
\Phi=(p,\ Hp,\ H(Hp),\ H(p\vee Hp),\ H(p\wedge\neg Hp)).
\]
Their bit-vector signatures on \(\Omega\) give exactly eight nonempty fibers, listed below. The final column is the smallest possible support cardinality for a world of that type.

| signature of \(\Phi\) | number of canonical points | least \(|S|\) | example \((S,t,r)\) with \(S\) written as a set |
|:---:|---:|---:|:---|
| 00001 | 2 | 2 | \((\{1,3\},1,1)\) |
| 00100 | 8 | 2 | \((\{1,2\},1,1)\) |
| 00101 | 2 | 3 | \((\{0,1,3\},1,1)\) |
| 01111 | 20 | 1 | \((\{0\},0,0)\) |
| 10010 | 2 | 2 | \((\{0,1\},1,0)\) |
| 10100 | 8 | 2 | \((\{1,2\},1,0)\) |
| 10110 | 2 | 3 | \((\{0,1,3\},1,0)\) |
| 11111 | 20 | 1 | \((\{1\},1,0)\) |

The table is an exhaustive finite calculation, not an infinite extrapolation. The reproducible operator definition and independent implementations are supplied in `support_checker.py`, `direct_checker.py`, and `closure_table.tsv`. In particular, the 256 rows of `closure_table.tsv` enumerate \(\widehat H\) on **every** Boolean union of the eight signature fibers, in lexicographic signature order. For each of the eight fibers and each input union, \(\widehat H\) contains either that entire fiber or none of it. This finite closure claim follows by enumerating the above explicit 64-element domain; `support_checker.py` regenerates every entry and checks it against the supplied table. Consequently the family of all unions of the eight fibers is closed under complement, intersections and \(\widehat H\), and contains \(P\). Conversely each fiber is defined by the conjunction of the appropriate five signed formulas in \(\Phi\), so every union of fibers is definable. These inclusions prove that the generated formula algebra on \(\Omega\) is exactly the powerset algebra of the eight fibers and that every formula has a depth-two representative.

**3. Sharp width and depth.** On \(\Omega_m\), a fiber appears if and only if its least support size in the table does not exceed \(m\). Thus \(\Omega_1\) has two types, \(\Omega_2\) has six, and \(\Omega_m\), for \(m\ge3\), has all eight. Because each type is definable by a Boolean combination of the formulas in \(\Phi\), the formula algebra on \(\Omega_m\) has precisely \(2^2,2^6,2^8\) elements. At modal depth zero only \(p\)'s value matters (two types). At modal depth at most one, the only additional information is \(Hp\), since \(H\top=H\bot=\top\) and \(H\neg p=Hp\): there are exactly four joint \((p,Hp)\)-types for every \(m\ge2\). Since six or eight types are attained only by depth two, the depth cutoff is sharp for those widths. For \(m=1\), each row class is a singleton, so \(H\varphi\) is always true and the depth-zero algebra is already complete.

## Verification
Run `python3 support_checker.py` alongside `closure_table.tsv`. It checks the \(64\)-point canonical reduction's finite part: the eight signature fibers, their sizes and minimum support widths, all \(256\) applications of \(\widehat H\) to unions of fibers, and the depth-one cardinality. Run `python3 direct_checker.py` separately. It enumerates all labelled valuations and worlds on grids of widths \(1,2,3,4\) (respectively \(8,64,384,2048\) pointed instances), evaluates the five formulas using **direct row/column coordinates** rather than canonical supports, and independently tests operator closure of the resulting classes. Both checks completed successfully from the stated file paths.

## Relationship to prior work
Ding and Yang's *A General Theory of Propositional Modal Bundled Modalities* (first posted March 27, 2026, arXiv:2603.26268), especially Sections 2–5 and the conclusion, develops general bundled semantics, bisimulations and axiomatizations, including someone-knows and non-contingency examples. Its operator \(\bigvee_a\Box_a\varphi\) is not the present \(\bigvee_a(\Box_a\varphi\vee\Box_a\neg\varphi)\), and its cited results do not give the above one-variable, two-row-grid algebra census. Hart, Heifetz and Samet's 1994 *Knowing Whether, Knowing That, and the Cardinality of State Spaces*, especially Sections 2 and 4, studies **separate** knowing-whether operators and shows much richer behavior on different information structures; it does not provide the disjunctively bundled grid cutoff. The present result also differs from existing full bimodal grid-algebra classifications, since neither operator is individually available in its syntax. No general undecidability or completeness claim is asserted.

## Limitations
The result depends on exactly two rows, full Cartesian product frames, one propositional letter and the particular disjunctive knowing-whether connective. It does not count formulas with separately available agent modalities, different numbers of rows, or arbitrary multi-agent frames. The last finite step uses a complete 256-case, 64-world computation: the infinite assertion additionally requires the independently stated support-reduction proof, not extrapolation from small grids. The publication-priority comparison is restricted to the identified texts and targeted searches; an equivalent finite-algebra computation in other literature remains possible. No independent external mathematical audit has been performed.

## References
1. Y. Ding and Y. Yang, *A General Theory of Propositional Modal Bundled Modalities*, arXiv:2603.26268 (first version March 27, 2026), DOI: 10.4204/EPTCS.447.17, Sections 2–6 and appendices. https://arxiv.org/abs/2603.26268
2. S. Hart, A. Heifetz and D. Samet, *Knowing Whether, Knowing That, and the Cardinality of State Spaces*, publicly listed April 10, 1994; Sections 2–4. https://econwpa.ub.uni-muenchen.de/econ-wp/game/papers/9404/9404002.pdf
3. Reproducible finite evidence supplied here: `support_checker.py`, `direct_checker.py`, `closure_table.tsv`.
