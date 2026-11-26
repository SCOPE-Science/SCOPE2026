# Independent mathematical audit

## correctness

PASS

For the mixture (not a difference) the MGF is a weighted sum on −b<Re z<a. The zero-free inference can be proved without analytic continuation of Lévy triplets: if X is infinitely divisible and Y_j are iid mth convolution roots for any m, Tonelli at every real argument in (−b,a) gives E exp(sX)=(E exp(sY_1))^m, so each root has the same strip of exponential moments at least. Their analytic MGFs obey this identity on the complex strip. Any zero of the MGF of X would have finite order divisible by every m, impossible since M(0)=1. For k≥2 put w=((1−p)/p)^(1/k) exp(iπ/k); w has nonnegative real part and w^k=−(1−p)/p. The inverse z=ab(w−1)/(bw+a) has z+b=b(a+b)w/(bw+a) and a−z=a(a+b)/(bw+a), both with strictly positive real part because Re w≥0 and |w|>0, including k=2 where Re w=0. Substituting gives (1+z/b)/(1−z/a)=w and cancels the numerator with neither denominator zero. For k=1, M=(1+cz)/[(1−z/a)(1+z/b)] with −1/a<c<1/b. Frullani's identity for each half-line gives the displayed logarithm. For c<0 the subtracted positive-side exponential decays faster than e^(−ax); for c>0 the reflected exponential decays faster than e^(−b|x|); for c=0 nothing is subtracted. The resulting nonnegative Lévy density integrates against 1∧|x|, yields the stated uncompensated finite-variation exponent with zero drift and no Gaussian part, and its MGF agrees near zero. Both p=0 and p=1 are excluded and would give infinitely divisible one-sided gamma laws for every stage.

## originality

PASS

The distinct claim supported by the searches is the uniform common-integer-stage boundary, particularly the explicit strict-strip obstruction for every stage at least two and arbitrary unequal rates and interior sign bias. The sign-mixture family and special exponential laws have antecedents; no priority is asserted for their definitions, or independently for the one-stage law or the general zero-free principle. The exact Resultary hit is the assigned record itself. The closest distinct analogue located in the catalogue is narrower; the closest family paper could not be read in full, so the pass is best of the available evidence, not historical uniqueness.

## value

PASS

The theorem isolates a distributional boundary for a standard sign-mixture model uniformly in rates and mixing weight: changing the number of exponential stages eliminates infinite divisibility even for arbitrarily imbalanced but nondegenerate mixtures, while a pure one-sided endpoint remains infinitely divisible. The explicit strip witness is needed because a generic nonvanishing theorem does not by itself decide whether the algebraic zero is eligible; the explicit one-stage Lévy triplet makes the positive side interpretable. The integer common-shape setting is natural for the Erlang model, not an arbitrary parameter slice manufactured from sampled cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
