# Strictly convex spectral filters and exact control resonances on complete bipartite networks

## Finding

Let \(p,q\ge 2\) be integers, let \(G=K_{p,q}\) have its unit-weight combinatorial Laplacian \(L\), and let \(N=p+q\). Fix a real-valued function \(f:[0,\infty)\to\mathbb R\) that is strictly convex and satisfies \(f(0)=1\). For \(h\ge0\), consider the **discrete-time, directly actuated** system

\[
z_{k+1}=T_f(h)z_k+B_Su_k,\qquad T_f(h)=f(hL),
\]

where \(B_S\) has one independent standard coordinate column for every vertex in \(S\subseteq V(G)\). Define \(\kappa_f(h)\) as the least cardinality of such a set making the pair \((T_f(h),B_S)\) Kalman-controllable. The following is an exact classification for **every** such function and every pair of part sizes:

* At \(h=0\), \(\kappa_f(0)=N\).
* For every \(h>0\) and \(p\ne q\), \(\kappa_f(h)=N-2\). Every minimum set leaves exactly one vertex unactuated in each part, and no other set of cardinality \(N-2\) works.
* For \(h>0\) and \(p=q=m\), set
  \[
  \mathcal R_f(m)=\{h>0:f(mh)=f(0)\text{ or }f(mh)=f(2mh)\}.
  \]
  Then
  \[
  \kappa_f(h)=\begin{cases}2m-1,&h\in\mathcal R_f(m),\\2m-2,&h\notin\mathcal R_f(m).\end{cases}
  \]
  Outside the resonances, every minimum set omits one vertex from each part. At a resonance, every choice of \(2m-1\) actuated vertices is controllable. The two equality types cannot hold simultaneously at positive \(h\).

This includes the classical explicit second-order and fourth-order Taylor heat steps

\[
F_2(x)=1-x+\frac{x^2}{2},\qquad F_4(x)=1-x+\frac{x^2}{2}-\frac{x^3}{6}+\frac{x^4}{24},
\]

which are both strictly convex on \([0,\infty)\). On \(K_{m,m}\), the exceptional **positive** timesteps for \(F_2(hL)\) are exactly

\[
h=\frac{2}{3m}\quad\text{and}\quad h=\frac2m.
\]

For \(F_4(hL)\), the exceptional positive timesteps are exactly

\[
h=\frac{\gamma}{m}\quad\text{and}\quad h=\frac{\beta}{m},
\]

where \(\gamma\) and \(\beta\) are the unique positive roots of the cubics

\[
24-36\gamma+28\gamma^2-15\gamma^3=0,\qquad
\beta^3-4\beta^2+12\beta-24=0.
\]

Numerically, \(\gamma\approx1.03893381686387255\) and \(\beta\approx2.78529356340528162\). At the first exceptional step for either method, **the update is a strictly positive stochastic matrix, yet the minimum number of coordinate inputs jumps from \(N-2\) to \(N-1\)**. In particular,

\[
F_2\!\left(\frac{2L}{3m}\right)=\frac59 I+\frac49\frac{\mathbf1\mathbf1^\top}{2m},
\]

and

\[
F_4\!\left(\frac{\gamma L}{m}\right)=cI+(1-c)\frac{\mathbf1\mathbf1^\top}{2m},\quad
c=F_4(\gamma)=F_4(2\gamma)\in(0,1).
\]

Thus nonnegative, mass-preserving state propagation does **not** by itself ensure preservation of a minimum coordinate-control placement.

## Assumptions and scope

The graph is simple, undirected and unweighted, with both bipartition classes of size at least two. \(L\) is the **combinatorial** Laplacian, not the normalized Laplacian. All inputs are independently applied at selected **state coordinates**. The system is the specified pair \((f(hL),B_S)\); it is not the zero-order-hold or Runge–Kutta discretization of the full forced differential equation with its corresponding transformed input matrix. At \(h=0\) the state transition equals \(I\), and the separate assertion above applies. The theorem concerns algebraic Kalman controllability, not robustness, Gramian conditioning, or finite input energy.

Strict convexity is essential to the general argument: an arbitrary noninjective filter can identify three or more distinct Laplacian eigenvalues, invalidating the three-level obstruction. No positivity assumption on a general filter \(f\) is needed; positivity is proved separately for the first RK2/RK4 resonance.

## Proof

**Step 1 (the exact eigenspaces).** Write the bipartition as \(A\sqcup B\), with \(|A|=p\) and \(|B|=q\). With coordinates ordered by the two parts,

\[
L=\begin{pmatrix}qI_p&-\mathbf1_p\mathbf1_q^\top\\-\mathbf1_q\mathbf1_p^\top&pI_q\end{pmatrix}.
\]

The mutually orthogonal eigenspaces are

