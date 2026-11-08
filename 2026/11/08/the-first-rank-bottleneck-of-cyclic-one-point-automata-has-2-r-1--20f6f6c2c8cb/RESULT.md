# The first rank bottleneck of cyclic one-point automata has \(2^{r-1}\) optimal words

## Finding
Let \(n,r\) be integers satisfying \(r\ge2\) and \(n\ge2r+1\). Consider the complete deterministic automaton with state set \(Q=\mathbb Z/n\mathbb Z\) and letters
\[
 a(i)=i+1\pmod n,\qquad b(0)=r,\qquad b(i)=i\ \text{for }i\ne0.
\]
For \(1\le j\le r+1\), let \(\lambda_j\) be the minimum length of a word \(w\in\{a,b\}^*\) with \(|Qw|\le n-j\). Then
\[
\lambda_j=2j-1\quad(1\le j\le r),\qquad \lambda_{r+1}=3r+1.
\]
For each \(1\le j\le r\), the unique optimal word is \(b(ab)^{j-1}\). There are exactly \(2^{r-1}\) optimal words for \(j=r+1\). They are precisely the words obtained by choosing, independently for each \(1\le i\le r-1\), one time from \(\{i,i+r\}\), adjoining times \(0\) and \(2r\), ordering the resulting \(r+1\) times as \(0=t_0<t_1<\cdots<t_r=2r\), and writing
\[
 b a^{t_1-t_0}b a^{t_2-t_1}b\cdots a^{t_r-t_{r-1}}b.
\]
In particular the first departure from a unique linear-cost rank-compression optimum is a gap of \(r+2\) letters between successive rank thresholds: \(\lambda_{r+1}-\lambda_r=r+2\).

## Assumptions and scope
Words act on subsets from left to right; their rank is the cardinality of the image of the entire state set. All counts concern distinct literal label strings, not state relabelings, target subsets, or equivalence classes of transformations. The hypothesis \(n>2r\) guarantees that time indices in \([0,2r]\) do not wrap around modulo \(n\). The theorem asserts only the first \(r+1\) rank thresholds, not the full synchronization profile. The range \(r\ge2\) isolates a nontrivial first-bottleneck family; the same proof also works for \(r=1\).

## Proof
Write \(A(w)\) and \(B(w)\) for the respective numbers of letters \(a\) and \(b\). A letter \(a\) is a permutation and cannot reduce image size. A letter \(b\) can reduce image size by at most one; after an effective \(b\), the state \(0\) is absent, so another effective \(b\) requires an intervening \(a\). Therefore reducing rank by \(j\) requires at least \(j\) letters \(b\) and \(j-1\) letters \(a\), giving \(\lambda_j\ge2j-1\). Equality forces the word \(b(ab)^{j-1}\). For \(1\le j\le r\), this word has \(j\) effective merges: its cyclic shift counts preceding successive occurrences of \(b\) are \(0,1,\ldots,j-1\), and none differ by \(r\). Thus the first claim and uniqueness follow.

For the next rank, we prove a stronger rotation-budget obstruction. After a prefix containing \(t\) letters \(a\), let \(S\) denote the image of \(Q\), and define the *co-moving hole set* \(H=a^{-t}(Q\setminus S)\). A subsequent \(a\) leaves \(H\) unchanged while increasing \(t\) by one. A subsequent \(b\) acts as follows: if \(-t\in H\), it does nothing; otherwise it adjoins the hole \(-t\) and removes any hole at \(r-t\). The subtraction is modulo \(n\). This follows directly from \(b(0)=r\) and the fact that \(b\) fixes all other states.

Suppose a prefix has at most \(2r\) occurrences of \(a\). Since \(n>2r\), each hole can be represented by an integer timestamp \(s\in[0,2r]\) via its location \(-s\pmod n\), and all these locations are distinct. At a letter \(b\) occurring at time \(t\), the only previously created hole potentially removed is timestamp \(t-r\), if this is nonnegative and currently occupied: indeed a previous timestamp \(s\le t\) satisfies \(-s\equiv r-t\pmod n\) only when \(t-s=r\), because \(0\le t-s\le2r<n\). Thus an occurrence of \(b\) at time \(t\) either does nothing, adds a new occupied timestamp \(t\), or moves occupancy from \(t-r\) to \(t\).

