# Independent mathematical audit

## correctness

PASS

The polar is the cyclic octagon with vertices (1,0),(1,t),(t,1),(0,1) and negatives, including degenerate edges at endpoints. For matrix rows r,s, exact inversion gives ||L^-1||=M(r,s)/|det L| with M the maximum of four sums of two absolute values, while ||L||≤1 puts both rows in the polar. Scaling rows separately to its boundary cannot increase M/|det|. The 48 nonexceptional edge pairs have single-branch certificates L_h−(1+t/2)det≥0, separately affine in edge parameters; its four corner polynomials are Bernstein-positive on eight rational t subintervals. Independently executed the symbolic coefficient check for all 13,824 rational entries. Remaining 16 edge pairs are reduced by swap/sign/row symmetries to three explicitly analyzed representatives; their averaged bounds, monotonicity, and concavity work for all 0≤t≤1. Upper map k=t/(2+t) has ||L||=1 and ||L^-1||=1+t/2. Handles both endpoints and arbitrary invertible real L, not just symmetry-respecting maps. Finite rational certificate represents continuum polynomial positivity, not sampling.

## originality

PASS

Closest identical-norm published result from 26 October determines projection constant λ=2(1+t)/(2+t), BM lower λ, upper 1+t/2, and only first-order BM expansion; it explicitly refrains from the exact interior identity. Lassak 2021 proves the affine-regular hexagon endpoint t=1 with BM=3/2. Deregowska–Lewandowska 2026 general projection-constant upper estimate λ/(4−3λ) is strictly weaker where applicable and not a full interior equality. No searched or full-read source asserts the all-t unrestricted exact equality. PASS best-of-knowledge, older affinely equivalent octagon formula possible.

## value

PASS

The exact all-parameter sharp distortion profile between square and affine-regular hexagon closes the meaningful gap between known projection-constant lower and optimal-map upper bounds. The unrestricted lower bound is not a substitution into an already exact formula; it resolves a natural planar Banach-space invariant. Despite a one-parameter family and finite symbolic certificate, no downstream theorem is required for the complete sharp invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
