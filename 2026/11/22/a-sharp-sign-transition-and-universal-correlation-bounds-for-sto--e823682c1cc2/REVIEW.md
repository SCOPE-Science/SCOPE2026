# Independent mathematical audit

## correctness

PASS

For q=1−μ and d=1−E(1−F)²≥μ>0, the backwards innovation series has summable L² norms and nonnegative terms, giving stationary existence and independence of X_n from current removal. Backward differences of stationary solutions equal the product of j residual fractions times a uniformly tight past difference. The product tends to zero in L², so the difference tends to zero in probability, proving uniqueness on the common innovations. Independently, write m=a/μ, V_X=Var(X), V_Y=Var(Y), U_2=Var(U). Conditional variance gives dV_X=v m²+U_2 and V_Y=(μ²+v)V_X+v m²=2μV_X−U_2. Conservation X_(n+1)=X_n−Y_n+U_(n+1) and independent terminal removal give Cov(Y_n,Y_(n+1))=μ Cov(Y_n,X_(n+1))=μ²V_X−μV_Y. Substitution yields the claimed a²[cμ²(1−μ)−v(1+cμ)]/d. Conditioning through the future gives factors q^(k−1) for export and q^k for stock. For V_Y>0, ρ_1=−μ+μ²V_X/V_Y. The exact bounds μ²V_X≤V_Y≤2μV_X follow from the two variance identities, with the first equality iff v=0 and the second iff U_2=0; V_X>0 when V_Y>0. This proves the all-lag envelope, strict signs and sharp equality cases. Both deterministic gives V_Y=0 and undefined correlation. At μ=1/2,c=a=1 the beta variances 1/20,1/12,1/8 give 1/14,0,−1/10 as stated. RESULT.md, VERIFICATION.md and check.py were inspected without executing the uploaded code. The 31,192 count is the script's tally of finite exact-rational component checks, not a proof of the envelope or general lags. The law is event-indexed and depends on mutual independence, not on rainfall or runoff data fit.

## originality

PASS

The recurrence motivates standard random-coefficient stock moments; the exported release is a different observable using the complement of the random state coefficient. The strongest inspected primary wash-off model carries residual mass but has dry-period loss and runoff-driven within-event erosion. Neither that comparison nor the closest indexed claims gives the sign classification and both sharp bounds. Access to other relevant historical papers is incomplete, so this is a bounded decision.

## value

PASS

Measured event exports and retained pollutant stocks have different memory, and replacing one by the other can reverse the sign. The result identifies which variances control this distinction using dimensionless moments, proves a sharp usable correlation interval, and shows distribution-insensitivity at both deterministic-input extremes. The exact threshold and extremizers are structural features of a natural wash-off and carryover model, useful as a benchmark without implying a field calibration or management result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
