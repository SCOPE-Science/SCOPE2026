# Independent mathematical audit

## correctness

PASS

For the frozen finding, the headline generating function is correct but the intermediate equality on line 37 of RESULT.md is false: its ending-one suffix must begin with 1 as well as end in 1, and has series z+z²/(1−2z), not z/(1−2z). The complete replacement repairs the proof without changing the theorem. After the correction, the weighted split c(u) is valid, with all cuts through the initial zero run and all cuts just after a one accounted for separately in the ending-one case. The squared weights sum via the explicit index-derivative formula in the replacement, and the separators 2 give the unique ordered decomposition used in the geometric-series argument. The cubic has a unique real zero 0<r<1/3, its conjugate roots have modulus (5r)^−1/2, and positivity precludes cancellation of the simple pole. Division by 9^n and the negative base-two logarithm yield the claimed entropy law. In an independent bounded calculation I encoded words of each fixed length as base-three integers, accumulated output histograms using the weak-pop stack, and squared and summed the bin counts through n=11. This reproduces all displayed terms and continues with 642495 and 2183967. The asymptotic values agree with independent root and residue evaluation. The infinite conclusion uses the algebraic proof, not this finite check; the supplied verification/exhaustive.py and verification/series.py and their recorded outputs were inspected, not rerun. Those are the package replay paths. Corrected file: repairs/5/RESULT.md.

## originality

PASS

Originality attaches to the evaluated ternary second-moment series and its specific growth constant, not to the tortoise map, per-word fertility, the binary recursion, or the general Rényi collision identity. The strongest compared prior statements do not establish that aggregate.

## value

PASS

An exact collision law for this standard stack map gives the concentration of the output distribution, information that cannot be inferred from the image language. The ternary case is the first with a nontrivial split of two binary fibers and subsequent renewal blocks; the evaluated all-length series and dominant rate provide useful benchmarks for more general alphabet or moment analyses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
