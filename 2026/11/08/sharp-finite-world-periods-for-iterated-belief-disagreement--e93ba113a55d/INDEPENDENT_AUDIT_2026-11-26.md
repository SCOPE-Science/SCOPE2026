# Independent mathematical audit

## correctness

PASS

Serial functionality yields total successor maps, and transitivity (or the Euclidean property) forces them to be idempotent; idempotent total maps have all three KD45 properties. Disagreement is XOR of the two successor truth values on every input truth set. Atomic valuations realize all of F_2^n, so operator equality is exactly the uniform frame condition. For a stable image U=im(T^h), T restricted to U is invertible; since every sufficiently large power maps onto U, its order is exactly the eventual period. T kills the nonzero all-one vector, so dim U<=n-1. Exact dyadic order 2^r implies (T|_U+I)^(2^r)=0 but (T|_U+I)^(2^(r-1)) is nonzero. A nilpotent operator with that property needs dimension at least 2^(r-1)+1. For the stated alternating retractions on 0,...,m, both maps fix their targets, and the XOR output is zero at 0 and x_i+x_(i-1) elsewhere. On x_0=0 the map is identity plus a single length-m shift, with m=2^(r-1)+1. That restriction is invertible, so U is already the first image, and the exact order is 2^r for every r>=1, including r=1. Stabilization cannot start at zero because T is singular. Choosing a dyadic period larger than the gap between any two positive exponents verifies inequivalence over the class, not on each frame. An independent labelled enumeration on n=1..4 found 1,9,100,1681 pairs and first occurrences of periods 2 and 4 at n=3 and 4; the uploaded checker was inspected, not executed. Finite tests are corroboration only.

## originality

PASS

The supported distinct claim is sharp realization of every exact dyadic period of iterated two-agent disagreement on a minimum-size functional KD45 frame. Neither the previously studied bundle nor the underlying characteristic-two algebra is claimed to be new. The accessible comparisons did not establish coverage of the frame-size result.

## value

PASS

A standard logical bundle built from two individually idempotent agents has no uniform collapse under iteration. The theorem answers the natural sharp finite-model question for every dyadic order and counts worlds rather than just constructing arbitrary large-period binary operators. It also gives finite witnesses distinguishing any two positive iterates. Non-dyadic periods and nonfunctional accessibility are not classified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
