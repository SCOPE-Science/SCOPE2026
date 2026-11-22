# Scientific review

**Claim reviewed.** The local-run iff classification of all shattered marked vertex-colour tests in the proper-three-colouring class of every simple cycle \(C_n\), \(n\ge3\), together with the complete coefficient formula and equivalent logarithmic extraction expression.

## Correctness: PASS
A properly coloured selected proper subset extends through each uncoloured cyclic gap. Consecutive marked tests must have distinct targets; a run of three requires alternating targets, and every run of four has a failed trace. All binary traces on permitted runs of lengths one, two and three are explicitly realized, so independent gap extension proves the iff statement. The rooted cyclic run-gap composition argument gives the precise \(n/r\) factor; the binomial expansion gives an independently checkable formula. The attached direct-trace enumerator checks all marked supports through cycle order eight. The full cycle and triangle edge cases are handled explicitly; no finite search is promoted to an all-size proof.

## Originality: PASS, with priority risk
The fully inspected previously published cycle result *Exact VC and Littlestone ranks for proper three-colourings of finite cycles* computes two scalar dimensions and explicitly states it does not classify individual shattered supports. The related fully inspected path result gives a four-run obstruction but not marked-run multiplicities or cyclic enumeration. Primary work on colour-structure learning, zero-set VC dimension and tree-shattering bounds does not imply this exact polynomial. Actual research-record, alias, equivalence and published-result searches are documented in the structured audit. Unindexed equivalent results remain possible; absolute priority is not certified.

## Value: PASS
This theorem answers the natural coefficientwise completion of an already studied learning invariant on a standard graph family, using a new full support-level classification and an all-order closed form. It is neither a numerical example nor a renamed dimension bound; the counts retain information about all target-colour choices lost under rank alone. The theorem also supplies an exact family of inclusion-maximal low-rank faces proving persistent nonpurity on even cycles.

## Limitations
Exactly three named colours on simple cycles and fixed binary vertex-colour tests. No extension to other palettes or graphs is claimed. The checker is exhaustive only to the stated finite cycle sizes. Independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
