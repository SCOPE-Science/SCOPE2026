# Independent mathematical audit

## correctness

PASS

The frozen proof at RESULT.md line 50 had an incorrect nonzero covariance prefactor. Write p=q² and J=(p;p)_∞. The published theta omits the factor J, while the frozen displayed theta includes it. Translating Eq. (2.30) to that convention requires J³/θ(−r;p), not J²/θ(−r;p). Independently, as u→1 from below, (1−u) times the defining Laurent sum tends to 1 (the positive-tail coefficient differs from 1 by a summable correction, and the negative tail stays bounded); θ(u;p)/(1−u)→J³, also forcing the corrected factor. A separately written 65-digit check at p=.09,r=.5,u=.4 gave a series–product residual below 10⁻⁶³ with the corrected prefactor, versus about −0.19858 as printed. Complete corrected RESULTS and self-review files are in /workspace/repairs/2/ (RESULT.md and REVIEW.md); the Finding is unchanged. In the repaired proof, the numerator zeros are exactly −ru=p^k with boundary products excluded; for nonintegral ξ the only admissible k is ceil ξ. Proper Gaussianity makes covariance zero equivalent to independence. Lift to the log strip, map it by exp(iπ(w+L)/L) to the upper half-plane, and minimize over deck lifts; the cosh formula increases in the magnitude of the lifted angular displacement, giving ±π for these product pairs. At fixed mean angle θ0=π{ξ}, letting b=sin²t measure radial imbalance gives cosh d=1+(cosh(π²/L)−1+2b)/(sin²θ0−b), strictly increasing on the admissible domain. Thus b=0 is the unique radial configuration, giving the orbit and exact arsinh distance. The core length is 2π²/L by the strip metric on its central geodesic, yielding the sharp half-length bound; at exceptional weights there is no pair, and sin(π{ξ})=sin(πh/(2L)) gives the stated divergence constant. Replay: repaired RESULT.md lines 41–83; arXiv:2008.04177v3 Eqs. (2.10)–(2.12), (2.30), Lemma 2.3. The supplied checker was inspected, not executed and does not test the normalization identity; the finite independent check only corroborates the analytical correction.

## originality

PASS

Reassessed the unchanged distance claim and corrected normalization/attribution. Only the sharp intrinsic geodesic minimization and resulting all-weight quantitative distance law are credited, not the covariance formula, zero products, existence or nonexistence of independent pairs, or the special conformally invariant pairing.

## value

PASS

Reassessed after the normalization repair: the smallest separation for exact independent sampling is a natural invariant of this weighted Gaussian field, and the full optimized formula gives information the already-known existence/product locus alone does not supply. It identifies the unique rotating configuration, the sharp relation to the geometric core, and the scale and constant of divergence when independence becomes impossible. This has use as an exact design constraint for the given field and metric, not as a broader mixing or zero-process theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
