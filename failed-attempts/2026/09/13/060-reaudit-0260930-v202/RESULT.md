# G3 = <a,b,c | (a b^{-1} a b c^2)^6 = 1> contains D_inf and is not CSA

## Context

Let F = F(a,b,c) and w3 = a b^{-1} a b c^2, R its image in G3 = F / <<w3^6>>.
The admitted target asks whether G3 contains a subgroup isomorphic to the
infinite dihedral group D_inf, either by exhibiting explicit order-2 elements
x,y with xy of infinite order, or by proving no such subgroup exists (hence
CSA). One-relator groups with torsion satisfy the classical torsion theorem
(R has exact order n; every finite-order element is conjugate to a power of
R), and for such groups CSA holds iff D_inf is absent (Gildenhuys-
Kharlampovich-Myasnikov). Deciding the instance requires witnesses, not just
the general criterion.

## Definitions

D_inf = Z/2 * Z/2 = <r,s | r^2 = s^2 = 1>, equivalently <t> rtimes Z/2 with
xtx^{-1} = t^{-1}. A group is CSA if every maximal abelian subgroup is
malnormal. Put x = R^3, y = a R^3 a^{-1}, t = xy in G3.
Abelianization: G3^ab = Z^3 / <6(2,0,2)> = Z^3 / <(12,0,12)>; [R] = (2,0,2).
Separating map theta: F -> S_4, theta(a) = (2 3), theta(b) = id,
theta(c) = (0 1 2 3), permutations composed left-to-right.

## Result

Theorem. In G3 = <a,b,c | w3^6 = 1> with w3 = a b^{-1} a b c^2, x = R^3 and
y = a R^3 a^{-1} are distinct involutions whose product t = xy has infinite
order, so <x,y> is isomorphic to D_inf. Consequently G3 contains D_inf and
is not CSA.

Word facts: w3 is cyclically reduced of length 6, involves a,b,c, is not a
proper power, and has exponent sums (2,0,2) with gcd 2, hence non-primitive.

## Proof / evidence

R has exact order 6 and every finite-order element of G3 is conjugate to
R^k (quoted Karrass-Magnus-Solitar/Newman/Pride torsion theorem, hypotheses
verified above). Hence x = R^3 has order 2, as does its conjugate y, and
x t x^{-1} = t^{-1} for t = xy by direct computation.

Distinctness: the word image theta(R) = (0 2)(1 3), of order 2, so
theta(R)^6 = id and theta descends to G3. Then theta(x) = (0 2)(1 3) != id
so x != 1, and theta(y) = (0 3)(1 2) != theta(x) so x != y; both verified
independently by script. The image has order 24 (onto S_4).

Infinitude of t: if t had finite order, t = g R^k g^{-1}; conjugacy
t^{-1} = xtx^{-1} forces R^k ~ R^{-k}. Since conjugates agree in
abelianization, 2k[R] = 0 with [R] of exact order 6 in G3^ab, so k = 0 or
3 mod 6. k = 0 gives t = 1, i.e. y = x, excluded above. k = 3 gives
[t] = [x], but [x] = (6,0,6) != 0 while [t] = [x]+[y] = 2(6,0,6) =
(12,0,12) = 0, contradiction. Hence t has infinite order.

Lemma: <x,y> with x^2 = y^2 = 1, x != y, xy of infinite order is D_inf,
since the surjection Z/2*Z/2 -> <x,y> kills no (rs)^m (infinite order) and
no r(rs)^m (else x = t^{-m} gives t^2 = 1). Applying it yields
<x,y> ~= D_inf. CSA failure: <t> is maximal abelian in D_inf with
x<t>x^{-1} = <t>, x not in <t>, violating malnormality;
subgroups of CSA groups are CSA, so G3 is not CSA.

## Limitations

The torsion theorem is quoted, not re-proved. The S_4 representation is only
a separating witness; its kernel is not analyzed. No claims are made about
the full subgroup lattice, hyperbolicity, or conjugacy beyond what is used.

## Reproducibility

Run output/artifacts/verify_w3.py (word combinatorics), verify_perm_rep.py
(S_4 witness, distinctness, image order), search_perm_rep.py (exhaustive
S_3/S_4 search), check_abelianization.py ([R] order 6, [x] order 2,
[t] = 0, conjugacy constraint). All rerun cleanly.

## References

Gildenhuys-Kharlampovich-Myasnikov, CSA-groups and separated free
constructions (1995): torsion one-relator CSA iff no D_inf. Newman (1968
thesis), Pride (1977), Karrass-Magnus-Solitar: torsion/centralizer and
two-generator subgroup theory.
