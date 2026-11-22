# Exact bfloat16 basin spectra of the rational logistic map under two rounding orders

## Finding

For the rational interval map \(K_\mu(x)=\mu x(1-x)/(1+x)\), fix the parameter \(\mu=11/2\) used in the originating article's Figure 7. Let \(R\) be exact bfloat16 rounding to nearest with ties to even; positive and negative zero are identified as one nonnegative zero state. Define
\[
A(x)=R\!\left(\frac{(11/2)x(1-x)}{1+x}\right),\qquad
B(x)=R\!\left(\frac{R\!\left(R((11/2)x)R(1-x)\right)}{R(1+x)}\right).
\]
The inner numerator multiplication and the final division are performed exactly before the indicated rounding. Both maps act on the finite set \(S\) of **all** nonnegative IEEE bfloat16 values in \([0,1]\). There are exactly 16,257 such values.

The complete recurrent cycle spectra and basin sizes are:

| Evaluation | Prime period | Full basin size | Maximum transient to its cycle |
|---|---:|---:|---:|
| Once rounded \(A\) | 1 (zero) | 2 | 1 |
| Once rounded \(A\) | 19 | 16,255 | 74 |
| Staged \(B\) | 1 (zero) | 2 | 1 |
| Staged \(B\) | 2 | 409 | 53 |
| Staged \(B\) | 6 | 5,958 | 64 |
| Staged \(B\) | 21 | 9,888 | 63 |

The two graphs disagree on exactly **1,371 of 16,257** immediate successor edges. In particular, the once-rounded graph has one nonzero recurrent component, but the staged graph has three, with different periods and basins. These statements classify every allowed initial state, not a sample trajectory.

## Assumptions and scope

The underlying exact-real map is \(K(x)=(11/2)x(1-x)/(1+x)\), \(x\in[0,1]\). Its real maximum is \((11/2)(3-2\sqrt2)<1\), so the exact map preserves the interval. The finite maps are **defined solely** by the two displayed arithmetic expression trees, not by a compiler's unspecified optimization choices. All exact constants and all intermediate operations are rational, and only the displayed \(R\) calls round. The formats use bfloat16's one sign bit, eight exponent bits, seven stored fraction bits, gradual underflow, and ties-to-even; zero is counted once. The staged map does not claim to be the unique hardware interpretation of the formula. Both maps' outputs lie in \(S\) under their exact definitions, as independently verified for every input code.

## Proof

**1. Exact state domain.** For each unsigned bfloat16 code \(k\) from hexadecimal `0000` through `3f80`, decode its exact rational value. For exponent field zero the value is \(m2^{-133}\), with integer fraction field \(0\le m<128\). Otherwise, with exponent field \(e\) and fraction field \(m\), the value is \((128+m)2^{e-134}\). These consecutive codes decode to exactly all nonnegative bfloat16 values in \([0,1]\); their count is \(0x3f80+1=16257\).

**2. Exact successor construction.** The attached checker `checks/verify.py` implements two separately specified rational rounding methods. One locates the two neighboring representables and compares exact rational distances, resolving ties by the even stored least-significant bit. The other computes the exact binary exponent, sets the normal or subnormal spacing, and rounds the rational quotient to the nearest even integer. Both algorithms agree on every representable value, each adjacent midpoint across the entire relevant positive table, and every actual intermediate operation in the two maps. Each evaluation therefore generates a mathematically exact successor, including for all subnormal inputs. Every successor is verified to be a member of the enumerated state set.

**3. Complete functional-graph certification.** In a finite deterministic graph, every orbit enters a directed cycle. The checker independently decomposes each of the 16,257-state graphs in two ways: (i) complete forward-path traversal, detecting the first repeated state and propagating component labels and transient distances backward; (ii) indegree-zero peeling followed by residual-cycle enumeration and backward component/distance propagation. Both return identical canonical lists of all recurrent cycles, basin sizes, and maximum preperiod lengths; the displayed table is the exact output. Basin totals are \(2+16255=16257\) for \(A\) and \(2+409+5958+9888=16257\) for \(B\). A direct successor-by-successor comparison gives 1,371 differences. Because the state codes are exhaustively enumerated and every successor has been certified, these finite exhaustive computations prove the complete classification for the defined finite systems.

For unambiguous replay, the SHA-256 digests of the 16-bit little-endian successor indices in increasing starting-code order are `61a5e82b755d2663346b81fce98adced48bacb0933638361e4e29635e8a25d71` for \(A\) and `eb02e69879f027f218499d3e54f21b936d0619cf219b386b5ab312721c106d4b` for \(B\). The two digests supplement, rather than replace, the complete verifiable successor-generation algorithm.

## Verification

Run `python3 checks/verify.py` using only the Python standard library. The command reconstructs the entire state space, checks exact rational rounding with two implementations, recomputes all successors and all cycles with two distinct graph algorithms, checks every listed basin and longest transient, and checks that the two successor lists differ at exactly 1,371 states. It prints `CHECK_OK` followed by the exact cycle codes, basin sizes and maximum transient distances. There is no randomness or floating-point dependency. Finite graph exhaustion is exhaustive **only** for the finite bfloat16 state space; it is not a proof of a continuum invariant measure or of real-map chaos.

## Relationship to prior work

Kumar, Alzabut, Kumari, Rani and Chugh introduce this rational logistic map, analyze fixed points and numerical dynamics, and specifically illustrate \(\mu=5.5\) as a chaotic-trajectory example in Figure 7. That paper's Sections 3--5 discuss trajectories, Lyapunov estimates and empirical entropy, not all-state bfloat16 cycle basins or competing operation-level rounding semantics. Klöwer, Coveney, Paxton and Palmer study periodic-orbit collapse in low-precision logistic and generalized Bernoulli maps, establishing the broader motivation, but their objects are not this rational logistic map at \(\mu=11/2\). Existing exact results about real-valued prime-two, prime-three and prime-four bifurcations of this rational family concern different state spaces and do not determine either finite rounding graph. Previously available finite-precision censuses of the ordinary logistic map and a beta shift likewise do not imply the recorded cycles and basins. The two verified edge lists and the source-motivated parameter supply the specific new finite classification.

## Limitations

The result is conditional on the precisely displayed evaluation orders. Actual processor behavior may use different rounding points, constant conversion, fused operations, flush-to-zero behavior, or distinct formats. No cryptographic-security conclusion follows from the cycle periods. No claim is made for other \(\mu\), alternative sign domains, real-map recurrence, or stochastic rounding. The literature comparison does not exclude unpublished or unindexed matching computations; independent mathematical verification remains outstanding.

## References

1. A. Kumar, J. Alzabut, S. Kumari, M. Rani, and R. Chugh, “Dynamical properties of a novel one dimensional chaotic map,” *Mathematical Biosciences and Engineering* **19** (2022), 2489–2505. DOI: 10.3934/mbe.2022115. First published 7 January 2022; Equation (3.1), Figure 7, Sections 3–5. https://www.aimspress.com/aimspress-data/mbe/2022/3/PDF/mbe-19-03-115.pdf
2. M. Klöwer, P. V. Coveney, E. A. Paxton, and T. N. Palmer, “Periodic orbits in chaotic systems simulated at low precision,” *Scientific Reports* **13** (2023), 11410. DOI: 10.1038/s41598-023-37004-4. https://www.nature.com/articles/s41598-023-37004-4
