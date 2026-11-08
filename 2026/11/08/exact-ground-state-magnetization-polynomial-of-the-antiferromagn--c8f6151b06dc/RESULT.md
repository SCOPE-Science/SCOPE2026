# Exact ground-state magnetization polynomial of the antiferromagnetic Ising model on the regular 24-cell

## Finding
Let \(G\) be the ordinary edge graph of the regular four-dimensional \(24\)-cell. For the nearest-neighbor, zero-field classical Ising antiferromagnet with fixed uniform coupling \(J>0\), its ground energy is
\[E_0=-32J.\]
With total magnetization \(M(\sigma)=\sum_{v\in V(G)}\sigma_v\), let \(g_m\) count the configurations with \(E(\sigma)=E_0\) and \(M(\sigma)=m\). The complete ground-state magnetization polynomial is
\[\boxed{\sum_m g_m z^m=948+672(z^2+z^{-2})+264(z^4+z^{-4})+48(z^6+z^{-6})+3(z^8+z^{-8}).}\]
In particular \(\sum_m g_m=2922\). Exactly \(64\) of the graph's \(96\) bonds are antialigned in every ground state; the other \(32\) are frustrated. The entropy of the finite zero-temperature ground-state ensemble is \(k_{\mathrm B}\log(2922)\), and its entropy per spin is \(k_{\mathrm B}\log(2922)/24\).

The structural part of the statement is an exact local characterization: a spin configuration minimizes energy if and only if, in each of eight naturally defined six-vertex octahedra, one complete opposite pair is spin up and a *different* complete opposite pair is spin down. The third pair may be homogeneous or mixed.

## Assumptions and scope
Take the vertex set
\[V=\{s e_i+t e_j:1\le i<j\le4,\ s,t\in\{-1,+1\}\}\subset\mathbb R^4.\]
Two distinct roots \(v,w\) are adjacent when \(v\cdot w=1\). This gives a simple, eight-regular graph with \(24\) vertices and \(96\) edges. At every vertex assign an Ising spin \(\sigma_v\in\{-1,+1\}\). The Hamiltonian is
\[E(\sigma)=J\sum_{\{v,w\}\in E}\sigma_v\sigma_w,\qquad J>0.\]
There are no fields, defects, additional couplings, spatial limits, or thermal-limit assertions. Replacing \(J\) by \(1\) merely fixes energy units; the exact ground-state counts do not depend on its positive magnitude.

For each coordinate index \(i\in\{1,2,3,4\}\) and sign \(s\in\{-1,+1\}\), define
\[O_{i,s}=\{v\in V:v_i=s\}.\]
The six vertices of \(O_{i,s}\) form an induced octahedral graph \(K_{2,2,2}\): each of the other three coordinate indices labels one nonadjacent opposite pair, consisting of its two possible signs.

## Proof
**1. Eight edge-disjoint octahedra.** If \(v\cdot w=1\) for distinct roots \(v,w\), they share precisely one nonzero coordinate with the same sign. They therefore belong to exactly one common signed-coordinate set \(O_{i,s}\), and within that octahedron to different opposite pairs. Conversely, two vertices in different opposite pairs of the same \(O_{i,s}\) have dot product \(1\). Hence the \(96\) edges partition into eight copies of the twelve-edge octahedral graph, and
\[E(\sigma)=J\sum_{i=1}^4\sum_{s=\pm1} E_{i,s}(\sigma),\]
where \(E_{i,s}\) is the local octahedral sum in units of \(J\).

**2. Sharp local lower bound.** Group an octahedron's six spins into its three opposite pairs and write their pair sums as \(a,b,c\in\{-2,0,2\}\). The local energy is
\[E_{i,s}=ab+ac+bc.\]
Directly checking the \(27\) possible ordered triples gives
\[E_{i,s}\ge-4,\]
with equality precisely when at least one of \(a,b,c\) equals \(+2\) and a *different* one equals \(-2\). One can verify this without numerical approximation: if both signs occur, the third pair sum cancels between them and the energy is \(-4\); otherwise no product sum is below zero. Therefore \(E(\sigma)\ge-32J\), with equality if and only if all eight local coexistence conditions hold.

