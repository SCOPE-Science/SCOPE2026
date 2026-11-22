# Image-rank-refined automorphism orbits of all dicyclic group endomorphisms

## Finding

Let \(m\ge2\), and let
\[
G_m=\operatorname{Dic}_m=\langle a,b\mid a^{2m}=1,\ b^2=a^m,\ bab^{-1}=a^{-1}\rangle.
\]
The group has order \(4m\). Let \(\mathcal K_m(z)\) count the conjugacy classes of **all** group endomorphisms under \(\operatorname{Aut}(G_m)\), weighted by the cardinality of each endomorphism's image. Here conjugation means \(\varphi\mapsto\alpha\varphi\alpha^{-1}\), not conjugation of two images as subgroups.

For \(m\ge3\), the complete image-rank-refined orbit polynomial is
\[
\boxed{\mathcal K_m(z)=z+(1+\mathbf1_{2\mid m})z^2+
\sum_{\substack{1\le u<2m\\u\text{ odd}}}
\tau\bigl(\gcd(u-1,2m)\bigr)z^{\,4m/\gcd(u,m)}
+3\mathbf1_{m\equiv2\pmod4}z^8.}
\]
For the exceptional quaternion group \(G_2\cong Q_8\),
\[
\boxed{\mathcal K_2(z)=z+z^2+5z^8.}
\]
Here \(\tau\) denotes the positive-divisor counting function. If \(m=2^e h\) with \(h\) odd and \(m\ge3\), the total number of classes is
\[
\boxed{\mathcal K_m(1)=(3\cdot2^e-1)\sigma(h)+2+\mathbf1_{e\ge1}+3\mathbf1_{e=1},}
\]
where \(\sigma(h)=\sum_{d\mid h}d\). In particular the family with \(e=1\) has three additional quaternionic orbits, of respective sizes \(4m,2m,2m\), absent at other valuations. The theorem also determines every individual conjugacy-class size as described below.

## Assumptions and scope

Groups and endomorphisms are ordinary abstract finite groups and group homomorphisms. All congruences on exponents of \(a\) are modulo \(2m\). Every element is uniquely \(a^r b^\epsilon\), with \(0\le r<2m\) and \(\epsilon\in\{0,1\}\). No hypothesis of characteristic, field, or commutativity is needed. The special case \(m=2\) is stated separately because its three cyclic subgroups of order four are permuted by automorphisms, whereas \(\langle a\rangle\) is characteristic for \(m\ge3\).

For \(m\ge3\), each endomorphism belongs to exactly one of these disjoint families:

1. **Coset-type:** \(F_{u,v}(a)=a^u\), \(F_{u,v}(b)=a^vb\), where \(u\) ranges over odd residues modulo \(2m\) and \(v\) ranges over all residues. There are \(2m^2\) such maps, each of image order \(4m/\gcd(u,m)\).
2. **Central-type:** \(a\mapsto1\) and \(b\mapsto1\) or \(a^m\), and, when \(m\) is even, also \(a\mapsto a^m\) with \(b\mapsto1\) or \(a^m\). The first map is trivial; the others have image order two.
3. **Quaternion-type (only \(m\equiv2\pmod4\)):** for \(v\bmod 2m\), let \(a\mapsto a^vb\), and let \(b\) map to one of \(a^{m/2},\ a^{3m/2},\ a^{v+m/2}b,\ a^{v+3m/2}b\). All \(8m\) maps have image \(Q_8\) of order eight.

In the coset family, write \(d_u=\gcd(u-1,2m)\). Two maps \(F_{u,v},F_{u',v'}\) are automorphism-conjugate if and only if \(u=u'\) and \(\gcd(v,d_u)=\gcd(v',d_u)\). For each divisor \(g\mid d_u\), the corresponding orbit has size
\[
\boxed{\frac{2m}{d_u}\,\varphi\!\left(\frac{d_u}{g}\right),}
\]
where \(\varphi(1)=1\). The central family gives two singleton classes if \(m\) is odd, and three classes (two singletons and a class of size two) if \(m\) is even. The quaternion-type family gives exactly the three classes specified in the Finding.

## Proof

**Exhaustion of endomorphisms.** A group homomorphism is uniquely specified by elements \(x=F(a)\) and \(y=F(b)\) satisfying \(x^{2m}=1\), \(y^2=x^m\), and \(yxy^{-1}=x^{-1}\); conversely these relations give a homomorphism by the presentation.

