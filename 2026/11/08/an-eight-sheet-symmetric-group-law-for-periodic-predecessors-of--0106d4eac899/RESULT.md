# An eight-sheet symmetric-group law for periodic predecessors of a nonlinear cellular automaton

## Finding

Let \(F_N\) be the binary cellular automaton on the cyclic ring of length \(N\), with
\[
(F_Nx)_i=x_i+x_{i+3}+x_{i+1}(1+x_{i+2})x_{i+4}\pmod 2,
\]
where all subscripts are cyclic and all algebra inside this formula is over \(\mathbb F_2\). For \(N\ge2\), let \(H_{N,j}\) count targets \(y\in\mathbb F_2^N\) with exactly \(j\) distinct cyclic predecessors. Then for each \(j\in\{0,1,\dots,8\}\),
\[
\lim_{N\to\infty}\frac{H_{N,j}}{2^N}
 =\frac{\binom8j\,!(8-j)}{8!},
\]
where \(!r\) denotes the number of derangements of \(r\) objects. More explicitly, the nine limiting probabilities, for \(j=0,1,\ldots,8\), are
\[
\frac{1}{40320}(14833,14832,7420,2464,630,112,28,0,1).
\]
The convergence is exponentially fast: there are constants \(C>0\) and \(0<\rho<1\), independent of \(N\), such that the absolute error of every displayed fraction is at most \(C\rho^N\). Consequently the image of \(F_N\) occupies a fraction tending to \(25487/40320\) of all targets. No cyclic target of any length \(N\ge2\) has exactly seven predecessors.

## Assumptions and scope

The alphabet is \(\mathbb F_2\). Spatial indices are cyclic, ring size \(N\) is an arbitrary integer at least two, and every target of length \(N\) has equal weight in the limiting frequency. A predecessor is a cyclic length-\(N\) binary configuration, not an arbitrary bi-infinite configuration. The result concerns one application of the local rule, not temporal periodic points or iterate fibers. All limits are as the ring length tends to infinity through the positive integers.

## Proof

**1. Reverse local transition.** For each target symbol \(e\in\{0,1\}\), introduce a map \(R_e\) on four-bit states by
\[
R_e(a,b,c,d)=(e+c+a(1+b)d,\ a,b,c).
\]
These maps are defined using Boolean arithmetic. If \((a,b,c,d)=(x_{i+1},x_{i+2},x_{i+3},x_{i+4})\), applying \(R_{y_i}\) gives \((x_i,x_{i+1},x_{i+2},x_{i+3})\). Each \(R_e\) is a deterministic map; it is not a permutation of all sixteen states because the first reconstructed bit need not recover the discarded fourth bit.

**2. Four invariant eight-element sheets.** Define \(S_{a,b}=R_aR_b(\mathbb F_2^4)\) as a *set of images of all states*. Here and below, composition acts from right to left. The sixteen-state calculation gives the following images (four-bit states encoded as integers between zero and fifteen):

| \((a,b)\) | \(S_{a,b}\) |
|---|---|
| \((0,0)\) | \((0,2,5,6,9,11,12,15)\) |
| \((0,1)\) | \((0,2,4,6,9,11,13,15)\) |
| \((1,0)\) | \((1,3,4,7,8,10,13,14)\) |
| \((1,1)\) | \((1,3,5,7,8,10,12,14)\) |

The images have eight rather than sixteen states; the claimed restricted bijections follow from their exact listed images. Specifically, for each \(a,b,e\in\{0,1\}\), direct substitution verifies
\[
R_e:S_{a,b}\longrightarrow S_{e,a}
\]
is bijective. (This is an eight-case table of permutations of eight entries; the accompanying program regenerates it.) Ordering each \(S_{a,b}\) increasingly supplies canonical ranks \(0,\ldots,7\).

**3. Finite permutation extension.** Consider the four-vertex directed graph with vertex \((a,b)\) and two arrows indexed by \(e=0,1\),
\[
(a,b)\xrightarrow{e}(e,a).
\]
Give each arrow the rank permutation obtained in Step 2. For every cyclic target \(y\), its reverse reading of symbols gives a unique anchored, length-\(N\) closed walk in this graph. The number of cyclic predecessors is the number of fixed points of the product of its arrow permutations. To see this, start with a four-bit input window and successively reconstruct the preceding bits with the \(R_e\). Closing the window is equivalent to obtaining the same four-bit state after one full tour; the invertible eight-sheet restriction accounts for every closed tour. This statement is verified directly against independent enumeration for \(2\le N\le13\).

