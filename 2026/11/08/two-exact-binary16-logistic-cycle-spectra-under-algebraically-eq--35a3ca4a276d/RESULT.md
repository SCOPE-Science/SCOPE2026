# Two exact binary16 logistic cycle spectra under algebraically equivalent evaluation

## Finding
Let \(R\) denote correctly rounded nonnegative IEEE 754 binary16 arithmetic, to nearest with ties to even. Let \(H\) be all 15,361 nonnegative binary16 values in \([0,1]\), including zero, subnormals and one. The logistic polynomial has two finite-state evaluations
\[
F(x)=R(4x(1-x)),\qquad
G(x)=R\bigl(1-R((R(2x-1))^2)\bigr).
\]
Only the explicitly shown rounded operations are performed; every other arithmetic operation inside an \(R\) argument is exact. Although both expressions equal \(4x(1-x)\) over the reals, their finite-state functional graphs have distinct exhaustive decompositions:

| Map | Primitive cycle periods | Corresponding basin sizes | Maximum steps to a cycle |
| --- | --- | --- | --- |
| \(F\) | \(1,1,5\) | \(15236,8,117\) | \(109\) |
| \(G\) | \(1,1,8\) | \(15048,3,310\) | \(70\) |

For both maps the two fixed points are \(0\) and \(3/4\); the remaining orbit is the indicated primitive cycle. Exactly 12,513 of the 15,361 one-step successors differ between \(F\) and \(G\). No other cycles occur, and all states eventually enter exactly one listed orbit. Basin cardinality counts distinct binary16 encodings, **not** Lebesgue measure on the real unit interval. Each transient bound excludes the first cycle state (which has distance zero).

## Assumptions and scope
A nonnegative binary16 value is represented by its unsigned 16-bit encoding \(i\) ranging from \(0\) through \(0\mathrm{x}3c00\) (decimal 15,360). Signed negative zero is excluded; exact intermediates may be negative but round symmetrically. Arithmetic is interpreted in the mathematical IEEE model, not according to a particular compiler's reassociation or contraction optimizations. Both maps are well-defined from \(H\) to \(H\), because all their intermediate magnitudes lie in \([0,1]\), apart from the exact argument \(2x-1\) which lies in \([-1,1]\).

## Proof
Every nonnegative binary16 encoding \(i\) in this domain has exact scaled integer value \(v_i=2^{24}x_i\), given, writing \(e=\lfloor i/1024\rfloor\) and \(f=i\bmod1024\), by
\[
v_i=\begin{cases}f,&e=0,\\ (1024+f)2^{e-1},&e\ge1.\end{cases}
\]
The integer list \((v_i)_{i=0}^{15360}\) is strictly increasing, starts at zero and ends at \(2^{24}\). For a nonnegative dyadic rational \(n/2^d\) within \([0,1]\), nearest-even binary16 rounding is exactly the encoding with minimum integer distance between \(n\,2^{24-d}\) and a scaled grid value \(v_i\), resolving midpoint ties in favor of the even encoding. The checker computes the two neighboring grid entries by binary search, then compares *integer* differences, without floating-point approximation.

Writing \(U=2^{24}\), the one-step successors on an encoding with scaled value \(v\) are therefore exactly
\[
F_i=R_{\rm bits}\left(\frac{4v(U-v)}{2^{48}}\right),\qquad
G_i=R_{\rm bits}\left(1-\frac{w}{U}\right),
\]
where \(z=R_{\rm bits}(|2v-U|/U)\) and \(w\) is the scaled integer of \(R((v_z/U)^2)\). The sign in \(2x-1\) is harmless because the next step squares it. These expressions produce all 30,722 successor encodings by exact integer operations.

For each directed graph, the checker traverses the unvisited successor chain of every vertex until a previously classified vertex or a repeated vertex is reached. In the second case the repeated tail segment is a new directed cycle; in both cases back-substitution assigns every newly visited vertex the unique cycle label and distance to that cycle. By induction on each reversed chain, the labels and distances are correct; because every vertex is visited, this is an exhaustive decomposition, not a sample. The checker reconstructs every cycle in successor order, verifies label invariance and distance relations at all vertices, and compares the full census with the exact table above. It also counts every differing successor edge. Its reported cycle encodings, complete edge-digests and transient bounds are recorded in `CENSUS.json`.

## Verification
Run `python verify_logistic_binary16.py` with Python 3 (standard library only). It recomputes the scaled binary16 grid, both exact rounding evaluations, all complete functional-graph components, two graph digests, and the 12,513-edge difference. On success it prints `EXACT_BINARY16_LOGISTIC_CENSUS_OK`. A separate implementation using NumPy's binary16 conversions and binary64 exact intermediates agreed on each of 30,722 outgoing edges; the bundled checker does not require NumPy. The result is a finite-state exact computation with an algorithmically exhaustive witness, not a theorem about infinite-precision or continuous real-orbit distributions.

## Relationship to prior work
The motivating 2022 public preprint and 2023 publication by Klöwer, Coveney, Paxton and Palmer document the instability of low-precision logistic-map simulations and bifurcation diagrams, but do not give these two algebraic-evaluation functional graphs or complete basin counts. Corless's August 2024 *Floats for Philosophers* slides report a binary16 logistic cycle of period 40 under a different evaluation convention, so that pre-existing result is not claimed here; both of the explicitly defined maps above instead have periods five and eight. Sayed et al. (2017) established the importance of operation order for fixed-point logistic implementations, but its finite-register truncation models and parameter-period charts do not imply the two IEEE binary16 nearest-even graph censuses. Real logistic map/doubling-map conjugacy does not intertwine either rounding operation; hence real periodic-point counts do not imply the finite-state tables. Finite-precision beta-shift computations concern a different map and do not cover either logistic evaluation.

## Limitations
All claims are for exactly the specified binary16 format, rounding mode, domain and evaluation trees. No claims concern binary32, stochastic rounding, hardware/compiler execution outside the stated semantics, arbitrary parameters, long-run physical accuracy, or cryptographic utility. Exhaustive finite enumeration proves only this finite system. Unindexed implementations or unpublished identical census tables remain a residual originality risk. Independent assessment has not been performed.

## References
1. M. Klöwer, P. V. Coveney, E. A. Paxton, T. N. Palmer, *Periodic orbits in chaotic systems simulated at low precision*, public preprint 8 November 2022, DOI: 10.21203/rs.3.rs-2223046/v1; *Scientific Reports* **13** (2023), 11410, DOI: 10.1038/s41598-023-37004-4. Open published text: https://pure.uva.nl/ws/files/187636674/Periodic_orbits_in_chaotic_systems_simulated_at_low_precision.pdf
2. R. M. Corless, *Floats for Philosophers: A Talk in Three Parts*, August 2024, p. 60. https://rcorless.github.io/FloatsForPhilosophers.pdf
3. W. S. Sayed, A. G. Radwan, A. A. Rezk, H. A. H. Fahmy, *Finite Precision Logistic Map between Computational Efficiency and Accuracy with Encryption Applications*, *Complexity* (2017), 8692046, DOI: 10.1155/2017/8692046.
