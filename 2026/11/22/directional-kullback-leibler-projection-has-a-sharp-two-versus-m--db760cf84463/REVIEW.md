# Independent mathematical audit

## correctness

PASS

Averaging Fourier coefficients over the regular polygon gives Q(θ)=P_{q,0}(mθ), q=r^m. Harmonic evaluation of log terms under P_{t,φ} gives the claimed reverse loss; for t>0 it is minimized in phase exactly when cos(mφ)=1. The aligned loss minus the uniform loss is F=2log(1−qt^m)−log(1−t²), and tends to +∞ at t→1. For t>0 write v=√(1−t²). The sign of F is the sign of g(v)−q, where g(v)=(1−v)/(1−v²)^{m/2}; (log g)′=((m−1)v−1)/(1−v²). Thus for m≥3 the unique nonzero tie occurs at v=1/(m−1), with exactly the claimed q_c and t_c. The derivative of F has the sign of 1−qt^{m−2}[m−(m−1)t²]; for m≥3 the bracketed product has a single turning point, and only the descending branch can give a positive-radius local minimum. Above q_c this minimum beats zero and is at t>t_c. For m=2 the derivative is strictly positive at all positive radii when q≤1/2, and otherwise changes from negative to positive at √(2−1/q). These facts give all the counts and the one-sided limits. In the forward direction the aligned average log candidate is log(1−t²)−(2/m)log(1−qt^m); it strictly decreases for t>0 since 1−qt^{m−2}>0. The symmetric second difference of x log x and the binomial series yield the two large-m formulas. CHECK.py was inspected, not executed; grids and quadrature there are diagnostics, not the global proof.

## originality

PASS

The all-order reverse-KL optimizer switch and the exact coexistence radius are distinct from the closest known squared-error and pairwise-KL results. Credit the common Poisson aliasing and phase symmetry as established ingredients, and the m=2 critical radius as a coincidence shared with squared error, not by itself a distinctive number.

## value

PASS

The result gives a global classification where symmetry alone does not select a unique candidate. Simply reversing KL turns a uniformly centered fit into one with competing symmetry-breaking minima; the proof determines their exact tie, jump and multiplicity rather than just instability. The distinction for all m≥4 is also real compared with squared-error fitting of the same natural mixture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