If the total number \(T=A(w)\) of rotations satisfies \(T<2r\), each residue class modulo \(r\) occurs at most twice among timestamps \(0,\ldots,T\), and the two possible timestamps differ by \(r\). The update rule makes it impossible to hold both simultaneously. Consequently \(|H|\le r\), even with arbitrarily many ineffective occurrences of \(b\). Hence achieving deficiency \(r+1\) necessarily requires \(A(w)\ge2r\). It also requires \(B(w)\ge r+1\), so \(|w|\ge3r+1\).

Equality entails exactly \(2r\) occurrences of \(a\) and exactly \(r+1\) occurrences of \(b\); every \(b\) must be effective. List their cumulative rotation times as \(t_0\le\cdots\le t_r\), between \(0\) and \(2r\). Two occurrences at the same time cannot both be effective. Nor can two selected times differ by exactly \(r\): the first makes a hole that the second would transport instead of creating another. Conversely, if all selected times are distinct and none differ by \(r\), each \(b\) creates a new hole, because modulo \(n\) there are no other collisions in this time range.

The graph whose vertices are \(0,\ldots,2r\) and whose edges join timestamps differing by \(r\) is the disjoint union of one three-vertex path \(0-r-2r\) and \(r-1\) two-vertex edges \(i-(i+r)\), for \(1\le i\le r-1\). An independent vertex set has at most \(2+(r-1)=r+1\) vertices, and equality holds exactly when it includes both endpoints \(0,2r\), excludes \(r\), and chooses one endpoint from each of the remaining \(r-1\) edges. These choices are independent, giving precisely \(2^{r-1}\) sets and hence distinct words as stated. Every such word has \(3r+1\) letters and exactly \(r+1\) effective merges. The theorem follows.

## Verification
The accompanying standalone `verify.py` computes the reachable subset automaton with breadth-first search and counts distinct shortest label strings through exact integer path-counting. For every \(5\le n\le14\) and \(2\le r<n/2\), it checked all \(r+1\) asserted rank thresholds and shortest-word counts (130 cases). It also replayed all constructive optimal words for \(2\le r\le11\) against three choices of \(n>2r\) (6,138 checks). Run `python verify.py` from a directory containing the script. Finite checks corroborate but do not replace the argument valid for all integers in scope.

## Relationship to prior work
Behague and Johnson studied general rendezvous times for \(k\)-sets and power-automaton rank bounds [1]; their stated bounds concern general automata and do not give exact shortest-label counts for this cyclic one-point family. Martyugin examined reset-word and compression problems for automaton classes [2], but the inspected passages did not supply this initial-rank optimizer enumeration. Related published exact rank-threshold studies on other automaton families and a codimension-two reachability classification use different transition maps or different target questions; neither of the located summaries establishes the present \(r+1\)-deficiency language or its \(2^{r-1}\) count. The new assertion is the complete sharp frontier and optimizer set in the stated \(n>2r\) family, not the general definitions or existing synchronization bounds.

## Limitations
The result does not determine subsequent rank thresholds \(j>r+1\), reset thresholds in all parameters, or the cases \(n\le2r\). No claim of priority against inaccessible or unindexed equivalent results is made. Independent validation has not been performed. The proof is mathematical; the packaged finite program is a reproducibility check only.

## References
[1] N. C. Behague and J. R. Johnson, *Synchronizing Times for \(k\)-sets in Automata*, arXiv:2008.12166 (first posted 2020-08-27), *Electronic Journal of Combinatorics* 29(3), P3.41 (2022), https://arxiv.org/abs/2008.12166.

[2] P. Martyugin, *Complexity of Problems Concerning Reset Words for Some Partial Cases of Automata*, *Acta Cybernetica* 19(2), 517–536 (2009), https://acta.bibl.u-szeged.hu/12877/.
