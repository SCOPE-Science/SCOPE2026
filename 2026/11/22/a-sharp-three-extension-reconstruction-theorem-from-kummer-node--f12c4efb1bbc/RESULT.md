# A sharp three-extension reconstruction theorem from Kummer node–trope incidences

## Finding

Let \(k=\mathbb F_q\) be any finite field of odd cardinality and \(C/k\) any smooth projective genus-two curve. In the canonical Kummer quartic of \(\operatorname{Jac}(C)\), let \(\mathcal N\) denote its reduced scheme of sixteen geometric nodes, \(\mathcal T\) its reduced scheme of sixteen geometric trope conics (equivalently, their trope planes), and \(\mathcal I\) the reduced finite étale scheme of node–trope incident pairs. The incidence scheme has degree \(96\). For every integer \(n\ge1\), write

\[
F_n=\#\mathcal I(\mathbb F_{q^n}).
\]

Write \(\sigma\in S_6\) for the arithmetic Frobenius permutation of the six geometric hyperelliptic branch points. Let \(f_n\) and \(t_n\) be the respective numbers of \(1\)-cycles and \(2\)-cycles of \(\sigma^n\). Then

\[
\boxed{F_n=f_n^2+\binom{f_n}{2}(f_n-2)+f_nt_n}\quad (n\ge1).
\]

The three counts \((F_1,F_2,F_3)\) uniquely determine the cycle partition of \(\sigma\), among the eleven partitions of six, and thereby the complete splitting of the branch sextic and the zeta functions of \(\mathcal I\), \(\mathcal N\), and \(\mathcal T\). This cutoff is sharp uniformly in \(q\): the types \((3,3)\) and \((6)\) both give \((F_1,F_2)=(0,0)\), but respectively \(F_3=96\) and \(F_3=0\); both types occur over every finite field of odd order.

In contrast, the full individual Frobenius spectra of nodes and of tropes each identify only nine of the eleven branch splitting types. The indistinguishable pairs for each individual scheme are \((1,1,2,2)\) versus \((2,2,2)\), and \((1,1,4)\) versus \((2,4)\). Thus their separate zeta functions, even known over *every* extension, cannot recover the branch partition, while three incidence counts can.

## Assumptions and scope

The base field is finite of **odd characteristic**. Any smooth genus-two curve has a separable hyperelliptic double cover with six geometric branch points, including potentially one branch point at infinity in an odd-degree affine model; the statement is independent of the choice of affine coordinate, rational Weierstrass point, or square-twist of its defining equation. The sixteen nodes and sixteen trope conics are taken as **reduced finite étale support schemes**; \(F_n\) counts *incident pairs of geometric supports descended to the extension*, not arbitrary intersection points, rational points on the trope conics, or points on a Kummer surface.

All eleven abstract six-point cycle types are covered. Realizability of **every** type over an individual small field is not asserted: for example, \(\mathbb F_3\) has only four points on \(\mathbb P^1\), so six rational branch points are impossible there. Crucially, the two sharpness types **are** realizable over every odd finite field: the product of two distinct irreducible cubic polynomials realizes \(3,3\), and an irreducible sextic realizes \(6\). Each squarefree sextic defines a smooth genus-two curve \(y^2=f(x)\). No characteristic-two analogue is claimed.

## Proof

**1. Equivariant geometric description.** Label the six branch points by \(B=\{1,2,3,4,5,6\}\). The sixteen nodes correspond to \(0\) and the fifteen unordered pairs \(P\subset B\) of size two. The sixteen tropes correspond to the six singletons \(\{i\}\) and the ten unordered partitions \(A\mid(B\setminus A)\) with \(|A|=3\). Classical Kummer incidence is exactly:

- Node \(0\) lies on every singleton trope and on no triple-partition trope.
- Node \(P\) lies on singleton trope \(i\) precisely when \(i\in P\).
- Node \(P\) lies on triple-partition trope \(A\mid(B\setminus A)\) precisely when both members of \(P\) lie in the same half.

These are geometric equalities of the reduced incidence configuration, compatible with every relabeling in \(S_6\), and hence with arithmetic Frobenius. Their degrees are \(6\) at each node and trope, giving \(16\cdot6=96\) flags.

