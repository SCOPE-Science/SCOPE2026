# Independent mathematical audit

## correctness

PASS

For a full cycle, examine its earliest block that varies. Earlier coordinates are constant, so at that block all projected endpoints use the same effective growth vector. Each projected edge is stationary or is a genuine weak edge, including at equal supports; after deleting stationary steps the resulting nonconstant closed directed walk contains a directed cycle. Conversely, choosing b on the offending block to match its growth vector and extending by zeros preserves precisely the changed supports and their rates. No inversion, strict invasion or finiteness of the equilibrium set is needed. For a two-species block each support gives at most one equilibrium. The origin cannot lie in a cycle (an incoming edge can only be from coexistence and then both intrinsic rates are nonpositive; it cannot return unless both are zero, precluding coexistence). On P,Q,R the singleton rates u=r_2(P), v=r_1(Q) are sufficient. Every 2-cycle forces at least one of u,v to vanish, and each 3-cycle orientation forces one conflicting pair of weak signs (v≤0≤v or u≤0≤u). A vanishing relevant singleton rate makes two distinct equilibria solve the same invertible two-row system. This also covers zero invasion boundaries and the size-one case is immediate. Positive diagonal scalings cancel opposite-sign off-diagonals, balance equal-sign entries with weights |d21|,|d12|, or make the single remaining off-diagonal small relative to the diagonal product. For lower blocks a large scaling of the earlier Lyapunov witness makes the Schur correction tend to zero. The comparison A4 has two positive 2×2 Lyapunov blocks of determinant 30000, normalized absolute spectral radius 2, and skew norm at least (h1+h2)/sqrt(h1 h2)≥2. For any true connecting trajectory, an entering coordinate with negative rate near the past equilibrium could not tend to zero backwards, and a departing one with positive rate near the future equilibrium could not tend to zero forwards; hence the weak inclusion. Sharpness uses the cited strict RPS orbit; independently, on the face 12 the unstable branch out of e1 has d log(u2/u1)/dt=3u1+u2 and positive total u1+u2 bounded away from zero in forward time by logistic comparison, so u1→0 and u2→1. Rotation supplies the other two legs and D3+D3^T=−2I. Reviewed VERIFICATION.md and checker.py; the recorded 660 exact trials only cover nonsingular small blocks, so the general proof, not the recorded runs, covers singularity and continua. Not a fixed-growth-vector converse.

## originality

PASS

The distinct result is exact localization of all-growth-rate weak-graph acyclicity without cross-block bounds or regularity assumptions, and the resulting feedback-size criterion. The three-species sharpness example, connection inclusion, and weak graph are existing ingredients, not discoveries here.

## value

PASS

The iff replaces full-network acyclicity tests by checks on genuinely feedback-coupled blocks and imposes no bound on feed-forward magnitudes. It also explains precisely why size two suffices under determinant conditions and size three can already fail. A4 makes the coverage gain concrete against the two strongest compared sufficient tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
