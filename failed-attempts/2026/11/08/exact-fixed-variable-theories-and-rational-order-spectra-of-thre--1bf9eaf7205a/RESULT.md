# Exact fixed-variable theories and rational order spectra of threshold graphs

## Finding

Let \(\mathcal T\) be the class of all nonempty finite simple undirected threshold graphs in the pure adjacency-and-equality language, without counting quantifiers. A threshold graph is obtainable from one vertex by successively adjoining vertices that are either adjacent to all existing vertices or to none. For each graph with at least two vertices, iteratively delete **all** universal vertices of the current induced graph if any exist, and otherwise delete **all** isolated vertices. Write the successive nonempty blocks, from outside inward, as
\[
\mathcal P(G)=((\epsilon_1,b_1),\ldots,(\epsilon_h,b_h)),
\qquad \epsilon_i\in\{U,I\},\quad b_i\ge1.
\]
This canonical list has alternating signs and final block size \(b_h\ge2\). For the one-vertex graph set \(\mathcal P(G)=\star\).

**Classification.** For every integer \(k\ge2\) and any \(G,H\in\mathcal T\),
\[
G\equiv_{\mathrm{FO}^k}H
\quad\Longleftrightarrow\quad
\mathcal P_k(G)=\mathcal P_k(H),
\]
where \(\mathcal P_k\) replaces each block size \(b_i\) by \(\min\{b_i,k\}\), leaving its sign and position unchanged, while \(\star\) is a separate signature. Equivalence is at **unrestricted quantifier depth**. For \(k=1\), all members of \(\mathcal T\) are equivalent.

**Exact theory and size spectra.** For a prescribed positive block count \(h\), there are exactly
\[
2(k-1)k^{h-1}
\]
logical theories (plus the singleton theory with no blocks). Every theory has a unique smallest representative within \(\mathcal T\), up to isomorphism, obtained by truncating every size at \(k\). Put
\[
A_j(z)=\sum_{s=1}^{j}z^s,\qquad B_j(z)=\sum_{s=2}^{j}z^s,
\qquad B_1(z)=0.
\]
If \(r_k(n)\) counts theories whose smallest representative has exactly \(n\) vertices, then
\[
R_k(z):=\sum_{n\ge1}r_k(n)z^n
=z+\frac{2B_k(z)}{1-A_k(z)}.
\]
If \(u_k(n)\) counts theories that admit *some* threshold-graph representative on exactly \(n\) vertices, define
\[
T_k(z):=z+\frac{2B_{k-1}(z)}{1-A_{k-1}(z)}.
\]
Then
\[
U_k(z):=\sum_{n\ge1}u_k(n)z^n
=T_k(z)+\frac{R_k(z)-T_k(z)}{1-z}.
\]
In particular, for \(k=2\), with \(F_1=F_2=1\) the Fibonacci numbers, one has
\[
r_2(1)=u_2(1)=1,\qquad
r_2(n)=2F_{n-1},\qquad u_2(n)=2(F_{n+1}-1)\quad(n\ge2).
\]
The hierarchy is strict for every successive variable width, including the passage from one to two variables.

## Assumptions and scope

All structures are finite, nonempty, undirected, simple and uncolored; \(E\) denotes adjacency. The definition of \(\mathrm{FO}^k\) permits arbitrarily deep quantifiers but at most \(k\) distinct reusable first-order variable names, and has no counting quantifiers or parameters. Logical equivalence and minimal representatives are *relative to threshold graphs*, not to all finite graphs. The graph order \(n\) and the variable bound \(k\) are positive integers as specified above. The empty graph is excluded.

## Proof

