# Three-periodic maximal recolouring mobility of four-coloured squared cycles

## Finding
Let \(C_n^2\) be the graph on the indexed vertices \(\mathbb Z/n\mathbb Z\), with an edge at cyclic distance one or two. Let \(\mathcal R_n\) be the graph whose vertices are all proper maps \(c:V(C_n^2)\to\{0,1,2,3\}\), including maps using only three colours, and whose edges join two maps that differ at exactly one vertex. Colours are named and the cycle vertices are indexed. For every integer \(n\ge6\), the maximum degree \(\Delta_n\) in this recolouring graph satisfies
\[
\boxed{\Delta_n=\begin{cases}
n,&n\equiv0\pmod3,\\
n-5,&n\equiv1\pmod3,\\
n-8,&n\equiv2\pmod3.
\end{cases}}
\]
Furthermore, the number \(M_n\) of colourings of this maximum degree is
\[
\boxed{M_n=\begin{cases}
24,&n\equiv0\pmod3,\\
24n,&n\equiv1\pmod3,\\
6n\binom{h+1}{3}+12n(h-1)+24\mathbf1_{\{n=8\}},
&n=3h+2\quad(h\ge2).
\end{cases}}
\]
The last expression is integral; equivalently it is \(n(h-1)(h^2+h+12)+24\mathbf1_{\{n=8\}}\).

The full degree enumerator \(D_n(t)=\sum_{c\in V(\mathcal R_n)}t^{\deg(c)}\) is also specified exactly by a \(48\)-state transfer: let \(\mathfrak P\) be the \(24\) ordered permutations \(g=(a,b,c,d)\) of the named palette, and set
\[
R(a,b,c,d)=(b,c,a,d),\qquad S(a,b,c,d)=(b,c,d,a).
\]
Define a \(48\times48\) polynomial matrix \(T(t)\), with states \((g,e)\in\mathfrak P\times\{0,1\}\), by the only nonzero transitions
\[
T(t)_{(g,e),(R(g),0)}=t^{\mathbf1_{\{e=0\}}},
\qquad T(t)_{(g,e),(S(g),1)}=1.
\]
Then \(D_n(t)=\operatorname{tr}(T(t)^n)\) for all \(n\ge6\). This last formula gives every intermediate degree multiplicity without asserting a small scalar closed form for them.

## Assumptions and scope
A proper colouring of the square of the simple cycle means that every three consecutive positions have distinct colours, with all subscripts interpreted modulo \(n\). The palette has exactly four available names, but not every colouring needs to use all four. A recolouring changes the colour at one indexed position to one of the other three palette elements, preserving all distance-one and distance-two inequalities. The degree counts distinct resulting maps. All assertions concern the entire infinite family \(n\ge6\). In the expression for \(M_n\), \(h=(n-2)/3\) is an integer only in the third case. The small case \(n=8\) is explicitly exceptional in the multiplicity, not in the maximum degree.

## Proof
**1. A four-colour permutation encoding.** Given a proper cyclic colouring \(c\), take the three distinct successive letters \(c_i,c_{i+1},c_{i+2}\) followed by the fourth unused letter, obtaining an ordered palette permutation \(g_i\). There are exactly two choices for \(c_{i+3}\): reuse \(c_i\), or use the missing fourth letter. Encode the first choice by \(b_i=0\) (a *return*) and the second by \(b_i=1\) (a *switch*). Moving the triple window ahead one site sends \(g_i\) respectively to \(R(g_i)\) or \(S(g_i)\), as explicitly defined above. The operators act on the four positions of a tuple, with \(R^3=S^4=1\). A cyclic binary control word \(b=(b_0,\ldots,b_{n-1})\) gives a valid indexed colouring exactly when the product of its successive \(R\)- and \(S\)-actions is the identity permutation. For each such word there are exactly \(24\) palette-labelled choices of \(g_0\), and conversely the colouring determines both \(g_0\) and \(b\). Hence this correspondence is \(24\)-to-one on control words and one-to-one after specifying \(g_0\).

**2. Mobility is the number of consecutive returns.** A vertex \(i\) has four neighbours in \(C_n^2\). Two of their colours, \(c_{i-2},c_{i-1}\), are different. Since the remaining available colours exclude the current \(c_i\), the vertex can be recoloured precisely when the four neighbours use exactly two colours; in that case there is exactly *one* alternative colour. The triple constraints force the neighbour-colour set to have size two precisely when \(c_{i+1}=c_{i-2}\) and \(c_{i+2}=c_{i-1}\), or equivalently \(b_{i-2}=b_{i-1}=0\). Consequently
\[
\deg(c)=\sum_{i=0}^{n-1}\mathbf1_{\{b_i=b_{i+1}=0\}}.
\]
The matrix \(T(t)\) stores the previous bit and the ordered palette permutation. A length-\(n\) closed walk necessarily satisfies both cyclic bit closure and identity permutation product; its weight is the displayed degree monomial. The trace thus counts each named colouring exactly once and proves the degree enumerator.

