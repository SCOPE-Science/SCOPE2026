# Complement symmetry and almost-Johnson skew-forcing exchanges on the folded five-cube

## Finding
Let \(G\) be the **five-regular Clebsch graph**, also known as the folded five-cube. Its vertices are the sixteen binary four-vectors, encoded by integers from \(0\) to \(15\); vertices \(a,b\) are adjacent precisely when their bitwise XOR is in \(\{1,2,4,8,15\}\). (This is the five-regular graph, **not** its ten-regular complement.) Let \(\mathcal F_G(z)=\sum_{S\subseteq V(G):S\text{ skew forces }G}z^{|S|}\), where **any** vertex, black or white, can turn its unique white neighbor black. Then

\[
\mathcal F_G(z)=6490z^8+9760z^9+7752z^{10}+4352z^{11}+1820z^{12}+560z^{13}+120z^{14}+16z^{15}+z^{16}.
\]

In particular the minimum skew-zero-forcing number is \(Z^-(G)=8\). Its family \(\mathcal B\) of minimum skew-forcing sets has exactly \(6490\) members, is closed under taking the **eight-element complement**, and consists of nine orbits under \(\operatorname{Aut}(G)\), of sizes \(10,160,240,320,480,480,960,1920,1920\).

Let \(\mathcal E\) have \(\mathcal B\) as its vertices, adjacent whenever one selected graph vertex can be replaced by one unselected vertex. This token-jump reconfiguration graph is connected and has \(116320\) edges, with degree distribution

\[
10t^{32}+3200t^{35}+2160t^{36}+1120t^{38}.
\]

It is nonregular but **self-centered**, of radius and diameter both \(8\). If \(S,T\in\mathcal B\), then

\[
8-|S\cap T|\ \leq\ d_{\mathcal E}(S,T)\ \leq\ 9-|S\cap T|.
\]

Equality with the upper bound occurs for exactly \(9120\) unordered distinct pairs, out of \(\binom{6490}{2}\). The collection \(\mathcal B\) is **not** the bases of a matroid: the basis-exchange axiom fails even though its token-jump graph is connected.

## Assumptions and scope
All graphs are finite, simple, undirected. Skew forcing has no requirement that the forcing vertex itself be black. The forcing closure of a black set \(S\) is obtained by repeatedly adding every white vertex that is the sole white neighbor of some vertex. Since each addition permanently decreases the white set and previously available forces remain effective, simultaneous and sequential iterations have the same final closure. A set skew forces if the closure is all sixteen vertices.

The statement concerns the **single finite graph** with the given adjacency, not a claimed formula for all folded hypercubes. All counts refer to labelled subsets of the explicitly labelled vertex set; the nine orbit sizes refer to the full graph automorphism group. A legal token jump changes exactly one black vertex and preserves cardinality eight and the skew-forcing property.

## Proof
**Finite closure characterization and exhaustion.** Represent a subset of the sixteen vertices by an integer mask \(s\in\{0,\ldots,65535\}\). Construct the five-neighbor mask \(A_v\) of each vertex using the five XOR generators. Beginning with \(s\), replace it by

\[
s\ \mathbin{\mathrm{OR}}\ \bigvee_{v:\ |A_v\setminus s|=1}(A_v\setminus s),
\]

until no change occurs. This terminates after at most sixteen strict increases; its fixed point is exactly the skew-forcing closure. The standalone `verify_clebsch.cpp` evaluates all \(2^{16}=65536\) masks and counts forcing masks by their popcount, with no skipped candidates. Its resulting full cardinality distribution is the polynomial displayed above, proving the claimed minimum and number of optima. It also checks directly that the complement of every optimum remains optimal.

**The automorphism action.** The five graph-edge generators have XOR zero, and every four of them are a vector-space basis. Any permutation of these five generators therefore extends uniquely to a linear automorphism of the four-dimensional binary vector space. The sixteen translations and the \(5!\) permutations of generators yield \(1920\) automorphisms. Conversely, fixing the image of a vertex and the permutation of its five neighbors fixes all ten remaining vertices, since each is uniquely the second common neighbor of a distinct pair of those five neighbors. Thus the group has exactly \(1920\) elements. Enumerating their actions on all \(6490\) optima partitions them into the nine asserted orbits; explicit representatives and sizes appear below.

**Exchange metric.** A one-token jump between size-eight subsets replaces exactly one element, so the ambient Johnson metric is \(8-|S\cap T|\), a lower bound for every path in \(\mathcal E\). The verifier builds all and only legal jumps by testing the \(8\cdot8=64\) possible replacement pairs for each optimum and looking up the resulting mask in the complete set of optima. It checks every edge in both directions and sums all degrees, yielding \(116320\) undirected edges and the displayed degree distribution. Breadth-first search from one representative of each of the nine group orbits visits all \(6490\) vertices and gives eccentricity eight and distance excess at most one over the Johnson bound. Symmetry makes these conclusions valid from **every** vertex. The numbers of excess-one targets for the nine representative orbits are \(0,0,0,0,0,0,9,5,0\); multiplying by orbit sizes and dividing the ordered-pair count by two gives

