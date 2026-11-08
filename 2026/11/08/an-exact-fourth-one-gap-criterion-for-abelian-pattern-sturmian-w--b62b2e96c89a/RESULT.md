# An exact fourth-one gap criterion for Abelian pattern Sturmian words

## Finding

Fix integers \(M\ge3\) and \(t\ge1\). There is an infinite binary Abelian pattern Sturmian word whose first four occurrences of \(1\) are exactly at the zero-based indices
\[
0,\ 1,\ M,\ M+t
\]
if and only if
\[
\boxed{t\ge4\quad\text{and}\quad M\bmod t\in\{3,4,\ldots,t-1\}.}
\]
Equivalently, the disallowed fourth gaps are \(1,2,3\) and the positive divisors of at least one of the three consecutive integers \(M,M-1,M-2\). For each permitted pair the proof supplies an explicit infinite continuation of the support. For each forbidden pair no continuation is possible.

## Assumptions and scope

An infinite binary word \(x=x_0x_1\cdots\) is called *Abelian pattern Sturmian* when, for every positive integer \(k\), the largest number of distinct Parikh vectors of factors taken along any \(k\)-point pattern is the least positive integer \(h\) such that \(\binom h2\ge k\). This is the definition and normalization in Zeng–Xue–Zeng [1]; it is not the usual contiguous-factor definition of Sturmian words.

For \(E\subseteq\mathbb N_0\), let \(\Gamma_E\) be the bipartite graph with different left and right copies \(L_i,R_j\) of each nonnegative integer, and with \(L_iR_j\) an edge precisely when \(i+j\in E\). Theorem E of [1] states that the characteristic word of an infinite set \(E\) is Abelian pattern Sturmian if and only if \(\Gamma_E\) is acyclic. We use that theorem as an established input; the arithmetic graph analysis below is proved directly.

The statement is about the first four \(1\)-positions in the sparse-letter convention; the word may have infinitely many later \(1\)'s. It does not assert that every continuation is admissible.

## Proof

**1. Reduction to four sums.** Put \(E_0=\{0,1,M,M+t\}\). If \(\Gamma_{E_0}\) has a cycle, so does every supergraph \(\Gamma_E\) with \(E_0\subseteq E\). If it has no cycle, it can be extended indefinitely without introducing one: whenever \(E\) is finite and its maximum is \(q\), adjoin \(p=2q+1\). The edges of new sum \(p\) are a matching. Each has at least one endpoint indexed above \(q\), hence an endpoint untouched by the old graph; therefore no new cycle occurs. Repetition produces an infinite set with the prescribed first four positions. Thus the assertion is equivalent to acyclicity of \(\Gamma_{E_0}\).

**2. The two large sums.** Let \(H=\Gamma_{\{M,M+t\}}\). Each sum separately gives a matching. Following two consecutive edges of different sums, starting at a left vertex, changes its index by \(t\) or \(-t\). There is no cycle: a finite cycle would require a nontrivial closed walk in an index path with consecutive differences \(\pm t\) and no backtracking. More precisely, the left vertices of an \(H\)-component are exactly those in one residue class modulo \(t\) that can be reached by these steps within the available range. As each residue chain contains \(L_r,L_{r+t},L_{r+2t},\ldots\) up to \(M+t\), its consecutive links are supplied by the shared right vertices \(R_{M-r},R_{M-r-t},\ldots\) whenever the smaller left index is at most \(M\). In particular the left vertices form a connected chain for each residue class among the indices \(0,\ldots,M+t\).

Every right vertex \(R_j\) incident with \(H\) has component label \(M-j\pmod t\): for \(0\le j\le M\), it meets \(L_{M-j}\), and for \(M<j\le M+t\), it meets \(L_{M+t-j}\). The left vertex \(L_i\) has label \(i\pmod t\). Therefore two of the four vertices \(L_0,L_1,R_0,R_1\) belong to the same \(H\)-component if and only if two of the residue labels
\[
0,\qquad1,\qquad M,\qquad M-1\pmod t
\]
coincide.

**3. The two small sums.** The edges of sums \(0\) and \(1\) form precisely the three-edge path
\[
R_1-L_0-R_0-L_1.
\]
Adding a path to a forest preserves acyclicity exactly when its four vertices belong to four different old components. Indeed, if they do, the successive new edges merely join four components into a tree; if two lie in the same old component, the old connecting path and the corresponding new path yield a cycle (or one of the successive joins itself closes a cycle). Consequently \(\Gamma_{E_0}\) is a forest exactly when the displayed four residues are pairwise distinct.

Pairwise distinctness of \(0,1,M,M-1\pmod t\) is equivalent to
\[
t>1,\qquad t\nmid M,\qquad t\nmid(M-1),\qquad t\nmid(M-2).
\]
As these are three consecutive integers, no \(t\le3\) works. For \(t\ge4\), they say precisely \(M\bmod t\notin\{0,1,2\}\). Combining with Step 1 and Theorem E of [1] proves both directions.

## Verification

The accompanying independent script `verify_prefix.py` enumerates the complete finite bipartite sum graph and detects a cycle by disjoint-set union. For all \(3\le M\le90\) and \(1\le t\le90\), it compares the graph output against the congruence formula, and for each admitted case checks three successive strict-more-than-double support extensions. All \(7920\) parameter pairs passed, including \(6895\) admitted pairs. These tests are corroboration only; Steps 1–3 are the proof for every integer parameter.

## Relationship to prior work

Zeng, Xue and Zeng [1, Theorem E, Section 7.1] prove the necessary and sufficient *forest* characterization. Their Proposition 7.12 provides rapidly growing examples, and Section 7.3 distinguishes the Sidon condition from forest acyclicity; these statements supply the conceptual framework. The explicit four-position residue obstruction here is **derived from**, not independent of, their theorem. Its new content is the complete parameter-level arithmetic evaluation for the non-lacunary fixed prefix \(0,1,M\) and all next gaps \(t\), together with its infinite extension boundary. For example, \(\{0,1,5,8\}\) has distinct positive pair differences but contains a longer incidence cycle; its fourth gap \(3\) is forbidden even though the support is Sidon. The original paper [2, Sections 1–4] introduced Abelian maximal pattern complexity for recurrent words and does not supply this arithmetic classification. The full text of [2] was also compared for an equivalent four-position statement.

## Limitations

This is a classification for a specified four-one prefix, not an arbitrary finite support or the full set of infinite admissible supports. The proof depends on the established Abelian pattern Sturmian/forest equivalence in [1]. Searches of indexed sources and the closely relevant portions of the full text of [1] did not find this residue classification; the general forest criterion is stronger in scope, and the possibility that this short specialization has appeared elsewhere remains a priority risk. No independent mathematical audit has been performed.

## References

[1] Q. Zeng, Y. Xue, C. Zeng, *Abelian maximal pattern complexity and extremal words*, arXiv:2609.28059 (first public version 2026-09-23), Theorem E and Sections 7.1–7.3. https://arxiv.org/abs/2609.28059

[2] T. Kamae, S. Widmer, L. Q. Zamboni, *Abelian maximal pattern complexity of words*, Ergodic Theory Dynam. Systems **35** (2015), 142–151; first public preprint 2013-01-22. https://arxiv.org/abs/1301.5113
