# Independent mathematical audit

## correctness

PASS

A moving median of affine inputs is continuous, piecewise affine, and away from ties its derivative at output i reads one input derivative h_{a_i} from within the clamped radius-r window. Every h decomposes as a constant plus weighted single jumps 1_{j>=t}; the selected image of a jump is constant 0 to the left of its influence band and 1 to its right, with at most 2r+1 output edges able to alternate. Triangle inequality and line integration yield V(Mx-My)<= (2r+1)V(x-y) for all real pairs, no genericity restriction. At n=2r+2, k=r+1, the interleaved baseline x=(0,2,...,2k-2,1,3,...,2k-1) has median output i; adding epsilon 1_{i>=k} makes output changes alternate 0/epsilon on all 2r+1 edges, proving equality. Appending endpoint baseline repetitions and perturbation ones preserves all original changes at larger n. For shorter paths, at most n-1<2r+1 output edges can change for a single jump, and the same selector decomposition gives a strict upper bound. Independently checked witnesses through r=31, boundary extension and sample exact pairs; no finite census is used as the universal proof.

## originality

PASS

The concrete external and published-record searches compared mathematical statements, operator domains, norms and implied subcases, not simply titles. Closest strong antecedents were read to their stated scope. No earlier theorem subsuming the final exact result was established. This is a best-of-knowledge conclusion, not priority certification; disclosed archival and nomenclature risks remain.

## value

PASS

Running medians are classical one-signal total-variation smoothers; their full-window amplification of differences is a substantial counterintuitive stability threshold. The theorem supplies the complete all-radii large-path exact law, optimal first path length 2r+2 and explicit rank-selector witnesses, not merely another radius-one or cyclic instance. It is a natural all-window invariant that matters in nonlinear robust filtering.

The dated certificate retains the supplied scientific assessment, sources and limitations.
