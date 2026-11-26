# Complete bfloat16 attractor collapse under intermediate rounding of a self-parameterized logistic map

## Finding

The published self-parameterized logistic construction at its maximal external control has the exact real expression
\[
f(x)=\left(\frac{197}{50}+\frac{x}{25}\right)x(1-x),\quad 0\leq x\leq1.
\]
Let \(S\) be the complete set of 16,257 distinct nonnegative bfloat16 numbers in \([0,1]\). Let \(R\) mean exact rounding to nearest representable bfloat16, with midpoint ties sent to the even low mantissa bit. Define **different arithmetic evaluation rules for this same real polynomial**:
\[
A(x)=R\!\left[\left(\frac{197}{50}+\frac{x}{25}\right)x(1-x)\right],\qquad
B(x)=R\!\left[R\!\left(\frac{197}{50}+\frac{x}{25}\right)\,R\!\bigl(x(1-x)\bigr)\right].
\]
Every multiplication, addition and subtraction not enclosed by an \(R\) is mathematically exact. The two self-maps of \(S\) have the following **complete**, not sampled, cycle/basin censuses. A basin includes all states eventually entering its cycle, including the cycle itself.

| Evaluation rule | Exact primitive cycle length | Basin cardinality | Maximum preperiod |
|---|---:|---:|---:|
| Once rounded \(A\) | 1 (zero) | 2 | 1 |
| Once rounded \(A\) | 5 | 2,026 | 77 |
| Once rounded \(A\) | 22 | 14,229 | 87 |
| Gain and kernel rounded \(B\) | 1 (zero) | 2 | 1 |
| Gain and kernel rounded \(B\) | 20 | 16,255 | 83 |

Exactly **2,205** of the 16,257 one-step edges differ between \(A\) and \(B\). The two nonzero cycle basins of \(A\), of sizes 2,026 and 14,229, together form the single period-twenty basin of \(B\). This basin consists of all representable states strictly between zero and one. The basin of the zero fixed point remains \(\{0,1\}\) in both maps.

## Assumptions and scope

The external control is exactly one, the bias is exactly \(0.975\), and the feedback coefficient is exactly \(0.01\), hence the real formula shown above. The finite state space is the bfloat16 encodings \(0,1,\ldots,\mathtt{0x3f80}\), representing \([0,1]\), with **positive zero only**. Negative zero is not a distinct state. No NaNs or infinities lie in \(S\). Rounding operations are exactly those explicitly displayed; this theorem does not equate \(B\) to an unspecified compiler-generated or FPGA instruction sequence, nor does it interpret exact rational coefficients as a rounded bfloat16 expression by default.

For normal nonnegative codes \(u\), put \(E=\lfloor u/128\rfloor\), \(m=u\bmod128\); the corresponding real number is \((128+m)2^{E-134}\), while subnormal codes \(0\leq u<128\) represent \(u2^{-133}\). The finite-state maps are well-defined because the exact unrounded transfer value and its staged product lie in \([0,1]\) after rounding, as checked exhaustively and also bounded from the displayed gain/kernel ranges.

## Proof

**Step 1: exact arithmetic and rounding.** Encode every bfloat16 value as an integer ratio. To round a positive rational, either (i) binary-search the sorted complete finite bfloat16 table and compare exact midpoint distances, or (ii) find its binary exponent exactly, scale to the 7-bit fraction lattice and perform nearest-even integer division. The two procedures agree on every input required by either state map. Consequently the successor arrays for all codes \(0\leq u\leq\mathtt{0x3f80}\) are exact, independent of host floating-point operations.

**Step 2: complete directed graph.** The complete integer successor arrays define directed graphs in which every vertex has exactly one outgoing edge. Each weakly connected component of a finite functional digraph has exactly one directed cycle. One traversal algorithm follows each unvisited vertex's orbit until an already labeled vertex or repeated vertex appears, and labels the full tail. A second algorithm removes all indegree-zero vertices recursively, enumerates the remaining directed cycles, and reinstates removed vertices in reverse order. Both procedures exhaust every one of the 16,257 vertices and agree independently on each vertex's eventual cycle and tail depth.

**Step 3: certified result.** In the first graph, the nonzero cycles have exactly the following **sorted hexadecimal bfloat16 state codes**:

