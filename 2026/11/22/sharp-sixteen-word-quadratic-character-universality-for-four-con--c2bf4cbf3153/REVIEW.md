# Independent mathematical audit

## correctness

PASS

For p>13 each quadratic is separable. A common root of distinct factors, even over the algebraic closure, would force (i−j)²+4 to vanish, impossible since the possible integers are 5, 8, 13. Thus every nonempty subproduct is squarefree of degree 2|I|, with at least one root of odd multiplicity. Expanding the 16-fold indicator and applying the standard Weil character-sum bound gives the total error (4+18+20+7)√p=49√p. At the at most eight zeros, the unnormalized indicator contributes at most eight per point, giving 16Nε≥p−49√p−64. At p=2529, (p−64)²−49²p=4096>0 and p−64>0; the lower bound increases thereafter. For the full complementary range, the separately written /workspace/branches/e933f95a-f897-4977-b6b8-6c2faa89f589/independent_replay.py uses trial division and both nonzero-square lookup and Euler's criterion; full_census.log reports agreeing 16-entry counts for every residue of all 368 odd primes below 2529. It reproduced exactly the 16 exceptional primes, only mask 1001 absent at 61, full coverage at 59 and 67, and SHA-256 194838fb1badf1f21c7f2a978cef964c71d50b13656a9a1537bd30f09ea254aa. The submitted checker was inspected, not executed. The exact all-prime result uses both the analytic tail and the independently exhaustive finite census; it does not assert a composite-modulus or incomplete-interval result.

## originality

PASS

The supported distinct claim is the exact exceptional-prime spectrum for these four ordered quadratic norms, including the sharp all-prime threshold and the gap at 61 after success at 59. The indicator and eventual existence via Weil are classical, and adjacent exact four-pattern thresholds are not new. The available statements for the closest distinct indexed results have incompatible behavior at boundary primes, so they do not state the same classification; no inspected broader result supplied the missing exact census for these quadratics. This is a bounded assessment, not a priority or exhaustiveness claim about the literature.

## value

PASS

The consecutive Gaussian norms and all ordered length-four sign words give a natural fixed simultaneous-residue problem. The exhaustive result separates a sharp threshold of 67 from the much weaker uniform analytic bound, exhibits the genuine p=59/61 nonmonotonicity, and gives a usable all-prime regime with exact exceptions. It is a motivated exact classification, not a small improvement to an asymptotic bound or a catalog of arbitrary instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
