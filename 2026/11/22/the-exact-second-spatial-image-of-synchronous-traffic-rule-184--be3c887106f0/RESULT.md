# The exact second spatial image of synchronous traffic Rule 184

## Finding
Let \(F:\{0,1\}^{\mathbb Z}\to\{0,1\}^{\mathbb Z}\) be synchronous elementary cellular automaton Rule 184. Its complete image after exactly two updates is
\[
F^2(\{0,1\}^{\mathbb Z})=X_{\{1100,110100\}},
\]
where \(X_{\mathcal W}\) is the bilateral shift avoiding every contiguous word in \(\mathcal W\). Both forbidden words are minimal. Hence the second image is a shift of finite type with exactly two minimal forbidden words.

Writing \(c_n=|\mathcal L_n(F^2(\{0,1\}^{\mathbb Z}))|\) (including the empty word at \(n=0\)), the exact block-count series is
\[
\sum_{n\ge0}c_n z^n=\frac{1}{1-2z+z^4+z^6}.
\]
In particular, \(c_n=2c_{n-1}-c_{n-4}-c_{n-6}\) for \(n\ge6\), with initial counts \(1,2,4,8,15,28\); and the topological entropy is
\[
h_{\mathrm{top}}(F^2(X))=\log\alpha,\qquad
\alpha^3-2\alpha^2+\alpha-1=0,\quad\alpha\approx1.75487766624669.
\]
The one-step image is the shift avoiding only `1100`, with entropy \(\log\tau\), where \(\tau\approx1.83928675521416\) is the tribonacci root. Thus the second update strictly reduces the spatial entropy.

## Assumptions and scope
The alphabet is binary, the spatial domain is the bilateral infinite integer lattice, and all initial configurations are allowed. For \(a,b,c\in\{0,1\}\), define the synchronous local update
\[
f(a,b,c)=(b\wedge c)\vee(a\wedge\neg b),\qquad (Fx)_i=f(x_{i-1},x_i,x_{i+1}).
\]
The second-iterate local map uses a five-bit input \(abcde\):
\[
g(a,b,c,d,e)=f(f(a,b,c),f(b,c,d),f(c,d,e)).
\]
The term *image* means the complete compact image of the bilateral full shift, not a fixed-size cyclic ring or a set of outputs of one initial configuration. Entropy is spatial topological entropy, not entropy per unit time.

## Proof
**A complete 17-pair finite-state equivalence certificate.** The time-two language is recognized by a nondeterministic labeled de Bruijn graph with sixteen states: state \(v\) is the four-bit integer representing a consecutive input block; for each appended bit \(b\in\{0,1\}\), advance to \((2v+b)\bmod16\) and label the edge by \(g\) on the corresponding five bits. The time-two output words are precisely the label sequences of finite paths, since each finite input block extends to a bilateral configuration. Starting from all sixteen states, take subset transitions for each emitted output bit. A word is allowed precisely when the resulting subset is nonempty.

Independently, a deterministic forbidden-word prefix automaton recognizes the words avoiding `1100` and `110100`. Its six nonrejecting states, in order, are the proper prefixes
\[
\varepsilon,\ 1,\ 11,\ 110,\ 1101,\ 11010.
\]
After each appended output digit, reject if the current suffix completes a forbidden word; otherwise retain the longest suffix that is one of these proper prefixes. Its exact transition table (entries are next-state indices; a dash denotes rejection) is:

| State | Prefix | Append 0 | Append 1 |
|---|---|---|---|
| 0 | empty | 0 | 1 |
| 1 | `1` | 0 | 2 |
| 2 | `11` | 3 | 2 |
| 3 | `110` | reject | 4 |
| 4 | `1101` | 5 | 2 |
| 5 | `11010` | reject | 1 |

The exact synchronized reachability closure of the two automata has seventeen nonrejecting pairs. In the following table, the subset is a sixteen-bit hexadecimal mask indexed by four-bit input states. The two final columns are the paired-state identifiers after emitting each digit, or `-` for joint rejection.

| ID | Subset mask | Prefix state | 0 | 1 |
|---:|:---:|---:|---:|---:|
|0|FFFF|0|1|2|
|1|477F|0|3|4|
|2|B8BF|1|1|5|
|3|077F|0|3|4|
|4|38BF|1|1|5|
|5|8880|2|6|7|
|6|4040|3|-|8|
|7|8080|2|9|10|
|8|3000|4|11|12|
|9|4000|3|-|8|
|10|8000|2|9|10|
|11|0700|5|-|13|
|12|0800|2|14|15|
|13|003F|1|3|16|
|14|0040|3|-|8|
|15|0080|2|9|10|
|16|0880|2|6|7|

