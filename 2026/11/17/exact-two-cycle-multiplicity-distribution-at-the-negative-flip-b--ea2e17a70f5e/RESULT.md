# Exact two-cycle multiplicity distribution at the negative-flip boundary of quasi-affine maps

## Finding
Consider the one-dimensional spatially discretized affine map
\[
f_{\varepsilon,\mu}(x)=\big\lfloor(-1+\varepsilon)x+\mu\big\rfloor,
\qquad 0<\varepsilon\le\tfrac12,\quad \mu\in\mathbb R.
\]
Let \(N_\varepsilon(\mu)\) be its number of *primitive, unordered* two-cycles, not its number of period-two points. Put \(d=2-\varepsilon\). Translation by an integer conjugates the map at \(\mu\) to the map at \(\mu+d\), so \(N_\varepsilon\) is \(d\)-periodic. If \(\mu\) is sampled uniformly from any interval of length \(d\), then for every integer \(m\ge1\), its **entire finite-parameter multiplicity distribution** is
\[
\boxed{
\Pr\big(N_\varepsilon\ge m\big)
=\frac{(1-(2m-1)\varepsilon)_++(1-2m\varepsilon)_+}{2-\varepsilon},
}\qquad (a)_+=\max\{a,0\}.
\]
This includes the exact expected number of two-cycles. Writing
\(K=\lceil1/\varepsilon\rceil-1\),
\[
\boxed{\mathbb E N_\varepsilon
=\frac{K-\varepsilon K(K+1)/2}{2-\varepsilon}.}
\]
The phase-resolved singular limit is uniform in the offset. Define \(v=\{\mu/d\}\in[0,1)\), \(w=v-\tfrac12\lfloor2v\rfloor\in[0,1/2)\), and the triangular, one-half-periodic function
\[
F(v)=\min\{2w,1-2w\}=2\operatorname{dist}(v,\tfrac12\mathbb Z).
\]
Then
\[
\boxed{\sup_{\mu\in\mathbb R}\big|\varepsilon N_\varepsilon(\mu)-F(\{\mu/(2-\varepsilon)\})\big|\le\tfrac32\varepsilon.}
\]
In particular, for uniformly distributed \(\mu\) on an offset period,
\[
\boxed{\varepsilon N_\varepsilon(\mu)\ \Longrightarrow\ \operatorname{Unif}[0,\tfrac12],}
\]
with distribution-function discrepancy at most \(3\varepsilon\). Thus the number of cycles grows like \(\varepsilon^{-1}\) for generic offsets, but its leading coefficient varies deterministically with offset and is uniformly distributed under random offset calibration.

## Assumptions and scope
The floor function has the standard left-closed/right-open convention. Every map has the *real* domain \(\mathbb R\); after one iteration its dynamics is on \(\mathbb Z\). The specified range \(0<\varepsilon\le1/2\) places the slope in \((-1,-1/2]\). All probabilities are with respect only to uniformly sampled \(\mu\), not random time evolution or random initial states. Cycle multiplicities are finite for every such \(\varepsilon\), including at exceptional floor-boundary offsets. The weak-limit statement takes \(\varepsilon\downarrow0\) through arbitrary real values, not only reciprocal integers. The original 2024 cycle-enumeration theorem is a prerequisite and is not claimed as new.

## Proof
**Step 1: translation symmetry and the exact cycle-gap condition.** Write \(\lambda=-1+\varepsilon\). For every integer \(a\),
\[
f_{\varepsilon,\mu+da}(x+a)=f_{\varepsilon,\mu}(x)+a,
\]
so it suffices to use \(0\le\mu<d\). By the explicit period-two classification of Hoseana [1, Theorem 2], a primitive two-cycle with positive gap \(k\) exists precisely when \(1\le k<1/\varepsilon\) and
\[
\big\lfloor u_k\big\rfloor-\big\lfloor u_k-b_k\big\rfloor=1,
\qquad u_k=\frac{\mu-k}{d},\qquad b_k=\frac{1-\varepsilon k}{d}.
\]
Since \(0<b_k<1\), this is equivalent to \(\{u_k\}<b_k\), with strictness at the upper boundary. For each gap \(k\), at most one two-cycle exists. Different gaps correspond to different unordered cycles. Thus \(N_\varepsilon\) is the count of the gap events above.

**Step 2: exact parity selection and nested phase windows.** Put \(v=\mu/d\in[0,1)\), \(\sigma=\lfloor2v\rfloor\in\{0,1\}\), \(w=v-\sigma/2\in[0,1/2)\). Since
\[
\frac{k}{d}=\frac{k}{2}+\frac{\varepsilon k}{2d},
\]
the fractional-part test can be separated by the parity of \(k\). For \(0<\varepsilon\le1/2\), it has no solutions if \(k\not\equiv\sigma\pmod2\). For the matching parity, the test holds **exactly** when
\[
\boxed{
\frac{\varepsilon k}{2d}\le w<\frac{1-\varepsilon k/2}{d}.}
\tag{1}
\]
To justify the branch conditions, set \(s=\varepsilon k/(2d)<1/(2d)\). In the matching parity the fractional-part argument is \(w-s\); if \(w<s\), its fractional part is \(1+w-s\ge1-1/(2d)\ge1/d\ge b_k\), so there is no solution. Otherwise \(w-s\ge0\), and \(w-s<b_k\) rearranges to (1). In the opposite parity, the fractional-part argument equals either \(v-s\), with \(v\ge1/2\), or \(v-1/2-s\), with \(v<1/2\). In the former case the inequality would force \(\varepsilon k<2(1-dv)\le\varepsilon\), impossible for even \(k\ge2\); in the latter it would force \(dv<-\varepsilon(k-1)/2\), impossible for odd \(k\ge1\). Boundary values satisfy the same conclusions under the strict upper endpoint.

