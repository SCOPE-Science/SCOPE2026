# Block-order reversal splitting for permutation complexes

## Finding

Let \(A\) and \(B\) be **disjoint, nonempty finite alphabets**, and let \(P\subseteq\mathfrak S_A\), \(Q\subseteq\mathfrak S_B\) be nonempty sets of full permutations. Write \(X(P)\) and \(X(Q)\) for the regular CW complexes of ordered injective words that occur as subsequences of permutations in \(P\) and \(Q\), respectively. Define \(P\mid Q=\{pq:p\in P,q\in Q\}\), where juxtaposition denotes concatenation, and put \(R=(P\mid Q)\cup(Q\mid P)\). Then the following is an **unstable integral homotopy equivalence** (all suspensions and joins of spaces, and all wedges taken after choices of paths/basepoints):

\[
\boxed{X(R)\simeq S^1\vee\Sigma X(P)\vee\Sigma X(Q)\vee (X(P)*X(Q))\vee(X(P)*X(Q)).}
\]

Consequently \(\pi_1(X(R))\cong\mathbb Z\), without any connectivity or torsion assumptions on the *higher* homotopy of the factor complexes. In particular, if \(P\) and \(Q\) are the entire symmetric groups on alphabets of sizes \(a,b\ge2\), and \(D(j)\) denotes the number of fixed-point-free permutations of \(j\) letters, then

\[
\boxed{X(R)\simeq S^1\vee\bigvee^{D(a)}S^a\vee\bigvee^{D(b)}S^b\vee\bigvee^{2D(a)D(b)}S^{a+b-1}.}
\]

When \(a=b\), \(R\) consists precisely of permutations preserving the two-block partition, with the option to exchange the blocks: the standard imprimitive wreath-product subgroup \(\mathfrak S_a\wr C_2\le\mathfrak S_{2a}\). The formula therefore gives an exact homotopy classification for this entire infinite family, including its free fundamental group and integral Betti numbers. If two sphere dimensions coincide, multiplicities are added, not identified as different degrees.

## Assumptions and scope

An injective word is a finite nonempty word with no repeated letter. Every length-\(k+1\) word is a \(k\)-cell, with faces obtained by deleting one letter; the face poset barycentric subdivision agrees with the permutation complexes defined via order complexes. A word belongs to \(X(P)\) precisely when it is a subsequence of some full permutation from \(P\). The empty word is used only as the formal unit of a join, not as an added vertex. All spaces are geometric realizations, all homotopy equivalences are nonequivariant, and \(\Sigma\) is reduced suspension of the connected space up to homotopy (equivalently its unreduced suspension).

No assumption is made that \(P\) or \(Q\) is a subgroup. The alphabets must be disjoint and nonempty and both permutation families nonempty. Finite regular CW subcomplex inclusions are cofibrations. The explicit wedge splittings are not asserted to be canonical or equivariant.

## Proof

**Step 1: two join hemispheres.** Let \(U=X(P\mid Q)\) and \(V=X(Q\mid P)\). A subword of a concatenation \(pq\) has all its \(A\)-letters before all its \(B\)-letters. It is uniquely of the form \(uv\), with \(u\) a (possibly empty) subword of some \(p\in P\) and \(v\) a (possibly empty) subword of some \(q\in Q\). Conversely any such \(uv\) extends to a concatenation \(pq\). The semisimplicial join of the two ordered-word complexes has exactly these cells and their deletion faces. Hence \(U\cong X(P)*X(Q)\) as regular CW complexes. Reversing the block order gives \(V\cong X(Q)*X(P)\), homeomorphic to the same join after swapping factors.

**Step 2: exact overlap.** A word containing at least one letter of each alphabet cannot place all \(A\)-letters before all \(B\)-letters and simultaneously all \(B\)-letters before all \(A\)-letters. Every word using a single block occurs in both hemispheres. Thus, as CW subcomplexes, \(U\cap V=X(P)\sqcup X(Q)\). In particular the overlap has exactly two path components, because each factor contains the full simplex arising from any one of its generating permutations, so each factor is path connected.

**Step 3: nullhomotopic attachment maps.** In either join, the inclusion of \(X(P)\) is nullhomotopic by coning it toward any chosen point in \(X(Q)\). Similarly, the inclusion of \(X(Q)\) is nullhomotopic toward a point in \(X(P)\). Since the ambient join is path connected, the two contractions may be adjusted to the same endpoint, so the inclusion of the whole disconnected overlap into either hemisphere is nullhomotopic. The subcomplex inclusions are cofibrations, hence the union \(X(R)=U\cup V\) is their homotopy pushout. Replacing both maps from the overlap by constant maps preserves this homotopy pushout and yields a wedge of \(U\), \(V\) and the unreduced suspension of \(X(P)\sqcup X(Q)\).

