# Independent mathematical audit

## correctness

PASS

Normalize each arm to [0,1] with measure mu_i ds. The hat matrix has leaf diagonal mu_i/3, center-leaf entries mu_i/6 and center M/3; eliminating the leaf block leaves M/4. Inverting gives center kernel (4-6s)/M and leaf-i kernel (-2+3s)/M + 3s 1_{j=i}/mu_i on arm j. Splitting absolute integrals at the roots gives center 5/3 and leaf 7/3-4mu_i/[3(M+mu_i)], strictly exceeding the center. The affine interpolation bound by (1-t) times the central integral plus t times the leaf integral is strictly below the maximum at every t<1, since the central integral is smaller; a real kernel sign attains the leaf functional even for complex input. Positive full support makes the continuous maximum equal the essential supremum. The normalized minimum mass ranges over (0,1/m], e.g. choose one such mass and divide the remaining mass equally; equality at 1/m forces all equal. Independent rational checks of center, leaf and maximizing nodes in five examples passed (python3 /workspace/repro/frozen_checks.py). The finite checks are not needed to extrapolate to all positive masses.

## originality

FAIL

The earlier 18 October Resultary result is mathematically equivalent to the entire frozen theorem, not merely its uniform-density case. On each arm the coordinate u=w_i x gives exactly Lebesgue measure on an arm of length mu_i, preserves continuity at the junction and affineness, and is isometric on both L2 and L-infinity. Thus it conjugates the orthogonal projectors and identifies every listed sharpness and equality statement. The later weighted record is not used as a priority premise.

## value

FAIL

The exact projection amplification and norming sites are natural quantities, but the frozen weighted scope adds no new invariant or new equality cases: its complete content is obtained by a coordinate substitution from the earlier star result. Thus it has no distinct scientific value as a new finding under the stated hypotheses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
