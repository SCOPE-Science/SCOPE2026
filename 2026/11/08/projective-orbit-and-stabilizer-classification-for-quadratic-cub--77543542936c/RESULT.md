# Projective orbit and stabilizer classification for quadratic–cubic Frobenius pentads

## Finding
Let \(q\) be any prime power and let \(\mathcal P_{2,3}(q)\) denote the set of reduced effective degree-five divisors on \(\mathbb P^1_{\mathbb F_q}\) consisting of one closed point of degree two and one closed point of degree three. The group \(G=\operatorname{PGL}_2(\mathbb F_q)\) acts on this set. Put \(N(q)=\#(\mathcal P_{2,3}(q)/G)\). Then
\[
N(q)=\begin{cases}
\dfrac{q(q-1)+4}{6},&q\equiv2\pmod 3,\\[3pt]
\dfrac{q(q-1)}6,&q\not\equiv2\pmod 3.
\end{cases}
\]
Every stabilizer is trivial, except that, when \(q\equiv2\pmod 3\), exactly **one** \(G\)-orbit has stabilizer cyclic of order three. This orbit has size \(q(q^2-1)/3\); every other orbit has size \(q(q^2-1)\). For every \(q\), the stabilizer-weighted orbit mass is
\[
\sum_{\mathcal O\in\mathcal P_{2,3}(q)/G}\frac{1}{|G_D|}=\frac{q(q-1)}6,
\]
where \(D\) is any member of \(\mathcal O\).

When \(q\equiv2\pmod3\), the exceptional orbit is represented constructively by the zero divisor of the product of \(z^2-z+1\) with **any** irreducible cubic factor of \(z^{q+1}-z^q+1\). The factorization into cubic factors is guaranteed and the representative is reduced. The assertion concerns *unordered divisors* (equivalently squarefree binary quintics up to scalar), not ordered five-tuples or five-pointed curves.

## Assumptions and scope
The field \(\mathbb F_q\) is arbitrary, including characteristics two and three. A closed point of degree \(d\) on \(\mathbb P^1\) means one orbit of length \(d\) under the \(q\)-power Frobenius on geometric points. Each object contains exactly five distinct geometric points, with Frobenius cycle type \((2)(3)\); in particular it has no \(\mathbb F_q\)-point. All automorphisms and equivalences are defined over \(\mathbb F_q\). The action has \(|G|=q(q^2-1)\).

## Proof
**Counting objects.** The number \(B_2\) of closed degree-two points of \(\mathbb P^1\) equals \((q^2-q)/2\). The number \(B_3\) of closed degree-three points equals \((q^3-q)/3\). Thus
\[
|\mathcal P_{2,3}(q)|=B_2 B_3
=\frac{q^2(q-1)^2(q+1)}6,
\qquad \frac{|\mathcal P_{2,3}(q)|}{|G|}=\frac{q(q-1)}6.
\]
The second equality is also the weighted orbit formula by orbit–stabilizer.

**Possible stabilizers.** A projectivity preserving a divisor must separately preserve its degree-two and degree-three Frobenius orbits. As a permutation of the three points in the latter, it commutes with the Frobenius three-cycle, so it belongs to its cyclic centralizer of order three. The map from the stabilizer to this permutation group is injective: a projectivity fixing three distinct geometric points is the identity. Consequently the stabilizer is either trivial or cyclic of order three. If an element \(g\) of order three stabilizes the divisor, its permutation of the two points of degree two is trivial, so these are both fixed points of \(g\). An order-three projectivity with two fixed points has them over \(\mathbb F_{q^2}\setminus\mathbb F_q\) only if \(q\equiv2\pmod3\). Indeed an order-three element is unipotent with one fixed point in characteristic three, split semisimple with two rational fixed points if \(3\mid q-1\), and nonsplit semisimple with one conjugate quadratic pair if \(3\mid q+1\).

**Counting the exceptional divisors.** Suppose \(q\equiv2\pmod3\). There are exactly \(q(q-1)\) elements of order three in \(G\): they form one nonsplit semisimple conjugacy class, with centralizer of size \(q+1\). Each such element \(g\) has exactly one quadratic closed point fixed pointwise, formed from its two eigenpoints. To determine the degree-three closed points invariant under \(g\), let \(F\) be \(q\)-Frobenius. Since a nonidentity projectivity cannot fix three geometric points, its action on an invariant degree-three Frobenius orbit must be either \(F\) or \(F^2\). For each \(h\in\{g,g^2\}\), the equation \(F(z)=h(z)\) has precisely \(q+1\) distinct geometric solutions on \(\mathbb P^1\). To see this directly, write \(h(z)=(az+b)/(cz+d)\) with \(ad-bc\ne0\). When \(c\ne0\), the degree-\(q+1\) equation
\[
cz^{q+1}+dz^q-az-b=0
\]
has no repeated root, since a repeated root would require \(cz^q=a\), forcing \(ad-bc=0\). When \(c=0\), the equation has \(q\) distinct affine roots and the additional solution at infinity. Since \(h\) is defined over \(\mathbb F_q\) and has order three, each such solution belongs to \(\mathbb P^1(\mathbb F_{q^3})\). Since \(h\) has no rational fixed point, none is rational. Therefore the solutions form exactly \((q+1)/3\) degree-three Frobenius orbits. The solutions for \(g\) and \(g^2\) give disjoint families (their intersection would consist of a fixed point of \(g\)). Thus each order-three element fixes exactly \(2(q+1)/3\) objects of \(\mathcal P_{2,3}(q)\).

Double-count pairs \((D,g)\) where \(D\in\mathcal P_{2,3}(q)\) and \(g\ne1\) stabilizes \(D\). There are \(q(q-1)\cdot2(q+1)/3=2|G|/3\) such pairs. Every exceptional divisor has exactly two nonidentity stabilizer elements, hence there are \(|G|/3\) exceptional divisors. Each exceptional \(G\)-orbit has size \(|G|/3\); there is exactly **one** exceptional orbit. Every other orbit is free. The number of free orbits is \((|\mathcal P_{2,3}(q)|-|G|/3)/|G|\), giving the first formula. If \(q\not\equiv2\pmod3\), all orbits are free and the second formula follows.

**Explicit exceptional representative.** The projectivity \(g(z)=1/(1-z)\) has order three, and its fixed-point polynomial is \(z^2-z+1\). This polynomial is irreducible over \(\mathbb F_q\) precisely when \(q\equiv2\pmod3\); this includes characteristic two. The Frobenius-twisted equation \(z^q=g(z)\) is \(z^{q+1}-z^q+1=0\). Its \(q+1\) roots are all of exact degree three, so it factors into \((q+1)/3\) distinct irreducible cubics. Each chosen cubic, together with \(z^2-z+1\), gives an exceptional divisor. Uniqueness of its projective orbit was just proved.

## Verification
The standalone file `verify_pentads.py` independently enumerates all irreducible monic quadratic and cubic polynomials over each prime field with \(q\in\{2,3,5,7,11,13\}\). It generates the actual projective orbits using translation, primitive scaling, and inversion, rather than Burnside's formula. It checks orbit sizes and stabilizer orders. Its output, freshly reproduced from this file, is:

```
p=2: degree2=1 degree3=2 pairs=2 orbits=1 stabilizers={3: 1} OK
p=3: degree2=3 degree3=8 pairs=24 orbits=1 stabilizers={1: 1} OK
p=5: degree2=10 degree3=40 pairs=400 orbits=4 stabilizers={1: 3, 3: 1} OK
p=7: degree2=21 degree3=112 pairs=2352 orbits=7 stabilizers={1: 7} OK
p=11: degree2=55 degree3=440 pairs=24200 orbits=19 stabilizers={1: 18, 3: 1} OK
p=13: degree2=78 degree3=728 pairs=56784 orbits=26 stabilizers={1: 26} OK
VERIFY_OK
```

These finite tests are checks, not an infinite proof. The proof above establishes all prime powers without reliance on enumeration.

## Relationship to prior work
The geometric theory of moduli and special symmetry loci of binary quintics is classical; du Plessis and Wall describe these loci over \(\mathbb C\). The new statement is specifically the arithmetic **Frobenius type \((2)(3)\)** orbit/stabilizer distribution over every finite field, including the unique nonsplit symmetry orbit and its weighted mass. Ho and Pries stratify finite-field Artin–Schreier branch loci by Frobenius splitting and analyze four-branch-point orbits; the present five-point stratum is not a consequence of their enumerations. Reis gives exact fixed-point formulas for the action on **irreducible** polynomials, but this divisor is reducible as a quadratic times a cubic, and stabilizer conditions tie together two different closed-point degrees. Gow and McGuire study invariant irreducible polynomials and the twisted Frobenius equation used here, but do not directly classify these mixed-degree orbit/stabilizer strata. These contributions and the elementary projective-group tools are not claimed as new.

## Limitations
This is one complete Frobenius stratum, not a count of all unordered five-point configurations or all Artin–Schreier covers with five branch points. It does not count covers with specified wild pole orders or full automorphism groups of the resulting curves. The projective symmetry group of the branch divisor need not be the full automorphism group of a cover branched there. An equivalent older finite-geometric orbit formula under different terminology remains a historical-priority risk. Independent mathematical audit is not claimed.

## References
1. A. du Plessis and C. T. C. Wall, *The moduli space of binary quintics*, European Journal of Mathematics; first online November 1, 2017. https://doi.org/10.1007/s40879-017-0187-8
2. A. M. Ho and R. Pries, *A Mass Formula For Artin–Schreier Curves Over Finite Fields*, arXiv:2203.10187 (March 18, 2022), especially Sections 2, 6, and 7. https://arxiv.org/abs/2203.10187
3. L. Reis, *On the existence and number of invariant polynomials*, arXiv:1811.02537 (November 6, 2018), especially Theorems 1.3–1.4. https://arxiv.org/abs/1811.02537
4. R. Gow and G. McGuire, *Invariant Rational Functions, Linear Fractional Transformations and Irreducible Polynomials over Finite Fields*, arXiv:2105.11247 (May 24, 2021), Sections 3, 5, and 9. https://arxiv.org/abs/2105.11247
