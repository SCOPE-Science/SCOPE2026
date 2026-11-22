# Sparse Walsh zeros of undirected Hamiltonian tours: the exceptional orders nine and ten

## Finding

For each integer \(n\ge6\), let \(E_n=E(K_n)\), let \(\mathcal H_n\subseteq\mathbb F_2^{E_n}\) be the binary edge-incidence vectors of **unoriented**, labelled Hamiltonian cycles, each counted once, and put
\[
W_n(S)=\sum_{C\in\mathcal H_n}(-1)^{|C\cap S|},\qquad S\subseteq E_n.
\]
For every \(n\ge6\) and every edge frequency \(S\) with \(|S|\le4\), \(W_n(S)=0\) **if and only if** one of the following holds:

1. \(n=9\), \(|S|=4\), and the graph whose edge set is \(S\), after removing isolated vertices, is a triangle together with an independent edge, or a three-edge star together with an independent edge.
2. \(n=10\), \(|S|=3\), and that graph is a triangle or a three-edge star.

There are exactly \(6{,}300\) such four-edge frequencies at \(n=9\), and exactly \(960\) such three-edge frequencies at \(n=10\). All Walsh multipliers of support degree at most four are nonzero at every other order \(n\ge6\). Consequently, the counting-convolution operator \(f\mapsto\mathbf1_{\mathcal H_n}*f\) is injective on the Walsh band of degrees at most four except for a \(6{,}300\)-dimensional kernel at \(n=9\) and a \(960\)-dimensional kernel at \(n=10\). The corresponding restricted ranks are \(60{,}412\) out of \(66{,}712\) at \(n=9\) and \(163{,}261\) out of \(164{,}221\) at \(n=10\).

In particular, for every \(n\ge11\), all degree-at-most-four Walsh signals can be recovered from their convolution with the Hamiltonian-cycle indicator. This is an exact finite-frequency statement, not a claim that convolution is invertible on the entire cube for these orders.

## Assumptions and scope

All graphs are labelled simple complete undirected graphs. A Hamiltonian cycle and its reversal represent the same incidence vector. Frequencies are arbitrary subsets of edges, and Fourier characters are \(\chi_S(x)=(-1)^{\sum_{e\in S}x_e}\). The transform and convolution are **unnormalized**. \(\mathcal H_n\) contains exactly \(M_n=(n-1)!/2\) vectors. The domain is all integers \(n\ge6\), and frequencies have at most four edges. Isolated vertices in a frequency graph are irrelevant.

## Proof

**1. Exact forced-edge counts.** If a nonempty set of \(j<n\) prescribed edges is contained in a Hamiltonian cycle, each of its components must be a path (including a single edge). For a union of \(b\) such nontrivial paths, contract the paths and arrange the resulting \(n-j\) vertices in a cyclic order, then choose an orientation for each path. This gives
\[
N_n(F)=2^{b-1}(n-j-1)!.
\]
A prescribed edge graph containing a vertex of degree at least three or a cycle of length smaller than \(n\) occurs in no Hamiltonian cycle. As \(|S|\le4<n\), there is no spanning-cycle exception. Expanding \(\prod_{e\in S}(1-2\mathbf1_{e\in C})\) yields
\[
W_n(S)=\frac{(n-1)!}{2}+\sum_{j=1}^{|S|}(-2)^j c_j(S)(n-j-1)!,
\]
where \(c_j(S)\) is the sum of \(2^{b(F)-1}\) over all \(j\)-edge subsets \(F\subseteq S\) that are path forests with \(b(F)\) nontrivial components. Put \(c_j=0\) for \(j>|S|\).

**2. Exhaustive four-edge signature classification.** Every graph with at most four edges has at most eight nonisolated vertices; up to vertex relabelling, it occurs in \(K_8\). An elementary classification by connected components gives the following complete \((c_1,c_2,c_3,c_4)\) table. A path on \(r\) vertices is denoted \(P_r\), the star on \(r\) leaves is \(K_{1,r}\), and disjoint union is \(\sqcup\).

| Number of edges | Graph types, with isolated vertices suppressed | \((c_1,c_2,c_3,c_4)\) |
|---|---|---|
| 0 | empty | \((0,0,0,0)\) |
| 1 | \(K_2\) | \((1,0,0,0)\) |
| 2 | \(P_3\) | \((2,1,0,0)\) |
| 2 | \(2K_2\) | \((2,2,0,0)\) |
| 3 | \(K_3\), \(K_{1,3}\) | \((3,3,0,0)\) |
| 3 | \(P_4\) | \((3,4,1,0)\) |
| 3 | \(P_3\sqcup K_2\) | \((3,5,2,0)\) |
| 3 | \(3K_2\) | \((3,6,4,0)\) |
| 4 | \(K_{1,4}\) | \((4,6,0,0)\) |
| 4 | triangle with pendant edge | \((4,7,2,0)\) |
| 4 | \(C_4\), the five-vertex tree with degrees \((3,2,1,1,1)\) | \((4,8,4,0)\) |
| 4 | \(K_3\sqcup K_2\), \(K_{1,3}\sqcup K_2\) | \((4,9,6,0)\) |
| 4 | \(P_5\) | \((4,9,6,1)\) |
| 4 | \(P_4\sqcup K_2\) | \((4,10,9,2)\) |
| 4 | \(2P_3\) | \((4,10,8,2)\) |
| 4 | \(P_3\sqcup2K_2\) | \((4,11,12,4)\) |
| 4 | \(4K_2\) | \((4,12,16,8)\) |

