# Scientific review

## Correctness — PASS

The theorem concerns one Boolean language for every integer modulus at least two. A direct recurrence for the three counters proves the upper construction. Writing every one-marker's preceding zero count as \(k_j\) gives both a parity constraint and exact reachability: the residue pairs \((k_j,k_j^2)\) generate precisely \(\{(B,Q):Q\equiv B\pmod{\gcd(m,2)}\}\). The construction handles legal words ending in either symbol, including the modular base state. Zero-padding each `1` by \(0^m\) preserves the action on all three counters while avoiding adjacent ones. Inverse transformations and the suffixes `0` and \(0^m10\) distinguish every unequal counter triple with Boolean acceptance, while a leading `1` distinguishes equal counters with opposite trailing-symbol flags. The accepting empty prefix is not an extra state. The sink is necessary. All quantifiers, arithmetic assumptions and boundary cases are covered.

`checker.py` independently minimizes all thirteen automata for moduli 2 through 14 and verifies 262,136 direct recognition comparisons. These calculations corroborate the proof but cannot substitute for it.

## Originality — PASS (qualified)

The closest fully inspected related theorem is the 2026 result on unrestricted modular scattered-`010` Moore-output complexity, which determines \(m^3/\gcd(m,2)\) output states and explicitly does not claim Boolean-residue minimality. The new result concerns the Boolean zero-residue language intersected with forbidden factor `11`. The prior output theorem does not establish the two separate legal last-symbol classes or their minimality. Kovačević–Vukobratović (2021) analyze run-limited information capacity, not this modular right-congruence. Černý (2010) supplies the underlying algebraic word-count machinery. Colbourn et al. (2018) study regularity of comparisons involving contiguous occurrence counts. Searches included alternative `101`/`00` formulations, composite moduli, safe padding and broader run restrictions. No covering result was found. The inaccessible full text of Alazemi–Černý (2011) and potentially unindexed literature remain historical-priority risks; they were not treated as proven noncoverage.

## Value — PASS

This is an exact all-modulus memory requirement for a natural constrained sequence system and a nonlocal (scattered) pattern statistic. The result is not merely a state-product upper bound: an unrestricted counter machine retains its full parity-sensitive orbit despite a stringent local constraint, and every counter state splits into exactly two Boolean-distinguishable boundary states. The mechanism is a reusable safe-simulation principle for reversible modular counters, while the exact parity defect and the rejecting-sink contribution matter to finite-state decoder design. This is narrower than a broad characterization of all constrained patterns, but the natural infinite family and structural matching lower bound make the specific invariant worthwhile.

## Remaining limitations

The source comparisons are not a guarantee of historical uniqueness. The result is not asserted for nonzero target residues, other patterns, or more general constraints. The included program is reproducible finite corroboration, not an infinite proof. Independent validation is not claimed.

Self-review: passed. Independent audit: not yet performed.