**3. A sharp defect bound.** For a cyclic control word with \(k\) switches (ones) and \(r\) positive zero gaps between successive switches, where \(0<k<n\), counting the zero-zero pairs gives
\[
\deg(c)=n-k-r.
\]
Indeed each zero gap of length \(a\ge1\) contributes \(a-1\), and their total length is \(n-k\). For the all-return word (\(k=0\)), the product condition is \(R^n=1\), i.e. \(3\mid n\), and its degree is \(n\). For the all-switch word (\(k=n\)), the condition is \(S^n=1\), i.e. \(4\mid n\), and its degree is zero.

To handle low values of \(k+r\), write an otherwise arbitrary cyclic word with \(k\) switches as \(1^{u_1}0^{a_1}\cdots1^{u_r}0^{a_r}\), with all \(u_j,a_j\ge1\), \(\sum u_j=k\). Its closure is checked by composing the indicated operators. Since \(R^3=1\), each positive \(a_j\) can be replaced by the unique representative in \(\{1,2,3\}\) congruent to it modulo three, without changing the closure, \(r\), or \(n\bmod3\). The following finite multiplication facts are exhaustive; they follow by applying the displayed four-position maps to the initial tuple \((0,1,2,3)\), and `verify.py` independently enumerates the indicated finite cases:

- For \(k=2\), the product is the identity only when the two zero gaps are both congruent to two modulo three; thus \(n\equiv0\pmod3\).
- For \(k=4\) and \(r\le3\), identity products never have \(n\equiv2\pmod3\). With \(r=1\), identity holds precisely when the single positive zero gap is divisible by three, giving \(n\equiv1\pmod3\). With \(r=4\) and \(n\equiv2\pmod3\), identity holds exactly when all four positive gaps are congruent to one modulo three.
- For \(k=6\) and \(r\le1\), no identity is possible. With \(r=2\) and \(n\equiv2\pmod3\), the identity holds exactly for two blocks of three ones, separated by two positive zero gaps each congruent to one modulo three.

For completeness, the first two facts can also be checked on the canonical form \(10^{a_1}\cdots10^{a_k}\) (allowing zero-length gaps) by reducing each \(a_i\) modulo three. For \(k=2\), the only identity residue vector is \((2,2)\). For \(k=4\), among the identity residue vectors with at most three positive zero gaps none has length congruent to two; at four positive gaps the only relevant identity vector is \((1,1,1,1)\). The six-switch two-run statement is checked by the five possible positive block lengths of the first one-run and the nine ordered pairs of positive gap residues, a \(45\)-case multiplication table. For added transparency, among the identity products with four switches and gap representatives from \(\{0,1,2,3\}\), the numbers by positive-gap count \(r\) and length residue \(n\bmod3\) are:

| \(r\) | residue 0 | residue 1 | residue 2 |
|---:|---:|---:|---:|
| 0 | 0 | 1 | 0 |
| 1 | 0 | 4 | 0 |
| 2 | 0 | 6 | 0 |
| 3 | 4 | 4 | 0 |
| 4 | 5 | 1 | 1 |

These are finite algebraic statements about the fixed four-position maps, not extrapolations from a sample of word lengths.

If \(n\equiv0\pmod3\), the all-return word achieves degree \(n\), the absolute upper bound, and is the only word doing so. If \(n\equiv1\pmod3\), the all-return word is unavailable; the two-switch identity has the wrong residue, and every admissible word of positive degree has \(k+r\ge5\). Exactly four consecutive switches followed by \(n-4\) returns achieve \(k+r=5\) for \(n\ge7\), since \(S^4R^{n-4}=1\) exactly in this residue. For \(n\equiv2\pmod3\), the multiplication facts exclude all \(k+r\le7\) (the only possible cases being two switches, four switches with at most three runs, and six switches with at most one run). Hence \(\deg(c)\le n-8\). This is achieved for \(n=8+3a\), \(a\ge0\), by the identity control words of types \(10^{1+3a}101010\) (four isolated switches) or \(1110^{1+3a}1110\) (two triple-switch blocks). The all-switch word is an additional maximizer only at \(n=8\). These arguments prove the three sharp upper bounds, including \(n=6\), with all-switch possibilities handled explicitly.

