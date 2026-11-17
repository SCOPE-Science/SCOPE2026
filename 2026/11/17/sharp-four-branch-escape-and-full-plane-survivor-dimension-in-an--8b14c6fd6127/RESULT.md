# Sharp four-branch escape and full-plane survivor dimension in an absolute-value planar map

## Finding
For every real \(c>1+\sqrt{3}\), the planar map
\[
T_c(x,y)=(|x|-1,\ x+c|y|-1)
\]
possesses a canonical compact forward-invariant set of bounded trajectories with a continuous one-parameter family of uniformly separated four-branch Cantor fibers. Its two-step dynamics on that set are topologically conjugate to an interval identity times the one-sided full four-symbol shift. The corresponding one-step entropy is \(\log 2\).

The Hausdorff dimension of **the full set of all bounded forward orbits in the plane**, including initial points outside the compact core, is exactly
\[
\boxed{1+\frac{\log 2}{\log c}}.
\]
In particular, that set has planar Lebesgue measure zero.

For initial conditions uniformly sampled by planar area from the canonical section strip defined below, the probability of surviving \(n\) two-step returns is exactly \((4/c^2)^n\). Therefore the first-exit clock is geometric, with mean \(c^2/(c^2-4)\). The bound \(c>1+\sqrt3\) is sharp for the stated **uniform, strictly separated four-full-branch property across every base phase**. This is not a claim that all lower parameters have zero entropy or no nontrivial invariant sets.

## Assumptions and scope
Fix \(c>1+\sqrt3\). Write the base coordinate on \([-1,0]\) as \(x=-u\) with \(0\le u\le1\), and set
\[
A_u=1+u,\quad B_u=2-u,\quad U_u=\frac{cA_u+B_u}{c^2-1},\quad J_u=[-U_u,U_u].
\]
The first and second images of the base coordinate are respectively \(-(1-u)\) and \(-u\). The second-return fiber map is
\[
H_u(y)=c\bigl|c|y|-A_u\bigr|-B_u.
\]
Define its compact nonescaping fiber
\[
K_u=\bigcap_{n\ge0}H_u^{-n}(J_u),
\]
and the planar core \(\mathcal K_c=\{(-u,y):u\in[0,1],\ y\in K_u\}\). Define the *global bounded-forward set* \(\mathcal B_c\) as all real initial conditions for which the complete forward orbit is bounded.

For the first-exit statement let \(\mathcal R_c=\{(-u,y):0\le u\le1,\ |y|\le U_u\}\), endowed with normalized two-dimensional Lebesgue area. Exit is observed at times \(2,4,6,\ldots\) by requiring each return coordinate to remain in its phase-specific interval \(J_u\).

## Proof
**1. Exact return map and escape boundary.** The scalar base map \(x\mapsto|x|-1\) carries every initial real \(x\) into \([-1,0]\) in finitely many steps: positive values greater than one decrease by one until they enter \([0,1]\), and negative values below \(-1\) first become positive. Inside \([-1,0]\), the base map is the involution \(-u\mapsto-(1-u)\), and direct substitution gives the displayed formula for \(H_u\).

The positive number \(U_u\) is an outer fixed point of \(H_u\): \(H_u(U_u)=H_u(-U_u)=U_u\). For any \(\delta>0\),
\[
H_u(U_u+\delta)=H_u(-U_u-\delta)=U_u+c^2\delta.
\]
Since \(c^2>1\), a return coordinate outside \(J_u\) has future return coordinates tending to \(+\infty\). Conversely, every return orbit remaining in \(J_u\) is bounded, as are its intervening odd steps. Thus \(K_u\) is precisely the bounded-return set in that fiber, and
\[
\mathcal B_c=\bigcup_{m\ge0}T_c^{-m}(\mathcal K_c).
\]

