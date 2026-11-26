# Independent mathematical audit

## correctness

PASS

Dhar burning at the hub gives independent ordinary triangle pairs (0,1),(1,0),(1,1). With the degree-two sink a_1, no triangle away from the sink can burn before the hub; b_1 burns first only at height one, which permits the hub to burn at height 2k−2 instead of 2k−1. This gives exactly the three stated gate states and the same independent pair choices on the other triangles. The central reduced Laplacian has k blocks with Smith factors 1,3, and the critical group is independent of the sink. To check the peripheral odometers, an unchanged outer pair has both toppling counts equal to the hub count. For a chosen outer pair, subtract the hub count from both coordinates: the increment vectors for the empty, single and double types are (0,0), (1,0) and (1,1), as follows by applying the two-site Laplacian to the claimed consecutive recurrent pair states with the input grain. Thus these types act on the gate as 0, 1 or 2 extra grains at c in the shifted height variables (h_c−(2k−2),h_b1); their reduced gate operator is the two-site matrix with diagonal 2 and off-diagonal −1. Its three-state addition cycles reproduce the gate toppling counts. The resulting states are recurrent, so uniqueness in each Laplacian class makes the candidate odometers the legal stabilization odometers; loss is u_c+u_b1. The gate-site terms carry weight 3^(k−1) per case, and each outer-site gate/pair type carries 2(k−1)3^(k−2). Of the nine such types four are negligible after division by k, four tend to 2, and one tends to 4. Counting the three gate-site and five outer-site types that reach 2k−1 gives the stated tail; the unique 4k+1 type and unique positive zero-loss type have identical counts. A fresh exhaustive check of both joint histograms passed for k=2 through 6; the all-k result follows from the recurrence and odometer argument, not the finite replay.

## originality

PASS

Qualitative sink dependence, a general avalanche polynomial, and an analogous wheel transition are already covered. One finite coefficient in the friendship laws is also implied by the full-avalanche bijection at a fixed sink-neighbor. The distinct contribution is the complete two-root joint evaluation, including repeated topplings from remote sources, and the resulting extensive-avalanche limit under uniform additions over all nonsinks. None of the compared statements imposes that evaluation or limit.

## value

PASS

The example quantifies how changing only one sink, not the graph or its critical group, replaces a uniformly bounded toppling law with extensive events of two distinct scaled sizes. The zero-loss class clarifies that nontrivial toppling and dissipation are different. The joint law and limiting weights for uniform additions supply more than the already-known qualitative sink dependence and the fixed-source wheel example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
