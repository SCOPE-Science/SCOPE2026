# Independent mathematical audit

## correctness

PASS

After x=βt, the bracket interpolates between 1+α and 1−α as t ranges from zero to infinity: exactly the claimed closed parameter range is nonnegative. Integrals of t exp(−bt) and t² exp(−bt) give the normalized rational transform. Recomputed the cubic discriminant, root brackets and Vieta relation A+2B=6. For 0<α<1, A>2 and B>1 directly dominate each subtracted exponential after bounding the cosine by 1. For −1<α<0, A>1 and B>2 yield Eα(t)≥exp(−t)−exp(−2t)>0. The logarithmic Frullani integral uses the root rates A/β and (B±iC)/β, all with positive real part; conjugate pairing gives the stated real kernel. Gamma subtraction removes exactly 2exp(−2x/β)/x. At interior parameters and at 0,1 the residual numerator vanishes at zero with a finite derivative and decays exponentially at infinity. Its mass follows from the atom at zero as s→∞, with residual transform limit (1+α)/4. At α=−1 the numerator of the transform is 6y+8 and the residual kernel is positive with xρ(x)→2, so it satisfies the Lévy integrability condition but has infinite activity. Also the fixed gamma residual is unique in law by division of Laplace transforms and cannot be finite-activity at this endpoint. Substituting s=1−z in the residual Lévy exponent and expanding exp(zx) gives the integer jump intensities for all α, including −1; the sum is ∫(1−exp(−x))ρ(x)dx<∞ by Lévy integrability. This establishes the endpoint count decomposition even though the proof's direct finite Poisson marking argument is restricted to α>−1. Independent symbolic reproduction by assembling the two elementary gamma integrals, taking the discriminant, and expanding G'(z)/G(z) at z=0 gave 432α²(α−1)(α+1), the three degenerate factorizations, G(0)=64/243, and the first three ν values 31/32, 1453/6144, 69263/884736 at α=1/9,β=1, hence μ_1=29/96. The frozen verification was inspected, not executed; numerical root samples do not establish the uniform kernel bound.

## originality

PASS

Qualified pass for the positive gamma-extracted Lévy kernel, exact activity transition, and count factorization; not for the underlying model, rational transform, or general Poissonization principle.

## value

PASS

The exact independent decomposition of a preexisting count model separates its negative-binomial baseline from positive compound-Poisson jumps. It also distinguishes the sharp loss of finite continuous residual activity from the persistence of a finite integer jump rate. Both conclusions concern the specific fixed gamma factor and full valid parameter interval, not a numerical grid or an identity merely renaming the original mixture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