To see that the graph-type list is complete, connected four-edge graphs are \(C_4\), a triangle with pendant edge, and the three trees on five vertices. The disconnected four-edge graphs comprise the four partitions of four forest edges into component sizes \((3,1),(2,2),(2,1,1),(1,1,1,1)\), where the three-edge component in \((3,1)\) may be a path or star; the remaining disconnected graph is \(K_3\sqcup K_2\). The degree-three table follows in the same way. The first standalone checker independently enumerates all labelled edge subsets in \(K_8\) and confirms exactly these signature sets.

**3. Exact cancellations for bounded \(n\).** For each table row \(c=(c_1,\ldots,c_4)\), evaluate the integer polynomial
\[
Q_c(n):=\frac{2W_n(S)}{(n-5)!}
=\prod_{t=1}^{4}(n-t)+2\sum_{j=1}^{4}(-2)^j c_j\prod_{t=j+1}^{4}(n-t).
\]
Empty products are one. Direct integer substitution for each of the 17 signature rows and every integer \(6\le n\le17\) yields zero only for \(n=9\) with \(c=(4,9,6,0)\) and for \(n=10\) with \(c=(3,3,0,0)\). The table is exhaustive, so this is an exhaustive finite proof for the stated range; the executable checker supplies every summand and exact comparison. For direct confirmation at the two exceptional orders,
\[
W_9(K_3\sqcup K_2)=20160-8\cdot5040+36\cdot720-48\cdot120=0,
\]
\[
W_{10}(K_3)=181440-6\cdot40320+12\cdot5040=0.
\]
The same values hold for the indicated star graphs because their signatures agree. The labelled frequencies number
\[
\binom93\binom62+9\binom83\binom52=6300
\]
and
\[
\binom{10}3+10\binom93=960,
\]
respectively; their two graph shapes are disjoint classes in each count.

**4. Uniform bound beyond the finite check.** A prescribed edge belongs to exactly \((n-2)!\) undirected Hamiltonian cycles. The number having odd intersection with \(S\) is at most the number having at least one edge of \(S\), which is at most \(|S|(n-2)!\). Thus
\[
W_n(S)\ge M_n-2|S|(n-2)!=M_n\left(1-\frac{4|S|}{n-1}\right)>0
\]
for all \(n\ge18\) and \(|S|\le4\). This completes the all-order classification.

**5. Fourier-rank conclusion.** Characters diagonalize convolution on \(\mathbb F_2^{E_n}\), and the eigenvalue at \(S\) is precisely \(W_n(S)\). Since characters are independent and our low-degree support set is invariant under convolution, the kernel dimension is the number of zero multipliers in that band. Summing \(\binom{\binom n2}{j}\) over \(0\le j\le4\) gives the stated exact ranks and dimensions.

## Verification

The self-contained `verify_signatures.py` checks the 17 path-forest signatures by enumerating every edge frequency of degree at most four on eight vertices, evaluates every signature at each order from 6 to 17 exactly, verifies the exceptional multiplicities, and checks the congruences for orders six through eight. The independent `verify_tours.cpp` enumerates all unoriented Hamiltonian tours on nine and ten labelled vertices with fixed start and reversal removal and directly computes signed sums at the two exceptional motifs and four control frequencies. Run:

```sh
python3 verify_signatures.py
c++ -std=c++17 -O2 verify_tours.cpp -o verify_tours
./verify_tours
```

Both checkers passed on the packaged source files. No floating-point arithmetic or probabilistic test enters the proof. For orders above seventeen, the union bound in Step 4 is symbolic rather than extrapolated from finite tests.

## Relationship to prior work

Hamilton-cycle incidence, counting, and signed-cycle existence have been studied extensively; see the cited primary literature. The relevant existing all-order two-adic nonvanishing theorem for certain special vertex orders already covers complete Fourier invertibility at orders six through eight and is **not** claimed as a new contribution here. An earlier exact all-frequency Walsh magnitude census at order nine also supplies a stronger global computation at that one order; this theorem's substantive addition is the uniform degree-four zero classification at **every** order, including the order-ten exception and the absence of sparse zeros for every order at least eleven. An incidence-shattering classification for Hamilton tours describes realization of binary edge assignments, not equality of positive and negative Hamilton-cycle counts. Signed-Hamilton-cycle literature characterizes existence of both signs, not their precise cancellation. The count-and-pack literature uses nonnegative permanent estimates rather than character-balanced enumeration.

## Limitations

The theorem does not classify Walsh zeros of degree five or higher (except by citing older results at specific orders), nor give the complete spectrum or a quantitative inverse bound. Earlier all-frequency calculations at order nine partly dominate isolated statements there; archival priority is subject to unindexed literature and inaccessible material. The proof uses a finite graph-signature table only through four edges, together with an independent symbolic bound for all larger vertex orders.

## References

- A. Ferber, M. Krivelevich, B. Sudakov, *Counting and packing Hamilton cycles in dense graphs and oriented graphs*, arXiv:1212.4667 (first publicly submitted 2012-12-19). https://arxiv.org/abs/1212.4667
- G. Sierksma, *Interchange graphs and the Hamilton cycle polytope*, Discrete Applied Mathematics **81** (1998), 217–224. https://doi.org/10.1016/S0166-218X(97)00086-3
- V. Ejov, J. A. Filar, S. K. Lucas, J. L. Nelson, *Solving the Hamiltonian Cycle Problem Using Symbolic Determinants*, Taiwanese Journal of Mathematics **10** (2006), 327–338. https://doi.org/10.11650/twjm/1500403828
- X. Yan, *Hamiltonian Cycles in Signed and Multisigned Complete Graphs*, arXiv:2502.10612 (2025). https://arxiv.org/abs/2502.10612
