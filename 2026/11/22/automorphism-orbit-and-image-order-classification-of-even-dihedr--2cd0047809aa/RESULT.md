# Automorphism-orbit and image-order classification of even dihedral retractions

## Finding

Let \(n\ge4\) be even and let \(G=D_{2n}=\langle r,s\mid r^n=s^2=1,\;srs=r^{-1}\rangle\), of order \(2n\). A *retraction* is an endomorphism \(f:G\to G\) with \(f^2=f\). Write \(d\parallel n\) for a *unitary divisor*, meaning \(d\mid n\) and \(\gcd(d,n/d)=1\); let \(\omega(n)\) count the distinct prime divisors. Put \(\epsilon_n=1\) for \(n\equiv2\pmod4\) and \(0\) otherwise.

The following four families are disjoint and exhaustive:

1. For every \(d\parallel n\), let \(a_d\) be the unique residue modulo \(n\) satisfying \(a_d\equiv0\pmod d\) and \(a_d\equiv1\pmod{n/d}\). There are exactly \(d\) maps
   \[
   F_{d,b}:\quad r\longmapsto r^{a_d},\qquad s\longmapsto r^b s,
   \qquad b\equiv0\pmod{n/d}.
   \]
   Their image has order \(2n/d\), and the \(d\) maps form a single automorphism-conjugacy orbit. The unitary divisor \(d=1\) gives the identity map, while \(d=n\) gives one of the two reflection-image orbits.

2. There are exactly \(n\) additional maps, indexed by \(0\le c<n\), given by
   \[
   H_c(r)=r^cs,\qquad
   H_c(s)=\begin{cases}r^cs,&c\text{ even},\\1,&c\text{ odd}.
   \end{cases}
   \]
   Each image has order two, and all \(n\) maps form one automorphism-conjugacy orbit.

3. Only if \(n\equiv2\pmod4\), putting \(z=r^{n/2}\), there are exactly two further maps
   \[
   J_0(r)=z,\quad J_0(s)=1;\qquad J_1(r)=z,\quad J_1(s)=z.
   \]
   Their images have order two and they constitute one orbit of size two.

4. The trivial homomorphism \(r,s\mapsto1\) is a singleton orbit with image order one.

Consequently the full image-order enumerator is
\[
 R_n(t)=\sum_{f^2=f}t^{|\operatorname{im}f|}
 =t+\sum_{d\parallel n}d\,t^{2n/d}+(n+2\epsilon_n)t^2,
\]
and hence
\[
 R_n(1)=1+n+2\epsilon_n+\prod_{p^a\parallel n}(1+p^a).
\]
The complete orbit-size multiset is \(\{1\}\sqcup\{d:d\parallel n\}\sqcup\{n\}\sqcup(\{2\}\text{ if }\epsilon_n=1)\); its cardinality is \(2^{\omega(n)}+2+\epsilon_n\). In the multiset, repeated numerical sizes denote distinct orbits.

## Assumptions and scope

The group has the stated presentation with \(n\) even and at least four; no claim is made for odd \(n\), or for alternative uses of dihedral notation in which the subscript denotes the rotation order. Conjugacy of endomorphisms means \(f\sim\alpha f\alpha^{-1}\) for \(\alpha\in\operatorname{Aut}(G)\), not conjugacy of their images alone. The image-size variable \(t\) records the number of elements in the image subgroup, not linear-algebra rank.

## Proof

**Generator-pair criterion.** Any homomorphism is determined by \(x=f(r)\), \(y=f(s)\), satisfying \(x^n=y^2=1\) and \(yxy=x^{-1}\). Idempotence is equivalent to \(f(x)=x\) and \(f(y)=y\). Every group element has the unique form \(r^j s^e\), with \(j\) modulo \(n\) and \(e\in\{0,1\}\). We partition possibilities according to whether \(x\) is a rotation or a reflection and whether \(y\) is a reflection.

**Rotation–reflection pairs.** Set \(x=r^a\) and \(y=r^bs\). The presentation relations are automatic, and \(f(x)=r^{a^2}\), \(f(y)=r^{ab+b}s\). Thus \(f^2=f\) precisely when \(a^2\equiv a\pmod n\) and \(ab\equiv0\pmod n\). By the Chinese remainder theorem, an idempotent residue \(a\) is specified by selecting, at each prime-power factor of \(n\), whether it is zero or one. Setting \(d=\gcd(a,n)\) gives \(d\parallel n\), \(a=a_d\), and the congruence on \(b\) forces \(b\equiv0\pmod{n/d}\), with exactly \(d\) solutions. The element \(r^{a_d}\) has order \(n/d\); its subgroup together with a reflection has order \(2n/d\).

**Reflection-image pairs.** Suppose \(x=r^cs\). Then \(x^2=1\), so the relation \(x^n=1\) holds because \(n\) is even. Since \(f(x)=f(r^cs)=x^c y=x\), necessarily \(y=x^{1-c}\), which equals \(x\) for even \(c\), and \(1\) for odd \(c\). These satisfy both the presentation and \(f(y)=y\). Hence exactly the \(n\) maps \(H_c\) arise, with image \(\{1,x\}\). In particular, no image of order four from two distinct commuting involutions can be the image of a retraction of this type.

