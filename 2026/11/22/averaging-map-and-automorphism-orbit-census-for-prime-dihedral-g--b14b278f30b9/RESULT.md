# Averaging-map and automorphism-orbit census for prime dihedral groups

## Finding

Let \(p\ge3\) be an odd prime and \(G=D_{2p}=\langle r,s\mid r^p=s^2=1,\;srs=r^{-1}\rangle\). An averaging map in the sense of Das is an arbitrary set map \(A:G\to G\) satisfying
\[
A(g)A(h)A(g)^{-1}=A\!\left(A(g)hA(g)^{-1}\right)\quad(g,h\in G).
\]
It is *pointed* when \(A(1)=1\). Two maps are equivalent when they are conjugate under \(\operatorname{Aut}(G)\), acting by \((\phi\cdot A)(x)=\phi(A(\phi^{-1}x))\).

Put \(m=(p-1)/2\), define the necklace polynomial
\[
\mathcal N_m(k)=\frac1m\sum_{d\mid m}\varphi(d)k^{m/d},
\]
and put
\[
U_p=\sum_{\substack{d\mid p-1\\d>1}}\varphi(d)p^{(p-1)/d}.
\]
Then the exact number of averaging maps, pointed averaging maps, automorphism-equivalence classes of all averaging maps, and automorphism-equivalence classes of pointed averaging maps are respectively
\[
\boxed{\begin{aligned}
A_p&=p^{p+1}+p(2^{p+1}-1)+p^m,\\
A_p^{\mathrm{pt}}&=p^p+p(2^p-1)+p^m,\\
O_p&=4\mathcal N_m(4)+\frac{p^{p+1}+U_p}{p-1}+\mathcal N_m(p)-1,\\
O_p^{\mathrm{pt}}&=2\mathcal N_m(4)+\frac{p^p+U_p}{p-1}+\mathcal N_m(p)-1.
\end{aligned}}
\]
The four generated-image subgroup strata have counts
\[
\begin{array}{c|cccc}
\langle A(G)\rangle&1&\langle r\rangle&\langle r^is\rangle\;(\text{each }i)&G\\\hline
\text{all maps}&1&p^{p+1}-1&2^{p+1}-1&p^m\\
\text{pointed}&1&p^p-1&2^p-1&p^m.
\end{array}
\]
For \(p=3\), the formulas reproduce \((129,51,60,25)\), previously published for \(S_3\cong D_6\). For \(p=5\), they yield \((15965,3305,3969,824)\).

## Assumptions and scope

The prime restriction is essential to this classification: the subgroup lattice used below has only the trivial group, the unique order-\(p\) rotation subgroup, \(p\) order-two reflection subgroups, and the whole group. Counts are of **all set maps**, not merely homomorphisms or retractions. The notion of averaging map is Das's conjugation identity, not the stronger associative-looking identity also called group averaging in later literature. The automorphism-equivalence quotient uses the full group automorphism group, of order \(p(p-1)\), not only inner automorphisms. Euler's \(\varphi\) is the usual totient, including \(\varphi(1)=1\). Empty products or sums have their standard interpretations.

## Proof

**1. Equivariance lemma.** Let \(H=\langle A(G)\rangle\). The defining identity says that \(A\) commutes with conjugation by each element of \(A(G)\). Conjugation maps form a group, so it commutes with conjugation by every element of \(H\). Conversely, this equivariance implies the defining identity. Thus the averaging maps whose image generates \(H\) are exactly the \(H\)-equivariant maps \(G\to H\) whose values generate \(H\). This general lemma is established in the published \(S_3\) census and is not claimed as new here.

**2. Generated-image subgroup counts.** For \(H=1\), there is one map. For \(H=R=\langle r\rangle\), conjugation by \(R\) fixes each of the \(p\) rotations and acts transitively on the \(p\) reflections; its action on the target \(R\) is trivial. Thus an equivariant map is an arbitrary \(p\)-valued function on \(p+1\) orbits. The only one not generating the prime-order group \(R\) is the identity-valued map. Hence \(p^{p+1}-1\) maps, or \(p^p-1\) when pointed.

For each \(H=\langle t\rangle\cong C_2\), with \(t\) a reflection, conjugation by \(t\) has \(p+1\) orbits: the fixed singleton sets \(\{1\}\) and \(\{t\}\), and \(m\) two-element pairs of nonidentity rotations and \(m\) two-element pairs of other reflections. Target conjugation is trivial, so equivariant maps are binary choices on these orbits. Removing the constant identity map leaves \(2^{p+1}-1\), or \(2^p-1\) when pointed. There are \(p\) distinct such subgroups.

For \(H=G\), a fully conjugation-equivariant map sends identity to the center \(Z(G)=1\). It sends \(s\) to its centralizer \(C_G(s)=\{1,s\}\); to generate \(G\), this value must be \(s\), forcing every reflection to itself. On rotations, the value of \(r^j\) must be a rotation \(r^{f(j)}\) with \(f(-j)=-f(j)\) and \(f(0)=0\). One value for each of the \(m\) opposite pairs is arbitrary in \(\mathbb F_p\), giving \(p^m\) maps, all pointed. Summing gives the first two boxed formulas.

