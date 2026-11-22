# Sharp heat-kernel Nyström landmark transition and vanishing success of diagonal sampling on stars

## Finding
Let \(m\ge2\), and let \(K_m(t)=\exp(-tL_m)\) for the combinatorial Laplacian of the unweighted star with \(m\) leaves. For each vertex \(v\), let
\[
N_v(t)=\frac{K_m(t)e_ve_v^{\mathsf T}K_m(t)}{[K_m(t)]_{vv}},\qquad
E_v(t)=\operatorname{tr}(K_m(t)-N_v(t)).
\]
There is a unique \(\tau_m>0\), defined by
\[
m e^{-(m+2)\tau_m}+e^{-(m+1)\tau_m}+e^{-\tau_m}=1,
\]
with this **complete rank-one trace-optimal landmark classification**: for \(0<t<\tau_m\), precisely the leaves minimize \(E_v(t)\); at \(t=\tau_m\) every vertex ties; for \(t>\tau_m\) the hub is uniquely optimal. Nevertheless, every leaf has strictly *larger heat-kernel diagonal* than the hub for all \(t>0\), so largest-diagonal greedy Cholesky picks a suboptimal landmark at every \(t>\tau_m\).

The transition obeys the sharp large-star law
\[
\tau_m=\frac{W(m^2)}{m}+O\!\left(\frac{\log m}{m^2}\right),\quad m\to\infty,
\]
where \(W\) is the positive Lambert function. At each fixed \(t>0\) the hub's captured trace tends to \(1\), while a leaf's tends to \(e^{-t}\); consequently the suboptimality gap in trace error tends to \(1-e^{-t}\). Rank-one spectral-leverage sampling chooses the optimal hub with probability \(1/(m+1)\), and first-step diagonal-proportional randomized Cholesky chooses it with probability asymptotic to \(e^t/m^2\). Their expected excess trace error above the optimal single-column approximation also tends to \(1-e^{-t}\) at each fixed positive \(t\).

## Assumptions and scope
- \(L_m\) is the *unnormalized, unweighted, symmetric combinatorial* Laplacian of \(K_{1,m}\), not a random-walk-normalized Laplacian; time \(t\) is strictly positive.
- Exactly one *unrescaled, sampled matrix column* of the symmetric positive-definite heat kernel is selected, with the standard one-column Nyström update \(N_v\). No optimization over arbitrary rank-one directions is claimed.
- The error is the positive-semidefinite residual's trace, equivalently its nuclear norm, and not its Frobenius or operator norm.
- For the large-star probabilities and regrets, \(t>0\) is fixed before sending \(m\to\infty\); no uniformity in vanishing \(t\) is claimed.
- At the transition, there are exactly \(m+1\) tied landmarks. At \(t=0\) (excluded) all vertices tie as well.

## Proof
Write \(n=m+1\), \(a=e^{-t}\), and \(b=e^{-nt}\); hence \(0<b<a<1\). Put \(\mathbf1=(1,\ldots,1)^{\mathsf T}\) and \(u=(m,-1,\ldots,-1)^{\mathsf T}\). The orthogonal spectral projectors are
\[
P_0=\frac{\mathbf1\mathbf1^{\mathsf T}}n,\qquad
P_n=\frac{uu^{\mathsf T}}{mn},\qquad
P_1=I-P_0-P_n.
\]
Directly, \(L_mP_0=0\), \(L_mP_n=nP_n\), and \(L_mP_1=P_1\). Thus \(K_m(t)=P_0+aP_1+bP_n\), while \(K_m(t)^2=K_m(2t)=P_0+a^2P_1+b^2P_n\).

Let \(h\) be the hub and \(\ell\) any leaf. The two diagonal values are
\[
H(t)=[K_m(t)]_{hh}=\frac{1+mb}{m+1},\qquad
D(t)=[K_m(t)]_{\ell\ell}=\frac{m+b+(m^2-1)a}{m(m+1)}.
\]
In particular
\[
D(t)-H(t)=\frac{m-1}{m}(a-b)>0.
\]
Because \(K_m(t)\succ0\), the rank-one Schur residual \(K_m(t)-N_v(t)\) is positive semidefinite. Cyclicity of trace and the semigroup identity give
\[
E_v(t)=\operatorname{tr} K_m(t)-G_v(t),\qquad
G_v(t)=\frac{[K_m(2t)]_{vv}}{[K_m(t)]_{vv}}.
\]
The captured-trace gains are therefore
\[
G_h(t)=\frac{1+mb^2}{1+mb},\qquad
G_\ell(t)=\frac{m+b^2+(m^2-1)a^2}{m+b+(m^2-1)a}.
\]
Clearing the strictly positive denominators and factoring gives the identity
\[
G_h(t)-G_\ell(t)=
-\frac{(m^2-1)(a-b)(mab+a+b-1)}{(1+mb)(m+b+(m^2-1)a)}.
\]
The final factor is \(f_m(t)=m e^{-(m+2)t}+e^{-(m+1)t}+e^{-t}-1\). It decreases strictly from \(f_m(0)=m+1\) to \(-1\). Hence it has exactly one positive root and changes sign once, giving the complete optimization classification and the strict failure of largest-diagonal pivoting afterward.

