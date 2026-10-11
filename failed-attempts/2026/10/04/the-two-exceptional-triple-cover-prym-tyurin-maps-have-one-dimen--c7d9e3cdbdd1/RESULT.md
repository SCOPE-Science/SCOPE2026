# The two exceptional triple-cover Prym–Tyurin maps have one-dimensional fibers
## Finding
Consider the elliptic Prym–Tyurin maps
\[
PT_{p,m}:\mathcal R(p,m)_\xi\longrightarrow
\mathcal A_{\frac m2(p-1)}
\]
constructed from cyclic covers of an elliptic curve in Valdebenito Sepúlveda, *Prym--Tyurin varieties coming from intermediate coverings of curves*.

For
\[
p=3,
\]
the two cases excluded from the paper's generic-finiteness theorem have an exact uniform description:
\[
\operatorname{rank}(dPT_{3,2})=1,
\qquad
\operatorname{rank}(dPT_{3,3})=2
\]
at every smooth point of the corresponding source. Since
\[
\dim\mathcal R(3,m)_\xi=m,
\]
both maps have generic fiber dimension
\[
1.
\]

There is also a moduli-theoretic interpretation of the rank defect. The associated principally polarized abelian varieties carry the order-\(3\) automorphism induced by the deck action. Its two nontrivial Hodge eigenspaces have dimensions
\[
(1,1)\quad\text{for }m=2,
\qquad
(1,2)\quad\text{for }m=3.
\]
The invariant tangent space in the principally polarized abelian moduli space therefore has dimensions
\[
1\quad\text{and}\quad2,
\]
respectively. The Prym–Tyurin differential has exactly these ranks, so it fills the whole invariant tangent space. Locally, the Prym–Tyurin images are full-dimensional inside the corresponding order-\(3\) Eisenstein automorphism loci.

## Assumptions and scope
The statement concerns the elliptic, ramified construction of the cited paper, with the discrete generating vector fixed and a nonzero \(3\)-torsion point marked as in the definition of \(PT_{p,m}\). The marking is finite and does not affect differential rank.

The source expresses the codifferential of the underlying Prym map as the sum of multiplication maps
\[
\mu_i:
H^0(E,M_i)\otimes H^0(E,N_i)
\longrightarrow
H^0(E,M_i\otimes N_i)
\simeq H^0(E,\mathcal O_E(D)),
\]
where
\[
1\le i\le\frac{p-1}{2}
\]
and
\[
\deg M_i+\deg N_i=m.
\]
For \(p=3\), there is exactly one index \(i=1\).

The source's Lemma 5.1(c) gives
\[
(\deg M_1,\deg N_1)=(1,1)
\]
when \(m=2\), and gives the unordered pair
\[
\{\deg M_1,\deg N_1\}=\{1,2\}
\]
when \(m=3\).

## Proof
On an elliptic curve, every positive-degree line bundle \(L\) satisfies
\[
h^0(E,L)=\deg L.
\]

For \(m=2\), both \(M_1\) and \(N_1\) have degree \(1\). Their spaces of sections are one-dimensional. The product of two nonzero sections on the integral curve \(E\) is nonzero, so
\[
\operatorname{rank}\mu_1=1.
\]
Because \(p=3\) supplies no second complementary pair, this is the entire codifferential. Hence
\[
\operatorname{rank}(dPT_{3,2})=1.
\]

For \(m=3\), after interchanging \(M_1,N_1\) if needed, take
\[
\deg M_1=1,\qquad \deg N_1=2.
\]
Let \(s\) be the unique nonzero section of \(M_1\), up to scalar. Multiplication by \(s\),
\[
H^0(E,N_1)\longrightarrow H^0(E,M_1\otimes N_1),
\]
is injective: if \(st=0\), then \(t\) vanishes on the nonempty open set where \(s\ne0\), hence \(t=0\). Therefore
\[
\operatorname{rank}\mu_1=h^0(E,N_1)=2,
\]
and thus
\[
\operatorname{rank}(dPT_{3,3})=2.
\]

The source parameter space has dimension \(m\). The rank theorem consequently gives generic fiber dimension
\[
m-(m-1)=1
\]
in both exceptional cases.

It remains to interpret the rank. The deck transformation \(\sigma\) of order \(3\) acts on the Prym–Tyurin Hodge space without a trivial summand. For \(p=3\), the two eigenspaces for the primitive cube roots of unity have dimensions
\[
a=\deg M_1,\qquad b=\deg N_1.
\]
Hence their multiplicities are \((1,1)\) or \((1,2)\).

At a principally polarized abelian \(m\)-fold, the tangent space to \(\mathcal A_m\) is
\[
\operatorname{Sym}^2 H^0(P,\Omega_P^1)^\vee.
\]
If \(\sigma\) has eigenvalues \(\zeta,\zeta^2\) with multiplicities \(a,b\), the invariant part of this symmetric square consists exactly of the cross terms
\[
V_\zeta^\vee\otimes V_{\zeta^2}^\vee,
\]
so it has dimension
\[
ab.
\]
For \((a,b)=(1,1)\) this is \(1\); for \((1,2)\) it is \(2\). Since the Prym–Tyurin family preserves \(\sigma\), its differential lands in this invariant tangent space. The ranks computed above equal its full dimension. Thus the image is locally full-dimensional in the corresponding order-\(3\) automorphism locus.

## Verification
The accompanying `verify.py` checks the complete dimension arithmetic used in the proof. It verifies the two degree patterns from the source, the elliptic \(h^0\)-dimensions, the resulting codifferential ranks \(1\) and \(2\), the generic fiber dimension \(1\), and the equality of those ranks with the invariant symmetric-square tangent dimensions.

The nonzero-section injectivity argument is mathematical rather than numerical: multiplication by a nonzero section of a line bundle on an integral curve is injective on global sections of any line bundle.

The saved replay output ends in `VERIFY_OK`.

## Relationship to prior work
The initiating paper proves generic finiteness of \(PT_{p,m}\) for
\[
p\ge5,\ m\ge2,
\]
and for
\[
p=3,\ m\ge4.
\]
Its proof explicitly treats \(m=2\) and \(m=3\) for \(p\ge5\) by using at least two complementary character pairs. For \(p=3\), only one pair exists, which is exactly why that argument does not apply.

The source states the degree patterns needed here but does not state the exact ranks, the one-dimensional generic fibers, or the identification of those ranks with the full invariant tangent dimensions of the order-\(3\) automorphism loci.

Targeted searches for the source identifier together with the exceptional parameters, for the rank statements, and for Prym–Tyurin families filling Eisenstein order-\(3\) loci found no covering result. Older literature on cyclic triple covers, Prym maps, and unitary or Picard modular loci supplies surrounding moduli theory but did not yield this statement for the present construction.

## Limitations
This does not extend the source's generic-finiteness theorem to the two exceptional cases; it proves the opposite behavior, namely one-dimensional generic fibers.

The local full-dimensional statement concerns the automorphism locus with the induced order-\(3\) action and its Hodge signature. It does not claim a global degree, birationality, or global equality with every connected component of an Eisenstein or Picard modular variety.

No claim is made about the separate genus-\(2\) isotropic étale family of the source.

## References
1. V. Valdebenito Sepúlveda, *Prym--Tyurin varieties coming from intermediate coverings of curves*, arXiv:2608.04298v1, 2026.
2. Classical deformation theory of principally polarized abelian varieties, identifying the tangent space with the symmetric square of the Hodge cotangent space.
3. Standard unitary PEL theory for order-\(3\) actions, in which signatures \((1,1)\) and \((1,2)\) give complex dimensions \(1\) and \(2\).
