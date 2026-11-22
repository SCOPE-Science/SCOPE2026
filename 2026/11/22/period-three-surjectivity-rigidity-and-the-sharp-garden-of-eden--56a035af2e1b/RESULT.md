# Period-three surjectivity rigidity and the sharp Garden-of-Eden horizon for elementary rules

## Finding

Let an ordered triple of elementary binary rules be used periodically across the spatial lattice: at cells congruent to zero, one and two modulo three use rules \(f\), \(g\), and \(h\), respectively. Among all \(256^3=16{,}777{,}216\) such labelled triples, **exactly \(12{,}888\) give a globally surjective map** on the bi-infinite full shift. Every surjective triple has **at least two constituents which, when used homogeneously, are surjective**. This restriction is sharp: \((f,g,h)=(23,60,102)\) is globally surjective although homogeneous Rule 23 is not.

The precise numbers of surjective triples with respectively zero, one, two, and three homogeneous-surjective constituents are \(0,0,2{,}784,10{,}104\). For each of the three possible positions of a sole homogeneous-nonsurjective constituent there are exactly \(928\) surjective triples.

For each nonsurjective triple, the shortest forbidden output word aligned with the three-cell phase and consisting of whole three-cell blocks has length **at most four blocks**. The complete shortest-length distribution is:

| Shortest forbidden length in three-cell blocks | Number of ordered rule triples |
|---|---:|
| 1 | 7,476,480 |
| 2 | 8,825,488 |
| 3 | 453,144 |
| 4 | 9,216 |
| No forbidden word (globally surjective) | 12,888 |

The cutoff is sharp. The triple \((22,22,90)\) has no missing aligned output word of one, two or three blocks, while the length-twelve binary output word `010010010010` has no predecessor.

## Assumptions and scope

Fix \(X=\{0,1\}^{\mathbb Z}\), the bi-infinite binary full shift. A Wolfram-rule integer \(r\in\{0,\ldots,255\}\) denotes the local map

\[
r(a,b,c)=\bigl\lfloor r/2^{4a+2b+c}\bigr\rfloor\bmod 2,
\qquad a,b,c\in\{0,1\}.
\]

For every ordered \((f,g,h)\in\{0,\ldots,255\}^3\), define \(H_{f,g,h}:X\to X\) by

\[
(H_{f,g,h}x)_{3j+t}=r_t(x_{3j+t-1},x_{3j+t},x_{3j+t+1}),
\quad j\in\mathbb Z,\quad t\in\{0,1,2\},
\]

with \((r_0,r_1,r_2)=(f,g,h)\). "Homogeneous-surjective" for rule \(r\) means that \(H_{r,r,r}\) is globally surjective on \(X\). No periodic boundary conditions are imposed on the spatial configurations. The term "shortest forbidden" concerns phase-zero-aligned output segments \([0,3\ell-1]\), and not an unrestricted unaligned length measure.

## Proof

**Finite-state characterization.** Let \(Q=\{00,01,10,11\}\). A three-cell output block depends on five consecutive input bits \((a,b,c,d,e)\); the three output bits are \(f(a,b,c)\), \(g(b,c,d)\), \(h(c,d,e)\). Construct an eight-letter labeled graph on \(Q\) with an arc from \(ab\) to \(de\) bearing the output-block label whenever the intermediate input bit \(c\) makes that five-bit window possible. Thus every labeled path of length \(\ell\) corresponds to at least one finite input of length \(3\ell+2\), with its length-\(3\ell\) output word split into three-bit labels.

For a subset \(S\subseteq Q\) and a three-bit output label \(v\in\{0,\ldots,7\}\), let \(T_v(S)\) be the union of all terminal vertices reachable by an arc with label \(v\) from some vertex of \(S\). A word of \(\ell\) output blocks is obtainable on its finite support **if and only if** the subset reached from initial set \(Q\) under those \(\ell\) transitions is nonempty.

This finite-support criterion is equivalent to global surjectivity: if \(H_{f,g,h}\) is onto, every finite aligned output block occurs. Conversely, if every finite aligned output block has an input, then for any prescribed bi-infinite output, every finite family of coordinate constraints on its preimages has a solution (extend the output segment to phase-zero block boundaries). The closed cylinder constraints have the finite-intersection property inside compact \(X\); hence the whole output has a preimage. It follows that **nonsurjectivity is equivalent to reachability of the empty subset** in the 16-state subset automaton starting at \(Q\). All 15 other subsets are accepting nonempty states. Breadth-first search thus decides global surjectivity and, when false, the exact shortest forbidden aligned length. No finite-input experiment is being mistaken for this all-length equivalence.