- Period five: `3dbb 3ea8 3ee5 3f5f 3f7a`.
- Period twenty-two: `3d3d 3d7b 3dd9 3e0a 3e32 3e68 3e8c 3ebf 3ed9 3eec 3f03 3f11 3f2b 3f31 3f49 3f59 3f61 3f6d 3f77 3f79 3f7c 3f7d`.

In the second graph the unique nonzero cycle has period twenty and sorted state codes:

`3d3d 3d9c 3dbb 3e31 3e8e 3ea0 3ea7 3eba 3eea 3f03 3f10 3f27 3f4b 3f59 3f5e 3f66 3f6a 3f7a 3f7b 3f7d`.

The singleton cycle is zero in both graphs; the other state converging to it is one. Directly tallying graph labels gives the basin cardinalities and maximum tail depths stated above. The first graph's basins sum to \(2+2026+14229=16257\), while the second sum to \(2+16255=16257\). Comparing the two exact successor arrays yields precisely 2,205 differing arrows. Since the graph contains **all representable states**, this is exhaustive proof of the full finite-state classification, not an inference from a finite time horizon or a sampling experiment.

## Verification

Run `python3 verify_bfloat_spm.py` with Python 3's standard library; no external data, third-party packages or hardware are needed. It checks independent exact rounding methods against all 16,257 successors for each map, then compares the two graph decompositions' per-cycle summaries and per-state depths. It asserts the reported periods, basin sizes and differing-edge count, and prints the cycle lists and maximum preperiods for comparison with `certificate.json`.

The SHA-256 digest of little-endian two-byte successor codes ordered by the 16,257 input codes is `a5f97abb67189fa2fe6942a74ea9a7b31a83ce6b4d3b85e96061598db896a519` for \(A\), and `7f213b1c256c08bf6156c0a034482c16ef633738e0ee03149f47cfe46fbd5327` for \(B\). The digests are reproducibility fingerprints, **not** independent proof in place of the exact computations.

## Relationship to prior work

Paul and collaborators' conference construction, later expanded in 2023, supplies the original real-valued self-parameterized logistic design and its natural choice of bias, feedback gain and outer control. Its results rely on real-map bifurcation and entropy diagnostics and a different tent-map-oriented hardware digitization; the specific complete bfloat16 logistic graphs above are not derived there. Klöwer and collaborators (2023) document precision-induced periodic collapse for the ordinary constant-parameter logistic and generalized Bernoulli maps, including bfloat16, but do not analyze the state-dependent logistic gain or the two specified rounding factorizations. Related exact binary16 classic-logistic cycle censuses concern a different number format and transfer function. The general fact that deterministic finite-state maps are eventually periodic is classical and is not claimed as new. The proposed contribution is these exact graph invariants for an original naturally parameterized hardware-security-motivated map at its control endpoint.

## Limitations

The result is an exact property of two mathematically specified bfloat16 semantics, not of all practical implementation paths or of the exact real map's infinite-state attractor. In particular, it does not prove anything about cryptographic randomness, physical security, or numerical convergence as precision increases. The basin cardinalities count **representable input states equally**, not uniformly distributed real initial values. No positive claim about a period-three/four cycle in the real map is made. Independent research verification and publication-priority checking remain to be performed. The 2021 conference date is used conservatively as December 1 (the last day of the documented event); an earlier online posting day for the conference manuscript has not been established.

## References

1. P. S. Paul et al., *Self-Parameterized Chaotic Map: A Hardware-efficient Scheme Providing Wide Chaotic Range*, 28th IEEE ICECS (2021), available at https://confcats-event-sessions.s3.amazonaws.com/icecs21/papers/2160.pdf .
2. P. S. Paul et al., *Self-Parameterized Chaotic Map for Low-Cost Robust Chaos*, Journal of Low Power Electronics and Applications **13**, 18 (2023), https://doi.org/10.3390/jlpea13010018 .
3. M. Klöwer, P. V. Coveney, E. A. Paxton and T. N. Palmer, *Periodic orbits in chaotic systems simulated at low precision*, Scientific Reports **13**, 11410 (2023), https://doi.org/10.1038/s41598-023-37004-4 .
