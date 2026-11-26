# Independent mathematical audit

## correctness

PASS

Independence gives the whole-duration factor exp(-mu T); there is no success before c_f. For s=lambda(T-c_f), the early and late smooth expressions, after dividing out exp(-mu c_f), are w g_1(s) and g_C(s), with g_A(s)=exp(-rs)-A exp(-(r+1)s). Differentiation gives the unique unrestricted maximum B A^(-r) at log(KA), B=r^r/(r+1)^(r+1). The two upper bounds tie exactly when C=w^(-1/r). At that tie e^d>K by the strict tangent inequality for w^(-1/r), and e^d/C=(1-w^K)/(1-w)<K by the strict tangent inequality for w^K. The late feasibility margin log(K[w exp(-d)+1-w]) decreases in d, so the winning late maximum is interior for d at or below the tie; the early maximum is interior for d at or above it. Strict unimodality excludes the join and all other durations. The winning height is continuous and the locations differ by -log(w)/mu. The exact witness has heights 1/24, 1/32, 1/24 at exp(T)=4,8,12 (replay: drawdown_witness() in /workspace/branches/independent_replay.py; no frozen script executed). This proves an unconstrained duration decision in the specified surrogate, including c_f=0, not a calibrated policy. One class has the single smooth optimum c+log(K)/lambda for the same rate assumptions.

## originality

PASS

The shifted Bateman mixture and its stationary locations and local mode-count criterion are known, including for this constrained amplitude path. The supported distinct claim is the strict GLOBAL dominance classification, feasible co-global tie and exact optimizer jump along that path. The closest verified source compares derivatives at the join, not global peak heights. No inspected matching result covers the global crossing; this is a bounded best-of-knowledge conclusion.

## value

PASS

A mode count alone cannot tell a decision maker which duration wins. This complete two-class classification shows that even a minimal heterogeneity can make the optimizer jump by a finite, identifiable amount while the value stays continuous. It supplies an exact benchmark for competing timing and exposure effects. It is deliberately model-specific: if mortality stops on refuge arrival and only survival to arrival is required, success as a function of allowed duration is a cumulative event and is nondecreasing. The result is not a river-operation recommendation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
