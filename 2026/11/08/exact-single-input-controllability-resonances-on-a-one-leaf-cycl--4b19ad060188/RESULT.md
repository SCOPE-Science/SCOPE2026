# Exact single-input controllability resonances on a one-leaf cycle

## Finding

For every integer \(n\ge3\), form a weighted tadpole (also called an \(n\)-pan graph) by giving the edges of the cycle \(0,1,\ldots,n-1,0\) conductance \(1\), and adding one leaf vertex \(p\) joined only to cycle vertex \(0\) with conductance \(t>0\). Write \(L_n(t)\) for the weighted combinatorial Laplacian. Apply one scalar input at vertex \(1\) to the continuous-time system \(\dot z=-L_n(t)z+e_1u\).

For each odd integer \(\ell\) satisfying \(1\le\ell\le n-3\), put

\[
\lambda_{n,\ell}=2-2\cos\!\left(\frac{\pi\ell}{n-2}\right),\qquad
\mathcal I_n=\left\{\ell:\ell\ \text{odd},\ 1\le\ell\le n-3,\ 3\ell<n-2\ \text{or}\ 2\ell>n-2\right\},
\]

and, only when \(\ell\in\mathcal I_n\), put

\[
t_{n,\ell}=\frac{\lambda_{n,\ell}(2-\lambda_{n,\ell})}{2(1-\lambda_{n,\ell})}>0.
\]

Then the exact rank of the \((n+1)\)-dimensional Kalman controllability matrix is

