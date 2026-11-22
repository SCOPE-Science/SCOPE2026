# Full unit-conjugacy orbit-size spectrum of finite cycle-graph endomorphisms

## Finding

Let \(C_n\) be the undirected, loopless graph with vertex set \(\mathbb Z/n\mathbb Z\) and edges \(\{i,i+1\}\), where \(n\ge4\). Let \(M_n=\operatorname{End}(C_n)\) be its monoid of adjacency-preserving total maps. The dihedral unit group \(D_n=\operatorname{Aut}(C_n)\), of order \(2n\), acts on \(M_n\) by **composition conjugation** \(f\mapsto ufu^{-1}\). Let \(\mathscr P_n(y)=\sum_{\mathcal O}y^{|\mathcal O|}\), summing over all \(D_n\)-conjugacy orbits in \(M_n\); thus coefficients count orbits, not labeled maps.

For **odd** \(n\ge5\),
\[
\boxed{\mathscr P_n(y)=y+\frac{n-1}{2}y^2+y^n.}
\]
For **even** \(n=2m\ge4\), put
\[
 B_m=\binom{2m}{m},\qquad
 H_m=\begin{cases}
 \binom{m}{m/2},&m\text{ even},\\
 \binom{m-1}{(m-1)/2},&m\text{ odd}.
 \end{cases}
\]
Then the complete orbit-size polynomial is
\[
\boxed{\mathscr P_{2m}(y)=2y+(m-1)y^2+2y^m+2H_my^{2m}+\left(\frac{B_m}{2}-H_m\right)y^{4m}.}
\]
Terms with equal exponents are to be combined; for example, at \(m=2\) the \(y^2\) terms coincide. In particular, precisely \(2H_m\) conjugacy classes of **nonautomorphisms** have size \(n\), and precisely \(B_m/2-H_m\) have size \(2n\). There are no other nonautomorphism orbit sizes. The complete class number is
\[
\boxed{K_{2m}=\mathscr P_{2m}(1)=\frac12\left(\binom{2m}{m}+2m+6+2H_m\right).}
\]
A uniformly chosen nonautomorphism has a nontrivial dihedral stabilizer with exact probability \(2H_m/B_m=O(2^{-m})\); consequently, \(K_{2m}\sim \frac12\binom{2m}{m}\sim4^m/(2\sqrt{\pi m})\).

The theorem also computes **centralizers of every unit inside the entire endomorphism monoid**. Write \(r^k(i)=i+k\) and \(h_c(i)=c-i\), \(0\le k,c<n\). When \(n=2m\),
\[
|C_{M_n}(r^k)|=\begin{cases}
 n(B_m+2),&k=0,\\
 2n,&k=m,\\
 n,&\text{otherwise},
 \end{cases}
\]
and reflection centralizers depend on the parity of \(c\):
\[
\begin{aligned}
 |C_{M_n}(h_c)|&=4+2H_m &&(m\text{ even, every }c),\\
 |C_{M_n}(h_c)|&=4 &&(m\text{ odd},\ c\text{ even}),\\
 |C_{M_n}(h_c)|&=4+4H_m &&(m\text{ odd},\ c\text{ odd}).
\end{aligned}
\]
For odd \(n\), all endomorphisms are units; their centralizers are the ordinary dihedral centralizers: \(2n\) for the identity, \(n\) for nonidentity rotations, and \(2\) for reflections.

## Assumptions and scope

We use *strict* graph endomorphisms: adjacent vertices must map to adjacent **distinct** vertices, without loops or edge collapse. Composition is ordinary function composition. An orbit is defined by simultaneous change of source and target coordinates using the **same** unit and its inverse, not by independent left and right multiplication; the latter defines a coarser double-coset equivalence. The parameter \(n\) is an integer at least four; no regularity or idempotence condition is imposed on an endomorphism. The formulas count all noninvertible maps, not merely retractions.

## Proof

