# Narayana–Chebyshev enumeration of losing positions in a balanced-end subtraction game

## Finding
Let \(\mathcal{P}_n\) be the losing words of length \(n\) in the following normal-play game on \(\{a,b\}^*\): a legal move deletes a nonempty prefix or nonempty suffix whose numbers of \(a\)'s and \(b\)'s agree. The empty word is losing. Every nonempty balanced word is winning. For every nonempty word with nonzero total balance \(h\), define its boundary itinerary by recording \(A\) at every prefix position of balance \(0\), and \(B\) at every prefix position of balance \(h\), including the two endpoints. **The word is losing exactly when its boundary itinerary belongs to \(A\mathcal{D}B\), where \(\mathcal{D}\) is the Dyck language with up-step \(A\) and down-step \(B\).**

This classification has the following explicit enumeration valid at **every length**, including contributions from every possible nonzero final balance. Introduce formal power series
\[
P(z)=\frac{1-\sqrt{1-4z^2}}2,\qquad
D_0(z)=D_1(z)=1,\quad D_r(z)=D_{r-1}(z)-z^2D_{r-2}(z)\ (r\ge2).
\]
For each integer \(h\ge1\), set
\[
u_h(z)=P(z)+\begin{cases}0,&h=1,\\ z^2D_{h-2}(z)/D_{h-1}(z),&h\ge2,\end{cases}
\qquad v_h(z)=\frac{z^h}{D_{h-1}(z)}.
\]
Let \(N(j,k)=\frac1j\binom jk\binom j{k-1}\) for \(j\ge1\) and \(1\le k\le j\). Then the generating function for losing words of final balance \(+h\) is
\[
F_h(z)=v_h(z)+\sum_{j\ge1}\sum_{k=1}^j
N(j,k)u_h(z)^{2(j+1-k)}v_h(z)^{2k-1}.
\]
Writing \(p_n=|\mathcal P_n|\), the complete exact enumeration is
\[
\boxed{p_0=1,\qquad p_n=2\sum_{h=1}^{n}[z^n]F_h(z)\quad(n\ge1).}
\]
All expressions are formal series; only finitely many \(h,j,k\) contribute to any fixed coefficient. In addition, the language of losing positions is **not regular**.

## Assumptions and scope
A prefix or suffix is contiguous, must be nonempty, and may be the entire word. A word has total balance \(H(w)=|w|_a-|w|_b\), and the prefix balance after \(t\) letters is \(S_t\). The player unable to move loses. The boundary itinerary is defined only when \(H(w)\ne0\), because levels \(0\) and \(H(w)\) must be distinct. All lengths are nonnegative integers and both letters have unit weights; the formula is not asserted for weighted alphabets or arbitrary deletion languages.

## Proof
**1. Reduction to a boundary game.** An eligible prefix ends exactly where \(S_t=0\), and an eligible suffix begins exactly where \(S_t=H(w)\). Prefix deletion leaves total balance \(H(w)\), as does suffix deletion. When \(H(w)\ne0\), every legal nonterminal move therefore deletes, respectively, an initial part ending at a noninitial \(A\), or a terminal part beginning at a nonterminal \(B\), of the itinerary \(A\,x\,B\). The remaining itinerary is again \(A\,y\,B\); its interior is obtained by removing an initial segment through an \(A\) in \(x\), or a terminal segment beginning with a \(B\) in \(x\). If there are no interior events, there is no legal move. This includes the empty interior. No whole-word deletion is possible for nonzero balance. For zero balance, whole-word deletion is legal and leads to the empty losing position, so every nonempty balanced word is winning.

**2. A direct normal-play characterization.** In the resulting finite game on the interior \(x\in\{A,B\}^*\), a move removes a prefix ending in \(A\) or a suffix beginning in \(B\). The losing interiors are exactly Dyck words. Indeed, a Dyck word cannot move to another Dyck word: a proper suffix after an \(A\) has negative net balance, and a proper prefix before a \(B\) has positive net balance. Conversely, if \(x\) has a prefix with more \(B\)'s than \(A\)'s, truncate from its first such \(B\) through the right end; the remaining prefix is Dyck. If no prefix is negative but the final balance is positive, remove the left prefix through the last unmatched \(A\) in the stack matching; the remaining suffix is Dyck. These cases cover every non-Dyck word. Induction on length proves the characterization.

