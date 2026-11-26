# Independent mathematical audit

## correctness

PASS

For T(x)=M^T x^[2], the fixed set is binary-linear. In a minimal K-linear dependence of binary-independent fixed vectors, normalize the coefficient of one vector to one. Applying T and subtracting the original relation forces each remaining coefficient to satisfy a²=a by minimality. This contradicts binary independence, including when M is singular. Thus ordered independent fixed k-tuples are exactly the fixed K-frames. Their Frobenius images are frames; each prespecified map from such a frame to its unsquared image imposes nk independent entry constraints and costs q^(-nk) for the unrestricted model. Counting frames gives H_{n,q}(k). Dividing by G_k gives the binary subspace moments, and Gaussian inversion by the finite q-binomial identity gives exactly the stated mass function. The diagonal 0/1 examples exhaust possible D values. The first two frame moments are E[N] and E[N(N−1)], yielding the asserted variance, including n=1 where the latter factorial moment is zero. In the invertible model each K-frame has uniform image among frames, so the fixed-frame moments are identically one, matching GL_n(F2) without assuming a law for singular maps. For the uniform error, 1−H_{n,q}(k)≤2^(k−n) and the absolute inversion coefficients decay faster than exponentially in k. For k=d+j, their magnitude is 2^(-dj−j(j+1)/2) divided by G_d and by the product of (1−2^(-r)) for 1≤r≤j. Euler's product therefore yields the stated limiting mass; the error from summing the omitted and perturbed terms is bounded by a constant depending only on d times 2^(-n). Tightness also follows from E[N]≤1. Total probability gives the singular formula, with invertibility probability c_{n,q}; for fixed q the limiting denominator is positive. Full fixed dimension forces an invertible M, as the squared frame is a basis. The frozen finite script and output were read, not run. The fresh bounded replay /workspace/matrix_replay.py exhausted 65,536 matrices at n=2 over GF(16), obtaining counts by D=0,1,2 of [20656,34680,10200] unrestricted and [256,4080,0] singular, agreeing with exact frame-moment inversion and conditioning. The finite replay is not the proof of uniform asymptotics.

## originality

PASS

Pass for the unrestricted extension-field law, uniform field-size limit and resulting singular-conditioned law, not for the binary ordinary corank case, the perfect-only law or the limiting probability constant itself. The comparison found no covering random-singular semilinear fixed-space theorem in the inspected literature and catalog.

## value

PASS

Uniform full matrices give the natural unrestricted labeled ensemble and include a positive limiting singular fraction at every fixed field size. The exact law separates finite-size field dependence from limiting field universality, even for growing field sizes in the unconditioned model, and shows persistence of that limit in the singular sector at fixed q. This is more than recomputing the classical binary corank constant or the perfect-algebra expectation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