**Step 4: circle and suspensions.** For two nonempty connected CW spaces \(E,F\), the unreduced suspension \(\Sigma_u(E\sqcup F)\) is homotopy equivalent to \(S^1\vee\Sigma E\vee\Sigma F\). One way to see this is to choose one point in each component, collapse a maximal tree consisting of the two suspension paths and their endpoints, and identify the remaining reduced suspensions and one independent loop. Applying this with \(E=X(P)\), \(F=X(Q)\) proves the first display. The suspensions of connected spaces are simply connected, and the join of two nonempty connected spaces is simply connected, so Van Kampen gives \(\pi_1(X(R))\cong\mathbb Z\).

**Step 5: full-block specialization.** For every \(j\ge2\), the full injective-word complex is homotopy equivalent to \(\bigvee^{D(j)}S^{j-1}\) by the Farmer/Björner–Wachs theorem. Suspension shifts each sphere by one. The join of \(\bigvee^{D(a)}S^{a-1}\) and \(\bigvee^{D(b)}S^{b-1}\) is homotopy equivalent to \(\bigvee^{D(a)D(b)}S^{a+b-1}\). Substitution in the first display yields the second. For equal block sizes, any permutation in \(\mathfrak S_a\wr C_2\) sends the first block either to itself or to the other block, so its ordered word is exactly one of the two permitted block concatenation orders. Conversely each such concatenation realizes a wreath-product element.

## Verification

The accompanying standalone \(block_reverse_checker.py\) constructs all subsequences of the prescribed facets, forms the exact signed deletion-boundary matrices, computes ranks over \(\mathbb F_2\) and \(\mathbb F_{101}\), and compares each Betti vector with the first splitting formula. Run `python block_reverse_checker.py` using Python 3 and no external packages. It checks all \(9\) nonempty pairs of permutation sets on \(2+2\) letters, all \(189\) pairs on \(2+3\) letters, and \(36\) specified representatives on \(3+3\) letters: \(234\) pairs in both characteristics. Full-block Betti vectors, including degree zero, are \((1,1,2,2)\) at \((2,2)\), \((1,1,1,2,4)\) at \((2,3)\), and \((1,1,0,4,0,8)\) at \((3,3)\). These checks corroborate exact finite cases only; the proof establishes the unbounded statement.

## Relationship to prior work

Govc's 2026 theorem establishes that the fundamental group of every permutation complex is free, but does not classify the block-reversal operation or supply the two-factor unstable homotopy decomposition. Chachólski, Levi and Meshulam (2019/2020) introduced permutation complexes, identified the full injective-word wedge of spheres, and derived a two-*individual*-permutation decomposition and a concatenation identity for intersections. Those ingredients do not state the result for two arbitrary nonempty permutation families and both block orders. The present formula recovers the circle arising from a single permutation in each factor as a special case; that special case alone is not claimed to be new. The 2026 pattern-avoidance paper studies subcomplexes from avoiding patterns and shellability, rather than this two-sided block-order construction.

A distinct indexed calculation for dihedral permutation complexes concerns rotations and reversals of a *single* full word and yields only two-dimensional sphere bouquets; it does not imply a general construction with arbitrary input complexes and a persistent fundamental circle. Other published join formulas for different graph complexes concern different underlying cell systems. The claim is about an explicit operation on permutation-complex generators, not a new abstract homotopy-pushout theorem.

## Limitations

This is a nonequivariant homotopy equivalence, not a canonical splitting of chain complexes, nor a claim about arbitrary interleavings of the two blocks. It does not establish a full classification of all permutation complexes or determine induced automorphism representations under block interchange. The calculated examples are finite checks, not an infinite certificate. The novelty comparison is limited to accessed literature; an equivalent formula under different terminology remains possible.

## References

- Dejan Govc, *Fundamental Groups of Permutation Complexes*, arXiv:2611.11362v1, first public 2026-11-08. https://arxiv.org/abs/2611.11362
- Wojtek Chachólski, Ran Levi and Roy Meshulam, *On the topology of complexes of injective words*, arXiv:1908.03394 (2019), J. Appl. Comput. Topol. 4 (2020), 29–44. https://arxiv.org/abs/1908.03394
- Sergi Elizalde, Philip Hanlon and Patricia Hersh, *Complexes of pattern-avoiding injective words*, arXiv:2610.07303v1, 2026-10-05. https://arxiv.org/abs/2610.07303
- Frank D. Farmer, *Cellular homology for posets*, Math. Japon. 23 (1978/79), 607–613.
- Anders Björner and Michelle Wachs, *On lexicographically shellable posets*, Trans. Amer. Math. Soc. 277 (1983), 323–341.
