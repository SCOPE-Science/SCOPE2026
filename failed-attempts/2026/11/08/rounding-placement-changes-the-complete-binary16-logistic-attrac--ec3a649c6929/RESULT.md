# Rounding placement changes the complete binary16 logistic attractor census

## Finding

Let \(\mathcal H\) be the 15,361 **nonnegative** IEEE 754 binary16 representable numbers in the closed unit interval, including zero and one, with the two signed zeros identified. Let \(\operatorname{rn}_{16}\) denote round-to-nearest, ties-to-even in binary16, with gradual underflow. Define two deterministic self-maps of \(\mathcal H\):

\[
 S(x)=\operatorname{rn}_{16}\!\left((4x)\,\operatorname{rn}_{16}(1-x)\right),
 \qquad
 U(x)=\operatorname{rn}_{16}\!\left(4x(1-x)\right).
\]

Each product or subtraction inside the outer \(\operatorname{rn}_{16}\) is exact real arithmetic unless a separate rounding operator is displayed. Because multiplication by four is exact for these inputs, \(S\) is the usual binary16 evaluation of \((4x)(1-x)\), with the subtraction rounded before the multiplication; \(U\) rounds the exact polynomial **only once, at the end**. The latter is an explicitly defined correctly rounded polynomial evaluation, not a claim about the operation order of an arbitrary compiler.

The **complete** functional-graph census, counting every member of a cycle in its basin, is:

| Evaluation | Attracting cycle | Period | Basin size | Maximum transient within basin |
|---|---|---:|---:|---:|
| staged \(S\) | zero | 1 | 5,092 | 55 |
| staged \(S\) | \(3/4\) | 1 | 2 | 1 |
| staged \(S\) | other | 40 | 10,267 | 83 |
| one-round \(U\) | zero | 1 | 15,236 | 109 |
| one-round \(U\) | \(3/4\) | 1 | 8 | 7 |
| one-round \(U\) | other | **5** | **117** | 14 |

Each graph has exactly three cycles and no other recurrent state. The two maps have different outgoing edges at precisely **2,774** of the 15,361 states. The maximum time to the first repeated state, across the full domain, is 123 iterations for \(S\) and 110 for \(U\). A complete orbit of the five-cycle of \(U\), given as unsigned binary16 encodings in cyclic order, is `0x3bd1, 0x2dbd, 0x3539, 0x3b09, 0x36ca`. The two common fixed-point encodings are `0x0000` and `0x3a00`.

This is an **exact finite-state theorem**, not an asymptotic claim or a sampling estimate. The staged period-40 orbit and its 10,267-state basin were reported previously; the new claim is the exact one-rounding census and the resulting all-state comparison between the two precise evaluation semantics.

## Assumptions and scope

The domain is exactly the nonnegative half-precision encodings from `0x0000` through `0x3c00` inclusive. Signed zero is a single dynamical state. No negative, NaN, or infinite encodings are admitted. Rounding uses the IEEE 754 binary16 nearest-even rule at all explicitly marked rounding points; denormal numbers are retained (no flush-to-zero); the two functions are defined as above and not by source-language expression syntax. Basins are counted with respect to **uniform counting measure on this discrete state set**, not Lebesgue or the real logistic-map invariant density.

For \(x\in\mathcal H\), the exact polynomial obeys \(0\le 4x(1-x)\le1\). For the staged operation, the intermediate rounded factor can make the exact product slightly exceed one, but every such output still rounds to one in binary16, so both definitions map \(\mathcal H\) into itself. No stochastic rounding or hidden fused operation is permitted.

## Proof

**Step 1: exact encoding.** Scale every state by \(Q=2^{24}\). For a positive binary16 encoding with exponent field \(e\) and fraction field \(f\) (with \(0\le f<1024\)), its scaled integer value is \(f\) if \(e=0\), and \((1024+f)2^{e-1}\) if \(1\le e\le15\). The encodings from `0x0000` through `0x3c00` are strictly increasing, so this formula enumerates exactly all 15,361 states without omissions.

**Step 2: exact rounding.** For nonnegative integers \(p\) and positive \(q\), round the real number \(p/(qQ)\) to the nearest adjacent scaled grid integers, resolving an equal-distance tie by the even binary16 significand. The supplied `CHECK.py` performs the comparisons as exact integer cross-products; it never uses floating-point arithmetic to construct the transition graphs. If a staged result is slightly above one, an exact bound checked at every state places it within the upper half-ulp rounding cell of one.

**Step 3: exact transitions.** If \(X\) is the scaled integer for \(x\), let \(Y\) be the scaled integer for \(\operatorname{rn}_{16}(1-x)\). Then the next staged scaled state is the nearest grid point to \(4XY/Q\); the next one-round scaled state is nearest to \(4X(Q-X)/Q\). These rules generate one integer successor for each of the 15,361 state encodings. `CHECK.py` additionally verifies for all these states that putting an extra binary16 rounding after the product \(x\operatorname{rn}_{16}(1-x)\), then scaling by four, does not change the staged map.

