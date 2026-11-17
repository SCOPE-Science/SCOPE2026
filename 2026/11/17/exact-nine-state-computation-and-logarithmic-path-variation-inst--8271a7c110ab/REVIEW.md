# Scientific review

## Correctness — PASS
Every active Haar mask is realized in a full-dimensional soft-threshold chamber for any positive threshold. The step-vector decomposition reduces the entire quotient seminorm to one-jump inputs. The signs and endpoint bounds for the wavelet detail of a step eliminate the absolute value at the child interface, yielding the exact nine-state recurrence for all depths. The disjoint-scale construction uses only dyadic intervals strictly interior to the path, and proves a linear-in-depth lower bound. The upper bound follows from one nonzero wavelet per scale and an explicit one-wavelet variation estimate. The bundled exact checker corroborates the dynamic program and the construction, but is not used as proof of the unrestricted statements.

## Originality — PASS, qualified
Donoho's 1995 source introduces coefficientwise soft thresholding, and Cohen et al. (2003) study the BV limitations of wavelet unconditionality. The latter gives broader qualitative context but neither supplies the finite two-input path-variation modulus nor the proposed nine-state exact computation. Steidl et al. (2004) prove multiscale Haar shrinkage/TV-diffusion representation equivalences but do not give exact global two-input path-variation coefficients or their growth. Osękowski (2013) develops restricted weak-type Haar-projection estimates in a different norm. The nearby indexed finite Haar endpoint results concern \(L^\infty\) signed multipliers rather than the path-variation norm of zero-one detail projections. Available material gives no identified prior implication of the current exact recurrence and its quantitative bounds. Historical priority remains uncertain, including inaccessible full texts or differently indexed work.

## Mathematical value — PASS
The exact sharp computation supplies a practical all-depth assessment of deterministic perturbation sensitivity for a standard nonlinear denoiser, replacing a search over exponentially many active sets by linear-size integer computation. The quantitative logarithmic divergence demonstrates a genuine and unavoidable stability discrepancy between Euclidean loss and adjacent total variation, relevant to edge-sensitive signal reconstruction. Neither correctness nor efficient computation alone motivates the result; the natural link to classical BV wavelet unconditionality and the sharp computed finite norms provide its mathematical significance.

## Closest work and limitations
The 2003 BV paper supplies qualitative non-unconditionality but not a finite formula; the statistical soft-thresholding papers investigate different errors. The result concerns real one-dimensional nonperiodic dyadic Haar soft-thresholding with identical positive thresholds, not other boundaries, wavelets, statistical risk, or an elementary closed form. Independent review and exhaustive historical priority checks are outstanding.

Self-review: passed. Independent audit: not yet performed.