The root equation can be rearranged as
\[
e^{-(m+1)\tau_m}(1+me^{-\tau_m})=1-e^{-\tau_m}.
\]
Comparison at \(t=(\log m)/m\) and \(t=3(\log m)/m\) shows that, for all large \(m\), \(z_m=m\tau_m=\Theta(\log m)\). Uniform Taylor expansions of the preceding equation on that range yield
\[
z_me^{z_m}=m^2\left(1+O\!\left(\frac{z_m}{m}\right)\right).
\]
The positive branch of \(W\) has bounded derivative with respect to the logarithm of its argument. Thus \(z_m=W(m^2)+O((\log m)/m)\), proving the stated sharp scale.

For fixed \(t>0\), \(a\in(0,1)\) is constant and \(b=a^{m+1}\to0\), so the explicit formulas give \(G_h(t)\to1\), \(G_\ell(t)\to a\). The principal eigenvalue of \(K_m(t)\) is \(1\), simple, with normalized eigenvector \(\mathbf1/\sqrt{m+1}\), so rank-one spectral-leverage probabilities are uniform. The first-step diagonal-proportional hub probability is
\[
p_h^{\rm diag}(t)=\frac{H(t)}{\operatorname{tr}K_m(t)}
=\frac{1+mb}{(m+1)(1+(m-1)a+b)}\sim\frac{e^t}{m^2}.
\]
For any rule selecting the hub with probability \(p_h\), every nonhub has the same gain; once \(t>\tau_m\), its expected excess trace error is exactly \((1-p_h)(G_h-G_\ell)\). Taking the limit finishes both sampling-regret assertions.

## Verification
The accompanying standalone `CHECK.py` uses only Python's standard library. It constructs the three spectral projectors over exact rational arithmetic, multiplies the full heat-kernel matrix symbolically at rational \(a=e^{-t}\) and verifies the semigroup law, trace-gain factorization, diagonal ranking and crossover signs for \(2\le m\le14\) and six rational \(a\) values. It separately bisects the unique crossing for ten star sizes. These are finite consistency checks; the general theorem and asymptotic claims follow from the analytical derivation above. An independent numerical check also compared the formulas with matrix exponentials of the graph Laplacian for several star sizes.

## Relationship to prior work
Drineas and Mahoney developed the sampled-column Nyström framework; Gittens and Mahoney analyzed leverage-based sampling and nuclear/trace error. Those are foundational results, not new contributions here. Chen, Epperly, Tropp and Webber develop the randomly pivoted Cholesky framework and compare diagonal-greedy, uniform and diagonal-proportional pivoting; the present exact structural family shows how the first pivot can systematically misidentify the best trace-error column. The new object-specific statement is the unique heat-time crossover, its Lambert scaling and the resulting failure probabilities and limiting regret, not the elementary general identity \(G_v=(K^2)_{vv}/K_{vv}\).

## Limitations
This is a deterministic single-pivot example, not a lower bound against multi-pivot randomized methods, oversampling guarantees, or approximate rank-one SVD. The absolute regret tends to a positive constant at fixed time, but the *relative* regret compared with the full residual trace need not remain positive because the latter may grow with \(m\). The statement concerns exact arithmetic and combinatorial heat kernels. The originality assessment is limited to the inspected literature and records, and independent mathematical validation has not been performed.

## References
1. P. Drineas and M. W. Mahoney, *On the Nyström Method for Approximating a Gram Matrix for Improved Kernel-Based Learning*, JMLR 6 (2005), 2153–2175. https://www.jmlr.org/papers/volume6/drineas05a/drineas05a.pdf
2. A. Gittens and M. W. Mahoney, *Revisiting the Nyström Method for Improved Large-Scale Machine Learning*, arXiv:1303.1849 (first publicly posted 2013-03-07); Proceedings of ICML 2013. https://arxiv.org/abs/1303.1849
3. Y. Chen, E. N. Epperly, J. A. Tropp and R. J. Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations*, Communications on Pure and Applied Mathematics, first published 2024-12-04. https://doi.org/10.1002/cpa.22234
