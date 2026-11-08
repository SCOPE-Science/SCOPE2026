# Arithmetic mean-square returns of the Fibonacci Hopfield Cantor attractor

## Finding
Let \(\varphi=(1+\sqrt5)/2\) and \(\alpha=(3-\sqrt5)/2=\varphi^{-2}\). Consider the contracted rotation
\[
 g(t)=\begin{cases}t/2+\delta,&0\le t<2(1-\delta),\\ t/2+\delta-1,&2(1-\delta)\le t\le1,\end{cases}
\]
where \(\delta=\frac12+\sum_{k\ge0}\omega_k2^{-k-2}\) and \(\omega_k=2+\lfloor(k+1)\varphi\rfloor-\lfloor(k+2)\varphi\rfloor\). Let \(C\) be its minimal Cantor attractor, and \(\mu\) its unique invariant probability. For integer \(n\ge1\), put \(\tau_n=\|n\alpha\|_{\mathbb R/\mathbb Z}\) and
\[
 \Delta_n=\int_C\left(g^n(t)-t\right)^2\,d\mu(t).
\]
**The exact arithmetic return identity** is
\[
 \boxed{\Delta_n=\frac43\tau_n-\frac23\sum_{k=1}^{\infty}2^{1-k}\left(\tau_n-\|k\alpha\|_{\mathbb R/\mathbb Z}\right)_+.}
\]
Here \((a)_+=\max(a,0)\). In particular, with Fibonacci numbers \(F_1=F_2=1\) and \(F_{j+1}=F_j+F_{j-1}\), for every integer \(j\ge3\),
\[
 \boxed{\frac23\,2^{1-F_{j+1}}\left(\varphi^{-j}-\varphi^{-(j+1)}\right)
 \le \frac43\varphi^{-j}-\Delta_{F_j}
 \le \frac83\varphi^{-j}2^{-F_{j+1}}.}
\]
Consequently \(\Delta_{F_j}=\frac43\varphi^{-j}(1+O(2^{-F_{j+1}}))\), with a strictly positive correction of the stated order. The near-return variance deficit is \(\operatorname{Var}_\mu(t)-\operatorname{Cov}_\mu(t,g^{F_j}(t))=\Delta_{F_j}/2\), and thus has leading coefficient \(2/3\).

For the Hopfield network of Pires with invariant Perron–Frobenius ray \(L=\{t\mathbf v:0\le t\le1\}\), and \(\mathbf F(t\mathbf v)=g(t)\mathbf v\), the induced stationary law \(\widehat\mu=(t\mapsto t\mathbf v)_*\mu\) satisfies the corresponding exact formula
\[
 \int_L\|\mathbf F^n(z)-z\|_2^2d\widehat\mu(z)=\|\mathbf v\|_2^2\Delta_n.
\]
This result concerns the invariant ray and its Cantor attractor, not arbitrary states outside it.

## Assumptions and scope
The exact map, Fibonacci word and invariant-line conjugacy are those given in Pires (2022 preprint, later published 2023). The rotation semiconjugacy and gap construction are those of Gaivão and Pires (2022). The network has a strictly positive weight matrix with row sums in \((3/4,1)\), Perron–Frobenius probability eigenvector \(\mathbf v\), and the activation functions specified by Pires; the present statement needs no genericity assumption on the matrix beyond those source hypotheses. Lebesgue measure is normalized on the rotation circle \(\mathbb R/\mathbb Z\). The formula holds for every integer \(n\ge1\); the two-sided estimate holds for each integer \(j\ge3\). The \(\ell_2\) distance on the network line is the ordinary Euclidean norm, not a rescaled coordinate norm.

## Proof
**1. Gap reconstruction and unique stationary law.** The full-text construction in Gaivão–Pires, Lemma 6, identifies disjoint gaps \(G_k\), \(k\ge1\), ordered according to \(p_k=\{k\alpha\}\), with exact lengths \(|G_k|=2^{-k}\), and an increasing semiconjugacy \(h\) to the irrational rotation \(R_\alpha(s)=\{s+\alpha\}\), collapsing \(G_k\) to \(p_k\). Since \(\sum_{k\ge1}2^{-k}=1\), the residual Cantor set has zero Lebesgue measure. At all \(s\notin\{p_k:k\ge1\}\), the unique preimage of \(s\) is the point
\[
 q(s)=\sum_{k\ge1}2^{-k}{\bf1}_{\{p_k<s\}}.
\]
The semiconjugacy gives \(g(q(s))=q(R_\alpha(s))\) for Lebesgue-almost every \(s\). Hence \(\mu=q_*ds\) is stationary. It is unique: for any stationary probability \(\nu\), its pushforward \(h_*\nu\) is invariant under irrational rotation and therefore equals Lebesgue measure; each exceptional fiber of \(h\) is supported above one of the countably many \(p_k\), all of zero pushforward mass, and \(h\) is injective elsewhere. The source's invariant-line identity gives the network lift.

