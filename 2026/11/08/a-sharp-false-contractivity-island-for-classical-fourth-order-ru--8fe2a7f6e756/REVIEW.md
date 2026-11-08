# Scientific review

## Correctness

**PASS.** The theorem is quantified over every real \(\gamma\ge0\) and step \(h\ge0\), including zero, the marginal \(\gamma=2\) case, and the RK4 scalar stability boundary. The algebra \(N^2=0\) yields the exact two-by-two polynomial, and an exact singular-norm identity reduces contractivity to one scalar inequality. A sum-of-squares identity proves \(r>0\) globally; an increasing cubic identifies the scalar boundary; a positive-coefficient transform of an eighth-degree polynomial proves the global monotonicity needed to rule out extra intervals. The logarithmic derivative of the exact semigroup identifies physical expansivity independently. The small-shear-bifurcation and large-shear endpoint laws come from explicit Taylor and simple-pole inversion. A standalone exact-rational certificate and 13,000+ numerical cross-checks passed. Finite checks are not used as universal proofs.

## Originality

**PASS under a documented, nonexclusive literature comparison.** The 2017 Sun--Shu three-state semidissipative counterexample is not the present two-state family and neither its proposition nor its two-step theorem implies the exact one-step false-contraction interval for \(\gamma>2\). The 2018/2019 Sun--Shu strong-stability results and the 2023 Achleitner--Arnold--Jüngel classification impose semidissipative hypotheses or characterize method-level stability, not the complete planar nondissipative RK4 norm phase diagram. Tadmor (2023) discusses Jordan blocks and spectral-stability insufficiency but not the stated quantitative interval topology and asymptotics. A previously published triangular-shear result concerns exact continuous semigroup \(L^p\) contractivity, not RK4's spurious numerical contraction. The statements, parameters and implications were compared rather than merely their titles; no examined source subsumes the new conjunction. Residual risk is that a specialized older numerical-contractivity example has the same exact one-step classification.

## Value

**PASS.** The exact disconnected time-step admissibility set is a sharp, motivated boundary phenomenon in nonnormal time discretization: at a particular RK4 step the nilpotent dynamics are erased entirely although the physical solution can exhibit arbitrarily large amplification. The theorem supplies a precise calibration case for timestep monitors based on eigenvalues or observed norm decay and distinguishes numerical contraction from physical energy decay. It is a complete classification for a natural minimal defective-matrix family, not a claim of generic RK4 stability or improved accuracy.

## Closest literature and limitations

See Tadmor (2023, arXiv:2312.15546), Sun--Shu (2017, 2018/2019) and Achleitner--Arnold--Jüngel (2023, arXiv:2308.05689). The result is confined to Euclidean one-step norms, real two-state Jordan matrices and classical RK4. Prior publication priority in highly specialized analyses cannot be ruled out conclusively. The cited 2017 article was compared using accessible extracted text; its graphical page view was inaccessible. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
