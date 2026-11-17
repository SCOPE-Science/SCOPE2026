# Independent mathematical audit

## correctness

PASS

Exact Catalan decomposition F=1+sum_j w_j (zF)^j, Lagrange inversion yields M_(m,s)=(n)_(m-1)/C_n * binom(2n-m-s,n-s), zero if s>n. For n>=3 and arbitrary repeated block sizes, the added-block ratio Q_(m,s)(b) is bounded by kappa_n mu_b, kappa_n=(2n-1)(n-1)/[(n+1)(2n-3)]; monotonicity in a=n-s,c=n-m and b, and tight pairs (1,1),(1,2),(2,1), justify all-order product kappa_n^(m-1). Distinct-size covariance and factorial variance follow algebraically. Independent rational small-n/m comparisons and inspected exhaustive checker corroborate, do not prove infinite bound.

## originality

FAIL

FAIL: two PRIOR published results on exactly the same uniform noncrossing block multiplicities already imply the COMPLETE claimed all-order theorem. October 18 theorem proves local logarithmic submodularity M(gamma+e_a+e_b)M(gamma)<=M(gamma+e_a)M(gamma+e_b) for arbitrary marks gamma; October 25 theorem proves sharp pair factor M(e_a+e_b)/(mu_a mu_b)<=kappa_n, including a=b via its explicit factorial-moment extension, equality for 1,1 and 1,2. Applying local submodularity to any pre-existing marked block bounds EVERY conditional additional-block ratio by the unconditional pair ratio <=kappa_n mu_b. Iterating recovers precisely kappa_n^(m-1), and published equality cases/covariances are identical. Both prior full RESULT.md files were read; this is a decisive statement-level implication, not a title match.

## value

FAIL

FAIL as an independent new mathematical finding: the all-order inequality and sharp uniform constant follow directly by composing the two prior established theorems without additional structural object, significant new boundary, or new invariant. Correct derived corollary is useful pedagogically but lacks independent mathematical value relative to the already-published same-object all-order repulsion and sharp pair constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