**2. Exact signed-atom correlation formula.** Regard \(q\) as a periodic function of rotation phase. Its signed distributional derivative on the circle is the finite signed atomic measure
\[
 \sigma=-\delta_0+\sum_{k\ge1}2^{-k}\delta_{p_k}.
\]
The negative unit atom at phase zero is indispensable; it records the wraparound jump of the periodic extension of the increasing staircase. For \(0<\tau\le1/2\), the increment \(q(s+\tau)-q(s)\) equals \(\sigma((s,s+\tau])\) for almost every phase. Two circular arcs of length \(\tau\), ending at phases \(a,b\), overlap in length \((\tau-\|a-b\|_{\mathbb R/\mathbb Z})_+\). Fubini is justified by \(|\sigma|(\mathbb T)=2\). Therefore
\[
 \int_0^1(q(s+\tau)-q(s))^2ds
 =\tau\Bigl(1+\sum_{k\ge1}4^{-k}\Bigr)
  +2\sum_{k\ge1}\left(-2^{-k}+\sum_{i\ge1}2^{-i}2^{-(i+k)}\right)
       (\tau-\|k\alpha\|)_+.
\]
The diagonal equals \(4\tau/3\) and the coefficient in parentheses simplifies to \(-2^{-k}+2^{-k}/3=-(2/3)2^{-k}\). Thus the off-diagonal term is \(-\frac23\sum_{k\ge1}2^{1-k}(\tau-\|k\alpha\|)_+\). Since \(q\) is periodic, the integral is unchanged if \(\tau\) is replaced by \(-\tau\). Substituting \(\tau=\tau_n\) proves the exact formula.

**3. Sharp Fibonacci bounds.** Binet's identity, or induction using \(\varphi^2=\varphi+1\), yields
\[
 F_j\alpha=F_{j-2}+(-1)^j\varphi^{-j}\qquad(j\ge2).
\]
Thus \(\tau_{F_j}=\varphi^{-j}\) for \(j\ge3\). The continued fraction \(\alpha=[0;2,1,1,\ldots]\) has consecutive best-return denominators \(F_j,F_{j+1}\), implying \(\|k\alpha\|\ge\varphi^{-j}\) for every integer \(1\le k<F_{j+1}\). Consequently only indices \(k\ge F_{j+1}\) contribute to the correction. Keeping the \(k=F_{j+1}\) term gives the displayed lower bound, since \(\|F_{j+1}\alpha\|=\varphi^{-(j+1)}\). Bounding every positive-part term by \(\varphi^{-j}\) and summing the geometric tail \(\sum_{k\ge F_{j+1}}2^{1-k}=2^{2-F_{j+1}}\) gives the upper bound. This proves both the positive defect and its doubly exponential-in-index scale.

**4. Covariance and vector version.** Stationarity implies \(\int_C(g^n(t))^2d\mu=\int_Ct^2d\mu\) and \(\int_Cg^n(t)d\mu=\int_Ct d\mu\); expansion of \(\Delta_n\) therefore gives \(\Delta_n=2(\operatorname{Var}(t)-\operatorname{Cov}(t,g^n(t)))\). On the invariant ray the coordinate difference is exactly \((g^n(t)-t)\mathbf v\), whose squared Euclidean norm is \(\|\mathbf v\|_2^2\) times the scalar square.

## Verification
The included `checker.py` independently integrates finite-jump approximations of the phase staircase by partitioning at every jump and its translated position, including the circular wraparound breakpoint. It compares the integral with the infinite arithmetic formula to an explicit exponentially small truncation tolerance for six Fibonacci indices and checks the bounds and Binet equalities. The source proof supplies the gap construction; the all-time identity and all-index Fibonacci estimates are analytic proofs, not consequences of the finite checker. Running `python checker.py` requires Python 3 and `mpmath`.

## Relationship to prior work
Pires (arXiv:2210.00414, first posted 2022-10-02; primary MSC 37E05) proves the existence, chaotic topological dynamics and invariant ray of this Hopfield network, but does not state its stationary mean-square return statistics. Gaivão–Pires (arXiv:2206.11933, first posted 2022-06-23), Lemma 6, constructs the underlying rotation semiconjugacy and the exact gap lengths \(2^{-k}\); these are explicitly credited as prior inputs rather than claimed anew. The new step converts this information into the exact all-time signed-atom autocorrelation series and its two-sided, Fibonacci-arithmetic, superexponentially accurate return law. An alternative full spectral computation in less easily indexed literature could affect publication priority; no independent audit has been performed.

## Limitations
The law is a stationary quadratic observable on the invariant Cantor set, not a pointwise bound for every initial condition. The network conclusion applies to the invariant Perron–Frobenius line, and does not characterize off-line convergence or physical basin statistics. The Fibonacci estimates concern specific best-return times, not all long integers. Finite numerical checks do not prove the infinite statements. No claim of independent verification or globally exhaustive publication-priority search is made.

## References
1. B. Pires, *A chaotic discrete-time continuous-state Hopfield network with piecewise-affine activation functions*, arXiv:2210.00414 (2022-10-02), https://arxiv.org/abs/2210.00414 ; published *Discrete and Continuous Dynamical Systems B* 28 (2023), 4683–4691, https://doi.org/10.3934/dcdsb.2023035.
2. J. P. Gaivão and B. Pires, *Chaotic time series in financial processes consisting of savings with piecewise constant monthly contributions*, arXiv:2206.11933 (2022-06-23), https://arxiv.org/abs/2206.11933, especially Lemma 6 and its gap construction.
3. Classical continued-fraction best-approximation theorem (used only for the Fibonacci return denominators; its elementary application is detailed above).
