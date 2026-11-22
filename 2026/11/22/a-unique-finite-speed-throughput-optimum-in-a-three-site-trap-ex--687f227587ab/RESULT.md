# A unique finite-speed throughput optimum in a three-site trap-exclusion channel

## Finding

A site-disordered, boundary-driven symmetric exclusion channel can have a **unique strict optimum at a finite, nonhomogeneous interior departure rate**, even though increasing that rate without bound is allowed. More precisely, for each admissible nonzero reservoir-density contrast, the three-site model below has one and only one current-maximizing centre dwell time \(t_*(\rho,\Delta)\), which lies in \((0,1)\). Its current is larger than the homogeneous current when \(0<t<1\), smaller when \(t>1\), and tends back to the homogeneous current as \(t\downarrow0\). The same system has an exactly odd but genuinely nonlinear current response for every \(t\ne1\).

The exact current (positive from left to right) is
\[
J(\rho,\Delta,t)=\frac{\Delta(2t+1)[t+1+\rho(t-1)]}{t(t-1)^2\Delta^2+8(t+1)(2t+1)[1+\rho(t-1)]}.
\]
Its finite-speed optimum is the unique positive root of the explicit quartic \(P_{\rho,\Delta}(t)\) in the proof. At \(\rho=1/2\), \(\Delta=1\), the optimum and current are exactly
\[
t_* = \frac{\sqrt 3-1}{2},\qquad J(t_*)=\frac{3\sqrt 3-2}{23}>\frac18=J(1).
\]

## Assumptions and scope

There are exactly three sites, each with occupancy \(\eta_i\in\{0,1\}\). A particle at a boundary site hops to the vacant adjacent site at rate \(1/2\). The centre site has dwell-time multiplier \(t>0\): a centre particle hops to either vacant neighbour at rate \(1/(2t)\). Every move is suppressed if its destination is occupied.

The left boundary injects into a vacancy at rate \(\rho_{\mathrm L}/2\) and removes a particle at rate \((1-\rho_{\mathrm L})/2\). The right boundary likewise exchanges at rates \(\rho_{\mathrm R}/2\) and \((1-\rho_{\mathrm R})/2\), with
\[
\rho_{\mathrm L}=\rho+\Delta/2,\qquad \rho_{\mathrm R}=\rho-\Delta/2,
\quad 0<\rho<1,\quad 0<\Delta\leq2\min\{\rho,1-\rho\}.
\]
Thus the centre's *departure speed* is proportional to \(1/t\). The positive stationary mean current \(J\) counts a rightward successful hop across either interior bond as \(+1\) and a leftward hop as \(-1\), per unit time and per bond. The finite-state process is irreducible throughout this domain. All time and rate units use equal boundary dwell and contact times equal to one. Negative contrasts follow by spatial reflection.

## Proof

**Exact stationary current.** Enumerate states in binary lexicographic order \(000,001,010,011,100,101,110,111\). Define the column generator \(Q\) by the stated transition rates, including the diagonal negative exit-rate sums. Replace its last row by eight ones to obtain \(A\), let \(b=(0,0,0,0,0,0,0,1)^\top\), and solve \(A\pi=b\). This enforces \(Q\pi=0\), \(\sum\pi=1\). The current row has entries
\[
c_\eta=\tfrac12\eta_1(1-\eta_2)-\tfrac1{2t}\eta_2(1-\eta_1).
\]
Exact rational elimination gives \(c\pi=J\) as displayed under Finding. The accompanying `verify.py` constructs \(Q\) from transitions, eliminates its eight unknown probabilities, and checks the identity symbolically; it independently verifies that the other bond current and the left-reservoir net current equal the same expression. Therefore this is a full stationary-generator identity, not a mean-field approximation or an inference from simulations.

**Global optimization.** Write the positive denominator of \(J\) as
\[
B=t(t-1)^2\Delta^2+8(t+1)(2t+1)[1+\rho(t-1)]>0.
\]
Direct differentiation yields \(\partial_t J=-\Delta P_{\rho,\Delta}(t)/B^2\), where \(P_{\rho,\Delta}(t)=\sum_{j=0}^4 p_jt^j\), with
\[
\begin{aligned}
p_4&=2(1+\rho)(\Delta^2+16\rho),\\
p_3&=2(3-\rho)(\Delta^2+16\rho),\\
p_2&=8\rho(5-3\rho)-(3\rho+5)\Delta^2,\\
p_1&=-4(1-\rho)(\Delta^2+4\rho),\\
p_0&=(1-\rho)(\Delta^2-8\rho).
\end{aligned}
\]
The physical contrast bound gives \(\Delta^2\leq4\rho(1-\rho)\). Consequently \(p_4,p_3>0\),
\[
p_2\geq4\rho(5-4\rho+3\rho^2)>0,
\]
and \(p_1,p_0<0\). The ordered coefficient signs are therefore \(+,+,+,-,-\), with precisely one sign change. Descartes' rule bounds the number of positive roots by one. Since \(P(0)<0\) and \(P(1)=144\rho>0\), continuity supplies exactly one positive root \(t_*\in(0,1)\). The derivative is positive before that root and negative thereafter. Hence this root is the unique global maximizer over all \(t>0\).

