# Sharp greedy-superstring ratio and all extremizers for binary four-letter inputs

## Finding

Let \(U=\{0,1\}^{4}\). For a nonempty \(S\subseteq U\), let \(\operatorname{OPT}(S)\) be the minimum length of a string containing every member of \(S\) as a contiguous factor. Starting from the distinct strings in \(S\), the maximum-overlap greedy superstring algorithm repeatedly chooses an **ordered pair of distinct live strings** with largest suffix-to-prefix overlap, replaces them by their maximal-overlap merge, and continues until one live string remains. All maximizing ordered pairs are permitted when there is a tie. Write \(\mathcal G(S)\) for its set of possible final strings.

The sharp worst-case ratio on the binary four-letter domain is
\[
\boxed{\max_{\varnothing\ne S\subseteq U}\;\max_{g\in\mathcal G(S)}\frac{|g|}{\operatorname{OPT}(S)}=\frac{17}{11}.}
\]
One equality witness is
\[
S_*=\{0000,0001,0010,0011,0100,0101,1000,1010\}.
\]
It has \(\operatorname{OPT}(S_*)=11\), attained by the superstring `00101000011`, and admits a legal greedy result `10101000100110000` of length \(17\). Moreover **exactly four** input sets attain the maximum: \(S_*\), the letterwise reversal \(R(S_*)\), bitwise complement \(C(S_*)\), and their composition \(RC(S_*)\). These four sets form one orbit under reversal and complement. Their bitmask indices (lexicographic indexing of all sixteen inputs) are `1343`, `5431`, `60584`, and `64672`.

## Assumptions and scope

Every input is a **distinct** binary word of length exactly four; all \(2^{16}-1=65535\) nonempty subsets of the sixteen possible inputs are considered, including singletons. The greedy algorithm does not choose nonmaximal overlaps and may use arbitrary ordered-pair tie-breaking. A zero-length overlap is permitted. This theorem is not a statement about a larger alphabet, inputs of other lengths, or randomly selected tie-breaks.

For strings \(a,b\), put \(o(a,b)\) equal to the greatest \(t\ge0\) for which the final \(t\) letters of \(a\) equal the initial \(t\) letters of \(b\). For distinct words in \(U\), \(0\le o(a,b)\le3\).

## Proof

**Endpoint lemma.** Each live greedy string is assembled from a nonempty, disjoint ordered group of original inputs. Its first four letters are its first original input, and its last four letters are its last original input. These two original words uniquely determine the overlap between this live string and another live string. Indeed, an overlap of length at least four would make the final original four-letter input of the first string identical to the initial original input of the second, impossible because their groups are disjoint. Therefore all inter-string overlaps lie in \(\{0,1,2,3\}\) and equal the four-word suffix/prefix overlaps of the terminal and initial inputs. Merging groups with endpoints \((a,b)\) and \((c,d)\) produces endpoints \((a,d)\).

**Exact optimum recurrence.** Number the sixteen binary four-letter strings from \(0\) through \(15\) in lexicographic order, and write \(w_i\) for the indexed word. For each nonempty index set \(T\) and \(j\in T\), define
\[
D(\{j\},j)=4,\qquad
D(T,j)=\min_{i\in T\setminus\{j\}}
\bigl(D(T\setminus\{j\},i)+4-o(w_i,w_j)\bigr).
\]
Then \(\operatorname{OPT}(T)=\min_{j\in T}D(T,j)\). One inequality follows from merging the words along each ordered path. Conversely, order one occurrence of each input in an arbitrary common superstring by starting position: consecutive selected occurrences overlap by at most three, and their physical overlap cannot exceed their maximal suffix-prefix overlap. The corresponding ordered-path construction is no longer than that superstring. Thus the recurrence computes the exact optimum, not merely a bound.

**Exact worst-greedy recurrence.** A state \(C\) is a sorted multiset of ordered endpoint pairs \((a_i,b_i)\), one for each live string. Write
\[
m(C)=\max_{i\ne j}o(w_{b_i},w_{a_j}).
\]
Let \(F(C)\) be the least total overlap saved by any legal future greedy execution starting from \(C\). For a singleton \(F(C)=0\). If \(m(C)>0\), then
\[
F(C)=m(C)+\min_{\substack{i\ne j\\o(w_{b_i},w_{a_j})=m(C)}}
F\bigl((C\setminus\{(a_i,b_i),(a_j,b_j)\})\uplus\{(a_i,b_j)\}\bigr),
\]
where the two displayed occurrences are removed separately, even if their endpoint pairs coincide. If \(m(C)=0\), then \(F(C)=0\): no later positive overlap can arise because any new inter-string overlap is an old one between the surviving terminal and initial endpoints. This is exact dynamic programming over **all** legal tie-breakings, including ties of overlap zero. On the initial diagonal state \(C_S=\{(i,i):w_i\in S\}\), the largest legal greedy output length is
\[
G(S)=4|S|-F(C_S).
\]