**3. Attainability and extreme magnetization.** Partition the four coordinate indices into two unordered pairs in any of the three perfect matchings. Assign spin down to all four roots supported on each of these two coordinate pairs, and spin up to the other sixteen roots. Each \(O_{i,s}\) then has one complete down pair and two complete up pairs, so \(E=-32J\). Global spin reversal gives opposite magnetization. The lower bound is therefore attained. The local rule forces at least two up and two down spins per octahedron. Every spin is counted in exactly two signed-coordinate octahedra, so there are at least eight spins of each sign globally and hence \(|M|\le8\). In the equality case, each octahedron has exactly one complete minority-spin opposite pair, forcing the two coordinate signs to match a common partner; the induced choices give a perfect matching of the four coordinate indices. Thus the \(|M|=8\) degeneracy is three for each sign. This endpoint count is also compatible with the published \(24\)-cell independence-set numbers; it is not claimed as an independently new invariant.

**4. Complete magnetization census.** For the minority-spin set \(S\) of cardinality \(k\), let \(e(S)\) denote its number of induced graph edges. The eight-regularity identity
\[|\partial S|=8k-2e(S),\qquad E/J=96-2|\partial S|=96-16k+4e(S)\]
shows that a ground state with \(8\le k\le12\) must have
\[e(S)=4k-32\in\{0,4,8,12,16\}.\]
The previously published independence-set table addresses only the first value \(k=8\), \(e(S)=0\). The remaining coefficients are established by an *exhaustive exact integer computation* with the included standalone file `verify_24cell_ising.cpp`. The algorithm constructs the twenty-four signed roots in the stated canonical order and explicitly constructs the eight three-pair octahedra. For each of the \(2^{24}=16{,}777{,}216\) binary spin vectors, represented by a unique unsigned integer mask, it tests the eight coexistence conditions and increments the exact integer counter indexed by \(M=24-2\operatorname{popcount}(\mathrm{mask})\). Each vector is tested once; no probabilistic sampling, truncation, symmetry-orbit assumption, or unproved extrapolation is involved. The resulting counts for magnetizations \(0,\pm2,\pm4,\pm6,\pm8\), respectively, are \(948,672,264,48,3\) for each specified sign (with zero counted once). All other coefficients vanish by the local counting bound.

As an independent implementation-level cross-check, the same program enumerates all \(2^{24}\) configurations by Gray code, updating the *original edge Hamiltonian* and the magnetization after each flipped spin. Its per-magnetization ground-energy multiplicities agree exactly with the separately evaluated local-condition census. The program also checks the octahedral edge partition on all \(\binom{24}{2}=276\) unordered vertex pairs. Those finite exhaustive computations are the proof of the remaining specific integer coefficients, supported by the structural equivalence from Steps 1–3.

**5. Frustrated bonds and entropy.** Write \(A\) for the number of antialigned bonds and \(F\) for aligned bonds. Since \(A+F=96\) and \(E_0/J=F-A=-32\), every ground state has \(A=64\), \(F=32\). For a uniform zero-temperature ensemble over all ground configurations, the finite entropy is the logarithm of the total number of states as stated.

## Verification
Compile and run `verify_24cell_ising.cpp` with GCC or Clang in C++17 mode (the program uses their integer bit-count intrinsics), for example:

```sh
g++ -O3 -std=c++17 -Wall -Wextra -pedantic verify_24cell_ising.cpp -o verify_24cell_ising
./verify_24cell_ising
```