For each positive integer \(k\), the interval of \(w\) in (1) has length
\[
\ell_k=\frac{(1-\varepsilon k)_+}{d}.
\]
For \(\varepsilon k<1\), it lies entirely in \([0,1/2)\), is centered at \(1/(2d)\), and shrinks as \(k\) increases. Consequently, separately in the even and odd half-periods of \(v\), the success windows are *nested*. On the first half-period only even gaps \(2,4,6,\ldots\) occur, while on the second only odd gaps \(1,3,5,\ldots\) occur.

**Step 3: exact law under uniform offset.** The event \(N_\varepsilon\ge m\) consists of the phase interval for even gap \(2m\) in the first half-period, and the phase interval for odd gap \(2m-1\) in the second. Their lengths are \(\ell_{2m}\) and \(\ell_{2m-1}\), respectively. Because \(v\) is uniform on \([0,1)\), their sum is the exact survival probability in the Finding. By the layer-cake identity for integer-valued nonnegative variables,
\[
\mathbb E N_\varepsilon=\sum_{m\ge1}\Pr(N_\varepsilon\ge m)
=\sum_{k=1}^{K}\ell_k
=\frac{K-\varepsilon K(K+1)/2}{d}.
\]
This proves the asserted finite-parameter distribution and expectation without any appeal to numerical averaging.

**Step 4: uniform critical-window limit.** For fixed phase \(w\), (1) is equivalently
\[
\varepsilon k\le2dw,\qquad \varepsilon k<2(1-dw).
\]
Thus \(N_\varepsilon\) counts positive integers of a specified parity on the mesh \(2\varepsilon\), below the effective cutoff \(H_\varepsilon(w)=\min\{2dw,2(1-dw)\}\). For both parity choices, elementary counting of a half-open arithmetic progression gives
\[
\left|\varepsilon N_\varepsilon-\frac{H_\varepsilon(w)}2\right|\le\varepsilon.
\]
Since \(d=2-\varepsilon\) and \(w\in[0,1/2)\), the function \(a\mapsto\min\{aw,1-aw\}\) is \(w\)-Lipschitz, hence
\[
\left|\frac{H_\varepsilon(w)}2-\min\{2w,1-2w\}\right|
\le\varepsilon w\le\frac\varepsilon2.
\]
The stated uniform \(3\varepsilon/2\) bound follows. Under uniform phase \(v\), the two triangular peaks of \(F\) have constant total level-set density \(2\) on \((0,1/2)\); therefore \(F(v)\) is uniformly distributed on \([0,1/2]\). Its cumulative distribution function is \(2\)-Lipschitz on \(\mathbb R\). The coupling inequality yields a uniform distribution-function error at most \(2(3\varepsilon/2)=3\varepsilon\). The entire conclusion holds uniformly over floor discontinuity offsets.

## Verification
The companion `CHECK.py` independently enumerates primitive two-cycles by direct integer iteration, rather than calling the cycle-gap formula, for seven rational slopes and 121 offset phases each (847 exact cases). It compares the count with (1), verifies the phase inequality, and checks the survival-probability/expectation identity in rational arithmetic. It prints `QUASI_AFFINE_NEAR_FLIP_LAW_OK: 847 exact integer-orbit cases`. The proof above—not the finite test—is the justification for all real parameters, all cycle counts and the scaling law. Exact open/closed interval endpoints are included in the proof and checker.

## Relationship to prior work
Hoseana [1, Theorem 2] proved the full cycle enumeration formula for quasi-affine maps. The current result uses that enumeration as an input, then supplies a new **nested offset-interval representation**, an **exact law over the affine-offset parameter**, and a **uniform near-unit-flip scaling law**. These are statements about parameter-space cycle multiplicity, not an alternate presentation of the fixed-offset enumeration. The posted result [2] studies deterministic eventual basin assignment and large-state settling for this same family, with no offset-averaged cycle multiplicity or near-flip law in its inspected proof. Rozikov–Sattarov–Usmonov [3] concerns the no-offset case and does not imply the random-offset distribution. Analogies to random-parameter mode-locking in contracted circle rotations are not implication because their rotation-number and attractor-period observables are different. The full 2025 journal revision of [1] was not available to inspect; it remains an explicit potential-priority risk.

## Limitations
The theorem concerns the spatially discretized *one-dimensional* affine map, and the exact random-parameter law assumes Lebesgue-uniform offset on a full conjugacy period. It does not describe noisy trajectories, arbitrary offset distributions, slopes \(\varepsilon>1/2\), or stochastic perturbations of the floor rule. The research establishes the displayed formulas as deductions from [1] but does not claim priority over potentially inaccessible, unindexed or unpublished versions. No independent mathematical audit has been performed.

## References
1. J. Hoseana, *The dynamics of one-dimensional quasi-affine maps*, arXiv:2406.14055v1 (first publicly available 2024-06-20), https://arxiv.org/html/2406.14055v1 ; journal version, *Journal of Difference Equations and Applications* 31 (2025), 418–433, doi:10.1080/10236198.2024.2428386.
2. *Outermost-cycle basin selection and logarithmic settling for quantized affine contractions* (published research result, 2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-outermost-cycle-basin-selection-and-logarithmic-settling-for-qua--b81ca333b81c .
3. U. A. Rozikov, I. A. Sattarov and J. B. Usmonov, *The dynamical system generated by the floor function*, arXiv:1503.07129v1 (2015-03-24), https://arxiv.org/abs/1503.07129 .