**Exhaustive finite certificate.** The included standalone C++17 program builds the sixteen-by-sixteen overlap table by literal bit comparisons, computes all \(D(T,j)\), memoizes \(F(C)\) over canonical endpoint-pair states, and scans each integer subset mask from \(1\) to \(65535\). Its comparison \(G(S)/\operatorname{OPT}(S)\) is entirely integer: it uses cross-products, not rounded floating-point thresholds. Resetting the memo cache after each 128 input masks changes no recurrence or mathematical outcome. The recorded full run returned the exact maximum \(17/11\) and exactly four maximizing subsets, with the four masks displayed above. Explicit mask transformations identify those four as the reversal/complement orbit of \(S_*\). Since the recurrence considers every possible nonempty input and every legal tie break, this gives the upper bound and complete extremizer classification for all cases.

For the witness, the seven greedy ordered merges, with overlaps indicated in parentheses, are

`1010 + 0101 (3) -> 10101`;
`1000 + 0001 (3) -> 10001`;
`10001 + 0010 (3) -> 100010`;
`100010 + 0100 (3) -> 1000100`;
`1000100 + 0011 (2) -> 100010011`;
`10101 + 100010011 (1) -> 1010100010011`;
`1010100010011 + 0000 (0) -> 10101000100110000`.

Each selected overlap is globally maximal at the indicated step. The independent witness checker recomputes those legality tests and checks the eleven-letter optimum by enumerating all \(8!\) orders of the eight source words. Hence the ratio \(17/11\) is attained, completing the proof.

## Verification

Compile `verify_greedy_binary4.cpp` using a C++17 compiler and run the executable without arguments; it checks every nonempty binary four-mer input subset, with cache resets used solely for memory management. Independently run `verify_witness.py` with Python 3. These programs use only standard language libraries and embedded input data. The text file `verification_output.txt` contains the output from the finite computations.

## Relationship to prior work

Chukhin, Kulikov, Mihajlin, and Smal (arXiv:2608.20018, August 20, 2026) define the same maximum-overlap greedy model and prove a worst-case ratio of \(9/5\) for **length-three strings over unrestricted alphabets**. Shibata (arXiv:2609.01365, September 1, 2026) finds greater-than-two examples at lengths at least ten over growing alphabets. A September 2026 small-length study proves lower bounds strictly above \(15/8\) for four-letter inputs over **unrestricted alphabets**, and reports the known unrestricted upper bound \(2\). None of these statements computes the sharp ratio for the complete binary four-letter domain. The alphabet restriction matters: this exact binary ratio is strictly smaller than those general-alphabet lower bounds.

## Limitations

This is an exact **finite-domain** classification, not a uniform theorem for all word lengths or alphabet sizes. The exhaustive upper bound relies on correctly executing the provided self-contained recurrence checker; the recurrence and endpoint lemma explain why that finite procedure is a proof. The independent witness checker establishes the lower bound but by itself does not establish the global upper bound. Unindexed equivalent computational results may exist, and no independent external audit has been performed.

## References

1. N. Chukhin, A. S. Kulikov, I. Mihajlin, and A. Smal, *The Greedy Superstring Algorithm Achieves Ratio 2 for Strings of Length 6 Already*, arXiv:2608.20018, first posted 2026-08-20. https://arxiv.org/abs/2608.20018
2. H. Shibata, *Disproving the Greedy Superstring Conjecture*, arXiv:2609.01365, first posted 2026-09-01. https://arxiv.org/abs/2609.01365
3. *The greedy superstring ratio at small string lengths: \(\rho_8,\rho_9,\rho_{11}>2\) and \(\rho_4,\rho_5>15/8\)*, September 2026, https://ideosphere.ai/papers/greedy-scs-v2.pdf
4. B. Cazaux and E. Rivals, *Relationship between superstring and compression measures: new insights on the greedy conjecture*, Discrete Applied Mathematics (2018). https://www.lirmm.fr/~rivals/publication/cazaux-dam-2018/
