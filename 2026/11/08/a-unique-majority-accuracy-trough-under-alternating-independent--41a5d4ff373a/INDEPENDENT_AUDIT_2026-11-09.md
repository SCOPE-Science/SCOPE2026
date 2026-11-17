# Independent mathematical audit

## correctness

PASS

Couple jury m+1 to jury m by one independent p-voter and one q-voter and compare only old margins ±1. The exact difference is p(1-p)(2q-1)t_m+(1-p)(1-q)(2p-1)v_m for a trinomial walk with up probability pq and down probability (1-p)(1-q). Its positive Fourier symbol L(theta)=c+2sqrt(ab)cos(theta) produces v_m/t_m=sqrt(a/b) E_m[cos(theta)]; changing m to m+1 tilts by L, yielding a strictly positive multiple of Var_m(cos theta), so ratio increases from zero to sqrt(a/b). The endpoint difference of squares has sign p+q-1, proving the all-m one-trough dichotomy including equality. LLN and zero-drift CLT give limiting 0, 1/2, 1, and continuity at p+q=1 gives arbitrarily late last negative increment. Independent direct rational enumeration at (p,q)=(9/10,2/5) gave J_0=9/10, J_1=441/500, J_2=22221/25000. Finiteness of such checks is not used for the infinite proof.

## originality

PASS

Berend and Sapir (2005) prove average correctness monotonicity of randomly selected subcommittees when every voter has competence >=1/2. Their complete author-shared theorem and proof were inspected; neither the all-competent hypothesis nor random-subcommittee comparison applies to a prescribed nested sequence adding one voter with q<1/2 each step. The 2007 dependent-voter extension also considers randomly selected subcommittees, and Hartmann–Rafiee Rad (2016) use general heterogeneous majority calculations as baseline for deliberation rather than proving the sharp single-trough law. Resultary related mixed/jury papers treat correlated or exchangeable regimes. No located result implies the full nonmonotone deterministic alternation theorem. Best-of-knowledge rather than unqualified priority.

## value

PASS

A sharp all-jury-size classification for deterministic recruitment of mixed-competence independent voters answers a natural finite-committee decision question that is not settled by classical homogeneous or randomly sampled Condorcet monotonicity. The explicit exact one-trough boundary, strict-size comparisons, and arbitrarily delayed recovery are mathematically substantive and can inform attempts to understand or optimize heterogeneous majority-panel sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
