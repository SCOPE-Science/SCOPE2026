# A sharp observation-horizon activation law for premium edges in diffusion stars

## Finding
Let \(K_{1,m}\), \(m\ge3\), have a hub and \(m\) leaves. A single distinguished spoke costs \(r>1\) per unit conductance; all other spokes cost one. For a fixed budget \(B>0\), independently select nonnegative conductances \(w_1,\ldots,w_m\) satisfying
\[
 r w_1+\sum_{j=2}^{m}w_j=B.
\]
At a fixed observation time \(t>0\), minimize the heat trace
\[
 H_t(w)=\operatorname{tr}\bigl(e^{-tL(w)}\bigr),
\]
where \(L(w)\) is the ordinary symmetric weighted combinatorial Laplacian, including all zero modes if the network is disconnected.

**Theorem.** The unrestricted optimum is unique. Its ordinary spokes have one common *strictly positive* conductance \(y_*(t)\); the premium spoke has conductance \(x_*(t)\ge0\). Define \(z=Bt/(m-1)\) and
\[
 R_m(z)=\frac{(m-1)\bigl[m+1+(m-1)e^{-mz}\bigr]}
 {m\bigl[me^{-mz}+(m-2)e^{-z}\bigr]}.
\]
Then
\[
 \boxed{x_*(t)=0\ \Longleftrightarrow\ r\ge R_m\!\left(\frac{Bt}{m-1}\right).}
\]
The function \(R_m\) is strictly increasing on \([0,\infty)\), from \(R_m(0)=1\) to infinity. Hence, for every \(r>1\), a **unique positive activation time** \(T_m(B,r)\) satisfies \(R_m(BT_m/(m-1))=r\). The premium edge is absent at \(0<t\le T_m\) and present at every \(t>T_m\), with all ordinary edges always present. In particular, a uniquely optimal finite-time diffusion design can disconnect a vertex despite the availability of a connected feasible design.

At fixed \(r>1\), this activation time satisfies the sharp growing-star law
\[
 \boxed{\lim_{m\to\infty}\frac{BT_m(B,r)}{m-1}=\log r.}
\]
For fixed \(m\ge3\) and large price \(r\), the same threshold obeys
\[
 \frac{BT_m(B,r)}{m-1}
 =\log r+\log\!\frac{m(m-2)}{m^2-1}+o(1).
\]

## Assumptions and scope
The vertex set is \(\{0,1,\ldots,m\}\), hub \(0\), and edges \(\{0,j\}\). The cost of \(\{0,1\}\) is \(r>1\), and every other edge has unit cost. The Laplacian is
\[
 L(w)=\sum_{j=1}^m w_j(e_0-e_j)(e_0-e_j)^{\mathsf T}.
\]
All choices \(w_j\ge0\) are admitted, whether connected or not. The time \(t>0\) and budget \(B>0\) are arbitrary and fixed when optimizing. The performance measure has a finite-time mean-square interpretation:
\[
 H_t(w)-1=\bigl\|e^{-tL(w)/2}(I-J)\bigr\|_F^2,
 \qquad J=\frac{\mathbf 1\mathbf 1^{\mathsf T}}{m+1}.
\]
For fixed \(m,B,r,t\) the optimizer is unique, not merely unique up to ordinary-leaf permutations. The theorem does not assert a closed elementary expression for the positive conductance after activation.

