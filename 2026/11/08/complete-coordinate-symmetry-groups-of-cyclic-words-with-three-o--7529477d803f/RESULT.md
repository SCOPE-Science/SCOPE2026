# Complete coordinate symmetry groups of cyclic words with three or more monochromatic runs

## Finding
Let \(q\ge3\), let \(c_0,\ldots,c_{q-1}\) be pairwise distinct letters, and choose any positive run lengths \(a_0,\ldots,a_{q-1}\). Put
\[
U=c_0^{a_0}c_1^{a_1}\cdots c_{q-1}^{a_{q-1}},\qquad p=\sum_{i=0}^{q-1}a_i,\qquad X=U^\omega.
\]
For every \(n\ge p\), let \(G_n(X)\) be the set of permutations of the \(n\) coordinate positions that carry **every** length-\(n\) factor of \(X\) to another such factor. Write \(n=mp+r\), where \(m\ge1\) and \(0\le r<p\). Then, as concrete permutation groups on the \(n\) positions,
\[
G_n(X)=\begin{cases}
(S_m)^p\rtimes C_p\cong S_m\wr C_p,&r=0,\\
(S_{m+1})^r\times(S_m)^{p-r},&1\le r<p.
\end{cases}
\]
The base factors permute positions of equal residue modulo \(p\). The cyclic quotient (when present) shifts the \(p\) residue classes. In particular,
\[
|G_n(X)|=\begin{cases}
p(m!)^p,&r=0,\\
((m+1)!)^r(m!)^{p-r},&1\le r<p.
\end{cases}
\]
Thus at lengths not divisible by \(p\), **every** symmetry fixes each residue class setwise. At multiples of the period the full cyclic quotient appears. This is an exact classification, not merely a lower bound on group size.

## Assumptions and scope
Coordinates are indexed \(0,1,\ldots,n-1\). The word \(X\) is one-sided infinite, and factors are contiguous words. The alphabet contains at least three distinct letters and each letter occurs in exactly one positive-length run per period; no equality of run lengths is assumed. The period \(p\) is minimal because the cyclic sequence of the distinct run letters cannot be repeated with smaller period. We restrict to \(n\ge p\). The group acts on positions, not on alphabet symbols; alphabet relabeling is not an allowed symmetry. All groups are considered up to the stated natural block permutation realization.

## Proof
**1. Recover residue blocks from the factor family.** Put \(u_j=U_{j\bmod p}\). For \(t\in\mathbb Z/p\mathbb Z\), let \(F_t=(u_t,u_{t+1},\ldots,u_{t+n-1})\). For \(n\ge p\), these are exactly the \(p\) distinct factors: if \(F_s=F_t\), the first \(p\) entries give the same cyclic rotation of \(U\), forcing \(s=t\) by minimality of \(p\).

Define \(i\sim j\) when all \(p\) words \(F_t\) have equal entries at positions \(i,j\). Since \(u_{t+i}=u_{t+j}\) for every \(t\) exactly when \(j-i\) is a period of the cyclic word \(U\), one has \(i\sim j\) exactly when \(i\equiv j\pmod p\). These equivalence classes are
\[
R_j=\{i\in\{0,\ldots,n-1\}:i\equiv j\pmod p\},\qquad j\in\mathbb Z/p\mathbb Z.
\]
Every symmetry of the factor family must preserve \(\sim\) and hence permutes the \(p\) nonempty blocks \(R_j\). Let \(f\) be its induced permutation of residues. Conversely any permutation internal to each \(R_j\) fixes every factor and belongs to \(G_n(X)\). We now classify possible \(f\).

**2. A cyclic-interval rigidity lemma.** For integers \(p\ge4\) and \(2\le\ell\le p-2\), let \(\mathcal I_\ell\) consist of all \(p\) cyclic intervals of \(\ell\) consecutive points of \(\mathbb Z/p\mathbb Z\). Every point permutation carrying \(\mathcal I_\ell\) onto itself is a rotation or reflection of the \(p\)-cycle. Indeed, replace \(\ell\) by \(h=\min(\ell,p-\ell)\) by taking complements. Here \(2\le h\le p/2\). For two *distinct points* at circular separation \(d\), the number of intervals of length \(h\) containing both is
\[
\max(0,h-d)+\max(0,h-(p-d)).
\]
Its maximum over distinct point pairs is \(h-1\), attained exactly at pairs of adjacent cycle vertices. Hence the interval family reconstructs the ordinary cycle graph via maximal pair co-occurrence. Its automorphisms are precisely the dihedral permutations.

