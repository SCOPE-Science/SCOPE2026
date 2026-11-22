# Exact random-tie overlap-phase law for the complete binary three-mer superstring instance

## Finding

Let \(S=\{0,1\}^3\) consist of **all eight distinct binary words of length three**. Apply the standard greedy shortest-common-superstring algorithm: at each step, among all ordered pairs of distinct current strings, select uniformly from those maximizing the proper suffix-prefix overlap, merge that pair, and continue until one string remains. Independent ties are selected at successive steps. Write \(X\) for the length of the final linear superstring.

The complete **joint distribution** of the numbers \((N_2,N_1,N_0)\) of merges with overlaps of lengths two, one and zero, respectively, is:

| \(N_2\) | \(N_1\) | \(N_0\) | Exact probability | Output length |
|---:|---:|---:|---:|---:|
| 7 | 0 | 0 | \(1136203/4365900\) | 10 |
| 6 | 1 | 0 | \(18241309/52390800\) | 11 |
| 5 | 2 | 0 | \(140831/635040\) | 12 |
| 6 | 0 | 1 | \(18647/136080\) | 12 |
| 4 | 3 | 0 | \(41/3920\) | 13 |
| 5 | 1 | 1 | \(93/7840\) | 13 |
| 4 | 2 | 1 | \(41/3920\) | 14 |

Every other triple has probability zero. Since every merge reduces the total concatenated length by its overlap, \(X=24-2N_2-N_1\). In particular,

\[
\begin{aligned}
\Pr(X=10)&=1136203/4365900,\\
\Pr(X=11)&=18241309/52390800,\\
\Pr(X=12)&=683551/1905120,\\
\Pr(X=13)&=5/224,\\
\Pr(X=14)&=41/3920.
\end{aligned}
\]

The probabilities sum to one exactly, and
\[
\mathbb E X=167269939/14968800.
\]

The optimal superstring length is ten, so a random ordered-pair tie rule attains an optimum with probability \(1136203/4365900\). The worst greedy length is fourteen, realized with probability \(41/3920\). The optimal length and worst greedy length alone were previously tabulated; the claimed new information is the **full rational law**, especially its seven overlap-phase signatures.

## Assumptions and scope

The input is a set, not a multiset. Strings remain ordered binary words and outputs are linear rather than cyclic. For current strings \(u,v\), an overlap \(o(u,v)\) is the greatest \(j\ge0\) such that a length-\(j\) suffix of \(u\) is a length-\(j\) prefix of \(v\), with both remaining outer parts nonempty. Their merge is \(u\odot v=u\,v[j:]\), in conventional programming notation. Pairs are ordered: \((u,v)\) and \((v,u)\) are different choices. Uniform selection is among **all currently eligible ordered pairs**, not among distinct successor states or among distinct possible overlap lengths. Zero-overlap pairs also participate when no positive overlap remains. All computations use exact rational arithmetic, not sampling.

## Proof

**Optimal length.** Any binary word of length \(L\) has at most \(L-2\) length-three contiguous factors, so covering all eight requires \(L\ge10\). The word `0001011100` has exactly eight length-three windows, all distinct, and therefore witnesses \(\operatorname{OPT}(S)=10\).

**Exact finite-state recurrence.** Let \(\mathcal C\) be a current collection of strings. Define \(P_{\mathcal C}(z)\) to be the probability generating polynomial for the ultimate output length under the specified tie rule. For a singleton \(\{u\}\), set \(P_{\{u\}}(z)=z^{|u|}\). Otherwise define
\[
M(\mathcal C)=\max_{u\ne v\in\mathcal C}o(u,v),\qquad
T(\mathcal C)=\{(u,v):u\ne v,\ o(u,v)=M(\mathcal C)\}.
\]
Then, without approximation,
\[
P_{\mathcal C}(z)=\frac{1}{|T(\mathcal C)|}
\sum_{(u,v)\in T(\mathcal C)}
P_{(\mathcal C\setminus\{u,v\})\cup\{u\odot v\}}(z).
\]
Indeed, the right side conditions on the first selected ordered pair and applies the law of total probability. Each successor has exactly one fewer current string. Thus induction on the number of current strings proves this recurrence accounts for **every** possible greedy execution, with the correct probability, and terminates after seven merges. Sorting current strings only identifies identical states; ordered choices are counted separately before averaging. The executable `verify_literal.py` implements this recurrence directly on literal merged strings, with exact `Fraction` arithmetic and 1,309 reachable memoized states. It asserts that all reachable current collections remain substring-free and that their overlaps are at most two, and evaluates the displayed distribution exactly.

