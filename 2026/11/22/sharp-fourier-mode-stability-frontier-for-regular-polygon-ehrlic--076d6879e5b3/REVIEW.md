# Independent mathematical audit

## correctness

PASS

Reconstructed the holomorphic derivative at inputs with w≠0 and B≠0. The distinct-root identity gives ∑_{j≠i}(z_i−z_j)^{-1}=(n−1)/(2z_i), so D_i=B/(2z_i) and the stated one-step image holds, including the zero-scale image now explicitly excluded from further pairwise-distinct iteration. The j≠i derivative is −4(t−1)^2/[B^2(1−ζ^{j−i})^2], and rotation with cyclic reindexing gives the constant diagonal. The Fourier-sum increments follow from T_1=−(n−1)/2 and T_{k+1}−T_k=1 on the indicated range, hence S_k−S_1=(k−1)(n+1−k)/2. Evaluating the scaling-mode derivative by the quotient rule and adding this Fourier difference gives the full spectrum. The mode constants are positive with maximum n²−1, and their transverse maximum is (n−1)². At t=r^n>0, (n−1)|t−1|<B, so purely transverse perturbations always contract. Comparing √(n²−1)|t−1| with B gives τ_n on t<1; for t≥1 the norm is bounded by (n−1)/(n+1). The exact factorization of Φ(r)−1 into (r−1)^3 times a positive polynomial divided by B follows by multiplying the three-term power difference and comparing coefficients; together with the sign of Φ(r)−r it proves no overshoot, positive monotone convergence, and the unique positive fixed point. At the correctly ordered root vector the derivative is zero and the map holomorphic, so a small contracting neighborhood exists; pulling it back along each finite radial orbit proves the open-basin assertion.

## originality

PASS

Best of current knowledge for the full ambient spectrum and its sharp norm frontier on positive scales. The particular scalar update is Halley's iteration on z^n−1, and the open-basin inference uses standard local dynamics; neither part is credited as a new standalone result. The verified comparison was scoped to actual catalogue summaries, the available 2026 abstract, and frozen descriptions of relevant passages whose primary versions could not be retrieved independently. No evidence established an earlier theorem giving the ambient modes or norm equality needed to obtain the frontier.

## value

PASS

Regular polygons are natural equally spaced starts for the binomial. The exact ambient decomposition identifies both the maximum one-step amplification and the unexpected fact that transverse modes strictly contract even in the scaling-mode expansion regime; it therefore separates perturbation mechanisms rather than just giving a scalar convergence rate. The result is a sharp idealized algorithm benchmark, not a claim that pure transverse perturbations expand or that nearby starts diverge.

The dated certificate retains the supplied scientific assessment, sources and limitations.
