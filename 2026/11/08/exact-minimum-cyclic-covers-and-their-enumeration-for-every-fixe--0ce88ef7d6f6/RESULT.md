# Exact minimum cyclic covers and their enumeration for every fixed nonzero weight

## Finding
Let \(q\ge 2\), \(n\ge 2\), and \(1\le k\le n\) be integers. Distinguish the symbol \(0\) in the alphabet \(\Sigma_q=\{0,1,\ldots,q-1\}\), and let \(\mathcal F_{q,n,k}\) be all length-\(n\) words with exactly \(k\) nonzero positions. An *exact cyclic track cover* is an unordered family of nonempty circular words whose cyclic length-\(n\) windows, with wraparound as often as necessary, comprise every member of \(\mathcal F_{q,n,k}\) exactly once and no other window. Rotations of a track are identified, but reversal and alphabet relabeling are not.

Write \(s=q-1\), and let \(N(n,k)\) be the binary fixed-weight necklace number
\[
N(n,k)=\frac1n\sum_{d\mid\gcd(n,k)}\varphi(d)\binom{n/d}{k/d}.
\]
The smallest number of tracks is precisely \(N(n,k)\). The **exact number of minimum-track covers**, as just defined, is
\[
\boxed{\mathcal C(q,n,k)=s^{\,s^{k-1}\binom{n-1}{k-1}-kN(n,k)}\big((s-1)!\big)^{\,s^{k-1}\binom{n-1}{k-1}}.}
\]
In fact, every binary necklace of length \(n\) and weight \(k\) has its own forced track. If the necklace has least rotational period \(h\) and its aperiodic support block has \(a=kh/n\) ones, the number of choices for that track is
\[
\boxed{s^{\,a s^{k-1}-k}\big((s-1)!\big)^{\,a s^{k-1}},}
\]
and the corresponding restricted de Bruijn component has exactly \(s^{\,a s^{k-1}-k}\) spanning in-arborescences rooted at any vertex.

For illustration, for \(q=3\), \(k=3\), and \(n=4,5,6\), the minimum track counts are \(1,2,4\), while the numbers of minimum covers are \(512\), \(262144\), and \(268435456\), respectively. The case \(k=n\) reduces to the standard enumeration of de Bruijn cycles on \(s\) nonzero symbols; the case \(q=2\) gives one minimum cover, consisting of one periodic track per binary support necklace.

## Assumptions and scope
A circular word is an indexed finite word modulo cyclic rotation, and its length-\(n\) windows are defined by periodic extension even if the word itself has length less than \(n\). A cover counts *distinct* windows, not merely one appearance of a class under rotation. Each track may have any positive length, and all windows must have exactly \(k\) nonzero positions. A cover is a family without ordering on its tracks; once support components are identified, they are distinguishable by support necklace, so this convention introduces no extra factorial. All symbols remain labeled. The proof works for the full range \(q\ge2\), \(n\ge2\), \(1\le k\le n\); the all-zero case \(k=0\) separately has one single-symbol track and one cover.

## Proof
**1. The overlap graph and its invariant.** Form the directed de Bruijn-type multigraph \(G\) whose edges are the words \(w\in\mathcal F_{q,n,k}\), with tail their length-\(n-1\) prefix and head their length-\(n-1\) suffix. Its vertices are exactly the length-\(n-1\) words of nonzero weight \(k-1\) or \(k\), with infeasible weights omitted. For a vertex of weight \(k-1\), every legal incoming or outgoing edge appends or prepends one of the \(s\) nonzero symbols; its in- and outdegree are both \(s\). At weight \(k\), those degrees are both one, supplied by \(0\). Hence \(G\) is balanced.

The zero/nonzero indicator sequence of a track satisfies \(b_{i+n}=b_i\), because consecutive length-\(n\) windows both have weight \(k\). Equivalently, consecutive edge-support indicators in \(G\) are cyclic rotations. Thus edges in different binary necklaces of length \(n\) and weight \(k\) cannot share a track. In particular every cover needs at least \(N(n,k)\) tracks; the displayed necklace formula is the classical Burnside rotation count.

**2. Structure of one support component.** Fix a binary support necklace with least period \(h\mid n\), and let \(a=kh/n\) be the number of ones in its aperiodic period block. For each of its \(h\) support phases \(S\), the vertex is uniquely the \(n-1\) prefix of \(S\), with arbitrary nonzero colors in the prefix. If the last support bit is zero, the prefix has \(k\) colored positions and supplies \(s^k\) vertices of outdegree one. If that bit is one, it has \(k-1\) colored positions and supplies \(s^{k-1}\) vertices of outdegree \(s\). There are \(h-a\) phases of the first kind and \(a\) phases of the second kind. Consequently the component has \((h-a)s^k+a s^{k-1}\) vertices, \(hs^k\) edges and \(a s^{k-1}\) vertices with outdegree \(s\).

Normalize the adjacency by dividing each outgoing edge weight by its tail outdegree to obtain a stochastic matrix \(P\) on these vertices. Each step advances the support phase by one and, when the newly appended position is nonzero, assigns its color uniformly and independently from the \(s\) possibilities. After exactly \(n\) steps, all original coordinates of a length-\(n-1\) vertex have shifted out; its remaining colors were freshly chosen, independently and uniformly. Since \(h\mid n\), the support phase returns to its starting value. Therefore \(P^n\) is a direct sum of \(h\) uniform rank-one blocks, one per phase. In particular the component is strongly connected: every state of every phase can be reached through sufficiently many transitions. Each component is thus Eulerian, achieving a minimum cover with one Euler tour per support necklace.

