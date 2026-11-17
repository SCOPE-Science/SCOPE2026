# Mixed-prime Moore summands in the alternating quotient of binary-colored injective words

## Finding

Let \(X\) be the regular CW complex of all nonempty binary-colored injective words on the label set \(\{1,2,3,4,5\}\), and let \(A_5\) relabel the first coordinates by even permutations, leaving colors unchanged. Its **ordinary geometric quotient** is

\[
|X|/A_5\simeq M(\mathbb Z/3,3)\vee M(\mathbb Z/30,3)\vee\bigvee^{37}S^4.
\]

Here \(M(\mathbb Z/m,3)\) is the Moore space obtained by attaching a four-cell to a three-sphere with degree \(m\). Consequently the quotient is simply connected and has \(\widetilde H_3\cong\mathbb Z/3\oplus\mathbb Z/30\), \(\widetilde H_4\cong\mathbb Z^{37}\), and zero reduced homology otherwise. The two torsion invariant factors are both essential; the third homology is not cyclic of order ninety.

## Assumptions and scope

A length-\(k\) cell is an ordered word \(((i_1,c_1),\ldots,(i_k,c_k))\), with pairwise distinct \(i_j\in\{1,2,3,4,5\}\), arbitrary \(c_j\in\{0,1\}\), and \(1\le k\le5\). Its \((k-1)\)-dimensional characteristic cell is an oriented simplex whose faces correspond to deleting individual word positions. The signed cellular boundary is the usual alternating deletion sum; thus this is the Boolean CW realization of the nonempty part of the binary-colored injective-word poset. The \(A_5\) action permutes only labels and preserves all cell orientations. A label-permutation stabilizer of any cell fixes that characteristic cell pointwise, so the finite quotient has a cellular structure indexed by the word orbits, with boundary induced directly by orbit projection. There are no nontrivial orientation multipliers or folded-cell boundaries.

## Proof

**1. Orbit cells.** For a word of length \(k\le3\), the five-letter alternating group is transitive on every ordered label \(k\)-tuple: it acts sharply transitively for \(k=3\). Hence a quotient cell is determined by its length-\(k\) color word, giving \(2^k\) cells. For \(k=4\), append the unique omitted label; for \(k=5\), use the complete label word. The parity of the resulting five-letter permutation distinguishes two orbits for every fixed color word. Therefore the quotient cell counts in dimensions \(0,1,2,3,4\) are respectively

\[
(2,4,8,32,64).
\]

**2. Integer cellular differentials.** Index the quotient generators in each dimension by their color word and, when length is four or five, the parity bit. On the representative word \(w\), define \(\partial[w]=\sum_{j=1}^{k}(-1)^{j-1}[w\setminus j]\). For a length-five word, deleting position \(j\) toggles the parity of its length-four face precisely when \(5-j\) is odd. This specifies every matrix entry without an incidence ambiguity. Direct exhaustive integer calculation gives:

| Boundary | Size | Rank | Nonzero Smith invariant factors |
|---|---:|---:|---|
| \(\partial_1\) | \(2\times4\) | 1 | \(1\) |
| \(\partial_2\) | \(4\times8\) | 3 | \(1,1,1\) |
| \(\partial_3\) | \(8\times32\) | 5 | five \(1\)'s |
| \(\partial_4\) | \(32\times64\) | 27 | twenty-five \(1\)'s, \(3\), \(30\) |

All consecutive products vanish exactly over \(\mathbb Z\). Since \(\mathrm{im}\,\partial_3\) is primitive in its target, the torsion in \(C_3/\mathrm{im}\,\partial_4\) is precisely the torsion in \(H_3\). The ranks and Smith factors yield the claimed integral homology. In particular, \(\ker\partial_4\) has rank \(64-27=37\).

