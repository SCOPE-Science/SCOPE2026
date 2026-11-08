# Scientific review: cubic strong-majority edge colouring

## Correctness

**PASS.** For a two-colour strong-majority colouring, writing \(r(v)\) for red incidence at a cubic vertex gives \(r(u)+r(v)=4\) on red edges and \(r(u)+r(v)=2\) on blue edges. The only allowed edge pairs keep the vertex types \(\{0,2\}\) separate from \(\{1,3\}\). Connectedness forces exactly one group; its red-degree-zero or red-degree-three class is a uniquely recoverable efficient dominating set. Conversely, marking the edges incident to a perfect code produces the required two-and-two split at every edge. The closed-neighbourhood counting argument proves the domination characterization. The circular-ladder special case follows from two simultaneous closed-neighbourhood equations, which force alternating occupied columns and rows. Direct independent exhaustive tests from `verify.py` agree with the theorem on a varied finite sample; the argument for all graphs is deductive, not experimental.

## Originality

**PASS, provisional historical priority.** The initiating 2026 strong-majority papers establish definitions and general colouring bounds rather than the exact two-colour spectrum for arbitrary connected cubic graphs. The known index-two exception \(K_4\) in a separate complete-graph study is a covered special case, not equivalent to this universal classification. Classical efficient-domination work treats perfect codes but does not compare them with the newly introduced edge-colouring invariant. The 2024 neighbourhood-balanced-colouring paper supplies an equivalent language on line graphs but its inspected results treat different graph classes and no general perfect-code equivalence. Searches for alternative formulations and stronger implication coverage found no direct prior theorem. Remaining risks include a hidden general statement in the literature or an uncatalogued version; independent priority assessment is needed.

## Mathematical value

**PASS.** This is an exact necessary-and-sufficient structural classification for **all** connected cubic graphs of a recently introduced colouring invariant, not a new bound on a tiny graph instance. It reduces the two-colour decision problem to the classical perfect-code problem, converts any perfect-code enumeration into an exact count of named edge colourings, and identifies an immediately checkable domination-number equality and divisibility obstruction. The cyclic-prism corollary illustrates the correspondence but is not necessary for its value and is not claimed novel independently.

## Scope and unresolved questions

No result about three- or four-colour minimization follows for graphs without perfect codes. This review does not certify the historical absence of equivalent results and does not perform external mathematical validation. The attached tests cover finitely many graphs and do not prove the universal statement.

Self-review: passed. Independent audit: not yet performed.
