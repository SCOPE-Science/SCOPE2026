# Independent mathematical audit

## correctness

PASS

Nonempty blocks make the character unique and give char(f^k)=chi^k; equality of consecutive powers forces only fixed cycles in chi. Pointwise, the same equality means each vertex has reached a fixed root by step h, with s the maximum such distance. All nonfixed block arrows are independent and transient; the fixed blocks are independent rooted forests, counted by adjoining a single new vertex to their roots and applying Cayley's formula. Dividing by the entire character-fiber count cancels the nonfixed-block factors. The upper bound follows by using exactly d_i transient steps and at most n_rho(i)-1 further edges. For any h in [d,H], maximize d_i+n_rho(i)-1 at i* and install a chain of length h-d_i* inside that terminal block. A precise reading of the routing construction chooses a representative in every transient block (not just the maximizing path), sends each transient block to its successor's representative or the chosen chain head, and directs other basins to a fixed vertex of their own terminal block. In the selected basin no block is deeper than i* since this would contradict its maximizing H; in other basins every distance is at most d. This realizes h exactly, including h=0 when applicable. Rooted trees of height at most h are a root and a labelled set of allowed child-type trees of height at most h-1; forest roots must have fixed types. This proves the stated EGF, its zero coefficient when positive-count cyclic types cannot occur below fixed roots, the exact-height differences, and the disjoint sum over characters.

## originality

PASS

Pass for the arbitrary-character stabilization profile, particularly the sharp gap-free support with its basin-dependent upper endpoint. The fixed-block rooted-forest count and labelled-set construction are classical; applying them here does not make those methods new. The strongest inspected nearby results cover idempotents, a particular square fiber, or a different forest class, not the complete profile.

## value

PASS

For a natural character fiber, the support theorem identifies all feasible convergence times and separates the roles of transient depth and the size of the particular terminal block. The saturated count and the distributive EGF answer distinct exact questions about that fiber; the cancellation shows why growing transient blocks does not change the probability of convergence while still affecting its height law. This is a useful constrained-map classification, not a claim of a new tree-enumeration method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
