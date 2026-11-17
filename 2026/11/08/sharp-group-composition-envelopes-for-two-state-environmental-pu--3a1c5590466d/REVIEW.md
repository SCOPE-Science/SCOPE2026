# Independent mathematical audit

## correctness

PASS

For a hyperedge with frozen cooperator fraction p, q -> p^2+(p-p^2)q is contractive because 1-p+p^2>=3/4; its unique fixed point is h=p^2/(1-p+p^2). h<=p holds from p-h=p(1-p)^2/(1-p+p^2). The lower supporting line 1-(1-p)/D(u), u=floor(g/2)/g, lies below h(j/g) because D minimized at u (and 1-u for odd g). h is strictly convex on [0,1/2], and the last supporting segment slope 1/D(u) is no lower than the preceding derivative. Jensen then yields the polygonal sharp lower envelope. Mixtures of segment endpoints attain it; upper envelope attained by all-defector and all-cooperator edges. Independent exact-rational convex-hull construction for every 2<=g<=120 found exactly j=0,...,floor(g/2) and g as extreme lower vertices, while odd g has an additional collinear contact at floor(g/2)+1. Exact four-person witnesses gave 2/3<9/13<3/4. Limitations: distributional sharpness not guaranteed for any specified connected hypergraph, only fixed strategies and the two given exponents.

## originality

PASS

The full Wei hypergraph primary model is broader dynamically but has no fixed-composition g-dependent stationary lower hull; no exact or stronger published Resultary match was identified after mathematical parameter comparison. Generic Markov and convexification tools are acknowledged.

## value

PASS

A meaningful model-specific structural classification: for every finite hyperedge size, it determines which cooperator-count compositions minimize and maximize long-run resource quality at a given aggregate cooperation level, with a parity-specific contact degeneracy and explicit arrangement reversals. The two-state stationary equation and Jensen are elementary, but the exact all-g supporting hull and equality cases are a potentially reusable group-allocation invariant, not a software-only restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
