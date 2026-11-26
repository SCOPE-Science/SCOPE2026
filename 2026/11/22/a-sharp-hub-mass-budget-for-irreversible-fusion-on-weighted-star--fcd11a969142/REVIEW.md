# Independent mathematical audit

## correctness

PASS

Soft-thresholding each leaf about hub h leaves a scalar hub KKT equation with clipped terms and strictly positive slope at least m_0; the unique solution yields fusion exactly when |h-y_i|≤λa_i/m_i. To check persistence at simultaneous events, scale by τ=1/λ and write v=τh and q_i=v-τy_i. On every incident affine clip-pattern cell with unsaturated set I, let M_I=m_0+Σ_{j∈I}m_j and S be the saturated signed penalty sum. At an upper contact q_i=c_i=a_i/m_i, the branch slope satisfies τM_I q_i'=M_Ic_i+S. If i is unsaturated then M_I≥m_0+m_i and S≥-Σ_{j≠i}a_j; if i is saturated then its sign is positive, S≥a_i-Σ_{j≠i}a_j and M_I≥m_0. Both bounds give q_i'≥0 by the local budget; at a lower contact the mirrored bounds give q_i'≤0. A branch identically on the boundary has slope zero. Thus no affine piece on the decreasing-τ side can leave the fused strip, including ties and simultaneous changes. For λ=0, the tied-to-hub leaves can form one fused block for small positive λ: all strictly unequal data stay outside the clipped strips, since |h-y_0|≤λΣa_j/m_0, and the tied block's drift divided by λ has magnitude at most Σ_{outside}a_j/M_I≤a_i/m_i for every tied leaf by its own budget. This handles initial exact ties. For failure on leaf i, take y_0=0, y_i=H>0 and the rest very large, so the other leaves stay above the hub on a chosen finite interval (use the same uniform bound on |h-y_0|). Writing B=Σ_{j≠i}a_j and c=(m_0+m_i)a_i/m_i<B, the fused KKT solution exists exactly for m_0H/(B+c)≤λ≤m_0H/(B-c) there. An interior test and a later test beyond the upper endpoint give actual fusion followed by separation. The stated four-leaf rational fits satisfy the clipping and hub equations. Q=BM^-1B^T has diagonal a_i²(1/m_0+1/m_i) and off-diagonal a_i a_j/m_0; its weak dominance inequality is exactly the local budget. Normalizing the weights to sum one changes this budget to a_i/Σa_j≥m_i/(m_0+2m_i); the sum condition is necessary and distributing any slack proves feasibility even at equality. This includes k=1 and the stated equal-mass examples. VERIFICATION.md and checks/verify_star_fusion.py were inspected; the optional replay path is python3 checks/verify_star_fusion.py from the package root, not a substitute for the proof.

## originality

PASS

A stronger prior sufficient result than the frozen citation alone was identified: Duan et al. already give primal coordinatewise shrinkage after the exact full-row-rank TV-to-lasso reduction under weak diagonal dominance. The sufficiency and its algebraic rewriting are not new. The surviving content is the sharp necessity for universal persistence with a genuine positive-length fusion-then-separation witness for any failed star row, and the resulting penalty-design feasibility for this path property. Same-day weighted-path and star-variation records overlap substantively but do not state that surviving result for branching stars. Historical priority remains provisional.

## value

PASS

An exact obstruction determines whether an irreversible-merge rule is universally sound on the fundamental branching graph and whether any positive edge-weight design can make it so. The converse supplies actual splitting after a nondegenerate interval, not merely a failed certificate, and the equal-mass four-spoke obstruction shows that tuning all the penalties cannot always fix it. The known sufficient criterion and the mass algebra alone are not the contribution. No general graph or statistical risk claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
