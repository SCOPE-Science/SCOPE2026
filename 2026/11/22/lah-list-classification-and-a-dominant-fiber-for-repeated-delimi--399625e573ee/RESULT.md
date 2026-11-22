# Lah-list classification and a dominant fiber for repeated-delimiter bigram observations

## Finding
Fix integers \(r\ge1\) and \(s\ge0\) and distinct symbols \(a,b_1,\ldots,b_s\). Let \(\mathcal W_{r,s}\) be the set of indexed linear words containing exactly \(r\) copies of \(a\) and one copy of every \(b_i\). Observe the complete multiplicity vector \(\Phi(w)\) of contiguous factors of lengths one and two (the full \(2\)-Abelian readout). A *return list* is a nonempty block of singleton symbols strictly between two consecutive occurrences of \(a\). Let \(k\) denote the number of return lists.

For every integer \(0\le k\le\min(s,r-1)\):

1. Exactly
   \[
   c_{s,k}=\frac{s!}{k!}\binom{s+1}{k+1}
          =\binom{s}{k}\frac{(s+1)!}{(k+1)!}
   \]
   distinct observations have \(k\) return lists. This is the unsigned Lah number \(L(s+1,k+1)\), counting partitions of \(s+1\) labeled atoms into \(k+1\) unordered, nonempty ordered lists.
2. Every observation in that stratum has exactly
   \[
   f_{r,k}=\frac{(r-1)!}{(r-1-k)!}
   \]
   source words. Thus the number of fibers of any size \(d\) is exactly \(\sum_{\{k:f_{r,k}=d\}}c_{s,k}\). Distinct \(k\) can yield the same size at boundaries; no uniqueness of the size label is assumed.

The sharp maximum number of source words distinguishable by this observation is therefore
\[
Q_{r,s}=\sum_{k=0}^{\min(s,r-1)}\frac{s!}{k!}\binom{s+1}{k+1}.
\]
For fixed \(s\), this capacity stabilizes once \(r\ge s+1\), and not earlier when \(s\ge1\): its limiting count is the known set-of-lists number \(A000262(s+1)\), with first values \(1,3,13,73,501,4051,37633\) for \(s=0,\ldots,6\). This numerical sequence is **not claimed new**; the exact two-parameter readout/fiber classification is the point of the theorem.

For every \(r\ge s+1\), precisely one observation has \(s\) nonempty singleton return lists: its words start and end with \(a\) and every singleton \(b_i\) is isolated between copies of \(a\). Its fiber contains \((r-1)!/(r-1-s)!\) words. A uniformly chosen source word therefore belongs to that **one specific observation fiber** with probability
\[
\frac{(r-1)!/(r-1-s)!}{(r+s)!/r!}
=\prod_{j=1}^{s}\frac{r-j}{r+j}
=1-\frac{s(s+1)}{r}+O_s(r^{-2})\quad(r\to\infty).
\]
For \(s=0\) the product is empty and equals one. For each fixed positive \(s\), the total number of source words grows as \(r^s\), but almost all of them eventually have an identical complete adjacent-pair readout.

## Assumptions and scope
Letters are **labeled** and \(b_i\ne b_j\) for \(i\ne j\), with every \(b_i\ne a\). Words are linear, not circular; all contiguous occurrences, including overlaps and equal-letter digrams, are counted. A class is the set of words having the same complete length-one and length-two factor multiplicities. No probability model is used except for the last assertion, where the source is uniform over \(\mathcal W_{r,s}\). The zero-singleton case \(s=0\), the one-delimiter case \(r=1\), and the possibility of coincident fiber sizes are all included.

## Proof
**Recovering endpoints and nonrepeating paths.** Regard each adjacent factor \(xy\) as a directed edge \(x\to y\), with its observed multiplicity. For each symbol \(x\),
\[
\#_x(w)-\sum_y\#_{xy}(w)=\mathbf1_{\{x=\operatorname{last}(w)\}},\qquad
\#_x(w)-\sum_y\#_{yx}(w)=\mathbf1_{\{x=\operatorname{first}(w)\}}.
\]
Thus the observation recovers both endpoints. Each \(b_i\) occurs only once, so its incoming and outgoing edges (when present) are unique. Following these forced edges recovers each maximal ordered chain of distinct singleton symbols. All such chains either lead from the starting endpoint to \(a\), lead from \(a\) to the ending endpoint, or leave \(a\) and later return to \(a\). The support is connected because it arises from a word, so there can be no other component. The first two chains, possibly empty, are uniquely distinguished by the recovered endpoints. All nonempty return chains are uniquely identified as an **unordered collection**; they are pairwise different because each contains an individual singleton symbol.

**Canonical profile data.** The original word has a unique factorization
\[
w=P\,a\,U_1\,a\,U_2\,a\cdots a\,U_{r-1}\,a\,S,
\]
where \(P,S,U_1,\ldots,U_{r-1}\) are possibly empty words on pairwise disjoint subsets of \(\{b_1,\ldots,b_s\}\). The previous paragraph shows that \(\Phi(w)\) determines exactly the ordered prefix list \(P\), the ordered suffix list \(S\), and the unordered collection of nonempty \(U_i\). Conversely these data, together with \(r\), recover every directed digram count: each nonempty return is a directed chain starting and ending at \(a\), and the remaining \(r-1-k\) empty returns contribute precisely that many \(aa\) edges. Hence two words have the same observation **if and only if** these canonical data agree. The value of \(k\) is therefore a profile invariant.

