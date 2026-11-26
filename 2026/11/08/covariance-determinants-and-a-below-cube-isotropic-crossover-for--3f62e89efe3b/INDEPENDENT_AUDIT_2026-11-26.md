# Independent mathematical audit

## correctness

PASS

Independent layer-maxima reconstruction: the pushforward of volume under M_i=max_j X_ij has density ∏ m_i M_i^(m_i−1) on ∑M_i≤1, so its integral is ∏m_i!/d! and the normalized law including the slack is Dirichlet(m_1,…,m_k,1). Given each maximum M_i, the maximum label is uniform and other coordinates are independent uniform on [0,M_i], independently across layers. This gives the stated means and diagonal, same-layer and distinct-layer mixed moments after integrating the Dirichlet moments. In the normalized block basis the off-block terms equal −h_i h_j, while adding h_i² back to a block diagonal entry leaves (m_i+1)(2m_i+1)/(6D). The contrasts carry λ_i, and the rank-one determinant lemma gives the displayed factor and R≥1/(d+1). With fixed k and p_i≥ε, λ_i=(p_i²/12)(1+O_{k,ε}(1/d)), a_i stays bounded away from zero and R→1/4 uniformly. Hence log detΣ=−d log12+2d∑p_i log p_i+O_{k,ε}(1). Stirling puts +(k−1)log d/2 in log volume; subtraction gives the stated leading negative defect. The cube cases k=1 and the triangle (1,1) agree, and the (30,30) strict opposite comparison holds by exact arithmetic. Replay: python3 /workspace/branches/independent_exact_replay.py independently builds the covariance via maxima and uses rational elimination and exact ratio comparisons in dimensions 2, 6, and 60; computed L² for (30,30) is approximately 0.0828036003. The frozen checker was inspected but not executed. This is not a uniform-as-k-grows assertion; the O bound is on sets with a fixed positive lower bound on proportions.

## originality

PASS

Pass for the factorized chain determinant and corresponding chain-polytopal comparison in the noncongruent k≥3 case. The standard volume, contrasts, and exact two-layer comparisons are covered or immediately recoverable. The order determinant and trace-gap matches are substantial but do not supply the across-layer chain mean-block factor. No priority inference is made from the same-day record.

## value

PASS

The determinant is the affine-invariant covariance datum needed for precise isotropic comparisons in a natural family of vertex-anchored free sums. The product and rank-one factor avoids an unevaluated growing determinant, gives explicit dependence on every layer, and yields the direction and leading size of the isotropic defect beyond the congruent cases. The metric question is not answered by the earlier inertia trace alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
