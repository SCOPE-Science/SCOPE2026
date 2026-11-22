# Fixed-window memory creates a sharp curvature-identification rate reversal in residual-adaptive gradient descent

## Finding

For the residual-geometric-mean adaptive gradient method of Hu, Pollock, Xue, and Zhu [1], consider the two-eigenvalue positive quadratic and invariant lower-eigenvalue starting ray specified below. For **every fixed finite window length** \(\ell\geq1\), the observed residual multipliers converge globally to \(q_*=(1-a)/(1+a)\); hence the adaptive steps converge to \(2/(1+a)\). Their \(\ell\)-dimensional local feedback Jacobian has characteristic polynomial

\[
P_\ell(z)=z^\ell+\frac a\ell\sum_{j=0}^{\ell-1}z^j.
\]

Writing \(r_\ell(a)\) for its spectral radius, the **sharp one-versus-two-window reversal** and **unbounded memory slowdown** are

\[
r_1(a)=a,\qquad r_2(a)=\sqrt{a/2},\qquad
r_2(a)\begin{cases}<r_1(a),&a>1/2,\\=r_1(a),&a=1/2,\\>r_1(a),&0<a<1/2,\end{cases}
\]

\[
\left(\frac a\ell\right)^{1/\ell}\leq r_\ell(a)\leq a^{1/\ell}<1,
\qquad \lim_{\ell\to\infty}r_\ell(a)=1.
\]

The limiting statement concerns the worst-case *linearized stepsize-estimation response*, first taking the iteration index to infinity at each fixed window, and then allowing the chosen window length to grow. It does **not** assert a deterioration of the asymptotic optimization-iterate rate for the specified invariant ray.

## Assumptions and scope

Let \(0<a<1\), \(A=\operatorname{diag}(a,1)\), and \(f(x)=\tfrac12x^\mathsf{T}Ax\). Initialize \(x_0=(s,0)\) for arbitrary \(s\ne0\), set \(b=0\), and use Algorithm 1 of [1], with \(\alpha_1=1\), \(x_k=x_{k-1}-\alpha_kAx_{k-1}\), residual \(R_k=-Ax_k\), and \(\alpha_{k+1}=1+\widehat\rho_k\). For one **fixed** integer \(\ell\ge1\) throughout the run, the source's actual practical estimator, including startup normalization, is

\[
\widehat\rho_k=\begin{cases}
(\|R_k\|/\|R_0\|)^{1/k}, &1\le k<\ell,\\
\displaystyle\left(\prod_{i=k-\ell+1}^k\|R_i\|/\|R_{i-1}\|\right)^{1/\ell},& k\ge\ell.
\end{cases}
\]

The notation \(q_k=1-a\alpha_k\) denotes the **signed single-step residual multiplier**; it is positive under the stated hypotheses. The local spectral radius is a property of the smooth \(\ell\)-lag feedback map in a neighborhood of its fixed point. No conclusion here extends to arbitrary initial spectral mixtures, varying windows \(\ell=k\), finite-precision underflow, or nonlinear objectives.

## Proof

**1. Exact recurrence and invariant interval.** The initial ray is invariant for every gradient step. Thus \(R_k=q_kR_{k-1}\) and \(q_1=1-a\). Set \(m_k=\min(k,\ell)\). Every residual ratio equals the positive \(q_i\), so the startup and full-window formulas agree exactly with

\[
q_{k+1}=1-a-a\left(\prod_{j=k-m_k+1}^{k}q_j\right)^{1/m_k},\qquad k\ge1.
\tag{1}
\]

Since \(q_1=1-a\), induction gives the invariant compact interval

\[
(1-a)^2\le q_k\le1-a<1\qquad(k\ge1).
\tag{2}
\]

Indeed every geometric mean of numbers in this interval remains in it; the next multiplier belongs to \([\,(1-a)-a(1-a),\ (1-a)-a(1-a)^2\,]\), which is contained in (2). Thus all residuals are nonzero and the ratios in the algorithm remain well-defined for every finite iteration.

**2. Global limit.** At any constant positive multiplier \(q\), equation (1) requires \(q=1-a-aq\), giving the unique fixed point \(q_*=(1-a)/(1+a)\), which lies in the interval (2). For numbers \(q_j\) and \(q_*\) in this interval, their geometric mean lies between the least and greatest entries, hence

\[
|q_{k+1}-q_*|\le a\max_{k-m_k+1\le j\le k}|q_j-q_*|.
\tag{3}
\]

