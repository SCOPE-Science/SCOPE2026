# A parity-induced magnetization step on finite Möbius Ising ladders

## Finding

For every integer \(n\ge3\), the antiferromagnetic nearest-neighbor Ising model on the \(2n\)-vertex Möbius ladder has an exact zero-temperature field response depending only on the parity of \(n\). With coupling \(J>0\), real magnetic field \(h\), and \(b=|h|/J\), its ground energy is
\[
\frac{E_0(h)}{J}=
\begin{cases}
\min\{-3n,\;3n-2nb\},&n\text{ odd},\\
\min\{-3n+4,\;-3n+6-2b,\;3n-2nb\},&n\text{ even}.
\end{cases}
\]
Thus the only positive critical field is \(b=3\) when \(n\) is odd, whereas the even case has critical fields \(b=1\) and \(b=3\). In an open field interval, the ground-state magnetization \(M=\sum_v\sigma_v\) is \(0\) for \(0<b<3\) when \(n\) is odd; for even \(n\) it is \(0\) for \(0<b<1\), then \(2\operatorname{sgn}(h)\) for \(1<b<3\). For both parities \(M=2n\operatorname{sgn}(h)\) when \(b>3\).

Every ground-state multiplicity is also exact. Define
\[
I_n=(1+\sqrt2)^n+(1-\sqrt2)^n-(-1)^n.
\]
For odd \(n\), the degeneracy is \(2\) at \(0\le b<3\), \(I_n\) at \(b=3\), and \(1\) at \(b>3\). For even \(n\), it is \(2n\) at \(0\le b<1\), \(4n\) at \(b=1\), \(2n\) at \(1<b<3\), \(I_n\) at \(b=3\), and \(1\) at \(b>3\). At \(b=3\), the ground states are in bijection with independent vertex sets of the Möbius ladder (the vertices carrying the minority spin). Consequently the residual entropy per spin at this coexistence field satisfies
\[
\lim_{n\to\infty}\frac{\log I_n}{2n}=\frac12\log(1+\sqrt2),
\]
while the entropy per spin on each lower-field open plateau tends to zero.

## Assumptions and scope

The finite, simple cubic graph has vertices \(a_1,\ldots,a_n,b_1,\ldots,b_n\) and edges \(a_ib_i\) for \(1\le i\le n\), \(a_ia_{i+1}\) and \(b_ib_{i+1}\) for \(1\le i<n\), and the two twisted seam edges \(a_nb_1\) and \(b_na_1\). This is the standard Möbius ladder \(M_{2n}\), the \(2n\)-cycle with antipodal chords. There are precisely \(3n\) undirected edges, each counted once. Every vertex carries one classical spin \(\sigma_v\in\{-1,+1\}\), and
\[
H(\sigma)=J\sum_{uv\in E(M_{2n})}\sigma_u\sigma_v-h\sum_v\sigma_v.
\]
All results concern finite \(n\ge3\), every real \(h\), and strictly antiferromagnetic uniform \(J>0\). The field sign is handled by global spin inversion. No quantum, random-coupling, finite-temperature, or infinite-volume phase assertion is made.

## Proof

**1. Energy and a universal cubic-graph inequality.** By symmetry assume \(h\ge0\), and let \(S\) denote the set of negative-spin vertices, \(k=|S|\). If \(h>0\), a minimizing state can have \(k\le n\), since global spin inversion strictly lowers its field energy otherwise. Let \(s=n-k\ge0\). Write \(f\) for the number of monochromatic edges and \(c\) for the number of opposite-spin edges. Since \(c+f=3n\) and each negative spin is incident with at most three cut edges, \(c\le3k\); hence
\[
f\ge3(n-k)=3s,\qquad \frac{H(\sigma)}{J}=-3n+2f-2bs.
\]
For \(h=0\), the same energy identity holds for either orientation, and unrestricted spin inversion permits choosing \(k\le n\).

**2. A topological frustration distinction.** Partition the edges into \(n\) successive quadrilateral faces: the \(i\)th face uses the rungs at \(i\) and \(i+1\), plus the two ordinary leg edges, with the last face using the two twisted seam edges. Along each quadrilateral the number of monochromatic edges is even: the product of the four edge spin products is \(1\). A rung belongs to two such quadrilaterals and each leg edge belongs to one.

When \(n\) is odd, alternating spins along each leg and opposite spins across each rung satisfy also the twist. The graph is connected and bipartite, so \(f=0\) occurs in exactly two configurations, both with \(k=n\).

When \(n\) is even, the cycle consisting of \(n-1\) consecutive top-leg edges, one twisted seam edge, and one rung has odd length \(n+1\); hence \(f\ge1\). In fact \(f\ge2\): a single monochromatic edge would belong to one or two quadrilateral faces and create an odd count in at least one face. Moreover, if \(f=2\), the two monochromatic edges must be the pair of leg edges in one quadrilateral. Two edges of distinct faces cannot make all face parities even, and two rungs have different two-face incidence pairs for \(n\ge4\). Conversely, for each of the \(n\) possible faces, alternating spins on the remaining legs with antialigned rungs realizes exactly that pair; there are precisely two configurations related by global inversion. Therefore \(f=2\) is attained in exactly \(2n\) configurations, all with one positive and one negative spin on each rung, so \(s=0\).

**3. Independent-set branch.** For any configuration, \(f=3s\) holds exactly when every edge incident with a negative vertex is a cut edge; equivalently \(S\) is an independent set. For odd \(n\), its maximum size is \(n\), attained in the two bipartition classes. For even \(n\), an independent set includes at most one vertex from each rung; selecting one on every rung would force alternation around the twisted cycle and is impossible. Thus \(\alpha(M_{2n})\le n-1\). Selecting one spin in every rung except a chosen empty rung, alternating the chosen row along the remaining rung path, attains \(n-1\). There are exactly \(n\) choices for the empty rung and two choices for alternation, hence exactly \(2n\) maximum independent sets, each giving \(s=1\).

