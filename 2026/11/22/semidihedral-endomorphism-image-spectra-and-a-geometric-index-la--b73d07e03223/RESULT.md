# Semidihedral endomorphism image spectra and a geometric index law

## Finding

For every integer \(n\ge4\), put \(m=2^{n-1}\) and \(h=m/2\), and let \(G_n\) be the semidihedral group of order \(2^n\) defined below. Write \(E_n(z)\) for the polynomial that counts all group endomorphisms by the **cardinality** of their image, and \(R_n(z)\) for the corresponding polynomial restricted to composition-idempotent endomorphisms (retractions). Then

\[
E_n(z)=z+\left(\frac{3m}{2}+3\right)z^2+\frac{3m}{2}z^4
+\sum_{j=3}^{n-1}m2^{j-3}z^{2^j}+\frac{m^2}{4}z^{2^n},
\qquad
R_n(z)=z+mz^2+z^{2^n}.
\]

In particular, there are exactly \(m^2/2+2m+4\) endomorphisms and exactly \(m+2\) retractions. The only proper, nontrivial **retract** is isomorphic to \(C_2\), although endomorphism images of order four exist and are all isomorphic to \(C_2\times C_2\). Every proper, nonabelian image is dihedral, with the orders \(2^3,2^4,\ldots,2^{n-1}\) all realized; the full image is semidihedral.

Under conjugation by \(\operatorname{Aut}(G_n)\), the retractions form exactly four orbits: two singleton orbits (trivial map and identity) and two orbits of size \(m/2\), each consisting of maps of image order two. Thus this proper-retraction geometry separates the semidihedral family from both the generalized-quaternion and dihedral families at the same power-of-two group order.

Finally, for uniformly random \(F\in\operatorname{End}(G_n)\), the index \(I_n=[G_n:\operatorname{im}F]\) converges in total variation, as \(n\to\infty\), to the distribution

\[
\Pr(I=1)=\frac12,\qquad \Pr(I=2^v)=2^{-v-1}\quad(v=1,2,\ldots).
\]

All equations count actual homomorphisms, not merely isomorphism types of images.

## Assumptions and scope

Let \(n\ge4\) be any integer, \(m=2^{n-1}\), \(h=m/2\), and \(a=h-1\). The group is

\[
G_n=\langle r,s\mid r^m=s^2=1,\ srs^{-1}=r^{a}\rangle
\cong C_m\rtimes C_2.
\]

Every element has a unique form \(r^i s^\epsilon\), for \(0\le i<m\) and \(\epsilon\in\{0,1\}\). The polynomials have coefficients in the ordinary integers and use cardinality rather than logarithmic rank. Define \(\operatorname{Ret}(G_n)=\{F\in\operatorname{End}(G_n):F\circ F=F\}\).

The first public research context used here is the 2023-04-20 open-access paper on cyclic and generalized-quaternion Hughes subgroups by Beike, Carleton, Costanzo, Heath, Lewis, Lu and Pearce, whose primary MSC is 20D15 and whose cyclic-index-two classification includes the semidihedral action. The earlier structural account of Flake and Thevis, publicly available from 2020-03-30, is supporting literature. Neither is used as a proof of the present enumerations.

## Proof

**Step 1: element orders and possible images.** Squaring gives \((r^i s)^2=r^{hi}\). Consequently \(r^i s\) is an involution exactly when \(i\) is even, and otherwise it has order four. The complete list of elements whose square is the identity is
\[
1,\quad c=r^h,\quad r^{2j}s\ (0\le j<m/2).
\]

An endomorphism is uniquely determined by \(x=F(r)\) and \(y=F(s)\), subject to
\[
x^m=1,\qquad y^2=1,\qquad yxy^{-1}=x^a.\]
We partition these possibilities by whether \(x\) lies in \(\langle r\rangle\).