For \(k\ge\ell\), define \(M_k=\max_{k-\ell+1\le j\le k}|q_j-q_*|\). Equation (3) implies \(M_{k+1}\le M_k\). Applying it for a further \(\ell\) updates, every entry in the new complete block has deviation at most \(aM_k\); therefore \(M_{k+\ell}\le aM_k\). Because \(0<a<1\), this proves \(q_k\to q_*\) geometrically in blocks for every fixed finite \(\ell\). In particular \(\alpha_k=(1-q_k)/a\to 2/(1+a)\), and \(\|x_k\|\) decays since \(q_k\le1-a\).

**3. Local characteristic equation.** For \(k\ge\ell\), the smooth map in the \(\ell\) coordinates \((q_k,\ldots,q_{k-\ell+1})\) sends the vector to \((1-a-aG,q_k,\ldots,q_{k-\ell+2})\), with \(G\) the \(\ell\)-term geometric mean. At the constant vector \((q_*,\ldots,q_*)\), \(\partial G/\partial q_j=1/\ell\). Its Jacobian has first row \((-a/\ell,\ldots,-a/\ell)\) and ones on its lower subdiagonal, so its characteristic polynomial is the displayed \(P_\ell\). It is Schur stable: the \(\ell\)-fold Jacobian power has maximum-row-sum norm at most \(a\), as each fresh first coordinate is bounded by \(a\) times the largest previous coordinate and after \(\ell\) updates every initial shift is replaced. Thus \(r_\ell(a)^\ell\le a\).

The constant term of \(P_\ell\) is \(a/\ell\). Vieta's product formula makes the product of absolute root moduli equal to \(a/\ell\), hence \(r_\ell(a)^\ell\ge a/\ell\). Combining the two bounds proves the spectral inequalities, and both bounds tend to one as \(\ell\to\infty\).

**4. Two-window crossover.** For \(\ell=1\), \(P_1(z)=z+a\), so \(r_1(a)=a\). For \(\ell=2\), \(P_2(z)=z^2+(a/2)z+a/2\) has discriminant \(a^2/4-2a<0\). Its two complex-conjugate roots have modulus \(\sqrt{a/2}\). The ordering reverses precisely where \(a=1/2\), proving the sharp crossover.

## Verification

Run `python verify.py` with Python 3 and NumPy. The standalone script checks exact rational values for the one- and two-window formulas; computes companion characteristic roots and their universal bounds for several \((a,\ell)\); and directly evaluates the source's startup and fixed-window iteration to check positivity and convergence. These calculations reproduce examples but are **not** substitutes for the all-window analytic proof above. For example, at \(a=1/4\), the one- and two-window feedback radii are \(1/4\) and \(1/\sqrt8\), respectively, so adding one history term worsens the linearized rate; at \(a=3/4\), the order reverses.

## Relationship to prior work

Reference [1], Section 2.1, supplies the precise practical geometric-mean estimator (its equation (3)), proves a general gradient-descent convergence guarantee (Lemma 2.5), analyzes the one-sample estimator in Theorem 2.7, and tests window lengths \(1\), \(5\), and the growing-history choice in Section 3. Its convergence analysis does not state the full finite-window companion polynomial, the strict one-versus-two-window crossover, or the spectral-radius limit as fixed window length grows. A prior published investigation [2] establishes an exact one-history-step identification recurrence on two-eigenvalue quadratics; that is consistent with \(r_1(a)=a\) but does not imply the \(\ell\ge2\) feedback classification. The current calculation is specific to the invariant lower-eigenspace trajectory and does not propose a different algorithm.

## Limitations

This result concerns a special invariant starting ray on a two-eigenvalue quadratic, not generic mixtures. The local feedback spectral radius is the worst-case infinitesimal perturbation rate of the \(\ell\)-coordinate recurrence, not a claim that the prescribed startup trajectory excites every eigenmode or attains that rate for each parameter. The pointwise limit \(r_\ell(a)\to1\) is for a succession of distinct fixed-window algorithms; it is not a convergence result for a single growing-memory run. The exact optimal choice among all window lengths for fixed \(a\) is not classified. Related general delay-recurrence theory may yield alternative proofs; independent historical-priority review remains open.

## References

[1] X. Hu, S. Pollock, Z. Xue, and Y. Zhu, *An adaptive framework for first-order gradient methods*, arXiv:2602.13620v1, publicly submitted 2026-02-14. https://arxiv.org/abs/2602.13620

[2] *Exact alternating identification on two endpoint spectra*, published mathematical finding, 2026-10-04, public record `2026/10/4/SCOPE-exact-alternating-identification-on-two-endpoint-spectra--70ce85b504e2`, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-alternating-identification-on-two-endpoint-spectra--70ce85b504e2 (published summary consulted; full content not available during comparison).
