# Scientific review of the inner-strip Hankel theorem

## Correctness — PASS
The \(H^2\) definition works for arbitrary inner functions fixing zero because odd powers are orthogonal and square-summable with the displayed coefficients. The two-valued boundary imaginary part gives an \(L^\infty\) Nehari symbol of norm \(\pi\). The Hilbert block is an exact compression by orthonormal powers, not a heuristic matrix approximation. A logarithmically long Rayleigh sequence gives the sharp lower norm; shifting its support to high indices gives the essential lower norm. The Poisson variance identity proves the exact kernel formula and complete norming locus. The claimed zero-fixing hypothesis is necessary for the simple orthogonal-power proof; no assertions are made without it. `CHECK.py` passed 107 finite checks, which are corroborative only.

## Originality — PASS relative to inspected evidence
The closest published record, *An exact square-root-two SRKT gap for the logarithmic Hilbert Hankel symbol* (October 2026), studies only \(-\log(1-z)\), and its kernel supremum is approached at the boundary rather than attained at an interior continuum. Dyakonov's September 2026 foundational full text gives the general test identity and SRKT question but not this all-inner classification. Dyakonov's 2025 full-text results give a general extreme-point implication and the variance of a boundary indicator but not the combined exact operator/essential norms or full inverse-image maximizer sets. The standard Hilbert matrix bound is not claimed as original. The new statement is stronger in its quantified inner-function domain, full essential norm and exact interior kernel maximizers. Residual risk is an unindexed formulation in older composition or Hilbert-transform literature, especially Girela (1986), whose complete material was not inspected.

## Mathematical value — PASS
The SRKT question concerns whether normalized Szegő kernels capture full Hankel norm. Here infinitely many unbounded BMOA symbols are analytically classified as a quantitative negative family, yet their testing maxima occur *inside* the disk, even with maximally noncompact operators. The exact norming geometry can be changed from one diameter to arbitrarily many intersecting diameters by choosing \(B(z)=z^m\), and all infinite inner factors are covered. The interplay between inner powers, essential norm and boundary step variance is a reusable structural mechanism rather than a small numerical improvement.

## Scope and residual risks
This is not a universal strict-gap theorem and does not settle existence of unbounded SRKT-positive symbols. Publication priority needs independent specialist checks for earlier general inner-composition results and older logarithmic BMOA work. Finite software checks cannot certify the infinite-dimensional conclusions.

Self-review: passed. Independent audit: not yet performed.
