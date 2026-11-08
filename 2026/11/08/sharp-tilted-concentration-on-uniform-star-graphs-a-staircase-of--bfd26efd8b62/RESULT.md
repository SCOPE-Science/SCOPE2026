# Sharp tilted concentration on uniform star graphs: a staircase of leaf-sign extremizers

## Finding

For every integer \(n\ge 3\), let \(S_n=K_{1,n}\) be the unit-edge star with one hub and \(n\) leaves, under the uniform probability measure on its \(N=n+1\) vertices. Define the optimal centered Laplace transform
\[
\mathcal L_n(t)=\max_{\operatorname{Lip}(f)\le1}\frac1N\sum_{v\in V(S_n)}\exp\bigl(t(f(v)-\overline f)\bigr),\qquad
\overline f=\frac1N\sum_v f(v).
\]
For every \(t>0\), put
\[
X_n(t)=\frac1{\exp(2t/N)-1}-\frac{1+n\exp(-t)}{\exp(t)-\exp(-t)},\qquad
k_n(t)=\lceil X_n(t)\rceil.
\]
Then \(0<X_n(t)<(n-1)/2\) and
\[
\boxed{\mathcal L_n(t)=\frac{1+(n-k_n(t))\exp(-t)+k_n(t)\exp(t)}{N}
\exp\!\left(-\frac{(2k_n(t)-n)t}{N}\right).}
\]
Every maximizer, modulo an additive constant, has hub value zero, exactly \(k_n(t)\) leaves equal to \(+1\), and all other leaves equal to \(-1\). When \(X_n(t)\) is an integer \(j\), both \(j\) and \(j+1\) positive leaves maximize, and there are no other maximizers. All choices of leaves of the indicated cardinalities occur.

The function \(X_n\) is strictly decreasing from \((n-1)/2\) to \(0\). Consequently there are exactly \(\lfloor n/2\rfloor-1\) distinct positive tilt thresholds, the unique solutions to \(X_n(t)=j\) for \(1\le j\le\lfloor n/2\rfloor-1\). Between thresholds the maximizing count is constant and decreases one at a time as \(t\) increases. For all sufficiently large \(t\), precisely one leaf has value \(+1\). Reflection of the potential gives \(\mathcal L_n(-t)=\mathcal L_n(t)\).

At any fixed \(t>0\), the asymptotic optimizing leaf fraction and optimal Laplace transform are
\[
\boxed{\lim_{n\to\infty}\frac{k_n(t)}n=\frac1{2t}-\frac1{\exp(2t)-1},\qquad
\lim_{n\to\infty}\mathcal L_n(t)=\frac{\sinh t}{t}\exp(t\coth t-1).}
\]
The second formula extends continuously to value \(1\) at \(t=0\).

## Assumptions and scope

The graph has exactly one hub and \(n\ge3\) labelled leaves, each joined only to the hub by an edge of length one; graph distance between distinct leaves is two. Functions are real-valued and satisfy \(|f(u)-f(v)|\le1\) on every edge. The probability measure is uniform on all \(n+1\) vertices. The optimization includes every real potential, not just integer potentials, and is invariant under adding a constant. The sharp equality classification is stated for \(t>0\) (at \(t=0\) every potential gives one). The smaller \(n=2\) star is the three-vertex path and belongs to prior path results.

## Proof

**1. The full continuous optimization reduces strictly to signs.** Fix \(f(o)=0\) at the hub. The feasible leaf vector is the full cube \([-1,1]^n\). For a fixed \(t>0\), its logarithmic centered Laplace transform is a log-sum-exp of affine functions minus a linear mean. Its Hessian on the leaf coordinates is \(t^2\) times the covariance matrix of the leaf-coordinate indicator vectors under the strictly positive exponentially tilted vertex distribution. Because that distribution gives strictly positive mass to the hub (whose leaf-coordinate vector is zero), this covariance matrix is positive definite. Thus the objective is strictly convex on \([-1,1]^n\). A maximum therefore occurs only at a cube vertex: every maximizing leaf value is \(+1\) or \(-1\). This also excludes any additional non-sign equality cases.

**2. Optimize the number of positive leaves exactly.** If precisely \(k\) leaves equal \(+1\), the mean is \((2k-n)/N\). Write
\[
F_k(t)=\frac{1+(n-k)e^{-t}+k e^t}{N}\,e^{-(2k-n)t/N},\quad 0\le k\le n.
\]
Set \(A_k=1+(n-k)e^{-t}+k e^t\) and \(\Delta=e^t-e^{-t}>0\). Then
\[
\frac{F_{k+1}(t)}{F_k(t)}=e^{-2t/N}\left(1+\frac{\Delta}{A_k}\right).
\]
This ratio is greater than, equal to, or less than one according as \(k\) is less than, equal to, or greater than
\[
\frac1{e^{2t/N}-1}-\frac{1+n e^{-t}}{e^t-e^{-t}}=X_n(t).
\]
The ratios decrease strictly with \(k\). Hence the sole maximum count is \(\lceil X_n(t)\rceil\), except that if \(X_n(t)=j\) exactly, \(F_j=F_{j+1}\) and these are the only two maximum counts.

