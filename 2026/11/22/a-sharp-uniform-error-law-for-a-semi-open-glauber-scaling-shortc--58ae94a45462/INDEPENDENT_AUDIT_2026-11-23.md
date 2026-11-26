# Independent mathematical audit

## correctness

PASS

For the continuum interval with generator (1/2)∂xx, the exact solution is the probability of hitting 0 before N by time t. The shortcut has strictly negative heat residual; the difference is the killed-heat evolution with positive forcing and zero boundary data. Starting the Duhamel formula at a positive time and letting that time decrease to zero justifies comparison despite the incompatible corner data: the bounded initial difference vanishes pointwise in the interior, and the residual is integrable at time zero. The reflection principle gives u≤ε_x and the strong Markov property gives ε_x−u≤ε_(2N−x), where ε_y=erfc(y/√(2t)). Indeed, dropping the order restriction on the first hit of N leaves two independent first-passage times across distances N−x and N; their Laplace transforms multiply to the transform across distance 2N−x. Substitution in v=(ε_x−ε_N)/(1−ε_N) gives the stated strict uniform upper bound. At x=N/2, ε_(2N−x)=o(ε_N) and ε_x→0 as t/N²→0, so the spatial supremum has asymptotic ε_N, without asserting a uniform pointwise equivalent. The numerical cutoff ratio is about 0.0046997190. Taylor division gives the positive 1/t coefficient x(N²−x²)/(6N), while the exact Dirichlet modes decay exponentially. Integrating the exact deficit gives −F''/2=1−x/N with zero endpoints, yielding the stated cubic, and the positive 1/t coefficient makes the shortcut integral diverge.

## originality

PASS

Credit Henkel for the heat boundary-value problem, its exact solution and the same erf-ratio approximation, including qualitative evidence of where it agrees. The checked source does not give the signed, quantitatively sharp comparison, or the stated integrated distinction. The pass is for that comparison, not for the exact correlation, the approximation, or discovery that it visibly deviates when extrapolated. The phrase about where the original author recommends using it is best read as where the source reports agreement; the source supplies no formal cutoff.

## value

PASS

The approximation is an actual published shortcut, so the error rather than a manufactured statistic is a motivated target. The result supplies a separation-independent tolerance and shows that its short-time scale cannot be improved even at a fixed bulk separation. The integrated comparison also identifies a concrete bias from extrapolating a convenient analytic form, rather than merely noting a visible mismatch.

The dated certificate retains the supplied scientific assessment, sources and limitations.
