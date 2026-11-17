# Distance-invariant majority oscillators on odd-cycle dumbbells

## Finding

Let \(D_{a,b,d}\), for odd integers \(a,b\ge3\) and integer \(d\ge1\), be the labelled graph obtained from two disjoint simple cycles \(C_a\) and \(C_b\) by joining distinguished vertices \(u\) and \(v\) by a simple path with \(d\) edges, internally disjoint from the cycles. Thus \(D_{a,b,d}\) has \(a+b+d-1\) vertices. At each synchronous step, every vertex adopts its open-neighborhood strict-majority binary opinion; on a tie it retains its current opinion. Write \(M\) for this update and let \(N_2(a,b,d)\) be the number of labelled *primitive temporal two-cycle orbits* (two time phases identified, but no spatial or color symmetries identified).

Set \(F_0=0\), \(F_1=1\), \(F_{k+2}=F_{k+1}+F_k\), and let the six-periodic sequence \(t_k\) have residues \((1,1,0,-1,-1,0)\) for \(k\equiv0,1,2,3,4,5\pmod6\). For every odd \(m\ge3\), put
\[
W_m=2\sum_{\substack{j\ge1\\4j\le m-1}}
  \binom{m-2j-2}{2j-1}
=F_{m-2}-t_{m-3}.
\]
Here all empty sums are zero. Then for **all** admissible \(a,b,d\),
\[
\boxed{N_2(a,b,d)=W_aW_b.}
\]
In particular the orbit count is **exactly independent of the length of the joining path**. A primitive two-cycle exists if and only if both odd ring sizes are at least five; the smallest graph exhibiting this mechanism has ten vertices. In every primitive two-cycle, precisely the vertices of the joining path (including its two endpoints) flip every step; every other vertex stays fixed. Along the joining path, the phase-zero opinions alternate in space, so the two endpoint opinions agree for even \(d\) and disagree for odd \(d\).

For fixed \(a,b\) the proportion of uniformly sampled initial states that are *already* in a primitive two-cycle is exactly
\[
\frac{2W_aW_b}{2^{a+b+d-1}},
\]
which halves each time the path is lengthened by one edge. With \(\varphi=(1+\sqrt5)/2\), as both odd \(a,b\to\infty\),
\[
N_2(a,b,d)\sim\frac{\varphi^{a+b-4}}5,
\]
uniformly in the connecting distance because the count does not depend on \(d\).

## Assumptions and scope

All vertices are distinctly labelled. Each cycle is a simple graph, so its length is at least three. The connecting path has one edge if \(d=1\), and contains exactly \(d-1\) degree-two internal vertices otherwise. Its distinguished endpoints each have degree three; all other vertices have degree two. The rule uses simultaneous updates, open-neighbor majority, and tie retention. A *primitive temporal two-cycle* is a pair of distinct configurations \(x,y\) such that \(M(x)=y\), \(M(y)=x\). We count only such initially periodic orbits, not transient states eventually reaching one. No periodicity claim is inferred merely from finite simulations. The classical general eventual-period-at-most-two theorem is acknowledged as background, not part of the new claim.

## Proof

**1. A degree-two flipping vertex forces both neighbors to flip.** Let \(x\leftrightarrow y\) be a primitive temporal two-cycle, and suppose a degree-two vertex \(w\) changes bit. Because the tie-retaining two-neighbor rule is the majority of the two neighbor bits and the current bit, the only way to change is for *both* neighbors to have the opposite opinion at time zero. At time one, the same vertex changes back, forcing both neighbors to have the reverse opinion. Therefore both neighbors flip too, and every edge incident to \(w\) is phase-zero bichromatic.

