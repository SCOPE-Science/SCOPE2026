# Alphabet-relabeling rigidity and exact symmetry counts for de Bruijn cycles

## Finding
Let \(A\) be a labeled alphabet of size \(q\ge2\), let \(\sigma\) be a nonidentity permutation of \(A\), and let \(n\ge1\). A de Bruijn cycle of order \(n\) is a length-\(q^n\) cyclic word containing each word in \(A^n\) exactly once as a cyclic consecutive block. Two cycles differing by rotation are identified. Write \(N_\sigma(q,n)\) for the number of cycles whose symbolwise image under \(\sigma\) is a rotation of the original cycle.

If the cycles of \(\sigma\) do not all have the same length, then \(N_\sigma(q,n)=0\). Otherwise all cycles of \(\sigma\) have a common length \(d\ge2\), and \(q=dm\) for an integer \(m\ge1\). Then
\[
N_\sigma(q,n)=
\begin{cases}
\varphi(d)d^{m-1}(m-1)!,&n=1,\\
T_m((2m-1)!)^m,&n=2,\ d=2,\ m\text{ odd},\\
0,&\text{otherwise},
\end{cases}
\]
where \(T_1=1\) and \(T_m=2^{m-1}m^{m-2}\) for \(m\ge2\). In particular, no ordinary de Bruijn cycle of order at least three is preserved up to rotation by a nontrivial alphabet permutation. For order two, nontrivial relabeling symmetry exists precisely for a fixed-point-free involution on an alphabet of size congruent to two modulo four.

For instance, a fixed-point-free involution on six symbols fixes exactly \(20{,}736{,}000\) distinct order-two de Bruijn cycles up to rotation.

## Assumptions and scope
The permutation \(\sigma\) acts **symbolwise**, without reversing word order. Rotations act on cyclic positions. Every symbol and every length-\(n\) block is distinguished by its actual label. The counting convention is rotation equivalence only, not quotienting by arbitrary alphabet relabelings. The alphabet has at least two symbols and the permutation is not the identity.

## Proof
**1. Uniform cycle lengths are necessary.** A de Bruijn cycle \(S\) of order \(n\) has primitive period \(q^n\): a shorter period would repeat a length-\(n\) block. Suppose \(\sigma(S)=R^tS\), where \(R\) rotates positions. If \(d\) is the order of \(\sigma\), then \(R^t\) has order \(d\), because the alphabet symbols all occur and the cyclic word has primitive period. Thus the induced permutation of the \(q^n\) positions by \(R^t\) consists solely of orbits of length \(d\). Under the unique correspondence between cyclic positions and length-\(n\) blocks, this is the action of \(\sigma\) on \(A^n\). In particular, the constant block \(a^n\) has orbit length equal to the length of the cycle of \(\sigma\) containing \(a\). Hence all symbol cycles have length \(d\).

**2. Quotient walk and voltage.** Assume that \(\sigma\) consists of \(m\) cycles of length \(d\), and label the alphabet \(A=\{(i,h):1\le i\le m,\ h\in\mathbb Z/d\mathbb Z\}\) so that \(\sigma(i,h)=(i,h+1)\). Use the standard de Bruijn directed multigraph: its vertices are length-\((n-1)\) words, and its edges are length-\(n\) words, directed from prefix to suffix. The free \(\sigma\)-action gives a directed quotient \(Q\) with \(q^n/d\) distinctly labeled edge orbits and \(q^{n-1}/d\) vertex orbits for \(n\ge2\). Every quotient vertex has \(q\) outgoing and incoming edges.

Choose each vertex-orbit representative to have phase zero in its first letter. A quotient edge has a well-defined **voltage** \(v\in\mathbb Z/d\mathbb Z\): the edge starting at the chosen source representative ends at \(\sigma^v\) of the chosen target representative. Lifting a closed quotient Euler tour once changes the phase of its starting vertex by the sum \(V\) of all edge voltages, independent of the Euler tour's edge order. The full lifted tour is one Euler cycle of the original graph precisely when \(V\) generates \(\mathbb Z/d\mathbb Z\); otherwise it splits into \(\gcd(V,d)\) cycles. Conversely, if \(\sigma(S)\) is a rotation of a de Bruijn cycle \(S\), its rotation offset has order \(d\) and is a unit multiple of \(q^n/d\); the first \(q^n/d\) edges project to a quotient Euler tour whose lift has generating voltage. These observations give a bijection between symmetry-fixed de Bruijn cycles and quotient Euler tours with generating voltage, both considered up to cyclic edge rotation.

**3. Compute the obstruction.** For \(n\ge3\), a chosen source vertex representative has a first symbol of phase zero and a second symbol of some phase \(h\). Every one of its \(q\) outgoing edges has voltage \(h\), whatever last symbol is appended. Consequently the sum of its outgoing voltages is \(qh=0\) modulo \(d\), and the total voltage is \(V=0\). Since \(d\ge2\), no lift is one Euler cycle.

