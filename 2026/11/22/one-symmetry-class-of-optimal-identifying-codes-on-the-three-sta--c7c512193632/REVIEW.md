# Scientific review

## Correctness: PASS

The claim is restricted to the simple undirected cyclic three-stage butterfly with 24 vertices and radius-one closed-neighborhood signatures. The hitting equivalence follows directly from set symmetric difference. Two independent exhaustive programs, `verify.py` and `verify.cpp`, generate the graph from its complete definition, verify the empty size-eight census and all 48 size-nine optimizers, and verify their natural symmetry orbit. The full set of 48 exact masks is embedded in `OPTIMA.txt`. Monotonicity of identifying codes makes the size-eight exclusion a proof for every smaller size. No untested dimension is inferred.

## Originality: PASS, with qualification

The closest primary antecedent is Foucaud's 2009 thesis, Section 4.2 (pages 46–49): its cyclic butterfly is exactly the present graph, but the specified general upper construction starts in dimension four and the text does not state the nine-sensor optimum or the 48-code one-orbit classification for dimension three. Chen–Lu–Miao's 2009 results concern paths and cycles. Ferrero and coauthors' 2016 butterfly article concerns a layered noncyclic graph and the distinct invariant of zero-forcing number. Public indexing comparisons reveal no equivalent exact result, but independent unindexed historical computations could remain.

## Mathematical value: PASS

The smallest nondegenerate four-regular cyclic butterfly is a natural parallel-computing network with a previously stated general sensor bound but no classified equality cases at this dimension. The exact sensor minimum, 48 labeled solutions, and their free transitive symmetry action give a complete finite optimum-design classification rather than an arbitrary local count. The strict gap between the generic eight-sensor bound and the true minimum is also a concrete boundary of the earlier general estimate. This does not assert anything for higher dimensions.

## Scope and integrity

The result is based on complete finite enumeration and executable source, not an asymptotic assertion or solver-independent symbolic certificate. The audit is a self-review; no independent mathematical audit has been conducted. The original thesis has only a month-specific date in the inspected text, not a verified exact public posting date.

Self-review: passed. Independent audit: not yet performed.
