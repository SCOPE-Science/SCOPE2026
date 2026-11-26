# Independent mathematical audit

## correctness

PASS

For the exact diagonal rate update, put A=τρ. Both updated coordinates are nonnegative for all positive τ,ρ and all simplex inputs. The gain in the residual is (s−s_+)−(i_+−i)=τi[1+As(1−ρi)/(1+Ai)]/(1+τ). At fixed i the residual itself is affine in s with coefficient −1/(1+Ai)−Ai/(1+τ)<0. Thus the worst input has s=1−i and r=0, and its residual is τi[1+A−Aρi(1−i)]/[(1+τ)(1+Ai)]. The i=0 value is zero; the quadratic factor is minimized at i=1/2, so the condition τρ(ρ−4)≤4 is necessary and sufficient and includes equality. Solving the strict quadratic gives the two stated infected-fraction roots; solving the affine residual inequality gives s_*(i), with a nonempty unsafe interval at fixed i exactly between those roots. Substituting τ=γh and ρ=βN/γ gives the stated h threshold. At (ρ,τ)=(5,1), the half-half input gives −1/56; at (5,4/5) it gives zero. Iteration of a simplex self-map then proves the all-step consequence, not a trajectory-specific claim when the criterion fails. RESULT.md, VERIFICATION.md and verify.py were inspected without running the uploaded code. RESULT.md overdescribes the checker as comparing polynomial coefficients: the frozen script does exact rational substitution on grids and witnesses instead. This is a reproducibility-description error, not a missing proof; the algebra above verifies the identity for arbitrary inputs. The claim does not extend to fitted rates or floating-point equality.

## originality

PASS

The primary source already provides the diagonal map and recognizes the residual positivity gap, but does not quantify it. Neither inspected coupled NSFD results nor the nearest distinct Resultary finding supply the necessary-and-sufficient condition for this particular physical-rate specialization. This is a best-of-knowledge assessment, not a priority certificate.

## value

PASS

The originating work explicitly flags negative reconstructed R; a numerical analyst deciding whether to use this splitting needs a guarantee for the whole simplex, not just independent positivity of S and I. The result gives the exact unrestricted range, a sharp denominator or step bound outside it, and a certified geometry of failure. It also separates numerical infeasibility from the usual continuous-time epidemic threshold and from behavior of learned rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
