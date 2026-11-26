# Independent mathematical audit

## correctness

PASS

For the exact directed bouquet and positive m and k, complementing turns AND into OR. Write r for the initial hub bit, u for the OR of the m two-cycle and k last three-cycle bits, and v for the OR of the k first three-cycle bits (all in the complement). The hub bits at times 0 through 3 are r, u, r OR v, and r OR u; from time 4 onward they are r OR u OR v, by the lag-two/lag-three recurrence. From time 2 onward the full configuration is occupied iff the current hub bit and its two predecessors are one; time 1 additionally requires every individual first three-cycle bit to be one. This partitions the labelled states directly: r=u=1 contributes time 0 for the fully occupied initial state, time 1 for the other states with all first bits one, and time 2 for the remaining first-bit assignments. For r=0, u=v=1 the hit is at 3. For r=1, u=0 the hit is at 4 regardless of first bits; for r=0,u=1,v=0 it is at 5; and for r=u=0,v=1 at 6. The one case r=u=v=0 stays unoccupied. The independent block weights reproduce (1,P-1,P(Q-1),P(Q-1),Q,P,Q-1) and one never-hit state, where P=2^(m+k)-1 and Q=2^k. This also proves sharpness, excludes other fixed points and cycles, and gives each of times 2 and 3 mass (1-2^(-m-k))(1-2^(-k))/2, uniformly approaching 1/2 in m≥1. I inspected the verifier and the stored samples rather than executing uploaded code. Its 33 pairs are the tested subset given by m≤7, k≤5 and n≤16, with 299696 states; the finite replay is corroboration only. The partition above reproduces the all-parameter result.

## originality

PASS

The genuinely distinct claim is the complete labelled first-hit law for arbitrary positive multiplicities. The known exponent/period method accounts for the maximal delay and fixed points, and a distinct same-day Resultary record genuinely covers the last two shells in the single m=k=1 case. That overlap is credited; it does not imply the remaining shells or arbitrary multiplicities. No evidence establishes broader exact coverage, and the same-day date does not resolve priority on the overlap.

## value

PASS

The family is the mixed bouquet of the two smallest coprime directed cycle lengths; the parameter sweep keeps that dynamical mechanism while varying both multiplicities without bound. A full labelled transient-time distribution rather than an exponent is useful here: it identifies which initial patterns actually need the worst-case horizon and shows that typical starts instead concentrate on two early steps. These are distinct exact facts not supplied by fixed-point or primitive-exponent results. No broader digraph significance is needed or claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
