# Independent mathematical audit

## correctness

PASS

A singleton at positive distances has a realizable distance vector exactly when the Katětov inequalities hold. Arbitrarily many copies at mutual distance 1 prove nonalgebraicity, and homogeneity makes the vector determine its type. With center value x and leaves y_i, the leaf-pair condition is y_i+y_k>=4, so a unique value-1 leaf, when allowed, forces the others to be at least 3. Splitting by x=1,2,3,4 gives (1+z)^n+nz, two copies of (2+z)^n+n2^(n-1)z, and (2+z)^n. Only coefficient 1 is raised relative to b_j=binom(n,j)(1+3·2^(n-j)). At internal j the reference inequality is 2(n+1)(1+t)^2>j(n-j)t with t=3·2^(n-j)>n-j. The sole possible failure is consequently grade 2, whose exact Turán bracket is (33-3n)Q²+(136-32n)Q+80-16n, Q=2^n. For n=3–5 its sign is positive directly; for n=6–10 it is at least 3Q²-184Q-80>0; for n>=11 it is negative. There is no internal grade 2 for n=1,2. Unimodality follows from c_0<=c_1, c_2<c_1 and c_3<c_2 when those grades exist for n<=7, and the initial rise followed by a log-concave tail when n>=8. Normalizing the polynomial gives a mixture with Bin(n,1/3) weight 3^(n+1)/F_n(1), proving the total-variation bound. The supplied artifacts/check_star_types.py and VERIFICATION.md were inspected, not executed. A separately written check (branches/50f06070-eb21-4db8-9bb4-e54dddd1d215/independent_star_check.py, check-complete.log) enumerated vectors through n=7 and checked exact coefficients and shape through n=300. At n=11 the grade-2 difference -2788445 was also recomputed from coefficients, not exhaustive distance-vector enumeration. The infinite claim follows from the sign and shape arguments, not the finite observations.

## originality

PASS

Pass for the full star grading together with its sharp all-order coefficient-shape classification. The Katětov extension theorem and the equilateral-leaf counting subproblem are covered ingredients; the sharp failure at eleven leaves, uniqueness of the offending grade, and coexistence with an exponentially accurate binomial approximation are not established by those ingredients alone.

## value

PASS

The star with leaf distances twice the radius is a natural metric family, and grading by the distances up to that radius is meaningful. The result isolates a low-grade obstruction to log-concavity at a sharp finite threshold, proves it is the only failure at every larger size, and exhibits why an exponentially small total-variation error does not control that local statistic. The value is in this classification and contrast, not just an elementary count of feasible vectors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
