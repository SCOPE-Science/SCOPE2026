# A sharp five-pair Garden-of-Eden test for all alternating elementary cellular automata

## Finding

For each ordered pair of elementary binary local rules \((f,g)\), apply \(f\) on even sites and \(g\) on odd sites of the bi-infinite binary lattice. Define \(L(f,g)\) to be the least positive number of consecutive **even-aligned output pairs** with an unattainable word, and put \(L(f,g)=\infty\) if every such finite word is attainable. Among all \(256^2=65{,}536\) ordered pairs, the exact distribution is

| \(L(f,g)\) | \(\infty\) | \(1\) | \(2\) | \(3\) | \(4\) | \(5\) |
|---|---:|---:|---:|---:|---:|---:|
| Number of ordered rule pairs | 708 | 8,552 | 38,436 | 15,920 | 1,776 | 144 |

There are no finite values exceeding five. Therefore **global surjectivity is equivalent to the attainability of every ten-bit output word at even-aligned coordinates**. The bound is sharp: the ordered rule pair \((22,105)\) has \(L(22,105)=5\).

Of the 708 globally onto alternating rules, 612 have both homogeneous constituents onto, 96 have exactly one homogeneous constituent onto, and none has two non-onto homogeneous constituents. Thus spatial alternation can restore surjectivity to a pair with one non-onto constituent; for example, \((51,54)\) is onto, although homogeneous Rule 54 is not.

The finer joint distribution, with rows denoting how many of the two individual homogeneous rules are onto, is

| Onto homogeneous constituents | \(L=\infty\) | \(L=1\) | \(L=2\) | \(L=3\) | \(L=4\) | \(L=5\) |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 7,556 | 32,400 | 10,768 | 336 | 16 |
| 1 | 96 | 984 | 5,920 | 5,056 | 1,376 | 128 |
| 2 | 612 | 12 | 116 | 96 | 64 | 0 |

## Assumptions and scope

Let \(X=\{0,1\}^{\mathbb Z}\), with the product topology. For a Wolfram-rule number \(r\in\{0,\ldots,255\}\), use the standard encoding
\[
r(a,b,c)=\left\lfloor\frac{r}{2^{4a+2b+c}}\right\rfloor\bmod2,\qquad a,b,c\in\{0,1\}.
\]
For ordered rules \((f,g)\), define \(H_{f,g}:X\to X\) by
\[
(H_{f,g}x)_{2j}=f(x_{2j-1},x_{2j},x_{2j+1}),\qquad
(H_{f,g}x)_{2j+1}=g(x_{2j},x_{2j+1},x_{2j+2}),\quad j\in\mathbb Z.
\]
A word of length \(k\) over the pair alphabet \(\{00,01,10,11\}\) is attainable if some input configuration produces that output on coordinates \(0,\ldots,2k-1\). Write \(L(f,g)=\infty\) when all such words at all lengths are attainable. This is equivalent to surjectivity on the entire bi-infinite full shift by compactness, not merely finite-ring surjectivity. The phase origin is fixed at the even site; swapping rules corresponds to shifting the phase and preserves surjectivity but not necessarily the displayed first-missing-word phase convention. In fact the least blocked *pair length* in the two phases need not agree, and no phase-independent sharp bound is asserted beyond the stated even-aligned formulation.

## Proof

Group sites in consecutive input pairs and introduce eight vertices, each indexed by a three-bit input state \(u=(a,b,c)\in\{0,1\}^3\). From \(u=(a,b,c)\), for every pair \((d,e)\in\{0,1\}^2\), draw an edge to \(v=(c,d,e)\) labeled by the pair
\[
\ell_{f,g}(a,b,c,d,e)=\bigl(f(a,b,c),\ g(b,c,d)\bigr).
\]
A path of \(k\) such edges corresponds exactly to an input word of \(2k+3\) bits that produces its length-\(k\) pair-label sequence. Initial and final vertices are unrestricted. Therefore a pair-output word is attainable if and only if the labeled graph contains a path spelling it.

For a set \(S\) of the eight vertices and output label \(y\) among the four pairs, write
\[
T_y(S)=\{v:\text{there is a }y\text{-labeled edge }u\to v\text{ with }u\in S\}.
\]
Starting at \(S_0\), the full eight-vertex set, successively apply \(T_y\) for the letters of a proposed output word. That word is unattainable exactly when the resulting subset is empty. Thus there is a **complete finite-state decision procedure**: breadth-first search over the at most \(2^8=256\) subsets, with four transitions from each; the first transition to the empty set occurs at the shortest forbidden pair-word length, and no reachable empty set means no forbidden word at any length. Breadth-first search never interprets the failure to encounter a forbidden word at a bounded length as proof by itself: full closure of the finite reachable subset graph is the certificate.

