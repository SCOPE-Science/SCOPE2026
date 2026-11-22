# Sharp first-forbidden-block horizon for every four-input binary cellular automaton

## Finding

Consider all \(2^{16}=65{,}536\) synchronous one-dimensional binary cellular automata whose local rule reads four consecutive input sites. Define the first-forbidden-block length \(L(r)\) to be the least positive integer \(n\) for which some binary length-\(n\) word is absent from the one-step spatial image of rule \(r\); write \(L(r)=\infty\) for a surjective rule. Then every nonsurjective rule satisfies the **sharp universal bound**

\[L(r)\le 18.\]

The complete census, including rules with \(L(r)=\infty\), is:

| \(L(r)\) | Number of rules |
|---|---:|
| 1 | 2 |
| 2 | 688 |
| 3 | 4,252 |
| 4 | 10,288 |
| 5 | 16,348 |
| 6 | 15,688 |
| 7 | 9,900 |
| 8 | 4,676 |
| 9 | 1,996 |
| 10 | 684 |
| 11 | 304 |
| 12 | 56 |
| 13 | 32 |
| 14 | 8 |
| 15 | 0 |
| 16 | 16 |
| 17 | 12 |
| 18 | 4 |
| \(\infty\) | 582 |

Exactly the four rule numbers `5482`, `22184`, `43351`, and `60053` attain \(L(r)=18\). Each admits **every** output word of length at most 17 but forbids exactly eight output words of length 18. The words `100101010010100101` and `010010110101101010` are respective forbidden witnesses for the first two and the last two rules. In particular, no rule has \(L(r)=15\), while the absolute maximal length is 18.

## Assumptions and scope

Let \(X=\{0,1\}^{\mathbb Z}\). For every integer \(0\le r<65{,}536\), define the local rule \(f_r:\{0,1\}^4\to\{0,1\}\) by

\[f_r(a,b,c,d)=\left\lfloor\frac{r}{2^{8a+4b+2c+d}}\right\rfloor\bmod2,\]

and its global map by \((F_r x)_i=f_r(x_i,x_{i+1},x_{i+2},x_{i+3})\) for every \(i\in\mathbb Z\). A length-\(n\) output word is *present* when it is a consecutive block of at least one member of \(F_r(X)\). Equivalently, there exists a length-\((n+3)\) binary input block producing it. No periodic boundary or fixed input boundary is assumed. The smallest excluded word (if any) is a finite Garden-of-Eden witness; \(L(r)\) counts a block's total length, not a time iterate. These definitions fix the rule numbering and include rules depending on fewer than four input coordinates.

## Proof

**1. Exact language recognition.** Form the binary order-three de Bruijn graph with vertex set \(V=\{0,\ldots,7\}\). For each \(s\in V\) and appended input digit \(b\in\{0,1\}\), there is an edge to \(t=(2s+b)\bmod 8\). Label that edge by \(f_r\) evaluated on the four-bit word of integer value \(2s+b\). A directed path of \(n\) edges corresponds bijectively to a length-\((n+3)\) input word, with the path labels exactly its length-\(n\) output. Therefore a word is present if and only if it labels a finite path beginning at some vertex.

**2. Finite determinization.** Represent the set of all possible current graph vertices by an eight-bit subset \(S\subseteq V\), initially \(S_0=V\). For each requested output \(j\in\{0,1\}\), define

\[\delta_r(S,j)=\{(2s+b)\bmod8:s\in S,\ b\in\{0,1\},\ f_r\bigl(\operatorname{bits}_4(2s+b)\bigr)=j\}.\]

After reading a word \(w\), the determinized state is precisely the set of graph endpoints for paths labeled \(w\), by induction on the length of \(w\). Consequently \(w\) is absent exactly when the corresponding subset equals \(\varnothing\). There are only \(2^8=256\) subset states. Breadth-first search (BFS) from \(V\) on both output symbols, remembering each visited subset, either finds \(\varnothing\) at its exact minimum distance \(L(r)\) or exhausts all reachable subsets without encountering \(\varnothing\). In the latter case every finite output word is present, so compactness of \(X\) (or a nested finite-preimage cylinder argument) makes \(F_r\) surjective: every bi-infinite output has a preimage.

