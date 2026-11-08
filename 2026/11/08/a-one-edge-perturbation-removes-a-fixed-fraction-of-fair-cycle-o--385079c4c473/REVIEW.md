# Self-review: A one-edge perturbation removes a fixed fraction of fair cycle orientations

## Correctness — PASS

The domain is the edge-good orientation model on a simple cycle with symmetric positive additive values at endpoints, one distinguished weight \(\tau>0\), remaining weights one, and strong zero-inclusive EFX. For every directed edge entering a two-good recipient, the only potentially positive post-removal envy comes from its tail, yielding the local iff criterion \(I_u\geq w_{uv}\). In uniform weights its violations are precisely isolated cyclic sign runs; a heavy perturbation forbids the distinguished edge ending a plus run or beginning a minus run, and a light perturbation forbids its interior-adjacent positions. Explicit cyclic rotations biject the removed sets. A four-state transfer matrix with characteristic polynomial \((x^2-x-1)(x^2-x+1)\) supplies both exact counts and the asymptotic loss \(1-\varphi/\sqrt5\). The proof separately covers \(n\ge4\) and positive nonunit weights on both sides of the threshold. A separate standalone Python script evaluates EFX directly for every agent pair and removable item in 81,880 labeled test orientations, and independently checks the transfer formulas to size 100. Computations support but do not replace the proof.

## Originality — PASS, with residual priority uncertainty

The EC 2023 graphical-orientation model [1] and Zeng--Mehta [2] supply the relevant EFX definition and existence results, with the bipartite theorem implying existence for the even cycles but not any count. Deligkas et al. [3], Zhou et al. [4] and later Kanellopoulos et al. [5] provide complexity, fairness-variant and parameterized results. The materially read relevant sections and comparative mathematical-record searches found no result claiming the exact one-defect cycle census or the nonvanishing discontinuity of its count. A prior isolated four-cycle equal-weight census matches the unit baseline at four vertices, but does not imply the weighted all-size theorem. Elementary restricted binary-word enumerations are not asserted to be new. An unindexed prior equivalent and undiscovered counting result remain possible, so no exhaustive publication-priority guarantee is claimed.

## Value — PASS

Uniform unit valuations are a standard tractable baseline for graphical fair division. The theorem shows that this baseline is combinatorially unstable: changing a single good by an arbitrarily small positive amount removes a limiting \(1-\varphi/\sqrt5\approx0.2764\) fraction of fair complete allocations as the network grows, despite leaving fairness existence intact. The exact all-size formula and heavy/light equinumerosity characterize this phenomenon rather than merely supplying a finite numerical sample. This is a motivated exact fairness-prevalence invariant for cycles, not a generic rebranded Fibonacci count.

## Closest literature and limits

[1] G. Christodoulou et al., *Fair Allocation in Graphs*, EC 2023, https://doi.org/10.1145/3580507.3597764 .

[2] J. A. Zeng and R. Mehta, *On the Structure of EFX Orientations on Graphs*, arXiv:2404.13527 (April 21, 2024), https://arxiv.org/abs/2404.13527 .

[3] A. Deligkas et al., *EF1 and EFX Orientations*, arXiv:2409.13616, https://arxiv.org/abs/2409.13616 .

[4] Y. Zhou et al., *A Complete Landscape of EFX Allocations on Graphs: Goods, Chores and Mixed Manna*, IJCAI 2024, https://doi.org/10.24963/ijcai.2024/338 .

[5] S. Kanellopoulos et al., *EF(X) Orientations: A Parameterized Complexity Perspective*, arXiv:2512.25033, https://arxiv.org/abs/2512.25033 .

The assertion does not cover zero-valued edges, arbitrary heterogeneous weight profiles, other graph families or weaker EFX notions. The verifier checks finite cases; independent external audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
