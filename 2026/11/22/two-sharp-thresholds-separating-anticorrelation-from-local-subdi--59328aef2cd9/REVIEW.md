# Self-review

## Correctness — PASS

For the precise stationary two-layer Gaussian OU model and all \(\gamma_1>\gamma_2>0\), \(D_1,D_2>0\), the proof verifies the stationary-law normalization, the two-pole autocorrelation, the Green–Kubo diffusion constant, the sign-changing slow mode, and the positive running diffusivity. Its critical global sign function \(H(t)=tM'(t)-M(t)=2\int_0^t sC(s)ds\) has derivative \(2tC(t)\); a two-exponential autocorrelation changes sign at most once. Consequently \(H\) is either always positive or has exactly one zero. Its exact limit produces the sharp \(d=1+q\) threshold, including equality, and its vanishing gives the exponential critical correction. No numerical root count is used as an infinite-domain proof. The independent Lyapunov-based extracted checker passes 847 tests and confirms finite representative cases; the analytic sign proof covers every admissible parameter.

## Originality — PASS, with explicit prior-equation dependence

The complete two-exponential autocorrelation and MSD are *not* original: see Voulgarakis (2023), Eqs. (15) and (16), and Wang–Voulgarakis (2024), Sec. 3. The latter source qualitatively describes subdiffusive profiles for \(D_2<D_1\). Primary-text inspection and targeted prior-index comparisons did not uncover the simultaneous all-parameter phase diagram separating velocity anticorrelation from the strict instantaneous MSD log-slope criterion, the unique ordered crossings, or the critical exponential cancellation. The source equations contain enough information to derive this fact; the contribution is a mathematical classification and proof, not a new stochastic solution. This direct implication risk and possible unindexed equivalents remain substantial publication-priority qualifications, not substitutes for proof.

## Mathematical value — PASS

The result identifies a concrete diagnostic failure: negative velocity autocorrelation need not produce any \(tM'(t)/M(t)<1\) interval, even with equal microscopic diffusion strengths. The exact separation between \(d=1-q^2\) and \(d=1+q\), unique dynamical crossings, and critical fast approach explain when a familiar qualitative diffusivity-ordering heuristic does or does not imply the more stringent observable. All three regions are open or have precisely stated equality boundaries; none is a numerical parameter sample masquerading as a theorem.

## Closest literature and limitations

Voulgarakis, *Physical Review E* **108** (2023), 064105: exact two-level stationary velocity ACF and MSD, qualitative negative-memory/subdiffusion statements; https://doi.org/10.1103/PhysRevE.108.064105 . Wang and Voulgarakis, *Physics* **6** (2024), 645–658: layered model, all-time MSD, finite-regime anomalous profiles; https://doi.org/10.3390/physics6020042 . This review is same-model only, not independent validation or priority certification. It concerns finite positive observation times, stationarily initialized Gaussian internal coordinates, and an exact pointwise derivative, not phenomenological finite-window power-law fits. The earlier exact expressions are credited rather than re-claimed.

Self-review: passed. Independent audit: not yet performed.
