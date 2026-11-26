# Independent mathematical audit

## correctness

PASS

The frozen formulas check; the repair changes scope and attribution rather than the mathematics. Shor's decomposition makes g a gap and gives the run [qa+1,g], with the ordinary a=g+1 case correctly contributing R=g. The frequency condition is a divides g-t and a>t. The exact mean numerator and denominator have the correct extra ordinary contribution and zero-entry exclusion. For the limiting result, discard u<g^(-1/2) with grid and interval cost O(g^(-1/2)), then count at most floor(sqrt(g))+1 affine level-set intervals with error at most 2/g each. Removing at most 2 sqrt(g) divisors, adding a=g+1 and renormalizing preserve the bound. The k-th branch contributes density 1/k on (0,1/(k+1)), giving a telescoping CDF tail 1/(K+1) and the term x H_K. Its second-moment contribution is 1/[3k(k+1)^3], hence 1-(zeta(2)+zeta(3))/3 after telescoping, and variance follows by the boundedness of X_g and the first-moment formula. Independent closure enumeration through genus 14 reproduced every histogram; at g=12 the counts are {1:1,2:2,3:1,4:1,5:1,12:1}. Exact replay is /workspace/repairs/4/check_by_reflectiveness.py. The frozen checker was inspected, not executed. The finite reproduction does not establish the asymptotic theorem. The repaired result and supporting public texts were checked against these derivations.

## originality

PASS

PASS for the repaired claim only. The frozen record counts the divisor histogram among its additional findings and overlooks direct coverage of the underlying finite table and the mean. The corrected package makes the finite histogram and first moment attributed background and claims only the explicit continuous distribution, uniform CDF estimate, and second moment and variance. Those do not follow from a relabeling of prior statements or from their first-moment estimates.

## value

PASS

The repaired theorem gives a complete, quantitative description of a natural normalized fixed-genus Frobenius statistic: a continuous law with a harmonic-step density, compact limiting support, uniform error at all thresholds, and an explicit fluctuation scale. This is information beyond averaging the classical remainder array and applies to the uniformly defined semigroup population. The finite rearrangement and first-moment constant alone would not carry this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