**1. Walk normal form.** Each \(f\in M_n\) is uniquely determined by \(a=f(0)\in\mathbb Z/n\mathbb Z\) and steps \(\varepsilon_i\in\{-1,+1\}\) satisfying
\[
 f(i+1)=f(i)+\varepsilon_i\pmod n,
 \qquad \sum_{i=0}^{n-1}\varepsilon_i\equiv0\pmod n.
\]
Uniqueness of each signed step holds because \(n\ge4\). Since the integer sum has absolute value at most \(n\), it is either \(-n,0,n\). The extreme cases force all steps equal and produce exactly the \(2n\) dihedral units. The zero sum occurs only when \(n=2m\), with exactly \(m\) positive and \(m\) negative steps. It gives exactly \(nB_m\) nonautomorphisms. Indeed, a balanced walk has a change of sign, hence repeats a vertex at distance two and cannot be bijective.

**2. No nonunit commutes with a nonidentity rotation.** If \(fr^k=r^kf\), then
\(f(i+k)=f(i)+k\pmod n\). Taking differences gives \(\varepsilon_{i+k}=\varepsilon_i\). With \(d=\gcd(n,k)\), the steps have period \(d\). For a balanced walk, this means \((n/d)\sum_{j=0}^{d-1}\varepsilon_j=0\) as an **integer**, hence the sum over one period is zero. Consequently \(f(i+d)=f(i)\) and thus \(f(i+k)=f(i)\), contradicting \(k\not\equiv0\pmod n\). For units, the usual dihedral relation shows that all rotations commute with \(r^k\), while a reflection commutes if and only if \(2k\equiv0\pmod n\). This proves the rotation-centralizer formula.

**3. Reflection-fixed walks.** A map commutes with \(h_c\) precisely when
\[
 f(c-i)=c-f(i),\qquad
 \varepsilon_{c-1-i}=\varepsilon_i
 \quad (i\in\mathbb Z/n\mathbb Z),
\]
where, conversely, the step equation together with the equation at \(i=0\) implies all the others. For \(c=0\), the step reflection \(i\mapsto-1-i\) has \(m\) disjoint pairs. A balanced step word exists only if \(m\) is even, with exactly \(\binom{m}{m/2}=H_m\) choices. Its initial value satisfies \(2a=0\pmod{2m}\), giving two choices. Thus there are \(2H_m\) singular maps commuting with an even-axis reflection if \(m\) is even and zero if \(m\) is odd. Every even \(c\) is conjugate to \(c=0\) by a rotation.

For \(c=1\), the step involution \(i\mapsto-i\) fixes edges \(0,m\) and has \(m-1\) pairs. Write the sum of paired signs as \(T\), so the full step sum is \(\varepsilon_0+\varepsilon_m+2T\). If \(m\) is even, the \(m-1\) pairs give odd \(T\); balance forces \(T=\pm1\) and both fixed signs to equal \(-T\). There are \(2\binom{m-1}{m/2}=H_m\) balanced step words. If \(m\) is odd, the pairs give even \(T\); balance forces \(T=0\) and opposite fixed signs. There are \(2\binom{m-1}{(m-1)/2}=2H_m\) balanced step words. The initial condition \(2a+\varepsilon_0\equiv1\pmod{2m}\) has exactly two solutions in either case. Thus there are respectively \(2H_m\) and \(4H_m\) singular endomorphisms commuting with an odd-axis reflection. Every odd \(c\) is conjugate to \(c=1\). Each reflection also centralizes exactly four dihedral units, giving the stated full centralizers.

**4. Orbit-size census.** The product of two distinct reflections is a nonidentity rotation. Step 2 therefore implies that a nonautomorphism is stabilized by **at most one** reflection, and has stabilizer order either one or two. As there are \(m\) even-axis and \(m\) odd-axis reflections, Step 3 shows that the total number of pairs \((f,h)\), with \(f\) singular and \(h\) a reflection fixing \(f\), is \(2nH_m\), in both parity cases. No singular \(f\) is counted twice. Exactly \(2nH_m\) singular maps consequently have stabilizer order two and conjugacy orbit size \(n\), yielding \(2H_m\) such orbits. The remaining \(nB_m-2nH_m\) singular maps have trivial stabilizer and orbit size \(2n\), yielding \(B_m/2-H_m\) orbits. The dihedral units themselves form two singleton conjugacy classes, \(m-1\) rotation classes of size two, and two reflection classes of size \(m\). Combining them gives \(\mathscr P_{2m}\). For odd \(n\), every endomorphism is a unit, and the ordinary odd-dihedral conjugacy classes give \(\mathscr P_n\).

