# Three endpoint phases for a binary discounted Bernoulli path maximum

## Finding

Consider independent Bernoulli-\(p\) marks \(B_v\) on the vertices of the complete rooted binary tree, with \(0<p<1\). Define the maximally discounted path score
\[
T_p=\sup_{\xi}\sum_{j=0}^{\infty}2^{-j}B_{\xi_j},\qquad D_p=2-T_p,\qquad F_p(x)=\Pr(D_p\le x).
\]
The supremum is over all infinite rays. The deterministic upper score is \(2\), so \(D_p\in[0,2]\). The sharp endpoint laws are:

- **Subcritical \(0<p<1/2\):** For each fixed \(0<x\le1\),
\[
 A_p(x)=\lim_{n\to\infty}(2p)^{-n}F_p(2^{-n}x)\in(0,\infty),
\]
with \(A_p(x/2)=2pA_p(x)\) and \(F_p(\varepsilon)\asymp\varepsilon^{\alpha_p}\), where \(\alpha_p=-\log_2(2p)>0\).
- **Critical \(p=1/2\):**
\[
 F_{1/2}(\varepsilon)\sim\frac{2\log 2}{\log(1/\varepsilon)}\qquad(\varepsilon\downarrow0).
\]
- **Supercritical \(1/2<p<1\):** An atom of mass \(r_p=(2p-1)/p\) occurs at the exact upper score (i.e., \(D_p=0\)), and for each \(0<x\le1\),
\[
 B_p(x)=\lim_{n\to\infty}[2(1-p)]^{-n}[F_p(2^{-n}x)-r_p]\in(0,\infty),
\]
with \(B_p(x/2)=2(1-p)B_p(x)\) and \(F_p(\varepsilon)-r_p\asymp\varepsilon^{\beta_p}\), where \(\beta_p=-\log_2[2(1-p)]>0\).

The dyadic limits provide positive finite scale-specific constants. The theorem does not assert continuity or nonconstancy of the scale amplitudes, or an all-scale limit after division by the stated power.

## Assumptions and scope

Marks at *all* vertices, including the root, are independent with the same success probability \(p\). Exactly two children emanate from every vertex. The score weights at generations \(j=0,1,\ldots\) are \(2^{-j}\). There are infinitely many generations, and every infinite ray is admissible. All assertions apply to every real \(p\in(0,1)\), and all limits are as the specified integer \(n\) tends to infinity or real \(\varepsilon\) decreases to zero. Natural logarithms are used. No general reproduction law or random discount is considered.

## Proof

**1. Well-defined optimum and recursive law.** The space of rays is the compact product \(\{0,1\}^{\mathbb N}\). The score is a uniform limit of cylinder-continuous partial scores, hence continuous and attains its maximum. The deficit is equivalently
\[
D_p=\min_\xi\sum_{j\ge0}2^{-j}(1-B_{\xi_j}).
\]
If \(D_1,D_2\) are independent copies of \(D_p\), and \(B\) is an independent Bernoulli-\(p\) mark at the root, then
\[
D_p\stackrel{d}{=}(1-B)+\tfrac12\min(D_1,D_2).
\]
For \(0\le x<1\), the root must have \(B=1\), giving the exact equation
\[
F_p(x)=f_p(F_p(2x)),\qquad f_p(y)=p(2y-y^2).
\tag{1}
\]

**2. The endpoint atom and an initial value.** The event \(D_p=0\) is exactly the existence of an infinite all-success ray. Writing its probability as \(r\), the finite-depth success events decrease and satisfy the iteration of \(f_p\), starting from \(p\). The limit is the largest fixed point of \(f_p\) in \([0,p]\), namely
\[
r_p=\begin{cases}0,&0<p\le1/2,\\(2p-1)/p,&1/2<p<1.\end{cases}
\tag{2}
\]
Because a root failure contributes at least one unit to the deficit, the event \(D_p\le1\) consists of a successful root (always allowed since the remaining deficit is at most one), or a failed root with at least one child having deficit exactly zero. Hence
\[
F_p(1)=p+(1-p)(2r_p-r_p^2).
\tag{3}
\]
For each \(x>0\), \(F_p(x)>r_p\): choose \(L\) with \(2^{-L}<x\), force every mark through generation \(L\) to be a success and every mark at generation \(L+1\) to fail. This positive-probability finite-cylinder event has \(0<D_p\le2^{-L}<x\). In particular \(F_p(x)>0\).

