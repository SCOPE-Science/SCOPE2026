# Twenty-five Frobenius spectra of Zariski chambers on smooth cubic surfaces

## Finding

**Theorem (full equivariant chamber classification).** Let \(S/\mathbb F_q\) be any smooth cubic del Pezzo surface and let \(F\) be its arithmetic Frobenius action on the geometric twenty-seven lines. A geometric Zariski chamber is labeled by the (possibly empty) support of the negative part of its Zariski decompositions. There are precisely \(2,764\) such chambers, with support-size polynomial

\[
1+27t+216t^2+720t^3+1080t^4+648t^5+72t^6.
\]

For each of the \(25\) conjugacy classes of \(W(E_6)\), the **entire cycle profile** of its action on the \(2,764\) geometric chambers is the one in the table below. These \(25\) conditional cases cover the Frobenius types of every smooth cubic del Pezzo surface over every finite field. In particular, the number of chambers descending to \(\mathbb F_q\) is the entry in the last column. Two conjugacy classes with the identical line splitting type \(3^9\) nevertheless have respectively \(1\) and \(13\) rational chambers. The twenty-seven-line splitting profile alone therefore does **not** determine arithmetic Zariski-chamber descent.

The table identifies a class by the combination of **element order, conjugacy-class cardinality, and its twenty-seven-line cycle partition** (these combined identifiers are unique among the \(25\) rows). The last profile is the chamber permutation cycle partition; exponent notation \(d^m\) denotes \(m\) cycles of length \(d\). The index numbers are table-local, **not** the Carter indices in other references.

| Case | Order | Class size in \(W(E_6)\) | Line cycles | Chamber cycles | Rational chambers |
|---|---:|---:|---|---|---:|
| 01 | 1 | 1 | \(1^{27}\) | \(1^{2764}\) | 2,764 |
| 02 | 2 | 45 | \(1^{3}\,2^{12}\) | \(1^{4}\,2^{1380}\) | 4 |
| 03 | 2 | 540 | \(1^{3}\,2^{12}\) | \(1^{36}\,2^{1364}\) | 36 |
| 04 | 2 | 270 | \(1^{7}\,2^{10}\) | \(1^{160}\,2^{1302}\) | 160 |
| 05 | 2 | 36 | \(1^{15}\,2^{6}\) | \(1^{648}\,2^{1058}\) | 648 |
| 06 | 3 | 240 | \(1^{9}\,3^{6}\) | \(1^{142}\,3^{874}\) | 142 |
| 07 | 3 | 80 | \(3^{9}\) | \(1\,3^{921}\) | 1 |
| 08 | 3 | 480 | \(3^{9}\) | \(1^{13}\,3^{917}\) | 13 |
| 09 | 4 | 540 | \(1\,2^{3}\,4^{5}\) | \(1^{2}\,2^{79}\,4^{651}\) | 2 |
| 10 | 4 | 3,240 | \(1\,2^{3}\,4^{5}\) | \(1^{10}\,2^{75}\,4^{651}\) | 10 |
| 11 | 4 | 540 | \(1^{3}\,4^{6}\) | \(1^{4}\,4^{690}\) | 4 |
| 12 | 4 | 1,620 | \(1^{5}\,2\,4^{5}\) | \(1^{30}\,2^{65}\,4^{651}\) | 30 |
| 13 | 5 | 5,184 | \(1^{2}\,5^{5}\) | \(1^{9}\,5^{551}\) | 9 |
| 14 | 6 | 2,160 | \(1\,2^{4}\,3^{2}\,6^{2}\) | \(1^{10}\,2^{66}\,3^{50}\,6^{412}\) | 10 |
| 15 | 6 | 1,440 | \(1^{3}\,2^{3}\,3^{4}\,6\) | \(1^{42}\,2^{50}\,3^{202}\,6^{336}\) | 42 |
| 16 | 6 | 1,440 | \(1^{3}\,2^{3}\,6^{3}\) | \(1^{4}\,2^{69}\,6^{437}\) | 4 |
| 17 | 6 | 720 | \(3\,6^{4}\) | \(1\,3\,6^{460}\) | 1 |
| 18 | 6 | 1,440 | \(3\,6^{4}\) | \(1\,2^{6}\,3\,6^{458}\) | 1 |
| 19 | 6 | 4,320 | \(3\,6^{4}\) | \(1^{3}\,2^{5}\,3^{11}\,6^{453}\) | 3 |
| 20 | 6 | 1,440 | \(3^{5}\,6^{2}\) | \(1^{3}\,2^{5}\,3^{215}\,6^{351}\) | 3 |
| 21 | 8 | 6,480 | \(1\,2\,8^{3}\) | \(1^{2}\,2\,8^{345}\) | 2 |
| 22 | 9 | 5,760 | \(9^{3}\) | \(1\,9^{307}\) | 1 |
| 23 | 10 | 5,184 | \(2\,5^{3}\,10\) | \(1^{3}\,2^{3}\,5^{129}\,10^{211}\) | 3 |
| 24 | 12 | 4,320 | \(1\,4^{2}\,6\,12\) | \(1^{2}\,2^{4}\,4^{33}\,6^{25}\,12^{206}\) | 2 |
| 25 | 12 | 4,320 | \(3\,12^{2}\) | \(1\,3\,12^{230}\) | 1 |

