# Frobenius orbit spectra of cubic-surface tritangent flags for a six-point blowup

## Finding
Let \(k=\mathbb F_q\) have characteristic at least \(5\). Let \(P\subset\mathbb P^2_{k}\) be a reduced, finite étale degree-six subscheme whose six geometric points are in general position (no three collinear and not all six on a conic). Let \(S=\operatorname{Bl}_P\mathbb P^2\), embedded as a smooth cubic surface by the anticanonical system. Denote by \(\mathcal L\), \(\mathcal T\), and \(\mathcal F\) the finite étale schemes of geometric lines on \(S\), tritangent planes, and incident pairs of a line contained in a tritangent plane. Their geometric degrees are \(27\), \(45\), and \(135\), respectively.

**Classification.** If the six-point Frobenius permutation has cycle type \(\lambda\), its cycle-count vectors on all three schemes are precisely those in Table 1, with notation \(d^m\) for \(m\) cycles of length \(d\). The statement is conditional on the specified blowup and does not assert that every type is realizable over each finite field.

| \(\lambda\) | \(\mathcal L\) cycles | \(\mathcal T\) cycles | \(\mathcal F\) cycles | Rational-plane composition \((n_0,n_1,n_3)\) |
|---|---|---|---|---|
| \((6)\) | \(3^1 6^4\) | \(1^1 2^1 3^2 6^6\) | \(3^3 6^{21}\) | \((1,0,0)\) |
| \((5,1)\) | \(1^2 5^5\) | \(5^9\) | \(5^{27}\) | \((0,0,0)\) |
| \((4,2)\) | \(1^1 2^3 4^5\) | \(1^1 2^2 4^{10}\) | \(1^1 2^5 4^{31}\) | \((0,1,0)\) |
| \((4,1,1)\) | \(1^5 2^1 4^5\) | \(1^3 2^1 4^{10}\) | \(1^7 2^2 4^{31}\) | \((0,1,2)\) |
| \((3,3)\) | \(3^9\) | \(1^3 3^{14}\) | \(3^{45}\) | \((3,0,0)\) |
| \((3,2,1)\) | \(1^3 2^3 3^4 6^1\) | \(2^3 3^5 6^4\) | \(2^9 3^{15} 6^{12}\) | \((0,0,0)\) |
| \((3,1,1,1)\) | \(1^9 3^6\) | \(1^6 3^{13}\) | \(1^{18} 3^{39}\) | \((0,0,6)\) |
| \((2,2,2)\) | \(1^3 2^{12}\) | \(1^7 2^{19}\) | \(1^9 2^{63}\) | \((0,6,1)\) |
| \((2,2,1,1)\) | \(1^7 2^{10}\) | \(1^5 2^{20}\) | \(1^{11} 2^{62}\) | \((0,2,3)\) |
| \((2,1,1,1,1)\) | \(1^{15} 2^6\) | \(1^{15} 2^{15}\) | \(1^{45} 2^{45}\) | \((0,0,15)\) |
| \((1,1,1,1,1,1)\) | \(1^{27}\) | \(1^{45}\) | \(1^{135}\) | \((0,0,45)\) |

Here \(n_r\) counts rational tritangent planes containing exactly \(r\) individually rational geometric lines; no rational plane contains exactly two rational component lines. Consequently, **a line-free cubic surface in this six-point-blowup class has a rational tritangent plane if and only if \(\lambda=(6)\) or \(\lambda=(3,3)\)**. In those two cases the counts are respectively one and three, and each rational plane contains no rational line. Every extension-field point count is determined by the same table: for any one of the three schemes \(\mathcal X\),
\[
\#\mathcal X(\mathbb F_{q^n})=\sum_{d\mid n}d\,c_d(\mathcal X),\qquad
Z(\mathcal X/\mathbb F_q,T)=\prod_d(1-T^d)^{-c_d(\mathcal X)}.
\]

## Assumptions and scope
All schemes are reduced finite étale *geometric configuration schemes*, not the positive-dimensional unions of the corresponding curves or planes. A line is rational when it is individually fixed by arithmetic Frobenius, a plane when the unordered triple of its component lines is Frobenius-stable, and a rational incidence flag means both the line and plane are individually rational. The geometric six-point set may be non-split over \(k\); the blowup is defined over \(k\) because the reduced centre is Frobenius-stable. The genus, characteristic, and smoothness assumptions enter through the standard six-point cubic-surface construction. A special cubic surface with additional automorphisms causes no difficulty because Frobenius still acts by its permutation of the marked six centres.

## Proof
1. **The geometric model.** Label the six points \(0,\ldots,5\) over \(\overline{k}\). Write \(E_i\) for the exceptional line, \(Q_i\) for the strict transform of the conic through all centres except \(i\), and \(L_{ij}=L_{ji}\) for the transform of the line through centres \(i,j\). These are exactly the \(6+6+15=27\) lines. The classical Schläfli description, checked directly by the intersection form on the blowup, gives precisely the \(30\) tritangent triples
\[
A_{ij}=\{E_i,Q_j,L_{ij}\}\quad(i\ne j)
\]
and the \(15\) triples
\[
B_{\mathcal M}=\{L_{ab}:\{a,b\}\in\mathcal M\},
\]
where \(\mathcal M\) runs over the partitions of the six indices into three unordered pairs. For completeness, a plane containing an \(E_i\) must have one \(Q_j\) with \(j\ne i\) and the unique residual component \(L_{ij}\); a plane containing no exceptional or conic line must contain three pairwise-disjoint-index \(L_{ij}\) lines, hence a perfect matching. These lists are exhaustive and have different component-line sets.