**A bijection with sets of lists.** Introduce one new distinguished token \(\star\). Form the ordered list \((P,\star,S)\), and place alongside it the unordered collection of \(k\) nonempty return lists. This is an unordered set of \(k+1\) nonempty ordered lists partitioning the \(s+1\) labeled tokens \(\{\star,b_1,\ldots,b_s\}\). Conversely every such list partition determines the special list containing \(\star\), hence its unique split into \(P,S\), and its \(k\) other return lists. It is realizable exactly when \(k\le r-1\): insert \(r-1-k\) empty returns in any positions. This proves a bijection, not just agreement of counting sequences.

To count sets of \(k+1\) lists, order all \(s+1\) atoms, choose the \(k\) cuts between lists among the \(s\) gaps, then forget the order of the \(k+1\) lists. The count is \(\binom{s}{k}(s+1)!/(k+1)!=c_{s,k}\).

**Fibers.** Once the data are fixed, the \(k\) nonempty returns are distinguishable, while the \(h=r-1-k\) empty returns are identical. Every ordering of this multiset of returns gives a different source word, and every word in the fiber occurs in exactly this way. The count is \((k+h)!/h!=(r-1)!/(r-1-k)!=f_{r,k}\). These statements also hold at \(k=0\). Summing \(c_{s,k}\) gives \(Q_{r,s}\), and choosing one representative per set of lists achieves the code-size upper bound.

**Sharp saturation and dominant fiber.** All partitions of the \(s+1\) tokens have at most \(s+1\) blocks, so every profile occurs if and only if \(r\ge s+1\). If \(s\ge1\) and \(r=s\), the one partition into \(s+1\) singleton lists is missing; thus the stated threshold is sharp. In the all-singleton partition the distinguished list is just \((\star)\) and the other \(s\) lists are \((b_i)\). It gives exactly one profile with \(k=s\), and its fiber size is \(f_{r,s}\). There are \((r+s)!/r!\) possible source words; dividing and expanding the finite product proves the displayed probability and asymptotic. No finite computation is used to justify an all-parameter step.

## Verification
Two standalone verification programs accompany this statement. Run `python3 check_direct.py` to enumerate actual indexed words, compute complete one/two-factor count vectors, and compare all observed fiber sizes and class counts to the formulas for 43 parameter pairs through total length ten. Run `python3 check_lists.py` to independently generate list partitions with a distinguished token, construct representative words, and verify distinctness and Lah-stratum counts for 56 parameter pairs; it also produces the seven saturation values displayed above. Actual successful output from both programs is included as `check-output.txt`. These bounded checks test normalization and boundaries; the proof establishes all \(r,s\).

## Relationship to prior work
The general definition and fundamental properties of \(k\)-Abelian equivalence come from Karhumäki, Saarela, and Zamboni (2013). Karhumäki, Puzynina, Rao, and Whiteland (2016 preprint; 2017 journal) prove a general Euler-trail formula for the cardinality of a single \(k\)-Abelian class (Proposition 4.7); **individual-class enumeration via this general theorem is prior work**, and no generalization of it is claimed. The present statement classifies and counts the entire quotient at a particular natural fixed content, identifies a precise unsigned-Lah stratum and saturation threshold, and determines its exact dominant-fiber law. The saturated integer sequence already occurs as OEIS A000262, counting sets of lists: neither that classical sequence nor the Lah numbers are claimed novel. A related published result on *scattered* length-two subsequence decks with singleton markers concerns a different observation and cannot imply adjacent-factor equality, while a homopolymer-free ternary 2-Abelian profile formula has a different fixed alphabet and source constraint.

## Limitations
All non-delimiter symbols must be individually distinguishable and occur exactly once. No formula for several repeated symbol types, cyclic words, length-three factors, noisy readouts, or a fixed alphabet with arbitrary content is claimed. The zero-error code size counts representatives of exact observations, not error-correcting packing under uncertain observations. Novelty is assessed against inspected accessible literature and known sequence records rather than independently certified; equivalent unindexed or implicit specialized enumerations remain a priority risk.

## References
1. J. Karhumäki, A. Saarela, and L. Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, arXiv:1301.5104 (first public version January 22, 2013), https://arxiv.org/abs/1301.5104.
2. J. Karhumäki, S. Puzynina, M. Rao, and M. A. Whiteland, *On cardinalities of k-Abelian equivalence classes*, arXiv:1605.03319 (first public version May 11, 2016), especially Sections 2–5 and Proposition 4.7, https://arxiv.org/abs/1605.03319.
3. OEIS A000262, *Number of sets of lists*, https://oeis.org/A000262 (previously known saturated numerical sequence).
4. *Exact two-deck spectra and fiber multiplicities with distinct marker letters*, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-two-deck-spectra-and-fiber-multiplicities-with-distinct-ma--26e221758afc (scattered-subsequence observation, distinct from contiguous bigrams).
5. *Exact 2-Abelian reconstruction capacity of homopolymer-free ternary words*, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-2-abelian-reconstruction-capacity-of-homopolymer-free-tern--9d4b0696d935 (different source language).
