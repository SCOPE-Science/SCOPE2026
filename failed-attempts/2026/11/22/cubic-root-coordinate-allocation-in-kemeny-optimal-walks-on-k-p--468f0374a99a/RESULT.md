# Cubic-root coordinate allocation in Kemeny-optimal walks on \(K_p\square K_q\)

## Finding

For every pair of integers \(p,q\ge2\), the unique symmetric nonnegative stochastic walk on the rook graph \(G=K_p\square K_q\) minimizing the non-return Kemeny constant \(\mathcal K_0\) is specified explicitly as follows. Set \(A=(p-1)/p\) and \(B=(q-1)/q\). Let \(t_{p,q}\) be the unique strictly positive root of
\[
q t^3(t+2)=p(2t+1).
\]
For vertices \((i,j)\), place transition probability
\[
x_* = \frac{t_{p,q}}{p(At_{p,q}+B)}
\quad\text{on each }\{(i,j),(i',j)\},\qquad
y_* = \frac{1}{q(At_{p,q}+B)}
\quad\text{on each }\{(i,j),(i,j')\},
\]
for distinct respective coordinates. Every diagonal holding probability is zero. This statement permits every competitor to use separately chosen transition probabilities on all edges, with positive holding allowed; symmetry of the optimizer is a conclusion, not an assumption.

For fixed \(p\ge2\) and \(q\to\infty\),
\[
t_{p,q}\sim\left(\frac{p}{2q}\right)^{1/3},\qquad
\mathcal K_0^*=pq+\frac{3(p-1)}{(4p)^{1/3}}q^{1/3}+O(1).
\]
For \(p=2\), the globally fastest absolute-eigenvalue mixing symmetric walk has relaxation rates \(\alpha=\beta=2/3\) and Kemeny constant \((9q-3)/4\), whereas the Kemeny-optimal value is \(2q+O(q^{1/3})\). Thus this fastest-mixing walk pays the asymptotically sharp cross-objective penalty
\[
\lim_{q\to\infty}\frac{\mathcal K_0(P_{\mathrm{fast}})}{\mathcal K_0(P_*)}=\frac98.
\]
The word “sharp” here refers only to this explicitly specified fastest-mixing design, not to every possible fastest-mixing minimizer.

## Assumptions and scope

The vertex set is \(\{1,\ldots,p\}\times\{1,\ldots,q\}\), with an edge precisely between different vertices that differ in one coordinate. Consider every real symmetric matrix \(P\) indexed by these vertices such that \(P\mathbf1=\mathbf1\), all its entries are nonnegative, and off-diagonal support is confined to graph edges. Self-loops are allowed, and the chain is assumed irreducible. Stationarity is uniform. Define \(L=I-P\), \(N=pq\), and \(J=\mathbf1\mathbf1^\top/N\). The non-return Kemeny constant is
\[
\mathcal K_0(P)=\operatorname{tr}((L+J)^{-1})-1
=\sum_{k=2}^{N}\frac1{1-\lambda_k(P)}.
\]
This convention omits the additive return-time term of one used in some Kemeny definitions; adding it does not change any optimizer.

## Proof

**1. Global strict convexity and unrestricted symmetry.** For each irreducible feasible \(P\), the restriction \(L|_{\mathbf1^\perp}\) is positive definite. For any nonzero symmetric perturbation \(H\) with \(H\mathbf1=0\), the second directional derivative of the inverse trace on this subspace is
\[
\frac{d^2}{ds^2}\operatorname{tr}((L+sH+J)^{-1})\bigg|_{s=0}
=2\operatorname{tr}((L+J)^{-1}H(L+J)^{-1}H(L+J)^{-1})>0.
\]
The strict inequality follows by conjugating with positive square roots and expressing the trace as a sum of strictly positive weighted squares for \(H\ne0\). Hence the objective is strictly convex in \(P\) on irreducible feasible matrices. Average any candidate over the graph automorphisms \(S_p\times S_q\). This preserves feasibility and connected support, does not increase the objective, and achieves equality only when the candidate is invariant under that group. The invariant matrices have two off-diagonal edge probabilities \(x,y\ge0\) and one common holding probability \(h=1-(p-1)x-(q-1)y\ge0\). Irreducibility requires \(x,y>0\). Strict convexity later proves uniqueness even among symmetry-breaking competitors.

**2. Spectrum and budget saturation.** Put \(\alpha=px\) and \(\beta=qy\). Tensor factor eigenspaces give the nonzero eigenvalues of \(L\): \(\alpha\), with multiplicity \(p-1\); \(\beta\), with multiplicity \(q-1\); and \(\alpha+\beta\), with multiplicity \((p-1)(q-1)\). Consequently
\[
\mathcal K_0(\alpha,\beta)
=\frac{p-1}{\alpha}+\frac{q-1}{\beta}
+\frac{(p-1)(q-1)}{\alpha+\beta},
\qquad A\alpha+B\beta\le1.
\]
For positive \(\alpha,\beta\), increasing both by a common factor strictly decreases every term. Thus the inequality is tight: \(A\alpha+B\beta=1\), equivalently \(h=0\).

**3. Unique algebraic optimum.** Write \(t=\alpha/\beta>0\). The saturated constraint gives \(\beta=(At+B)^{-1}\). The reduced objective is
\[
F(t)=(At+B)\left(\frac{p-1}{t}+q-1+
\frac{(p-1)(q-1)}{1+t}\right).
\]
Exact differentiation and cancellation yield
\[
F'(t)=\frac{(p-1)(q-1)}{pq\,t^2(1+t)^2}
\bigl(qt^4+2qt^3-2pt-p\bigr).
\]
Now \(\phi(t)=t^3(t+2)/(2t+1)\) increases strictly from zero to infinity: its logarithmic derivative is
\[
\frac{\phi'(t)}{\phi(t)}=\frac3t+\frac1{t+2}-\frac2{2t+1}>0
\quad(t>0).
\]
Therefore \(q\phi(t)=p\) has exactly one positive solution. The sign of \(F'\) changes from negative to positive there, proving the explicit unique global minimum. Substituting \(\alpha=t/(At+B)\), \(\beta=1/(At+B)\) gives the stated \(x_*,y_*\).

**4. Singular-size asymptotics.** For fixed \(p\) and \(q\to\infty\), the root identity implies \(t\to0\) and, after division by \(2q\), \(t^3\sim p/(2q)\). Write \(t=u q^{-1/3}\) and expand the exact rational expression in step 3, uniformly for \(u\) in compact positive intervals:
\[
F(uq^{-1/3})=pq+q^{1/3}(p-1)\left(\frac1u+\frac{u^2}{p}\right)+O(1).
\]
The unique minimum of the bracket occurs at \(u=(p/2)^{1/3}\); its value is \(3/(4p)^{1/3}\), completing both asymptotics.

**5. Mixing comparison.** On \(K_2\square K_q\), take \(\alpha=\beta=2/3\). It is feasible because \(\alpha/2+(q-1)\beta/q=1-2/(3q)\le1\), and the nontrivial transition eigenvalues are \(1/3,1/3,-1/3\), with respective multiplicities. Its second-largest absolute eigenvalue is \(1/3\). For any automorphism-invariant candidate of SLEM \(r\), the three eigenvalues enforce \(\alpha,\beta\ge1-r\) and \(\alpha+\beta\le1+r\); hence \(2(1-r)\le1+r\) and \(r\ge1/3\). Because the SLEM is the operator norm of \(P-J\), it is convex and cannot increase upon graph-automorphism averaging. Thus no unrestricted symmetric feasible walk has SLEM below \(1/3\). The exact Kemeny constant of this fastest-mixing walk is \((9q-3)/4\), and step 4 gives the limiting \(9/8\) ratio.

## Verification

The accompanying pure-standard-library program `rook_kemeny_check.py` builds the full \(pq\)-vertex rational matrix \(I-P+J\), inverts it independently by exact Gauss–Jordan elimination, and compares its trace against the tensor eigenvalue expression for small \(p,q\). It also solves the scalar root by bisection, samples alternative allocations, tests boundary constraints, and checks the stated asymptotic regimes and the \(p=2\) fastest-mixing candidate. Its successful execution yielded 990 reported finite exact-algebra, optimizer, and asymptotic assertions. These checks supplement, but do not replace, the all-size analytic proof above.

## Relationship to prior work

Boyd, Diaconis and Xiao give the general symmetric fastest-mixing Markov-chain formulation, minimizing the second-largest absolute eigenvalue, not the Kemeny inverse-trace sum. Boyd, Diaconis, Parrilo and Xiao analyze symmetry reduction and Cartesian-product mixing spectra under that different objective. Agharkar, Patel and Bullo study surveillance/first-passage optimization and formulate general Kemeny-driven convex methods. Zhang and collaborators study mean first-passage network navigation under unweighted graph walks. None of the *inspected portions* of those works states the precise two-factor Kemeny-optimal cubic-root allocation or its \(9/8\) fastest-mixing cost comparison. Generic convexity and product eigenvalues are acknowledged as prior methods; the explicit specialized optimization is the asserted contribution.

## Limitations

No independence, peer review, or exhaustive global literature-priority certification is claimed. The uniqueness assertion is restricted to real symmetric stochastic walks with uniform stationary distribution; arbitrary nonreversible or nonuniform-stationary Markov chains are outside scope. The asymptotic is for fixed \(p\), not for joint unrestricted growth. Finite verifier checks cannot establish all-size correctness without the proof. Unindexed equivalent specializations may exist.

## References

1. S. Boyd, P. Diaconis, and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. DOI: https://doi.org/10.1137/S0036144503423264 . First electronic publication recorded October 29, 2004. Open PDF: https://stanford.edu/~boyd/papers/pdf/fmmc.pdf .
2. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization 20 (2009), 792–819. DOI: https://doi.org/10.1137/070689413 . Open PDF: https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf .
3. P. Agharkar, K. Patel, and F. Bullo, *Robotic surveillance and Markov chains with minimal first passage time* (2014). Open PDF: https://motion.me.ucsb.edu/pdf/2014b-apb-conference.pdf .
4. Z. Zhang et al., *Optimal and suboptimal networks for efficient navigation measured by mean-first passage time of random walks*, arXiv:1211.4295v1 (2012). https://arxiv.org/pdf/1211.4295 .
