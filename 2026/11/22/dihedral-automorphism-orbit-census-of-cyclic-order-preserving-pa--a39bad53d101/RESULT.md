# Dihedral automorphism-orbit census of cyclic-order-preserving partial permutations

## Finding

For each integer \(n\ge3\), let \(\mathcal P_n=\mathcal{POPI}_n\) be the inverse monoid of all injective, cyclic-order-preserving partial maps on a regularly ordered \(n\)-point circle. Let \(O_{n,k}\) be the number of orbits on its rank-\(k\) elements under its **full semigroup automorphism group**. Its known automorphism group is the dihedral group of order \(2n\), acting by simultaneous relabeling of sources and targets. The following formulas determine every \(O_{n,k}\), for \(0\le k\le n\), without generating the monoid.

For a rotation by \(s\) places, set \(g=\gcd(n,s)\) (so \(\gcd(n,0)=n\)) and \(d=n/g\), and define

\[
R_{n,s}(z)=1+\sum_{\ell=1}^{g}d\ell\binom g\ell^2 z^{d\ell}.
\]

For a reflection with \(f\in\{0,1,2\}\) fixed ambient vertices, set \(m=(n-f)/2\), and define

\[
H_{n,f}(z)=1+\sum_{j=0}^{f}\sum_{t=0}^{m}\mathbf1_{j+2t>0}\gcd(2,j+2t)\binom fj^2\binom mt^2 z^{j+2t}.
\]

Here \(\mathbf1\) denotes the usual indicator. Then the complete rank-orbit polynomial is

\[
\boxed{\sum_{k=0}^n O_{n,k}z^k=\frac1{2n}\left(\sum_{s=0}^{n-1}R_{n,s}(z)+\begin{cases}nH_{n,1}(z),&n\ \text{odd},\\ \frac n2\bigl(H_{n,0}(z)+H_{n,2}(z)\bigr),&n\ \text{even}.\end{cases}\right).}
\]

In particular the total number \(O_n=\sum_k O_{n,k}\) has the divisor-sum form

\[
\boxed{O_n=\frac14\sum_{g\mid n}\varphi(n/g)\binom{2g}{g}+\begin{cases}\frac32\binom{n-1}{(n-1)/2},&n\ \text{odd},\\ \frac12\binom n{n/2}+2\binom{n-2}{(n-2)/2},&n\ \text{even}.\end{cases}}
\]

Here \(\varphi\) is Euler's totient. Further, \(O_{n,0}=1\), \(O_{n,1}=O_{n,n}=\lfloor n/2\rfloor+1\), and the next-to-unit stratum has the particularly simple size

\[
\boxed{O_{n,n-1}=\binom n2+1.}
\]

As \(n\to\infty\), \(O_n\sim \frac14\binom{2n}{n}\sim4^n/(4\sqrt{\pi n})\). Equivalently, the proportion of elements whose dihedral conjugation stabilizer is nontrivial tends to zero exponentially.

## Assumptions and scope

Identify the points with \(\mathbb Z/n\mathbb Z\) in their standard circular order. An element of \(\mathcal P_n\) is the empty map or a partial bijection \(u:A\to B\) such that reading the image of \(A\) in cyclic order produces \(B\) in cyclic order (possibly starting at another point). For fixed nonempty subsets \(A,B\) of common cardinality \(k\), exactly \(k\) such maps exist; explicitly the increasing lists \(A=(a_0,\ldots,a_{k-1})\), \(B=(b_0,\ldots,b_{k-1})\) are paired by \(a_i\mapsto b_{i+t\bmod k}\), for \(0\le t<k\). Distinct pairings are distinct partial maps. Rank means the cardinality of the domain, equal to the image cardinality, and rank zero contains only the empty map. The formula is for automorphism orbits of elements, not Green classes, the number of endomorphisms, or the ordinary conjugacy relation by arbitrary members of the monoid.

The automorphism-group identification \(\operatorname{Aut}(\mathcal P_n)\cong D_{2n}\), by conjugation with the \(n\) rotations and \(n\) reflections of the circular point set, is a previously established theorem, not a new assertion here. The formulas themselves are proved below for all \(n\ge3\).

## Proof

**1. Burnside reduction.** Let \(G=D_{2n}\) act on partial maps by \(u\mapsto p u p^{-1}\). Since the rank is invariant and \(G\) is the full automorphism group, Burnside's lemma computes the rank-orbit polynomial by averaging over all \(2n\) fixed-map rank polynomials. We determine the rotational and reflectional polynomials directly.

