# Review of the sharp eighth-power covering threshold

## Correctness — PASS

The proof uses the smooth degree-eight Fermat twist for every nonzero target over an odd prime field. Its genus is \(21\), so Hasse--Weil gives at least \(p+1-42\sqrt p\) projective points; at most eight are at infinity. Thus every nonzero target has an affine representation for \(p\ge1783\), while zero has the trivial representation. The finite component is an exhaustive census for every prime at most \(1777\), not a sample. The checker verifies exact represented-residue counts, independently recomputes the eighth-power image by repeated squaring, and tests the subgroup-size identity. Critical limits: no claim is made about prime-power rings or the complete representation-count distribution.

## Originality — PASS on inspected evidence

The closest source is Arias--Borja--Anaya (2023), Corollary 21 and Section 6. Their general eventual bound applies but cannot determine the sharp cutoff or the eleven exceptional primes in the genuinely octic branch. Their fourth-power theorem already covers the three exceptions \(5,13,29\), which are credited and are not presented as new. Bergelson--Best--Iosevich (2020) proves general large-field existence, not the sharp octic exception list. Searches for equivalent characterizations (two-term modular Waring number, additive basis of eighth-power residues, Fermat octic twists, exact octic exceptional primes) revealed no covering theorem. A possibly relevant 2022 thesis is an unresolved bibliographic risk, not evidence of novelty.

## Value — PASS

The represented-residue invariant and the two-summand modular Waring threshold are standard natural arithmetic questions. The infinite general theorem leaves a genuine finite gap, and the complete classification reveals the last obstruction at prime \(761\), yielding an exact stable prime threshold at \(769\). The nontrivial eleven-prime octic branch, exact exceptional cardinalities, and reusable sharp proof boundary make the result more than a random finite sample or an unexplained incremental bound.

## Reproducibility and scientific limitations

Run `python3 verify.py` to reproduce all finite calculations using only standard Python. The output is recorded in `checks.txt`. The proof's large-prime part relies on Hasse--Weil. Exhaustive computation is a finite certificate, not an independent proof of every result in the literature, and novelty remains subject to uncatalogued publications.

Self-review: passed. Independent audit: not yet performed.
