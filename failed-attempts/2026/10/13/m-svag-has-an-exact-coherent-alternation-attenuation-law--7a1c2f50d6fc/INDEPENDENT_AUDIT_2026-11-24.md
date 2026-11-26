# Independent mathematical audit

## correctness

PASS

For zero initialization the normalized weights at time t are w_h=β^h/Σ_{a=0}^t β^a, h=0,…,t. Their sum is one and the squared-weight sum is ρ_t as displayed. The normalized raw second moment is G², while the first moment divided by g_t is Σ_h (−1)^h w_h, giving the finite-time ratio. At t=0 the ordinary division by 1−ρ_t would be 0/0; the expressly stipulated source convention is ŝ_0=0, γ̂_0=1 here. For t≥1 the correction is well-defined. Taking limits with r=(1−β)/(1+β) gives ŝ_∞=G²(1+r), γ̂_∞=r/(1+2r), and direction gain r²/(1+2r). At β=9/10 these give the stated 20G²/19, 1/21 and 1/399, with momentum ratio 1/19. A nonzero constant gradient yields exactly zero corrected variance and direction gain one. This is an exact statement about prescribed gradients and the paper's update direction, not noise measured on an objective trajectory. The frozen moment-checking script was inspected, not executed.

## originality

PASS

Narrowly, the explicit M-SVAG period-two response is not separately stated as a response theorem in the inspected source or matches. The EMA response and entire variance-adaptation algorithm are prior; the response numbers are direct consequences of those rules, which defeats the value requirement below. No credit for a new mechanism or general result is warranted.

## value

FAIL

The deterministic stress test is interpretable, and it shows an extra attenuation factor beyond momentum. But for this prescribed input the raw second moment is constant by definition, the first moment is a single geometric sum, and both the positive corrected variance and gain then follow mechanically from the published estimator by substitution. Nothing in the record establishes a more informative boundary or robustness statement, a distinct mechanism, or a need for these particular constants beyond illustrating the source's stated stationarity limitation. This is a useful worked example, not a surviving nonroutine exact result; a prose-only reframing would not repair it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