**3. Rigorous monotonicity and phase counting.** A hyperbolic rearrangement gives
\[
X_n(t)=\frac{n-1}2+\frac12\left(\coth(t/N)-n\coth t-\operatorname{csch}t\right).
\]
Differentiating, \(X_n'(t)<0\) is equivalent, with \(y=t/N>0\), to
\[
\left(\frac{\sinh(Ny)}{\sinh y}\right)^2>N\bigl(N-1+\cosh(Ny)\bigr).
\]
The elementary identity
\[
\left(\frac{\sinh(Ny)}{\sinh y}\right)^2
=N+2\sum_{j=1}^{N-1}(N-j)\cosh(2jy)
\]
reduces the desired strict inequality to
\[
2\sum_{j=1}^{N-1}(N-j)\bigl(\cosh(2jy)-1\bigr)
>N\bigl(\cosh(Ny)-1\bigr).
\]
For \(N\ge5\), the indices \(j>N/2\) alone have coefficient sum \(\sum_{j>N/2}(N-j)\ge N/2\), and each corresponding \(\cosh(2jy)-1\) strictly exceeds \(\cosh(Ny)-1\). For \(N=3,4\), use respectively the single terms \(j=2\) and \(j=3\), and the strict inequality \((\cosh(ay)-1)/(\cosh(by)-1)>(a/b)^2\) when \(a>b>0\); the resulting lower factors are \(2(4/3)^2>3\) and \(2(6/4)^2>4\). Thus \(X_n'\) is strictly negative for every \(n\ge2\).

Elementary expansions give \(\lim_{t\downarrow0}X_n(t)=(n-1)/2\). As \(t\to\infty\), its first term is asymptotic to \(e^{-2t/N}\), which dominates the exponentially smaller second term when \(N\ge3\), hence \(X_n(t)\to0\) from above. The strictly decreasing continuous curve crosses exactly each integer \(j\) with \(1\le j<(n-1)/2\), which is precisely \(j=1,\ldots,\lfloor n/2\rfloor-1\). This proves the complete staircase and equality cases.

**4. Infinite-leaf limit.** At fixed positive \(t\), division of the defining expression for \(X_n(t)\) by \(n\) yields
\[
\frac{X_n(t)}n\longrightarrow p(t)=\frac1{2t}-\frac1{e^{2t}-1}.
\]
Since \(0\le k_n(t)-X_n(t)<1\), the leaf fraction has the same limit. Writing \(a(t)=2p(t)-1=1/t-\coth t\), the centered discrete Laplace transform converges to \(e^{-a(t)t}(\cosh t+a(t)\sinh t)\). Using \(\cosh t+a(t)\sinh t=\sinh t/t\) gives exactly the stated limit.

## Verification

A self-contained standard-library program `scripts/check_star_laplace.py` enumerates all \(2^n\) leaf-sign assignments for small stars; independently compares the proposed maximizing count against every \(F_k\) at 77 exact rational exponential tilts \(t=N\log r\); checks the exact variance and parity of small-tilt optimizers for 199 sizes; tests tilt monotonicity at multiple sizes; and checks the infinite-leaf limit numerically. In its exact tests, each centered moment is a rational number because \(e^{t/N}=r\) is rational. The finite tests are corroboration, not a substitute for steps 1–4.

## Relationship to prior work

Bobkov, Houdré and Tetali (2006) define optimal centered graph Laplace transforms and determine formulas for paths and complete graphs, including the three-vertex path \(K_{1,2}\). Their path argument exploits line ordering; their complete-graph argument uses pairwise distance one. Neither metric hypothesis describes \(K_{1,n}\) for \(n\ge3\), which has branching and distinct-leaf distance two. Sammer and Tetali (2009) study transportation bounds and cycle/exponential-moment constants, rather than this star-specific sharp optimizer staircase. Prior published work supplies the concentration framework and convexity principle, not the formula, strict derivative inequality, complete tilt transitions, or asymptotic optimizing fraction established here. Database searches did not identify a directly matching claim; absence from a search is not a uniqueness theorem.

## Limitations

This is an exact result for the full centered moment generating envelope \(\mathcal L_n(t)\), not an elementary closed-form evaluation of the further optimization \(\sup_{t>0}2t^{-2}\log\mathcal L_n(t)\) defining the sub-Gaussian variance proxy. It does not cover unequal vertex masses, weighted edges, other trees, or arbitrary graph products. Finite experiments alone would not establish the universal theorem. An equivalent result could exist in literature not indexed by the searches described here; independent verification has not been performed.

## References

1. S. G. Bobkov, C. Houdré and P. Tetali, *The subgaussian constant and concentration inequalities*, Israel Journal of Mathematics **156** (2006), 255–283, DOI: 10.1007/BF02773835. Author-accessible full text: https://tetali.math.gatech.edu/PUBLIS/BHT_SUB85.pdf. Relevant material: Sections 1, 3 and 6.
2. M. Sammer and P. Tetali, *Concentration on the discrete torus using transportation*, Combinatorics, Probability and Computing **18** (2009), 835–860, DOI: 10.1017/S0963548309990319. Author-accessible full text: https://tetali.math.gatech.edu/PUBLIS/torus_Jun3.pdf. Relevant material: Introduction and Sections 3–5.
