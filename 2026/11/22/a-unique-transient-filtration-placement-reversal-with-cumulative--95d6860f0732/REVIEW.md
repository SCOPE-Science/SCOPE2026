# Scientific review

## Correctness — PASS

The statement quantifies \(v\geq0\), \(k,p>0\) and every positive horizon. The two transfer resolvents are both \(k^2/D_j(s)\), and their determinant difference is exactly \(pk(s+v)\). All six eigenvalues exceed \(v\), so the inverse product resolvent is a positive six-fold convolution of exponentials. Standard preservation of log-concavity under convolution makes its logarithmic derivative decreasing; analyticity and the order-five zero at the origin make the decrease strict. Its endpoint limits force exactly one crossing of \(-v\). Direct integration yields a strictly positive, explicit cumulative-difference certificate for every \(T>0\), and the infinite integral and two-room case follow by exact identities. `verify.py` verifies algebra and numerical illustration but is not relied upon for the all-parameter conclusion.

## Originality — PASS on inspected evidence

**Closest empirical work:** Novoselac and Siegel (2009), DOI 10.1016/j.buildenv.2009.03.023, studies multizone purifier placement and its transient performance in a simulated house, so neither placement effects nor transient variation are claimed as new. Mao et al. (2023), DOI 10.1016/j.apr.2023.101716, compares air-cleaning and ventilation strategies experimentally. **Closest analytic setting:** Parker et al. (2014), DOI 10.1007/s12273-013-0136-5, gives a multizone state-space methodology but explicitly excludes indoor filtration from the model it analyzes. General Prékopa convolution log-concavity and matrix-exponential methods are established. The inspected texts do not imply the exact *unique crossing plus strict all-horizon integral ordering plus minimal three-zone threshold* for the stated filter-placement comparison. Residual risk: older state-space and stochastic-network work may encode equivalent consequences without using these application terms; no global priority certificate is asserted.

## Value — PASS

Portable filter placement is physically motivated, and the theorem reveals a meaningful mismatch among three operational metrics: instantaneous concentration after an impulse, time-integrated exposure, and concentration under sustained emission. A universally unique time reversal, together with a strict integrated ordering and a minimality obstruction, gives a sharp test case for multizone simulators and clarifies when a late-time concentration ranking can mislead about cumulative exposure. This is a deliberately narrow homogeneous benchmark; it is not a recommendation for real buildings with changed airflow, uneven mixing or heterogeneous ventilation.

Self-review: passed. Independent audit: not yet performed.