**3. Subcritical dyadic law.** Fix \(0<x\le1\) and put \(y_n=F_p(2^{-n}x)\). By (1), for all \(n\ge0\),
\[
y_{n+1}=2p\,y_n(1-y_n/2).
\tag{4}
\]
For \(a=2p<1\), \(0<y_n\le a^n y_0\), so \(\sum_n y_n<\infty\). Consequently
\[
a^{-n}y_n=y_0\prod_{j=0}^{n-1}(1-y_j/2)
\longrightarrow A_p(x)\in(0,\infty).
\tag{5}
\]
All factors lie strictly between zero and one, and summability makes the product positive. Replacing \(x\) by \(x/2\) proves \(A_p(x/2)=aA_p(x)\). Taking \(x=1\), and sandwiching arbitrary \(\varepsilon\) between consecutive dyadic thresholds, yields the two-sided power-order estimate in the statement.

**4. Critical logarithmic constant.** At \(p=1/2\), (4) becomes \(y_{n+1}=y_n-y_n^2/2\). Since its only fixed point below one is zero, \(y_n\downarrow0\), and
\[
\frac1{y_{n+1}}-\frac1{y_n}=\frac1{2-y_n}\longrightarrow\frac12.
\tag{6}
\]
By Cesàro averaging, \(n y_n\to2\) for any fixed \(x\in(0,1]\). Taking \(x=1\) and squeezing between consecutive powers of two gives \(F_{1/2}(\varepsilon)\log_2(1/\varepsilon)\to2\), which is the claimed sharp constant.

**5. Supercritical dyadic law.** Suppose \(p>1/2\). Let \(r=r_p\) and \(z_n=y_n-r>0\). Subtracting the fixed-point equation yields
\[
z_{n+1}=b z_n-pz_n^2=bz_n\left(1-\frac p b z_n\right),\qquad b=2(1-p)\in(0,1).
\tag{7}
\]
Since \(z_0\le1-r=(1-p)/p=b/(2p)\), every factor in (7) is at least \(1/2\). Also \(z_n\le b^n z_0\), so \(\sum_n z_n<\infty\). Therefore
\[
b^{-n}z_n=z_0\prod_{j=0}^{n-1}\left(1-\frac p b z_j\right)
\longrightarrow B_p(x)\in(0,\infty).
\tag{8}
\]
Scaling \(x\) by one half gives \(B_p(x/2)=bB_p(x)\). Using the dyadic sandwich on the nondecreasing function \(F_p(x)-r\) yields the two-sided power-order estimate. This proves the complete theorem.

## Verification

The standalone program `checker.py` performs finite-depth distribution recursions using exact rational probabilities, independently enumerates all mark assignments in a two-generation tree, checks the endpoint fixed-point algebra and dyadic recurrences for rational parameter values, and numerically spot-checks convergence toward the critical constant. Run `python3 checker.py` and compare the printed result with `verification_output.txt`. Its finite tests do not prove the infinite-tree endpoint laws; Steps 1–5 are the proof.

## Relationship to prior work

Skiredj and Berrada, *Persistent occupation and critical marked sums on branching random walks* (2026, arXiv:2610.33897v1), analyze boundedness and convergence of discounted marked tree sums and include constant-displacement models. Zhang, *Boundedness of discounted branching random walks via generic chaining* (2026, arXiv:2602.18919v1), proves boundedness criteria and explicitly records a max-type fixed-point integral equation for general discounted tree processes. Aldous and Bandyopadhyay, *A survey of max-type recursive distributional equations* (2005, arXiv:math/0401388), provides the broader recursive-equation setting. The present claim concerns the **near-upper-endpoint probability** for one canonical bounded Bernoulli instance, giving its precise critical coefficient and noncritical positive dyadic amplitudes; boundedness alone does not specify these endpoint laws. The fixed-point recursion is acknowledged as a classical tool, not itself claimed as novel.

## Limitations

This is a special deterministic binary tree with fixed dyadic discount and independent Bernoulli marks; no statement is made about general offspring, marks, or discount schedules. The amplitude functions are defined as convergent limits rather than elementary closed forms; their continuity, strict oscillation, and global all-scale constants are not established. The subcritical and supercritical all-real-scale claims are two-sided orders, not ratio-one equivalents. Broad max-type recursive-distribution literature could contain a more general theorem implying some endpoint cases, and historical priority requires independent specialist assessment. The result has only self-review, not independent audit.

## References

1. A. Skiredj and I. Berrada, *Persistent occupation and critical marked sums on branching random walks*, arXiv:2610.33897v1, first posted 2026-10-24. https://arxiv.org/html/2610.33897v1
2. Z. Zhang, *Boundedness of discounted branching random walks via generic chaining*, arXiv:2602.18919v1, first posted 2026-02-21. https://arxiv.org/html/2602.18919v1
3. D. J. Aldous and A. Bandyopadhyay, *A survey of max-type recursive distributional equations*, arXiv:math/0401388, 2004 preprint / 2005 journal. https://arxiv.org/abs/math/0401388
4. K. B. Athreya, *Discounted branching random walks*, Adv. Appl. Probab. 17 (1985), 53–66. https://doi.org/10.2307/1427052
