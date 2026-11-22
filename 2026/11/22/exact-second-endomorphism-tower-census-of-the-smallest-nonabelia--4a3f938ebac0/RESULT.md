# Exact second endomorphism tower census of the smallest nonabelian symmetric group

## Finding

Let \(G=S_3\). Write \(E_1=\operatorname{End}(G)\), the monoid of all semigroup endomorphisms under composition, and \(E_2=\operatorname{End}(E_1)\). Endomorphisms here need **not** preserve the identity of a monoid. Then
\[
|E_1|=10,\qquad |E_2|=43,
\]
and the complete image-rank polynomial of the second tower is
\[
\boxed{\sum_{f\in E_2} z^{|f(E_1)|}=5z+14z^2+9z^3+3z^4+6z^7+6z^{10}.}
\]
In particular, \(E_2\) has exactly six automorphisms, and there are no endomorphisms of ranks five, six, eight or nine. Of the 43 semigroup endomorphisms, exactly 33 preserve the identity of \(E_1\).

## Assumptions and scope

A semigroup endomorphism is a multiplication-preserving map, with no requirement to send identity to identity. For a group, such a map automatically preserves the identity; for the monoid \(E_1\), this need not hold. The theorem is specific to \(S_3\), the smallest nonabelian symmetric group, and concerns the complete second tower, not higher levels or arbitrary \(S_n\).

## Proof

**First level.** The normal subgroups of \(S_3\) are \(1\), \(A_3\) and \(S_3\). Every endomorphism of \(S_3\) is therefore one of: six automorphisms; three sign maps \(t_s\) taking every odd permutation to a specified transposition \(s\) and every even permutation to the identity; or the trivial homomorphism \(0\). Their composition monoid has ten elements. Its six units \(U\cong S_3\), three nonzero singular idempotents \(T=\{t_s\}\), and absorbing zero \(0\) obey, for \(u\in U\),
\[
t_s t_t=t_s,\qquad t_su=t_s,\qquad ut_s=t_{u(s)},\qquad 0x=x0=0.
\]
The identity is the identity automorphism in \(U\). The idempotents are exactly these five elements: \(0\), the identity and the three \(t_s\).

**Identity-preserving second-level maps.** If \(F:E_1\to E_1\) is a semigroup endomorphism with \(F(1)=1\), its restriction \(\alpha\) to \(U\) is a group endomorphism, with exactly ten possibilities. Its four remaining values \(F(0)\) and \(F(t_s)\) must be idempotents, leaving only \(10\cdot5^4=6250\) candidate assignments. Each candidate is checked against the exact ten-element multiplication, using all \(100\) ordered pairs. This exhaustive test finds \(33\) valid maps, with image ranks \(1,2,3,4,7,10\) and multiplicities \(1,8,9,3,6,6\), respectively. `CHECKER.py` constructs the first-level monoid from permutation maps and independently reproduces these finite counts.

**Nonidentity-preserving maps.** For an arbitrary \(F\), the element \(d=F(1)\) is idempotent and acts as a two-sided identity on \(F(E_1)\). If \(d=0\), the only possibility is the constant zero map. If \(d=t_s\), the submonoid on which \(d\) acts as identity is exactly \(\{0,t_s\}\), with \(t_s\) acting as its identity. The six units must all map to \(t_s\). Left-zero multiplication and the transitive action of \(U\) on the three \(t_r\) force their images to agree. If their common value is \(t_s\), \(F(0)\) can be \(0\) or \(t_s\); if it is \(0\), then \(F(0)=0\). Thus there are exactly three such maps for each of the three choices of \(s\): three constant maps of image rank one, and six rank-two maps in all. Including the constant-zero map yields exactly ten nonidentity-preserving maps. Combining their rank distribution with the 33 identity-preserving maps proves the formula.

## Verification

Run `python3 CHECKER.py` using the Python 3 standard library. The program enumerates all maps on the six permutations respecting the group multiplication, reconstructs \(E_1\), checks its idempotents, units, identities, its full multiplication and all \(6250\) identity-preserving candidates, and then exhausts the nonidentity-preserving cases as well. Its final marker is `S3_SECOND_ENDOMORPHISM_TOWER_43_OK`. These are exhaustive finite checks, not evidence for unexamined higher ranks or group degrees.

## Relationship to prior work

Gould, Grau, Johnson and Smith, *The endomorphism tower of a finite symmetric group* (arXiv:2606.24274, publicly posted June 23, 2026), classify the second tower for \(S_n\) with \(n\ge7\), excluding the exceptional small degrees. The exact degree-three 43-element census and its image-rank polynomial are outside their stated range. An earlier published analysis of proper-unit-image retractions for degrees \(n\ge7\) likewise cannot yield this case by specialization. Searches of accessible publications and indexed findings did not identify a covering \(S_3\) rank census; historical priority outside those sources is unresolved.

## Limitations

The result is a complete finite classification for \(S_3\), not an extension of the higher-degree formulas in the motivating paper and not a theorem for all small symmetric groups. The proof uses a finite exhaustive table computation in one step, justified by a complete enumeration of the relevant finite candidate space. No independent mathematical audit has been performed.

## References

1. Victoria Gould, Ambroise Grau, Marianne Johnson and Jamie Smith, *The endomorphism tower of a finite symmetric group*, arXiv:2606.24274 (first public June 23, 2026), https://arxiv.org/abs/2606.24274 .
2. V. Gould, A. Grau, M. Johnson and M. Kambites, *Translational hulls of semigroups of endomorphisms of an algebra*, arXiv:2404.14005, https://arxiv.org/abs/2404.14005 .