For each case with chamber cycle multiplicities \(m_d\), the number of chambers descending over the extension \(\mathbb F_{q^n}\) is \(N_n=\sum_{d\mid n}d m_d\), and the zeta function of the associated finite Frobenius support-set is \(\prod_d (1-T^d)^{-m_d}\). In particular, the two distinct classes with line type \(3^9\) have respectively chamber cycle types \(1\,3^{921}\) and \(1^{13}3^{917}\). This distinction persists in their extension-field support counts.

## Assumptions and scope

The surface is smooth and geometrically integral over a finite field (arbitrary characteristic), with \(-K_S\) ample and \(K_S^2=3\). Over an algebraic closure, every such surface is the blow-up of six general-position points of \(\mathbb P^2\). With \(H\) the pulled-back line and \(E_i\) the six exceptional curves, the twenty-seven negative curves have classes

\[
E_i\ (1\le i\le6),\qquad H-E_i-E_j\ (i<j),\qquad 2H-\sum_{j\ne i} E_j\ (1\le i\le6).
\]

Divisors use the integer coordinate convention \(D=dH-\sum_i m_iE_i\), and their intersection product is \(D\cdot D'=dd'-\sum_i m_i m_i'\). All negative curves on a smooth cubic surface are these twenty-seven \((-1)\)-curves. The Weyl action is the intersection-form-preserving, canonical-class-preserving action on their labels; no claim is made that every Weyl element is realized over every finite field.

## Proof

**1. Exact characterization of supports.** A Zariski chamber other than the nef chamber is indexed by a reduced negative-definite set of negative curves, by the Zariski-support correspondence [1, Proposition 1.1]. For two distinct \((-1)\)-curves on a smooth cubic surface the intersection number is \(0\) or \(1\). Any meeting pair yields intersection matrix \(\left(\begin{smallmatrix}-1&1\\1&-1\end{smallmatrix}\right)\), which is not negative definite; conversely, a pairwise disjoint family has matrix \(-I\) and is negative definite. Thus chambers correspond **bijectively** to the empty set and all pairwise disjoint subsets of the twenty-seven lines.

**2. Arithmetic descent, including actual divisors.** If a support \(\mathcal S\) is stable under Frobenius, set \(B=\sum_{C\in\mathcal S}C\), a divisor defined over \(\mathbb F_q\). The divisor \(P=-K_S+B\) is nef: for \(C\in\mathcal S\), \(P\cdot C=1-1=0\); for any irreducible \(C\notin\mathcal S\), the ampleness of \(-K_S\) and nonnegative intersections between distinct irreducible curves imply \(P\cdot C>0\). Also \(P^2=3+|\mathcal S|>0\), so \(P\) is big. Hence the rational divisor \(D=P+B=-K_S+2B\) has precisely the Zariski decomposition \(P+B\), with negative support \(\mathcal S\). The empty support is realized by \(-K_S\). Conversely, the negative part of the Zariski decomposition of any ground-field divisor is Frobenius-stable by uniqueness. Therefore Frobenius-fixed supports correspond to genuine ground-field Zariski chambers, not merely formal fixed indices.

**3. The finite Weyl model.** In the above integer lattice take six simple roots \(\alpha_i=E_i-E_{i+1}\) for \(1\le i\le5\), and \(\alpha_6=H-E_1-E_2-E_3\). Reflections \(s_\alpha(D)=D+(D\cdot\alpha)\alpha\) act by permutations of the twenty-seven line classes. Exhaustive closure under these six reflections produces exactly \(51,840\) distinct permutations, the full Weyl group \(W(E_6)\). The induced conjugation closure partitions them into exactly \(25\) conjugacy classes, whose cardinalities add to \(51,840\). The algorithm uses exact integer lattice arithmetic and finite permutations, not sampling.

**4. Exhaustive chamber and orbit enumeration.** Use the complete intersection matrix to construct the disjointness graph. Enumerate all cliques by increasing line index; every clique occurs exactly once by its unique increasing ordering. The numbers by clique size \(0,1,2,3,4,5,6\) are \((1,27,216,720,1080,648,72)\), summing to \(2,764\). For each of the \(25\) class representatives, act on each clique by permuting its member lines, then follow its orbit. This produces exactly the table's cycle partitions, each satisfying \(\sum_d d m_d=2,764\). Because conjugate permutations act by conjugate permutations on the clique set, the table depends only on the Weyl conjugacy class.

**5. Independent fixed-point check.** A support fixed by a power \(F^n\) is a union of entire \(F^n\)-orbits on lines, each internally pairwise skew, with distinct chosen line-orbits pairwise skew. Independently enumerate such orbit-unions without enumerating the original \(2,764\) list. For every positive integer \(n\) up to the order of each of the \(25\) representatives, the number agrees with \(\sum_{d\mid n}d m_d\), using the spectra in the table. Finally, Burnside's identity gives \(\sum_{[g]} |[g]|\,|\operatorname{Fix}(g)|=414,720=8\cdot51,840\). The eight ordinary Weyl orbits are the support-size strata, except size five, which splits into two orbits. This is a further consistency check, not a substitute for the exhaustive enumeration.

## Verification

The attached standalone Python 3 standard-library artifacts `verify_weyl_chambers.py`, `verify_orbit_union.py`, and `e6_spectra.json` reproduce the exact finite computation. Execute `python3 verify_weyl_chambers.py` and `python3 verify_orbit_union.py` in the same extracted directory. The first reconstructs the entire Weyl group, its twenty-five conjugacy classes, all supports and all chamber cycles, comparing every computed entry to the supplied table data. The second independently rederives the fixed-support count for every power of each representative by the orbit-union method and verifies the Burnside total. Both scripts contain assertions; their explicit successful completion messages mark a complete pass. The infinite statement for all smooth cubic surfaces follows from the standard geometric classification and the exact finite Weyl model, rather than from tests over selected finite fields.

## Relationship to prior work

Bauer–Funke–Neumann [1] proved the geometric total \(2,764\) and the general negative-definite support correspondence, **not** the twenty-five Frobenius permutations of chambers. Rybakov–Trepalin [2] list all twenty-five Weyl conjugacy classes and classify minimal cubic surface types through their actions on Picard groups, **not** the permutation action on chamber supports. Sottile–Yahl [3] compute and tabulate twenty-seven-line splitting types, which do not in general distinguish chamber spectra: two order-three classes both have line cycle type \(3^9\) but unequal chamber fixed counts. The published work [4] proves the homotopy type of **the same finite complex of disjoint lines** and includes its complete face numbers, but its conclusion is non-equivariant and does not determine the twenty-five Frobenius chamber permutations. A separate chamber calculation for a singular, one-nodal cubic [5] concerns a different intersection configuration. These distinctions compare mathematical implications rather than titles; no previous source identified in the searches contains the complete table.

## Limitations

This is a **conditional** table for the Frobenius Weyl conjugacy class of a given smooth cubic surface, not a proof that every class occurs over every \(\mathbb F_q\). The two distinct classes with line type \(3^9\) show that a twenty-seven-line splitting partition by itself can be insufficient to select a table row; a full Weyl-type determination is needed. The numerical chamber-count input of [1] and the root-system classification are established prior results, not novel components. The cycle table is a finite exact computation with a proof of its exhaustive scope and an independently designed fixed-point verifier; no separate external mathematical audit has been performed. The search cannot exclude an obscure or unindexed earlier equivalent equivariant cycle table.

## References

1. T. Bauer, M. Funke and S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958v1, publicly posted December 4, 2009, https://arxiv.org/html/0912.0958v1, especially Proposition 1.1 and the theorem on degree-three del Pezzo surfaces.
2. S. Rybakov and A. Trepalin, *Minimal cubic surfaces over finite fields*, arXiv:1611.02475v1, publicly posted November 8, 2016, https://arxiv.org/html/1611.02475v2, especially Appendix A.
3. F. Sottile and T. Yahl, *Splitting types of the 27 lines on cubic surfaces*, https://franksottile.github.io/research/stories/27_Frobenius/index.html.
4. *A wedge of twenty-six four-spheres from the 27 lines on a cubic surface*, public full result at https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-a-wedge-of-twenty-six-four-spheres-from-the-27-lines-on-a-cubic--4e8fcf03196e/RESULT.md.
5. *Zariski chamber spectrum of a one-nodal cubic's minimal resolution*, published record at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-zariski-chamber-spectrum-of-the-one-nodal-cubic-s-minimal-resolu--4b531d234d53.
