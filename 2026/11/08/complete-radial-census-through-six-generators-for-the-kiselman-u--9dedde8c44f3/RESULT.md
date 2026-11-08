# Complete radial census through six generators for the Kiselman ultrametric

## Finding
For the Kiselman monoid \(K_n\) with \(1\le n\le6\), let \(f_n=a_n a_{n-1}\cdots a_1\) be its zero element. Let \(d_n\) be the ultrametric defined by deleting initial intervals of generator labels, as in Andrenšek (2026). Denote the radial sphere multiplicities by \(s_{n,r}=|\{x\in K_n:d_n(x,f_n)=r\}|\), for every integer \(0\le r\le n\). The **complete exact radial census** is:

| \(n\) | \((s_{n,0},s_{n,1},\ldots,s_{n,n})\) |
|---:|:---|
| 1 | \((1,1)\) |
| 2 | \((1,2,2)\) |
| 3 | \((1,5,7,5)\) |
| 4 | \((1,18,39,39,18)\) |
| 5 | \((1,115,434,611,434,115)\) |
| 6 | \((1,1710,13170,27106,27106,13170,1710)\) |

For **each** \(1\le n\le6\), the positive-radius sphere counts in this table satisfy the *finite checked symmetry* \(s_{n,r}=s_{n,n+1-r}\) for \(1\le r\le n\). No palindromicity theorem or inequality for arbitrary \(n\) is claimed.

## Assumptions and scope
The monoid is given by the presentation
\[
K_n=\langle a_1,\ldots,a_n\mid a_i^2=a_i,\ a_i a_j a_i=a_j a_i a_j=a_i a_j\ (1\le j<i\le n)\rangle.
\]
For \(0\le r\le n\), let \(\partial_{[r]}\) delete every occurrence of \(a_1,\ldots,a_r\). The distance is
\[
d_n(x,y)=\min\{r\in\{0,\ldots,n\}:\partial_{[r]}(x)=\partial_{[r]}(y)\}.
\]
This is the specific finite ultrametric introduced in [1]; its metric properties are prior work. We classify only the multiset of distances to the distinguished zero \(f_n\), not pairwise distances between arbitrary elements, and only for \(n\le6\).

## Proof
We use the known **unique canonical-word theorem** for \(K_n\) [2,3]. A word on the alphabet \(\{1,\ldots,n\}\) represents a canonical element exactly when, between every pair of consecutive occurrences of the same letter \(i\), there are both a letter smaller than \(i\) and a letter larger than \(i\). In particular, different canonical words represent different elements, and all elements have one. We neither reprove nor claim novelty for this standard normal-form theorem.

Here is a *finite exhaustive proof*, supported by the complete standalone enumerator `verify_sphere_census.py` and its recorded output. Beginning with the empty word, append a letter \(i\) only if its previous occurrence, when present, is separated from the new occurrence by at least one lower and at least one higher label. Since every obstruction concerns the latest pair of the same label, no invalid prefix can be extended to a canonical word. Conversely, every canonical word has only canonical prefixes and therefore occurs exactly once in this breadth-first generation. The enumerator consequently lists **all and only** canonical representatives. For each \(n\le6\), the exact generated orders are \(2,5,18,115,1710,83973\), agreeing with the established Kiselman monoid order sequence [3]. Equality with the order sequence is an independent consistency check, not the proof of exhaustiveness; exhaustiveness follows from the prefix argument and canonical theorem.

To compute each distance, start with level \(\ell=n\) and read the word from left to right, decrementing \(\ell\) by one precisely when the next generator label equals \(\ell\). The final \(\ell\) equals \(d_n(x,f_n)\) by Andrenšek's exact right-multiplication level rule [1, Theorem 5.10]. This rule applies to **every** word, so the procedure is valid on the canonical representatives. Tallying the resulting levels yields exactly the table above; the code exhibits the complete loops, elementary integer predicates, and asserted values.

