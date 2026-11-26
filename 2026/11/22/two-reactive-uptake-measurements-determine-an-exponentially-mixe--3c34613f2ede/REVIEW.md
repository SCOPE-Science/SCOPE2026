# Independent mathematical audit

## correctness

PASS

With y=x exp(z/(2ℓ)) and C=yW, the forward ODE becomes y²W''+yW'−(y²+1)W=0. Only K₁ satisfies decay, and (yK₁)'=−yK₀ ensures decreasing positive C and gives U=√(D₀k)F(x), F=K₀/K₁∈(0,1). The water-side correction is exactly T=k_m v/(k_m−v)=θU; positive finite parameters require 0<v<k_m. The Riccati equation gives E=xF'/F=1+x(F−1/F) and E'=2F+x(F²−F⁻²)=−H/F². The small-x expansion gives H=x+o(x); the large-x coefficients of F are 1, −1/2, 3/8, −3/8 in successive powers of 1/x, yielding H=1/(2x²)+O(x⁻³). At a zero of H, F'=(1−F²)²/(2F²), which gives H'=−2(1−F²)²/(1+F²)<0. All zeros would cross downward, impossible given positivity at both ends. Thus for r=√(k₂/k₁)>1, the log derivative of R(x)=rF(rx)/F(x) is [E(rx)−E(x)]/x<0; the small-x x log(1/x) behavior and large-x F→1 give the unattained endpoints r² and r. Every corrected ratio inside the open interval gives a unique x, then direct positive reconstruction of D₀ and ℓ from T₁. With only one admissible reading, letting x vary over (0,∞) yields the entire continuous ambiguity family of distinct pairs. The supplied SciPy checker was inspected, not run; its root bracket and tests cover bounded ranges and are not a proof or a universal implementation guarantee.

## originality

PASS

The forward bed model and Bessel identities are credited as inputs. What survives the bounded comparison is global scale identification from two known reaction rates, the sharp data interval, and one-reading minimality. No retrieved stronger statement supplied the required geometric concavity of this particular Bessel ratio or the exact inverse design. Relevant unavailable texts are identified below and are not negative evidence.

## value

PASS

In a motivated two-parameter uptake model, the exact range separates physically incompatible readings from uniquely identifying readings and tells which perturbation is needed to break the continuous one-reading ambiguity. The strict interval is stronger than local Jacobian nonsingularity: it describes the whole attainable data set including singular endpoint behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
