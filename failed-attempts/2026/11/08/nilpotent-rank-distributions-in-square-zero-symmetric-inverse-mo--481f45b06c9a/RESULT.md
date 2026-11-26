# Nilpotent rank distributions in square-zero symmetric inverse monoid centralizers

## Finding
Let \(\mathcal I_n\) be the symmetric inverse monoid of partial injections on a labeled \(n\)-element set, including the empty map. Fix any \(f\in\mathcal I_n\) with \(f^2=\varnothing\) and rank \(r\); write \(s=n-2r\). For \(m\ge0\) put
\[
P_m(t)=\sum_{j=0}^{m}\binom mj^2j!t^j,\qquad P_{-1}(t)=0.
\]
Define the rank enumerators of the centralizer and its nilpotent elements:
\[
C_{r,s}(t)=\sum_{g f=f g}t^{\operatorname{rk}g},\qquad
N_{r,s}(t)=\sum_{\substack{g f=f g\\g\text{ nilpotent}}}t^{\operatorname{rk}g}.
\]
**Theorem.** For every \(r,s\ge0\) with \(2r+s=n\ge1\),
\[
\boxed{C_{r,s}(t)=\sum_{k=0}^{r}\binom rk^2k!\,t^{2k}P_{r-k+s}(t).}
\]
For \(r\ge1\), set \(a_{r,k}=\binom rk\binom{r-1}k k!\) (understanding \(\binom{r-1}r=0\)). For \(r=0\), set \(a_{0,0}=1\). Then
\[
\boxed{N_{r,s}(t)=\sum_{k=0}^{r}a_{r,k}\,t^{2k}
\bigl(P_{r-k+s}(t)-s t P_{r-k+s-1}(t)\bigr).}
\]
Thus both complete rank distributions depend only on the pair \((r,s)\), not on the particular square-zero partial injection. In particular, for \(r\ge1\), the coefficient of \(t^{n-1}\) in \(N_{r,s}(t)\) is \(r!s!\), equal to the number of full-rank elements of the centralizer. For \(r=0\), the coefficient is \(s!\), the classical count of maximal-rank nilpotent partial injections. This is a rank-enumeration refinement of established structural centralizer descriptions, not a new characterization of which maps commute.

For illustration, if \((r,s)=(2,2)\), then
\[
C_{2,2}(t)=1+16t+76t^2+132t^3+98t^4+32t^5+4t^6,
\]
\[
N_{2,2}(t)=1+14t+56t^2+74t^3+32t^4+4t^5.
\]

## Assumptions and scope
A *partial injection* on a finite set \(X\) is an injective function whose domain is an arbitrary subset of \(X\). The everywhere-undefined partial injection is \(\varnothing\). Composition is the ordinary composition of partially defined maps; rank is domain cardinality. An element is *nilpotent* if some positive power is \(\varnothing\). No ground field or characteristic is involved. Every square-zero partial injection of rank \(r\) has disjoint directed arrows \(a_i\mapsto b_i\) for \(1\le i\le r\) and \(s\) remaining isolated vertices \(c_j\). The formula includes \(r=0\) and \(s=0\), with \(n\ge1\).

## Proof
**1. Complete and unique centralizer decomposition.** Put \(A=\{a_1,\ldots,a_r\}\), \(B=\{b_1,\ldots,b_r\}\), and \(D=\{c_1,\ldots,c_s\}\), all disjoint. For a commuting partial injection \(g\), the equality \(fg=gf\) implies: if \(g(b_i)\) is defined, then \(g(a_i)=a_j\) and \(g(b_i)=b_j\) for a common index \(j\); if \(g(a_i)\) is defined but does not lie in \(A\), then \(g(b_i)\) is undefined; and any defined \(g(c_j)\) belongs to \(B\cup D\). Conversely, these conditions, together with injectivity, ensure commutation, by checking the domain and value of each product at the three vertex types.

Thus a commuting map determines a unique partial injection \(\alpha\) of the \(r\) chain indices: \(\alpha(i)=j\) exactly when \(g(a_i)=a_j\); it forces \(g(b_i)=b_j\). If \(\operatorname{rk}\alpha=k\), the remaining defined arrows of \(g\) are an arbitrary partial injection \(h\) from the \(m=r-k+s\) unused vertices in \(A\cup D\) to the \(m\) unused vertices in \(B\cup D\). The two lists overlap precisely in the \(s\) vertices of \(D\). This decomposition is bijective and \(\operatorname{rk}g=2k+\operatorname{rk}h\). There are \(\binom rk^2k!\) possible \(\alpha\), while the rank polynomial for \(h\) is \(P_m\): choose its source and target subsets and then a bijection. Summing proves the first formula.

**2. Nilpotency of the two factors.** A partial injection on a finite set is nilpotent precisely when its directed graph contains no cycle. Every arrow of \(g\) either stays inside a chain-source set \(A\), stays inside a chain-target set \(B\), moves from \(A\) into \(B\cup D\), or moves from \(D\) into \(B\cup D\). No directed cycle can mix these sets. Cycles inside \(A\) and \(B\) occur precisely when the partial injection \(\alpha\) has cycles; the only remaining possible cycles lie entirely in \(D\) and come from \(h\). Therefore \(g\) is nilpotent if and only if \(\alpha\) is acyclic and \(h\) has no cycle entirely in \(D\).

**3. Acyclic chain-index injections.** For \(r\ge1\), an acyclic rank-\(k\) partial injection on the chain indices decomposes into \(r-k\) unordered nonempty directed paths, allowing paths consisting of a single isolated vertex. Enumerate these by ordering the \(r\) vertices, cutting the list into \(r-k\) nonempty successive blocks, and forgetting the ordering of blocks. This gives
\[
\frac{r!}{(r-k)!}\binom{r-1}{r-k-1}
=\binom rk\binom{r-1}k k!=a_{r,k}.
\]
At \(k=r\) the count is zero. At \(r=0\), there is a single empty partial injection, as prescribed.

