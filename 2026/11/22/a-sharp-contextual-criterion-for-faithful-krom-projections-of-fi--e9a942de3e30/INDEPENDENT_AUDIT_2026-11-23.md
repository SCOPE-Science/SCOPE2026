# Independent mathematical audit

## correctness

PASS

Replacing a nonempty rule body by one of its members strengthens the implication. Thus every projected model is a source model, and the projected least model equals M_F exactly when M_F satisfies every selected unary implication. For each body this permits precisely the atoms present in none of the M_F missing its head; retained facts and duplicate unary rules do not alter the test. Empty context families are vacuous. When no atom is permitted, pick a blocking context for each body member. A single width-t conjunction with t singleton body-member contexts (t≥2) forces all t contexts in a minimal obstruction. For the original least model alone, a missing head implies a missing body member. For all fact contexts, the singleton {b} tests entailment of a by b, which then holds in every source model containing b. For m=max(1,w(P)), start the padded body enumeration with the faithful choice and distribute the rest across factors. This reconstructs each original body (and every fact) in the body-union. Each factor's least model contains M_F and the first equals it, proving intersection equality including width zero. This does not require syntactic equality of programs.

## originality

PASS

The core additions are the criterion for simultaneous faithful rulewise selection over a prescribed family of fact contexts, its sharp width-sized obstruction, and the use of that choice to attain exact least-model intersection in the nonminimalist setting when the criterion holds. Antecedent entailment under all fact contexts and Horn closure machinery are standard; neither the Krom-only uniform equivalence result nor Antić's general factor approximation covers these additions. This is a bounded comparison, not a historical priority guarantee.

## value

PASS

The test addresses when a Krom upper approximation can be made exact with constrained rule choices, beyond the minimalist domain. For an explicit family one can compute source closures once and select per rule instead of enumerating the Cartesian product of choices. A failed instance has a checkable certificate whose worst-case context count is exactly the body width, not program size or total number of contexts. This contextual control is useful even though the proof and the original-model special case are short.

The dated certificate retains the supplied scientific assessment, sources and limitations.
