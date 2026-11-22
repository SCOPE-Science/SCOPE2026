# Scientific review

## Correctness

**PASS.** The primary geometric sources identify the eighty Rosenhain tetrads with all affine nonisotropic two-planes of \(\mathbb F_2^4\). A quadratic refinement has parity one over each such plane, giving the displayed kernel inclusion. The five-coordinate homomorphism is surjective with target of order \(128\). Sixteen explicitly listed incidence vectors have exact determinant \(+128\), forcing equality of the span and kernel. A standalone exact-integer checker reconstructs every tetrad and reproduces the determinant and congruences. No numeric extrapolation is used.

## Originality

**PASS with residual priority risk.** Keum (1997) and Dolgachev (arXiv:2302.13101, 2023) provide the geometry, but do not give the integral Rosenhain incidence lattice, its eightfold congruence or Smith type. The published Göpel-tetrad lattice handles the distinct isotropic incidence family and has exponent four, not eight. Cullinane's projective-binary visualization describes the same 80 combinatorial tetrads, not an integral Smith calculation. Equivalent code-theoretic tables may exist under different terminology.

## Mathematical value

**PASS.** Formal integral reconstruction of node weights from geometrically distinguished tetrads is natural and distinct from rational spanning. The exact order-eight obstruction, contrasted with order four for Göpel tetrads despite the equal index \(128\), captures an integral distinction between complementary Kummer configurations. It gives a complete membership criterion rather than a sampled numerical invariant. It does not identify this quotient with a Picard or Chow quotient.

## Scope and evidence

The finite determinant and parity identities are checkable from `verify_rosenhain.py` and `rosenhain_80.csv`. Historical sources are cited in `RESULT.md`. The only classification is for the reduced two-torsion of genus-two Jacobians in characteristic different from two. Historical priority is qualified, and no independent audit is represented.

Self-review: passed. Independent audit: not yet performed.
