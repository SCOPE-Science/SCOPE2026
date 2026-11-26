# Independent mathematical audit

## correctness

PASS

With δ=t/K and P=I+αuuᵀ, the two objectives at fixed α reduce to extremizing the Rayleigh quotient of S or S⁻¹. For α>0 both select the t mode and for −1<α<0 both select the δ mode; optimizing q=1+α gives q equal to the chosen eigenvalue in either direction. The residual cost differences are (1−1/K)t−log K and log K−(K−1)/t, with simple roots T_F and T_R. The nonzero extrema are simple, identity is strictly worse, and ties between the two directions occur only at the stated objective-specific thresholds. The global spectral comparator follows by interlacing the sign-definite rank-one change in S^(1/2)P⁻¹S^(1/2) from S: the endpoint ratio is at least 1/δ for α>0 and at least t for α<0, with respective diagonal equality examples. A unit middle eigenvalue is essential; in dimension two P=diag(δ/t,1) makes both generalized eigenvalues t. The logarithmic mean satisfies L_K/√K=sinh(h)/h>1 for h=(log K)/2, and 1<T_F and T_R<K follow from the strict log bounds. The mismatch ratios K/t² and t²/K are monotone up to the relevant excluded ties and give the common sharp supremum. This is a statement about spectral ratios, not Krylov iteration counts. The source package records 9,093 finite seeded checks; the all-update proof does not require their execution.

## originality

FAIL

The distinct Resultary result 81737ab36f99 covers the forward half and the same unrestricted spectral comparator. The reverse half follows exactly by simultaneous inversion: D(P,S)=D(S⁻¹,P⁻¹), the admissible rank-one class is preserved, and the preconditioned spectrum is reciprocated without changing the condition number. At fixed K, S⁻¹ is the same family after swapping the extreme coordinates and replacing t by K/t. Thus its forward threshold and mismatch law reflect to the reverse threshold and mismatch law, giving the full claimed phase diagram and the common sharp supremum. Extending the matched 3×3 model to repeated unit modes adds no new degrees of freedom by rotation of the unit eigenspace. This is established equivalent coverage in the inspected corpus, not a claim that the October 26 record preceded the October 19 frozen one.

## value

PASS

The exact conditioning loss is a motivated counterexample to using exact divergence minimization as a spectral performance guarantee. The mixed-sign model and comparator over noncommuting rank-one updates make that question meaningful even in dimension three. This is the value of the mathematical conclusion, not evidence of a distinct contribution beyond the equivalent corpus result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
