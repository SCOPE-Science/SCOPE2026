# Independent mathematical audit

## correctness

PASS

Checked the finite reduction for every n>=3: each ordered support determines the multiset of nonzero four-bit point-incidences and is uniquely determined by it up to relabeling. For an internal subset S of size k<=3, completing it to a center takes exactly 3-k external points; the open trace is the complement of the incidence OR, and the closed trace adds equality with a queried triple only for k=3. The largest, over the 16 traces, of their least external costs is precisely the activation threshold. Factorial placement counts on a given ground subset and division by 24 correctly give unordered coefficients, since every support uses distinct queries. Independently generated shapes by adjoining each next triple as a subset of old points plus canonically introduced new points, deduplicating the resulting incidence multisets, then evaluated each trace cost by internal subset size. This regenerated 666 shapes, all 15 buckets, and the unique first active profile (1,2,4,8,15,15) in both modes at n=9. It gives 1260 in both modes at n=9 and 280350 versus 607950 at n=10. Collecting the stable coefficients yields exactly the stated three-term difference. The all-n result follows from the complete reduction, not numerical extrapolation.

## originality

PASS

The open onset and the common-core open witness are prior coverage; novelty here is the exact all-order two-family coefficient census, including the classification of all first-layer supports and the distinct closed activations, not shattering existence or the witness itself.

## value

PASS

This refines a natural VC-dimension threshold to exact counts on a standard graph family and quantifies how equality of query and center affects shattering. The first-layer rigidity, several earlier closed activation thresholds, and identical leading coefficient despite a positive closed surplus give information not encoded by maximum dimension or by isolated examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