**Step 4: exhaustive functional-graph argument.** Every vertex has exactly one outgoing edge. The checker visits each previously unvisited vertex, follows successors until entering an earlier visited path or its own current path, labels the newly detected cycle if any, and assigns all predecessor-path vertices to its cycle. Every vertex is marked visited once; finite-state termination follows from the 15,361-vertex bound. The graph therefore decomposes uniquely into disjoint basins of all cycles, and the printed basin sizes, periods, and transient maxima are exhaustive. For \(S\), the basin sizes sum to \(5092+2+10267=15361\); for \(U\), they sum to \(15236+8+117=15361\). The precise accepted cycle table and the count of differing outgoing edges are asserted against independently calculated integers in `CHECK.py`.

The certificate is an exhaustive proof for the specified **finite** floating-point state space, not a statement about real-valued orbit dynamics or arbitrary precision.

## Verification

Run `python3 CHECK.py` (Python standard library only) from a directory containing this file and the checker. It reproduces all graph counts and prints `VERIFY_OK exact_integer_full_graphs=2 states_each=15361 edge_comparisons=15361`. The recorded SHA-256 hashes of the complete successor arrays, serialized as little-endian unsigned 16-bit indices, are:

- staged: `300ed95c25d2fe4a9b836b60802d0c6b8af3c9c1c01e0654f895781ea889027c`;
- one-round: `262e0316d1e5e82c3b1c694ecde3dde9b8c6a8a24956d407f6b6b008c2d116af`.

An **independent implementation** in `VERIFY_NUMPY.py` uses NumPy binary16 operations for the staged map and binary64 polynomial evaluation followed by one binary16 cast for the single-round map. For binary16 inputs, the exact product integer needs fewer than 53 binary digits, so the binary64 expression in this check is mathematically exact. It matches **all 30,722 successor entries bit-for-bit**. NumPy is an optional dependency only for this cross-check. The verification report records the actual output markers of both programs.

## Relationship to prior work

Velichko and Pham (2026) analyze exact digital recurrence and forecast degradation for the logistic map at parameter four, using a staged float32 implementation, not the complete binary16 comparison above. Galias (2021) gives systematic functional-graph cycle enumeration for binary32 and binary64 and already notes that algebraically equivalent computational formulas can yield different trajectories; **neither the method nor the qualitative order sensitivity is claimed as new here**. Klöwer and collaborators (2023) investigate float16 logistic-map degradation with deterministic and stochastic rounding, but the accessible text did not establish this all-state staged/one-rounding paired census. Corless and Fillion's 2024 discussion explicitly reports a 40-cycle with a 10,267-state basin for a half-precision logistic map; that staged-side result is **not** new. The new contribution is the exact one-round period-five/117-basin graph, its 15,236-state zero basin, and the 2,774-edge comparison under precisely specified operator semantics.

## Limitations

This is a finite classification at one standard format and one logistic parameter. It does not provide a parameter-continuation theorem, asymptotic formula as precision grows, higher-precision cycle counts, a global statistical statement for continuous initial distributions, or a claim about arbitrary hardware implementations. The general dependence of numerical dynamics on computation order is well established. Historical priority for these **particular paired binary16 counts** remains provisional; the complete 2023 article was not available for line-by-line inspection in the accessible sources, and an unindexed older arithmetic census could exist. Independent audit is not yet performed.

## References

1. A. Velichko and V.-T. Pham, *When More Data Become Less Informative: Finite-Precision Periodicization and Collapse of Forecast-Error Lyapunov Estimates*, arXiv:2608.16120, first public 17 August 2026. https://arxiv.org/abs/2608.16120.
2. Z. Galias, *Periodic Orbits of the Logistic Map in Single and Double Precision Implementations*, IEEE Trans. Circuits Syst. II 68 (2021), 3471–3475. DOI: 10.1109/TCSII.2021.3081604. https://www.zet.agh.edu.pl/~galias/ps/tcasii2021lpublished.pdf.
3. M. Klöwer, P. V. Coveney, E. A. Paxton, T. N. Palmer, *Periodic orbits in chaotic systems simulated at low precision*, Scientific Reports 13 (2023), 11410. DOI: 10.1038/s41598-023-37004-4. https://discovery.ucl.ac.uk/id/eprint/10179144/.
4. R. M. Corless, with N. Fillion, *Floats for Philosophers: A Talk in Three Parts*, August 2024, logistic-map slides 60–62. https://rcorless.github.io/FloatsForPhilosophers.pdf.
