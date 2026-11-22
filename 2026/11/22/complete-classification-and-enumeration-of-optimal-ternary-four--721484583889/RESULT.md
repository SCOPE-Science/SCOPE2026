# Complete classification and enumeration of optimal ternary four-list multiset deletion codes

## Finding

Let \(n\ge4\) and
\[
\mathcal S_{n,3}=\{(x_0,x_1,x_2)\in\mathbb Z_{\ge0}^3:x_0+x_1+x_2=n\}.
\]
A code \(C\subseteq\mathcal S_{n,3}\) has *list allowance four with two surviving unordered symbols* if, for every \(y\in\mathcal S_{2,3}\), at most four different \(x\in C\) satisfy \(y_i\le x_i\) for each \(i\). Distinct codebooks are counted as subsets of the labeled multiplicity-vector simplex; message order is irrelevant, and symbol relabelings count separately unless they fix the subset.

**Theorem.** For every \(n\ge4\), the maximum code size is \(11\). Moreover, **all** size-eleven codebooks belong to the following two disjoint families, and their exact number is
\[
\boxed{12n-36}.
\]
Write \(e_0,e_1,e_2\) for the standard basis, and for distinct \(i,j,k\in\{0,1,2\}\), define
\[
P_i=ne_i,\quad A_i^j=(n-1)e_i+e_j,\quad B_i=(n-2)e_i+e_j+e_k.
\]
The twelve *one-heavy* vectors form
\[
U=\{P_i,A_i^j,A_i^k,B_i:i\in\{0,1,2\}\}.
\]
Here \(j,k\) are the two labels other than \(i\). The two families are:

**Type I (three codebooks):** \(C=U\setminus\{B_i\}\), for a choice of \(i\).

**Type II (\(12n-39\) codebooks):** Choose one unordered label pair \(\{i,j\}\) with remaining label \(k\), then select exactly one of these alternatives:

- **Edge addition:** Choose \(r\in\{2,\ldots,n-2\}\) and \(x=re_i+(n-r)e_j\). Let \(D\) be exactly one of \(\{B_i,B_j\}\), \(\{A_i^j,B_j\}\), or \(\{B_i,A_j^i\}\), and take \(C=(U\setminus D)\cup\{x\}\).
- **Interior addition:** Choose \(r\in\{2,\ldots,n-3\}\) and \(x=re_i+(n-1-r)e_j+e_k\). Set \(C=(U\setminus\{B_i,B_j\})\cup\{x\}\).

An interval with reversed endpoints is empty. In particular, interior additions do not exist when \(n=4\). To avoid double-counting, the coordinates of \(r\) and \(n-r\) are assigned to the **labeled** pair using its unique increasing order \(i<j\); the codebook itself does not depend on any ordering of its eleven members.

## Assumptions and scope

The model concerns exactly \(n-2\) deletions, leaving an unordered multiset of cardinality two. The six received types are \(00,11,22,01,02,12\). A codeword can generate a received pair if and only if it componentwise dominates that pair. A coordinate is *heavy* precisely when it is at least two, and the six possible output loads count distinct parent vectors, not deletion sequences. A codebook is optimal when it has maximum cardinality under the four-parent-per-output constraint. No assertion is made about larger alphabets, ordered surviving pairs, or shorter \(n\).

## Proof

**1. A sharp eleven-word upper bound.** Every vector of length \(n\ge4\) has a heavy coordinate: if all three coordinates were at most one, they would sum to at most three. Each heavy coordinate generates its monochromatic received pair \(ii\). Consequently, summing the three monochromatic list loads gives at least \(|C|\) and at most \(3\cdot4=12\); thus \(|C|\le12\). Equality would force every codeword to have exactly one heavy coordinate and all three monochromatic loads to equal four. There are precisely twelve one-heavy vectors, namely \(U\), so a twelve-word code would have to be all of \(U\). But every mixed received pair \(ij\) has five parents in \(U\): \(A_i^j,A_j^i,B_0,B_1,B_2\). This exceeds the permitted four. Thus \(|C|\le11\). Removing any \(B_i\) from \(U\) makes every mixed load exactly four and leaves monochromatic loads at most four, proving attainability.

**2. Restriction to eleven-word equality cases.** For any size-eleven code let \(T\) be the number of its one-heavy vectors and let \(H\) count all incidences with monochromatic received pairs. Each other selected vector has at least two heavy coordinates, and therefore
\[
22-T\le H\le12.
\]
Hence \(T\ge10\). If \(T=11\), the code is \(U\) minus one member, and every mixed output must lose at least one of its five parents. The deleted member must therefore belong to all three mixed outputs, which holds precisely for \(B_i\), giving Type I.

