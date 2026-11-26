# Independent mathematical audit

## correctness

PASS

The series for E_n reduces modulo 2 to (1+t)^(n-1), whose interior coefficients all vanish exactly for a power-of-two exponent. In those cases for n>=5, A(n,1)=2^n-n-1 is 2 mod 4. If an odd prime l divides the content, evaluating E_n(t) = 1+t^(n-1) modulo l at t=1 forces l>n. For the cumulant step, the nth derivative of e^z/(1-e^z) has just the leading pole (-1)^(n+1)n!/z^(n+1) and an analytic remainder. Thus after multiplying by (1-e^z)^(n+1)e^(-z)/n!, the remainder cannot affect the first four log coefficients. The variance and fourth cumulant compare modulo l with those of the equally weighted endpoint law; the needed denominators are units for l>n>=5. They yield (3n-1)(n-2)=0 and 5(n-1)^2=1 modulo l. Hence l=11 and n=4 mod 11, incompatible with 5<=n<11. The n=3,4 rows give 4 and 11 directly. Independently written exact replay agreed on all 238 tested row contents for n=3..240, checked inclusion-exclusion through row 48 and cumulants for rows 4..20 (1,462 checks in total); it is finite corroboration, not the unbounded proof. The supplied check_eulerian.py was inspected, not executed. Replay: python3 /workspace/branches/a4c7b1a7-5e57-44a6-b5f3-e3c22efa582a/audit_eulerian_independent.py.

## originality

PASS

The supported distinct contribution is the all-index integer-content classification, in particular the exclusion of every odd prime outside the exceptional row. Standard Eulerian parity, moments, and finite values are not new. No equivalent prior classification was established by the available comparisons; this is a best-of-knowledge assessment, not a priority certificate.

## value

PASS

Removing the unit endpoints selects all and only the coefficients on which an Eulerian-row congruence can be nontrivial. The content determines every modulus for which the entire row reduces to the two endpoints, for every index, and identifies the unique odd obstruction. That is a useful arithmetic invariant of a standard triangle rather than an arbitrary column choice or a recomputation of a finite list.

The dated certificate retains the supplied scientific assessment, sources and limitations.