**5. Asymptotics.** The binomial estimate \(\binom{2m}{m}\sim4^m/\sqrt{\pi m}\) holds. In either parity, \(H_m=O(2^m/\sqrt m)\), hence \(2H_m/B_m=O(2^{-m})\), and the formula for \(K_{2m}\) yields the stated asymptotic.

## Verification

The standalone Python program `check_cycle_units.py` uses exact integer arithmetic and enumerates all signed closed-walk maps for \(n=4,6,8,10,12\). It computes **each individual centralizer by direct composition tests**, compares against both reflection parity types, and checks Burnside's identity. For \(n=4,6,8,10\) it constructs actual conjugacy orbits and compares the singular orbit-size histogram to the closed formula. For \(n=4,6\), a second enumeration over all \(n^n\) maps checks that the signed-walk encoding has omitted none. Odd-cycle dihedral orbit histograms are directly checked at \(n=5,7,9,11\). The computed all-orbit counts at even lengths \(4,6,8,10,12\) are respectively \(10,18,48,140,491\). Execution prints `CYCLE_ENDOMORPHISM_UNIT_COMMUTANT_CHECKS_PASSED`. These experiments corroborate, but are not substitutes for, the all-parameter proof in Steps 1–5.

## Relationship to prior work

Dimitrova, Fernandes, Koppitz and Quinteiro (first publicly posted 6 October 2023) establish the full cycle-graph endomorphism monoid, its elements, Green relations, generating sets, and labeled counts. Their Section 3 explicitly uses an equivalence \(f=u g v\) with **independently chosen** units \(u,v\); this is not conjugation by a single unit and cannot determine the orbit-size spectrum asserted here. Their labeled total \(n(B_m+2)\) is used, not claimed as new. The published exact rank profile of **all labeled** cycle endomorphisms is likewise coarser with respect to symmetry and does not imply an orbit-size distribution. Previously established unit-conjugacy orbit counts for **idempotent** cycle endomorphisms concern only a proper subset of the maps treated here; this theorem does not claim that idempotent subcase as new.

Michels and Knauer's 2009 work counts endomorphisms and their induced **kernel congruence classes**; kernel partitions are neither composition-conjugacy classes nor an obvious mechanism for recovering the present orbit stabilizers. Its full text was not accessible for a conclusive historical exclusion. The distinction between equivalences is mathematical rather than terminological. The new object determined is the full ambient **conjugacy-orbit size distribution**, not the already known labeled endomorphism count, an image-rank distribution, or a two-sided action quotient. Burnside's lemma and central binomial asymptotics are standard ingredients and not claimed as original.

## Limitations

Only ordinary strict graph endomorphisms of simple cycles of length at least four are covered. Weak endomorphisms, arbitrary source/target cycles, and complete image-rank refinement of the orbit polynomial are not covered. Historical priority is conditional on the inspected public record; the full 2009 Michels–Knauer article was inaccessible despite bounded searches for public full text. No independent mathematical audit has been performed.

## References

1. I. Dimitrova, V. H. Fernandes, J. Koppitz, and T. M. Quinteiro, *On monoids of endomorphisms of a cycle graph*, arXiv:2310.04149v1, first posted 6 October 2023, https://arxiv.org/abs/2310.04149 . Full preprint inspected, especially Proposition 1.9, Sections 2–3, and the distinct two-sided unit equivalence in Section 3.
2. M. A. Michels and U. Knauer, *The congruence classes of paths and cycles*, *Discrete Mathematics* 309 (2009), 5352–5359, DOI:10.1016/j.disc.2008.11.022, https://doi.org/10.1016/j.disc.2008.11.022 . Abstract and bibliographic data consulted; full text not inspected.
3. *Exact image-rank profile and mean of endomorphism monoids of finite cycles*, publicly available result, 26 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-image-rank-profile-and-mean-of-endomorphism-monoids-of-fin--a0fa99757b61 . Complete RESULT.md inspected for implication comparison.
4. OEIS A112850, *Number of graph endomorphisms of undirected cycles of even length*, https://oeis.org/A112850 ; OEIS A112849, *Congruence classes induced by graph endomorphisms of undirected cycles*, https://oeis.org/A112849 . These are existing aggregate sequences, not the present orbit sequence.