**3. Exhaustive finite certificate.** The embedded standalone programs `verify_census.cpp` and `verify_census.py` implement this transition relation and examine each integer rule from 0 through 65,535 **without sampling**. Each enumerator searches at most 256 subset states for each rule and increments exactly one histogram bin. The Python implementation explicitly constructs the sixteen four-bit edges and their output-labeled successor sets; the C++ implementation constructs transitions by binary shifts. Both independently return the complete displayed histogram and the exact four maximizers, with all integer comparisons. The Python verifier additionally checks the two 18-digit witness strings, confirms that each exceptional rule has zero absent length-17 words and exactly eight absent length-18 words via integer path-counting on deterministic subsets, and compares the predicted short-language fullness with direct enumeration of finite input blocks for nine sample rules. Thus the universal bound, sharpness, exceptional set, and absence of the length-15 stratum follow by finite exhaustive proof, not extrapolation from experimental lengths.

## Verification

From a directory containing the two included independent checker files, execute `python3 verify_census.py`; then execute `c++ -std=c++17 -O2 verify_census.cpp -o verify_census && ./verify_census`. Both print the full histogram, with `-1` in the compiled output representing \(\infty\). The Python checker asserts each census bin and exactly the four length-18 rules; independently enumerates finite input blocks for the stated controls; and checks the complete missing-word count at the sharp boundary. All tests completed successfully when the package was prepared. Their finite exhaustive nature is sufficient because the language-to-subset-automaton equivalence is proved for **arbitrary word length** above.

## Relationship to prior work

Gravner and Kulhanek (2026, publicly posted October 22) study randomly chosen one-dimensional cellular automata through labeled de Bruijn graphs and derive asymptotic probabilistic results; the present sharp all-rule, four-site first-forbidden-horizon histogram is a finite distribution of a different invariant. Fukś and Skelton (2012, Section 2.1, Table 1) already report the total \(582\) surjective rules among all \(65{,}536\) four-site binary rules. **That total is prior knowledge and is not the new claim.** Their inspected paper does not state the finer \(L(r)\) distribution, sharp horizon, or four extremal rule numbers. Known first-offender results for elementary three-site automata and second-update image tests concern different domains and do not imply these four-site, one-step counts. The elementary subset-automaton mechanism is standard; the claimed contribution is the complete exact finite census and its sharp obstruction horizon.

## Limitations

The result is restricted to one spatial dimension, binary alphabet, exactly four **available consecutive input positions**, and the **one-update spatial image**. It is not a claim about first forbidden words of later iterates, cyclic-ring reachability, arbitrary neighborhood shapes, or all neighborhood lengths. The computational certificate does not provide a shorter conceptual classification of individual rules. Exhaustive verification covers the declared finite rule family; independent mathematical audit and unrestricted historical-priority certification have not been performed. Earlier unpublished or machine-generated tables might contain overlapping finite data.

## References

1. J. Gravner and T. Kulhanek, *Random Cellular Automata and deBruijn Graphs*, arXiv:2610.31764v1, publicly posted 2026-10-22, https://arxiv.org/abs/2610.31764 .
2. H. Fukś and A. Skelton, *Classification of two-dimensional binary cellular automata with respect to surjectivity*, Proceedings CSC 2012, Section 2.1 and Table 1 (including one-dimensional counts), https://worldcomp-proceedings.com/proc/p2012/CSC2550.pdf .
3. J. Kari, *Lecture Notes on Cellular Automata*, 2022, https://users.utu.fi/jkari/wp-content/uploads/sites/1251/2022/03/fullnotes.pdf .
