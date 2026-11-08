# Review of the local chirped-tone spectral transition

## Correctness

**PASS.** The complex Gaussian integral produces the normalized even intensity in `RESULT.md` without asymptotic approximation. Exact derivatives give the critical quartic coefficient \(q(r)\), the sixth-order coefficient \(-8/45\), and the positive derivative \(Q=(4+2\sqrt2)/3\) at \(r_*=\sqrt2-1\). The local stationary equation is analytic in squared frequency. The ordinary implicit-function theorem proves the square-root branch away from the critical chirp, while a rescaled double-root system with nonzero Jacobian proves the quartic-root branch and the quadratic fold coefficient. Strict local concavity of the reduced derivative establishes the stated multiplicities. The supplied executable independently checks analytic coefficients, direct Gaussian integration, and representative root types; it is not an infinite proof.

## Originality

**PASS relative to the inspected evidence, with a specified residual risk.** Chand–Nolen–Wu, arXiv:2601.10910, investigates two-component harmonic spectral interference, not a common linear-chirp deformation with a sixth-order central degeneracy. Li–Cai–Han–Jiang–Ji, arXiv:1812.11292, §§3–4.2, develops Gaussian linear-chirp STFT and sufficient support-zone separation estimates, which do not imply the local exact multi-peak classification or its fold coefficient. Searches for common chirp, quartic-root, sixth-order spectral bifurcation, two-component STFT interference, and saddle-node alternatives produced no equivalent indexed statement. The Chand–Nolen–Wu full text was inaccessible; its public abstract and journal metadata were compared, but a buried equivalent theorem cannot be excluded with certainty. Independently written work can also remain unindexed.

## Value

**PASS.** Spectral peak count is a natural observable for frequency-component resolution. The result identifies an explicit, previously unaccounted-for chirp-dependent transition between continuous side-peak onset and hysteretic three-peak coexistence. The exact critical ratio, universal local exponents, and quadratic fold constant resolve a motivated structural question rather than a sample-specific numerical feature. The scope is deliberately local; no unsupported finite-resolution or global-ridge conclusion is claimed.

## Limitations

The literature comparison does not establish formal publication priority. Other chirp rates, unequal component amplitudes, different analysis times or windows, and measurement noise are not treated. The linear-chirp source is not square-integrable, but the defining windowed Fourier integral converges absolutely.

Self-review: passed. Independent audit: not yet performed.
