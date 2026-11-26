# Nine Frobenius spectra of the fifteen genus-two Richelot kernels

## Finding

Let \(k=\mathbb F_q\) have odd characteristic, and let \(C/k\) be the smooth genus-two curve obtained by projectively completing \(y^2=f(x)\), for a squarefree polynomial \(f\in k[x]\) of degree six. Let \(\mathscr R_C\) denote the finite étale \(k\)-scheme whose geometric points are the maximal Weil-isotropic subgroups of \(\operatorname{Jac}(C)[2]\). Each subgroup is the kernel of a geometrically separable polarized \((2,2)\)-isogeny to a principally polarized abelian surface. These are *kernels*, not isogeny maps modulo automorphisms, and their codomains need not all be Jacobians.

The Frobenius action on the 15 geometric points of \(\mathscr R_C\) is determined by the irreducible-degree partition \(\lambda\) of the six roots of \(f\). All eleven possible partitions and their complete kernel cycle profiles are:

| Branch partition \(\lambda\) | Kernel Frobenius cycles | \(\#\mathscr R_C(k)\) | \(\#\operatorname{Jac}(C)(k)[2]\) |
|---|---|---:|---:|
| \((6)\) | \(1\,2\,3^2\,6\) | 1 | 1 |
| \((5,1)\) | \(5^3\) | 0 | 1 |
| \((4,2)\) | \(1\,2\,4^3\) | 1 | 2 |
| \((4,1,1)\) | \(1\,2\,4^3\) | 1 | 2 |
| \((3,3)\) | \(1^3\,3^4\) | 3 | 1 |
| \((3,2,1)\) | \(3\,6^2\) | 0 | 2 |
| \((3,1,1,1)\) | \(3^5\) | 0 | 4 |
| \((2,2,2)\) | \(1^7\,2^4\) | 7 | 4 |
| \((2,2,1,1)\) | \(1^3\,2^6\) | 3 | 4 |
| \((2,1,1,1,1)\) | \(1^3\,2^6\) | 3 | 8 |
| \((1,1,1,1,1,1)\) | \(1^{15}\) | 15 | 16 |

Here an entry \(d^m\) means \(m\) distinct Frobenius orbits of length \(d\), with omitted exponents equal to one. Thus there are exactly **nine distinct kernel cycle spectra** and exactly **two collisions**: the pairs of branch partitions \((4,2),(4,1,1)\) and \((2,2,1,1),(2,1,1,1,1)\). The exact possible numbers of rational maximal isotropic kernels are \(0,1,3,7,15\), subject to realizability of the branch partition over the chosen field.

In particular, the full zeta function \(Z(\mathscr R_C,T)\) does **not** determine the number of rational Jacobian two-torsion points. For explicit smooth curves over \(\mathbb F_7\), take

\[
C_1:\quad y^2=(x^2+1)(x^2+2)x(x-1),
\]
\[
C_2:\quad y^2=(x^2+1)x(x-1)(x-2)(x-3).
\]

Their respective branch partitions are \((2,2,1,1)\) and \((2,1,1,1,1)\), hence

\[
Z(\mathscr R_{C_1},T)=Z(\mathscr R_{C_2},T)
=\frac{1}{(1-T)^3(1-T^2)^6},
\]

but \(\#\operatorname{Jac}(C_1)(\mathbb F_7)[2]=4\) and \(\#\operatorname{Jac}(C_2)(\mathbb F_7)[2]=8\). More exceptionally, an irreducible branch sextic gives **one rational Richelot kernel while the Jacobian has no nonzero rational two-torsion point**. The kernel is rational as a subgroup scheme without having rational nonidentity elements.

## Assumptions and scope

The base field is finite of odd characteristic. The hyperelliptic branch divisor consists of the six distinct finite roots of a squarefree sextic; the family therefore excludes characteristic two and branch collisions. The statements are conditional on the actual six-root factorization partition and hold for every such curve. Every partition listed is realized by some curve for every odd \(q\ge7\); for smaller fields some patterns, especially six distinct finite rational roots, may be unavailable. The scheme \(\mathscr R_C\) records maximal isotropic order-four subgroup schemes and not individual generators, codomain isomorphism classes, or the full Jacobian zeta function.

## Proof

1. **Fifteen-point identification.** Let the six geometric Weierstrass branch points be \(b_0,\ldots,b_5\). The geometric two-torsion of the genus-two Jacobian is the symplectic vector space of even subsets of the six labels, modulo complementary subsets, giving exactly 16 classes. The nonzero classes correspond to unordered pairs of labels. Each maximal Weil-isotropic subgroup contains zero and three nonzero classes whose pair representatives partition the six labels into three disjoint pairs. Conversely, each unordered perfect matching of six labels gives a maximal isotropic subgroup. There are \(6!/(2^3 3!)=15\) such matchings. This is the standard Richelot quadratic-splitting description (see references).

2. **Frobenius equivariance.** The \(q\)-power Frobenius permutes the six branch roots, with disjoint-cycle lengths equal to the irreducible factor degrees of \(f\). Since the preceding construction uses only the canonical branch-point labels, Frobenius acts on the 15 matchings by relabeling. This shows that the cycle decomposition of \(\mathscr R_C\) depends only on the partition of six, not on the coefficients of \(f\).

3. **Exhaustive exact classification.** There are exactly eleven integer partitions of six. For each partition, select a permutation with those cycle lengths and apply it to all 15 unordered matchings. Partitioning the resulting 15-element permutation into its orbits yields the second column. The accompanying stand-alone verifier constructs the matchings recursively, computes each orbit decomposition, and independently cross-checks it via fixed-point counts of every power of the permutation. It likewise enumerates the 16 even-subset classes modulo complements and checks the rational two-torsion column. It checks that precisely the two stated pairs share a profile and that no other collisions occur. This is an exhaustive finite enumeration of the complete mathematical cases, not sampling of selected curves.

4. **Examples and consequence.** Over \(\mathbb F_7\), both \(x^2+1\) and \(x^2+2\) are irreducible, since \(-1\) and \(-2\) are nonsquares. The linear roots displayed above are distinct and avoid the quadratic roots, so both sextics are squarefree. Their factorization partitions and the table give the two equal kernel-scheme zeta functions and unequal rational two-torsion orders. The checker also verifies squarefreeness of both expanded sextics by polynomial gcds and verifies the quadratic irreducibility directly. The case \((6)\) in the same table proves the rational-kernel/rational-point distinction.

For any finite étale zero-dimensional scheme with \(m_d\) closed points of residue degree \(d\), its zeta function is \(\prod_d(1-T^d)^{-m_d}\). Applying this identity to each row completes the zeta classification and the two collision assertions.

## Verification

Run `python3 richelot_kernel_spectra.py` with standard Python 3. It reports the eleven partitions, their 15-point Frobenius cycles, rational kernel counts and rational Jacobian two-torsion counts. It terminates with `RICHELOT_FROBENIUS_NINE_KERNEL_SPECTRA_VERIFIED` only after independently checking all power-fixed-point equations, all stated collisions, and the two smooth illustrative curves. No external packages, downloaded datasets or unlisted files are needed.

## Relationship to prior work

The identification of Richelot kernels with quadratic splittings, the generic count 15, and the construction of polarized \((2,2)\)-isogenies are classical and are *not* claimed as new. Brock–Howe (2020) discuss the characteristic-not-two count while studying a different characteristic-two phenomenon. Kunzweiler (2022/2024) develops explicit finite-field genus-two isogeny computation and generally works with chosen kernels, often with rational generators. Magma's Richelot documentation explains the quadratic splitting over cubic algebras, including nonsplit rational kernels. The additional subject here is the exact **eleven-type Frobenius orbit table, its nine distinct kernel zeta fingerprints, and the two collisions, including the mismatch with rational two-torsion**. These are not the same as counts of *split ordered quadratic factorizations*, since a subgroup may descend without its three nonidentity elements descending individually.

The S\(_6\)-combinatorial framework and finite-field isogeny literature make the classification accessible, so the main residual priority risk is an earlier unindexed cycle-index calculation or a stronger published theorem explicitly tabulating the same action. No uniqueness beyond the searches recorded with the accompanying review is asserted.

## Limitations

The classification is for the reduced finite étale kernel scheme, not the geometry of individual isogeny codomains, moduli isomorphism classes, or higher-power torsion. The table does not claim that all eleven factorization patterns occur over every small finite field. It neither establishes a new method for computing Richelot isogenies nor proves a statement about characteristic two. Its originality assessment remains provisional pending independent literature review.

## References

- N. Bruin and K. Doerksen, *The Arithmetic of Genus Two Curves with (4,4)-Split Jacobians*, 2009-02-19 original public preprint, https://arxiv.org/abs/0902.3480, sections 4 and 6: the complete Galois-stable matching construction and criteria for multiple rational kernels, without the eleven-cycle zeta classification.
- S. Kunzweiler, *Efficient Computation of (2^n,2^n)-Isogenies*, Cryptology ePrint 2022/990, initially approved 2022-08-03, https://eprint.iacr.org/2022/990, later published at https://doi.org/10.1007/s10623-024-01366-1 (2024).
- B. W. Brock and E. W. Howe, *Purely inseparable Richelot isogenies*, initial public preprint 2020-02-06, https://arxiv.org/abs/2002.02122, especially the introduction on the 15 characteristic-not-two kernels.
- Magma Handbook, *Richelot Isogenies*, https://magma.maths.usyd.edu.au/magma/handbook/text/1615, the quadratic-splitting and cubic-algebra descriptions.
- H. T. Dang and D. V. Nguyen, *Derivative-Free Richelot Isogenies via Subresultants with Algebraic Certification*, public preprint 2026-07-03, https://arxiv.org/abs/2607.03376, especially section 2 on split quadratic factorization and the distinction from nonsplit kernels.