**2. Three disjoint flag species.** The six \(0\)-singleton flags identify with the six elements of \(B\). The thirty pair–singleton flags identify with **ordered pairs of distinct elements** of \(B\), by mapping \((P,i)\) to \((i,j)\) where \(P=\{i,j\}\). The sixty pair–triple flags identify with triples \((P,k)\), where \(|P|=2\) and \(k\in B\setminus P\): the unique partition has one half \(P\cup\{k\}\) and the other its complement. Conversely, any incidence of this species supplies precisely that unique third member \(k\). This establishes a canonical \(S_6\)-equivariant disjoint union

\[
\mathcal I(\bar k)\simeq B\;\sqcup\;\{(i,j)\in B^2:i\ne j\}\;\sqcup\;\{(P,k):|P|=2,\ k\notin P\}.
\]

**3. Fixed-point formula.** Put \(\tau=\sigma^n\), and let \(f=f_n\), \(t=t_n\). The three species contribute respectively \(f\), \(f(f-1)\), and \(\binom f2(f-2)+tf\) fixed flags. In the third species, either both elements of \(P\) are individually fixed (and its third element is one of the remaining fixed labels), or \(P\) is a two-cycle and its third element is fixed. These cases are disjoint and exhaustive. Their sum yields the boxed formula for every \(n\ge1\).

**4. Exhaustive eleven-type classification.** Frobenius on a six-element étale set has one of the eleven cycle partitions, with a unique conjugacy class for each. The following table gives the complete node cycles, incidence-flag cycles, and counts in the first three extensions. The trope cycle structure is identical to the node cycle structure in each row; this equality concerns cycle *multisets*, not a canonical equality of schemes. A cycle expression \(d^m\) signifies \(m\) Frobenius cycles of length \(d\).

| Branch partition | Node cycles (and trope cycles) | Flag cycles | \(F_1\) | \(F_2\) | \(F_3\) |
|---|---|---|---:|---:|---:|
| \((1,1,1,1,1,1)\) | \(1^{16}\) | \(1^{96}\) | 96 | 96 | 96 |
| \((1,1,1,1,2)\) | \(1^{8}\, 2^{4}\) | \(1^{32}\, 2^{32}\) | 32 | 96 | 32 |
| \((1,1,1,3)\) | \(1^{4}\, 3^{4}\) | \(1^{12}\, 3^{28}\) | 12 | 12 | 96 |
| \((1,1,2,2)\) | \(1^{4}\, 2^{6}\) | \(1^{8}\, 2^{44}\) | 8 | 96 | 8 |
| \((1,1,4)\) | \(1^{2}\, 2^{1}\, 4^{3}\) | \(1^{4}\, 2^{2}\, 4^{22}\) | 4 | 8 | 4 |
| \((1,2,3)\) | \(1^{2}\, 2^{1}\, 3^{2}\, 6^{1}\) | \(1^{2}\, 2^{5}\, 3^{10}\, 6^{9}\) | 2 | 12 | 32 |
| \((1,5)\) | \(1^{1}\, 5^{3}\) | \(1^{1}\, 5^{19}\) | 1 | 1 | 1 |
| \((2,2,2)\) | \(1^{4}\, 2^{6}\) | \(2^{48}\) | 0 | 96 | 0 |
| \((2,4)\) | \(1^{2}\, 2^{1}\, 4^{3}\) | \(2^{4}\, 4^{22}\) | 0 | 8 | 0 |
| \((3,3)\) | \(1^{1}\, 3^{5}\) | \(3^{32}\) | 0 | 0 | 96 |
| \((6)\) | \(1^{1}\, 3^{1}\, 6^{2}\) | \(6^{16}\) | 0 | 0 | 0 |

The eleven triples in the last three columns are distinct, which proves injectivity. The first two columns \((F_1,F_2)\) coincide only for \((3,3)\) and \((6)\), establishing sharpness once both realizability cases above are invoked. The two pairs of repeated node/trope cycle multisets are visible directly in the table. For any row whose flag Frobenius cycles are \(d^{m_d}\), its flag-scheme zeta function is exactly

\[
Z(\mathcal I/k,T)=\prod_{d\ge1}(1-T^d)^{-m_d},
\]

with the analogous formula using the node/trope cycles for their zeta functions; this makes the extension count assertions fully explicit.

