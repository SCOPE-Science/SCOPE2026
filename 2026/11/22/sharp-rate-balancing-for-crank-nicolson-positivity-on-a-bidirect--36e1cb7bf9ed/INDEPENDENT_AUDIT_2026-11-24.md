# Independent mathematical audit

## correctness

PASS

With A=ma and s=h/2, the resolvent is the exponential-time average of the Markov semigroup, strictly positive for s>0 by irreducibility; the completed step is 2 times the resolvent minus the identity. An independent decomposition uses the hub/aggregate-leaf two-state chain with decay rate A+b and the leaf differences with decay rate b. It gives resolvent hub return b/(A+b)+[A/(A+b)]/[1+s(A+b)], and leaf return (1-1/m)/(1+sb)+(1/m){A/(A+b)+[b/(A+b)]/[1+s(A+b)]}. These yield diagonal numerators 1+s(b-A) and 1+As-b[b+(m-2)a]s^2 over positive denominators. For b<A the hub threshold is increasing in b; substitution there makes the leaf diagonal 1-(2m-1)b/(am^2). The unique positive leaf zero decreases strictly with b because the coefficient of -s^2 increases strictly. Thus the two thresholds coincide only at b*=m^2 a/(2m-1)<A, the positivity interval increases up to this switch and decreases after it, and for b>=A the hub imposes no restriction. Inserting b* and b=a respectively gives the claimed maximum and factor 2-1/m. At the switch all diagonals vanish; h=0 gives the identity. For instance m=3,a=1 gives b*=9/5 and h*=5/3; the boundary step sends the hub uniformly to leaves and each leaf to the hub with probability 3/5 and to each other leaf with probability 1/5, with no diagonal mass. This is for the completed step and the stated two-direction homogeneous family only. The frozen SymPy script was inspected, not run.

## originality

PASS

Pass for the separate inward-rate design theorem: the unique non-symmetric maximizer, exact simultaneous binding and gain relative to the equal-rate chain. The full-chain diagonal criterion, the fact that positivity holds on one interval, and the symmetric-star law are covered by prior principles and special cases and are not counted as novel. The retrieved sources do not give or imply the optimizer from a stronger rate-design statement.

## value

PASS

The star isolates a natural hub-versus-leaf tradeoff in a positivity-preserving Markov discretization. With outward rates fixed and inward rates a modelling choice, the exact switch gives a design rule and nearly doubles the safe step relative to symmetric rates. The switching mechanism and quantitative gain are more informative than applying the generic diagonal test to one fixed generator. Varying b changes the underlying chain and stationary law, so this is not a method for improving the accurate timestep of an unchanged generator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
