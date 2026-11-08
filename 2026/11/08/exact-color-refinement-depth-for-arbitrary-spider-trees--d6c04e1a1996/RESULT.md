# Exact color-refinement depth for arbitrary spider trees

## Finding

Let \(T\) be a finite simple *spider tree*: there is exactly one vertex \(c\) of degree at least three, and deleting \(c\) leaves \(k\ge3\) paths, with lengths in edges \(a_1,\ldots,a_k\ge1\). Let \(L\) be the largest **distinct** length and, if it exists, let \(B\) be the second-largest distinct length. Run ordinary uncolored one-dimensional Weisfeiler--Leman color refinement, with round zero the uniform partition. Define \(s(T)\) to be the minimum nonnegative integer \(t\) for which the partition at round \(t\) equals the partition at round \(t+1\). Then

\[
s(T)=\begin{cases}
\lceil L/2\rceil,&\text{if all arm lengths coincide},\\
\max\{\lceil L/2\rceil,B+1\},&\text{otherwise}.
\end{cases}
\]

Every round-\(t\) color class for \(t\ge1\) has an explicit description by truncated distances to the branching center and to the leaf of the vertex's arm. In particular, the stable color partition is precisely the automorphism-orbit partition.

The appearance of the *second-largest distinct* length is essential: adding one edge to a single arm of a spider with three arms of length \(m\) changes the stabilization time from \(\lceil m/2\rceil\) to \(m+1\), for every \(m\ge1\).

## Assumptions and scope

All graphs are finite, simple, undirected, and initially uncolored. An arm length counts edges from the unique vertex of degree at least three to a leaf. Arm multiplicities may be arbitrary, but at least three arms are required. Color refinement is the exact simultaneous update

\[
\chi_{t+1}(v)=\bigl(\chi_t(v),\,\{\!\{\chi_t(w):w\sim v\}\!\}\bigr),\qquad \chi_0(v)=0.
\]

Colors may be renamed injectively in each round. The number of *strict* rounds is the last index at which a split occurs, not the number of calls including an extra no-change test. Equivalently \(s(T)=\min\{t:\mathcal P_t=\mathcal P_{t+1}\}\). No claim is made about joint color refinement across different graphs or the minimum quantifier rank of a graph-identifying sentence.

## Proof

**Step 1: Explicit colors at every round.** For a noncentral vertex \(v\), let \(d(v)\ge1\) be its distance from \(c\), and let \(e(v)\ge0\) be its distance from the leaf on the same arm. For integers \(t\ge1\) write

\[
\theta_t(v)=\bigl(\min\{d(v),t\},\min\{e(v),t\}\bigr).
\]

We prove that two noncentral vertices have equal colors after \(t\) rounds if and only if their \(\theta_t\)-pairs agree; the center has a color not used elsewhere.

At \(t=1\), vertices have colors according to degrees: the center has degree \(k\ge3\), the leaves have degree one, and all remaining vertices have degree two. The three cases are exactly distinguished by the pairs \(\theta_1\) and the singled-out center.

Assume the assertion for round \(t\). The color at round \(t+1\) consists of the old color and the multiset of old neighbor colors. For every noncentral vertex the neighbors are the predecessor along its arm (or the center when \(d=1\)) and, if \(e>0\), the successor along its arm. A predecessor different from the center has distance coordinates \((d-1,e+1)\); a successor has coordinates \((d+1,e-1)\). The center has its already unique color. Consequently, the old color and old-neighbor-color multiset depend only on \(\theta_{t+1}(v)\): truncating each of these neighbor coordinates at \(t\) is determined by the coordinates of \(v\) truncated at \(t+1\).

Conversely, if two vertices have different \(\theta_t\), they are already differently colored. Suppose their \(\theta_t\)-pairs agree but their \(\theta_{t+1}\)-pairs differ. A new distinction must be that one center distance equals \(t\) while the other exceeds \(t\), or that one leaf distance equals \(t\) while the other exceeds \(t\). In the first case exactly the former vertex has a neighbor whose center-distance coordinate truncated at \(t\) is \(t-1\) (when \(t=1\), the neighbor is the uniquely colored center); the latter does not. In the second case exactly the former has a neighbor whose leaf-distance coordinate truncated at \(t\) is \(t-1\); the latter does not. These are distinctions in the multiset of round-\(t\) neighbor colors. Thus the new colors differ. This closes the induction.