**1. Canonical extremal peeling.** The standard extremal-vertex characterization says that every nonempty threshold graph contains an isolated or dominating vertex, and deleting one such vertex leaves a threshold graph; see Reilly--Scheinerman, Theorem 2.7. In a graph with at least two vertices, a universal and an isolated vertex cannot coexist. Therefore the full set of universal vertices or the full set of isolated vertices is uniquely selected. Each induced residue is threshold. Two successive nonempty blocks cannot have the same sign: a universal vertex of the residue immediately after deleting a universal block would already have been universal before deletion; similarly for isolated blocks. A final isolated singleton cannot remain after an earlier block, since its adjacency to the immediately preceding block would make it another vertex of that same extreme block. Hence the final block has size at least two. Conversely, any alternating signed list with positive block sizes and final size at least two gives a unique threshold graph up to isomorphism: build its innermost clique (if \(U\)) or independent set (if \(I\)) and add earlier blocks as complete joins with cliques (\(U\)) or disjoint unions with independent sets (\(I\)). Thus \(\mathcal P\) is an isomorphism invariant and a normal form. In particular, adjacency of distinct vertices depends only on their blocks: within a block it is the indicator of \(U\); between different blocks it is the indicator that the *earlier* block is \(U\).

**2. Recovering the block word by two-variable formulas.** The singleton is separated by \(\neg\exists x\exists y\,(x\ne y)\). For graphs with at least two vertices, define \(Q_0(x):=(x=x)\). Once a sign \(\epsilon_i\) and the remainder predicate \(Q_i(x)\) are known, set
\[
\begin{aligned}
D_i(x)&:=Q_i(x)\wedge\forall y\,[Q_i(y)\Rightarrow(x=y\lor E(x,y))],\\
Z_i(x)&:=Q_i(x)\wedge\forall y\,[Q_i(y)\Rightarrow\neg E(x,y)],\\
L_i(x)&:=\begin{cases}D_i(x),&\epsilon_i=U,\\Z_i(x),&\epsilon_i=I,\end{cases}\\
Q_{i+1}(x)&:=Q_i(x)\wedge\neg L_i(x).
\end{aligned}
\]
All these unary predicates use only the two names \(x,y\); when substituting \(Q_i(y)\), its internally bound variable is renamed to \(x\), with standard capture avoidance. The corresponding formulas are finite for every fixed \(i\). The first sign is determined by which one of \(\exists x\,D_0(x)\) and \(\exists x\,Z_0(x)\) holds. Induction recovers every sign; existence of a further block is detected by \(\exists x\,Q_i(x)\). In each detected block, for every \(1\le t\le k\) a formula with at most \(k\) names asserts that \(t\) distinct vertices satisfy \(L_i\):
\[
\exists x_1\cdots\exists x_t
\left(\bigwedge_{a<b}x_a\ne x_b\ \wedge\ \bigwedge_{a=1}^{t}L_i(x_a)\right).
\]
Each occurrence of the unary two-variable formula is evaluated locally; its auxiliary bound name may shadow another \(x_a\) *inside that conjunct* without affecting the external inequality conjunction. Therefore this genuinely uses at most \(k\) names, even when \(t=k\). Its truth for \(t=1,\ldots,k\) recovers exactly \(\min\{b_i,k\}\). Differences of truncated signatures therefore yield a distinguishing \(\mathrm{FO}^k\) sentence.

**3. The unrestricted converse.** Suppose the truncated signatures agree. In the infinite-round \(k\)-pebble game, Duplicator preserves the block index and, within each block, equality of occupied vertices. For a block of actual size below \(k\), its size agrees on both sides and a fixed bijection suffices. For a block with size at least \(k\) on both sides, at most \(k-1\) other pebbles are present when one is moved, so a fresh counterpart is always available when Spoiler chooses an unoccupied vertex. If the chosen vertex is already occupied, copy its matched counterpart. Equal block signs preserve all adjacency and nonadjacency relations, as established in step 1. This is a permanent legal response strategy and proves equivalence at *all* quantifier depths, not just finitely bounded depths.

**4. Enumeration and minimum models.** The final block of a non-singleton canonical list can take any actual size at least two. After truncation, its representative size lies in \(\{2,\ldots,k\}\); every earlier block has representative size in \(\{1,\ldots,k\}\). There are two choices of the starting sign; later signs alternate. This gives \(2(k-1)k^{h-1}\) truncated lists of length \(h\), and the generating function \(R_k\) follows by multiplying the final-block polynomial \(B_k\) by a geometric series of preceding blocks with polynomial \(A_k\). The truncated representative is the unique smallest one because every actual size producing the same truncation is at least its truncated size.