**Exact finite census.** The accompanying `checker_grouped.cpp` and `checker_windows.cpp` exhaust all integers \(f,g,h\) from zero through 255, construct the complete transition relation, and run breadth-first search over all nonempty reachable subsets until either the empty subset occurs or the reachability closure is exhausted. The first checker constructs block arcs by extending each start pair with eight three-bit choices and uses the ordinary one-symbol graph for homogeneous surjectivity. The second checker independently enumerates 32 length-five input windows per triple, loops through the ordered triples in a different order, and computes homogeneous surjectivity by a separate three-block subset search. Both programs return *identical* exact counts, including the entire five-row distribution and the \(0,0,2784,10104\) constituent classification. Since the loops traverse precisely \(256^3\) distinct triples, this is an exhaustive **finite** proof of the census. The source and exact build/run instructions are included under Verification; no inaccessible data, files or randomness are required.

**Sharp witness.** For \((f,g,h)=(22,22,90)\), process the output block `010` repeatedly. Starting from the full four-vertex mask `0xF`, the successive subset masks are `0x7`, `0x6`, `0x2`, and `0x0`. Thus `010010010010` is forbidden. The same complete subset search confirms no forbidden word of one, two or three aligned blocks for this triple. Therefore the universal cutoff four is attained. The triple \((23,60,102)\) provides a surjective example with exactly one defective homogeneous constituent, so the restriction requiring at least two surjective constituents is best possible.

## Verification

On an ordinary C++17 compiler, run in the directory containing the two supplied sources:

```sh
g++ -O3 -std=c++17 checker_grouped.cpp -o checker_grouped
./checker_grouped
g++ -O3 -std=c++17 checker_windows.cpp -o checker_windows
./checker_windows
```

The first output labels `count 0` as surjective, and positive counts as shortest missing length; the independent output labels the same bins `L 0`, `L 1`, ... . Both must produce \(12{,}888\), \(7{,}476{,}480\), \(8{,}825{,}488\), \(453{,}144\), and \(9{,}216\) in order. The exact numbers for the constituent-surjectivity masks are zero for masks `0`, `1`, `2`, `4`; \(928\) for masks `3`, `5`, `6`; and \(10{,}104\) for mask `7`. Both total all \(16{,}777{,}216\) triples. Only the finite exhaustive calculation is computer-assisted; the labeled-graph equivalence, compactness argument and interpretation of the masks are proved above.

## Relationship to prior work

Paturi and Kari (first arXiv public release 9 July 2025, subsequently published in 2026) establish the Garden-of-Eden equivalence for recurrent nonuniform rule distributions. Period-three assignments fall within their hypotheses, but their theorem does not supply the exact census, a restricted number of defective constituent rules, or the sharp shortest-forbidden-word cutoff. Salo's 2014 realization paper establishes an automata-theoretic framework for surjectivity of nonuniform rule assignments, and studies elementary-rule *pairs* and more general sofic rule-distribution languages; its inspected treatment does not tabulate the complete ordered period-three family. Dennunzio, Formenti and Provillard (2012) develop decidability tools for nonuniform cellular automata. Those general tools make finite classification possible in principle but do not imply the present explicit all-triples counts without the additional calculation. A separately obtained period-two classification likewise concerns a different assignment family and does not determine the period-three census.

## Limitations

The results concern exactly radius-one binary local rules, a fixed spatial period-three assignment, and phase-zero-aligned forbidden words. They do not classify other periods, larger alphabets or neighborhoods, or arbitrary nonperiodic rule distributions. The exact enumeration is supported by two inspectable programs rather than an independent formal proof assistant or external audit; software/compiler errors remain a residual reproducibility risk. Historical priority is provisional, because an unindexed or unpublished prior enumeration may exist.

## References

1. K. Paturi and J. Kari, *On the surjunctivity and the Garden of Eden theorem for non-uniform cellular automata*, arXiv:2507.06987, first submitted 2025-07-09; *Natural Computing* 25, article 9 (2026). https://arxiv.org/abs/2507.06987 ; https://doi.org/10.1007/s11047-026-10067-8
2. V. Salo, *Realization Problems for Nonuniform Cellular Automata*, preprint dated 2014-09-17, and *Theoretical Computer Science* 559 (2014), 91–107. https://villesalo.com/article/RPfNCA.pdf ; https://doi.org/10.1016/j.tcs.2014.07.031
3. A. Dennunzio, E. Formenti and J. Provillard, *Non-Uniform Cellular Automata: Classes, Dynamics, and Decidability*, *Information and Computation* 215 (2012), 32–46. https://doi.org/10.1016/j.ic.2012.02.008