**Sharp comparison and nonlinearity.** Algebraic subtraction gives
\[
J-\frac{\Delta}{8}=-\frac{\Delta t(t-1)[\Delta^2(t-1)+8\rho(2t+1)]}{8B}.
\]
The final bracket is positive: for \(0<t<1\) it is at least \(8\rho-\Delta^2>0\), and for \(t\geq1\) positivity is immediate. It follows that \(J>\Delta/8\) for \(0<t<1\) and \(J<\Delta/8\) for \(t>1\). The exact formula gives \(\lim_{t\downarrow0}J=J(1)=\Delta/8\), and \(\lim_{t\to\infty}J=0\). Finally, the denominator depends on the contrast only through \(\Delta^2\); hence \(J(-\Delta)=-J(\Delta)\), yet for \(t\ne1\), \(J/\Delta\) strictly decreases with \(|\Delta|>0\). This proves genuine odd nonlinearity without rectification. At the specified fully biased half-density example, the quartic factors as \(\tfrac32(3t+1)^2(2t^2+2t-1)\), giving the stated radical optimum and current.

## Verification

Run `python verify.py` with SymPy installed. It builds the eight-state generator directly from the model, solves its normalized stationary equations, checks the closed current on both bonds and at the reservoir, verifies differentiation, all limiting identities, the quartic factorization and the exact special case, and performs 45 admissible rational CTMC sample checks. It completed successfully in the supplied package. The proof for the continuum of admissible parameters uses exact rational identities and sign inequalities, not the finite sample checks.

## Relationship to prior work

Sakai and Akimoto (2026, arXiv:2609.03560) introduce and study the corresponding boundary-driven site-trap exclusion model with a general landscape, using a Galerkin linear-response approximation and a higher-order closure for nonlinear response. Their exact spatial-reflection argument explains why this symmetric single-defect channel cannot rectify, but the inspected work does not supply this three-site full-current identity or optimize a centre departure rate. The present result adds an exact all-contrast control optimum: **infinite departure speed is strictly suboptimal** even though the landscape is reflection symmetric. Their earlier periodic, externally biased model (arXiv:2512.03316) addresses a different driving protocol. Derrida, Douçot and Roche (2004) cover open homogeneous exclusion current statistics; the homogeneous case here is recovered at \(t=1\).

## Limitations

This is a three-site, hard-core, continuous-time model with equal endpoint waiting and contact scales. It does not claim an analogous optimum for larger channels, different contact kinetics, or a general disordered landscape. The fast-centre endpoint \(t\downarrow0\) is a limit, not a process with zero dwell time. The exact claim is about stationary **mean current**, not the variance, thermodynamic efficiency, or finite-time throughput. The positive-contrast optimization excludes the trivial zero-current case \(\Delta=0\); a unique optimum of the linear-response conductance can be considered separately. Publication priority relative to any unindexed exact finite-chain treatment remains uncertain.

## References

1. I. Sakai and T. Akimoto, *Sample-specific rectification-like response in a boundary-driven exclusion process*, arXiv:2609.03560, first submitted 2026-09-03. https://arxiv.org/abs/2609.03560
2. I. Sakai and T. Akimoto, *Symmetry breaking of current response in disordered exclusion processes*, arXiv:2512.03316, first submitted 2025-12-03. https://arxiv.org/abs/2512.03316
3. B. Derrida, B. Douçot, and P.-E. Roche, *Current Fluctuations in the One-Dimensional Symmetric Exclusion Process with Open Boundaries*, Journal of Statistical Physics 115, 717–748 (2004). https://doi.org/10.1023/B:JOSS.0000022379.95508.b2
4. I. Sakai and T. Akimoto, *Unexpected effects of disorder on current fluctuations in the symmetric simple exclusion process*, Physical Review E 111, 014134 (2025). https://doi.org/10.1103/PhysRevE.111.014134
