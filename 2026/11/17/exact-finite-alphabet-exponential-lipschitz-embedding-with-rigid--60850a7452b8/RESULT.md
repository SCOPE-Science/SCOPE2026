# Exact finite-alphabet exponential Lipschitz embedding with rigid tensor extremizers and an arithmetic quantization phase

## Finding

Fix a real parameter \(\lambda>0\). For integers \(d\ge1\) and \(m_1,\ldots,m_d\ge2\), set \(X=\prod_{j=1}^d\{1,\ldots,m_j\}\) with uniform probability, Hamming distance, and the Lipschitz seminorm \(\operatorname{Lip}(f)=\max_{x\ne y}|f(x)-f(y)|/d_H(x,y)\). The sharp exponential integration constant of the finite-dimensional discrete Lipschitz function space is

\[
\sup_{\operatorname{Lip}(f)\le1}\mathbb E e^{\lambda(f-\mathbb Ef)}
=\prod_{j=1}^d M_{m_j}(\lambda),\qquad
M_m(\lambda)=\max_{1\le k\le m-1}\left(1+\frac{k}{m}(e^\lambda-1)\right)e^{-\lambda k/m}.
\]

Every maximizing \(f\) is, up to an arbitrary additive constant, exactly \(f(x)=\sum_{j=1}^d\mathbf1_{S_j}(x_j)\), where \(S_j\) is a nonempty proper subset with \(|S_j|\) maximizing the displayed one-alphabet factor. Conversely all these functions maximize. In particular, no genuinely interacting Lipschitz function attains this sharp exponential norm.

Let
\[
B_m(\lambda)=\frac1{e^{\lambda/m}-1}-\frac{m}{e^\lambda-1}.
\]
It is strictly decreasing from \((m-1)/2\) to \(0\). At nonintegral \(B_m(\lambda)\), the unique optimizing subset size is \(k=\lceil B_m(\lambda)\rceil\). At \(B_m(\lambda)=k\in\{1,\ldots,\lfloor m/2\rfloor-1\}\), precisely sizes \(k\) and \(k+1\) tie. Thus alphabet cardinality \(m\) has exactly \(\max\{0,\lfloor m/2\rfloor-1\}\) positive-parameter optimizer transitions.

There is a sharp *arithmetic alphabet-quantization effect*. Define
\[
p_\lambda=\frac1\lambda-\frac1{e^\lambda-1},\qquad
M_\infty(\lambda)=\frac{e^\lambda-1}{\lambda}\exp\left(-1+\frac\lambda{e^\lambda-1}\right).
\]
For fixed \(\lambda>0\), as \(m\to\infty\),
\[
\log M_\infty(\lambda)-\log M_m(\lambda)
=\frac{\lambda^2}{2m^2}\operatorname{dist}(mp_\lambda,\mathbb Z)^2+O_\lambda(m^{-3}).
\]
If \(p_\lambda\) is rational, the normalized discrepancy has a finite set of subsequential limits; if \(p_\lambda\) is irrational, its subsequential-limit set is the full interval \([0,\lambda^2/8]\). In particular at \(\lambda=1\) the full interval \([0,1/8]\) occurs because \(p_1\) is irrational.

## Assumptions and scope

All alphabets are finite and uniformly weighted; the metric is the unweighted Hamming distance, and functions and exponential parameters are real. The supremum is taken over all functions with coordinatewise oscillation at most one, equivalently over the unit ball modulo constants of the discrete Lipschitz seminorm. The exponential functional is center-normalized by the exact uniform mean. The extremizer statement holds for every finite \(d\ge1\), all \(m_j\ge2\), and each fixed \(\lambda>0\), including all transition values. The quantization statement concerns fixed \(\lambda\) and alphabet size tending to infinity.

## Proof

**Single alphabet.** Translation invariance permits shifting every vector of oscillation at most one into the cube \([0,1]^m\). Put
\[
\Phi(u)=\log\left(\frac1m\sum_{i=1}^m e^{\lambda u_i}\right)-\frac\lambda m\sum_{i=1}^m u_i.
\]
When all coordinates but \(u_i\) are held fixed, its second derivative equals \(\lambda^2 w_i(1-w_i)>0\), where \(w_i=e^{\lambda u_i}/\sum_j e^{\lambda u_j}\in(0,1)\) because \(m\ge2\). Hence a maximizer on \([0,1]^m\) cannot have an interior coordinate: replacing it by one endpoint strictly improves the functional. Thus every single-site maximizing vector is binary. The value for \(k\) ones is exactly \(M_m\)'s displayed factor; \(k=0,m\) give one, while any \(1\le k<m\) gives greater than one by strict Jensen. This also proves the full single-alphabet equality characterization.

**Tensorization.** Write \(X=Y\times Z\) with \(|Z|=m_d\), and set \(h(y)=\mathbb E_z f(y,z)\). The function \(h\) remains 1-Lipschitz on \(Y\). For every fixed \(y\), the last-coordinate fiber has oscillation at most one. Therefore
\[
\mathbb E_{y,z}e^{\lambda(f(y,z)-\mathbb Ef)}
=\mathbb E_y\left[e^{\lambda(h(y)-\mathbb Eh)}\mathbb E_z e^{\lambda(f(y,z)-h(y))}\right]
\le M_{m_d}(\lambda)\mathbb E_y e^{\lambda(h(y)-\mathbb Eh)}.
\]
Induction yields the product upper bound; binary additive functions give equality.

