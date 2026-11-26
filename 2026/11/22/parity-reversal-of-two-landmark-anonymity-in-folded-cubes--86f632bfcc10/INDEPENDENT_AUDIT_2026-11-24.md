# Independent mathematical audit

## correctness

PASS

Translate the first landmark to zero and permute coordinates so the second differs on h coordinates. Count words by their two block weights (i,j), fold their two distances, divide by two for the free antipodal action, then remove the two landmark classes. Interior coordinate counts give at least h per complement orbit away from the central layer; the one possible self-complementary count pair still gives at least h because the second block is larger. Toggling one of the h differing coordinates exhibits the exact smallest class (1,h-1) if 2<=h<n/2. For h=1 each nonlandmark pair has an interior second-block count, so its product of binomial factors is at least n-1; the class (1,2) attains this. Line 45's literal wording about 'a binomial factor equal to one' is imprecise (the first factor is always one); the product and the intended bound are as just shown. For even n=2m and h=m, if both block counts are interior the orbit count is at least m^2, except the halved central count which is still at least 2m for even m>=4. When one is an endpoint, swapping the two blocks gives a disjoint complement orbit of size at least m with the same signature. The neighbors of a attain 2m. At n=4 the self-complementary class contributes the exceptional two vertices. The resulting comparison across h proves the optimizing separations; shell sizes n and half the central binomial coefficient give the claimed unordered-pair counts. Independent replay: python3 /workspace/review_checks/folded.py uses BFS from the Cayley quotient generators, and matches every coefficient as well as minima and optimal-pair counts for n=4..14. The frozen scripts and bounds were inspected; the universal proof is the counting argument, not finite checking.

## originality

PASS

The folded profile counts are classical pair-sphere intersection numbers and the displayed polynomial is a direct aggregation of the earlier ordinary-cube profile. Do not credit either the binomial input or the folded enumerator as an independent novelty claim. The supported distinct claim, consistent with the frozen originality scope, is the all-separations smallest-positive-class evaluation after folding, including the even central exception and the parity-controlled optimal two-landmark geometry. Existing profile data determine individual values but the inspected sources give no uniform minimum theorem or inequality implying that sharp classification.

## value

PASS

The worst nonempty distance-signature class is a natural exactly-two-landmark anonymity invariant. Uniformly locating its minimum over cropped joint profiles and proving all optimizing separations reveals a parity-dependent geometry not given by a one-landmark shell size or the unquotiented minimization. This goes beyond recomputing individual intersection tables; no claim about arbitrary landmark counts or empirical privacy follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
