# Independent mathematical audit

## correctness

PASS

The Finding's global cycle bound and interior sharpness witness are correct. The displacement F(x)-x is positive on the left by concavity and negative on the right by convexity, using the right extension at b only for the sign argument. Thus each primitive two-cycle has a unique smaller left coordinate x. With t=(b-x)/b, H(t)=0 is equivalent to the return equation exactly when y=1-(1-a)t^2>b. H'' is negative then positive with at most one zero on the nonnegative interval; H' has at most two zeros and Rolle bounds the number of roots even counting admissible endpoints. At the witness a>b, the four stated rational signs force three interior admissible roots. The three sign-changing roots are simple by degree four; the derivative relation to the multiplier classifies the two sinks and the repeller, and the implicit function theorem gives open persistence. Independent rational root and multiplier enclosures were computed in /workspace/branches/audit_witnesses.py. The wording of the proof's multiplier formula is too broad if read for all cycles: t=0 is possible exactly when c=b, giving (b,1); the positive smooth multiplier argument applies to interior witness cycles, not generally at this switch. This does not affect the stated witness or the global census. The failed disposition concerns coverage and value, not a counterexample to the Finding.

## originality

FAIL

Verified distinct indexed coverage, not a claim about historical priority: Resultary dd9acbf9570b gives the same normalized quartic, the same root-bound mechanism, and a stronger exact census and two-sink criterion throughout the strict-alternation domain containing the submitted witness. The bound on the full cube is a mechanical extension of its algebraic root bound by filtering inadmissible roots; the derivative count does not require the strict-alternation assumptions. The particular witness is inside the already classified three-cycle region. Neither the date nor lack of access to the affine-gap paper decides this result.

## value

FAIL

A sharp first-period census and bistability are natural questions, but the substantive coexistence already lies in an exact stronger classification. The new parameter triple is not selected by an independent scientific constraint; it is a point in that classified open region. The remaining all-cube screening observation is a routine restriction of the same polynomial's roots and does not classify dynamics in the extra regimes. There is no distinct valuable remainder for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