If \(T=10\), the eleventh vector \(x\notin U\) has exactly two heavy coordinates and \(H=12\). Say they are \(i,j\), leaving \(k\). All three monochromatic loads are saturated; relative to all of \(U\), exactly two one-heavy vectors have been deleted and the two-heavy \(x\) added. Monochromatic saturation forces the two deleted vectors to have distinct heavy labels \(i,j\). In \(U\), a vector heavy at \(i\) contributes to the mixed pair \(ij\) exactly when it is \(A_i^j\) or \(B_i\); analogously at \(j\). Since \(x\) contributes to mixed pair \(ij\) and \(U\) had five parents of that pair, **both** deletions must contribute to \(ij\). Thus the deleted pair is chosen from
\[
\{A_i^j,B_i\}\times\{A_j^i,B_j\}.
\]
For the other mixed pairs \(ik\) and \(jk\), each initially has five parents. If \(x_k=0\), the new vector does not contribute to those two pairs, and at least one of the deletions must contribute to each; this happens exactly when at least one deleted vector is \(B_i\) or \(B_j\). The sole excluded choice is \(\{A_i^j,A_j^i\}\), leaving the three edge-addition deletion choices. Conversely, all three pass each mixed and monochromatic constraint.

If \(x_k=1\), then \(x\) contributes to *every* mixed pair; each of \(ik\) and \(jk\) must lose both deleted parents. Within the displayed Cartesian product, this is possible exactly when both deleted vectors are \(B_i,B_j\). Conversely that pair suffices. Since \(x\) has exactly two heavy coordinates, necessarily \(x_k\in\{0,1\}\); these are the stated edge/interior alternatives, and no others exist.

**3. Distinctness and enumeration.** The Type I deletion has three choices. Each Type II code uniquely reveals its sole two-heavy word \(x\), its unordered pair of heavy labels and the two one-heavy members missing from \(U\). For each of the three choices of heavy pair, an edge word has \(n-3\) possible splits and three allowed deletion pairs, while an interior word has \(n-4\) splits and one allowed deletion pair. Therefore the number of Type II codes is
\[
3\bigl(3(n-3)+(n-4)\bigr)=12n-39,
\]
and the total number of optimal codebooks is \(3+(12n-39)=12n-36\). This argument is valid at \(n=4\) using zero interior choices. Every step is an exact incidence or counting implication, not a numerical extrapolation.

## Verification

The standalone files `checks/brute.py` and `checks/structural.py` require only Python 3 and its standard library. Run `python checks/brute.py` and `python checks/structural.py` from the directory containing this document. The first independently tests all size-eleven subsets of the *whole* simplex for \(n=4,5\) (respectively 1,365 and 352,716 subsets). It obtains 12 and 24 admissible codebooks. The second enumerates all candidates allowed by the proven monochromatic-incidence restriction, using direct six-output trace tests, for every length \(4\le n\le40\). It confirms respectively three Type I and \(12n-39\) Type II optimizers at every length; the last total is 444 at \(n=40\). Recorded stdout is included in `checks/brute.out` and `checks/structural.out`. These finite checks do **not** prove the theorem for all \(n\); the complete incidence proof above does.

## Relationship to prior work

Multiset deletion codes use multiplicity vectors, whose unordered deletion shadows and unique-decoding properties were studied by Kreindel, Barouch Essayag and Zabokritskiy (arXiv:2601.05636, first public 9 January 2026), and in their follow-up on deletion-ball geometry (arXiv:2603.18322, first public 18 March 2026). Both concern primarily **unique** decoding and general geometric bounds, not the exact family of **four-list optimal codebooks**.

The public result *High-list saturation for ternary two-symbol multiset deletion codes* proves the optimal cardinality for all \(L\ge5\) in a uniform length regime and explicitly notes the separately known capacity \(11\) for \(L=4\). It also gives an even-list structural rigidity statement only for \(L\ge6\). The present theorem **does not claim the capacity eleven as new**: its contribution is the all-length classification of every maximizing subset at \(L=4\), the exact labeled optimizer count \(12n-36\), and the two distinct equality structures. In contrast to the \(L\ge6\) saturation regime, some four-list maxima necessarily replace two one-heavy vectors by a two-heavy one. The general prior two-survivor unique-decoding and small-list results do not imply this optimizer census.

## Limitations

The alphabet size is exactly three, the list allowance exactly four, and the survivor size exactly two. The explicit formula counts labeled-alphabet codebooks, not equivalence classes under symbol permutations. The classification does not claim a formula for the sizes or counts of suboptimal codes. Earlier unindexed or inaccessible work with an equivalent optimizer census remains a priority risk. The result has undergone only the review documented here; there is no independent audit or formal proof-assistant certification.

## References

1. A. Kreindel, I. Barouch Essayag, A. L. Zabokritskiy, *Multiset Deletion Codes: Cyclic Syndrome Constructions, Bounds, and Exact Results*, arXiv:2601.05636, first publicly submitted 9 January 2026, https://arxiv.org/abs/2601.05636 .
2. A. Kreindel, I. Barouch Essayag, A. L. Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322, first publicly submitted 18 March 2026, https://arxiv.org/abs/2603.18322 .
3. *High-list saturation for ternary two-symbol multiset deletion codes*, available online, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-high-list-saturation-for-ternary-two-symbol-multiset-deletion-co--99b929446e96 .
4. *Sharp list-capacity plateau for high-deletion multiset channels*, available online, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-list-capacity-plateau-for-high-deletion-multiset-channels--992c110431e7 .