**3. Exact directed tree count.** The image of \(P^n\) consists of functions constant on each of the \(h\) phases, and \(P\) cyclically permutes these phases. The restriction to the kernel of \(P^n\) is nilpotent. Hence the nonzero eigenvalues of \(P\), including algebraic multiplicities, are exactly the \(h\)-th roots of unity, with all remaining eigenvalues zero. The product of the nonzero eigenvalues of \(I-P\) is therefore
\[
\prod_{j=1}^{h-1}(1-e^{2\pi i j/h})=h,
\]
with the empty product understood as one when \(h=1\). Because each transition sends a uniform distribution on the colorings of one support phase to a uniform distribution on the colorings of the next, its stationary probability at a vertex \(v\) with \(m(v)\) nonzero prefix positions is \(\pi_v=1/(h s^{m(v)})\).

Let \(D\) be the diagonal outdegree matrix and \(L=D(I-P)\) the outgoing directed Laplacian. The adjugate identity for an irreducible stochastic matrix, equivalently the directed Matrix-Tree theorem plus the characteristic-polynomial derivative at zero, gives
\[
\tau_v=\frac{\prod_u d(u)}{d(v)}\,h\pi_v.
\]
Here \(\tau_v\) is the number of directed spanning trees toward root \(v\), with parallel arcs counted separately. Since every vertex has \(d(v)s^{m(v)}=s^k\) and \(\prod_u d(u)=s^{a s^{k-1}}\), this simplifies to
\[
\tau_v=s^{a s^{k-1}-k},
\]
independent of the root. This also holds for \(s=1\), where the graph is one directed support cycle and the count is one.

**4. Euler tours and multiplication.** By the BEST theorem, a connected Eulerian directed graph with distinguishable edges has \(\tau_v\prod_u(d(u)-1)!\) cyclic Euler tours up to cyclic reindexing of its edges. In the present graph the distinct edges are distinct full length-\(n\) words, and the only nontrivial local factor occurs at the \(a s^{k-1}\) vertices of degree \(s\). This gives the track count
\[
s^{a s^{k-1}-k}((s-1)!)^{a s^{k-1}}.
\]
Every minimum cover contains one track per support necklace and choices in different components are independent. Summing \(a\) over all binary support necklaces gives \(\binom{n-1}{k-1}\): each necklace of size \(h\) contributes \(kh/n\), and the sizes of the orbits sum to \(\binom nk\). Multiplying the component factors gives the displayed global formula, completing the proof.

## Verification
The included stand-alone script `verify.py` uses only the Python standard library. For each listed \((q,n,k)\), it builds all labeled full-word edges, groups them by binary support necklace, verifies the vertex and edge counts and balanced degrees, computes integer Laplacian cofactors using a fraction-free determinant, and compares each component factor and the global product with the formulas. For three small instances it independently enumerates cyclic Euler tours by fixing one edge and explicitly traversing all remaining edge orderings.

Successful exact checks cover \((q,n,k)\) equal to \((2,5,3)\), \((3,3,2)\), \((3,3,3)\), \((3,4,2)\), \((3,4,3)\), \((3,4,4)\), \((3,5,3)\), \((3,6,3)\), \((4,3,2)\), \((4,3,3)\), \((4,4,2)\), and \((4,4,3)\). These finite checks are not the proof of the infinite theorem: the stochastic reset, Laplacian, and BEST argument above supplies that proof.

## Relationship to prior work
The existing fixed-weight string literature emphasizes shortening the representation by omitting a redundant symbol, thereby joining what would otherwise be separate support components into a single universal cycle. Sawada and Williams construct fixed-content shorthand universal cycles; Campbell, Janik-Jones and Sawada (March 2026) give efficient bounded-weight and subset/multiset constructions; Gabrić, Imam, Janik-Jones and Sawada (March 2026) give efficient decoding for bounded-weight cycles. These works use a different representation and do not determine the present exact enumeration of minimum covers in the *unshortened* full-word model. The \(k=2\) specialization agrees with the simpler two-nonzero case, which is not presented as an independent new result. The present claim is the simultaneous arbitrary-\(k\) classification and closed enumeration.

## Limitations
The result counts only covers that use the *minimum possible number of tracks*. It does not classify larger-track decompositions, track lengths under additional restrictions, quotient by reversal or nonzero-alphabet permutations, or universal cycles for a different shorthand representation. Its novelty assessment is limited to the inspected accessible literature and indexed records; unindexed equivalent results may exist. Independent mathematical audit has not been performed.

## References
- C. Campbell, L. Janik-Jones and J. Sawada, *Universal cycle constructions for k-subsets and k-multisets*, arXiv:2603.11954, first publicly submitted 2026-03-12. https://arxiv.org/abs/2603.11954
- D. Gabrić, W. Imam, L. Janik-Jones and J. Sawada, *Decoding universal cycles for t-subsets and t-multisets by decoding bounded-weight de Bruijn sequences*, arXiv:2603.11934, first publicly submitted 2026-03-12. https://arxiv.org/abs/2603.11934
- J. Sawada and A. Williams, *A Universal Cycle for Strings with Fixed-Content*, available full text. https://skeeter.socs.uoguelph.ca/~sawada/papers/fixedContentUCycle.pdf
- N. G. de Bruijn, *A combinatorial problem*, Proc. Koninklijke Nederlandse Akademie van Wetenschappen, 1946 (classical de Bruijn sequence enumeration).
- G. W. Smith and W. T. Tutte, directed Matrix-Tree theorem (standard directed tree enumeration); de Bruijn, van Aardenne-Ehrenfest, Smith and Tutte, BEST theorem (standard Euler circuit enumeration).