**Rotation–rotation pairs.** Suppose \(x=r^a\) and \(y\) is a rotation of order dividing two. Since \(y\) centralizes \(x\), the presentation forces \(x=x^{-1}\), so \(x=1\) or \(x=z=r^{n/2}\). If \(x=1\), idempotence of \(y\) forces \(y=1\), giving the trivial map. If \(x=z\), the choices are \(y=1,z\). Both satisfy \(f(x)=x^{n/2}=x\) precisely when \(n/2\) is odd, equivalent to \(n\equiv2\pmod4\); then \(f(y)=y\) is automatic. This proves exhaustive disjointness and the image-order formula.

**Automorphism orbits.** For \(n\ge4\), the rotation subgroup is characteristic (it consists of the identity together with the elements of order greater than two and their generated subgroup); all automorphisms are
\[
 \alpha_{u,v}(r)=r^u,\quad \alpha_{u,v}(s)=r^vs,\qquad \gcd(u,n)=1,\quad v\in\mathbb Z/n\mathbb Z.
\]
Conjugation sends a rotation–reflection map with parameters \((a,b)\) to one with
\[
 a'=a,\qquad b'\equiv ub+(1-a)v\pmod n.
\]
For fixed \(d\parallel n\), multiplication by \(1-a_d\) is bijective on the allowed residue subgroup \((n/d)\mathbb Z/n\mathbb Z\): it equals one modulo \(d\) and zero modulo \(n/d\). Thus \(v\) moves every allowed \(b\) to every other, and each such family is one orbit of size \(d\).

For the reflection-image family, \(\alpha_{u,v}H_c\alpha_{u,v}^{-1}=H_{uc+v}\) (the second generator image adjusts with the parity of the new index). Varying \(v\) gives one orbit of size \(n\). In the central exceptional family, every unit \(u\) is odd and fixes \(z\), while conjugation by \(\alpha_{1,v}\) interchanges \(J_0\) and \(J_1\) when \(v\) is odd. The trivial map is fixed. Distinct families cannot mix: automorphisms preserve the characteristic rotation subgroup, the property that \(f(r)\) is a rotation or reflection, and the value \(a\) for rotation-image maps. Therefore these are exactly the orbits, and there are \(2^{\omega(n)}+2+\epsilon_n\) of them. Summing the orbit sizes gives \(R_n(1)\).

## Verification

The accompanying standalone Python checker enumerates all possible generator images in the finite dihedral group, filters by the defining presentation, directly evaluates \(f^2=f\), and compares the complete set of resulting maps with the four families above. It independently constructs every automorphism and its conjugation action, then compares the actual orbit-size multiset and image-order histogram to the symbolic formulas. Every even \(n\) from \(4\) through \(32\) was checked, giving fifteen complete finite instances. See `verify_dihedral.py` and `verify_output.txt`. These checks validate sample instances, not the universal quantifier; the preceding argument supplies the all-\(n\) proof.

For example, the total retraction counts at \(n=4,6,8,10,12\) are \(10,21,18,31,33\). The two-adic exceptional maps first occur at \(n=6\), and occur exactly when \(n\equiv2\pmod4\).

## Relationship to prior work

Jeremiah Johnson (2012) counts all homomorphisms \(D_m\to D_n\), and for even \(n\) obtains \((n+2)^2\) endomorphisms. That baseline does not determine which satisfy \(f^2=f\), their image-order profiles, or their orbits under automorphisms. Madhusudanan, Sudhakara, and Seth (2023), Section 5, classify *descending* dihedral endomorphisms and their associated element graph; a descending endomorphism preserves every normal subgroup. The present object instead consists of every idempotent group endomorphism, including non-descending retractions, and the invariant is the automorphism-conjugacy and image-order spectrum. Work on retractions of generalized dihedral groups with odd-order abelian kernels has a disjoint parity hypothesis. The formulas here are not claimed to follow merely from matching numeric endomorphism totals.

## Limitations

The result is restricted to finite even dihedral groups \(n\ge4\) and ordinary group endomorphisms. It does not describe the full endomorphism monoid multiplication table, commuting pairs of retractions, or arbitrary generalized dihedral groups with noncyclic even kernels. Finite verification extends only through \(n=32\); the proof does not depend on those experiments. Historical priority cannot be established by an unsuccessful literature search; a broader unindexed theorem on group retracts could imply these orbit formulas. A related 2023 book chapter on descending endomorphisms was found at abstract level only, although the associated journal article's complete dihedral section was materially inspected.

## References

1. Jeremiah Johnson, *The Number of Group Homomorphisms from \(D_m\) into \(D_n\)* (2012), arXiv:1201.2363, https://arxiv.org/abs/1201.2363 .
2. Vinay Madhusudanan, G. Sudhakara, and Arjit Seth, *Descending endomorphism graphs of groups*, AKCE International Journal of Graphs and Combinatorics **20** (2023), 148–155, published online 15 August 2023, DOI:10.1080/09728600.2023.2234956, https://doi.org/10.1080/09728600.2023.2234956 .
3. Vinay Madhusudanan, Arjit Seth, and G. Sudhakara, *Descending Endomorphisms of Some Families of Groups*, in *Applied Linear Algebra, Probability and Statistics* (2023), DOI:10.1007/978-981-99-2310-6_20 (abstract inspected, full text unavailable).