**4. Minimize the exact bounds.** For odd \(n\), the inequality \(f\ge3s\) gives \(H/J\ge-3n+(6-2b)s\) with \(0\le s\le n\). When \(b<3\) the minimum occurs at \(s=0\), attained by the two bipartite antiferromagnetic configurations. When \(b>3\) it occurs at \(s=n\), attained only by all positive spins. At \(b=3\), equality holds precisely for independent negative-spin sets.

For even \(n\), the case \(s=0\) obeys \(f\ge2\), attaining energy \(-3n+4\) in exactly \(2n\) states. For integers \(1\le s\le n\), \(f\ge3s\), so the best energy is at \(s=1\) if \(b<3\), at \(s=n\) if \(b>3\), and at every independent-set size when \(b=3\). The \(s=1\) equality states are precisely the \(2n\) maximum independent sets. Comparing \(-3n+4\) with \(-3n+6-2b\) gives the sole additional crossing \(b=1\). At this field the two disjoint ground families have total degeneracy \(4n\). This proves the energies, magnetizations and every degeneracy except the explicit independent-set count.

**5. Exact saturation-field multiplicity.** An independent set on one rung has one of three states: empty, top occupied, bottom occupied. Between ordinary consecutive rungs the only forbidden transitions are two consecutive top occupations and two consecutive bottom occupations. In that state order the compatibility matrix and the twist permutation are
\[
T=\begin{pmatrix}1&1&1\\1&0&1\\1&1&0\end{pmatrix},\qquad
P=\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}.
\]
The number of independent sets is \(I_n=\operatorname{tr}(T^nP)\). The symmetric sector has eigenvalues \(1+\sqrt2\) and \(1-\sqrt2\), both fixed by \(P\); the antisymmetric sector has eigenvalue \(-1\) and \(P\)-sign \(-1\). Therefore \(I_n=(1+\sqrt2)^n+(1-\sqrt2)^n-(-1)^n\). Since \(|1-\sqrt2|<1\), the entropy limit follows.

## Verification

The finite-parameter proof above does not rely on computer enumeration. The standalone script `verify_exhaustive.py` enumerates each of the \(2^{2n}\) spin states for \(3\le n\le9\), at nine exactly representable fields, testing both the minimum energy and exact multiplicity. The independently structured `verify_transfer.py` builds the four-rung transfer recursion for exact fixed-magnetization energies, checks the formula for every \(3\le n\le50\), and separately counts independent sets by powering the three-state compatibility matrix. Both scripts use only the Python standard library and print terminating PASS markers when successful. These finite checks corroborate, but do not replace, the all-\(n\) proof.

## Relationship to prior work

Shrock and Tsai (1999) derive chromatic polynomials of cyclic and twisted ladder families, including their two-row case, for the zero-temperature Potts antiferromagnet. Their proper-coloring observable does not determine the energy and field magnetization of frustrated two-state configurations. Lu and Wu (2000) give field-free Ising partition functions for Möbius strips, including the width-two lattice; this substantially covers the zero-field model and can imply its zero-field thermodynamics. It does not evaluate the external-field branches, the finite field-one step or field-three independent-set coexistence. Kaneda and Okabe (2001) investigate critical-temperature finite-size magnetization distributions, not this zero-temperature field envelope. Jurčišinová and Jurčišin (2014) study an infinite zigzag Ising ladder with multisite interactions in a field; the publisher abstract concerns a different interaction geometry and the infinite-size setting, and its complete text was not accessible for a decisive all-section comparison. The elementary facts that the Möbius ladder is bipartite precisely for odd rung count and that independent sets count states at a regular-graph saturation field are used as ingredients, not claimed independently novel. Exact statements about the parity-dependent finite-field classification and multiplicities are the subject of this result.

## Limitations

The \(M=2\) intermediate field plateau for even \(n\) is a finite-size defect: its normalized magnetization vanishes as \(n\to\infty\). The positive-field transition at \(b=3\) has exponentially many coexistence states, but this alone establishes no finite-temperature phase transition. General inhomogeneous couplings, long-range terms, different twists and quantum fluctuations are outside scope. Historical priority remains provisional: an equivalent unindexed Möbius-ladder field computation or a stronger specialized finite-strip theorem could subsume this formula, and the full text of one potentially related 2014 ladder paper could not be compared.

## References

1. R. Shrock and S.-H. Tsai, *Ground State Entropy of the Potts Antiferromagnet on Cyclic Strip Graphs*, arXiv:cond-mat/9903233v1, first posted 1999-03-15. https://arxiv.org/abs/cond-mat/9903233
2. W. T. Lu and F. Y. Wu, *Ising model on nonorientable surfaces: Exact solution for the Moebius strip and the Klein bottle*, arXiv:cond-mat/0007325v1, first posted 2000-07-20. https://arxiv.org/abs/cond-mat/0007325
3. K. Kaneda and Y. Okabe, *Finite-size scaling for the Ising model on the Moebius strip and the Klein bottle*, arXiv:cond-mat/0101054v1, first posted 2001-01-05. https://arxiv.org/abs/cond-mat/0101054
4. E. Jurčišinová and M. Jurčišin, *Solution of the antiferromagnetic Ising model with multisite interaction on a zigzag ladder*, Phys. Rev. E 90, 032108 (2014), DOI:10.1103/PhysRevE.90.032108. https://doi.org/10.1103/PhysRevE.90.032108
