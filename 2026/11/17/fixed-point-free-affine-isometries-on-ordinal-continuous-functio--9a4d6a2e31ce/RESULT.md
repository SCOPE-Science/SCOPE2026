# Fixed-point-free affine isometries on ordinal continuous-function balls and sharp relaxation residuals

## Finding
For every infinite limit ordinal \(\tau\), the closed unit ball of the **real** space \(X=C_0([0,\tau))\) admits a fixed-point-free, order-preserving affine isometric embedding \(T\) into the unit sphere. For every \(0<\theta<1\), the averaged map \(T_\theta=(1-\theta)I+\theta T\) is fixed-point-free and nonexpansive. Starting at zero, its successive residuals satisfy the **exact** identity
\[
\|T_\theta^{n+1}(0)-T_\theta^n(0)\|_\infty
=\theta\max_{0\le k\le n}\binom nk\theta^k(1-\theta)^{n-k}
\sim\sqrt{\frac{\theta}{2\pi(1-\theta)n}}
\quad(n\to\infty).
\]
In particular the exact decay exponent is \(1/2\), even though no fixed point exists; this remains true for \(\tau\) of uncountable cofinality.

## Assumptions and scope
An **infinite limit ordinal** is an ordinal \(\tau\ge\omega\) with no largest predecessor. Give \([0,\tau)\) its ordinal order topology, and let \(X=C_0([0,\tau),\mathbb R)\) have supremum norm. Here vanishing at infinity means that for every \(\varepsilon>0\), the set \(\{\alpha<\tau:|f(\alpha)|\ge\varepsilon\}\) is compact, hence bounded in \(\tau\). The indicator \(e_k\) of the isolated point \(k\in\mathbb N_0\) is in \(X\).

Define \(U:X\to X\) pointwise by
\[
(Uf)(\beta)=\begin{cases}
0,&\beta=0,\\
f(\alpha),&\beta=\alpha+1<\tau,\\
f(\beta),&0<\beta<\tau\text{ is a limit ordinal}.
\end{cases}
\]
Set \(T(f)=e_0+Uf\) on the closed unit ball \(B_X\). These definitions are uniform over all the indicated ordinals; no separability, completeness beyond the ordinary \(C_0\) norm, or special cardinal hypothesis is assumed.

## Proof
**1. Continuity, decay, and isometry of \(U\).** At successor points and at zero, continuity is automatic. Fix a nonzero limit ordinal \(\lambda<\tau\). Given \(\varepsilon>0\), choose \(\gamma<\lambda\) such that \(|f(\xi)-f(\lambda)|<\varepsilon\) for every \(\gamma<\xi\le\lambda\). Then for \(\gamma+1<\eta<\lambda\), either \(\eta\) is limit and \((Uf)(\eta)=f(\eta)\), or \(\eta=\xi+1\) and \((Uf)(\eta)=f(\xi)\) with \(\xi>\gamma\). Thus \(Uf\) is continuous at \(\lambda\). If the \(\varepsilon\)-superlevel set of \(|f|\) is contained in \([0,\beta]\) for some \(\beta<\tau\), then that of \(|Uf|\) is contained in \([0,\beta+1]\); this is compact because \(\tau\) is limit. Therefore \(Uf\in X\). The definition is linear and positive. Every value of \(f(\alpha)\) appears as \((Uf)(\alpha+1)\), and every value of \(Uf\) has modulus at most \(\|f\|_\infty\). Consequently \(\|Uf\|_\infty=\|f\|_\infty\): \(U\) is a positive linear isometry.

**2. The affine fixed-point obstruction.** The function \(e_0\) is supported at zero, whereas \(Uf(0)=0\). Hence
\[
\|Tf\|_\infty=\max\{1,\|Uf\|_\infty\}=1 \quad(f\in B_X),
\qquad\|Tf-Tg\|_\infty=\|U(f-g)\|_\infty=\|f-g\|_\infty.
\]
Thus \(T\) is an affine isometric ball self-embedding with image in the sphere. It preserves order because \(U\) is positive. If \(Tf=f\), then \(f(0)=1\). A transfinite induction shows \(f(\alpha)=1\) for all \(\alpha<\tau\): the successor step follows from \(f(\alpha+1)=(Uf)(\alpha+1)=f(\alpha)\), while at each nonzero limit the preceding constant values and continuity force \(f(\lambda)=1\). The constant-one function does not belong to \(C_0([0,\tau))\), since \([0,\tau)\) is noncompact. Hence \(T\) has no fixed point.