\[
E_0=\operatorname{span}\{\mathbf1_A+\mathbf1_B\},\qquad
E_N=\operatorname{span}\{q\mathbf1_A-p\mathbf1_B\},
\]

and

\[
E_q=\{x:\operatorname{supp}x\subseteq A,\ \sum_{A}x=0\},\qquad
E_p=\{x:\operatorname{supp}x\subseteq B,\ \sum_{B}x=0\}.
\]

Their eigenvalues are \(0,N,q,p\) and dimensions \(1,1,p-1,q-1\), respectively. When \(p=q=m\), the last two spaces share eigenvalue \(m\), and their direct sum has dimension \(2m-2\).

**Step 2 (PBH and two missing vertices).** The PBH test for a real symmetric state matrix says the system is uncontrollable exactly when an eigenvector vanishes on all controlled coordinates. For \(|S|=N-2\), write the two uncontrolled coordinates as \(u,v\). A witness must be supported on \(\{u,v\}\). If both lie in the same bipartition class, \(e_u-e_v\) belongs to that class's zero-sum eigenspace of \(L\), hence is an eigenvector of \(f(hL)\) for **every** \(h\). This proves that every \(N-2\)-input controlling set must omit one vertex from each part. If at most \(N-3\) inputs are chosen, the pigeonhole principle leaves two uncontrolled vertices in one part, so no smaller set ever suffices.

Now take \(u\in A\), \(v\in B\), and write an arbitrary vector on those two vertices as \(w=\alpha e_u+\delta e_v\). Its projections onto \(E_q\) and \(E_p\) are

\[
\alpha\left(e_u-\frac{\mathbf1_A}{p}\right),\qquad
\delta\left(e_v-\frac{\mathbf1_B}{q}\right),
\]

and are nonzero exactly when the corresponding coefficients are. Its projections onto \(E_0\) and \(E_N\) are nonzero exactly when, respectively,

\[
\alpha+\delta\ne0,\qquad q\alpha-p\delta\ne0.
\]

**Step 3 (the unequal-part immunity).** If \(p\ne q\), the four Laplacian eigenvalues \(0,p,q,N\) are distinct. A nonzero vector supported on \(\{u,v\}\) has nonzero projections on **at least three distinct eigenspaces**: with one coefficient zero, the surviving local contrast plus both global modes are active; with both coefficients nonzero, both distinct local contrasts are active and the two global-mode coefficients cannot vanish simultaneously. A strictly convex real function takes any fixed value at at most two distinct arguments in an interval: if three ordered arguments had the same value, strict convexity at the middle argument would contradict equality. Applied to \(x\mapsto f(hx)\) for \(h>0\), this means that three distinct Laplacian eigenvalues cannot be mapped to one eigenvalue of \(T_f(h)\). Consequently no such nonzero \(w\) can be an eigenvector of \(T_f(h)\). The PBH test proves that exactly one uncontrolled vertex in each part works for all \(h>0\).

**Step 4 (the equal-part resonances).** If \(p=q=m\), the projections of a nonzero \(w\) onto \(E_m=E_p\oplus E_q\) are never jointly zero. The \(E_0\) projection vanishes precisely for \(\delta=-\alpha\); the \(E_{2m}\) projection vanishes precisely for \(\delta=\alpha\). If neither vanishes, \(w\) has three distinct spectral levels, impossible for an eigenvector of \(T_f(h)\) by strict convexity. The choice \(w=e_u-e_v\) is an eigenvector precisely when \(f(mh)=f(2mh)\), and \(w=e_u+e_v\) is an eigenvector precisely when \(f(0)=f(mh)\). This proves the claimed exact resonance condition for all placements with two unactuated vertices. At a resonance, the merged eigenspace has dimension \(2m-1\), forcing at least \(2m-1\) coordinate inputs by PBH. Conversely, any single-coordinate vector \(e_u\) has nonzero projections on all three eigenspaces \(E_0,E_m,E_{2m}\), so it cannot be an eigenvector of \(T_f(h)\) for \(h>0\). Thus every \(N-1\)-input placement works. The same argument shows that the two exceptional equality types are disjoint.

**Step 5 (exact RK2 and RK4 thresholds).** For \(F_2\), elementary factorization gives \(F_2(x)=F_2(2x)\) at positive \(x\) exactly for \(x=2/3\), and \(F_2(x)=F_2(0)\) exactly for \(x=2\). For \(F_4\), the same equalities become

\[
F_4(x)-F_4(2x)=\frac{x}{24}(24-36x+28x^2-15x^3),
\]

\[
F_4(x)-1=\frac{x}{24}(x^3-4x^2+12x-24).
\]