**Step 2: cyclic image for the first generator.** Suppose \(x=r^i\). If \(y=1\) or \(c\), conjugation fixes \(x\), so \(m\mid(a-1)i\). Since \(\gcd(m,a-1)=2\), necessarily \(i\in\{0,h\}\). This gives four endomorphisms: one trivial and three with image order two.

If \(y=r^{2j}s\), for arbitrary \(0\le j<m/2\), the relation holds for **every** residue \(0\le i<m\). There are \(m^2/2\) such maps. For odd \(i\), the map is an automorphism: the \(m/2\) odd choices of \(i\) and the \(m/2\) possibilities for \(j\) give \((m/2)(m/2)=m^2/4\) automorphisms. For \(i=0\) the image has order two, and for \(i=h\) it is \(C_2\times C_2\), each occurring \(m/2\) times. For any nonzero even \(i\ne h\), set \(v=v_2(i)\), so \(1\le v\le n-3\). The element \(r^i\) has order \(2^{n-1-v}\), while conjugation by \(r^{2j}s\) acts on it by inversion because \(a\equiv-1\pmod {2^{n-1-v}}\). Thus the image is a dihedral group of order \(2^{n-v}\). There are
\[
\frac m2\cdot \frac m{2^{v+1}}=\frac{m^2}{2^{v+2}}=m2^{n-v-3}
\]
such maps for each \(v\) in that interval.

**Step 3: coset image for the first generator.** Suppose \(x=r^i s\). If \(i\) is odd, then \(x\) has order four and \(x^a=x^{-1}\). The central involutions \(1,c\) cannot conjugate \(x\) to its inverse. If \(y=r^{2j}s\), the relation would imply \(4j+2ai\equiv0\pmod m\), whose left side is \(2\pmod4\). Hence there are no endomorphisms with odd \(i\). If \(i\) is even, \(x^a=x\); exactly the four involutions
\[
y\in\{1,c,x,xc\}
\]
commute with \(x\). For each of the \(m/2\) even choices of \(i\), the choices \(1,x\) give image \(C_2\) and the choices \(c,xc\) give image \(C_2\times C_2\). Thus this case contributes \(m\) endomorphisms of image order two and \(m\) of image order four.

**Step 4: collect coefficients.** Adding the three cases yields one trivial map, \(3m/2+3\) maps of image order two, \(3m/2\) of image order four, \(m2^{j-3}\) of each image order \(2^j\) for \(3\le j\le n-1\), and \(m^2/4\) automorphisms. This proves the displayed formula for \(E_n(z)\), including the endomorphism total.

**Step 5: idempotence and automorphism orbits.** If \(F\) is idempotent, then its image generators are fixed by \(F\). In the cyclic-first-generator case, this leaves the trivial map, the identity \(r\mapsto r,\ s\mapsto s\), and \(m/2\) projections \(r\mapsto1,\ s\mapsto r^{2j}s\). In the coset-first-generator case it leaves precisely \(m/2\) projections \(r\mapsto r^{2j}s,\ s\mapsto r^{2j}s\). All have image order two unless they are trivial or identity. (In particular, none of the maps with order-four image is idempotent.) This proves \(R_n(z)\).

Every automorphism has \(r\mapsto r^u\), \(s\mapsto r^{2w}s\), with \(u\) odd and \(w\) a residue modulo \(m/2\). These automorphisms act transitively on the parameter \(j\) within each family of projections. The two families cannot be conjugate: one kills the characteristic cyclic subgroup's generator \(r\), whereas the other does not; equivalently, their kernels have different intersections with \(\langle r\rangle\). This gives exactly the four stated orbits and their sizes.

**Step 6: index law.** Exactly \(m^2/4\) endomorphisms have index one; for each \(1\le v\le n-3\), exactly \(m^2/2^{v+2}\) have index \(2^v\). There are only \(O(m)\) additional endomorphisms, with image order at most four, against a total of \(m^2/2+2m+4\). After dividing by this total, each fixed index mass converges to the displayed value. The omitted geometric tail after \(v>V\) is uniformly \(O(2^{-V})\) up to a term \(O(m^{-1})\), giving total-variation convergence, not just convergence of individual masses.

