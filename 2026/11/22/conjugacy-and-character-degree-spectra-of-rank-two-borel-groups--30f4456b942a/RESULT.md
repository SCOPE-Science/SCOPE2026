# Conjugacy and character-degree spectra of rank-two Borel groups over square-zero local rings

## Finding

Let \(R\) be any finite commutative unital local ring with nonzero maximal ideal \(\mathfrak m\), \(\mathfrak m^2=0\), residue field of order \(q\), and \(d=\dim_{R/\mathfrak m}\mathfrak m\ge1\). Set
\[
U=(q-1)q^d,\qquad T=q^{d+1},\qquad L_j=\frac{q^j-1}{q-1}\quad(j\ge0).
\]
For the group \(G=B_2(R)\) of invertible upper-triangular two-by-two matrices over \(R\), the **complete conjugacy-class-size multiset** is obtained by taking the following sizes and respective numbers of classes, adding multiplicities when sizes coincide:

| Size of each class | Number of classes |
|---|---:|
| \(T\) | \(U(U-q^d)\) |
| \(U\) | \(Uq^d\) |
| \(q(q-1)\) | \(U(q^d-1)L_{d-1}\) |
| \(q\) | \(U(q^d-1)\) |
| \(q-1\) | \(UL_d\) |
| \(1\) | \(U\) |

Zero multiplicities are omitted. The **complete ordinary complex irreducible-character degree multiset** is likewise the following, with coincident degrees merged:

| Irreducible character degree | Multiplicity |
|---|---:|
| \(1\) | \(U^2\) |
| \(q-1\) | \(Uq^d\) |
| \(q(q-1)\) | \(Uq^{d-1}L_d\) |

In particular the class number, equivalent to the number of irreducible characters, and the ordinary commuting probability are
\[
k(G)=q^{2d-1}\big((q-1)q^2+q^d-1\big),\qquad
\operatorname{cp}(G)=\frac{(q-1)q^2+q^d-1}{(q-1)^2q^{d+2}}.
\]
For fixed \(q\) and \(d\to\infty\), this probability tends to \(1/[q^2(q-1)^2]\). The same statistics hold for all rings with the same \((q,d)\), regardless of characteristic, splitting, or principal-ideal structure.

## Assumptions and scope

The ring is finite, commutative, has identity, has one maximal ideal \(\mathfrak m\ne0\), and satisfies \(\mathfrak m^2=0\). Then \(\mathfrak m\) is a vector space over \(k=R/\mathfrak m\), of dimension \(d\), and \(|R|=q^{d+1}\), \(|R^\times|=(q-1)q^d\). No coefficient-field section or restriction on the characteristic is assumed. An irreducible character means an ordinary complex character of the finite group, not a modular character. Class sizes are group-conjugacy orbit sizes; multiplicities in coincident numerical rows must be added. The result includes \(q=2\), nonprincipal rings for \(d\ge2\), and mixed-characteristic rings such as \(\mathbb Z/4\mathbb Z[\epsilon]/(2\epsilon,\epsilon^2)\).

## Proof