**2. No non-endpoint ring vertex can flip.** If any degree-two vertex of either odd cycle flips, the rule of Step 1 propagates flipping around the entire cycle, including its endpoint. Phase-zero neighboring opinions would then have to alternate on every edge of that odd cycle, an impossibility. Thus all ring vertices other than \(u,v\) are static. If a nonconstant periodic orbit exists, some connector vertex must flip. An internal connector flip propagates to both endpoints by Step 1. If an endpoint \(u\) flips, its two ring neighbors are static, so its only time-varying input is the next vertex on the joining path, which must also flip; propagation reaches \(v\). The same reasoning applies with the endpoints exchanged. Hence in every primitive two-cycle **all and only** joining-path vertices flip.

**3. Alternation and the endpoint boundary conditions.** Every internal path vertex has degree two and flips, so its two neighbors have bits opposite to its initial bit. At an endpoint, its two ring-neighbor bits are static, say \(p,q\); the third neighbor on the connecting path flips. To make a degree-three strict majority alternate in both directions, one must have \(p\ne q\), in which case the endpoint copies its path neighbor. The endpoint can therefore flip precisely when that path neighbor has the opposite phase-zero bit. This extends spatial alternation along the entire connector, giving the asserted parity relation between \(u\) and \(v\).

**4. Static ring words.** Remove \(u\) from the first odd cycle and read its remaining vertices in cyclic order along the path from one neighbor of \(u\) to the other. The resulting binary word has length \(a-1\). Its endpoints must differ by Step 3. To be fixed in *both* phases while their neighbor \(u\) flips, the first two bits must agree, and the final two bits must agree; otherwise an endpoint of the word would change during one of the two phases. At every other position, a static degree-two vertex changes precisely when it is an isolated singleton between two opposite bits. Therefore the necessary and sufficient condition is: endpoints differ and **every maximal constant run has length at least two**. The identical argument applies independently to the word of length \(b-1\) on the second odd cycle. Conversely, two such words and either choice of the initial bit at \(u\), together with the forced alternating connector, satisfy every update equation in both phases. They reconstruct all primitive temporal two-cycles uniquely as labelled states.

**5. Count and distance invariance.** A word with unequal endpoints has an even number \(2j\ge2\) of maximal constant runs. To have length \(L\), each run must have length at least two; the number of ordered run-length compositions is \(\binom{L-2j-1}{2j-1}\), and the first bit can be chosen in two ways. Consequently the ring of odd length \(m\) has precisely \(W_m\) admissible static words. The two rings can be chosen independently. Choosing the bit at \(u\) in two ways determines every connector bit and the bit at \(v\), so there are exactly \(2W_aW_b\) primitive-two *states*, or \(W_aW_b\) temporal orbits. No extra degree of freedom appears when an internal path vertex is inserted: its bit is forced by alternation. This proves exact invariance with \(d\).

**6. Closed formula, threshold, and asymptotics.** A constant run of length at least two has ordinary generating function \(R(z)=z^2/(1-z)\). Summing an even positive number of runs yields
\[
\sum_{L\ge0} W_{L+1}z^L
=2\sum_{j\ge1}R(z)^{2j}
=\frac{2z^4}{(1-z)^2-z^4}
=\frac{z^2}{1-z-z^2}-\frac{z^2}{1-z+z^2},
\]
where the extension to all positive \(L\) defines the same admissible-word count. The first rational term has coefficient \(F_{L-1}\) for \(L\ge2\), and the second has coefficient \(t_{L-2}\), where \(t\) has the displayed period six. Thus \(W_m=F_{m-2}-t_{m-3}\). For odd \(m=3\), the required length-two word does not exist; for every odd \(m\ge5\), the word consisting of \(m-3\) zeros followed by two ones is admissible. Hence primitive-two orbits exist exactly when \(a,b\ge5\). Binet's formula gives \(W_m=\varphi^{m-2}/\sqrt5+O(1)\), proving the stated product asymptotic. The graph has \(a+b+d-1\) binary sites, which gives the exact initially periodic-state probability and its factor-of-two decay under distance extension.

## Verification

The complete executable source `verify_corridors.cpp` enumerates every binary state for 56 odd-cycle parameter triples with \(3\le a\le b\le9\), \(1\le d\le6\), and at most 20 graph vertices. It independently checks both the count and the exact flipping support. Its recorded output is `corridors_output.txt`.