**3. Exact relaxed orbit and asymptotics.** Fix \(0<\theta<1\), put \(A_\theta=(1-\theta)I+\theta U\), and note \(T_\theta f=A_\theta f+\theta e_0\). It is nonexpansive and its fixed points are exactly those of \(T\), hence there are none. Starting at zero and writing \(x_n=T_\theta^n(0)\), we have \(x_{n+1}-x_n=\theta A_\theta^n e_0\). For every \(k\ge0\), \(Ue_k=e_{k+1}\); by the binomial theorem,
\[
A_\theta^n e_0=\sum_{k=0}^n\binom nk(1-\theta)^{n-k}\theta^k e_k.
\]
These nonnegative disjoint singleton indicators have supremum norm equal to their largest coefficient, proving the exact residual formula for every integer \(n\ge0\). The largest binomial probability lies at any mode \(k_n=\lfloor(n+1)\theta\rfloor\), with the usual tied modes when \((n+1)\theta\) is integral. Stirling's formula gives
\[
\binom n{k_n}\theta^{k_n}(1-\theta)^{n-k_n}\sim\frac{1}{\sqrt{2\pi n\theta(1-\theta)}};
\]
multiplying by \(\theta\) yields the asserted sharp constant.

## Verification
The proof is valid for every infinite limit ordinal, including uncountable-cofinality cases; the infinite-dimensional and transfinite conclusions are analytical, not inferred from finite experiments. The accompanying Python checker verifies the finite-coordinate binomial identity using rational arithmetic for small integer \(n\) and rational \(\theta\), and checks that the mode chosen by \(\lfloor(n+1)\theta\rfloor\) maximizes the binomial probabilities. To reproduce, run `python3 check_binomial.py` with Python 3. The checker is supplementary and is not a substitute for the transfinite continuity and no-fixed-point arguments.

## Relationship to prior work
DiPaulo [1] proves failure of the ball fixed point property for all noncompact locally compact Hausdorff spaces, without claiming that its witness is an **affine isometric embedding** with an exact relaxation-residual law. Barroso [2] builds transfinite contractive propagation for nonexpansive fixed-point-free maps on certain \(C(K)\) balls, using order profiles and positive operators; the construction and claim here concern a direct global **affine isometry of the whole ball of ordinal \(C_0\)** and its exact relaxed orbit. Avilés and coauthors [3] develop the earlier ball fixed point property framework. The elementary \(c_0\) shift is a special case; the new ordinal extension requires compatibility at every limit ordinal, and applies even when no countable sequence is cofinal. Searches for equivalent claims and stronger coverage did not establish a prior implication. This is a claim of best-knowledge comparison, not a guarantee of historical priority.

## Limitations
This statement is restricted to **ordinal** locally compact spaces \([0,\tau)\), not arbitrary noncompact locally compact Hausdorff spaces. For \(\theta=1\) the residual is constant, rather than following the \(n^{-1/2}\) law; the asymptotic constant assumes fixed \(0<\theta<1\). The affine map is an isometric **embedding**, not asserted to be surjective. No independent external mathematical audit has been performed. An older unindexed affine-shift formulation, especially in the literature on ordinal \(C_0\) spaces and nonexpansive maps, remains a possible bibliographic priority risk.

## References
1. Lily DiPaulo, *The ball fixed point property for continuous functions on locally compact spaces*, arXiv:2611.01486v1, publicly submitted 2026-11-01, https://arxiv.org/abs/2611.01486.
2. Cleon S. Barroso, *Transfinite contractive propagation and the ball fixed point property in \(C(K)\)*, arXiv:2609.16318, https://arxiv.org/abs/2609.16318.
3. Antonio Avilés, María Japón, Christopher Lennard, Gonzalo Martínez-Cervantes, Adam Stawski, *The ball fixed point property in spaces of continuous functions*, arXiv:2506.17995, https://arxiv.org/abs/2506.17995.