\[
\frac{960\cdot9+1920\cdot5}{2}=9120.
\]

The presence of complement pairs, which have Johnson distance eight, also gives an independent sharp lower bound on the diameter.

**Matroid boundary.** Take the optimal masks `0x037d` and `0x195d`. The element indexed \(5\) is in the first set but not the second; the possible additions from the second set that are not in the first are exactly vertices \(11\) and \(12\). Both candidate exchanges (`0x0b5d` and `0x135d`) stall without any additional force. Hence the matroid basis-exchange property fails.

The complete orbit table uses hexadecimal representatives of the original four-bit vertex-mask convention. The final column counts partners whose exchange distance exceeds the ambient Johnson distance by one.

| Representative | Orbit size | Exchange degree | Excess-one partners |
|---|---:|---:|---:|
| `0x3cc3` | 10 | 32 | 0 |
| `0x033f` | 160 | 38 | 0 |
| `0x069f` | 240 | 36 | 0 |
| `0x166b` | 320 | 35 | 0 |
| `0x037d` | 480 | 38 | 0 |
| `0x06bb` | 480 | 38 | 0 |
| `0x035f` | 960 | 35 | 9 |
| `0x036f` | 1920 | 35 | 5 |
| `0x067b` | 1920 | 36 | 0 |

## Verification
The package contains two standalone, independently written finite checkers. Compile the C++17 implementation with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_clebsch.cpp -o verify_clebsch` and run `./verify_clebsch`. Run the independent Python 3 standard-library implementation with `python3 verify_evenfive.py`.

The first checker uses XOR generators on four-bit vertices, bit-mask parallel forcing, full sixteen-bit mask exhaustion, explicit group transformations and orbit-representative breadth-first search. The second uses the sixteen even-parity five-bit words joined at Hamming distance four, sequential forcing on Python sets, independent coordinate permutations and a separately built token-jump graph. Both enumerate all \(65536\) seeds and both recover the entire forcing polynomial, nine orbit sizes, complementation invariance, degree distribution, edge count, radius, diameter and exactly \(9120\) exceptional metric pairs. Both also verify a matroid basis-exchange failure. These checks ran on the embedded code; the programs include executable assertions for the stated numbers.

For illustration, the first source set `0x035f` and the target `0x0acf` share six vertices, so their Johnson distance is two, yet their legal exchange distance is three. Each of the four possible intermediate one-token jumps for a two-step route fails skew forcing. The complete breadth-first-search certificate checks all pairs via symmetry, not just this example.

## Relationship to prior work
L. M. DeAlba's foundational paper on minimum skew-zero-forcing sets (first public version 6 April 2014) defines this forcing rule and proves results on complete multipartite, bipartite and unicyclic graphs, including a matroid-basis theorem under special hypotheses. The five-regular Clebsch graph is none of those graph classes. Our negative basis-exchange result makes that distinction concrete.

J. Geneson, R. Haas and L. Hogben's zero-forcing reconfiguration work (first posted 1 September 2020) develops token-jump graphs for **ordinary** zero forcing, which requires the forcing vertex to be black. The skew process here is different, so their theorems do not supply this census or its metric.

Related indexed mathematical research describes skew forcing on odd prisms, ordinary zero forcing on the four-cube, perfect-matching flips on the Clebsch graph and identifying/determining or dominating subsets of the Clebsch graph. Those objects or forcing rules differ substantially. The stated numerical values were not recovered from the checked primary results or indexed records. Lack of a matching search hit is **not** proof of universal priority; an unindexed earlier enumeration remains possible.

## Limitations
The theorem is finite and exhaustive, not an infinite folded-cube family theorem. Its proof uses finite enumeration supported by two independent programs rather than a short noncomputational classification. The graph's ten-regular complement, sometimes also called the Clebsch graph, is **not** in scope. The listed orbit-mean excess counts, not a full all-pairs geodesic polynomial, are established. Novelty is assessed against accessible literature and indexed records, not asserted as an absolute first-publication claim. Independent third-party mathematical verification has not been performed.

## References
1. L. M. DeAlba, *Some results on minimum skew zero forcing sets, and skew zero forcing number*, arXiv:1404.1618, first publicly posted 6 April 2014, https://arxiv.org/abs/1404.1618.
2. J. Geneson, R. Haas, and L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220, first publicly posted 1 September 2020, https://arxiv.org/abs/2009.00220.
3. E. W. Weisstein, *Clebsch Graph*, MathWorld, https://mathworld.wolfram.com/ClebschGraph.html (five-regular versus complementary convention).
