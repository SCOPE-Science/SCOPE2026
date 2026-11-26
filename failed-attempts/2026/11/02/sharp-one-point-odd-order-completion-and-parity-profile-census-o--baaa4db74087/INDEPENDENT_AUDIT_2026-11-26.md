# Independent mathematical audit

## correctness

PASS

Existing directed cycles cannot acquire new edges in an extending bijection, so an even one is fatal on every superset. The only free arrows pair the terminals and initials of distinguished open paths (an isolated vertex counts as both), specifying a permutation of paths. A resulting cycle has odd vertex length precisely when it contains an odd number of odd paths. Deleting the even objects leaves an odd-cycle permutation on u objects, and reinserting v labelled even objects in ordered lists after the u odd objects gives v! binom(u+v-1,v) choices per base permutation. The known odd-cycle EGF, or the labelled cycle construction in the frozen proof, then gives the displayed integer count and series. With no odd objects there are no nonempty admissible cycles; an empty path set is the unique completion if the existing cycles are odd. Adding one specified isolated point in the obstructed open-path case forces a single path-cycle with the point and all v even paths, giving v! and proving minimality. An independent enumeration agreed on all 36 coloured profiles of total size at most 7; it did not use the supplied checker. The proof, not the test, covers arbitrary finite sets and does not concern simultaneous extensions.

## originality

FAIL

The presentation for partial bijections was not found verbatim, but the entire count and EGF are a routine ordered-gap insertion consequence of the existing exact odd-cycle enumeration after contracting the prescribed paths. The sharp one-point case is just the one-gap case with u=1, and the impossibility cases are immediate from fixed cycles and parity. This judgment does not rely on inaccessible references or claim that a prior source printed the partial-bijection wording.

## value

FAIL

A finite census is relevant to the motivated odd-extension problem, but here the single-map case is exhausted by the immediate path permutation bijection and a textbook ordered-list insertion into the known odd-cycle class. The one-point witness and its factorial count are the single-gap instance, not an additional structural phenomenon in extension theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
