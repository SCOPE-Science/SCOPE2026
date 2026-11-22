# An exact Dürer majority basin spectrum with two dynamically isolated layer equilibria

## Finding
Let \(G=GP(6,2)\) be the Dürer graph. Synchronous binary strict-neighbor majority on its twelve labelled vertices has **fifteen distinct attraction-basin sizes**, given by the complete orbit-basin tables below. Every one of its \(4096\) configurations enters a periodic orbit within **five updates**, and this bound is attained by exactly \(96\) states, all ultimately fixed rather than oscillatory. The two non-consensus states consisting of opposite monochromatic outer and inner layers are fixed points whose attraction basins contain **only themselves**. In fact, that isolation property holds for *every* cubic generalized Petersen graph \(GP(n,k)\) with \(n\ge5\) and \(1\le k<n/2\).

The previously known recurrent population of the Dürer graph is \(14\) fixed points and \(184\) primitive temporal two-cycle orbits; **these counts are context, not the new claim**. The exact complete *individual attraction-basin size distribution* is:

| Least temporal period | Basin size | Number of distinct temporal orbits |
|---:|---:|---:|
| 1 | 1 | 2 |
| 1 | 8 | 6 |
| 1 | 13 | 4 |
| 1 | 736 | 2 |
| 2 | 2 | 42 |
| 2 | 4 | 24 |
| 2 | 6 | 27 |
| 2 | 10 | 24 |
| 2 | 12 | 12 |
| 2 | 14 | 12 |
| 2 | 16 | 3 |
| 2 | 21 | 24 |
| 2 | 26 | 2 |
| 2 | 70 | 12 |
| 2 | 92 | 2 |

The exact number of starting states with first periodic-entry time \(t\) is:

| \(t\) | Eventually period 1 | Eventually period 2 | Total |
|---:|---:|---:|---:|
| 0 | 14 | 368 | 382 |
| 1 | 192 | 1086 | 1278 |
| 2 | 360 | 780 | 1140 |
| 3 | 528 | 240 | 768 |
| 4 | 384 | 48 | 432 |
| 5 | 96 | 0 | 96 |

The sharp dynamical identity is \(F^7=F^5\); for example, the state encoded by integer \(79\) visits \(79,263,70,257,64,0\), first becoming periodic after its fifth update. Each unanimous state attracts \(736\) starts; these are the two largest individual basins. Under the full twelve-element dihedral graph automorphism group, the recurrent orbits form **seven fixed-point** and **31 primitive-two-cycle** geometric classes.

## Assumptions and scope
The outer vertices of \(GP(n,k)\) are \(u_i\) and the inner vertices \(v_i\), indexed by \(i\in\mathbb Z/n\mathbb Z\). Edges are \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+k}\). For the finite census \(n=6,k=2\), labels \(0,\ldots,5\) represent \(u_i\) and \(6,\ldots,11\) represent \(v_i\); bit \(j\) of an integer state gives its vertex color. At every simultaneous update, a vertex becomes one if at least two of its three **open neighbors** are one, and zero otherwise. No self-feedback or retained-tie rule is needed: degree three makes ties impossible.

For an initial state \(x\), its *first periodic-entry time* is the least \(t\ge0\) for which \(F^t(x)\) already lies on a periodic orbit. An *attraction basin* of a temporal orbit \(\mathcal O\) is the set of labelled initial states whose forward iterates eventually enter \(\mathcal O\). Two phases of one primitive temporal two-cycle count as **one orbit and one shared basin**; other configurations are never identified by spatial symmetry except in the separately reported geometric-class counts. Each outer–inner vertex pair has four possible binary assignments, and the whole labelled graph has exactly \(2^{12}=4096\) configurations.

## Proof
**1. Structural isolation, valid throughout the generalized-Petersen family.** Consider the state with every outer bit one and every inner bit zero. It is fixed because each outer vertex has two outer-one neighbors, and each inner vertex has two inner-zero neighbors. Suppose an arbitrary input has \(A\) outer ones and \(B\) inner ones, but its next state is that polarized fixed configuration. Summing the \(n\) required outer-output-one majority inequalities gives \(2A+B\ge2n\). Summing the \(n\) required inner-output-zero inequalities gives \(A+2B\le n\). The second inequality implies \(2A+B\le2n-3B\), so \(B=0\) and then \(A=n\). Thus the polarized state is its **sole predecessor**, and therefore its own entire attraction basin. Global color complementation commutes with majority and gives the other isolated fixed state. The argument uses only that each layer is two-regular and the spokes form a perfect matching; it applies for all \(n\ge5\), \(1\le k<n/2\).

**2. Complete finite functional-graph proof on Dürer.** Construct \(F\) explicitly by the three neighbors of each of the twelve vertices, as in the accompanying `verification/majority_gp.py`. Every state \(x\in\{0,\ldots,4095\}\) has exactly one successor \(F(x)\). Initialize each state's indegree, remove every indegree-zero state recursively, and retain the disjoint directed cycles; in reverse peeling order, attach each discarded state to the orbit of its already-classified successor, incrementing the entry time by one. This finite process visits every state exactly once for classification, and the directed functional-graph lemma guarantees no missing or double-counted orbit/basin. Direct integer checks then produce precisely the two tables above. In particular the orbit population is \(14+184=198\), and the basin-weight sum equals exactly \(4096\). The distribution of cycle lengths is \(14\) of length one and \(184\) of length two, with no longer cycle. The largest entry time is five, and its full population is \(96\), all eventually on fixed points.