**Step 1: Reduction to the affine group.** Let \(H=R^+\rtimes R^\times\), with multiplication \((b,s)(b',s')=(b+sb',ss')\). The assignment
\[
\begin{pmatrix}a&b\\0&c\end{pmatrix}\longmapsto
\big(c,(bc^{-1},ac^{-1})\big)
\]
is a group isomorphism \(G\cong R^\times\times H\). Direct matrix multiplication verifies it: the bottom diagonal entry multiplies as \(cc'\), and the normalized upper-right entry becomes \(bc^{-1}+(ac^{-1})(b'c'^{-1})\). Since \(R^\times\) is abelian, every conjugacy class of \(H\) gives exactly \(U\) classes of \(G\) of the same size, and every irreducible of \(H\) gives exactly \(U\) irreducibles of \(G\) of the same degree.

**Step 2: Complete conjugacy orbits of \(H\).** For fixed multiplier \(s\in R^\times\), conjugation transforms a translation coordinate \(b\) as
\[
b\longmapsto wb+(1-s)z,\qquad w\in R^\times,\ z\in R.
\]
Thus its classes are exactly the \(R^\times\)-orbits in \(R/(1-s)R\), each lifted through the ideal \((1-s)R\). There are precisely three cases.

If \(1-s\) is a unit, there is one class for that multiplier, of size \(T\). There are \(U-q^d\) such multipliers.

If \(1-s\in\mathfrak m\setminus\{0\}\), its principal ideal is the one-dimensional \(k\)-line \(k(1-s)\) of size \(q\). The quotient has a radical vector space of dimension \(d-1\). Its unit cosets comprise one orbit of size \((q-1)q^{d-1}\), lifting to a class of size \(U\). Its zero coset lifts to a class of size \(q\). Each of the \(L_{d-1}\) projective lines of its nonzero radical contributes one orbit lifting to a class of size \(q(q-1)\). There are \(q^d-1\) such multipliers.

If \(s=1\), the action is ordinary unit multiplication on \(R\). Its orbit sizes are \(U\) for all units, \(1\) for zero, and \(q-1\) for every nonzero radical line, of which there are \(L_d\). This occurs for one multiplier.

Multiplying all six affine class multiplicities by \(U\) proves the conjugacy table. Distinct multipliers cannot be conjugate, so the three cases exhaust every element.

**Step 3: Complete character-degree spectrum.** Write \(\widehat{R^+}\) for the complex additive-character group. In the usual little-group construction for the abelian normal subgroup \(R^+\), each \(R^\times\)-orbit \(\mathcal O\) in \(\widehat{R^+}\) contributes exactly \(|H_\chi|\) irreducible characters of degree \(|\mathcal O|\), where \(H_\chi\le R^\times\) stabilizes an orbit representative \(\chi\). Indeed \(\chi\) extends to \(R^+\rtimes H_\chi\), and inducing its products with the one-dimensional characters of the abelian group \(H_\chi\) gives all irreducibles above the orbit by the Mackey–Clifford little-group criterion.

Every additive character \(\chi\) restricts to a character of the \(k\)-vector space \(\mathfrak m\). Via the nondegenerate finite-field trace pairing, there is a unique \(k\)-linear functional \(\beta:\mathfrak m\to k\) such that
\[
\chi(v)=\exp\!\left(\frac{2\pi i}{p}\operatorname{Tr}_{k/\mathbb F_p}\beta(v)\right)
\quad(v\in\mathfrak m),
\]
where \(p\) is the residue characteristic. There are exactly \(q\) extensions of each such restricted character to \(R^+\).

If \(\beta=0\), the character descends to the additive group of \(k\). One orbit is trivial, has stabilizer \(R^\times\) of order \(U\), and yields \(U\) affine characters of degree \(1\). The other \(q-1\) additive characters of \(k\) form one orbit under \(k^\times\), with stabilizer \(1+\mathfrak m\) of order \(q^d\); this yields \(q^d\) affine characters of degree \(q-1\).

If \(\beta\ne0\), a stabilizing unit must reduce to \(1\in k\), since otherwise it scales the nonzero functional \(\beta\). For \(1+w\) with \(w\in\mathfrak m\), it stabilizes \(\chi\) precisely when \(\chi(wr)=1\) for all \(r\in R\), equivalently \(\beta(w)=0\). Its stabilizer is therefore \(1+\ker\beta\), of order \(q^{d-1}\). Every such orbit has length \((q-1)q\). There are \(q(q^d-1)\) characters whose restriction is nonzero, hence \(L_d=(q^d-1)/(q-1)\) orbits. They contribute \(q^{d-1}L_d\) affine irreducibles of degree \(q(q-1)\).

The three affine degree rows, multiplied by \(U\), give the stated complete \(G\)-degree table. The sum of their squared degrees equals \(|G|=U^2T\), independently confirming exhaustiveness; their total count agrees with the conjugacy table, as required by ordinary character theory.

**Step 4: Total and limit.** Summing the class rows or the character-degree multiplicities gives
\[
k(G)=U\big(U+q^d+q^{d-1}L_d\big)=q^{2d-1}\big((q-1)q^2+q^d-1\big).
\]
The commuting probability is \(k(G)/|G|\), since summing element-centralizer orders counts commuting ordered pairs. Substitute \(|G|=U^2T=(q-1)^2q^{3d+1}\) and let \(d\) increase at fixed \(q\) to get the exact formula and limit.

## Verification

The accompanying dependency-free `verify.py` directly constructs finite rings, enumerates all invertible upper-triangular matrices, computes the full conjugacy orbit-size histogram using explicit matrix products and inverses, enumerates every additive character of each ring, and computes its orbits under units to reconstruct the predicted character degrees. It compares the outcomes against both tables and the class-number identity. The tested cases are split square-zero rings at \((q,d)=(2,1),(3,1),(2,2)\), residue rings \(\mathbb Z/4\mathbb Z\) and \(\mathbb Z/9\mathbb Z\), and the mixed-characteristic ring \(\mathbb Z/4\mathbb Z[\epsilon]/(2\epsilon,\epsilon^2)\). These are six full finite enumerations, including two rings of order eight of different characteristic. Run `python3 verify.py`; successful completion prints `VERIFY_OK`. The proofs of all prime-power cases and unbounded dimensions are symbolic and do not rely on finite testing.

## Relationship to prior work

Murray's 2000 work on conjugacy classes in parabolic subgroups supplies a general abelian-normal-subgroup orbit lemma and analyzes upper-block triangular groups over **fields**. Its results justify the orbit approach but do not count the classes or irreducible degrees here for nonprincipal finite local rings. More recent work on affine groups over finite **chain rings** establishes detailed conjugacy classes and full characters when the radical is principal; that case corresponds to \(d=1\), whereas the new nonprincipal case \(d\ge2\) has no generating additive character of the ring and requires the dual restriction argument above. A separate study of centralizers in **full affine monoids** counts commutation with noninvertible affine maps and does not give the ordinary group character-degree census. The general identification of the projective rank-two Borel group with an affine group is known, as is the classical little-group method. The contribution here is their combination with the nonprincipal radical geometry to give complete uniform class-size and character-degree spectra, including mixed-characteristic cases and the limiting commuting law.

## Limitations

The ring must be commutative and local with nonzero square-zero maximal ideal; no claim is made for longer radicals or noncommutative rings. Only irreducible **degrees and multiplicities**, not individual character values or an ordinary character table, are classified. The uniform spectra do not imply group isomorphism. Identical numerical rows, especially in characteristic two, must be merged. A historical equivalent of the nonprincipal finite-affine-group character-degree formula may exist under different terminology; the inspected sources and searches do not establish absolute priority. Finite computational checks do not replace the universal proof.

## References

- S. H. Murray, *Conjugacy classes in maximal parabolic subgroups of general linear groups*, arXiv:math/0001031v1, first public version 2000-01-06. https://arxiv.org/pdf/math/0001031
- *Conjugacy and ordinary character spectra of affine groups over finite chain rings*, public mathematical result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-conjugacy-and-ordinary-character-spectra-of-affine-groups-over-f--0a4181d7ad6d
- *Centralizer spectra of finite affine monoids distinguish local-ring geometry*, public mathematical result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-centralizer-spectra-of-finite-affine-monoids-distinguish-local-r--5531b23a5b4d
- D. Lins de Araujo, *Twisted conjugacy in soluble arithmetic groups*, Mathematische Nachrichten (2025), Section 3.1. https://doi.org/10.1002/mana.202300448