**2. Rotational fixed maps.** Fix \(p(i)=i+s\pmod n\). This permutation has \(g=\gcd(n,s)\) cycles, each of length \(d=n/g\). A partial map \(u:A\to B\) commutes with \(p\) only if both \(A\) and \(B\) are unions of cycles of \(p\). Thus their common size must be \(k=d\ell\), and there are \(\binom g\ell^2\) choices of \((A,B)\). Conversely, for each such choice, \(p\) shifts the cyclicly ordered \(k\)-element sets \(A\) and \(B\) by the **same number of cyclic positions**: a rotation of the ambient circle by \(s\) places passes through exactly \(ks/n\) selected positions, an integer under this invariance condition. Every one of the \(k\) cyclic-order-preserving bijections \(A\to B\) therefore commutes with \(p\). The empty map is fixed. This proves \(R_{n,s}\), including the identity case \(s=0\).

**3. Reflectional fixed maps.** Let \(p(i)=a-i\pmod n\) be a reflection. It has \(f\) fixed ambient vertices and \(m=(n-f)/2\) exchanged pairs, where \(f=1\) if \(n\) is odd and \(f\in\{0,2\}\) if \(n\) is even. For a \(p\)-invariant subset of size \(k=j+2t\), select \(j\) of the \(f\) fixed vertices and \(t\) of the \(m\) exchanged pairs. The reflection restricted to this \(k\)-point cyclic set is again an order-reversing involution of a circle with exactly \(j\) fixed points. Two such cyclic sets \(A,B\) admit a commuting **cyclic-order-preserving** bijection if and only if their numbers \(j\) of restricted fixed points agree: the corresponding involutions are conjugate inside the group of rotations of the ordered \(k\)-gon precisely when their axes have the same vertex/edge type. For \(k\) odd there is exactly one such cyclic shift; for \(k\) even there are exactly two, the number of solutions of \(2v\equiv c\pmod k\). Equivalently there are \(\gcd(2,k)\) shifts. This statement includes \(k=1\) (one shift) and \(k=2\) (two shifts), where every bijection of the two ordered points is cyclic-order-preserving. Hence the coefficient of \(z^{j+2t}\) in the nonempty fixed-map polynomial is \(\gcd(2,j+2t)\binom fj^2\binom mt^2\). Adding the empty map proves \(H_{n,f}\).

**4. Rank-orbit formula.** There are \(n\) rotations. For odd \(n\), all \(n\) reflections have \(f=1\). For even \(n\), exactly \(n/2\) reflections have \(f=0\), and \(n/2\) have \(f=2\). Averaging the fixed-map polynomials gives the boxed rank-orbit identity. Each coefficient is a nonnegative integer because it is an orbit count, not merely an integer-valued formal expression.

**5. Total and boundary coefficients.** Vandermonde's identity and a distinguished-element count give
\[
\sum_{\ell=1}^{g}\ell\binom g\ell^2=\frac g2\binom{2g}{g},\qquad\sum_{t=0}^m\binom mt^2=\binom{2m}{m}.
\]
Consequently \(R_{n,s}(1)=1+\frac n2\binom{2g}{g}\) and
\[
H_{n,f}(1)=\left(2+f^2+2\binom f2^2\right)\binom{2m}{m}-1.
\]
(The negative unit corrects the separately counted empty map.) There are \(\varphi(n/g)\) rotations with \(\gcd(n,s)=g\). Substitution into Burnside's formula cancels the constant contributions of rotations and reflections and yields the stated divisor sum, with the two reflection parity cases.

For rank one, a partial map is specified by an ordered source–target pair; the dihedral orbit is determined by the circular distance between the two points up to negation, giving \(\lfloor n/2\rfloor+1\) orbits. For rank \(n\), the elements are the \(n\) rotations, and reflection conjugation identifies a rotation with its inverse, giving the same count. For rank \(n-1\), no nonidentity rotation can preserve an \((n-1)\)-point subset, so the identity rotation fixes exactly \((n-1)n^2\) maps. Every parity of \(n\) yields a total of exactly \(2n\) reflection-fixed rank-\(n-1\) maps: if \(n\) is odd every reflection fixes \(2\); if even, the \(n/2\) two-vertex-axis reflections fix \(4\), and the remaining reflections fix none. Dividing their sum by \(2n\) yields \(\binom n2+1\).

