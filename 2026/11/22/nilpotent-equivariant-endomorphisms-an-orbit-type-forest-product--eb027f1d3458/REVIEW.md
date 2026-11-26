# Independent mathematical audit

## correctness

PASS

An equivariant map out of G/H_i is uniquely determined by an H_i-fixed image of H_i, and onto its chosen destination orbit. There are w_i=|N_G(H_i):H_i| choices on each same-type target. Between distinct types a map strictly decreases the finite orbit cardinality; equal-sized nonisomorphic orbits admit no maps. A finite orbit path eventually reaches the basepoint if and only if it avoids nonbase cycles, and such cycles can only lie within a single block. Thus independent type blocks have R_i external choices at each forest root and w_i labels on each internal arrow. As an independent check of the determinant, adjoin the sink and orient a labeled tree toward it. In a Prüfer sequence of length m−1 the sink appears d−1 times for degree d, so the weighted count sums binom(m−1,d−1)m^(m−d)R^d w^(m−d) over d=1,...,m, giving R(R+mw)^(m−1), including m=1. With no nonbase copies there is exactly the zero map. Two identical types give 1+2w; distinct ones give 1+h_ij+h_ji, as at most one cross-arrow can be used. Known orbit sizes orient the only possible nonzero entry, and ties give two zero entries. Under the GAP convention the resulting matrix is transposed; the fixed-point data are the same. The sharp index is the maximal number of available copies along a chain of admissible type quotients: follow all copies of these types in order, send remaining orbits to the basepoint, and count the arrows until absorption. A singleton pointed space has index one. The strict-size argument specifically uses finiteness of the orbits; the proof need not assert that a finite acting group is independently necessary for that step.

## originality

PASS

Credit the homogeneous nilpotent count, the isotypic wreath structure, the standard weighted forest enumeration and the table of marks itself. The supported distinct content is the arbitrary-mixture factorization in which the weights of exits are the cross-type marks, and its inverse giving all marks from the very restricted two-nonbase-orbit nilpotent probes. No inspected exact or stronger statement provided this forward-and-inverse relation for mixed types.

## value

PASS

The acyclicity statistic gives a closed product across all stabilizer types rather than requiring exhaustive iteration of the full point maps. More importantly, the inverse shows exactly how a very restricted family of small probes determines a standard finite-group invariant once the transitive types and sizes are known. This is a usable information-recovery result for arbitrary actions, not a claim to recover the group or to recompute an already tabulated homogeneous count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
