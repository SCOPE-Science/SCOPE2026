# A five-torsion Moore summand in Singer quotients of the binary type-\(A_3\) building

## Finding

Let \(V=\mathbb F_2^4\) and let \(\mathcal B\) be the two-dimensional order complex of all nonzero proper linear subspaces of \(V\), with a simplex for each strict chain of such subspaces. Identify \(V\) with \(\mathbb F_{16}=\mathbb F_2[t]/(t^4+t+1)\) and let \(g\) be multiplication by \(t\). Then \(g\) has order \(15\). For each divisor \(d\mid15\), put \(C_d=\langle g^{15/d}\rangle\).

Define the two-dimensional Moore space \(M(\mathbb Z/5,1)=S^1\cup_{5}e^2\), where the two-cell is attached with degree five. The **ordinary geometric orbit spaces**, not homotopy-orbit/Borel constructions, have the following complete homotopy types:

| Subgroup | Homotopy type of \(|\mathcal B|/C_d\) |
|---|---|
| \(C_1\) | \(\bigvee^{64}S^2\) |
| \(C_3\) | \(\bigvee^{24}S^2\) |
| \(C_5\) | \(M(\mathbb Z/5,1)\vee\bigvee^{12}S^2\) |
| \(C_{15}\) | \(M(\mathbb Z/5,1)\vee\bigvee^{4}S^2\) |

Consequently, the first homology of the \(C_5\) and \(C_{15}\) quotients is exactly \(\mathbb Z/5\), and their second integral homology is free of ranks \(12\) and \(4\), respectively. The \(C_1\) and \(C_3\) quotients are simply connected and have free second homology of ranks \(64\) and \(24\). All positive-degree integral homology not specified here vanishes.

## Assumptions and scope

The vertices of \(\mathcal B\) are the \(15\) one-dimensional, \(35\) two-dimensional and \(15\) three-dimensional \(\mathbb F_2\)-subspaces of \(V\). Its simplices are all nonempty chains. The group acts on every vertex by sending a subspace \(U\) to \(tU\). Because the action preserves subspace dimension, no nontrivial group element permutes vertices within a simplex. Every subgroup of \(\langle g\rangle\cong C_{15}\) is one of the four listed, so the result covers all its subgroups.

## Proof

**1. Finite exact model.** Represent a vector of \(V\) by its integer bit mask in \(\{0,\ldots,15\}\). Multiplication by \(t\) is left shift modulo the binary polynomial \(t^4+t+1\). Its nonzero powers are distinct and \(t^{15}=1\), so it has order \(15\). Enumerating spans of all independent \(k\)-tuples for \(k=1,2,3\) produces the complete subspace sets of sizes \((15,35,15)\). Counting strict inclusions and maximal flags yields \((f_0,f_1,f_2)=(65,315,315)\).

**2. Quotient cells.** For each \(d\mid15\), a simplex orbit gives a genuine cell in the quotient, with oriented boundaries obtained by deleting one vertex of the increasing-dimensional chain. The dimensions distinguish its vertices, so the action cannot reverse or identify faces of a simplex internally. Compute orbit representatives by lexicographically minimizing the vector-subspace chains over \(C_d\). The results are:

| \(d\) | Zero-cells | One-cells | Two-cells | Edges in quotient spanning tree |
|---|---:|---:|---:|---:|
| \(1\) | 65 | 315 | 315 | 64 |
| \(3\) | 25 | 105 | 105 | 24 |
| \(5\) | 13 | 63 | 63 | 12 |
| \(15\) | 5 | 21 | 21 | 4 |

Each quotient one-skeleton is connected. Collapse a spanning tree. Its remaining one-cell generators number \(251,81,51,17\), respectively. A two-simplex \((P<L<H)\) has attaching word \(e_{P,L}e_{L,H}e_{P,H}^{-1}\), with tree edges omitted and each remaining edge oriented by increasing subspace dimension. All these attaching words are constructed exactly from the orbit representatives.

**3. Homotopy-preserving cancellations.** Apply the following finite algorithm: if an attaching word \(w=a\,x^{\pm1}b\) contains a one-cell generator \(x\) exactly once, solve this relation for \(x\), substitute into every other attaching word, then discard the corresponding generator and two-cell. This is an elementary two-cell/one-cell elimination (Tietze expansion/collapse), not merely a homology reduction. Free and cyclic reductions of attaching words are allowed, since cyclic conjugation changes only the chosen basepoint on the attaching loop. The deterministic certificate, reconstructed by `verify_singer_building.py`, makes \(251,81,50,16\) such eliminations for \(d=1,3,5,15\), respectively.

The residual attaching maps are then:

| \(d\) | One-cell generators | Residual two-cell attaching degrees |
|---|---:|---|
| \(1\) | 0 | 64 zero maps |
| \(3\) | 0 | 24 zero maps |
| \(5\) | 1 | 6 maps of degree \(+5\), 7 zero maps |
| \(15\) | 1 | 1 map of degree \(+5\), 1 of degree \(-5\), 3 zero maps |

The final one-skeleton in the latter two cases is one circle. All its attaching maps are determined up to homotopy by integer degree. Elementary two-cell slides reduce any collection of \(r\ge1\) maps of degrees \(\pm5\) to one degree-five map and \(r-1\) null attaching maps. The quotient is therefore a degree-five Moore space wedged with the listed number of two-spheres. If no one-cell remains, every null-attached two-cell is an independent two-sphere. This proves all four homotopy equivalences.

**4. Structural cross-check.** The order-three subgroup fixes exactly the five two-dimensional subspaces that are one-dimensional over \(\mathbb F_4\); its fixed-point complex consists of five isolated vertices. Elements of order five or fifteen fix no nonzero proper subspace and hence no geometric point. The \(C_5\)-action is free; the \(C_{15}\)-quotient has nonfree order-three isotropy. This predicts the Euler characteristics \(65,25,13,5\) and independently explains the fundamental-group difference between \(C_3\) and the larger subgroups. The reduced cellular presentations above prove the stronger complete homotopy assertions.

## Verification

The included Python 3 standard-library script `verify_singer_building.py` is self-contained. From first principles it enumerates all subspaces and flags, computes the four orbit CW presentations, contracts a spanning tree, constructs each attaching word, and performs the explicit homotopy-preserving generator eliminations. It asserts all cell counts, cancellation counts, residual degrees and final types; successful execution ends with `VERIFY_OK`. No symbolic algebra libraries, precomputed files, or online services are needed.

## Relationship to prior work

**Earlier calculations of this same Singer action already give considerable information and are not claimed as new.** In particular, prior result `f4aed456-3942-4ca4-ab32-20bd58c3997b` establishes the full Singer quotient's fundamental group \(C_5\), first homology \(\mathbb Z/5\) and second homology \(\mathbb Z^4\) as the binary case of a prime-power family. Prior result `321e74dc-927b-4dd4-a0e1-359a00de8394` determines all Singer-subgroup fundamental groups and rational top Betti numbers in every rank, and result `608e12b6-d804-4fc2-bb75-f59f5256e7ec` gives integral homology of free prime-order Singer actions. Combined with the two-dimensional nature of the complex, these facts already imply the sphere-wedge types for the trivial and order-three subgroups. **The additional conclusion established here is the actual Moore-space wedge decomposition for the order-five and order-fifteen quotients**: fundamental groups and homology groups alone do not identify their attaching maps or their two-dimensional homotopy types. Result `1f1057cf-987c-4d7e-8661-1fe16a2950d9` addresses the larger semilinear normalizer's quotient and is not a computation for these cyclic subgroup quotients.

The Solomon–Tits theorem establishes the original binary type-\(A_3\) building's wedge homotopy; Chao Ku's 1998 full proof concerns the unquotiented building. Giuzzi and Sonnino's 2007 preprint (especially Theorem 4 and Sections 6–7) analyzes Singer subspace orbits and the distinguished line spread in \(\operatorname{PG}(3,2)\), but not the quotient attaching maps. Papikian's 2010 preprint concerns quotients of affine Bruhat–Tits buildings by arithmetic groups, a different situation.

## Limitations

The theorem applies exactly to the order-fifteen Singer group of \(\operatorname{PG}(3,2)\) and its four subgroups. It does not assert analogous formulas for larger field orders, higher ranks, arbitrary subgroups of \(\operatorname{GL}_4(\mathbb F_2)\), or homotopy-orbit constructions. The finite verifier is a complete exhaustive calculation **only for this precisely specified finite complex**; it is not evidence for an unbounded generalization. A mathematically equivalent unindexed older computation of these orbit homotopy types has not been ruled out.

## References

1. Chao Ku, “A new proof of the Solomon–Tits theorem,” *Proceedings of the American Mathematical Society* **126** (1998), 1941–1944. DOI: https://doi.org/10.1090/S0002-9939-98-04453-0 . Accessible full text: https://scispace.com/pdf/a-new-proof-of-the-solomon-tits-theorem-41g6r3j6kp.pdf .
2. Luca Giuzzi and Angelo Sonnino, “LDPC codes from Singer cycles,” first public preprint 2007-09-18, arXiv:0709.2813, https://arxiv.org/html/0709.2813v1 ; subsequently *Discrete Applied Mathematics* **157** (2009), 1723–1728.
3. Mihran Papikian, “On finite arithmetic simplicial complexes,” arXiv:1006.3198, first posted 2010-06-16, https://arxiv.org/abs/1006.3198 .
