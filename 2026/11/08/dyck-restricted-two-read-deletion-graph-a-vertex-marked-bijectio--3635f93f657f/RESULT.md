# Dyck-restricted two-read deletion graph: a vertex-marked bijection and sharp degree

## Finding
Let \(\mathcal D_n\) be the length-\(2n\) Dyck words over \(\{0,1\}\), with \(1\) an up-step and \(0\) a down-step, and let \(C_n=\binom{2n}{n}/(n+1)\). For \(w\in\mathcal D_n\), let \(D_1(w)\) be the **set** of distinct words formed by deleting exactly one symbol. Form a simple graph \(G_n\) on \(\mathcal D_n\), joining distinct \(x,y\) when \(|D_1(x)\cap D_1(y)|=2\).

**Theorem.** For every \(n\ge1\), the edge set of \(G_n\) is naturally in bijection with triples consisting of an integer \(k\ge1\), a Dyck word of semilength \(n-k\), and a marked **positive-height vertex** of that word. Consequently,
\[
|E(G_n)|=\sum_{m=1}^{n-1}\left((2m+1)C_m-C_{m+1}\right)
=\sum_{m=1}^{n-1}\frac{m(2m+1)}{m+2}C_m.
\]
Furthermore, if \(d_n(w)\) is the degree in \(G_n\), then
\[
\max_{w\in\mathcal D_n}d_n(w)=(n-1)^2.
\]
For \(n\ge3\) its unique maximizing vertex is \(1(10)^{n-1}0\); for \(n=2\), both Dyck words maximize. The edge count has the asymptotic form
\[
|E(G_n)|\sim\frac23nC_n\sim\frac{2}{3\sqrt\pi}\frac{4^n}{\sqrt n},
\qquad \frac{2|E(G_n)|}{C_n}\sim\frac43n.
\]
The **integer sequence and its asymptotic constant were previously known** as the total peak count in Catalan words, OEIS A371965 (Baril et al., 2024). The distinct assertion here is its deletion-reconstruction graph interpretation, canonical edge bijection, and the exact sharp degree bound.

## Assumptions and scope
Dyck words have \(n\) copies of each symbol, nonnegative prefix heights, and total height zero. Positions of a path vertex include both endpoints. An alternating interval has consecutive unequal symbols; its *two phases* are obtained by complementing every symbol in the interval. Deletion balls are **sets**, not multisets. The graph uses the threshold of two **distinct** common descendants, not the threshold of merely one. All claims concern the restricted source space \(\mathcal D_n\); they do not determine optimal code sizes or the entire degree distribution.

## Proof
**1. Alternating-interval characterization.** A published one-deletion intersection theorem (Cai–Kiah–Nguyen–Yaakobi, cited below) states that two distinct equal-length binary words have at most two distinct common one-deletion descendants, and attain two exactly when they agree off their first-to-last differing interval and the two restrictions there are opposite phases of an alternating word of length at least two. This interval is uniquely determined by its endpoints. Because \(x,y\in\mathcal D_n\) have equal symbol counts, the interval must have even length \(2k\), and both phases have zero net height. In particular, its two forms are \((10)^k\) and \((01)^k\).

**2. The edge bijection.** Removing the differing interval from either word produces the same Dyck word \(v\in\mathcal D_{n-k}\), marked at the splice vertex. The height \(h\) at the splice is positive: the phase \((01)^k\) takes a down-step immediately, which would violate Dyck nonnegativity if \(h=0\). Conversely, at any marked vertex of \(v\) of height \(h>0\), insert alternatively \((10)^k\) or \((01)^k\). Both insertions remain Dyck: throughout either inserted block the height is \(h\) or \(h\pm1\), never negative, and the block returns to \(h\). The resulting words differ precisely on that length-\(2k\) interval, hence are adjacent by the stated characterization. Recovering their unique first-to-last differing interval recovers \(k\), \(v\), and the marked vertex. Thus the correspondence is bijective on **unordered** edges, without an orientation factor.

**3. Exact edge enumeration.** Let \(H_m\) denote the number of positive-height vertices, summed over all \(v\in\mathcal D_m\). There are \((2m+1)C_m\) marked vertices in total. A zero-height marked vertex splits a Dyck path uniquely into an ordered pair of Dyck paths, and conversely concatenating such a pair marks its separating ground vertex. Hence the generating function for ground-vertex marks is \(C(z)^2\), where \(C(z)=\sum_{m\ge0}C_mz^m=1+zC(z)^2\). By the Catalan recurrence, \([z^m]C(z)^2=C_{m+1}\), so
\[
H_m=(2m+1)C_m-C_{m+1}=\frac{m(2m+1)}{m+2}C_m.
\]
For a fixed \(k\in\{1,\ldots,n\}\), the bijection counts \(H_{n-k}\) edges; since \(H_0=0\), summing gives the formula.