The embedded program `verify_subset.c` implements that exact decision procedure for every integer pair \((f,g)\) in \(0\le f,g\le255\), enumerating every subset transition and giving the complete histogram and cross-tabulation displayed above. All arithmetic is integer/bitwise; there are no numerical tolerances or heuristic cutoffs. A second independently constructed program `verify_windows.c` evaluates all \(2^{12}=4096\) possible finite input windows directly for every ordered rule pair, and reproduces all output-word reachability statuses through five pairs. The two methods agree on the exact distribution.

The finite-graph argument proves the absence of forbidden words at *all* lengths whenever the search terminates without reaching the empty subset. Any bi-infinite output has preimages for all finite sets of coordinates when all finite pair words are attainable. These are finite cylinder constraints on the compact space \(X\); their finite intersection property yields a single global preimage. Conversely a missing pair word clearly prevents surjectivity. Consequently the reported 708 onto cases and five-pair sharp horizon hold on \(X\), without a finite-ring or random-sampling assumption.

## Verification

From the extracted package directory, run:

```sh
cc -O2 -std=c11 -Wall -Wextra verify_subset.c -o verify_subset
./verify_subset
cc -O2 -std=c11 -Wall -Wextra verify_windows.c -o verify_windows
./verify_windows
```

The first program prints the complete five-row cross-tabulation and the 708/8552/38436/15920/1776/144 length histogram, checks 30 onto homogeneous elementary rules, and tests the sharp and mixing witnesses. The second independently enumerates complete twelve-bit input windows and must print the same length histogram. A nonzero exit indicates failed built-in checks. The direct-window test alone does not prove an infinite-length claim; the closed subset graph provides that step.

## Relationship to prior work

Paturi and Kari (first public 9 July 2025) study Garden-of-Eden properties for nonuniform cellular automata with recurrent local-rule distributions; a two-periodic rule assignment is a natural special case, but their general theorem does not supply this all-pairs census or first-forbidden-word cutoff. Paturi's separate 2025 paper establishes balancing and reversibility properties for recurrent distributions, without these exact enumerations. Dennunzio, Formenti and Provillard develop finite-automaton techniques for nonuniform cellular-automaton decision questions; the decision method is prior knowledge and is not claimed as new. The 2014 realization-problem literature studies the sofic set of surjective rule distributions for selected local-rule alphabets, again not the numerical census or sharp depth for *all* 256 elementary rules. Existing uniform elementary-automaton image and finite-ring classifications do not directly imply the displayed period-two spatial-alternation table or its exact five-pair horizon.

## Limitations

This is an exact finite-parameter classification for **two alternating radius-one binary rules**, not a general theorem for arbitrary spatial periods, alphabet sizes, or larger radii. It concerns one simultaneous update on the bi-infinite lattice. It does not enumerate arbitrary finite-ring images, temporal iterates, injective systems, or dynamical orbit types. The independent checker has no role in establishing all-length completeness beyond the finite graph argument. Exhaustive source searching is not a proof of historical priority. A potentially relevant 2024 paper on randomly mixed diploid automata was accessible only by abstract; it treats probabilistic mixing and qualitative dynamical classification, and the possibility of uncatalogued partial overlap remains. Independent mathematical audit has not been performed.

## References

1. K. Paturi and J. Kari, *On the surjunctivity and the Garden of Eden theorem for non-uniform cellular automata*, arXiv:2507.06987, first public 2025-07-09, https://arxiv.org/abs/2507.06987.
2. K. Paturi, *Reversibility, balance and expansivity of non-uniform cellular automata*, arXiv:2507.06896, first public 2025-07-09, https://arxiv.org/abs/2507.06896.
3. A. Dennunzio, E. Formenti and M. Provillard, *Non-uniform Cellular Automata: classes, dynamics, and decidability*, arXiv:1107.5228, https://arxiv.org/abs/1107.5228.
4. *Realization problems for nonuniform cellular automata*, Theoretical Computer Science 559 (2014), 91–107, https://doi.org/10.1016/j.tcs.2014.07.031.
5. S. Roy et al., *Are Some Family Members Harmful? – A Study on Diploid Cellular Automata*, ACRI 2024, https://doi.org/10.1007/978-3-031-71552-5_2 (abstract inspected; full chapter unavailable).