**3. Aut-equivalence on the reflection subgroup stratum.** Every group automorphism is \(r\mapsto r^u,\;s\mapsto r^vs\) with \(u\in\mathbb F_p^\times,\;v\in\mathbb F_p\). All reflection subgroups are conjugate under automorphisms. Fix one, say \(\langle s\rangle\). Its stabilizer acts through the multiplier \(u\in\mathbb F_p^\times\). The multiplier \(-1\) is conjugation by \(s\), and already fixes any \(\langle s\rangle\)-equivariant map. Thus the effective stabilizer is cyclic of size \(m\), simultaneously cycling the \(m\) opposite pairs of rotations and the \(m\) opposite pairs of reflections. Their two output bits combine into one of four colors per pair; the two singleton orbits supply four independent choices, or two choices if pointed. Burnside's lemma yields \(4\mathcal N_m(4)\), respectively \(2\mathcal N_m(4)\), orbits of equivariant maps to this subgroup. Removing the one identity-valued map gives \(4\mathcal N_m(4)-1\) and \(2\mathcal N_m(4)-1\) classes in the generated-image reflection stratum.

**4. Aut-equivalence on the rotation subgroup stratum.** A rotation-subgroup-valued equivariant map is specified by \(f:\mathbb F_p\to\mathbb F_p\) and a scalar \(c\in\mathbb F_p\): \(A(r^j)=r^{f(j)}\) and \(A(r^js)=r^c\). The translation parameter \(v\) of an automorphism acts trivially on this specification; the multiplier \(u\) acts by \(f(j)\mapsto u f(u^{-1}j)\) and \(c\mapsto uc\). For \(u=1\), the fixed-point counts are \(p^{p+1}\) (all) and \(p^p\) (pointed, where \(f(0)=0\)). If \(u\ne1\) has multiplicative order \(d\), fixedness forces \(f(0)=c=0\), while one value can be chosen freely for each of the \((p-1)/d\) nonzero multiplier cycles, giving \(p^{(p-1)/d}\) fixed maps. There are \(\varphi(d)\) multipliers of order \(d\). Burnside therefore gives \((p^{p+1}+U_p)/(p-1)\), or \((p^p+U_p)/(p-1)\), orbit classes before removing the identity-valued map. Subtract one in either case.

**5. Aut-equivalence on the whole-group stratum.** In the fully equivariant maps of step 2, all inner automorphisms act trivially. The multiplier \(-1\) is inner, so the effective quotient on the \(m\) free rotation-pair values is \(\mathbb F_p^\times/\{\pm1\}\cong C_m\). The quotient permutes these \(m\) values cyclically, while the compatible signed action on the values is conjugate, by a coordinate change, to ordinary coordinate permutation. Explicitly fix representatives of the \(m\) pairs as powers \(\gamma^j\) of a primitive root \(\gamma\), with \(j=0,\ldots,m-1\), and rescale \(f(\gamma^j)\) by \(\gamma^{-j}\). Then a multiplier generator acts by cyclic shift of the rescaled coordinates (including the wraparound sign, canceled by the oddness of \(f\)). Consequently an element of order \(d\mid m\) fixes \(p^{m/d}\) maps. Burnside gives \(\mathcal N_m(p)\) classes, all pointed. Adding the trivial class, the three nontrivial strata from steps 3–5, proves both orbit formulas.

## Verification

The independent executable `artifacts/verify.py` uses explicit coordinates for \(D_{2p}\) and constructs *every* subgroup-equivariant map for each generated-image stratum without relying on the closed totals. It checks the averaging identity directly for each constructed map and every ordered pair of group elements, verifies distinctness of the maps, constructs the full \(\operatorname{Aut}(G)\) action and independently counts its orbits. On \(p=3\) it yields \((129,51,60,25)\); on \(p=5\) it yields \((15965,3305,3969,824)\). The final marker is `PRIME_DIHEDRAL_AVERAGING_VERIFIED`. The proof for all odd primes is mathematical; these finite checks are corroboration, not an exhaustive check over all primes.

## Relationship to prior work

Das (2024) introduced the conjugation-based group averaging identity and related it to racks; his Section 2 was inspected for the exact definition and group examples. The published \(S_3\) averaging-map census already proves the general subgroup-equivariance lemma and counts \(129\) maps, \(51\) pointed maps, \(60\) automorphism classes and \(25\) pointed automorphism classes for \(p=3\). Its full result was inspected and no general prime-dihedral formula was stated. Those earlier results are not claimed as new. The present claims are the all-odd-prime formulas, particularly the arithmetic necklace-polynomial orbit counts. Zhang–Gao (2024/2025) define a stronger different group averaging identity; its results cannot be substituted for this definition.

## Limitations

Nothing is claimed for composite rotation order, other finite groups, or the stronger Zhang–Gao identity. This is self-review, not independent peer validation. The literature and database search did not locate these four prime-dihedral formulas, but incomplete indexing or a broader older enumeration could establish them implicitly; the conclusion of original contribution is qualified by that residual priority risk.

## References

1. A. Das, *Averaging operators on groups, racks and Leibniz algebras*, arXiv:2403.06250v1, first public 2024-03-10, https://arxiv.org/abs/2403.06250.
2. *The symmetric group \(S_3\) has \(129\) averaging maps and \(51\) pointed ones*, publicly available published-finding corpus mathematics record (2026-10-12), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-the-symmetric-group-s-3-has-129-averaging-maps-and-51-pointed-on--3cc43f08406b.
3. H. Zhang and X. Gao, *Averaging operators on groups and Hopf algebras*, arXiv:2412.11600, first public 2024-12-16, https://arxiv.org/abs/2412.11600 (different operator identity).