**3. Independent reconstruction and graph identification.** The separate standard-C++17 program `verification/majority_lcf.cpp` builds the graph from the twelve LCF shifts \((-4,5,2,-4,-2,5,-5,2,4,-2,-5,4)\), classifies all states by first-repetition path tracing rather than peeling, and derives exactly the same tables. Its explicit relabelling from LCF coordinates to \(GP(6,2)\) coordinates is the permutation \((0,1,7,11,9,3,2,8,6,10,4,5)\), whose edge preservation the program checks. Thus the independent encodings cover the **same** Dürer graph and not merely two graphs of the same order.

**4. Geometric classes.** Vertices on the inner layer each lie in a triangle, whereas no outer vertex does. Hence every automorphism preserves the two layers; its restriction to the outer six-cycle lies in the dihedral group of order twelve, and each outer dihedral symmetry extends uniquely through the spokes. The Python program applies these twelve permutations to all recurrent configurations, reducing a two-cycle to an unordered pair of its two phases. It obtains seven fixed and 31 two-cycle geometric classes. Its separate Burnside calculations give fixed-state incidence total \(84=12\cdot7\) and two-cycle incidence total \(372=12\cdot31\), confirming the quotient counts.

## Verification
Use only the complete source files supplied with this result. From the directory containing this document, execute `python3 verification/majority_gp.py`, then `g++ -std=c++17 -O2 -Wall -Wextra verification/majority_lcf.cpp -o majority_check` and `./majority_check`. Both implementations construct their own adjacency representations and evolve **all** 4096 states. The Python implementation separately verifies the full automorphism group and the Burnside counts. Each program independently checks the exact per-period first-entry histogram, individual basin-size multiplicities, sharp entry time, and consensus-basin sizes. These are exhaustive **finite** arguments, not projections from sampled states; they assert no all-size census beyond the separately proved polarization-isolation lemma. The output transcript in `verification/replay.txt` records successful checks, but the actual source logic is the certificate.

## Relationship to prior work
Goles and Olivos established eventual period at most two for finite symmetric threshold systems, and Benjamini, Chan, O'Donnell, Tamuz and Tan (arXiv:1405.2486v1, 11 May 2014) state and discuss that theorem. Neither specifies the Dürer attraction-basin populations. Published generalized-Petersen results titled *Ninth-degree spin sectors and an entropy gap in majority dynamics on generalized Petersen graphs* and *An equilibrium–oscillation entropy reversal on generalized Petersen graphs* already determine all-size **fixed-point and immediate two-cycle counts** on \(GP(n,2)\), including the \(n=6\) counts \(14\) and \(184\). Those are not claimed novel here. The latter publication explicitly excludes basin and transient-entry classification from its scope. A dodecahedral majority census concerns \(GP(10,2)\), whose numerical attraction structure does not imply the \(GP(6,2)\) basin census. A published truncated-tetrahedral/cuboctahedral comparison concerns different twelve-vertex cubic graphs, not Dürer. The present contribution is **basin sizes, first-entry times, spatial orbit classes and a general isolation argument** that are not consequences of the previously published recurrent-count formulas alone.

## Limitations
The complete basin census and sharp five-update claim are proved only for \(GP(6,2)\), not for every generalized Petersen graph; the broader assertion concerns the two polarized singleton basins only. The basin counts depend on the specified simultaneous, open-neighbor, binary majority rule and on labelled initial configurations. The proof is a complete finite exhaustive algorithm supplemented by the symbolic isolation lemma, not a concise scalar closed formula for arbitrary circumference. Published search and inspected primary texts do not establish absolute historical priority against an unindexed computation or unexamined special-purpose table. No independent external validation has been performed.

## References
1. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, L.-Y. Tan, *Convergence, Unanimity and Disagreement in Majority Dynamics on Unimodular Graphs and Random Graphs*, arXiv:1405.2486v1 (first public 11 May 2014), https://arxiv.org/abs/1405.2486.
2. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1.
3. *An equilibrium–oscillation entropy reversal on generalized Petersen graphs*, publicly available mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-an-equilibrium-oscillation-entropy-reversal-on-generalized-peter--e1d2b1ea8d39.
4. *Ninth-degree spin sectors and an entropy gap in majority dynamics on generalized Petersen graphs*, publicly available mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-ninth-degree-spin-sectors-and-an-entropy-gap-in-majority-dynamic--81296e8da636.
5. *Dodecahedral majority dynamics: an exact recurrent, basin and symmetry census*, publicly available mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-dodecahedral-majority-dynamics-an-exact-recurrent-basin-and-symm--095dfb0decea.
6. *Dürer graph*, graph reference, https://en.wikipedia.org/wiki/D%C3%BCrer_graph (graph identification only, not evidence for the dynamical census).
