# Independent mathematical audit

## correctness

PASS

The upper bound follows because each 4-edge consumes six vertex-pairs and linearity makes those pair-sets disjoint. For the lower bound, in G^(4)(n,p) with p=alpha/n^2, the conflict-pair union bound gives E[Y] at most alpha^2 n^2/16 and injective placements give E[Z] at most alpha^7 for F+ copies. Deleting at most one edge per recorded conflict and copy leaves a linear F+-free graph. Combining with C(n,4) and optimizing alpha/24-alpha^2/16 at alpha=1/3 yields exactly n^2/144-n/12-1/2187. No finite experiment is used as an infinite proof.

## originality

PASS

Best-of-knowledge searches found general hypergraph-extension and container literature but not this exact linear-host extremal statement for the 4-uniform linear expansion of the Fano plane. The exact constants therefore survive originality, although their derivation is elementary and value fails separately.

## value

FAIL

The claimed positive-density window is obtained by the standard first-moment/alteration template with a universal pair-packing upper bound. The proof uses no Fano-specific structure beyond the fixed 14-vertex/7-edge copy count, so essentially the same calculation works for many fixed configurations at this scaling. The exact 1/144 constant is a crude optimizer of that generic estimate, not a motivated structural boundary or classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