**4. Exact cancellation sieve for cycles on the isolated vertices.** Fix \(k\) and \(m=r-k+s\). Let \(H_{m,s}(t)\) enumerate partial injections from the \(m\)-element source list into the \(m\)-element target list which have no cycle contained in their common \(s\)-element subset \(D\). Use inclusion-exclusion on the collection of directed cycles supported on \(D\). If marked cycles jointly cover exactly \(j\) of the \(s\) common vertices, choose those vertices, put on them a permutation \(\sigma\in S_j\), and retain an arbitrary matching on the \(m-j\) unused sources and targets. Each chosen cycle supplies a sign \(-1\). Thus
\[
H_{m,s}(t)=\sum_{j=0}^s\binom sj t^j P_{m-j}(t)
\sum_{\sigma\in S_j}(-1)^{\operatorname{cyc}(\sigma)}.
\]
For \(j=0\) the inner sum is \(1\); for \(j=1\) it is \(-1\); and for \(j\ge2\) it vanishes. Indeed, \(\sum_{\sigma\in S_j}z^{\operatorname{cyc}(\sigma)}=z(z+1)\cdots(z+j-1)\), evaluated at \(z=-1\). Hence
\[
\boxed{H_{m,s}(t)=P_m(t)-s t P_{m-1}(t).}
\]
The nilpotent enumeration follows by multiplying the independent counts of acyclic \(\alpha\) and cycle-free \(h\), with the rank shift \(2k\), and summing over \(k\).

**5. Highest rank.** Assume \(r\ge1\). For \(k\le r-2\), summands in the nilpotent polynomial have degree at most \(2k+m=r+k+s\le n-2\). The only contribution at degree \(n-1\) comes from \(k=r-1\). Its chain-index coefficient is \(a_{r,r-1}=r!\). In this term \(m=s+1\), and the leading coefficient of \(P_{s+1}-s t P_s\) is \((s+1)!-s\,s!=s!\). Thus \([t^{n-1}]N_{r,s}=r!s!\). Likewise \([t^n]C_{r,s}=r!s!\) comes solely from \(k=r\). At \(r=0\), \(N_{0,s}=P_s-stP_{s-1}\); its top degree is \(s-1\), with coefficient \(s!\), the number of full-length directed chains. This completes the proof.

## Verification
The accompanying self-contained `verify.py` enumerates every partial injection on labeled sets of sizes \(1\) through \(6\), for every possible square-zero rank \(r\). It composes actual maps, filters those commuting with a standard square-zero map, and independently detects cycles in their functional digraphs. It compares every observed coefficient of both rank polynomials against the formulas, including all zero coefficients. There are 15 parameter pairs. The recorded stdout in `verification_output.txt` ends with `ALL_ROOK_CENTRALIZER_NILPOTENT_RANK_CHECKS_PASS`. This is a finite corroboration, not the proof for all \(r,s\); the preceding counting and cancellation establish the infinite family.

## Relationship to prior work
Konieczny (first published online September 28, 2012), particularly Proposition 3.1 and Theorem 3.4, already completely characterizes the individual partial injections commuting with an arbitrary member of a symmetric inverse semigroup. This result **does not claim a new centralizer membership theorem**; its new candidate content is the uniform two-parameter **nilpotent rank generating polynomial**, together with the explicit rank enumerator for context, obtained by isolating an acyclic chain-index factor and applying the nontrivial signed cycle-marking cancellation on a shared set of isolated points. Gomes and Howie (1987), especially Lemma 2.1 and Theorem 2.8, already characterize general nilpotent partial injections as unions of directed chains. Their result does not state the joint constraint of nilpotency *and* commutation with a prescribed square-zero map or the corresponding full rank distribution. The finite centralizer Green-relations paper of Konieczny (2020) is a relevant possible source of broader coverage; its abstract was checked, but its full text could not be inspected, so no whole-document noncoverage is asserted. Earlier treatments of symmetric inverse monoids, including Lipscomb's 1996 monograph, remain a historical priority risk. A prior full centralizer classification can imply element membership without directly supplying the evaluated enumerator; novelty of the polynomial is provisional pending wider literature verification.

## Limitations
The formulas specialize to centralizers of square-zero elements and classify only counts by partial-injection rank. They do not determine joint cycle-length or nilpotency-index refinements, Green classes, or the general centralizer of arbitrary partial injections. Independent mathematical validation and historical-priority certification have not been performed. The 2020 centralizer article and the relevant monograph were not fully inspected.

## References
- J. Konieczny, “Centralisers in the Infinite Symmetric Inverse Semigroup,” *Bulletin of the Australian Mathematical Society* **87** (2013), 462–479; first published online 2012-09-28. https://doi.org/10.1017/S0004972712000779. In particular Proposition 3.1, Theorem 3.4.
- G. M. S. Gomes and J. M. Howie, “Nilpotents in Finite Symmetric Inverse Semigroups,” *Proceedings of the Edinburgh Mathematical Society* **30** (1987), 383–395. https://doi.org/10.1017/S0013091500026778. In particular Lemma 2.1, Theorem 2.8, Corollary 2.9.
- J. Konieczny, “The Structure of Centralizers in the Finite Symmetric Inverse Semigroup,” *Communications in Algebra* **48** (2020). https://doi.org/10.1080/00927872.2020.1782926 (abstract inspected; full text unavailable).
- S. Lipscomb, *Symmetric Inverse Semigroups*, AMS Mathematical Surveys and Monographs **46** (1996), especially chapters on commuting partial transformations and centralizers (bibliographic reference; full chapter text not inspected).