**3. The induced residue action is a rotation.** A permutation of coordinates in \(G_n(X)\) permutes the factor rows \(F_t\), say \(F_t\mapsto F_{\sigma(t)}\). For each letter \(c_i\), its residue-position set in \(F_t\) is a cyclic interval \(I_i-t\) of size \(a_i\). Consequently \(f(I_i-t)=I_i-\sigma(t)\) for every phase \(t\).

If some \(a_i\ge2\), then \(a_i\le p-2\) since at least two other positive runs exist. The family of translates \(I_i-t\) is exactly \(\mathcal I_{a_i}\), so the lemma forces \(f\) to be a cycle rotation or reflection. A reflection would map the original cyclic word to a reversed rotation: evaluating the factor at phase zero shows that the cyclic order of the \(q\) distinct run labels would have to be simultaneously \((c_0,c_1,\ldots,c_{q-1})\) and its reverse, up to rotation. That is impossible for \(q\ge3\). Thus \(f\) is a rotation.

If instead all \(a_i=1\), then \(p=q\) and every position of \(U\) has a different label. The condition that \(f\) takes \(F_0\) to a cyclic rotation determines \(f\) uniquely as a rotation. Thus in all cases the induced action is a subgroup of \(C_p\).

**4. Count and realize all possibilities.** If \(n=mp+r\) with \(0\le r<p\), then \(|R_j|=m+1\) for the consecutive residues \(0\le j<r\), and \(|R_j|=m\) otherwise. A residue rotation can be implemented by a permutation of coordinate positions only if it preserves these block sizes. For \(1\le r<p\), the subset of the first \(r\) residues is a nonempty proper cyclic interval and has no nonidentity rotational stabilizer; hence \(f\) must be the identity. All and only the independent internal block permutations survive.

For \(r=0\), the \(p\) blocks each have size \(m\). Every cyclic rotation of blocks is implementable: identify \(R_j\) with \(\{(j,k):0\le k<m\}\) and map \((j,k)\) to \((j+1,k)\). Applied to each factor, this simply advances its phase by one; it is a group element of order \(p\), and conjugation cyclically permutes the internal symmetric factors. This gives the stated semidirect/wreath product. Counting permutations proves both order formulas. \(\square\)

## Verification
The standalone Python 3 program `verify.py` constructs the entire factor set and checks **every** permutation of coordinates for each of 382 configurations: all compositions of periods \(3\le p\le8\) into \(q\ge3\) positive runs, all admissible \(q\), and every \(p\le n\le8\). Each computed group order agrees with the formula. It also checks the sharp binary boundary \(U=0011\), whose length-four group order is eight, whereas the formula for three or more distinct run letters would give four. Execute `python3 verify.py` in a directory containing the extracted file. This finite computation is corroboration, not the proof for arbitrary parameters.

## Relationship to prior work
Luchinin and Puzynina, *Sequences of symmetry groups of infinite words* (first preprint December 9, 2021), introduce this exact coordinate-symmetry invariant. Their Proposition 6 states that all within-residue permutations lie in the symmetry group for a periodic word; their Corollary 2 supplies a cyclic shift at lengths divisible by the period. The theorem here determines the **entire** group and its order for cyclic words with at least three distinct single-run letters, by showing that no additional residue actions exist, and describes the sharp dependence on the factor length modulo the period.

Charlier, Puzynina, and Zamboni (2015) study group-action factor complexity, which counts factor orbits for prescribed groups rather than the maximal coordinate-permutation group preserving a given periodic factor language. The 2026 discussion of universal group complexity of eventually periodic words likewise addresses attainable orbit counts, not this group equality.

## Limitations
This result does not classify smaller factor lengths \(n<p\), arbitrary periodic words with repeated nonadjacent run letters, or two-letter cycles. The condition \(q\ge3\) is essential: for \(U=0011\), eight position permutations preserve the four cyclic rotations, including reflections, not just the four rotations predicted by a naive extension. Searches and examination of the cited source do not prove absolute bibliographic uniqueness; an unindexed equivalent remains possible. The proof treats all positive run profiles under the stated hypotheses; the enumerator checks only a bounded finite range.

## References
1. S. Luchinin and S. Puzynina, *Sequences of symmetry groups of infinite words*, arXiv:2112.04848v1, first posted December 9, 2021, especially Definition 1, Proposition 6, and Corollary 2. https://arxiv.org/pdf/2112.04848v1
2. É. Charlier, S. Puzynina, and L. Q. Zamboni, *On a group theoretic generalization of the Morse-Hedlund theorem*, arXiv:1505.03848, first posted May 14, 2015. https://arxiv.org/abs/1505.03848
3. M. Launer, S. Puzynina, and E. Voloshinova, *On possible values of the group complexity function of infinite words*, arXiv:2607.07620, July 8, 2026. https://arxiv.org/abs/2607.07620
