# Sharp Crank–Nicolson positivity under asymmetric bipartite degree caps

## Finding

Let \(p>q\ge 2\) be integers. For **every** finite connected simple bipartite graph \(G=(U\sqcup V,E)\) with unit edge conductances, degrees \(d(u)\le p\) for \(u\in U\), and degrees \(d(v)\le q\) for \(v\in V\), let \(L_G=D_G-A_G\) be the ordinary (unnormalized) graph Laplacian and let
\[
C_G(s)=(I+sL_G)^{-1}(I-sL_G),\qquad s\ge0.
\]
Set
\[
\begin{aligned}
B_{p,q}&=2p^2-2pq-2p+q,\\
D_{p,q}&=p(2pq-p-q),\\
t_{p,q}&=\frac{B_{p,q}+\sqrt{B_{p,q}^2+4(2p-1)D_{p,q}}}{2(2p-1)},\\
\sigma_{p,q}&=t_{p,q}^{-1}.
\end{aligned}
\]
Then **every entry** of \(C_G(s)\) is nonnegative whenever \(0\le s\le\sigma_{p,q}\). This bound is sharp uniformly over the entire class: for every \(s>\sigma_{p,q}\), some finite radius ball in the infinite \((p,q)\)-biregular tree, rooted at a degree-\(p\) vertex, has \((C_G(s))_{oo}<0\).

In particular the permissible physical Crank–Nicolson step is \(h\le2\sigma_{p,q}\) (because \(s=h/2\)). The asymmetric condition is strictly more permissive than the sharp maximum-degree-only threshold \(\sigma_p=(2p-1)/(2p(p-1))\):
\[
\sigma_{p,q}>\sigma_p\quad\text{for }p>q\ge2.
\]
For example \(\sigma_{3,2}=5/(1+\sqrt{106})\approx0.4426490543\), compared with \(\sigma_3=5/12\).

## Assumptions and scope

The graph is finite, undirected, connected, simple and bipartite, with at least one edge. The bipartition and its separate **upper** degree caps are part of the assumptions; equality of all actual degrees to their caps is not required. All edge conductances are one, there is no vertex-mass matrix, no Dirichlet killing, and \(L_G\) is not a normalized Laplacian. The infinite tree is used only as a comparison object and source of finite sharpness witnesses. The result is entrywise one-step positivity, not a stability-error estimate or a claim about variable weights. The assertion for \(s=0\) is nonnegativity of the identity; strict positivity is not asserted there.

## Proof

**1. Resolvent criterion.** Let \(R_G(s)=(I+sL_G)^{-1}\). Direct multiplication gives \(C_G(s)=2R_G(s)-I\). For \(s>0\) and connected \(G\), \(R_G(s)\) is entrywise strictly positive: \(I+sL_G\) is an irreducible nonsingular \(M\)-matrix, or equivalently its inverse has a positive walk expansion. Thus off-diagonal entries of \(C_G(s)\) are strictly positive and positivity is equivalent to
\[
R_G(s)_{vv}\ge\tfrac12\quad\text{for all vertices }v.
\]

**2. Two monotone comparisons.** Write \(K=I+sL_G\), \(H=\operatorname{diag}(1+s d_v)\), and \(X=sH^{-1/2}A_GH^{-1/2}\). The symmetric nonnegative matrix \(X\) has operator norm less than one, and
\[
R_G=H^{-1/2}\sum_{k\ge0}X^kH^{-1/2}.
\]
Fix a vertex \(v\) and lift walks to the universal covering tree \(\widetilde G\). A closed lifted walk is a closed base walk; the converse fails when a base loop lifts to a different terminal sheet. All corresponding walk products are equal and nonnegative, since covered vertices retain the same degrees. Hence, term by term,
\[
R_G(s)_{vv}\ge R_{\widetilde G}(s)_{\tilde v\tilde v}.
\]
The cover is a bipartite tree with the same side-specific degree caps. Embed it as an edge-induced subtree of the infinite \((p,q)\)-biregular tree \(T_{p,q}\) by completing missing branches. Extend its Laplacian to the remaining vertices by isolated zeros. Adding the missing unit edges increases the Laplacian in quadratic-form order; since inversion reverses positive-definite Loewner order,
\[
R_{\widetilde G}(s)_{\tilde v\tilde v}\ge R_{T_{p,q}}(s)_{oo},
\]
where the type of \(o\) matches that of \(v\). Bounded degrees justify these operators and the limiting resolvents on \(\ell^2\). This is a comparison of ordinary graph Laplacians, not normalized random-walk Laplacians.

**3. Exact two-type return resolvents.** Put \(t=1/s>0\). Let \(a\) and \(b\) denote \(s\) times the cavity diagonal resolvents at degree-\(p\) and degree-\(q\) vertices, respectively, after removing their parent links *but retaining the original full degree on the diagonal*. Schur complementation gives
\[
a=\frac1{t+p-(p-1)b},\qquad
b=\frac1{t+q-(q-1)a},\qquad 0<a,b<1.
\]
These are the unique physical cavity values in \((0,1)^2\). Indeed the eliminated quadratic in \(b\) is strictly concave, negative at zero and positive at one, and therefore has exactly one root in \((0,1)\); the associated \(a\) is then unique. The full-tree root returns are
\[
R_p(s)=\frac1{1+sp(1-b)},\qquad
R_q(s)=\frac1{1+sq(1-a)}.
\]
Equivalently, \(R_p/R_q=a/b\), as follows from the Schur complements and the common factor \(1-ab\). As \(p>q\), the cavity maps \(f_d(x)=1/[t+d-(d-1)x]\) are increasing in \(x\) and strictly decreasing in \(d\) for \(x<1\). If \(a\ge b\), then \(a=f_p(b)<f_q(b)\le f_q(a)=b\), a contradiction. Therefore \(a<b\), so \(R_p(s)<R_q(s)\) for all \(s>0\). The degree-\(p\) root alone controls the uniform threshold.