The row \(0\) is the initial pair (full subset, empty prefix). Every target is among these seventeen rows; checking each edge by the stated local rule yields the table. Crucially, **both components reject on exactly the same emitted digits**. By induction on word length, the two finite-word languages agree for all lengths. Equality of subshift languages implies equality of the compact bilateral image and the two-forbidden-word shift. Both displayed forbidden words are minimal: `1100` cannot contain `110100`, while `110100` does not contain `1100`, and every proper subword of either is accepted by the prefix automaton.

**Rational counts and entropy.** With rows and columns indexed by the six proper-prefix states above, the edge-count adjacency matrix is
\[
A=\begin{pmatrix}
1&1&0&0&0&0\\
1&0&1&0&0&0\\
0&0&1&1&0&0\\
0&0&0&0&1&0\\
0&0&1&0&0&1\\
0&1&0&0&0&0
\end{pmatrix}.
\]
Every admissible finite word has one deterministic path from state zero, so \(c_n=e_0^\top A^n\boldsymbol1\). Elementary determinant and adjugate computation gives
\[
\det(I-zA)=1-2z+z^4+z^6,
\qquad e_0^\top(I-zA)^{-1}\boldsymbol1=\frac1{1-2z+z^4+z^6}.
\]
The characteristic polynomial factors as
\[
\det(tI-A)=(t^3-t-1)(t^3-2t^2+t-1).
\]
The directed graph of \(A\) is strongly connected and has a loop at state zero, hence is primitive. Its Perron root is the real root \(\alpha>1\) of the second cubic: that root is about \(1.7548776662\), while the first cubic's largest real root is about \(1.3247179572\) and the remaining roots have smaller modulus. Perron–Frobenius theory and the block-growth characterization of shift entropy give \(h_{\mathrm{top}}=\log\alpha\).

Finally the independently known one-step image forbids `1100` alone and has tribonacci growth constant \(\tau>1.839\); hence \(\alpha<\tau\), yielding strict entropy loss. No assertion is made about times three and higher.

## Verification
Run `python3 verify.py` (Python standard library only). It reconstructs the sixteen-state labeled graph from the two-step local rule, synchronizes it with the six-state avoidance automaton and checks every transition in the exact seventeen-pair closure. It independently brute-forces all input blocks giving output lengths one through eleven, compares each resulting language to the two-forbidden-word language, and checks seventeen transfer-matrix word counts and the exact six-lag recurrence. Expected output begins `VERIFY_OK`.

The all-length proof is the finite deterministic closure argument, not numerical experimentation. A full independent external mathematical audit has not been performed.

## Relationship to prior work
De Oliveira, Ruivo, Costa, Miki and Trafaniuc (first online 2015) constructed finite-time elementary-cellular-automaton process graphs, explicitly including Rule 184's first and second graphs in their Figure 8; their Rule 184 section studies subsequent process-graph growth and the limit language. These graphs provide applicable finite-state information, but the inspected text does not give the two-word minimal antidictionary, the exact all-length second-image count series, or its Perron entropy. The present result makes those specific two-step consequences explicit and proves a complete minimal SFT presentation; it does not claim novelty for the process-graph construction.

Recent work on elementary-cellular-automaton causal structure (Pita, first public March 2026) provides an independent motivation for exact finite-state spatial constraints derived from local rules, but does not assert this image theorem. A published first-versus-second image census for all elementary rules establishes that many rules strictly shrink their images at the second step; it does not give the exact second-image language and entropy of Rule 184. An existing exact one-step cyclic image result identifies the `1100` obstruction, but only for one update and periodic input. The two-sided two-step assertion above is different from both. The underlying finite automaton and Perron–Frobenius tools are standard.

## Limitations
The theorem concerns synchronous Rule 184 on the bilateral full shift and **exactly two updates**. It is not a theorem about the full infinite-time limit set, every later image, or exact finite-ring predecessor multiplicities. The smallest forbidden words and the growth rate are mathematical consequences of a finite local graph; historical studies may have encoded the result implicitly in graph tables, and exhaustive bibliographical priority has not been independently established.

## References
- Manuel Pita, *How local rules generate emergent structure in cellular automata*, arXiv:2604.00273v1, first public 2026-03-31, https://arxiv.org/abs/2604.00273.
- P. P. B. de Oliveira, E. L. P. Ruivo, W. L. Costa, F. T. Miki, V. V. Trafaniuc, *Advances in the study of elementary cellular automata regular language complexity*, *Complexity* 21 (2016), 267–279, first online 2015-05-06, https://doi.org/10.1002/cplx.21686.
- *A sharp twelve-symbol threshold for second-update image loss in elementary cellular automata*, public research record (2026-10-26), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-twelve-symbol-threshold-for-second-update-image-loss-in--5742d176c6e4.
- *Exact one-step reachability, inversion, and density spectrum of the cyclic traffic automaton*, public research record (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-one-step-reachability-inversion-and-density-spectrum-of-th--5a87e3038c99.