**Rigidity of equality.** Equality forces \(h(y)=c+\sum_{j<d}\mathbf1_{S_j}(y_j)\) by induction, with each \(S_j\) a nonempty proper subset. If \(y,y'\in Y\) differ only in coordinate \(j\) across the cut \(S_j\) and its complement, then \(|h(y)-h(y')|=1\). For each \(z\), the corresponding signed difference \(f(y,z)-f(y',z)\) lies in \([-1,1]\) and its average is the endpoint \(\pm1\); hence it equals that endpoint for every \(z\). Thus \(f(y,z)-h(y)=f(y',z)-h(y')\) across every cut edge. In each coordinate, the complete bipartite graph between the two nonempty sides is connected, and so is the Cartesian product of these graphs. Consequently \(f(y,z)-h(y)\) is independent of \(y\). Writing it as \(v(z)\), equality in the single-site bound forces \(v\) to be a binary cut indicator plus a constant. This completes induction. For \(d=1\), the single-site argument supplies the base case.

**Exact staircase.** With \(a=e^\lambda-1>0\) and \(H_m(k)=e^{-\lambda k/m}(1+ak/m)\), direct division gives
\[
\frac{H_m(k+1)}{H_m(k)}\ge1\quad\Longleftrightarrow\quad k\le B_m(\lambda).
\]
Thus the maximum over integer \(k\) is at \(\lceil B_m\rceil\), with the stated adjacent tie when \(B_m\) is integral. Differentiating,
\[
B_m'(\lambda)=\frac{m}{4\sinh^2(\lambda/2)}-
\frac1{4m\sinh^2(\lambda/(2m))}<0,
\]
because \(\sinh(mt)>m\sinh(t)\) for \(t>0\) and \(m>1\). Exponential expansions give the endpoint limits, so every integer level listed in the finding is crossed once and no other level is crossed.

**Quantization.** For the continuous density \(p\in[0,1]\), set \(g_\lambda(p)=\log(1+p(e^\lambda-1))-\lambda p\). Its unique critical point is \(p_\lambda=1/\lambda-1/(e^\lambda-1)\in(0,1/2)\), and \(g_\lambda''(p_\lambda)=-\lambda^2\). Consequently \(g_\lambda(p_\lambda)=\log M_\infty(\lambda)\). A comparison of the two neighboring lattice values of mesh \(1/m\), followed by Taylor's theorem with bounded third derivative, gives the displayed quantization expansion with an \(O_\lambda(m^{-3})\) remainder: the discrete maximizer lies among the nearest lattice points to \(p_\lambda\), up to an \(O(m^{-2})\) rounding discrepancy which does not affect the stated remainder. If \(p_\lambda\) is rational, the fractional parts of \(mp_\lambda\) are periodic; if it is irrational, they are dense in \([0,1]\), and continuity of squared distance to an integer gives exactly the claimed accumulation interval. Finally \(p_1=1-1/(e-1)\) is irrational since \(e\) is irrational.

## Verification

The standalone `check.py` checks the sharp formula by independently enumerating **all integer vertices** of the fixed-origin bounded-difference polytope for small Hamming products. The constraint matrix is the directed edge-vertex incidence matrix, which is totally unimodular; with integer bounds and one fixed vertex, every polytope vertex is integral. Therefore this finite enumeration genuinely covers all vertices for those particular small products, rather than merely sampling arbitrary functions. It also checks 140 explicit phase selections and 351 quantitative quantization approximations. Its terminal output is `ALL_LIPSCHITZ_EXPONENTIAL_DIAGNOSTICS_PASSED`. The universal theorem and irrational-alphabet limit are established analytically, not inferred from finite experiments.

To reproduce, execute `python check.py` with a Python 3 interpreter; only the standard library is used.

## Relationship to prior work

McDiarmid's classical bounded-differences method supplies general concentration inequalities for independent coordinates (1989). Bentkus (2007) develops sharper concentration estimates for separately Lipschitz functions. Samorodnitsky (arXiv:0807.1679) analyzes a modified log-Sobolev inequality for the **binary** Hamming cube, not the exact finite-alphabet centered exponential functional. Dzindzalieta (arXiv:1205.6300, first public 2012-05-29) gives exact **one-sided deviation probabilities** using distance-function optimizers on Hamming rectangles; those individually optimized tail probabilities are not the same variational functional as the single centered exponential integral at fixed \(\lambda\). The present result specializes to familiar binary Rademacher exponential moments when all \(m_j=2\); the full arbitrary-alphabet optimizer-rigidity, cardinality-transition and arithmetic-quantization assertions are distinct additional statements. The 1989 chapter and the 2007 paper could not be inspected in full through accessible sources, so an equivalent historical formulation cannot be ruled out.

## Limitations

No assertion is made for nonuniform coordinate measures, other metrics, Banach-valued functions, negative or zero exponential parameters, or growing \(\lambda\) in the quantization limit. The additive equality classification requires uniform complete product alphabets and exact Hamming distances. Nothing here asserts sharp *pointwise tail-event* probabilities; optimizing an exponential moment is a different problem. The priority assessment is based on accessible sources and may miss an earlier result implied by a strong convex-order theorem or a full-text-only statement.

## References

1. C. McDiarmid, *On the method of bounded differences*, Surveys in Combinatorics 1989, pp. 148–188, DOI: 10.1017/CBO9781107359949.008; public date recorded 1989-08-03.
2. V. Bentkus, *On measure concentration for separately Lipschitz functions in product spaces*, Israel J. Math. 158 (2007), pp. 1–17, DOI: 10.1007/s11856-007-0001-2.
3. A. Samorodnitsky, *A modified logarithmic Sobolev inequality for the Hamming cube and some applications*, arXiv:0807.1679, first posted 2008-07-10, https://arxiv.org/abs/0807.1679.
4. D. Dzindzalieta, *Extremal Lipschitz functions in the deviation inequalities from the mean*, arXiv:1205.6300, first posted 2012-05-29, https://arxiv.org/abs/1205.6300.