The first cubic has derivative \(-36+56x-45x^2<0\) for all real \(x\), and has opposite signs at \(x=1\) and \(x=11/10\). The second cubic has derivative \(3x^2-8x+12>0\) for all real \(x\), and has opposite signs at \(x=11/5\) and \(x=3\). Each therefore has exactly one positive zero, with \(1<\gamma<11/10<\beta/2\) and \(11/5<\beta<3\). Since \(F_4(x)>0\) for \(x\ge0\) (positive even Taylor truncation of \(e^{-x}\)), and \(F_4(x)<1\) for \(0<x<\beta\), their common value \(c=F_4(\gamma)=F_4(2\gamma)\) belongs to \((0,1)\). Both RK2/RK4 first-resonance matrices therefore have eigenvalue \(1\) on the constant vector and a common eigenvalue \(c\in(0,1)\) on its orthogonal complement, giving the stated strictly positive stochastic complete-graph kernels.

At \(h=0\), the transition is the identity, so \(\kappa_f(0)=N\). This finishes all cases.

## Verification

The standalone `verify.py` performs exact rational matrix construction and full Kalman-Krylov rank calculations, rather than relying on floating-point eigenvalue rank tolerances. It checks both \(F_2\) and \(F_4\) on all \(K_{p,q}\) with \(2\le p,q\le4\), at several rational timesteps including the **exact** two RK2 resonances, and tests all choices of two omitted vertices together with representative one-omission sets. The delivered replay returned `OK`: 100 rational matrices, 1,884 exact coordinate-rank checks, 1,584 two-omission checks. It separately checks the symbolic second-order identities and rational isolation intervals \(1.038933<\gamma<1.038934\), \(2.785293<\beta<2.785294\).

The exact RK4 resonances are proved algebraically in Step 5; finite rational-step testing does not verify an irrational zero by numerical approximation, and is not the justification of the infinite-family theorem. Reproduce with `python3 verify.py` using only the Python standard library.

## Relationship to prior work

The PBH/Kalman spectral criterion is classical. Burgarth, D'Alessandro, Hogben, Severini and Young (2011) connect graph zero forcing to linear controllability; Monshizadeh, Zhang and Camlibel (2014) give structural zero-forcing criteria for graph-based systems, including qualitative classes of discrete state matrices. Those results concern either the given generator or an entire graph-sparsity class, rather than the exact spectral mergers of a specified \(f(hL)\) and a minimal fixed-coordinate actuator set.

Apers and Sarlette (2015), in their original public preprint, study polynomial spectral filtering of consensus, specifically discuss balanced and unbalanced complete bipartite graphs in Section 2.1, and analyze eigenvalue clustering and robustness. Their objective is convergence speed and finite-time consensus, not coordinate-input controllability at a prescribed filter and the input-rank jumps classified here. Their spectral-clustering discussion is directly relevant motivation, and its complete-bipartite examples are not claimed as new here. Mousavi, Haeri and Mesbahi (2018) classify minimal inputs for the original Laplacian dynamics on cographs, including complete bipartite graphs; the continuous-time \(N-2\) baseline is thus a known consequence of prior graph-mode analysis. It does not decide which polynomial filters merge critical eigenspaces at positive timesteps. The distinction between injective and noninjective spectral maps is also classical; the new conclusion is the all-filter, all-part-size input classification and the exact positivity-compatible resonance instances.

## Limitations

This result is specifically about an unweighted, two-part complete bipartite Laplacian and independently applied coordinates. It does not establish the same dichotomy for arbitrary weighted bipartite graphs, more than two parts, arbitrary nonconvex spectral functions, or physical zero-order-hold discretization of controlled continuous-time equations. Strict convexity is a sufficient hypothesis for the exact classification, not shown necessary. Positive stochasticity is claimed only at the first RK2/RK4 resonances, not for all positive timesteps. No independent mathematical review or specialist publication-priority certification has been undertaken.

## References

1. Burgarth, D., D'Alessandro, D., Hogben, L., Severini, S., and Young, M., *Zero forcing, linear and quantum controllability for systems evolving on networks*, arXiv:1111.1475v1, first posted 2011-11-07, https://arxiv.org/abs/1111.1475.
2. Monshizadeh, N., Zhang, S., and Camlibel, M. K., *Zero forcing sets and controllability of dynamical systems defined on graphs*, arXiv:1403.4868v1, posted 2014-03-19, https://arxiv.org/abs/1403.4868.
3. Apers, S., and Sarlette, A., *Accelerating Consensus by Spectral Clustering and Polynomial Filters*, arXiv:1503.01269v1, first posted 2015-03-04, https://arxiv.org/abs/1503.01269.
4. Mousavi, S. S., Haeri, M., and Mesbahi, M., *Laplacian Dynamics on Cographs: Controllability Analysis through Joins and Unions*, arXiv:1802.03599, first posted 2018-02-10; inspected accessible v2, https://arxiv.org/abs/1802.03599.
