# Exact orientation-dependent Floquet multipliers for circular-arc oscillators

## Finding
For the piecewise-cubic circular-arc oscillator of Kai and Maehara, the transverse multiplier has an explicit product of continuous contraction factors and interface factors. Reversing every angular velocity **reciprocates the geometric interface factor** rather than preserving it. The four-arc geometry illustrated in their numerical example consequently supports a rigorously repelling clockwise periodic orbit when the four angular coefficients are \(-1000\).

Let \(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\). Write the branch dynamics as
\[
\dot z=\omega_iJ\nabla V_i(z)-V_i(z)\nabla V_i(z),\qquad V_i(z)=|z-c_i|^2-R_i^2.
\]
The arc \(S_i\) is the segment of the circle \(V_i=0\) in the sector between rays through \(P_i\) and \(P_{i+1}\). Suppose it is traversed with no tangency, in the cyclic order \(1,\ldots,N\) when all \(\omega_i>0\), and in reverse order when all \(\omega_i<0\). Set \(e_i=P_i/|P_i|\),
\[
d_j(P_i)=\langle e_i,P_i-c_j\rangle,
\quad
G=\prod_{i=1}^N\frac{d_i(P_i)}{d_{i-1}(P_i)},
\]
with indices cyclic, and require both one-sided crossing distances to be positive at each switch. If \(\psi_i\in(0,2\pi)\) is the unsigned central angle of arc \(S_i\), then its nontrivial transverse multiplier is
\[
\Lambda_+=G\exp\!\left(-\sum_{i=1}^N\frac{2R_i^2\psi_i}{\omega_i}\right)
\quad(\omega_i>0),\qquad
\Lambda_-=G^{-1}\exp\!\left(-\sum_{i=1}^N\frac{2R_i^2\psi_i}{|\omega_i|}\right)
\quad(\omega_i<0).
\]

For the four-arc data below, \(G=261/7942\). Consequently, when all \(\omega_i=-1000\),
\[
\Lambda_->\frac{7942}{261}\exp\!\left(-\frac{4\pi}{1000}\cdot\frac{416235}{23716}\right)>24>1.
\]
Thus the periodic orbit is **transversely repelling**. Its precise numerical multiplier is approximately \(26.71577\), but the strict analytic bound alone proves instability.

## Assumptions and scope
Take distinct nonzero \(P_i\) in counterclockwise order, sector-wise circular arcs \(S_i\) joining successive \(P_i\) through specified \(Q_i\), and no tangencies at radial interfaces. Assume each branch field crosses the corresponding interface in the direction dictated by the common sign of \(\omega_i\). The example uses
\[
\begin{aligned}
&P_1=(1,0),\;P_2=(0,2),\;P_3=(-3,0),\;P_4=(0,-4),\\
&Q_1=(1,2),\;Q_2=(-4,3),\;Q_3=(-5,-2),\;Q_4=(2,-3).
\end{aligned}
\]
The \(Q_i\) are interior to their sectors and determine outward circular arcs as in the original construction. This is a statement about the corresponding exact piecewise classical crossing orbit; no global uniqueness, basin assertion, sliding solution, or generic stability is assumed.

## Proof
**1. Within-sector variational contraction.** Since \(\nabla V_i=2(z-c_i)\), the scalar defect satisfies
\[
\dot V_i=-V_i|\nabla V_i|^2=-4|z-c_i|^2V_i.
\]
On the periodic circle \(V_i=0\), the first variation of \(V_i\) decays with rate \(4R_i^2\). On that circle \(\dot z=2\omega_i J(z-c_i)\), so the traversal time of its arc is \(\psi_i/(2|\omega_i|)\). The resulting linear defect factor is exactly \(\exp(-2R_i^2\psi_i/|\omega_i|)\).