**3. Generating functions for individual boundary passages.** Fix final balance \(h>0\). Decompose any binary lattice path at successive visits to the two boundary levels \(\{0,h\}\). Each resulting nonempty segment has no intermediate visit to either level. The series for a segment returning to its starting boundary is identical at \(0\) and \(h\), by reflection, and equals \(u_h\): a primitive excursion away from the interval \([0,h]\) has series \(P(z)\); an interior return traverses \(0\to1\), walks on the \(h-1\) interior states, and returns \(1\to0\), with series \(z^2D_{h-2}/D_{h-1}\) when \(h\ge2\). A segment crossing between boundaries has series \(v_h\). To prove these formulas, let \(A_{h-1}\) be the adjacency matrix of the path on interior states \(1,\ldots,h-1\). The continuant identity \(\det(I-zA_r)=D_r(z)\) follows by expanding the last row; the inverse entries at the endpoint and opposite endpoint are \(D_{h-2}/D_{h-1}\) and \(z^{h-2}/D_{h-1}\), respectively. The \(h=1\) case is one direct crossing step and no interior return.

**4. Narayana weighting and exact enumeration.** A primitive Dyck itinerary has the form \(A\,x\,B\) with \(x\) Dyck of semilength \(j\ge0\). For \(j=0\), its one boundary crossing contributes \(v_h\). For \(j\ge1\), suppose \(x\) has \(k\) peaks; there are \(N(j,k)\) choices. Along the full itinerary there are exactly \(2k-1\) changes between distinct boundary symbols and \(2(j+1-k)\) adjacent equal-symbol pairs. The passage series is therefore \(v_h^{2k-1}u_h^{2(j+1-k)}\). Multiplication is valid because the path passages are independently and uniquely concatenated. Summing yields \(F_h\). Exchanging \(a\) and \(b\) bijects the losing words with final balances \(+h\) and \(-h\), giving the coefficient formula for \(p_n\). As any word of length \(n\) has \(|H(w)|\le n\), the outer sum is finite coefficientwise.

**5. Nonregularity.** Intersect the losing language with the regular slice \(b^+a^+b\). For every \(i,j\ge1\), the word \(b^ia^jb\) is losing exactly when \(j\ge i+2\). To see this, for \(j\ge i+2\) the endpoint level is positive and the boundary itinerary is \(AABB\). For \(j=i+1\) the word is balanced and therefore winning. For \(j\le i\), the endpoint level is negative and the first interior boundary event is \(B\), so the interior is not Dyck. The slice \(\{b^ia^jb:i\ge1,\ j\ge i+2\}\) is not regular by the pumping lemma (or by infinitely many distinguishable residuals). Since regular languages are closed under intersection, the losing language is not regular.

## Verification
The accompanying `verify_series.py` computes the exact coefficient formula through length \(18\) by integer polynomial arithmetic and independently evaluates normal-play mex values for all binary words through length \(16\). The accompanying `verify_boundary.py` independently compares the exact game with the boundary-itinerary criterion through length \(16\) and tests the infinite-slice characterization on \(196\) parameter pairs. Both scripts were executed from their actual enclosed paths, and their exact outputs appear in `verify_series.out` and `verify_boundary.out`. The resulting losing counts for lengths \(0\) through \(18\) are
\[
1,2,2,2,2,6,14,24,34,80,154,292,494,1070,1996,3974,7114,14908,27772.
\]
Finite verification is supplemental to, not a substitute for, the preceding all-length proof.

## Relationship to prior work
Inoue and Inazu introduced a broad framework for word subtraction games and discuss prefix/suffix rules and two-sided examples. The classical Timber game has the exact Dyck losing-position criterion used in Step 2; Nowakowski, Renault, Lamoureux, Mellon and Miller studied it on paths. The present new enumerative claim concerns **balanced-end removals on the original binary word**, with variable final endpoint height and a weighted Narayana/finite-path-resolvent summation. Neither inspected source provides this all-length count. Related published investigations of Dyck-only removals and other trigger languages have different legal options; the distinction is substantive, not a claim that the elementary Dyck game is new.

## Limitations
Only losing positions, not all Sprague–Grundy numbers, are classified or counted. The expression is exact but coefficientwise and involves a height sum; no simpler universal asymptotic or closed elementary formula is claimed. Absence of an indexed equivalent cannot establish absolute novelty.

## References
1. Y. Inoue and T. Inazu, *Word Subtraction Games*, arXiv:2611.09157v1 (first public submission 2026-11-06), https://arxiv.org/abs/2611.09157 .
2. R. J. Nowakowski, G. Renault, E. Lamoureux, S. Mellon and T. Miller, *The Game of timber!*, Journal of Combinatorial Mathematics and Combinatorial Computing 85 (2013), 213–225, https://combinatorialpress.com/article/jcmcc/Volume%20085/vol-085-paper%2013.pdf .
3. T. W. Narayana, *Sur les treillis formés par les partitions d'un entier et leurs applications à la théorie des probabilités*, Comptes Rendus de l'Académie des Sciences 240 (1955), 1188–1189 (classical peak-count distribution; invoked as the standard Narayana formula).
