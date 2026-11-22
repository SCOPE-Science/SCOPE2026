# The exact random-tie output law of a binary four-mer greedy-superstring obstruction

## Finding
For the eight distinct binary four-mers
\(S=\{\mathtt{0000},\mathtt{0001},\mathtt{0010},\mathtt{0011},\mathtt{0100},\mathtt{0101},\mathtt{1000},\mathtt{1010}\}\), let \(X\) be the final length produced by ordinary ordered maximum-suffix-prefix-overlap greedy merging. At every stage, choose **uniformly and independently** from the ordered pairs of distinct current components attaining the globally largest proper suffix-prefix overlap (zero overlaps included). Merge the chosen pair. Starting from the eight equal-length, substring-free input words, stop with one component. Then the complete distribution of \(X\) is

| \(j\) | \(\Pr(X=j)\) |
|---:|---:|
| 11 | \(928099/4989600\) |
| 12 | \(617809/3326400\) |
| 13 | \(195829/680400\) |
| 14 | \(8384459/29937600\) |
| 15 | \(38719/855360\) |
| 16 | \(41/5040\) |
| 17 | \(13939/1995840\) |

All other lengths have probability zero. In particular \(\Pr(X=17)=13939/1995840\), and \(\mathbb E X=3209609/249480\). The optimal superstring length is 11, witnessed by \(\mathtt{00101000011}\), and the maximum possible greedy length is 17. Thus the strict \(3/2\)-approximation-loss event has the exact probability \(13939/1995840\). The same law holds for each image of \(S\) under reversing every word and/or complementing every bit.

## Assumptions and scope
A proper suffix-prefix overlap \(o(u,v)\) is the greatest \(t\) with \(0\le t<\min(|u|,|v|)\) for which the last \(t\) letters of \(u\) equal the first \(t\) of \(v\). A merge produces \(u\) followed by the remaining \(|v|-t\) letters of \(v\). Do not deduplicate or discard unrelated components after a merge. An ordered pair is chosen uniformly among all maximum-overlap eligible ordered pairs; this is **not** the distribution from sampling random total permutations of ties. All probabilities are exact rationals. Only the displayed eight-read instance and its reversal/complement images are claimed, not arbitrary inputs.

## Proof
Represent each active component by the ordered list \(p\) of its constituent original read indices. Because the original reads all have common length four and are distinct, every component carries a first and a last index. For this specific input, a separate exhaustive traversal of the directly merged-string states checks that no legal maximal-overlap merge has overlap greater than three and that no unrelated component is absorbed. Thus the path endpoint reduction is valid **on these reachable states**, rather than assumed for arbitrary inputs. The standalone direct-string recursion independently evaluates the exact law without relying on this reduction.

For a set \(P\) of ordered index lists, let \(h(P)=\max_{p\ne q}o(\mathrm{last}(p),\mathrm{first}(q))\), let \(E(P)\) be the set of ordered pairs attaining \(h(P)\), and define the probability generating polynomial for the *remaining accumulated overlaps* recursively:
\[
F_P(z)=\frac{1}{|E(P)|}\sum_{(p,q)\in E(P)}z^{h(P)}F_{(P\setminus\{p,q\})\cup\{pq\}}(z),\qquad F_{\{p\}}(z)=1.
\]
All states strictly reduce the number of components, so this is a finite induction, not a simulation estimate. If the accumulated overlaps equal \(r\), the final length is \(32-r\). Exact rational evaluation of this recurrence in `verify_paths.py` reaches 428 memoized states and yields the seven rational probabilities above. An independently written direct-string recursion in `verify_strings.py` reaches 418 memoized string states and yields precisely the same seven probabilities. Both check normalization to one by exact fraction arithmetic. The minimum superstring length 11 follows from eight distinct length-four factors requiring at least eight starting positions in any linear word, and the length-11 witness above realizes the bound. The reflection and complementation bijections carry every eligible ordered merge to an eligible merge and preserve its probability, proving the symmetry statement.

## Verification
Run `python verify_paths.py` and `python verify_strings.py` with Python 3's standard library. Their exact results are preserved in `verify_paths_output.txt` and `verify_strings_output.txt`. The programs enumerate all greedy tie choices recursively with fractions rather than using randomized trials. The identical output laws, including \(\Pr(X=17)\) and normalization, provide two independent computational routes. The finite recurrence proves this claim for the fixed eight-word input; it makes no assertion concerning other numbers of input words.

## Relationship to prior work
The general maximum-overlap greedy-superstring approximation problem and the difficulty of its tie behavior are treated in Chukhin et al., *The Greedy Superstring Conjecture Is False* (arXiv:2609.01365, first public version September 1, 2026). Kulikov, Savinov and Sluzhaev analyze greedy merging of length-four strings at CPM 2015. An earlier exact extremal census of binary four-mers identifies a minimal eight-word strict \(3/2\) obstruction and its worst-case length, but the existential worst length does not imply any of the transition probabilities or the exact distribution in this result. The present result quantifies the random-tie robustness of one such intrinsically motivated extremal input.

## Limitations
This is an exact, narrowly scoped probability law for one extremal symmetry orbit, not a distribution over all binary four-mer sets, and it depends on **uniform ordered-pair tie resolution**. The two computations are finite exhaustive certificates, not independent peer review. A previously unindexed equivalent probability census remains a possible priority risk.

## References
- *The Greedy Superstring Conjecture Is False*, arXiv:2609.01365v1 (2026-09-01), https://arxiv.org/abs/2609.01365.
- A. Kulikov, S. Savinov, and G. Sluzhaev, *Greedy Conjecture for Strings of Length 4*, CPM 2015 presentation, https://cpm.cs.helsinki.fi/cpm15/26_Kulikov.pdf.