As a second, different computation, the standalone script independently enumerates the right-multiplication closure of the identity by appending each generator and normalizing using the two elementary semigroup reductions: when two consecutive \(i\)'s enclose only smaller letters delete the latter, and when they enclose only larger letters delete the former. Every reduction strictly decreases word length. The resulting set is compared *element by element*, not just by cardinality, against the direct canonical-language enumeration for all six sizes. Each word's greedy level is additionally compared against the least \(r\) for which normalization of the word with all labels \(\le r\) deleted equals the descending word \(n,n-1,\ldots,r+1\). This is exactly the deletion definition of \(d_n(x,f_n)\); the two methods agree on every one of the \(85823\) separately examined canonical representatives across \(n=1,\ldots,6\). The explicit comparisons of the resulting integer rows establish all finite equalities and the stated finite positive-radius symmetry, without extrapolation to larger \(n\).

## Verification
Run `python3 verify_sphere_census.py` using Python 3 (standard library only), from the directory containing this file. The script requires neither a network connection nor external datasets. It generates complete direct canonical languages, an independently normalized multiplication closure, and the two level determinations; asserts that they agree; and prints one exact sphere row and a SHA-256 of the sorted canonical words for each \(n\). The accompanying `verification_output.txt` contains its observed successful output. All \(85823\) canonical words are covered. The maximal case involves exactly \(83973\) elements, hence the finite enumeration is exhaustive *for the stated range*. It neither proves any \(n=7\) count nor any all-\(n\) symmetry.

## Relationship to prior work
Andrenšek [1], published April 28, 2026, introduced \(d_n\), proved the right multiplication rule for its level, characterized its balls, and identified the extreme sphere cardinalities \(s_{n,1}=s_{n,n}=|K_{n-1}|\). Those results, the underlying normal forms, and the overall monoid orders are **not new**. In particular, the published integer sequence \(|K_n|\) [3] yields the row *sums*, not the interior partitions computed here. The new result is the complete **radius-by-radius** exact finite census through six generators, especially the previously unreported interior coefficients \(39,434,611,13170,27106\) as appropriate to degree, and the checked positive-radius reflection in all six rows. The April 2026 primary manuscript's Section 7 gives only the two endpoint sphere formulas; no comparable interior table was found in checked primary text or targeted searches. Historical priority of a differently indexed table remains unverified.

## Limitations
The claim is **finite** and its proof depends on a cited canonical-word theorem and an executable exhaustive enumeration. The symmetry of the positive radii is asserted only for the six enumerated sizes. A general symmetry theorem is neither proved nor claimed. No closed formula for interior radii at arbitrary \(n\) is given. The count of \(22263378\) elements in \(K_7\) [3] explains the meaningful computational cutoff at six generators, but is not a proof that further enumeration is impossible. A prior unindexed table with the same radius counts would supersede the novelty claim. Independent mathematical audit has not been performed.

## References
1. Luka Andrenšek, *Dynamics, Random Products, and Ultrametric Geometry in Kiselman's Semigroup*, arXiv:2604.25892v1 (first publicly posted April 28, 2026), Sections 5–7. https://arxiv.org/abs/2604.25892 ; accessible full text: https://www.researchgate.net/publication/404282016_Dynamics_Random_Products_and_Ultrametric_Geometry_in_Kiselman's_Semigroup .
2. Ganna Kudryavtseva and Volodymyr Mazorchuk, *On Kiselman's semigroup*, Yokohama Mathematical Journal **55** (2009), 21–46, including canonical forms; cited in [1].
3. OEIS A125625, *Number of elements in the semigroup of type K_n*, with the canonical-word characterization attributed to Mazorchuk and order table. https://oeis.org/A125625 .
4. Riccardo Aragona and Alessandro D'Andrea, *Normal form in Hecke-Kiselman monoids associated with simple oriented graphs*, Algebra and Discrete Mathematics **30** (2020), 161–171; arXiv:1904.10745. https://arxiv.org/abs/1904.10745 .
