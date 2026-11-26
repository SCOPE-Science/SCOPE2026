# The split permutation normalizer of a monogenic inverse submonoid with a genuine chain

## Finding

Let \(f\) be a partial bijection of \([n]\) whose directed graph contains at least one chain with an arrow. Let \(H_f=\langle1_n,f,f^{-1}\rangle\) be the embedded inverse submonoid of the symmetric inverse monoid, with the ambient identity included. Write \(a_d\) for the number of directed cycles of vertex length \(d\), and \(b_l\) for the number of directed chains of vertex length \(l\). An undefined singleton counts as a chain of vertex length one; a fixed point of \(f\) instead counts as a cycle of length one.

Set
\[
K=\prod_{d\ge1}(C_d^{a_d}\rtimes S_{a_d})\times\prod_{l\ge1}S_{b_l},
\]
where the indicated symmetric groups in the cycle factors permute equal-length components and zero multiplicities contribute trivial factors. Then \(K\) identifies with \(C_{S_n}(f)\), and the permutation normalizer of the embedded submonoid splits as
\[
 N_{S_n}(H_f)\cong K\rtimes C_2.
\]
The nonidentity element of the displayed complement acts by **simultaneously inverting all cyclic phase rotations**, fixing all the displayed symmetric-group factors. In particular, the same involution lifts inversion of the generator on every component; there is only one quotient bit, not a separate reversal choice on each chain. This specifies the extension and its action, not just the size of the normalizer.

## Assumptions and scope

The claim concerns conjugation by full permutations of a finite set, not abstract automorphisms of the submonoid. The chain condition requires \(b_l>0\) for some \(l\ge2\); for \(n<2\) it is vacuous. No original contribution is claimed here for the no-chain-arrows normalizer, for the order of the stabilizer, or for the numerical conjugacy-orbit classification.

## Proof

**Generator fiber.** Two embedded census results establish that the inverse generators of \(H_f\) in this case are exactly \(f,f^{-1}\) [1, 2]. To see this, any nonempty word in \(f,f^{-1}\) has an exponent sum \(t\). It acts on cycles by rotation by \(t\), and on chains as a restriction of displacement by \(t\). Exponent sum zero gives an idempotent, which cannot generate \(f\). If \(|t|\ge2\), on a chain of length \(l\) it has rank at most \(\max(l-|t|,0)\), strictly less than \(l-1\) for any genuine chain. On the other components its rank is at most that of \(f\). Since two generators of the same inverse submonoid have equal rank by rank monotonicity (each is an inverse word in the other), only \(t=\pm1\) can give another generator. At those exponents the word is a restriction of \(f\) or \(f^{-1}\), respectively, and equal rank forces equality. The ambient identity alone does not generate \(f\). The two generators are distinct because a genuine chain has a first directed edge.

**Kernel.** A permutation normalizes \(H_f\) exactly when it sends \(f\) to a generator of \(H_f\); its action on this two-element set gives a homomorphism into \(C_2\) with kernel \(C_{S_n}(f)\). A permutation centralizes \(f\) exactly when it is an automorphism of the directed graph, preserving its partial transition rule. It may independently permute equal-length components, and any bijection between two specified equal-length cycles also has a choice of rotation phase. Between two specified equal-length directed chains it must preserve positions, so there is exactly one such bijection. This gives the kernel \(K\) above.

**Section and action.** Use disjoint labels for cycles and chains. On a cycle a vertex has coordinates \((d,i,j)\), with \(i\) its component index among the cycles of length \(d\), \(j\in\mathbb Z/d\mathbb Z\), and arrows \(j\mapsto j+1\). On a chain use coordinates \((l,i,j)\) with \(1\le j\le l\) and arrows \(j\mapsto j+1\) for \(j<l\). Define a permutation \(r\) by
\[
 r(d,i,j)=(d,i,-j)\quad\text{on cycles},\qquad
 r(l,i,j)=(l,i,l+1-j)\quad\text{on chains}.
\]
Conjugation by \(r\) reverses every directed edge, including exchanging the initial and terminal positions of every chain. Thus \(rfr^{-1}=f^{-1}\). The map \(r\) squares to the identity and is not in the kernel, so it defines a section of the two-element quotient. Changing \(i\) by a permutation leaves the displayed formula for \(r\) unchanged, so \(r\) commutes with all the chosen index-permutation factors. On a cycle a phase translation by \(a\) becomes a translation by \(-a\) under conjugation by \(r\). These computations prove the claimed action, also when a chain is a singleton or a rotation factor is trivial.

## Reproducibility and limitations

The proof is by explicit permutations and holds for every finite \(n\) in the stated regime. The accompanying `verify.py` enumerates generator fibers and orbit sizes through five vertices; those finite checks concern related numerical consequences, not the splitting or induced action. The explicit coordinate computation above establishes those structural assertions. This result does not identify abstract automorphism groups and does not assert historical priority over all permutation-normalizer treatments.

## Relationship to prior work

The embedded census theorems [1, 2] give the generator fibers. The cycle-chain element conjugacy classification [3, Proposition 2.11] implies that \(f^{-1}\) is conjugate to \(f\). Together these facts already give the index two of the centralizer in the normalizer, and hence the exact stabilizer order and orbit size once the component-centralizer order is counted. The corresponding statements without a genuine chain follow numerically from the unit-power generator fiber. Neither the bipartition count nor these numerical formulas are presented as original. For a single full cycle the multiplier splitting is classical [4]; componentwise multipliers extend that construction when there are no chain arrows. The claim here is restricted to the section and simultaneous-inversion action for the embedded submonoids with a genuine chain. An arbitrary conjugator to \(f^{-1}\) in the element classification does not by itself furnish an involutory section with the specified action.

## References

1. *Embedded monogenic inverse submonoids: a chain-period spectrum and a half-density law*, 2 November 2026, Proof §1. https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-embedded-monogenic-inverse-submonoids-a-chain-period-spectrum-an--d8394c30e54e
2. *Embedded monogenic inverse submonoids: exact census and a square-root nilpotent law*, 8 November 2026, Proof Steps 1–2. https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-embedded-monogenic-inverse-submonoids-exact-census-and-a-square--77e542c8edb6
3. J. Araújo, M. Kinyon and J. Konieczny, *Conjugacy in inverse semigroups*, Proposition 2.11, https://arxiv.org/abs/1810.03208.
4. Y. Chang et al., *Classification of Cyclic Steiner Quadruple Systems*, Journal of Combinatorial Designs 25 (2017), §2. https://wrap.warwick.ac.uk/id/eprint/80062/7/WRAP-classification-cyclic-systems-Holt-2016.pdf