For \(n=2\), the quotient vertices are the \(m\) symbol-orbits. For each ordered pair of orbits, there are \(d\) quotient edges, one of each target phase \(h\). Their total voltage is
\[
V\equiv m^2\sum_{h=0}^{d-1}h
=m^2\frac{d(d-1)}2\pmod d.
\]
If \(d\) is odd this is zero. If \(d\) is even, it is either zero or the unique element of order two, depending on whether \(m\) is even or odd. It generates the phase group if and only if \(d=2\) and \(m\) is odd.

**4. Count order-one cycles.** Let \(n=1\). The unique rotation corresponding to \(\sigma\) is a shift by \(mr\) positions, with \(r\) any unit modulo \(d\). For a fixed \(r\), the first \(m\) consecutive positions must contain one symbol from each of the \(m\) symbol-orbits. There are \(m!d^m\) indexed words: choose the orbit order and a starting phase for each orbit; the remaining positions are forced. Every such word uses each of the \(q\) symbols once and has exactly \(q\) distinct rotations. Different units \(r\) give disjoint families. Dividing by \(q=dm\) yields \(\varphi(d)d^{m-1}(m-1)!\).

**5. Count order-two cycles.** In the sole permissible case \(d=2\), \(m\) odd, the quotient graph has \(m\) vertices and exactly two distinguished arcs from every vertex to every vertex, including loops. Every quotient Euler tour has odd total voltage and hence lifts to exactly one symmetry-fixed de Bruijn cycle. By the directed BEST theorem, the number of cyclic Euler tours with labeled edges equals the number \(T_m\) of directed in-arborescences at a chosen root times \(\prod_v(\operatorname{outdeg}(v)-1)!\), namely \(T_m((2m-1)!)^m\). For \(m=1\), the empty tree has count one. For \(m\ge2\), the directed matrix-tree cofactor of the Laplacian \(2mI-2J\) is \(T_m=2^{m-1}m^{m-2}\): its nonzero cofactor eigenvalues are \(2\) once and \(2m\) with multiplicity \(m-2\). The quotient-tour/lift bijection completes the enumeration.

## Verification
Run `python3 VERIFY.py` and `python3 CROSSCHECK.py` using only the Python standard library. `VERIFY.py` exhaustively enumerates all binary, ternary and quaternary order-two de Bruijn cycles, checks their symbol-relabeling symmetries, and constructs verified optimal-symmetry cycles for alphabet sizes two, six and ten. `CROSSCHECK.py` independently counts all Euler tours in the quotient multigraph by exact subset dynamic programming for \(m=1,2,3\), obtaining \(1,72,20736000\), and verifies the voltage criterion over a grid of group orders and orbit counts. Computation is corroboration; the proof above covers all positive parameters without finite extrapolation.

## Relationship to prior work
Classical de Bruijn-cycle generation and its Euler-tour correspondence are standard. Etzion's work on binary self-dual sequences treats the special binary complement symmetry and general self-dual sequence families; the binary nonexistence consequence is not asserted to be new. Burris, Motta and Shipman's 2016 unoriented de Bruijn theory studies reversal of block order, a different (antimorphic) operation. Kari and Xu's pseudo de Bruijn sequences likewise use antimorphic involutions and relax complete one-way coverage. Etzion's 2025 account treats general self-dual cyclic sequences (and nonbinary addition), but its inspected account does not give the stated complete classification and exact count of ordinary full de Bruijn cycles under every nonidentity alphabet permutation. The new claim is the all-permutation, all-order fixed-cycle enumerator, not the general Euler/BEST tools or the binary special case.

## Limitations
The result concerns **ordinary complete** de Bruijn cycles, not pseudo or unoriented covers, partial cycles, fixed-weight cycles, or reversal and reverse-complement operations. The count does not classify inequivalent cycles under the full symmetric group on the alphabet. Historical priority remains open to comparison with inaccessible older self-dual-sequence papers; no independent mathematical or priority audit is claimed.

## References
- C. S. Burris, F. C. Motta and P. D. Shipman, *An Unoriented Variation on de Bruijn Sequences*, arXiv:1608.08480v1, first posted 2016-08-30, https://arxiv.org/abs/1608.08480.
- T. Etzion, *Self-dual sequences*, Journal of Combinatorial Theory, Series A **44** (1987), 288–298; author bibliography https://etzion.net.technion.ac.il/publications/.
- L. Kari and Z. Xu, *De Bruijn Sequences Revisited*, AFL 2011; journal version DOI 10.1142/S0129054112400540, https://research.google/pubs/de-bruijn-sequences-revisited/.
- T. Etzion, *Binary and Non-Binary Self-Dual Sequences and Maximum Period Single-Track Gray Codes*, arXiv:2512.09655, first posted 2025-12-10, https://arxiv.org/abs/2512.09655.
- N. G. de Bruijn, *A combinatorial problem*, Koninklijke Nederlandse Akademie van Wetenschappen **49** (1946), 758–764; classical graph/cycle enumeration background.