A class whose truncated list has **no** entry equal to \(k\) can only occur at exactly the size of its smallest representative. Their generating polynomial series is \(T_k\). A class with at least one truncated entry equal to \(k\) occurs at *every* greater order by enlarging that block, producing the geometric factor \(1/(1-z)\). Therefore \(U_k=T_k+(R_k-T_k)/(1-z)\). Specializing \(k=2\) gives \(R_2=z+2z^2/(1-z-z^2)\) and \(U_2=z+2z^2/[(1-z)(1-z-z^2)]\), yielding the Fibonacci formulas. Finally, width one has just one theory because \(E(x,x)\) is always false; for each \(k\ge2\), \(K_k\) and \(K_{k+1}\) have equal \(k\)-truncated lists but different \((k+1)\)-truncated lists. The width-one-to-two step is witnessed by a one-vertex graph and \(K_2\).

## Verification

Two separate standard-library programs are bundled. Run `python3 verify_finite_variable.py` and `python3 verify_spectra.py` in the directory containing this document. The first independently computes stable counting-free \(k\)-tuple types (iteratively tracking the **sets**, not multiplicities, of types reachable by replacing each coordinate) for all binary creation words through seven vertices at width two, six at width three and five at width four. It finds respectively \(41,47,29\) distinct sentence theories, exactly matching the proposed signatures, without a disagreement. These runs cover \(127,63,31\) graphs and \(4{,}861,9{,}549,12{,}405\) tuple states respectively. The second independently enumerates all binary creation words through twelve vertices for each width \(2\le k\le6\), comparing both proposed rational spectra with the signatures of the generated graphs; all comparisons pass. Exact machine-readable output files are bundled as `verify_finite_variable_output.json` and `verify_spectra_output.json`. All finite experiments corroborate; neither substitutes for steps 1--4, which prove the infinite-parameter assertions.

## Relationship to prior work

Threshold graphs and their extremal-vertex creation sequences are classical. Reilly and Scheinerman (2009), especially Theorem 2.7 and Propositions 2.12--2.14, give the graph normal form and the count of nonisomorphic threshold graphs of a fixed order. Sciriha and Farrugia's *On the Spectrum of Threshold Graphs* (first online in 2012), in particular Sections 3 and 4, studies nested split/cotree representations and adjacency-matrix spectra, not \(\mathrm{FO}^k\) logical theories. Kiefer, Schweitzer and Selman (arXiv version 2015), especially the introduction and identification results, study the **stronger** logic \(C^2\) with counting quantifiers and graph identification among all finite graphs. These do not themselves state the precise no-counting, all-width truncated-block equivalence, canonical minimum representatives or their rational order spectra. The present statement is an additional consequence of the classical decomposition together with a specific finite-variable game analysis, not a claim that the graph decomposition itself is new. A general uninspected logical-composition theorem for graph modules might imply this classification; historical priority is therefore provisional.

## Limitations

The theorem is relative to finite nonempty threshold graphs and to pure adjacency without counting. It does not characterize which arbitrary graphs outside this family have the same \(\mathrm{FO}^k\) theory, does not cover colored or weighted variants, and makes no assertion about optimal distinguishing quantifier rank. It does not imply any analogous closed classification for arbitrary cographs or split graphs. The computation checks bounded orders and widths only; the general results depend on the written proof. Historical priority and mathematical validation have not been independently established.

## References

1. E. Perez Reilly and E. R. Scheinerman, *Random Threshold Graphs*, Electronic Journal of Combinatorics 16(1), #R130 (published 2009-10-31), DOI: 10.37236/219. Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v16i1r130/pdf/
2. I. Sciriha and S. Farrugia, *On the Spectrum of Threshold Graphs*, International Scholarly Research Notices, volume 2011, article 108509 (first published online 2012-01-17), DOI: 10.5402/2011/108509. Full text: https://onlinelibrary.wiley.com/doi/10.5402/2011/108509
3. S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792 (first version 2015-03-30). Full text: https://arxiv.org/pdf/1503.08792
4. P. Skums, *H-product and H-threshold graphs*, arXiv:1011.4726 (first submitted 2010-11-22). https://arxiv.org/abs/1011.4726