**3. Fundamental group.** The two-skeleton has two vertices (the colors), four oriented edges \(e_{ab}\) for ordered color pairs, and eight two-cells indexed by color triples \((a,b,c)\). Such a two-cell gives the group relation \(e_{ab}e_{bc}=e_{ac}\) after the usual connecting-path choices. Choose \(e_{01}\) as a maximal-tree edge. Relations for \((0,0,0)\), \((1,1,1)\), and \((0,1,0)\) respectively eliminate the loops \(e_{00}\), \(e_{11}\), and \(e_{10}\); all remaining generators are tree edges. Thus \(\pi_1=1\). Higher-dimensional cells do not alter this group.

**4. Upgrade to homotopy type.** Let \(Y_3\) be the three-skeleton of the quotient. The computed homology gives \(\widetilde H_2(Y_3)=0\) and \(H_3(Y_3)\cong\mathbb Z^{27}\). Because \(Y_3\) is simply connected, the Hurewicz theorem makes it two-connected and identifies \(\pi_3(Y_3)\) with \(H_3(Y_3)\); a wedge of twenty-seven three-spheres maps to \(Y_3\) by generators, and the homology Whitehead theorem makes this a homotopy equivalence. Every four-cell is consequently attached by a homotopy class in \(\pi_3(\bigvee^{27}S^3)\cong\mathbb Z^{27}\), with attaching-coordinate matrix equal to the last cellular differential after an integral basis identification. Unimodular row and column operations are realized by self-equivalences of the wedge and elementary changes of the attaching-cell basis. Its Smith form is \(\mathrm{diag}(1^{25},3,30,0^{37})\). Unit attachments cancel twenty-five three/four-cell pairs, the two nonunit attachments yield the displayed Moore spaces, and thirty-seven null attachments yield four-spheres. This proves the stated homotopy equivalence.

## Verification

Run `python verify_colored_a5.py` with Python 3 and SymPy 1.14.0 (also recorded in `requirements.txt`). The self-contained verifier enumerates **every** label/color word at lengths one through five, applies all sixty even permutations to validate the orbit classifier, checks every projected incidence against every original labeled word, confirms \(\partial^2=0\), computes all four exact Smith normal forms, and checks the two-skeleton presentation. `verification_output.txt` is the actual successful run output. The finite computation is exhaustive for this particular five-label CW complex; no extrapolation to other sizes or color counts is used.

## Relationship to prior work

Athanasiadis (2016), Example 3.2 and Theorem 4.1, defines precisely the colored injective-word poset and determines the corresponding **rational symmetric-group homology representation**. Those character calculations do not determine the integral cellular Smith invariants of its ordinary \(A_5\) geometric orbit space, in particular the independent three- and thirty-primary torsion factors. Jonsson and Welker (2009) develop the Boolean cell-complex framework for uncolored injective words; that framework alone also does not determine this colored quotient. Work on moment-angle spaces associated with injective-word complexes concerns a different construction, and the one-color case is a proper specialization rather than a formula for binary coloring.

## Limitations

This theorem treats exactly five labels and two colors under label-only \(A_5\) symmetry. It does not classify larger alternating groups, extra color-permutation symmetries, or Borel quotients. The homotopy equivalence does not claim a PL or homeomorphism classification. The computational certificate is exact but uses a mathematical software implementation of Smith normal form, not a separate formal proof assistant. An unindexed equivalent calculation could still exist; no claim of an independently audited publication is made.

## References

1. C. A. Athanasiadis, *The symmetric group action on rank-selected posets of injective words*, arXiv:1606.03829 (first public preprint 2016-06-13), Sections 3–4, especially Example 3.2 and Theorem 4.1. https://arxiv.org/abs/1606.03829
2. J. Jonsson and V. Welker, *Complexes of Injective Words and Their Commutation Classes*, Pacific Journal of Mathematics **243** (2009), 313–329. https://doi.org/10.2140/pjm.2009.243.313
3. W. Chacholski, R. Levi and R. Meshulam, *On the topology of complexes of injective words*, Journal of Applied and Computational Topology **4** (2020), 29–44. https://arxiv.org/abs/1908.03394