**Independent phase-path recurrence.** By the classical endpoint-overlap lemma for greedy superstring merging on an initially substring-free set (Chukhin et al., Lemma 2.2, arXiv:2608.20018), two current strings formed from disjoint ordered paths of original three-mers overlap by exactly the suffix-prefix overlap between the last original three-mer of the first path and the first original three-mer of the second. Hence a state can instead be represented as an unordered collection of disjoint **ordered paths of input indices**. The overlap weight between paths \(A,B\) is
\[
w(A,B)=\begin{cases}
2,&\text{last two bits of the last word of }A\text{ equal the first two of }B,\\
1,&\text{otherwise, if their last and first bits agree},\\
0,&\text{otherwise}.
\end{cases}
\]
Only currently maximal-weight ordered edges are eligible. The independent `verify_paths.py` transfers exact probability masses **forward**, rather than recursing backward from outputs, and increments one coordinate of \((N_2,N_1,N_0)\) per merge. Its reachable state counts at the eight successive levels are \((1,14,78,220,332,288,224,192)\). The resulting exact seven-cell joint table is as stated and projects onto the same five length probabilities as the literal-string recursion. This second algorithm uses endpoint indices, not reconstructed merged strings, to decide all moves. The endpoint reduction is justified by the cited lemma, and direct literal-state cross-checking independently verifies it for this instance.

**Boundary witnesses.** A legal maximal-overlap execution can finish at length fourteen with the merges, in order: `001`+`010` (overlap 2), `011`+`110` (2), `0110`+`101` (2), `100`+`0010` (2), `000`+`01101` (1), `0001101`+`10010` (1), and `00011010010`+`111` (0), producing `00011010010111`. A length-ten greedy execution follows the successive overlap-two chain `000`,`001`,`010`,`101`,`011`,`111`,`110`,`100`, producing `0001011100`. The exhaustive recursion proves no other lengths or signatures are attainable.

## Verification

Using Python 3 and only the standard library, run `python3 verify_literal.py` and `python3 verify_paths.py`. Both terminate without external data or random sampling; the actual outputs are embedded as `verify_literal.out` and `verify_paths.out`. The former asserts all noncontainment and overlap preconditions and reports 1,309 cached states. The latter independently propagates probability over 1,349 path states across all levels (with phase-signature annotations) and gives all seven exact phase probabilities. Both prove exact total mass one, identical five length probabilities and the mean above. Their source code, not merely recorded logs, is part of this package. Replaying the actual packaged files produced identical outputs.

## Relationship to prior work

Chukhin et al. (arXiv:2608.20018, first public August 20, 2026, Sections 2 and 5) establish the general maximum-overlap endpoint lemma and the all-alphabet worst-case approximation ratio \(9/5\) for inputs of length three. The expanded November 6, 2026 version of arXiv:2609.01365 also analyzes the fixed-length-three bound. These are worst-case guarantees, not probabilities for uniform ordered-pair tie choices on the full binary three-mer input. A published exact binary-three-mer census (*Sharp binary three-word greedy-superstring ratio and all equality cases*) exhausts all 255 nonempty input subsets and, for the full set, records the optimal and worst possible lengths ten and fourteen. Its result and full-set census row do **not** give this seven-cell phase law or the intervening output probabilities; the census explicitly leaves typical tie-breaking unanalyzed. Earlier probability studies of shortest common superstrings sample input strings rather than all tie decisions on this fixed complete input.

## Limitations

This is a finite exact distribution for the canonical complete binary three-mer instance under the **specified** uniform-at-each-merge ordered-pair rule. It neither predicts other input subsets or read lengths nor makes a statement about adversarial tie-breaking on arbitrary instances. The output-length endpoints were already known, so they are not asserted as new. These computations are exhaustive finite proofs, not infinite-family results. Independent mathematical audit and definitive priority verification have not been performed; an unindexed equivalent exact tie law remains possible.

## References

1. N. Chukhin, A. S. Kulikov, I. Mihajlin and A. Smal, *The Greedy Superstring Algorithm Achieves Ratio 2 for Strings of Length 6 Already*, arXiv:2608.20018 (first public 2026-08-20), especially Sections 2 and 5. https://arxiv.org/abs/2608.20018
2. N. Chukhin et al., *The Greedy Superstring Conjecture Is False*, arXiv:2609.01365v2 (initial public version 2026-09-01, revised 2026-11-06), especially Sections 2 and 5. https://arxiv.org/abs/2609.01365
3. *Sharp binary three-word greedy-superstring ratio and all equality cases*, public published-finding corpus mathematical record, 2026-11-08, especially RESULT.md and complete 255-subset census. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-binary-three-word-greedy-superstring-ratio-and-all-equalit--f43f5caa07c5
4. A. Golovnev et al., *Collapsing Superstring Conjecture*, APPROX/RANDOM 2019, article 26. https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2019.26