## Verification

The attached standard-library script `verify_kummer_flags.py` constructs the sixteen nodes, sixteen tropes, and ninety-six incidences directly from the stated three incidence rules; confirms six tropes at every node and six nodes at every trope; and enumerates **all \(6!=720\) permutations** of \(B\). For each permutation it computes orbit decompositions on nodes, tropes, and flags and independently evaluates the fixed-point formula. It checks conjugacy consistency for all eleven cycle types, uniqueness of the eleven three-count signatures, the single two-count collision, the two pairs of individual node/trope spectrum collisions, and every CSV row. Running `python verify_kummer_flags.py kummer_flag_spectra.csv` reproduces `kummer_flag_spectra.csv` and prints `KUMMER_96_FLAGS_720_SIX_POINT_ACTIONS_11_TYPES_SHARP_THREE_EXTENSIONS_VERIFIED`. The verified finite enumeration is exhaustive because there are exactly \(720\) permutations, and the geometric equivariance makes every finite-field instance a specialization of one of these cases. No finite-field sample is substituted for an infinite-field proof.

## Relationship to prior work

The Kummer \((16_6)\)-configuration, its labeling by six branch points, the identification of 2-torsion nodes with unordered branch pairs, and its odd/even trope incidence rules are **classical, not new**. Castorena–Frías-Medina give a genus-two/Kummer geometric framework in their 2021 preprint, later published in 2023. Gonzalez-Hernandez's 2024 preprint, later published in 2025/2026, explicitly describes all sixteen nodes and tropes in Section 2.2 and tabulates *base-field node and trope counts* by branch factorization in Table 1. In particular, the geometric inputs to this theorem and a substantial part of the arithmetic setup are already published.

The additional claim here is the exact arithmetic of the *ninety-six incident flags*, their eleven zeta spectra, and the sharp three-extension inverse theorem; these are not stated in those inspected works. For comparison, a previously published classification of sixty Segre-cubic node–plane flags and one of 180 Pascal–Kirkman incidence flags also give eleven splitting-type spectra for six labels, but concern different finite schemes and do not supply the 96-flag formula or inverse calculation by implication alone. The independent Kummer Göpel-tetrad lattice study addresses an integral incidence lattice, not these Frobenius fixed-point data. All comparisons are best-knowledge priorities, not proof of global novelty.

## Limitations

The theorem concerns splitting partitions, not the positions or cross-ratios of the six branch points, curve isomorphism, Weil polynomials, rational points on the Kummer surface, or the geometry of the trope conics themselves. The classification and reconstruction use reduced geometric supports. Characteristic two is excluded. The first-public source date below refers to the 2021 literature lead, not the discovery date of this classification. An unindexed equivalent character/cycle-index table could predate the present claim, and the published Kummer label formulas make this exact computation substantially more approachable; that historical priority and the independent check remain unresolved. Independent review has not been performed.

## References

1. A. Castorena and J. B. Frías-Medina, *Geometric aspects on Humbert-Edge curves of type 5, Kummer surfaces and hyperelliptic curves of genus 2*, preprint arXiv:2106.00813 (first public 2021-06-01), *Glasgow Mathematical Journal* 65 (2023), 612–624. DOI: 10.1017/S0017089523000174. https://arxiv.org/abs/2106.00813
2. A. Gonzalez-Hernandez, *Explicit desingularisation of Kummer surfaces in characteristic two via specialisation*, arXiv:2409.04532 (first public 2024-09-06), *Journal of Symbolic Computation* 135 (2026), 102541, especially Section 2.2 and Table 1. DOI: 10.1016/j.jsc.2025.102541. https://arxiv.org/abs/2409.04532
3. *Brill-Noether loci on an Enriques surface covered by a Jacobian Kummer surface*, 2025, especially the Kummer incidence description in Section 1.2. DOI: 10.1007/s00013-025-02129-7. https://link.springer.com/article/10.1007/s00013-025-02129-7
4. Related distinct six-label incidence findings: `2026/11/2/SCOPE-frobenius-spectra-of-the-sixty-node-plane-incidence-flags-of-tra--4c734c76e2d7`; `2026/11/2/SCOPE-frobenius-orbit-spectra-and-rational-incidence-obstructions-for--1e6ef0f36929`.