2. **Equivariance.** Frobenius sends \(E_i\) to \(E_{\sigma(i)}\), \(Q_i\) to \(Q_{\sigma(i)}\), \(L_{ij}\) to \(L_{\sigma(i)\sigma(j)}\), \(A_{ij}\) to \(A_{\sigma(i)\sigma(j)}\), and \(B_{\mathcal M}\) to \(B_{\sigma\mathcal M}\). Thus the three schemes are finite permutation sets of sizes \(27,45,135\) with the latter consisting of \((\text{plane},\text{one of its three lines})\). The action depends only on the conjugacy class of \(\sigma\in S_6\), i.e. one of the eleven partitions of six.

3. **Independent fixed-point formulas.** For a permutation \(\sigma\), let \(f\) be the number of fixed centres, let \(u\) be the number of fixed unordered index pairs, and let \(m(V,\sigma)\) count invariant perfect matchings of an even-sized \(\sigma\)-stable subset \(V\). Then
\[
\#\operatorname{Fix}(\mathcal L)=2f+u,\quad
\#\operatorname{Fix}(\mathcal T)=f(f-1)+m([6],\sigma),
\]
\[
\#\operatorname{Fix}(\mathcal F)=3f(f-1)+
\sum_{e\text{ a fixed unordered index pair}}m([6]\setminus e,\sigma).
\]
Indeed a fixed \(A_{ij}\) forces both indices fixed and yields three fixed flags, whereas a fixed flag in a \(B\)-plane selects an invariant index pair and an invariant matching of the other four indices. Applying these identities to \(\sigma^n\), and using
\[
F(n)=\sum_{d\mid n}d\,c_d,
\]
gives the unique cycle counts displayed in Table 1. A second direct orbit enumeration on each of the 27, 45, and 135 labelled sets, across all 720 permutations in \(S_6\), gives the identical table; the standalone verifier checks both routes.

4. **The line-free boundary.** A rational \(E_i\) or \(Q_i\) requires a fixed centre; a rational \(L_{ij}\) requires either two fixed centres or a two-cycle. Therefore no rational lines means \(\sigma\) has neither fixed points nor two-cycles; the only partitions of six with this property are \((6)\) and \((3,3)\). The fixed-matching formula gives respectively one and three fixed \(B\)-planes, none with a fixed pair, hence no rational incidence flag. Finally, if a rational plane contains two fixed component lines then its third residual line is Galois-fixed, eliminating the \(n_2\) case in every row.

5. **Zeta functions.** A Frobenius orbit of length \(d\) on a finite étale scheme contributes exactly \(d\) points over \(\mathbb F_{q^n}\) if \(d\mid n\) and none otherwise. Summing and exponentiating yields the asserted formula for each of the three schemes over every extension field.

## Verification
Run `python3 verify_tritangent_flags.py` with Python 3 and no external dependencies. It constructs the 15 matchings and the 27, 45, and 135 objects; checks distinctness, incidence, all 720 actions and all eleven conjugacy types; matches directly enumerated orbit cycles to the table; compares fixed counts against the separate fixed-centre/pair/matching formulas; checks the Möbius fixed-point identities over all relevant extension degrees; and tests the line-free boundary. Successful execution prints `TRITANGENT_FLAG_FROBENIUS_CLASSIFICATION_VERIFIED_OK`. The script concerns only finite combinatorics; the proof above establishes its geometric applicability. Neither script output nor computation alone substitutes for the geometric identification.

## Relationship to prior work
The twenty-seven lines and 30-plus-15 tritangent description are classical and explicitly appear as Lemma 2.2 of Polo-Blanco–Top (2008), so they are not new here. Elsenhans–Jahnel (2010) study Galois descent and tritangent configurations; notably their involution fixed-point counts agree with the corresponding rows here. Das (2020) obtains the aggregate distribution of rational tritangent counts among *all* smooth finite-field cubic surfaces, supported by the broader \(W(E_6)\) action. That work gives a general mechanism for deriving finite configuration statistics, and is a significant priority risk for routine reformulations. The specific contribution here is limited to the simultaneous **full orbit cycles** of three finite étale schemes in the marked six-point subfamily, the complete rational line-in-plane composition table, and the sharp line-free/rational-plane descent phenomenon. The results neither improve Das's population counts nor characterize every cubic surface without a rational sixer.

## Limitations
The classification is conditional on a smooth cubic obtained from a Frobenius-stable six-point blowup; it is not a classification of every \(W(E_6)\) Frobenius class. The table counts geometric lines, tritangent planes and incidence flags as finite étale schemes, not the number of rational points on their unions. The eleven rows are possible conjugacy types, not a promise of realizability over every \(q\). The arithmetic orbit counts are a combinatorial consequence of the classical geometric model and are susceptible to being implicit in existing broader character tables. Historical priority is not independently certified.

## References
- I. Dolgachev, B. van Geemen, S. Kondō, *A complex ball uniformization of the moduli space of cubic surfaces via periods of K3 surfaces*, arXiv:math/0310342, first posted 2003-10-21. https://arxiv.org/abs/math/0310342
- I. Polo-Blanco, J. Top, *Explicit Real Cubic Surfaces*, Canadian Mathematical Bulletin 51 (2008), 125–133, DOI:10.4153/CMB-2008-014-5. https://www.researchgate.net/publication/228384579_Explicit_Real_Cubic_Surfaces
- A.-S. Elsenhans, J. Jahnel, *Cubic surfaces with a Galois invariant pair of Steiner trihedra*, arXiv:1006.1474, first posted 2010-06-08. https://arxiv.org/abs/1006.1474
- R. Das, *Arithmetic statistics on cubic surfaces*, arXiv:2002.11183, first posted 2020-02-25. https://arxiv.org/abs/2002.11183
