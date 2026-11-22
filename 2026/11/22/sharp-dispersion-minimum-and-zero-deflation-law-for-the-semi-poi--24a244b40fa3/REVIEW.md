# Review of sharp dispersion and zero calibration in the semi-Poisson law

## Correctness — PASS

The exact source probability mass function has normalizer \(S(t)=(t^2-t+1)e^t-1\), and the exponential-family identities \(\mu=tS'/S-2\), \(V=t\mu'\) follow by termwise differentiation. The strictly decreasing size-biased adjacent-mass ratio proves \(V<\mu\) with no numerical assumptions. Differentiation gives the explicitly displayed four-term exponential polynomial as the numerator of \(F'\); the attached independent standard-library checker recomputes that identity and all signed coefficients. The first negative coefficients occur in degrees 10–14, all coefficients from degree 15 onward are positive, with positivity for degrees at least 26 established by four exact shifted-polynomial certificates. Therefore \(N/t^{14}\) rises strictly across zero exactly once. Exact rational exponential bounds bracket that unique point and the minimum value. The equimean zero-mass ratio follows by differentiating \(\log(p_0e^{\mu})\) and checking both asymptotic limits. This is a proof for all positive rates and all counts, not a finite simulation. Risk: a computational/transcription implementation error would affect the certificates; the derivative and coefficients were independently reconstructed from definitions within the supplied program and checked by execution.

## Originality — PASS, qualified

The 2023 original introduced the semi-Poisson mass function and printed overdispersion, a ratio above one, and a purported maximum near 1.4; the proved law instead has a unique *minimum* around 1.4074 and is strictly underdispersed. A subsequent general treatment of weighted Poisson laws (Puig, Valero, Fernández-Fontelo, Proposition 5) already implies underdispersion from log-concave weights, so underdispersion is **not** claimed as new in isolation. Cahoy, Di Nardo and Polito give broader factorial-moment criteria. Those known broader principles do not imply the exact uniqueness of the model-specific minimizer or its rational coefficient certificate and sharp equimean zero-mass calibration. Relevant scientific records and model/parameter aliases were searched without identifying a covering exact theorem. Residual risk: unindexed/later papers may have independently established the same model-specific sharp results; lack of a search hit is not proof of priority.

## Value — PASS

A model presented as flexible for overdispersed count data is actually underdispersed across its whole parameter space. Its sharp global Fano minimum is a natural, fit-relevant statistic (the largest achievable fractional reduction in variance at equal population mean), and the monotone zero-mass comparison quantifies a systematic count-zero deficit relative to an equimean Poisson baseline. The uniqueness certificate replaces an erroneous qualitative Figure-2 interpretation with a mathematically complete shape theorem. These facts constrain which kinds of claim-count variation the original model can represent and support model comparison and calibration; they are not an arbitrary finite parameter slice.

## Closest literature and limits

The mathematically defining primary source is Almuhayfith et al., *Mathematics* 11 (2023), 1122, https://doi.org/10.3390/math11051122. The broader weighted-Poisson comparison is Puig et al., https://doi.org/10.1111/sjos.12677, and Cahoy et al., https://doi.org/10.1007/s00362-021-01222-7. The result covers only the printed one-parameter probability mass function; empirical conclusions and modified/mixed laws are not evaluated. Independent mathematical validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