**6. Asymptotics and generic stabilizer.** The identity-rotation contribution to Burnside is \(\frac14\binom{2n}{n}+\frac1{2n}\). Every nonidentity rotation has \(g\le n/2\), so their total contribution is \(O(n2^n)\); all reflection contributions are also \(O(n2^n)\) by the displayed binomial identities. Thus \(O_n=\frac14\binom{2n}n+O(n2^n)\), which yields the asymptotics. Since the monoid has \(1+\frac n2\binom{2n}n\) elements, the union bound applied to fixed sets of nonidentity group elements shows that the proportion with nontrivial stabilizer is \(O(n^2 2^n/(n\binom{2n}n))=O(n^{3/2}2^{-n})\). In particular it vanishes exponentially.

## Verification

The accompanying Python program `verify_orbits.py` independently builds all cyclic-order-preserving partial injections of degrees \(3\) through \(7\), checks each rotation and reflection fixed-point count **separately in each rank**, and verifies the Burnside orbit polynomial. For degrees \(3\) through \(6\), it additionally constructs actual orbits under relabeling rather than relying on Burnside's lemma. It also checks the identity between the divisor-sum total and the polynomial sum in all degrees \(3\) through \(18\).

The resulting total orbit counts for \(n=3,4,5,6,7\) are \(9,27,74,262,891\), respectively. The five rank-orbit vectors are included in `verification_output.txt`. The file concludes with `CYCLIC_ORIENTED_INVERSE_MONOID_ORBIT_CHECKS_PASSED`. These are **finite corroborations**, not substitutes for the above proof for all \(n\).

## Relationship to prior work

The basic cyclic-image definition, rank cardinalities and total monoid cardinality are established in earlier work, particularly Umar (2011), Proposition 33 and Corollaries 34–37, and are **not** claimed here. The group identification is established in Araújo–Fernandes–Jesus–Maltcev–Mitchell (2011), Theorem 5.5, recalled in Li–Fernandes (2022), which classifies endomorphisms and counts them; the action is used, not rediscovered here. The inspected primary sections treat cardinalities of *labeled elements* or of *endomorphisms*, rather than the number of element-orbits for simultaneous rotations and reflections. This distinction is essential: dividing the raw rank count by \(2n\) is generally incorrect because of stabilizers, and the contribution of reflections is parity dependent.

A related published study of maximal-index nilpotent chains in the same monoid restricts to a very special subset of the rank-\(n-1\) stratum and gives endpoint-attainability and totient-fibre results. It does not imply the present **full-automorphism orbit count on every rank**. A different published study counts involutions in the **dihedral restriction inverse monoid**, a strictly narrower object defined using restrictions of global isometries; its object and invariant are distinct. No claim of a new general Burnside principle is made. Exhaustive historical priority cannot be certified: a general cycle-index/partial-map equivalence theorem might give the same formulas after specialization.

## Limitations

The result covers \(\mathcal{POPI}_n\), not all oriented partial injections \(\mathcal{PORI}_n\), noninjective orientation-preserving maps, or restrictions of global dihedral symmetries. The enumeration counts automorphism-orbits, **not** semigroup conjugacy under arbitrary nonunits, automorphism-group orbits on subsemigroups, or individual orbit sizes. The classical 2000 article introducing the monoid was inspected through its abstract only; its full text was not accessible through the tried public sources. Its emphasis on presentations, ideals and congruences makes overlap less likely but not logically impossible. The claim remains subject to independent mathematical verification and historical-priority assessment; no independent audit has been performed.

## References

1. D. B. Li and V. H. Fernandes, *Endomorphisms of semigroups of oriented transformations*, arXiv:2207.12823v1, 26 July 2022. https://arxiv.org/abs/2207.12823. In particular, the introduction and Theorem 2.12.
2. J. Araújo, V. H. Fernandes, M. M. Jesus, V. Maltcev, J. D. Mitchell, *Automorphisms of partial endomorphism semigroups*, Publ. Math. Debrecen 79 (2011), 23–39, Theorem 5.5. https://doi.org/10.5486/PMD.2011.4703. Open text: https://publi.math.unideb.hu/paper/1584/download/10_5486_PMD_2011_4703.pdf.
3. A. Umar, *Combinatorial Results for Semigroups of Orientation-Preserving Partial Transformations*, Journal of Integer Sequences 14 (2011), Article 11.7.5, Section 4. https://cs.uwaterloo.ca/journals/JIS/VOL14/Umar/umar2.pdf.
4. V. H. Fernandes, *The monoid of all injective orientation preserving partial transformations on a finite chain*, Communications in Algebra 28 (2000), 3401–3426. https://doi.org/10.1080/00927870008827033. Full text not inspected.
5. D. B. Li and V. H. Fernandes, *On semigroups of orientation-preserving partial permutations with restricted range*, arXiv:2401.02185v1 (4 January 2024). https://arxiv.org/abs/2401.02185. The abstract treats restricted-range Green relations, regularity and rank.