**4. The exact maximum degree and its uniqueness.** A neighbor of \(w\) is specified by a unique even-length alternating interval whose two phase choices both remain Dyck. Neither end of \(w\) can belong to such an interval: changing the first symbol would change the required initial \(1\) to \(0\), and changing the last symbol would change the required final \(0\) to \(1\). Therefore the interval lies in the interior of length \(2n-2\), which has exactly \((n-1)^2\) nonempty even-length subintervals. Each could give at most one neighbor, proving the upper bound. For \(w=1(10)^{n-1}0\), the whole interior alternates, and the height immediately before every interior position is at least one; thus **every** even interior interval is admissible, proving equality. For \(n\ge3\), equality forces all length-two interior intervals to alternate, so the entire interior alternates. The opposite phase \(1(01)^{n-1}0\) is ruled out by the length-two interior interval beginning at its second interior symbol, where the starting height is zero. Therefore the maximizer is unique. At \(n=2\), both possible phases have one admissible interior interval.

**5. Asymptotics.** The usual Catalan estimate \(C_m\sim4^m/(\sqrt\pi m^{3/2})\) gives \(H_m\sim2mC_m\). Since \(H_{m-1}/H_m\to1/4\), summing the positive geometric tail gives \(\sum_{m<n}H_m\sim(4/3)H_{n-1}\sim(2/3)nC_n\). For rigor, split at a fixed large \(M\); for \(m\ge M\), consecutive ratios are eventually bounded by a fixed number strictly below one, allowing dominated convergence on the reversed index, while the finitely many smaller terms are negligible. The degree average follows from the handshaking identity.

## Verification
Run `python3 verify.py` with the Python 3 standard library. The script generates every Dyck word for semilengths \(1\) through \(10\), constructs the alternating-interval graph, and verifies the exact edge formula and the claimed degree maximum. For semilengths \(1\) through \(8\), it separately constructs every distinct one-deletion ball and verifies equality of the two edge sets, not merely equality of edge totals. It also independently counts positive-height vertices for semilengths \(1\) through \(10\). The observed edge totals are \(0,1,6,27,111,441,1728,6733,26181,101763\). Finite tests corroborate the proof; they are not used to infer its universal quantifiers.

## Relationship to prior work
The Type-A characterization in Cai, Kiah, Nguyen and Yaakobi gives the unrestricted pairwise ambiguity condition. A previously recorded unrestricted \(q\)-ary reconstruction-graph theorem counts edges on **all** words, rather than edges on the Dyck-induced subgraph; taking a ratio or substituting a Catalan vertex count does not determine the induced edges. Frandsen et al. study dynamic membership for Dyck languages, not this edge graph. The total edge counts here **exactly coincide** with OEIS A371965 and the peak total in Baril et al., whose 2024 Corollary 5.4 already gives the same generating function, number sequence, and leading asymptotic. Neither the inspected Catalan-peaks paper nor the indexed sequence identifies these integers as a deletion-confusability edge count or proves the unique maximum-degree Dyck word. Thus the numerical sequence itself is not claimed as new.

## Limitations
No optimum reconstruction-code cardinality, graph independence number, complete degree distribution, or multideletion statement is established. The bijection relies on the published binary Type-A one-deletion intersection characterization. The known matching OEIS entry lowers any claim of novelty for the scalar edge totals; only the interpretation and extremal graph result are proposed as new. Bibliographic coverage cannot rule out unindexed or differently named equivalents, and no independent mathematical audit has been performed.

## References
1. G. S. Frandsen, T. Husfeldt, P. B. Miltersen, I. Rauhe, and S. Skyum, *Dynamic Algorithms for the Dyck Languages*, BRICS RS-95-1, first released 1995-01-11, https://www.brics.dk/RS/95/1/BRICS-RS-95-1.pdf.
2. K. Cai, H. M. Kiah, T. T. Nguyen, and E. Yaakobi, *Coding for Sequence Reconstruction for Single Edits*, arXiv:2001.01376; accessible author version https://yaakobi.net.technion.ac.il/files/2020/07/108_Reconstruction_Edit_ISIT20.pdf.
3. J.-L. Baril, P. E. Harris, K. J. Harry, M. McClinton, and J. L. Ramírez, *Enumerating runs, valleys, and peaks in Catalan words*, arXiv:2404.05672, first released 2024-04-08; full paper https://jl.baril.u-bourgogne.fr/pamkim.pdf, Corollary 5.4.
4. OEIS Foundation, sequence A371965, https://oeis.org/A371965.
5. *Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph*, available at https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-edge-count-of-the-finite-alphabet-two-read-single-deletion--737fed325e91/RESULT.md.