If \(x=a^u\) and \(y\notin\langle a\rangle\), then \(y^2=a^m\) and \(x^m=a^{um}\), so \(u\) is odd. The inversion relation is automatic and \(y=a^vb\) is otherwise unrestricted. If both \(x,y\in\langle a\rangle\), then inversion forces \(x^2=1\), so \(x=1\) or \(a^m\). The equation \(y^2=x^m\) gives \(x=1\), \(y\in\{1,a^m\}\) for odd \(m\); for even \(m\), it gives the four central-type maps. For odd \(m\), the potential solution \(x=a^m\) is already in the coset family with \(y=a^vb\), since a rotation cannot have square \(a^m\).

If \(x=a^vb\), it has order four. For odd \(m\), the element \(x^m\) lies outside \(\langle a\rangle\) whereas every square lies inside, so no solutions exist. For \(4\mid m\), \(x^m=1\); every possible \(y\) with \(y^2=1\) is central and cannot invert \(x\). For \(m\equiv2\pmod4\), \(x^m=a^m\), and the solutions \(y^2=a^m\) are rotations \(a^{m/2},a^{3m/2}\) and all coset elements. The inversion relation retains exactly the four displayed choices, using \(2(v'-v)\equiv m\pmod{2m}\) for a coset element \(a^{v'}b\). This proves completeness and image orders.

**Automorphism action.** For \(m\ge3\), \(\langle a\rangle\) is the unique cyclic subgroup of order \(2m\), because all other elements have order four. Hence every automorphism, and only an automorphism, has form
\[
\alpha_{r,s}(a)=a^r,\qquad \alpha_{r,s}(b)=a^s b,
\quad r\in(\mathbb Z/2m\mathbb Z)^\times,\quad s\in\mathbb Z/2m\mathbb Z.
\]
Direct substitution shows
\[
\alpha_{r,s}F_{u,v}\alpha_{r,s}^{-1}=F_{u,\,rv+(1-u)s}.
\]
For fixed \(u\), the translations by \((1-u)s\) have quotient \(\mathbb Z/d_u\mathbb Z\). The reduction of the unit group modulo \(2m\) onto the unit group modulo any divisor \(d_u\) is surjective. Multiplication by units on \(\mathbb Z/d_u\mathbb Z\) has one orbit for each gcd value \(g\mid d_u\), containing \(\varphi(d_u/g)\) classes modulo \(d_u\). Each residue there lifts to \(2m/d_u\) possible \(v\)'s. Thus the claimed orbit labels, sizes and \(\tau(d_u)\) classes at fixed \(u\) follow.

On central maps, both maps with \(a\mapsto1\) are fixed. For even \(m\), the remaining two are exchanged by \(\alpha_{r,s}\) with odd \(s\), giving the stated classes.

For quaternion-type maps, put \(m=2h\) with \(h\) odd. The automorphism group acts transitively on the \(2m\) possible values of \(x=F(a)\) outside \(\langle a\rangle\), so fix \(x=b\). The stabilizer of this value is parameterized by \(r\) a unit: if \(r\equiv1\pmod4\), take \(s=0\); if \(r\equiv3\pmod4\), take \(s=m\). On the four possible values of \(F(b)\) at this fixed \(x\), namely \(a^h,a^{3h},a^hb,a^{3h}b\), the stabilizer fixes the first two and interchanges the last two. The three full orbits consequently have sizes \(2m,2m,4m\), all image order eight.

For \(m=2\), \(G_2=Q_8\), every noncentral endomorphism is an automorphism, giving \(\operatorname{Aut}(Q_8)\cong S_4\). Conjugation on these 24 maps gives five conjugacy classes (the five cycle types). The three nontrivial maps with central image of order two form one orbit and the trivial map another. This yields \(z+z^2+5z^8\).

**Arithmetic summation.** The identity \(\tau(n)=\sum_{d\mid n}1\) gives
\[
\sum_{u\text{ odd }(\bmod\,2m)}\tau(\gcd(u-1,2m))
=\sum_{d\mid2m}\#\{u\text{ odd}:u\equiv1\pmod d\}.
\]
For even \(d\), the inner count is \(2m/d\); for odd \(d\), it is \(m/d\). With \(m=2^e h\) and \(h\) odd, summing first over powers of two gives
\[
(2^{e+1}-1)\sigma(h)+2^e\sigma(h)
=(3\cdot2^e-1)\sigma(h).
\]
Adding the central orbit count \(2+\mathbf1_{e\ge1}\) and the quaternionic count \(3\mathbf1_{e=1}\) proves the total formula. Since all orbit sizes and image orders were established above, it also proves the full polynomial.

