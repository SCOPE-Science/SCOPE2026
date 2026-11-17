# Independent mathematical audit

## correctness

PASS

An arc containing three selected edges is shortest iff two consecutive cyclic index gaps sum <=floor(n/2)-1, so legal sets require each adjacent pair sum >=floor(n/2). Summing inequalities excludes five edges n>=6; composition counting yields exact even and odd cubic/quartic coefficients, and a triple is extendable to a four-set iff one gap >=floor(n/2). Independent symbolic substitution checks every coefficient against the October26 earlier formulas identically for both parities; the proof itself valid. The supplied standard-library verify.py enumerates original geodesic paths instead of only gap formulas. n<=5 has no geodesic of 3 edges.

## originality

FAIL

An October 26 published exact cycle theorem has exactly the same P_n(z), M_n(z), same 3-or-4 maximal spectrum, and purity C7 exception. Its gap formulation uses at-most-ceiling half-cycle triple gaps, algebraically equivalent to the submitted consecutive-gap lower bound. Thus the entire current final mathematical claim is strictly covered and fails originality. Earlier Manuel–Prabha–Klavzar established only maximum cardinality, but the later stronger prior is decisive.

## value

FAIL

No new independent invariant or motivated remainder survives the already-published complete face/facet/purity theorem. Re-expression of a gap inequality and a new finite checker are not substantive scientific contribution. Value FAIL of this already-covered final claim, independent of proof correctness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
