# Independent mathematical audit

## correctness

PASS

The local rule tables define 4x4 Boolean transfer relations on overlapping predecessor pairs. A binary output has a cyclic predecessor iff the product of these relations has nonzero diagonal, valid even n=1,2. Independently regenerated the reachable deterministic relation automata (83 states for Rule 172, 34 for Rule 184), checked 83+34 exact scalar q(T) seed recurrences with q172=t^4-2t²-2t-1 and q184=t^4-2t³+1, and directly enumerated cyclic image sets for each n<=12; all agree. By Cayley–Hamilton the seed identities extend to all n>=1 and imply the rational generating functions and L_n-(-1)^n, L_n+1 formulas. Thus infinite proof uses a finite exact matrix argument, not a finite-census extrapolation.

## originality

PASS

Best-of-knowledge searches found earlier Rule 172 preimage-tree/Bernoulli-block probability formulas and Rule 184 traffic/reachability foundations, but not the paired all-length cardinality formulas or exact parity identity between the indexed cyclic image sets. Related earlier published cellular-automaton image counts concern Rule 18, Rule 110 and other rules, so they neither state nor imply the two-rule parity identity.

## value

PASS

The exact number of distinct one-step reachable configurations on a finite ring is a natural cellular-automaton invariant with entropy rate, and the uniform parity discrepancy between two distinct elementary rules is a motivated structural surprise. It yields all-size finite-ring reachability counts not recoverable from a handful of simulations; an exact automaton certificate supports possible future dynamical comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
