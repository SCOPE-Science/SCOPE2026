# Cubic-contact bitangent hexads: tetrad extensions and a connected exchange graph

## Finding

Let \(C\subset\mathbb P^2_{\mathbb C}\) be a very general smooth plane quartic. A *cubic-contact hexad* is an unordered six-set of its bitangents whose twelve contact points lie on a plane cubic. Partition the hexads into class I (no syzygetic triads) and class II (eight syzygetic triads). The known class sizes are \(1008\) and \(5040\), respectively; those sizes and the distinction between classes are not new.

**Tetrad extension classification.** For each unordered four-set \(T\) of the \(28\) bitangents, let \(e_i(T)\) be the number of cubic-contact hexads of class \(i\) containing \(T\). The complete spectrum is

| \((e_{\mathrm I},e_{\mathrm{II}})\) | Number of tetrads | Intrinsic criterion |
|---|---:|---|
| \((0,0)\) | 315 | All four contact divisors lie on a conic (a syzygetic tetrad). |
| \((3,3)\) | 5040 | No syzygetic triad among the four bitangents. |
| \((0,4)\) | 15120 | Exactly two syzygetic triads among the four. |

No fourth extension type occurs.

**Complete cross-hexad intersection numbers.** For a fixed hexad \(H\) of class \(i\), let \(N_{ij}(r)\) count class-\(j\) hexads \(H'\) satisfying \(|H\cap H'|=r\), including \(H'=H\) when \(i=j\) and \(r=6\). These numbers depend only on \(i,j,r\), not on the chosen \(H\):

| Fixed class \(i\) | Other class \(j\) | \(r=0\) | \(r=1\) | \(r=2\) | \(r=3\) | \(r=4\) | \(r=5\) | \(r=6\) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| I | I | 152 | 540 | 225 | 60 | 30 | 0 | 1 |
| I | II | 1005 | 2100 | 1470 | 420 | 45 | 0 | 0 |
| II | I | 201 | 420 | 294 | 84 | 9 | 0 | 0 |
| II | II | 996 | 2124 | 1449 | 428 | 42 | 0 | 1 |

**Connected exchange geometry.** Form a bipartite graph with all \(6048\) cubic-contact hexads as vertices, and join a class-I hexad to a class-II hexad when they share exactly four bitangents (thus two bitangents are exchanged). This graph is **connected**, has exactly \(45360\) edges, and is biregular with degrees \(45\) on class I and \(9\) on class II. Graph connectivity concerns changes of the selected bitangents on a *fixed* quartic; it does **not** assert a deformation between the topologically distinct line arrangements.

## Assumptions and scope

The curve is complex, smooth, nonhyperelliptic of genus three, and taken sufficiently general so all \(28\) bitangents are ordinary and no three bitangents concur. A bitangent \(L\) cuts out twice its effective contact divisor \(D_L\) of degree two, so \(2D_L\sim K_C\). The familiar bijection between bitangents and odd theta characteristics is used. The term *syzygetic triad* means that the six contact points from three bitangents lie on a conic; *syzygetic tetrad* means the eight contact points of four bitangents lie on a conic. The graph is on unlabeled six-subsets of the fixed \(28\)-element bitangent set, not on isomorphism classes of curves or families of embedded arrangements.

## Proof

**Geometric reduction.** Choose an even theta characteristic \(\theta_0\) and identify the theta-characteristic torsor with \(V=J(C)[2]\cong\mathbb F_2^6\), with quadratic parity form
\[
q(a_1,a_2,a_3,b_1,b_2,b_3)=a_1b_1+a_2b_2+a_3b_3\pmod 2.
\]
The \(28\) bitangents correspond precisely to the anisotropic vectors \(O=\{v\in V:q(v)=1\}\). In this coordinate system the class of \(D_L-\theta_0\) is its vector \(v_L\).

For six distinct bitangents \(L_1,\dots,L_6\), their twelve points lie on a cubic exactly when
\[
\sum_{i=1}^6D_{L_i}\sim 3K_C
\quad\Longleftrightarrow\quad
v_{L_1}+\cdots+v_{L_6}=0\text{ in }V.
\]
The first equivalence holds because canonical embedding identifies plane cubics with \(H^0(C,3K_C)\): the exact sequence \(0\to\mathcal O_{\mathbb P^2}(-1)\to\mathcal O_{\mathbb P^2}(3)\to\mathcal O_C(3K_C)\to0\) has vanishing first cohomology on the left. The second follows from \(2\theta_0\sim K_C\) and cancellation of six copies of \(\theta_0\). Because all twelve contact points are distinct, a cubic containing them cannot have a repeated line component, so the resulting cubic is reduced.

Similarly, three distinct odd characteristics with vectors \(u,v,w\) form a syzygetic triad exactly when \(q(u+v+w)=1\); in this case the complementary effective degree-two theta characteristic fills out the fourth bitangent on the contact conic. A four-set is syzygetic precisely when its four vectors sum to zero. These equivalences also follow from the classical theta-characteristic correspondence as stated in the references.

**Exact finite certificate.** The remaining statements are finite theorems about the explicitly specified quadratic space \((V,q)\), not probabilistic or sample-based extrapolations. The complete standalone checker `artifacts/verify_hexads.py` contains the following exhaustive steps, with assertions on every intermediate classification:

1. Enumerate all \(64\) vectors, select exactly \(28\) satisfying \(q=1\), and check that for each nonzero \(s\), exactly \(12\) odd vectors \(v\) have \(v+s\) odd (six unordered pairs).
2. Enumerate every one of \(\binom{28}{6}=376740\) six-set, retain precisely those of vector sum zero, then count their syzygetic triads by checking all \(20\) triples. Exactly \(1008\) retained sets have zero such triads, and \(5040\) have eight.
3. Form the full incidence relation between every retained hexad and its \(15\) tetrads. Independently visit all \(\binom{28}{4}=20475\) tetrads and count extensions by class. The three displayed profiles are exhaustive; the checker also verifies them against the zero-sum and syzygetic-triad criteria for *every* tetrad.
4. For **each** of the \(6048\) hexads, count intersections of sizes \(0\) through \(6\) with **all** \(6048\) hexads and verify all four rows of the stated intersection table. This verifies uniformity, not just representative cases. The impossibility of intersection size five also follows immediately by subtracting the zero-sum relations for two hexads.
5. Build the cross-class four-overlap graph directly from tetrad containment (a separate procedure from the intersection-spectrum loop). Check every degree, count edges, and perform a breadth-first traversal from one vertex; it reaches all \(6048\) vertices. Therefore the graph is connected.

All operations are comparisons, XOR, population counts, finite combinations, and exact integer counts. The loops cover the entire finite domains as specified. No classification or connectivity claim rests on a finite sample or an external solver.

## Verification

Extract `artifacts/verify_hexads.py` from this package without altering its contents and run `python3 artifacts/verify_hexads.py` in Python 3. The program has no third-party dependencies, carries all finite parameters explicitly, and prints `VERIFY_OK` only if all assertions succeed. The complete search checks \(376740\) candidate hexads, \(20475\) tetrads, all ordered pairs of the \(6048\) retained hexads, and full graph connectivity.

## Relationship to prior work

Bannai and Tokunaga (2026) introduce a new construction of the two distinct cubic-contact hexad families and identify their syzygetic-triad patterns (zero versus eight); this work does not claim those discoveries. Shimada (2022) gives a detailed orbit decomposition of all six-bitangent subsets, including orbit sizes \(1008\) and \(5040\), but its table concerns **individual** marked six-subsets. Bannai and Ohno (2020) study the two-graphs of arrangements on one selected six-subset, not the pairwise intersections of *distinct cubic-contact hexads*. Bergvall (2023) explains theta characteristics and the \(315\) syzygetic tetrads, without the cubic-contact hexad extension incidence.

The contribution here is the exact tetrad-to-hexad extension spectrum, the entire two-class hexad intersection table, and the connected biregular cross-class exchange graph. Those conclusions are not implied by the published single-hexad counts alone; each is independently computed from the theta-characteristic model. The standard quadratic-space description does permit recomputation of all numbers, so specialist historical priority checking remains appropriate.

## Limitations

The result concerns one very general complex quartic at a time; it does not assert anything about real bitangents, degenerating quartics, moduli-space components or continuous deformations between topologically distinct arrangements. The combinatorial enumeration is a complete proof for the specified finite symplectic model but does not independently prove the classical theta-characteristic dictionary cited above. A broader historical source could contain equivalent, implicitly computable incidence numbers; no assertion of absolute priority or independent certification is made.

## References

1. S. Bannai and H. Tokunaga, *A curve of genus 2 over C(t) and hexads of bitangents to a smooth quartic*, arXiv:2610.38071v1 (first public 2026-10-27), Introduction and Section 4, especially Lemma 4.1. https://arxiv.org/abs/2610.38071
2. I. Shimada, *Zariski multiples associated with quartic curves*, Journal of Singularities 24 (2022), 169–189, Sections 8–9 and Table 9.1; arXiv:2209.11938. https://arxiv.org/abs/2209.11938
3. S. Bannai and M. Ohno, *Two-graphs and the embedded topology of smooth quartics and its bitangent lines*, Canadian Mathematical Bulletin 63 (2020), 802–812, especially Sections 3–4. DOI:10.4153/S0008439520000053.
4. O. Bergvall, *Arithmetic and topology of classical structures associated with plane quartics*, European Journal of Mathematics 9, article 117 (2023), especially Section 3.6. DOI:10.1007/s40879-023-00711-3.
5. I. Dolgachev, *Classical Algebraic Geometry: A Modern View*, Cambridge University Press (2012), Chapter 6.
