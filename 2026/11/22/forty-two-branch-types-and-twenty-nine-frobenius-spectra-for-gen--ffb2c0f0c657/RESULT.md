# Frobenius on the two kernel components of a genus-four hyperelliptic Jacobian

## Finding

Let \(C/\mathbb F_q\) be a smooth projective geometrically connected hyperelliptic curve of genus four in odd characteristic, with ten geometric branch points \(B\). Its finite étale scheme of maximal Weil-isotropic subgroups of \(\operatorname{Jac}(C)[2]\) splits into two finite étale subschemes of degrees \(945\) and \(1350\). The first consists of kernels coming from perfect matchings of the ten branch points; the second is the complementary orbit. The columns `orbit_945` and `orbit_1350` of `kernel_spectra.csv` give their two complete Frobenius cycle spectra for each of the \(42\) possible branch partitions. There are **38 distinct ordered pairs** of component spectra among the \(42\) partitions, compared with 29 aggregate spectra.

**The component zeta functions contain strictly more information than the total kernel zeta function even together with rational Jacobian two-torsion.** In fact, branch types \(4\,2^3\) and \(4\,2^2\,1^2\) both have eight rational Jacobian two-torsion points and aggregate kernel spectrum \(1^7 2^{64}4^{540}\). Their component spectra differ:

| Branch type | Matching component | Complementary component |
|---|---|---|
| \(4\,2^3\) | \(1^7 2^{19}4^{225}\) | \(2^{45}4^{315}\) |
| \(4\,2^2\,1^2\) | \(1^3 2^{21}4^{225}\) | \(1^4 2^{43}4^{315}\) |

Here \(d^m\) denotes \(m\) cycles of length \(d\). These types are realized over \(\mathbb F_5\) by the smooth projective curves with affine equations
\[
y^2=P Q_1 Q_2 Q_3,\qquad y^2=P Q_1 Q_2 x(x-1),
\]
where \(P=x^4+2\), \(Q_1=x^2+2\), \(Q_2=x^2+3\), and \(Q_3=x^2+x+1\).

## Assumptions and scope

A rational kernel means a Frobenius-stable subgroup scheme, not a subgroup whose geometric points are all rational. Each kernel has order \(16\), and its quotient is a principally polarized abelian fourfold, not necessarily a Jacobian. A branch partition may include a point at infinity via a binary degree-ten branch form. The table applies whenever the partition occurs; it does not say that every partition is realized over each small field. Geometric and arithmetic Frobenius yield the same cycles up to reversal.

## Proof

**The two components.** The standard equivariant model for hyperelliptic two-torsion is the vector space of even subsets of \(B\) modulo complements, with symplectic form given by intersection parity. Its dimension is eight: on the even-weight subspace in ten binary coordinates the dot-product radical is exactly the all-ones line. The maximal isotropic subspaces have dimension four. They are the geometric points of the kernel scheme because two is invertible. The degree is \(\prod_{i=1}^4(2^i+1)=2295\).

A perfect matching partitions \(B\) into five pairwise orthogonal two-element subsets. Their classes span a maximal isotropic subspace: the only nontrivial relation is the sum of all five, which represents the whole branch set. The weight-two classes in this subspace are exactly those five pairs, since any union of pairs has size two or eight precisely when it uses one or four pairs. Thus the map from matchings is injective. All \(9!!=945\) matchings form one orbit under the symmetric group. For the complement, the exhaustive calculation below proves that it is another orbit. Both are Frobenius-invariant, making the decomposition intrinsic over the base field.

**Complete finite calculation.** Represent a two-torsion class by its even binary vector with tenth bit zero. The first eight bits are free and the ninth is their parity. The pairing of free vectors \(a,b\) is the parity of their intersection plus the product of their parities, modulo two. The supplied `verify_kernel_spectra.py` enumerates all \(200787\) four-dimensional subspaces by unique binary reduced row-echelon bases, tests the six pairings of the basis, and gets exactly \(2295\) isotropic subspaces. A separate enumeration by orthogonal extensions gives the same set. Coordinate permutations act by permuting the ten bits, complementing if the tenth bit is one. Using the adjacent transpositions gives exactly two orbits of sizes \(945,1350\). For each of the 42 partitions one representative permutation suffices, because conjugation of branch permutations conjugates the induced actions. Walking every cycle on each orbit verifies both columns of the supplied table. Distinct ordered pairs of columns give the count 38, independently checked by `verify_split_profiles.py`. The two rows in the finding are the rows for \((4,2,2,2)\) and \((4,2,2,1,1)\).