**4. Full permutation monodromy.** At vertex \((0,0)\), the closed label words \(0\) and \(100\) give, in canonical sheet ranks, the permutations
\[
\alpha=(0,4,1,5,6,2,3,7),\qquad
\beta=(1,0,3,6,4,5,7,2).
\]
The complete closure under composition of these two explicit permutations has cardinality \(40320=8!\). The finite calculation uses breadth-first enumeration of permutations represented by eight-entry integer tuples, beginning with the identity; no probabilistic assumption is involved. Therefore the monodromy group is the full symmetric group \(S_8\). The same calculation certifies that \(\alpha\) has order six, while the closed label word \(10000\) has permutation order seven. The two lifted closed-walk lengths six and thirty-five are coprime.

**5. Primitive extension and equidistribution.** Form the finite directed graph whose vertices are \((v,g)\), with \(v\) a base vertex and \(g\in S_8\), and whose arrows multiply \(g\) on the left by the arrow's rank permutation. From any base vertex, two labels lead to the root \((0,0)\), while two appropriate labels lead from the root to any prescribed base vertex. Since positive root loops generate the entire finite group \(S_8\), the extended graph is strongly connected. The two closed walks from Step 4 imply that its period divides both six and thirty-five, so it has period one. Thus its nonnegative adjacency matrix is primitive. Its indegrees and outdegrees are both two, so its stationary distribution is uniform on the \(4\cdot40320\) vertices. Finite-state Perron–Frobenius theory yields exponentially fast convergence of the normalized path counts. In particular, for every \(g\in S_8\), the fraction of cyclic length-\(N\) targets whose monodromy is \(g\) tends exponentially to \(1/40320\).

**6. Fixed-point law.** Exactly \(\binom8j\,!(8-j)\) permutations in \(S_8\) have exactly \(j\) fixed sheet labels. Applying Step 3 and the uniform group limit from Step 5 gives the claimed formula. The table follows by inclusion–exclusion for derangements. A permutation of eight elements cannot fix exactly seven; hence that multiplicity is absent for every finite ring, not just asymptotically.

## Verification

The standalone `verify.py` reconstructs every reverse transition, all four eight-element subsets and eight arrow permutations, checks the two explicit monodromy generators and their closure of size \(40320\), and checks the coprime cycle lengths. Independently, for every length from two through thirteen, it enumerates every cyclic input and every cyclic target, computes direct fiber sizes, and checks agreement with the fixed-point count of the corresponding permutation. This covers \(16380\) distinct target words. It also verifies the nine derangement numerators. The expected terminal line is:

`VERIFY_OK group_order=40320 lifted_cycle_lengths=6,35 cyclic_targets=16380 limit_numerators=14833,14832,7420,2464,630,112,28,0,1`

Run `python3 verify.py` with Python's standard library. The exponential convergence is derived from a proved primitive finite graph; it is not deduced from the finite enumerations. No explicit optimal mixing constant is calculated.

## Relationship to prior work

Haugland, Larsen, Omland and Rustad introduce the exact five-neighbor rule and prove its open and locally eventually onto behavior, including its generic eight-to-one property on bi-infinite configurations. The present finding does not claim these established properties as new; it analyzes a different invariant, the distribution of preimages of *finite cyclic targets* as the ring size grows. Mariot, Leporati, Dennunzio and Formenti give general de Bruijn procedures for computing periods and multiplicities of preimages of an individual spatially periodic target; the full symbolic limiting distribution and the symmetric-group mechanism for this particular nonlinear rule are not stated in the portions inspected. The reverse-state method shares this established finite-graph vocabulary.

## Limitations

The conclusion applies to the specified local rule, the uniform distribution on finite cyclic target words and one-step fibers only. It does not classify the full exact histogram at each finite ring length or the spectrum of spatially primitive predecessors. The existence of exponential convergence is established, not a sharp numerical rate. Although relevant sources and the known general finite-state method were compared, exhaustive historical priority and independent external validation are not established.

## References

1. Jan Kristian Haugland, Nadia S. Larsen, Tron Omland, Henrikke G. Rustad, *Locally eventually onto cellular automata*, arXiv:2610.33131v1, first submitted 2026-10-23. https://arxiv.org/abs/2610.33131
2. Luca Mariot, Alberto Leporati, Alberto Dennunzio, Enrico Formenti, *Computing the Periods of Preimages in Surjective Cellular Automata*, Natural Computing 16 (2017), 367–381. DOI:10.1007/s11047-016-9586-x. Author-posted version: https://lucamariot.org/files/papers/mldf_naco_2017_postprint.pdf
3. Classical finite-state Perron–Frobenius theorem for primitive nonnegative matrices and the classical rencontres (fixed-point) enumeration of permutations.
