# Independent mathematical audit

## correctness

PASS

For SPD A and rank-one bb^T, nonzero active spectral components of b produce at least r distinct Lyapunov-operator eigenvalues and prevent CG breakdown in the first r steps. The exact k-th CG iterate is q_{k-1}(L_A)(bb^T), with leading coefficient (-1)^{k-1} product of positive CG step lengths. Its sum kernel q(lambda_i+lambda_j)=V C V^T has an invertible anti-triangular middle matrix C of size k; continuous removal of lower coefficients preserves its inertia, leaving alternating positive/negative pairs and, for odd k, a positive central value. The full-rank spectral-projection matrix adds n-k zeros. The exact continuous-time Gramian solution is PSD of rank r. This proves the universal first-r inertia, not later iterates or finite-precision rank. Independent Frobenius CG calculations for 15 SPD samples in dimensions 2..6 corroborated every early iterate.

## originality

PASS

Resultary checks on early CG rank/indefiniteness and published Lyapunov solvers did not yield the specific matrix-CG law In(X_k)=(ceil(k/2),floor(k/2),n-k). Lungová and Plešinger study the same operator CG and give upper rank bounds (secondary substantive account and primary abstract read) but the full paper was inaccessible, so their complete proof cannot be declared not covering from abstract alone. A general real-polynomial sum-kernel anti-triangular inertia lemma coupled with CG alternating leading coefficient is the distinct content on current evidence.

## value

PASS

Exact signs and rank of every early iterate give a sharp, surprising positivity failure of an algorithm solving a PSD Lyapunov equation. This resolves a natural qualitative numerical-linear-algebra question beyond upper rank bounds and gives a reusable polynomial sum-kernel inertia lemma. The result is exact arithmetic and restricted to rank-one right-hand sides; these scope limits are stated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