**Independent matching-component calculation.** A preserved matching is a fixed-point-free involution commuting with the branch permutation. For each branch-cycle length \(d\), let \(m\) be its multiplicity. Choose \(2k\) of those cycles and group them into \(k\) unordered pairs; each pair has \(d\) equivariant identifications. A cycle not paired with another must have even length and uses its unique antipodal matching. Thus the fixed-matching factor for length \(d\) is
\[
\sum_{\substack{0\le 2k\le m\\ d\,\mathrm{even}\ \mathrm{or}\ 2k=m}}
\frac{m!\,d^k}{(m-2k)!\,2^k k!}.
\]
Multiplying over \(d\) gives the fixed matching count. For each positive exponent \(h\) dividing the order of Frobenius on \(B\), replace a length-\(d\) cycle by \(\gcd(d,h)\) cycles of length \(d/\gcd(d,h)\) to apply this formula to the \(h\)-th power. For either component, if \(F(h)\) is the number of fixed points of that power, the number \(m_d\) of cycles of length \(d\) is recovered by inverting \(F(h)=\sum_{d\mid h}d m_d\). Its zeta function is \(\prod_d(1-T^d)^{-m_d}\). In particular the matching fixed counts at the two types of the witness are 7 and 3, although the aggregate has 7 in both cases.

**The curves over \(\mathbb F_5\).** The three quadratics are pairwise different and have nonsquare discriminants. The quartic \(P=x^4+2\) has no root since every nonzero fourth power is one. A factorization into monic quadratics would have the form \((x^2+a x+b)(x^2-a x+c)\), with \(bc=2\), \(b+c=a^2\), and \(a(c-b)=0\). If \(a=0\) it gives \(b^2=3\); otherwise \(c=b\) gives \(b^2=2\). Both contradict nonsquareness. The displayed products are therefore squarefree of degree ten. In each type a fixed torsion class has a fixed even-set representative: in the first type a set exchanged with its complement would have odd size five, and in the second there are fixed branch points. In the first type there are 16 even subsets formed from its four even cycles; in the second there are eight unions of even cycles and two ways to include the fixed points with even parity. Quotienting by complements gives eight rational torsion points in both cases.

## Reproduction

Run `python3 verify_kernel_spectra.py` and `python3 verify_split_profiles.py` alongside `kernel_spectra.csv`. The former recomputes the complete finite action. The latter checks the perfect matching fixed counts for all relevant powers of all 42 permutations, verifies the ordered count 38 and the two component rows of the witness, and checks the irreducibility of the quartic and quadratics by finite factor tests.

## Relationship to prior work and limitations

Bernatska–Kopeliovich, [arXiv:2306.14889](https://arxiv.org/abs/2306.14889), §5.2, already give the 2295 geometric Göpel systems and the 945/1350 split. The geometric counts and the standard matching count are not originality claims. Bruin–Kulkarni, [arXiv:2309.01959](https://arxiv.org/abs/2309.01959), study a different genus-four \((2,2)\)-decomposability question; Bruin–Doerksen, [arXiv:0902.3480](https://arxiv.org/abs/0902.3480), describe related arithmetic in genus two.

The distinct same-date record [Frobenius-stable maximal isotropic 2-torsion kernels for genus-four hyperelliptic Jacobians](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-frobenius-stable-maximal-isotropic-2-torsion-kernels-for-genus-f--70477d357316/RESULT.md) supplies the aggregate fixed counts for all 42 branch partitions. In particular it already states the examples of counts 151 and 39 for types \(2^5\) and \(2^4 1^2\), respectively, both with 16 rational two-torsion points. Moreover the power-partition and fixed-point inversion calculations above reconstruct all aggregate cycle spectra from that fixed-count table; the aggregate columns are included for comparison, not claimed as a distinct theorem here. The added statement is the two-component evaluation and the realized failure of aggregate data to determine it. This does not assert priority solely from the record dates or exclude unindexed equivalent calculations. The result describes the finite kernel scheme, not the polarized quotient targets or the frequencies of branch patterns in moduli.