\[
\boxed{\operatorname{rank}\,[e_1,L_n(t)e_1,\ldots,L_n(t)^n e_1]
=n+1-\#\{\ell\in\mathcal I_n:t=t_{n,\ell}\}.}
\]

In particular, this single-input system is controllable except at the explicitly listed positive edge weights; at every exceptional weight the rank loss is at most two. Two sharp arithmetic examples are

\[
\begin{aligned}
t=1:\quad&\operatorname{rank}=n+1-2\mathbf 1_{\{n\equiv6\pmod8\}},\\
t=\tfrac12:\quad&\operatorname{rank}=n+1-2\mathbf 1_{\{n\equiv7\pmod{10}\}}.
\end{aligned}
\]

## Assumptions and scope

The cycle is simple, with \(n\ge3\); its every edge has conductance \(1\). The extra edge has real conductance \(t>0\). The Laplacian is the *unnormalized symmetric conductance Laplacian*: \((Lz)_i=\sum_jw_{ij}(z_i-z_j)\), with the leaf indexed by \(p=n\), so the state dimension is \(n+1\). There is precisely one input, in cycle coordinate \(1\). No assertion is made for a directed, normalized, stochastic, signed, negative-weight, multiple-leaf, or arbitrary-weighted-cycle model. The rank formula concerns exact real arithmetic and standard Kalman controllability of the fixed matrix, not qualitative strong structural controllability of all weight assignments.

## Proof

**1. Reflection sectors and simplicity.** Reflect the cycle by \(i\mapsto n-i\pmod n\), fixing cycle vertex \(0\) and the leaf \(p\). This is an involution commuting with \(L_n(t)\). Its odd sector has the distinct eigenpairs

\[
v^{(k)}_i=\sin(2\pi ki/n),\quad v^{(k)}_p=0,\quad
\mu_k=2-2\cos(2\pi k/n),\quad
1\le k\le\lfloor(n-1)/2\rfloor.
\]

Each such eigenvector has \(v^{(k)}_1\ne0\). In the normalized reflection-orbit basis, ordered from the leaf through vertex \(0\) to successive mirrored pairs and (for even \(n\)) the antipodal singleton, the even-sector restriction of \(L_n(t)\) is a real symmetric irreducible tridiagonal matrix: its successive off-diagonal entries have nonzero magnitudes \(t\), \(\sqrt2\), and positive adjacency coefficients of the remaining cycle orbits. For odd \(n\), the terminal mirrored pair has an internal edge, changing only its diagonal. For even \(n\), the last edge to the antipodal singleton has nonzero magnitude \(\sqrt2\). The even sector therefore has simple real eigenvalues by the standard irreducible-Jacobi recurrence.

The two sector spectra are disjoint. Suppose an even eigenvector \(y\) had an odd-sector eigenvalue \(\mu_k>0\). On the cycle, its eigenvector equation is

\[
(L_{C_n}-\mu_k I)y_{\mathrm{cycle}}=t(y_p-y_0)e_0.
\]

Taking the inner product with the \(k\)-th cosine eigenvector \(\cos(2\pi ki/n)\), whose value at vertex \(0\) is one, gives \(y_p=y_0\). The leaf equation \(t(y_p-y_0)=\mu_k y_p\) then forces \(y_p=y_0=0\). Hence \(y_{\mathrm{cycle}}\) is an even eigenvector of \(L_{C_n}\) at \(\mu_k\) with value zero at vertex \(0\), impossible because its even eigenspace is spanned by the corresponding cosine vector, with value one at \(0\). Thus all \(n+1\) eigenvalues of \(L_n(t)\) are simple.

**2. Characterization of modes invisible at vertex \(1\).** Let \(v\ne0\) be an eigenvector with eigenvalue \(\lambda\) and \(v_1=0\). Simplicity allows the eigenvector to be chosen with definite reflection parity. Odd eigenvectors cannot vanish at vertex \(1\), so \(v\) is even and \(v_{n-1}=0\). Also \(v_0\ne0\): otherwise the equation at vertex \(1\) forces \(v_2=0\), successive cycle equations force every cycle coordinate zero, and the leaf equation and connectivity force \(v_p=0\).

On the path of interior vertices \(1,2,\ldots,n-1\), the eigenvector recurrence is

\[
v_{i+1}=(2-\lambda)v_i-v_{i-1}\quad(2\le i\le n-2),
\qquad v_1=v_{n-1}=0.
\]

A nontrivial Dirichlet path eigenvector therefore has, for exactly one integer \(1\le\ell\le n-3\),

\[
\lambda=2-2\cos\theta,\quad\theta=\frac{\pi\ell}{n-2},\quad
v_i=c\sin((i-1)\theta),\quad c\ne0.
\]

Reflection evenness is equivalent to \((-1)^{\ell+1}=1\), hence \(\ell\) is odd. The equation at vertex \(1\) gives \(v_0=-v_2=-c\sin\theta\ne0\); the equation at vertex \(n-1\) is then consistent because \(\ell\) is odd. At the root and leaf, the remaining equations are

\[
(2+t-\lambda)v_0-tv_p=0,\qquad-tv_0+(t-\lambda)v_p=0.
\]

A nonzero solution exists if and only if

\[
\lambda^2-2(1+t)\lambda+2t=0,
\]

or equivalently

\[
t=\frac{\lambda(2-\lambda)}{2(1-\lambda)}.
\]

The exceptional quotient is positive precisely for \(0<\lambda<1\) or \(2<\lambda<4\). Under \(\lambda=2-2\cos(\pi\ell/(n-2))\), these conditions are respectively \(3\ell<n-2\) and \(2\ell>n-2\). At \(\lambda=1\) the quadratic cannot hold for \(t>0\); at \(\lambda=2\) it forces \(t=0\); the Dirichlet eigenvalues lie strictly in \((0,4)\). Therefore every invisible eigenvector determines a unique \(\ell\in\mathcal I_n\) with \(t=t_{n,\ell}\).

Conversely, for any such index, choose \(c=1\), \(v_0=-\sin\theta\), \(v_i=\sin((i-1)\theta)\) for \(1\le i\le n-1\), and \(v_p=t v_0/(t-\lambda)\). The scalar equation implies \(t\ne\lambda\), so the leaf coordinate is well-defined. The cycle recurrence, reflection condition, root equations, and leaf equation now hold, yielding a nonzero eigenvector with \(v_1=0\). This proves the exact correspondence.

**3. Rank and special weights.** For a real symmetric matrix with simple spectrum, the PBH criterion and an eigenbasis representation of the Krylov matrix show that its controllability rank equals the number of eigenvectors with a nonzero coordinate at the actuated vertex. Thus each listed \(\ell\) reduces the rank by exactly one. The quadratic from step 2 has at most two distinct roots, giving the stated maximum deficiency.

For \(t=1\), that quadratic has roots \(2\pm\sqrt2\), realized by \(\theta=\pi/4,3\pi/4\). Both corresponding Dirichlet indices are odd exactly when \(n-2\) is four times an odd integer, i.e. \(n\equiv6\pmod8\); otherwise neither is an eligible odd integer. For \(t=\tfrac12\), the roots are \((3\pm\sqrt5)/2\), realized by \(\theta=\pi/5,3\pi/5\); both are eligible exactly when \(n-2\) is five times an odd integer, i.e. \(n\equiv7\pmod{10}\). This completes the proof for all \(n\ge3\) and \(t>0\).

## Verification

Run the supplied standalone standard-library program using `python3 verify.py`. It constructs the exact rational Laplacian action, computes full Krylov ranks over two large prime fields for 322 graph-and-weight cases (all \(3\le n\le48\) and seven rational weights), checks 785 explicitly constructed resonant eigenvectors numerically for \(3\le n\le64\), and compares both modular rank-loss laws through \(n=100\) (196 checks). Exact finite-field tests are supportive: they neither independently prove the infinite family nor establish the correctness of floating-point near-equality at arbitrary positive irrational weights. The analytical argument above handles the infinite family, the parameter boundaries, and absence of hidden eigenmodes.

## Relationship to prior work

Monshizadeh, Zhang and Camlibel (2014) relate graph zero forcing to controllability over qualitative matrix classes and discuss bare paths and cycles. Their framework does not directly yield the parameter-dependent rank of the single fixed Laplacian here: the singleton \(\{1\}\) cannot be a zero-forcing set because vertex \(1\) has two white neighbors initially, yet this input controls the present graph away from a discrete set of weights. Their discussion explicitly distinguishes controllability of a fixed symmetric Laplacian from control of all matrices in a qualitative class. Hsu (2019) gives controllable interconnected path/antiregular constructions, not a weighted one-leaf cycle with a complete exceptional-conductance classification. Farrugia and Sciriha (2014) address adjacency and signless-Laplacian graph-control criteria; those are different operators and do not imply this weighted Laplacian result. The literature cited below motivates the question and provides methods, not a claimed proof of novelty by absence of search hits.

## Limitations

The theorem is for a single leaf, uniform cycle weights, and the specified input vertex only. It does not classify other leaders, multiple leaves, or arbitrary edge weights. Scientific priority is provisional pending broader literature inspection; in particular, full access to the Liu–Ji study of path and cycle-derived systems was unavailable, and its scope could not be conclusively checked beyond available metadata/abstract. No independent mathematical audit is asserted.

## References

1. N. Monshizadeh, S. Zhang, K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, arXiv:1403.4868v1 (first public March 19, 2014). https://arxiv.org/abs/1403.4868
2. S.-P. Hsu, *Generalising Laplacian controllability of paths*, IET Control Theory & Applications 13 (2019), https://doi.org/10.1049/iet-cta.2018.6214 (public full text).
3. A. Farrugia and I. Sciriha, *Controllability of undirected graphs*, Linear Algebra and its Applications 454 (2014), 138–157, https://www.um.edu.mt/library/oar/handle/123456789/28166 (abstract and access metadata).
4. Y. Liu and Z. Ji, *Controllability of multiagent systems based on path and cycle graphs*, International Journal of Robust and Nonlinear Control, https://doi.org/10.1002/rnc.3870 (abstract/metadata inspected; full paper not available).
