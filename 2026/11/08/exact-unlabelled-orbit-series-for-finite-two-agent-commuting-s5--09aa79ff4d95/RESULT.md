# Exact unlabelled orbit series for finite two-agent commuting S5 frames

## Finding

Consider finite two-agent S5 frames whose **named** accessibility equivalences commute. Writing \(C(z)\) for the ordinary generating series of *connected* frames up to isomorphism, and \(U(z)\) for **all** frames up to isomorphism, the complete formulas are

\[
C(z)=\sum_{r,s\geq1}\ \sum_{\lambda\vdash r}\sum_{\mu\vdash s}
\frac{1}{z_{\lambda}z_{\mu}}
\prod_{i,j\geq1}
\left(\frac{z^{\operatorname{lcm}(i,j)}}{1-z^{\operatorname{lcm}(i,j)}}\right)^{\gcd(i,j)m_i(\lambda)m_j(\mu)},
\qquad U(z)=\exp\left(\sum_{h\geq1}\frac{C(z^h)}{h}\right).
\]

Here \(m_i(\lambda)\) counts parts of size \(i\) in a partition, and \(z_{\lambda}=\prod_{i\geq1}i^{m_i(\lambda)}m_i(\lambda)!\). A factor raised to exponent zero is one. Both series are formal power series; the coefficient of degree \(n\) receives contributions only from \(rs\leq n\).

The coefficients for \(n=0,1,\ldots,12\) are:

| \(n\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| connected \(c_n\) | 0 | 1 | 3 | 5 | 10 | 14 | 27 | 36 | 64 | 90 | 150 | 213 | 358 |
| all \(u_n\) | 1 | 1 | 4 | 9 | 25 | 54 | 136 | 294 | 684 | 1476 | 3271 | 6958 | 14980 |

There is also an exact transitivity refinement: the number of isomorphism classes of such frames on \(n\geq1\) worlds whose full automorphism group is transitive equals the number \(d_4(n)\) of ordered quadruples of positive integers with product \(n\).

## Assumptions and scope

A frame is a finite nonempty set \(W\) with **ordered, individually named** equivalence relations \(E,F\subseteq W\times W\). The defining requirement is \(E\circ F=F\circ E\), using ordinary relational composition. Isomorphism means a bijection of worlds preserving each named relation separately; no interchange of agent names is permitted. A connected component is an equivalence class of the join \(E\vee F\). The coefficients at \(n=0\) use the empty frame only as a combinatorial convention; no empty Kripke frame is otherwise assumed. Vertex transitivity always refers to automorphisms preserving both agent names. The coefficient tables and the series apply to every finite size, not merely to the tested sizes.

## Proof

**1. Connected components and matrices.** The composite of commuting equivalences is itself an equivalence relation: it contains each relation, is reflexive, is transitive by the equation \((EF)^2=E(FE)F=E(EF)F=EF\), and is symmetric because \((EF)^{-1}=FE=EF\). Therefore \(EF=E\vee F\). Fix a component \(D\) of this join; write its \(E\)-classes \(R_1,\dots,R_r\), and its \(F\)-classes \(S_1,\dots,S_s\). For any \(x\in R_i\) and \(y\in S_j\), the fact that \(x(EF)y\) gives a witness in \(R_i\cap S_j\). Thus every intersection is nonempty. Define \(a_{ij}=|R_i\cap S_j|\), producing a positive-integer \(r\)-by-\(s\) matrix.

Conversely, for any positive-integer matrix, construct disjoint cells of its prescribed cardinalities and define \(E\) by common row and \(F\) by common column. Both composites are universal on that component. Hence every positive matrix specifies a connected commuting frame. Because cells can be permuted freely internally, connected frames are isomorphic precisely when their matrices differ by a row permutation and a column permutation. Different components are unordered, so general frames are precisely finite multisets of these matrix-orbit types. This matrix description is existing background, not claimed as an independent new theorem.

**2. Counting the connected types.** Fix matrix dimensions \(r,s\). Burnside's lemma averages the fixed positive-integer matrices over \(S_r\times S_s\). Suppose the row permutation has \(m_i(\lambda)\) cycles of length \(i\) and the column permutation has \(m_j(\mu)\) cycles of length \(j\). One pair of these cycles induces exactly \(\gcd(i,j)\) cell orbits, each of length \(\operatorname{lcm}(i,j)\). Each cell orbit gets an independently chosen positive integer \(t\) and contributes \(\operatorname{lcm}(i,j)t\) worlds. Its generating factor is therefore \(z^{\operatorname{lcm}(i,j)}/(1-z^{\operatorname{lcm}(i,j)})\). Multiplying all such factors gives the fixed-matrix weight series. There are \(r!/z_{\lambda}\) row permutations of cycle type \(\lambda\), and \(s!/z_{\mu}\) column permutations of type \(\mu\); Burnside's average is the displayed \(C(z)\).

Every positive matrix has at least \(rs\) worlds, so for each coefficient only finitely many shapes contribute, justifying the unrestricted formal sums.

**3. Arbitrary component multisets.** If there are \(c_m\) connected isomorphism classes of size \(m\), any type can occur with multiplicity zero, one, two, and so on. Thus \(U(z)=\prod_{m\geq1}(1-z^m)^{-c_m}\). Taking formal logarithms yields the stated \(\exp(\sum_{h\geq1}C(z^h)/h)\) formula. This is an exact ordinary orbit generating series, with no adjustment by world-label permutations.

**4. Automorphisms and vertex transitivity.** For a connected component encoded by \(A=(a_{ij})\), an automorphism induces row and column permutations preserving \(A\), and may independently permute the \(a_{ij}\) worlds in each cell. Consequently
\[
|\operatorname{Aut}(A)|=\left(\prod_{i,j}a_{ij}!\right)
\left|\operatorname{Stab}_{S_r\times S_s}(A)\right|.
\]
If this group acts transitively on worlds, all cell sizes are equal, since cell cardinality is invariant; and its action is transitive on the cells, since an automorphism maps cells to cells. In particular all \(a_{ij}=t\) for one positive integer \(t\). Conversely, a constant \(r\)-by-\(s\) matrix has the transitive automorphism action of \(S_r\times S_s\), together with internal cell permutations. A general frame is vertex-transitive exactly when every component is isomorphic and each component is vertex-transitive. Thus its isomorphism type is uniquely specified by four positive integers \((h,r,s,t)\), standing for number of components, number of rows, number of columns, and common cell size, with \(n=hrst\). As the named relations prevent exchanging rows with columns, distinct ordered quadruples give different types. This proves the exact count \(d_4(n)\).

## Verification

The accompanying standalone `checker.py` uses exact rational arithmetic, integer partitions, and finite cycle-index products through degree 12; it asserts both displayed coefficient lists. Independently, it generates all ordered pairs of set partitions on \(n\leq6\) labelled worlds, tests the condition that each intersection matrix component is strictly positive, canonicalizes matrices modulo independent row/column permutations, and counts the resulting unordered component multisets. There are 44,168 partition pairs in total for sizes one through six; the direct labelled totals \(1,4,19,117,864,7459\) agree with the independently published labelled sequence OEIS A354458, while isomorphism totals \(1,4,9,25,54,136\) agree with Burnside. Direct canonical types also reproduce the transitive-subclass values \(1,4,4,10,4,16\). Execute `python3 checker.py` with Python 3.9+; only the standard library is required. The code verifies finite instances; the general series and quadruple formula follow from the preceding proof.

## Relationship to prior work

Rumenova and Tinchev's 2022 presentation *Modal definability of some classes of modal products: Two commuting equivalence relations* explicitly decomposes commuting S5 frames into matrices of nonempty cells, including disjoint collections of such matrices. That structural representation is therefore prior, and the present finding does **not** assert its novelty. The 2024/2025 paper of Anagnostopoulou-Merkouri, Bailey, and Cameron studies commuting partitions in transitive permutation groups, orthogonal block structures, and related groups; it supplies context and bears especially on the transitive subfamily. The present exact weighted Burnside orbit series counts arbitrary, not necessarily uniform, not necessarily transitive finite commuting frames up to isomorphism; this full isomorphism spectrum and its initial values are not implied by the previously tabulated **labelled** sequence A354458 alone. Balbiani, van Ditmarsch, and Lerouvillois (first public 2026-06-30) provide recent two-agent epistemic motivation through knowledge and intersection modalities, but their asynchronous dynamic theory is not asserted to contain this finite-frame enumeration.

## Limitations

Only two named equivalence relations are considered; swapping their names, adding valuations, requiring extra frame axioms, or counting pointed frames changes the problem. The matrix decomposition and general Burnside/multiset methods are well established; the intended contribution is their exact complete specialization to the unlabelled commutative S5 frame spectrum and its transitivity refinement. No asymptotic estimate for \(u_n\) is proved. Historical priority remains limited by specialist material not fully accessible, including the journal version of the 2022 commuting-relations study. The finite checker is evidence for selected coefficients only, not a substitute for the symbolic argument. Independent mathematical review has not been performed.

## References

- Philippe Balbiani, Hans van Ditmarsch, Clara Lerouvillois, *Resolving Asynchronous Distributed Knowledge*, arXiv:2606.31855 (first public 2026-06-30), https://arxiv.org/abs/2606.31855 .
- Yana Rumenova and Tinko Tinchev, *Modal definability of some classes of modal products: Two commuting equivalence relations*, presentation, February 11, 2022, https://www.math.bas.bg/algebra/seminarAiL/2022/No5_2022_02_11_Y_Rumenova/11Feb2022.pdf . See slides 12–14 for the pre-existing matrix decomposition.
- Marina Anagnostopoulou-Merkouri, R. A. Bailey, Peter J. Cameron, *Permutation groups, partition lattices and block structures*, first public September 16, 2024, arXiv:2409.10461, https://arxiv.org/html/2409.10461v3 . In particular Proposition 2.1 and the study of transitive partition systems.
- OEIS A354458, *Number of commuting pairs of equivalence relations on [n]*, Geoffrey Critzer (2022), https://oeis.org/A354458 . Published **labelled** counts, used as independent finite checks.