The separate Python program `verify_corridors_construct.py` enumerates all admissible run words through length 18, reconstructs every predicted primitive-two configuration for eight chosen parameter triples including joining lengths one through seven, directly checks their two consecutive updates, and checks the binomial, rational-generating-function and six-periodic Fibonacci formulas through length 100. Its recorded output is `corridors_construct_output.txt`. Both programs completed successfully. These bounded checks corroborate the infinite-family proof above; they do not substitute for it. To reproduce, compile the C++ source using `g++ -std=c++17 -O2 verify_corridors.cpp -o verify_corridors` and run `./verify_corridors`; execute the Python source using `python3 verify_corridors_construct.py`. Both are standalone and use no external packages.

Selected primitive-two orbit counts: \(N_2(3,5,d)=0\), \(N_2(5,5,d)=4\), \(N_2(5,7,d)=12\), \(N_2(7,9,d)=72\), and \(N_2(9,11,d)=408\), for **every** \(d\ge1\).

## Relationship to prior work

The period-at-most-two property for symmetric finite threshold dynamics is classical [1–3], but gives neither this exact count nor the localization on a path between odd cycles. A published census of a cycle with one pendant vertex [4] already derives the **same single-ring word-count sequence**; this local Fibonacci-and-period-six identity is not claimed as new here. Our statement instead classifies simultaneous oscillation of two odd ring endpoints with an arbitrarily long connecting path, proves there are no other primitive-two mechanisms, and establishes distance invariance of their full product population. An odd singly chorded ring [5] has a different graph topology (two internally disjoint routes between the same two endpoints), with additional one-path and all-vertex flipping mechanisms, and its count cannot directly supply the dumbbell result. Existing bridge-connected clique results [6] find no oscillations when either clique is odd; replacing the cliques with odd cycles changes the mechanism and the onset. A separate study [7] uses the term *dumbbell graph* for cycles connected by paths but studies evolutionary death–birth updates rather than the deterministic majority map and does not furnish this count.

## Limitations

The theorem applies only to two **odd** simple cycles connected by one simple path and to the specified synchronous binary rule. It does not classify even-ring dumbbells, multiple connectors, nonbinary opinions, time-to-attraction, or basin sizes. The generating-function identity for one path word is an already-known ingredient rather than a separately original claim. The main mathematical contribution is the exact joining and distance-invariance theorem. Closely related unindexed graph-threshold literature might affect historical priority; the searches and inspections described in the companion review do not certify absolute priority. Independent external verification has not been performed.

## References

1. E. Goles and J. Olivos, “Periodic behaviour of generalized threshold functions,” *Discrete Mathematics* 30 (1980), 187–189, DOI 10.1016/0012-365X(80)90121-1. Original full text not independently inspected.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, “Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs,” arXiv:1405.2486v1 (first posted 2014-05-11), https://arxiv.org/abs/1405.2486.
3. D. Kaaser, F. Mallmann-Trenn, and E. Natale, “On the Voting Time of the Deterministic Majority Process,” arXiv:1508.03519v1 (first posted 2015-08-14), https://arxiv.org/abs/1508.03519.
4. “One pendant edge preserves majority equilibria but creates Fibonacci-many oscillations,” published mathematical record, identifier published-finding corpus:404ec1da0b60 (proof and formula inspected).
5. “A single chord activates and enumerates majority two-cycles on odd rings,” published mathematical record, identifier published-finding corpus:59a6c7d954ec (proof and all three mechanisms inspected).
6. “Parity-locked majority oscillations and sharp settlement on bridge barbells,” published mathematical record, identifier published-finding corpus:9d6d10116c2e (complete graph-family statement and proof inspected).
7. H. Richter, “Spectral dynamics of guided edge removals and identifying transient amplifiers for death–Birth updating,” *Journal of Mathematical Biology* 87 (2023), Article 3, DOI 10.1007/s00285-023-01937-1 (different update rule).