**2. Interface derivatives.** On the ray \(z=se_i\) at its switching point \(P_i=s_ie_i\),
\[
V_j(se_i)=2d_j(P_i)(s-s_i)+O((s-s_i)^2).
\]
Therefore rewriting the same infinitesimal radial displacement in the new sector's defect coordinate multiplies it by \(d_{\mathrm{new}}(P_i)/d_{\mathrm{old}}(P_i)\). This is a direct Poincaré-section calculation (equivalently, the scalar form of the saltation factor). In counterclockwise order the product is \(G\); traversing the same interfaces clockwise exchanges old and new and gives \(G^{-1}\). Composing these factors with the within-sector contractions proves both formulas. Since the return section is one-dimensional, the resulting positive factor is precisely the nontrivial Floquet multiplier; the autonomous phase direction contributes the trivial multiplier \(1\).

**3. Exact four-arc geometry.** Solving the three-point circle equations for each triple \(P_i,Q_i,P_{i+1}\) gives
\[
\begin{aligned}
&c_1=(1/2,1),&R_1^2&=5/4,\\
&c_2=(-47/22,43/22),&R_2^2&=1105/242,\\
&c_3=(-33/14,-37/14),&R_3^2&=725/98,\\
&c_4=(3/14,-27/14),&R_4^2&=425/98.
\end{aligned}
\]
All relevant \(d_j(P_i)\) are strictly positive. At the four interfaces the ratios \(d_i(P_i)/d_{i-1}(P_i)\) are, in order,
\[
\frac7{11},\quad\frac1{22},\quad\frac{99}{133},\quad\frac{29}{19};
\qquad G=\frac{261}{7942}.
\]
The radii obey \(\sum_iR_i^2=416235/23716\). Since every arc's unsigned central angle lies strictly between \(0\) and \(2\pi\), at \(\omega_i=-1000\)
\[
0<\sum_i\frac{2R_i^2\psi_i}{1000}<\frac{4\pi}{1000}\frac{416235}{23716}<0.221.
\]
This yields the displayed lower bound above \(24\), proving a repelling clockwise cycle despite each sector's strictly contracting normal dynamics.

## Verification
The standalone `check.py` in this package reconstructs the four circles using rational arithmetic, checks the four switching ratios and their product, evaluates the exact instability inequality, and independently calculates the circular central angles as a supplementary numerical check. The reported output is `FOUR_ARC_CLOCKWISE_REPELLING_EXACT_GEOMETRY_OK`. The proof of instability needs only the exact rational geometry and the elementary bound \(\psi_i<2\pi\), not floating-point central-angle estimates.

## Relationship to prior work
Kai and Maehara (2023) introduce exactly this piecewise nonlinear construction, prove the closed orbit and state stability under a further **admissible-strip** condition; their numerical section uses these same four points and moderate negative angular speeds. Their article gives orbital periods but no transverse multiplier or interface-product formula. The geometric multiplier demonstrates why orientation reversal or increasing speed cannot be treated as neutral for stability. General saltation/variational principles underlie the proof; no new general saltation theorem is claimed. In particular, this example does **not** establish that their auxiliary admissible-strip hypothesis is satisfiable at the high-speed parameters, and it does not purport to disprove their theorem interpreted strictly with all its premises.

## Limitations
The explicit repelling conclusion applies to the listed four-arc geometry and \(\omega_i=-1000\), with ordinary transverse crossing at every switch. The general multiplier formula requires the stated regular crossing assumptions. The original article's admissible-strip condition has not been certified for this example, so only an unconditional clockwise-stability interpretation is ruled out. This is an analytical same-author-independent argument, not an independent externally certified validation. Potential unindexed equivalent calculations remain a publication-priority risk.

## References
1. T. Kai and K. Maehara, *Design and Analysis of Piecewise Nonlinear Oscillators with Circular-Type Limit Cycles*, IEICE Transactions on Fundamentals E106-A (2023), 1234–1240, doi:10.1587/transfun.2022EAP1116 (first public advance publication 2023-03-20). Specifically equations (3)–(7), (17)–(19), Theorem 1 and the four-arc example in Section 4. https://doi.org/10.1587/transfun.2022EAP1116
2. Standard variational-flow and saltation-map identities for transverse switches in piecewise-smooth planar systems; here the interface derivative is reconstructed directly from the circle equations, without requiring an external saltation theorem.
