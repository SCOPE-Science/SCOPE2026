# Independent mathematical audit

## correctness

PASS

For any antichain trace B, its ideal fiber is the interval between down(B) and the complement of up(S minus B). If these endpoints differ, adjoining a minimal element of the difference to the lower endpoint realizes the other parity. On the fence a size-m support with r selected maxima must omit exactly r+1 minima; equality in the incident-minima count forces one consecutive block. For rigidity the selected queried maxima must cover the block's minima, and every exterior maximum must touch a negative queried minimum. The trace with the full block of maxima and no exterior positives forces size 2r+1; omitting an interior maximum when r>=3, or adding a positive exterior minimum away from the block when an exterior side has length >=2, gives a rigid even trace. In the remaining cases the rigid parity is always odd. The all-minima support fails both parities on small traces, and deleting any one minimum supplies a parity toggle. In top degree the common facets are a simplex boundary; for m=3 and 4 the extra faces are eliminated by codimension-one incidence in the boundary equations, while the odd complexes for m=1 and 2 have respectively three isolated vertices and a triangle with a second path between two of its vertices. There are no higher boundaries. Independently enumerated ideal traces and computed exact rational boundary nullities for both parities through m=8 (python3 /workspace/checks/finite_review.py 3; /workspace/checks/3.txt). The integral top groups are free subgroups of the top chain group; the all-order result follows from the incidence proof, not enumeration. No assertion about general fences or lower degrees.

## originality

PASS

The closest inspected parity-ideal classification and topology result is for disjoint chains; the closest exact fence results are for cardinality ranks. Neither determines parity-sensitive rigid traces on this connected fence or the extremal incidence classification. Pass for the exact maximum-support and top-homology result within the checked evidence, not for unrestricted ideals shattering antichains or for historical priority worldwide.

## value

PASS

Parity is a natural rank restriction on the fence ideal lattice. The exact list of maximum shattered supports distinguishes the odd and even complexes in a way neither the VC number nor the rank polynomial can do. The top cycle classification shows which exceptional faces actually contribute to homology: the four small sizes with extra faces give only two exceptional homology ranks. This is a useful structural invariant for a canonical connected family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
