# Independent mathematical audit

## correctness

PASS

The matrices were matched entrywise to Rodrigues's primary text. Independent exact replay (python /workspace/checks/3.py) solves augmented equal-payoff systems on the full and face supports, and reproduces the Sylvester minors, rational branches, strict sign certificates, simple root brackets, endpoint states and endpoint log rates. Negative tangent definiteness extends over each affine path and makes every equal-payoff system on a fixed support nonsingular (subtract two solutions and take the inner product with their tangent difference). The support-wise relative entropy has derivative at most a strictly negative quadratic away from the candidate, while its sublevels keep all candidate-supported coordinates bounded away from zero. This yields convergence from all positive initial data even when the absent-type invasion rate is zero. The boundary equilibrium is unique as a Nash equilibrium and interior limit, not as an arbitrary stationary point on a face. The rate follows from Cesàro averaging the limiting log derivative. Small endpoint changes preserve invertibility and positivity uniformly; near the simple zero the signs persist by derivative control and away from it by compactness. A zero of the candidate's disappearing coordinate is exactly a zero of the face invasion gap, by uniqueness of the full equal-payoff solution. Thus the qualitative local perturbation clause holds.

## originality

FAIL

A distinct indexed record, ae547ad29046, has demonstrably equivalent coverage of the substantive conclusion, including the same model, paths, both threshold polynomials and identities of the disappearing strategies, global attraction, and both endpoint rates. It also states the full post-threshold rate functions. The endpoint ratio is an arithmetic consequence, and qualitative persistence is a standard local consequence of the strict signs and simple support crossing already visible in those exact branches. This is a statement-level coverage finding, not a priority or provenance determination from the catalogue dates.

## value

FAIL

An exact support diagram for these illustrative but motivated payoff paths would be useful on its own. Compared with the independently located matching diagram and its wider rate functions, this package adds essentially a numerical ratio of two known exact magnitudes and qualitative simple-crossing persistence without a quantified robustness domain. Those increments do not provide a separately valuable classification or method, and the affine interpolation is not a physical pH calibration. No surviving valuable repair is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