**2. The sharp four-branch condition.** The four monotone pieces of \(H_u\) are separated by \(-A_u/c,0,A_u/c\), with fold values \(H_u(\pm A_u/c)=-B_u\) and \(H_u(0)=cA_u-B_u\). Each monotone piece covers the entire interval \(J_u\), with strict excess at the interior turning values, precisely when
\[
U_u<B_u\quad\text{and}\quad cA_u-B_u>U_u.
\]
Elementary rearrangement, using \(L=c-2/c\), yields
\[
L^{-1}<A_u/B_u<L.
\]
The ratio \(A_u/B_u\) ranges monotonically from \(1/2\) to \(2\) as \(u\) ranges from zero to one. Hence all phases satisfy the strict four-full-branch condition exactly when \(L>2\), or \(c>1+\sqrt3\). At equality one extremal phase has a fold image on the target boundary; below equality at least one phase fails the strict four-branch condition. This proves sharpness in the claimed sense.

For each \(\sigma,\tau\in\{-1,1\}\), the four inverse branches defined on the entire \(J_u\) are
\[
g_{\sigma,\tau,u}(t)=\frac{\sigma}{c}\left(A_u+\frac{\tau(t+B_u)}{c}\right).
\]
The inequalities above prove that each branch maps \(J_u\) into its distinct monotonicity interval, all four images are pairwise disjoint compact subintervals of \(J_u\), and \(H_u\circ g_{\sigma,\tau,u}\) is the identity on \(J_u\). The two outer images meet the outer boundary of \(J_u\) only at its endpoints; this does not affect pairwise positive separation. Their common contraction modulus is exactly \(c^{-2}\). Since the phase interval is compact and all inequalities are strict uniformly in \(u\), there is a single positive separation constant for the four first-level images.

**3. Symbolic dynamics and entropy.** By the disjoint contraction construction, every infinite sequence of the four branch labels selects a unique point of \(K_u\); different sequences select different points. The coding varies continuously with \(u\), uniformly over all symbolic sequences, and has a continuous inverse. Accordingly, \(\mathcal K_c\) is homeomorphic to \([0,1]\times\{1,2,3,4\}^{\mathbb N}\), under which \(T_c^2\) acts as the identity on the first factor and the left shift on the second. The core is forward invariant under \(T_c\) because bounded trajectories remain bounded. The topological entropy identity \(h_{\rm top}(T_c^2|\mathcal K_c)=2h_{\rm top}(T_c|\mathcal K_c)\) gives \(h_{\rm top}(T_c|\mathcal K_c)=\log2\).

**4. Hausdorff dimension.** At each fixed phase the four inverse branches are similarities of equal ratio \(c^{-2}\) with disjoint images, so the elementary strong-separation dimension argument gives
\[
s=\dim_H(K_u)=\frac{\log4}{2\log c}=\frac{\log2}{\log c}.
\]
The contraction maps have \(u\)-derivatives bounded by \(c^{-1}+c^{-2}\). Consequently the depth-\(n\) cylinder maps, and their limiting coding graphs over \(u\), are uniformly Lipschitz, with Lipschitz constant at most \((c^{-1}+c^{-2})/(1-c^{-2})\). Covering each of the \(4^n\) cylinder graph strips by \(O(c^{2n})\) squares of side \(O(c^{-2n})\) gives \(\dim_H\mathcal K_c\le 1+s\).