## Verification

The included pure-Python program `check.py` constructs multiplication and inversion directly from the presentation, enumerates **all** generator-image pairs satisfying the defining relations, computes their actual image sets, and tests composition-idempotence and automorphism conjugation. It verifies every coefficient of both polynomials, the total counts, and the four retraction orbits for \(m=8,16,32,64\), corresponding to group orders \(16,32,64,128\). The accompanying `CHECK_OUTPUT.txt` contains the deterministic output of the program. This is finite corroboration; the proof above establishes the infinite family.

## Relationship to prior work

Beike et al. (2023) classify tidy finite \(p\)-groups using cyclic and quaternion Hughes subgroups, and explicitly describe the semidihedral action among cyclic-index-two groups. That paper does not count all semidihedral endomorphisms, image types, or retractions. Flake and Thevis (2020/2023) compare maximal-class families by commutator and origami data, not the image-rank distribution. Puusemp (1996) works under a coprime cyclic-factor restriction that excludes this example; Puusemp (2002) addresses endomorphism-semigroup characterizability for cyclic semidirect products even in the prime-power case, making it a particularly relevant **unresolved historical-priority risk** because the full article was unavailable for a complete comparison. Puusemp (2005/2006) covers groups of order 16 and groups of order below 32; those bounded cases do not by themselves state the all-order formula or limiting index law. Previously published dihedral and generalized-quaternion retraction distributions are only comparisons; no priority for those comparisons is asserted.

## Limitations

The theorem concerns group homomorphisms of these finite semidihedral groups, **not** their group algebras, semigroup endomorphisms of other objects, or all finite \(2\)-groups. The smallest semidihedral group in the family has order sixteen; no smaller-order extrapolation is claimed. The novelty assessment is limited by an inaccessible 2002 paper on the endomorphism semigroups of the same general semidirect products and by possible unindexed stronger classifications. Finite numerical verification alone does not certify infinite correctness, and no independent mathematical audit is asserted.

## References

1. N. F. Beike, R. Carleton, D. G. Costanzo, C. Heath, M. L. Lewis, K. Lu, and J. D. Pearce, *\(p\)-groups with cyclic or generalised quaternion Hughes subgroups: classifying tidy \(p\)-groups*, Bulletin of the Australian Mathematical Society 108 (2023), 443–448. First public online 2023-04-20. https://doi.org/10.1017/S000497272300031X
2. J. Flake and A. Thevis, *Strata of \(p\)-Origamis*, arXiv:2003.13297, first publicly posted 2020-03-30; subsequently Mathematische Nachrichten 296 (2023), 1087–1116. https://arxiv.org/abs/2003.13297
3. P. Puusemp, *A characterization of the semidirect product of cyclic groups by its endomorphism semigroup*, Proceedings of the Estonian Academy of Sciences, Physics, Mathematics 45 (1996), 134–144. https://doi.org/10.3176/phys.math.1996.2/3.03
4. P. Puusemp, *On the definability of a semidirect product of cyclic groups by its endomorphism semigroup*, Algebras, Groups and Geometries 19 (2002), 195–212. Abstract-level comparison only; full text not verified. https://www.researchgate.net/publication/267430404_On_the_definability_of_a_semidirect_product_of_cyclic_groups_by_its_endomorphism_semigroup
5. P. Puusemp, *Non-Abelian Groups of Order 16 and Their Endomorphism Semigroups*, Journal of Mathematical Sciences 131 (2005), 6098–6111. Abstract-level comparison only. https://doi.org/10.1007/s10958-005-0463-x
6. P. Puusemp, *Groups of Order Less Than 32 and Their Endomorphism Semigroups*, Journal of Nonlinear Mathematical Physics 13 (2006), 93–101. https://doi.org/10.2991/jnmp.2006.13.s.11