**Step 2: When the partition stabilizes.** At any round \(t\ge1\), the center is separate and the noncentral classes are the fibers of \(\theta_t\). The full untruncated pairs \((d,e)\) are precisely the automorphism orbits: equality entails equality of arm length \(d+e\) and position \(d\), while permutations among equal-length arms realize all such equivalences.

Within an arm of length \(a\), different positions have equal truncated pairs at round \(t\) exactly when at least two positions have both \(d\ge t\) and \(e\ge t\). Such positions exist at depths \(d=t,\ldots,a-t\); their number is \(\max\{0,a-2t+1\}\). Therefore positions on the same arm become fully separated precisely by \(t\ge\lceil a/2\rceil\). Simultaneously separating positions on every arm requires \(t\ge\lceil L/2\rceil\).

For two arms of unequal lengths \(a<b\), their leaves have the same truncated pair \((t,0)\) whenever \(t\le a\). Thus they cannot be separated before round \(a+1\). At round \(t=a+1\), any vertex on the shorter arm has first coordinate \(d<t\). A vertex on the longer arm with the same first coordinate must have the same \(d\), but its second coordinate is strictly larger than the shorter arm's \(a-d<t\). Hence every orbit on the shorter arm is now distinguished from every orbit on the longer arm. The required separation time across such a pair is exactly \(a+1\). Taking the maximum over unequal lengths yields \(B+1\), the largest of the smaller two distinct lengths plus one, if unequal lengths exist.

The least round at which every orbit is a separate color class is therefore the maximum stated in the theorem. Automorphism invariance prevents further splitting, so this is the stabilization round \(s(T)\). In every earlier round at least one orbit pair is still merged, and Step 1 guarantees a later split; hence stabilization cannot occur earlier. This proves all assertions.

## Verification

Run `python3 verify_spider.py` with Python 3 and its standard library. The program independently builds each spider graph, executes simultaneous 1-WL updates, and compares the resulting vertex partitions against both the explicit truncated-distance classes at each round and the predicted stabilization time. It also checks the final orbit partition directly from arm-length/position data. No randomized test or precomputed result file is used as proof.

The reproducible run checks all unordered length multisets with \(3\) to \(6\) arms and each length from \(1\) to \(9\): \(165+495+1287+3003=4950\) instances. Forty-eight larger, separately chosen boundary instances with lengths up to \(35\) are also checked. The recorded output ends with `VERIFY_OK cases=4998`.

## Relationship to prior work

Krebs and Verbitsky (2014) analyze universal covers and color-refinement depth in general, without a fixed-spider two-distinct-length formula in the inspected sections. Arvind, Köbler, Rattan, and Verbitsky (2015) define color refinement and establish broad structural and isomorphism-recognition results, observing that trees are amenable. Their definitions and results do not by themselves give the exact stabilization time for spiders. Kiefer and McKay (2020) study the iteration number and prove sharp global worst-case bounds; those bounds do not imply the arm-length formula above. The present theorem concerns the local, per-input stabilization time on a natural family, not the general maximum at a fixed order.

## Limitations

The result requires a spider with at least three arms and a *unique* branching vertex. It is not asserted for arbitrary trees, forests, colored initial partitions, or joint comparison of two graphs. The finite verifier tests only specified finite parameter ranges; the unrestricted theorem follows from Steps 1 and 2. No independent audit has been performed. Historical-priority assessment cannot rule out unindexed or differently formulated earlier special-case results.

## References

1. A. Krebs, O. Verbitsky, *Universal Covers, Color Refinement, and Two-Variable Counting Logic: Lower Bounds for the Depth*, arXiv:1407.3175, first posted 2014-07-11, https://arxiv.org/abs/1407.3175.
2. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 2015-02-04, https://arxiv.org/abs/1502.01255.
3. S. Kiefer, B. D. McKay, *The Iteration Number of Colour Refinement*, arXiv:2005.10182, first posted 2020-05-20, https://arxiv.org/abs/2005.10182.