For the reverse inequality, assign each phase fiber its equal-weight four-symbol Bernoulli measure. The uniform first-level separation and equal contraction ratios yield a uniform Frostman estimate \(\nu_u(I)\le C|I|^s\) for any interval \(I\), where \(C\) is independent of the phase. Integrating these measures over \(u\in[0,1]\) gives a probability on \(\mathcal K_c\) whose mass in every radius-\(r\) planar ball is at most \(C' r^{1+s}\). The mass distribution principle yields \(\dim_H\mathcal K_c\ge1+s\).

On each of the finitely many affine quadrant pieces, \(T_c\) is invertible and has nonzero Jacobian determinant of absolute value \(c\). Every finite iterate has finitely many such pieces; each inverse branch is affine-Lipschitz on its domain. The displayed countable-union formula for \(\mathcal B_c\) therefore implies \(\dim_H\mathcal B_c=\dim_H\mathcal K_c=1+s\). Since \(c>1+\sqrt3>2\), this is strictly less than two, proving area zero.

**5. Exact first-exit law.** Each depth-\(n\) inverse cylinder of \(H_u\) has length \(2U_u c^{-2n}\), and the \(4^n\) cylinders are disjoint. Consequently, for each fixed \(u\), the fraction of the original interval \(J_u\) that avoids exit for \(n\) returns is exactly \(4^n c^{-2n}\). This fraction does not depend on \(u\); integrating with the actual section-area weight \(2U_u\,du\) gives
\[
\Pr_{\mathcal R_c}(\text{no exit at returns }1,\dots,n)
=\left(\frac4{c^2}\right)^n\quad(n\ge0).
\]
The first-exit return index is thus geometric on positive integers, with parameter \(1-4/c^2\) and mean \(c^2/(c^2-4)\). This completes the proof.

## Verification
The accompanying dependency-free script `verify.py` uses exact rational arithmetic to check all four inverse identities, strict branch gaps, first-level values, and all depth-one through depth-four cylinder lengths for thirty-five parameter/phase pairs. It also checks strictness failure below the exact algebraic threshold and the outer escape identities. The successful output is `EXACT_FOUR_BRANCH_OK`, `SHARP_THRESHOLD_WITNESS_OK`, and `ESCAPE_IDENTITIES_OK`. These finite checks test the formulas; the universal quantifiers, countable-union dimension formula, and infinite symbolic conjugacy follow from the proof above, not from finite sampling.

## Relationship to prior work
Tikjha's 2026 four-partition map provides the model and studies inverse geometry, periodic orbits and bifurcations, and a different one-dimensional degeneracy. The present result concerns the complementary zero-horizontal-coupling slice with strongly expanding vertical dynamics and classifies its entire bounded-forward set, not isolated attracting cycles. Previous mathematical reports give complete inverse-fiber multiplicity information for other parameter chambers and an exact period-four core for the same family at \(c=1\); neither determines the bounded-repeller dimension or first-exit distribution in the regime \(c>1+\sqrt3\). Kim and Ju (2014) study dimensional properties of broader skew-product attractors under different dynamical hypotheses; the general equal-ratio similarity dimension formula is standard and is not claimed as new. What is asserted here is the explicit sharp construction, exact phase-uniform survival law, and full-plane bounded-set identification for the specified recent model.

## Limitations
All conclusions require the strict inequality \(c>1+\sqrt3\) and zero horizontal coupling. The threshold only characterizes uniform strictly separated four full branches across all phases; it does not classify all bifurcations at or below the threshold. The entropy is that of the canonical compact invariant core; no entropy is assigned to the noncompact global bounded-forward set. The exact geometric law uses normalized planar area on the stated natural section and the two-step first-exit clock, not arbitrary initial distributions. No claim is made about robustness for nonzero horizontal coupling, unique physical invariant measures, or complete historical priority. Mathematical validation beyond the present proof and reproducibility checks has not been performed.

## References
1. W. Tikjha, *Noninvertibility and Bifurcation Phenomena in a Four-Partitions Piecewise Linear Map*, arXiv:2607.13519 (first public version 15 July 2026), https://arxiv.org/abs/2607.13519.
2. J. Kim and H. Ju, *Dimension theoretical study on skew product maps with coupled-expanding property*, arXiv:1401.3206 (2014), https://arxiv.org/abs/1401.3206.
3. Standard equal-ratio iterated-function-system separation theorem and the mass distribution principle; the particular separation and measures required here are explicitly constructed above.
