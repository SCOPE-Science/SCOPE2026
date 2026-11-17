# Independent mathematical audit

## correctness

PASS

The number K=floor(L/2) of extra starting-vertex visits has tails P(K≥j)=t^j with t=(1−p)². For any two-walk coupling, Var((K1+K2)/2)=(μ+E K1K2)/2, μ=t/(1−t). Layer-cake and Fréchet give E K1K2 ≥ J(t)=Σ_{j,k≥1}(t^j+t^k−1)_+, and the inverse-CDF antitone coupling attains each event intersection bound simultaneously. Stagewise survival has P(L1≥u,L2≥v)=r^{min(u,v)}q^{|u−v|}, r=(1−2p)_+; summing even tails yields M_stage=r²(1+t)/((1−r²)(1−t)). The strict p<1/2 loss follows already from j=k=1 excess (with no negative excess elsewhere). The p=1/3 triple (2/5,9/16,18/25) and 5 rational cases were independently checked. With ε=1−t, εK(U)→−log(1−U), εK(1−U)→−log U and dominated convergence gives ∫log u log(1−u)du=2−π²/6. Universal optimality rests on the full Fréchet proof, not finite tests.

## originality

PASS

Best-of-knowledge PASS for the complete sharp benchmark, not for global antithetic coupling as a method: inverse-CDF rearrangement and graph-walk OT are explicitly known. Earlier graph-feature papers optimize a bilinear kernel/feature cost, not this single-walk linear Green diagonal with exact unrestricted p thresholds and rare-stopping ratio. A hidden specialized marginal coupling example remains possible.

## value

PASS

An exact optimization over ALL legal joint length laws on the simplest nontrivial walk gives a reference benchmark for stagewise antithetic algorithms, identifies two distinct parameter thresholds and quantifies the asymptotic efficiency gap. The two-state graph is motivated as the minimal nontrivial resolvent test, and explicit sharp all-p comparisons are not merely a renamed textbook formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