**4. Counts of the maximizers.** In residue zero, the unique maximizing control word is all returns, contributing \(24\) named colourings. In residue one, every maximizing word for \(n\ge7\) has a single run of four switches and one positive gap of \(n-4\) zeros. Its \(n\) different cyclic placements give \(24n\) colourings.

Now take \(n=3h+2\ge8\). One type of maximizing control word has four isolated switches with four zero-gap lengths \(1+3a_1,\ldots,1+3a_4\), where the nonnegative integers satisfy \(a_1+\cdots+a_4=h-2\). Selecting a marked switch gives \(n\binom{h+1}{3}\) descriptions, and each word has exactly four marked switches, so the number of words of this type is \(\frac n4\binom{h+1}{3}\). The other type has two runs \(111\) with zero gaps of lengths \(1+3a\), \(1+3b\), where \(a+b=h-2\). Marking either one of the two identical switch-runs gives \(n(h-1)\) descriptions, so their number is \(\frac n2(h-1)\). At \(n=8\) only, the all-switch word has the same degree zero and contributes one more control word. Multiplying the sum by \(24\) proves the exact maximizing-colouring formula.

## Verification
Run `python3 verify.py` with the Python 3 standard library in the same directory. The program reconstructs the return/switch maps, verifies the finite group residue cases needed for the bound, computes all cyclic identity control words through length \(18\), computes the weighted transfer trace through length \(12\), and independently enumerates all proper named four-colourings through length \(15\) (fixing the initial three colours and multiplying by the free \(24\)-fold palette action). The two methods give identical complete degree distributions for lengths \(6\) through \(15\), and the sharp maxima and counts agree through length \(18\). Expected terminal marker: `VERIFY_OK group_relations=checked finite_gap_table=checked transfer_orders=6..12 direct_coloring_orders=6..15 binary_products_orders=6..18 extremal_counts=6..18`. The infinite statement follows from the encoding and exhaustive small group identities, not from finite-range numerical agreement.

## Relationship to prior work
The recolouring graph and frozen-colouring condition are standard; see Belavadi, Cameron and Merkel (arXiv:2206.09268, first submitted 18 June 2022), especially Sections 1 and 3, for the one-vertex recolouring definition and general graph-class connectivity rather than squared-cycle local degree extrema. Fujii, Iwamasa, Kimura and Suzuki (ISAAC 2022) study algorithmic recolouring under restrictions on permitted colour changes, rather than the sharp degree spectrum of these cyclic-square colouring graphs. Relevant published work on squared cycles, *Fall-coloring spectrum and complete color-class enumerator of squared cycles* (2026), computes frozen colourings, namely degree-zero states for a fixed palette, and their existence/count; it does **not** supply the maximal positive recolouring degree or the nonzero-degree maximizing populations claimed here. In particular, the fact that all \(168\) four-colourings of \(C_8^2\) are frozen is compatible with that existing result and is not isolated as a separate novelty claim. No previously inspected result yielded the three-residue sharp maximum and complete extremizer classification. Searches are not an unconditional priority proof.

## Limitations
Only the palette of four named colours, the ordinary square of a labelled simple cycle, and one-site recolourings are treated. There is no claim of connectedness, mixing, or an optimal path algorithm for the recolouring graph. The degree enumerator is given by a finite matrix trace, not by a factored scalar rational function. The proof uses finite group multiplication with complete small-case classifications; the standalone checker is corroboration and reproducibility, not independent certification. Related unindexed or differently phrased formulas may exist. Independent mathematical audit has not been performed.

## References
1. M. Belavadi, K. Cameron and O. Merkel, *Reconfiguration of Vertex Colouring and Forbidden Induced Subgraphs*, arXiv:2206.09268 (first public version 18 June 2022), [HTML full text](https://arxiv.org/html/2206.09268v3).
2. S. Fujii, Y. Iwamasa, K. Kimura and A. Suzuki, *Algorithms for Coloring Reconfiguration Under Recolorability Digraphs*, ISAAC 2022, LIPIcs 248, article 4, DOI: 10.4230/LIPIcs.ISAAC.2022.4, [publication](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ISAAC.2022.4).
3. *Fall-coloring spectrum and complete color-class enumerator of squared cycles*, published result (2026), [text](https://github.com/published-finding corpus/2026/blob/main/2026/10/13/SCOPE-fall-coloring-spectrum-and-complete-color-class-enumerator-of-sq--6fa05fffdf4b/RESULT.md).