The spectral theorem shows that \(R_p(s)\) decreases continuously and strictly from one as \(s\downarrow0\) to zero as \(s\to\infty\). The limiting value is zero because the connected infinite tree has no nonzero square-summable constant, hence no \(\ell^2\) zero-eigenfunction of its Laplacian. Therefore \(R_p(s)=1/2\) has precisely one positive root.

**4. The quadratic frontier.** At \(R_p(s)=1/2\), the root formula forces \(b=1-t/p\). Substituting in the first cavity equation gives
\[
a=\frac{p}{p+(2p-1)t}.
\]
Substitution in the second cavity equation and cancellation of the harmless factor \(t>0\) gives
\[
P_{p,q}(t)=D_{p,q}+B_{p,q}t-(2p-1)t^2=0.
\]
Since \(D_{p,q}>0\), \(P_{p,q}(0)>0\), \(P_{p,q}(p)=-2p^2<0\), and the leading coefficient is negative, this polynomial has exactly one positive root in \((0,p)\), namely \(t_{p,q}\) above. At that root \(a,b\in(0,1)\) solve both cavity equations, so the root is the physical return threshold. Steps 1–3 establish the nonnegativity bound for every finite graph in the class.

**5. Uniform sharpness and strict improvement.** Let \(B_r\) be the radius-\(r\) finite ball about a degree-\(p\) vertex of \(T_{p,q}\), with its ordinary internal-edge graph Laplacian. The extended ball Laplacians converge strongly to the full-tree Laplacian and are uniformly bounded; hence the root resolvent entries converge to \(R_p(s)\). If \(s>\sigma_{p,q}\), then \(R_p(s)<1/2\), so for all sufficiently large finite \(r\), \((C_{B_r}(s))_{oo}=2R_{B_r}(s)_{oo}-1<0\). Such balls obey both degree caps.

Finally compare \(T_{p,q}\) to the \(p\)-regular tree \(T_{p,p}\). The two-type cavity iteration from zero is monotone in the allowed degree of the second type: replacing degree \(p\) by \(q<p\) strictly increases its cavity value and then strictly increases the degree-\(p\) root return for every \(s>0\). Thus its \(1/2\) crossing is strictly later, so \(\sigma_{p,q}>\sigma_p=(2p-1)/(2p(p-1))\).

## Verification

The standalone, standard-library-only `verify.py` checks 45 asymmetric degree pairs, verifies the root return and strict comparison numerically, computes the negative finite-ball witnesses just above the claimed frontier, checks the elimination identity with exact rational arithmetic for 45 parameter pairs, and checks 223 admissible small bipartite graphs using exact-rational matrix inversion below the theoretical bound. Running `python3 verify.py` on the included file produced:

```
VERIFY_OK tree-root-threshold-tests 45 rational-inverse-graphs 223 exact-elimination-identities 45
```

Finite tests corroborate the formulas; the universal result and uniform sharpness follow from the proof rather than enumeration. The exact root is defined by an algebraic expression, not estimated from finite balls.

## Relationship to prior work

Faragó and Horváth [1] develop discrete maximum-principle and positivity conditions for parabolic time-stepping, including the \(\theta\)-method and Crank–Nicolson on finite-difference and finite-element meshes. Their Theorem 4.2/4.11 and §6 yield matrix conditions and sufficient mesh restrictions, not the stated sharp two-cap graph-family frontier. Chung and Yau [2] study coverings, heat kernels and regular-tree comparisons; their covering walk arguments supply antecedents for step 2, but do not give the two-type Crank–Nicolson cutoff. The general diagonal-resolvent criterion for positivity and the sharp degree-\(p\)-only regular-tree bound are also prior results. The present new statement is the **strict, sharp asymmetric** \((p,q)\) graph-family improvement with its explicit quadratic boundary. Existing two-type tree Green functions [3] are also not claimed as novel.

## Limitations

This classification assumes unit undirected conductances, a known bipartition, integer caps \(p>q\ge2\), and the unnormalized Laplacian. It does not extend by substitution to arbitrary weighted, directed or nonbipartite graphs, higher-order integrators, boundary-killed diffusion, or accuracy claims. The nonnegative guarantee is uniform and sharp as an infimum across finite graphs; no particular finite graph is asserted to attain equality. Priority against every uncatalogued specialized graph-diffusion result has not been independently established.

## References

[1] I. Faragó and R. Horváth, *Discrete Maximum Principle and Adequate Discretizations of Linear Parabolic Problems*, SIAM Journal on Scientific Computing 28(6), 2313–2336 (first online December 21, 2006), https://doi.org/10.1137/050627241 .

[2] F. Chung and S.-T. Yau, *Coverings, Heat Kernels and Spanning Trees*, Electronic Journal of Combinatorics 6 (1999), R12 (public December 12, 1998), https://doi.org/10.37236/1444 .

[3] A. Mondal, S. Parikh, P. Pradhan and R. Sengar, *Holography on Biregular Trees*, arXiv:2507.20886 (first public July 29, 2025), https://arxiv.org/abs/2507.20886 . Used only as related literature on the biregular-tree resolvent, not as evidence for a Crank–Nicolson stability classification.