## Proof
**1. Strict global convexity and symmetry.** Put \(f(\lambda)=e^{-t\lambda}\). For every real symmetric matrix \(A\) and nonzero real symmetric perturbation \(K\), in an eigenbasis of \(A\) the Hessian of \(\operatorname{tr}f(A)\) has the form
\[
 D^2\operatorname{tr}f(A)[K,K]
 =\sum_{i,j} f'^{[1]}(\lambda_i,\lambda_j)|\widetilde K_{ij}|^2>0,
\]
where \(f'^{[1]}(a,b)=(f'(a)-f'(b))/(a-b)\) if \(a\ne b\), and \(f''(a)\) otherwise. The coefficients are strictly positive, since \(f''(\lambda)=t^2e^{-t\lambda}>0\). Distinct spoke weights give distinct Laplacians (inspect the hub-to-leaf off-diagonal entries). Thus \(H_t\) is strictly convex in the \(m\) independent weights. On the compact feasible budget simplex, it has exactly one minimizer. Every permutation of ordinary leaves fixes the objective and feasible region; by uniqueness the ordinary rates agree. Write \(w_1=x\), \(w_2=\cdots=w_m=y\), so
\[
 r x+(m-1)y=B,\qquad 0\le x\le B/r,
 \qquad y=(B-rx)/(m-1).
\]
Strict convexity also holds along this scalar segment.

**2. Ordinary spokes cannot vanish.** If \(y=0\), then \(x=B/r\), one two-vertex component remains and \(m-1\) leaves are isolated. Set \(E=e^{-2tB/r}\). The heat-kernel quadratic form on the premium edge is \(2E\), while on each ordinary edge it is \((3+E)/2\). Since
\[
 \frac{\partial H_t}{\partial w_j}
 =-t(e_0-e_j)^{\mathsf T}e^{-tL(w)}(e_0-e_j),
\]
raising every ordinary rate by \(\varepsilon\) and lowering \(x\) by \((m-1)\varepsilon/r\) has directional derivative
\[
 -t(m-1)\left(\frac{3+E}{2}-\frac{2E}{r}\right)<0,
\]
because \(0<E<1\) and \(r>1\). Hence the unique optimum always has \(y_*>0\), and \(x=0\) is its only possible boundary.

**3. Exact derivative at premium-edge deletion.** At \(x=0\), the ordinary star has \(m-1\) spokes of common conductance \(y=B/(m-1)\) and the premium leaf is isolated. The ordinary component has eigenvalues \(0\), \(y\) with multiplicity \(m-2\), and \(my\). By elementary orthogonal spectral projection, the heat-kernel quadratic forms across the premium and ordinary spokes are respectively
\[
 A=\frac{m+1+(m-1)e^{-mty}}{m},\qquad
 C=\frac{me^{-mty}+(m-2)e^{-ty}}{m-1}.
\]
Consequently the right directional derivative along the budget line is
\[
 \left.\frac{d}{dx}H_t\left(x,\frac{B-rx}{m-1}\right)\right|_{x=0^+}
 =-t(A-rC)=tC\left(r-\frac AC\right).
\]
The ratio \(A/C\) is exactly \(R_m(Bt/(m-1))\). A strictly convex differentiable function on \([0,B/r]\), whose right endpoint is not optimal by step 2, has its unique minimum at its left endpoint exactly when this derivative is nonnegative. This gives the *if and only if*, including equality, and proves that in the complementary region both types of spokes are positive.

For completeness, with \(x,y>0\) the nonzero spectrum consists of \(y\) with multiplicity \(m-2\), and the two roots
\[
 \lambda_{\pm}=\frac{2x+my\pm\sqrt{(2x+my)^2-4(m+1)xy}}{2}.
\]
Thus the positive optimum may be reproduced as the unique stationary point in \((0,B/r)\) of
\[
 1+(m-2)e^{-ty}+e^{-t\lambda_-}+e^{-t\lambda_+},
 \qquad y=(B-rx)/(m-1).
\]
No finite grid search is needed to establish optimality.

**4. One and only one activation.** Let \(s=e^{-z}\in(0,1]\). Apart from the positive prefactor \((m-1)/m\), the function \(R_m\) equals \(N(s)/D(s)\), with \(N=m+1+(m-1)s^m\) and \(D=ms^m+(m-2)s\). Its derivative has numerator
\[
 N'D-ND'=(m-1)^2(m-2)s^m-m^2(m+1)s^{m-1}-(m-2)(m+1)<0.
\]
Indeed, \(s^m\le s^{m-1}\), and \((m-1)^2(m-2)<m^2(m+1)\) for every \(m\ge3\). Since \(s\) decreases strictly with \(z\), \(R_m\) increases strictly. Direct substitution yields \(R_m(0)=1\). The term \((m-2)e^{-z}\) dominates its denominator as \(z\to\infty\), giving
\[
 R_m(z)\sim\frac{m^2-1}{m(m-2)}e^z\to\infty.
\]
This proves existence and uniqueness of \(T_m(B,r)\) for each \(r>1\), and taking logarithms gives the large-price expansion.

For the growing-star limit, at any fixed \(z>0\), \(e^{-mz}\to0\) and
\[
 R_m(z)\longrightarrow e^z\qquad (m\to\infty).
\]
Fix \(r>1\) and any \(0<\delta<\log r\). For sufficiently large \(m\), strict monotonicity and the last pointwise limit yield \(R_m(\log r-\delta)<r<R_m(\log r+\delta)\). Its unique root \(z_m=BT_m/(m-1)\) is between these bounds. Letting \(\delta\downarrow0\) proves \(z_m\to\log r\).

## Verification
The standalone `verify.py` checks exact symbolic derivative and characteristic-polynomial identities, evaluates the boundary heat-kernel projections against direct symmetric matrix eigendecomposition, checks the sign of the forbidden ordinary-edge boundary, compares scalar convex optima with the analytic activation criterion, and tests the growing-star law. Run `python verify.py` with Python 3, NumPy, SciPy and SymPy. It prints `VERIFY_OK 849 checks` in the reproduced environment. These finite tests supplement, and do not replace, the all-size and all-real-parameter analytic proof above.

As an illustration only, for \(m=4\), \(B=1\), \(r=3\), the unique threshold is approximately \(T_4\approx2.0041342\). At \(t=1\) the premium edge is absent; at \(t=3\) it is present with computed rate approximately \(0.05195\). Neither decimal is used in the proof.

## Relationship to prior work
Sun, Boyd, Xiao and Diaconis (2006) optimize the *asymptotic* spectral-gap objective for independently costed edges, and the known priced-star solution keeps all star spokes strictly positive, even at arbitrarily high price. Boyd (2006) gives the broader convex spectral-function framework. The present finite-time heat-trace criterion is different: it penalizes every nonzero mode at the given time and can optimally disconnect the premium leaf. Neither general convexity nor spectral-gap optimization implies the explicit threshold, its monotonicity, or its network-size scaling. Shakeri and colleagues (2015) analyze a separate spectral-gap budget transition in multiplex networks. Clark and colleagues (2013) analyze finite-time leader selection, rather than continuously choosing edge conductances. A published weighted-star heat-Lipschitz extremum concerns a different operator norm, and also does not imply the trace-optimal design.

## Limitations
The sharp classification concerns the *ordinary combinatorial Laplacian*, one strictly more expensive spoke, homogeneous ordinary prices, a linear cost equality, and nonnegative real conductances. It does not claim the general multi-price star solution or a closed form for the interior weights. It deliberately allows disconnected designs: if connectivity were imposed as a strict constraint, the zero-rate optimum would not be feasible and the infimum in the early regime would only be approached. The value and originality of a specific threshold may be judged independently of the general convex optimization framework; an unindexed equivalent calculation remains possible. The proof is mathematical, not a statement of independent external validation.

## References
1. J. Sun, S. Boyd, L. Xiao and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf, doi:10.1137/S0036144504443821.
2. S. Boyd, *Convex Optimization of Graph Laplacian Eigenvalues*, International Congress of Mathematicians (2006), https://people.csail.mit.edu/jrennie/trg/papers/boyd-convex-06.pdf.
3. H. Shakeri, N. Albin, F. D. Sahneh, P. Poggi-Corradini and C. Scoglio, *Maximizing Algebraic Connectivity in Interconnected Networks*, arXiv:1510.06785v1, first public 2015-10-22, https://arxiv.org/abs/1510.06785.
4. A. Clark, B. Alomair, L. Bushnell and R. Poovendran, *Minimizing Convergence Error in Multi-Agent Systems via Leader Selection*, arXiv:1306.4949v1, first public 2013-06-20, https://arxiv.org/abs/1306.4949.
5. *Two-conductance stars: exact heat-Lipschitz norm, slow-edge rigidity and a sharp fixed-size amplification envelope*, published November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-two-conductance-stars-exact-heat-lipschitz-norm-slow-edge-rigidi--20e568f24dba.
6. *The square-price transition for fastest mixing on a weighted star*, published October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-the-square-price-transition-for-fastest-mixing-on-a-weighted-sta--94423c8faa44.