The verifier checks every graph edge and nonedge against its signed-coordinate partition (\(276\) comparisons), runs two distinct exhaustive configuration enumerations (\(16{,}777{,}216\) assignments each), checks all magnetization coefficients and ground energies, and independently reconstructs the published independent-set face vector as a control. On success it prints `VERIFY_OK`. The presence of code alone is not a proof of an infinite claim: the mathematical claim here has a *finite* domain of exactly \(2^{24}\) spin configurations, and the loops visit that entire domain.

## Relationship to prior work
Yu's 2015 article on antiferromagnetic Ising models on the eleven Archimedean lattices motivates the study of geometrical frustration and exact or numerical ground-state entropy, but concerns two-dimensional lattice families and does not analyze the finite regular four-dimensional \(24\)-cell. MathWorld's *24-Cell* entry documents the standard root coordinates, its \(24\) vertices, \(96\) edges, and octahedral cells; those underlying geometric facts are not new.

A separately published calculation, *The 24-cell graph independence complex is a mixed wedge of 31 two-spheres and 21 three-spheres* (published-finding corpus, 2026), enumerates the independent-set face vector of the *same* graph, with counts \((1,24,180,488,474,216,84,24,3)\). That published table covers the enumeration of independent sets, including the maximum independent sets; it is explicitly **not** a new claim here. Independent-set counts only record \(e(S)=0\); the other magnetization sectors of this ground-state problem require the exact induced-edge counts \(e(S)=4|S|-32>0\). Independent-set counts alone do not determine these positive-edge counts. The present finding additionally provides the local octahedral energy rule and the complete *zero-field ground-state magnetization polynomial*. Saito and Yamamura (2022) also study spins on the *same regular 24-cell*, but the publicly accessible abstract explicitly specifies continuous headless spins interacting by a twist-preference potential, not the binary antiferromagnetic Ising Hamiltonian. The full 2022 paper could not be examined in the available public sources, so only this material-read comparison is asserted. Their 2023 follow-up studies a different infinite 24-cell honeycomb with a twelve-neighbor local graph. No priority claim is made over hypothetical unindexed tables of maximum cuts, full Ising polynomials, or equivalent exact antiferromagnetic enumerations.

## Limitations
The conclusion applies to exactly the defined \(24\)-vertex regular polytope graph with uniform nearest-neighbor, classical two-state, zero-field antiferromagnetic coupling. The exhaustive integer calculation is feasible here because the graph is finite; it is not an infinite-lattice formula or evidence of a thermodynamic phase transition. Fields, anisotropic couplings, quantum spin dynamics, random disorder and finite-temperature partition coefficients are outside the claim. Historical originality remains subject to specialist comparison against possible precomputed graph-Ising and max-cut tables; independent scientific validation has not been conducted.

## References
1. U. Yu, *Ising antiferromagnet on the Archimedean lattices*, Physical Review E **91** (2015), 062121, publicly published 17 June 2015. DOI: https://doi.org/10.1103/PhysRevE.91.062121 . Full open manuscript: https://arxiv.org/pdf/1606.08191 .
2. E. W. Weisstein, *24-Cell*, Wolfram MathWorld, https://mathworld.wolfram.com/24-Cell.html .
3. *The 24-cell graph independence complex is a mixed wedge of 31 two-spheres and 21 three-spheres*, published-finding corpus, published 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-24-cell-graph-independence-complex-is-a-mixed-wedge-of-31-tw--f4b41c9ffb3d .
4. K. Saito and Y. Yamamura, *Small Spin Clusters Mimicking a Temperature-Induced Phase Transition: Spins on Vertices of Regular Octahedron and Icositetrachoron*, Journal of the Physical Society of Japan **91** (2022), 104603, https://doi.org/10.7566/JPSJ.91.104603 . The abstract is accessible at https://chem.tsukuba.ac.jp/kazuya/kazuya/spin_twist.html .
5. K. Saito and Y. Yamamura, *Three-Step Ordering of Classical Headless Spins Preferring Twists on Icositetrachoric Honeycomb*, Journal of the Physical Society of Japan **92** (2023), 054003, https://doi.org/10.7566/JPSJ.92.054003 .
