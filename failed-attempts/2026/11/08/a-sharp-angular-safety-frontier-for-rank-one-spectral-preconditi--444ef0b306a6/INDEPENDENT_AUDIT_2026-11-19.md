# Independent mathematical audit

## correctness

PASS

For every n≥2, κ>1, unit u,v, 0<p≤1 and w=(uᵀv)², the congruence P_p^(1/2)HP_p^(1/2) has a 2-dimensional active block with trace T=κ+p+(p−1)(κ−1)w and determinant κp; the remaining spectrum is 1. The characteristic polynomial at 1 is (κ−1)(p−1)(1−w)≤0, so the active roots straddle 1 and K is their ratio including endpoint w=0 or w=1. With a=κ−(κ−1)w, b=1+(κ−1)w, normalized trace (a/√p+b√p)/√κ is minimized at p=min(1,a/b); a<b exactly when w>1/2. Evaluating ab/κ=1+[(κ−1)²/κ]w(1−w) yields (sqrt(1+t)+sqrt(t))². At p=1/κ direct comparison yields w>1−sqrtκ/(1+sqrtκ)². For g standard Gaussian, X=g_1²~χ²_1 and Y=Σ_{2..n}g_i²~χ²_(n−1) are independent, so w=κ^(2q)X/(κ^(2q)X+Y), and both asserted success probabilities are exact F_{1,n−1} survival functions. As n→∞, Y/(n−1)→1 in probability, giving the erfc limit at c∈(0,∞), and the zero/one endpoint limits. All normalization cases and quantifiers were checked analytically; finite corroboration was not used as proof.

## originality

FAIL

The central deterministic theorem (optimal scalar p, 45-degree iff barrier, attained minimum condition number) is the k=1 inverse-matrix specialization of the previously published October 18 two-level principal-angle boost theorem. Explicitly, H^{-1}=κ^{-1}uu^T+(I-uu^T) has low eigenspace span(u), and P_p^{-1}=I+(p^{-1}-1)vv^T is its rank-one boost; (P_p^{1/2}HP_p^{1/2})^{-1}=P_p^{-1/2}H^{-1}P_p^{-1/2}, preserving the condition number. The earlier γ_*=max(1,(κw+1-w)/(w+κ(1-w))) therefore yields p_*=min(1,(κ-(κ-1)w)/(1+(κ-1)w)), the same 45-degree threshold and the same exact minimum ratio. Independently, the October 12 robust one-step two-eigenvalue PCG theorem gives the same optimizer and even the exact nominal inverse-eigenvalue threshold. Set r=1/κ and angular deviation T=1-w. Its Q=((K-1)/(K+1))^2 is strictly increasing in K, so q_*(r,T)=p_*; its nominal T<sqrt(r)/(1+sqrt(r))^2 yields exactly the audited threshold. The Gaussian F tails are a routine pushforward of this already established angular event using (κ^{2q}X)/(κ^{2q}X+Y), with X,Y independent chi-squares. No separate nontrivial new stochastic theorem survives after crediting those complete antecedents. Direct overlap predates the November 8 source: Git commit dates Oct 25 (two deterministic records) and Nov 1 (Gaussian precedent).

## value

FAIL

The one-spike preconditioner and power-sketch reliability are naturally motivated, and an exact probability can be practically interpretable. But the central 45-degree barrier, unique optimal shrinkage, minimum condition number and nominal-scaling boundary were already fully proved by the stronger October 12 and October 18 statements. The only remaining quantitative specialization is the Gaussian power-vector success probability, obtained by a one-line substitution of a known angular threshold into the standard independent chi-square/F ratio and a routine law-of-large-numbers limit. It is mechanically implied by established results and a textbook distributional identity, not an unknown structural invariant, motivated nontrivial cutoff independent of prior theory, or substantive new mathematical gap. A useful numerical or engineering illustration alone does not make this repackaged claim an original mathematically valuable research theorem under the common V bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