## Verification

The self-contained Python 3 script `verify_dicyclic_endomorphism_orbits.py` enumerates every pair of elements satisfying the group presentation for \(2\le m\le12\), independently constructs the three normal-form families, and verifies equality of the resulting **sets**. It then enumerates the actual automorphism action on each pair, computes its orbits, checks the complete image-order-refined class distribution and individual sizes, and verifies the sum formula for each \(m\). For \(m=2\) it enumerates all 24 automorphisms directly rather than incorrectly using the affine stabilizer of \(\langle a\rangle\). Execute `python3 verify_dicyclic_endomorphism_orbits.py` in a directory containing that script; an ordinary Python 3 installation suffices. The expected final line is `DICYCLIC_FULL_ENDOMORPHISM_ORBIT_CHECKS_PASSED`. The enumeration checks only the finite range stated; the algebraic proof covers all \(m\ge2\).

Representative rank-orbit coefficient vectors are: \(\mathcal K_3(z)=z+z^2+2z^4+6z^{12}\); \(\mathcal K_4(z)=z+2z^2+11z^{16}\); \(\mathcal K_6(z)=z+2z^2+8z^8+15z^{24}\); and \(\mathcal K_{10}(z)=z+2z^2+8z^8+25z^{40}\).

## Relationship to prior work

Hu and Ruan (2022) classify smooth **skew morphisms** of dicyclic groups (generalized permutations with a power function). This is not a classification of all possibly nonbijective group endomorphisms modulo automorphism conjugacy. The authors' July 29, 2022 online article has primary MSC 20B25, secondary 05C10 and 14H57.

Madhusudanan, Sudhakara and Seth (2023), Theorem 6.1, quote and describe **descending** dicyclic endomorphisms. Their even-parameter family restricts the exponent of the image of \(b\) to even values and omits the quaternion-type maps; moreover, they study induced graphs on group elements, not the automorphism-orbit census of all endomorphisms. Their source's primary MSC is 05C25 and is used here as supporting context, not as the qualifying algebra source.

Malone (1973), Theorem 2, already provides total endomorphism and automorphism counts for generalized quaternion groups of power-of-two order. The unrefined total is therefore not claimed as novel. Puusemp (2006) studies endomorphism-semigroup determination for groups of order below 32, not the present uniform orbit-size and image-rank formulas. Standard elementary structure of dicyclic groups is used without claims of priority.

## Limitations

This is an internal self-review, not independent validation or a priority certification. Completeness over all \(m\) follows from the presented group-theoretic argument, not finite checks. The full text of Hu–Ruan's subscription article was unavailable beyond publisher/repository previews, but its stated object is bijective skew morphisms; no corresponding orbit theorem appears in material inspected. Other earlier unindexed results or a broader general conjugacy theorem could imply the result, so bibliographic originality remains provisional. No claim is made about group homomorphisms between different dicyclic groups, nor about simultaneous conjugation of tuples of endomorphisms.

## References

- K. Hu and D. Ruan, *Smooth skew morphisms of dicyclic groups*, Journal of Algebraic Combinatorics 56 (2022), 1119–1134. Published online 29 July 2022. https://doi.org/10.1007/s10801-022-01149-8
- V. Madhusudanan, G. Sudhakara and A. Seth, *Descending endomorphism graphs of groups*, AKCE International Journal of Graphs and Combinatorics 20 (2023), 148–155, especially §6 and Theorem 6.1. https://doi.org/10.1080/09728600.2023.2234956
- J. J. Malone, *Generalised quaternion groups and distributively generated near-rings*, Proceedings of the Edinburgh Mathematical Society 18 (1973), 235–238, especially Theorem 2. https://doi.org/10.1017/S0013091500009974
- P. Puusemp, *Groups of Order Less Than 32 and Their Endomorphism Semigroups*, Journal of Nonlinear Mathematical Physics 13, Supplement 1 (2006), 93–101. https://doi.org/10.2991/jnmp.2006.13.s.11
