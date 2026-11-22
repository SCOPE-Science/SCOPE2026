# Associator-value laws of \(M(G,2)\) and group commutator fibers

## Finding

Let \(G\) be any finite group of order \(m\), and let \(M=M(G,2)\) be the classical Chein loop with an involutory outside coset. For \(w\in G\), put
\[
C_G(w)=\#\{(a,b)\in G^2:a^{-1}b^{-1}ab=w\}.
\]
Define the (left-inverse convention) associator of elements of \(M\) by
\[
\alpha(x,y,z)=((xy)z)^{-1}(x(yz)).
\]
It always belongs to \(G\), and its complete fiber law is
\[
\boxed{N_G(w)=\#\{(x,y,z)\in M^3:\alpha(x,y,z)=w\}=m^3\mathbf1_{w=1}+7mC_G(w).}
\]
Equivalently, for three independent uniform elements of \(M\), the associator-value distribution is \(\frac18\delta_1+\frac78\mu_G\), where \(\mu_G\) is the distribution of the commutator \(a^{-1}b^{-1}ab\) of independent uniform group elements. In particular the complete group commutator distribution is recovered from associator fibers, even when the association probability alone cannot distinguish nonidentity fibers.

For odd \(n\ge3\) and the dihedral group \(D_{2n}=\langle r,s:r^n=s^2=1,\ srs=r^{-1}\rangle\), this becomes
\[
N_G(1)=22n^3+42n^2,\quad N_G(r^j)=42n^2\ (1\le j<n),\quad N_G(sr^j)=0\ (0\le j<n).
\]
These are *value-specific* fibers, not just the previously known total count of associating triples.

## Assumptions and scope

The group \(G\) is finite but otherwise unrestricted, including nonabelian groups of arbitrary exponent. The multiplication on the disjoint union \(M=G\sqcup Gu\) is explicitly
\[
g\cdot h=gh,\qquad g\cdot(hu)=(hg)u,\qquad (gu)\cdot h=(gh^{-1})u,\qquad (gu)\cdot(hu)=h^{-1}g.
\]
Hence \(u^2=1\). No variant with a nonidentity central twisting element is included. The group commutator convention is \([a,b]=a^{-1}b^{-1}ab\). Every count concerns ordered triples, with repeats allowed; each \(w\) labels an actual element of \(G\), not a conjugacy class.

## Proof

Let \(g,h,k\in G\). Divide \(M^3\) into eight disjoint coset patterns according to whether each position is in \(G\) or in \(Gu\). Since both bracketings have the same coset parity, their quotient \(\alpha\) is always an element of \(G\). Direct multiplication with the displayed four Chein rules gives the following exhaustive associator-value identities, with pattern \(0\) denoting \(G\) and \(1\) denoting \(Gu\):

| Pattern | Associator value |
|:---:|:---|
| 000 | \(1\) |
| 001 | \([g,h]\) |
| 010 | \([g,k^{-1}]\) |
| 011 | \([g,k^{-1}h]\) |
| 100 | \([h^{-1},k^{-1}]\) |
| 101 | \([h^{-1},k^{-1}g]\) |
| 110 | \([k,h^{-1}g]\) |
| 111 | \(h^{-1}[kh^{-1},gh^{-1}]h\) |

Every pattern other than 000 gives \(m\) independent choices of a third free group variable and a bijective change of variables from the other two group variables to an ordered pair \((a,b)\). Thus each of the first six nontrivial rows contributes \(mC_G(w)\) triples to the fiber at \(w\). For pattern 111, the change of variables \((g,h,k)\leftrightarrow(kh^{-1},gh^{-1},h)\) is bijective. The commutator fiber \(C_G(w)\) is constant under conjugating \(w\): conjugate both input variables by the same group element. Consequently the 111 row also contributes \(mC_G(w)\) for every \(w\). Pattern 000 contributes \(m^3\) to the identity fiber only. Summing proves the boxed equation, its normalization, and recovery of \(C_G\).

For \(G=D_{2n}\) with odd \(n\), each commutator is a rotation. The rotation–rotation ordered pairs, of which there are \(n^2\), commute. For each prescribed rotation, reflection–reflection pairs contribute exactly \(n\) commutators: the commutator exponent is twice a difference of their rotation labels, and multiplication by two permutes \(\mathbb Z/n\mathbb Z\). Rotation–reflection and reflection–rotation pairs each contribute exactly \(n\) occurrences of a prescribed rotation, because their commutator exponents are twice a rotation label. Therefore \(C_G(1)=n^2+3n\), \(C_G(r^j)=3n\) for \(1\le j<n\), and \(C_G(sr^j)=0\). Substitution with \(m=2n\) proves the three claimed fiber values.

## Verification

The independent standalone script `verify_associators.py` builds the group law of symmetric groups on three and four letters and dihedral groups of orders eight and ten. It directly enumerates all group commutators and all Chein loop associators, then compares each individual fiber with the formula. This includes noncentral and nonidentity output classes, not just the number of trivial associators. It independently checks the dihedral closed form for odd cycle lengths three and five. Running `python verify_associators.py` terminates with `CHEIN_ASSOCIATOR_FIBERS_VERIFIED` upon success. The infinite assertion follows from the exhaustive eight-pattern symbolic proof, not from finite enumeration.

## Relationship to prior work

Chein's classical construction and its four multiplication rules are established and not claimed new. Britten's 2022 paper studies power graphs and discusses Chein-type loop constructions; its power-graph results are not a full associator-value census. Bashir and Ahmadidelir (2020) determine the binary noncommuting graph of dihedral Chein loops, including a precise decomposition for odd dihedral parameters; this graph does not encode ternary associator values. Ahmadidelir's *Associativity Degree in Finite Moufang Loops* (Będlewo 2015 lecture) already proves exactly \(\operatorname{Pas}(M(G,2))=\frac18+\frac78\operatorname{Pr}(G)\), the **identity fiber** obtained from the boxed theorem. That earlier probability and its \(43/64\) bound are **not** claimed as new. Levin (2025) proves a more general upper bound on association probability under a nuclear-commutator hypothesis but not prescribed associator-output fibers. The present claim is the complete elementwise associator law, including nonidentity fibers and inversion of the group commutator-word distribution, together with its uniform dihedral evaluation. Elementary group commutator character formulas may be substituted into this law, but they are not claimed new.

## Limitations

The result does not apply to all central-twisted variants of the Chein construction, nor to arbitrary Moufang loops. Having the associator distribution need not recover the group up to isomorphism: it recovers its commutator-word distribution only. Published scalar association formulas are strictly weaker data, yet an unindexed full-fiber equivalent could still affect publication priority. No independent mathematical audit has been performed.

## References

1. Riley Britten, *Power graphs of Moufang loops*, arXiv:2204.07165v1, first posted 2022-04-13, https://arxiv.org/abs/2204.07165 (motivation and Chein-loop context).
2. Hamideh Hasanzadeh Bashir and Karim Ahmadidelir, *Some structural graph properties of the non-commuting graph of a class of finite Moufang loops*, Electronic Journal of Graph Theory and Applications 8 (2020), 319–337, DOI:10.5614/ejgta.2020.8.2.9 (classical multiplication, binary graph; not the ternary fibers).
3. Karim Ahmadidelir, *Associativity Degree in Finite Moufang Loops*, Groups and Their Actions, Będlewo 22–26 June 2015, https://mat.polsl.pl/groups/talks/Ahmadidelir.pdf (the already known identity-fiber probability formula).
4. Ilan Levin, *How Associative Can a Non-Associative Moufang Loop Be?*, arXiv:2501.02294, first posted 2025-01-04 (general upper bounds for association probability).
5. Orin Chein and Edgar G. Goodaire, *Bol loops with a large left nucleus*, Comment. Math. Univ. Carolin. 49 (2008), 171–196, https://dml.cz/dmlcz/119714 (general loop associator background, different nucleus assumptions).
