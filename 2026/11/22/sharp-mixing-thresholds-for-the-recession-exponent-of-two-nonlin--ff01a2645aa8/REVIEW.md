# Scientific review

## Correctness

**PASS.** Exact differentiation establishes the pointwise exponent identity (3). The derivative sign is controlled by one function with one zero on its permitted interval, yielding a global classification for every real \(p>1\). The amplitude-optimized envelope has an attained maximum over positive amplitudes, and its sharp \(p=2\) crossing of two is algebraically equivalent to the offset ratio condition. The physical storage law is obtained by integrating each discharge over future time and has finite positive storage precisely under the stated \(p>1\) assumption. The standalone exact checker verifies multiple rational parameter tuples, derivative signs and both displayed special cases. These finite checks are not a substitute for the proof.

## Originality

**PASS relative to inspected literature, with residual priority risk.** Wittenberg (1999) provides the isolated nonlinear storage law; Harman, Sivapalan and Kumar (2009) provide linear-reservoir aggregation theory; McMillan et al. (2011) explicitly motivate multiple nonlinear stores but do not give the same two-store parameter classification in the inspected text. Gao et al. (2017) discuss two *linear* reservoirs. Jachens et al. (2020) already illustrate superposition of nonlinear power-law events and large changing recession slopes, so the qualitative phenomenon is not new; their analysis does not state the sharp two-component offset ratio or complete one-peak theorem. Roques et al. (2022) analyze compartmentalized hillslope hydrology with linear benchmark mixtures. The reviewed materials do not imply either the exact single-peak condition or sharp superquadratic threshold for two equal-power nonlinear stores. Important limitations: Wittenberg (1999) and Gao et al. (2017) could only be read at abstract/metadata level; mathematical priority has not been independently certified. Bibliographic comparisons are detailed in `AUDIT.json`.

## Value

**PASS.** The result answers a diagnostic problem arising in catchment-model structure selection: precisely when a mixture of two individually identical-exponent nonlinear drainage laws yields a transiently elevated apparent exponent, including a high-curvature behavior often used to judge how many active flow pathways are needed. The threshold \(b/a>3\) is a sharp, interpretable bound for two square-law discharges. This fact does not presume observational calibration and is not a routine reparametrization of the single-store law.

## Scope and risks

The result applies to rainless, independent, equal-power nonlinear stores and instantaneous differential slopes. Field recession estimates depend on noise, recharge history, finite windows and heterogeneous exponents. General identifiability and empirical fit are not established. Relevant sources and access limits are stated in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
