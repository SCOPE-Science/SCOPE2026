# Sharp signed radial Schur norms on the two-hub complete split graph

## Finding
For every integer \(n\ge2\) and every real \(-1\le t\le1\), let \(G_n=K_2\vee\overline{K_n}=K_{1,1,n}\) be the graph consisting of two adjacent hubs, each adjacent to all \(n\) mutually nonadjacent leaves. Its graph distance takes the values \(0,1,2\). Define the real symmetric kernel
\[
M_{n,t}(i,j)=\begin{cases}1&i=j,\\t&d_{G_n}(i,j)=1,\\0&d_{G_n}(i,j)=2,\end{cases}
\]
and the entrywise Schur map \(S_{n,t}:B(\mathbb C^{n+2})\to B(\mathbb C^{n+2})\), \(S_{n,t}(X)=M_{n,t}\circ X\). Equip both spaces with the spectral operator norm, and denote the completely bounded amplification norm by \(\|S_{n,t}\|_{\mathrm{cb}}\).

Set
\[
a_t=\frac{1+t}{2},\qquad b_n=\frac1n,\qquad \kappa_{n,t}=t^2-a_tb_n,\qquad q_{n,t}=a_t+b_n+2|t|.
\]
Then the exact norm, including both signs of the edge weight, is
\[
\boxed{\|S_{n,t}\|=\|S_{n,t}\|_{\mathrm{cb}}=1+\frac{2\max\{0,\kappa_{n,t}\}}{q_{n,t}}.}
\]
The multiplier is contractive if and only if its kernel is positive semidefinite, equivalently if and only if
\[
t_-\le t\le t_+,\qquad t_\pm=\frac{1\pm\sqrt{1+8n}}{4n}.
\]
For \(\kappa_{n,t}>0\), an explicit norming rank-one probability vector has squared coordinate magnitudes
\[
p_1=p_2=\frac{s_*}{2},\qquad p_{2+j}=\frac{1-s_*}{n}\ (1\le j\le n),\qquad
s_*=\frac{b_n+|t|}{q_{n,t}}.
\]
An associated norming input of operator norm one is the spectral sign of \(\operatorname{diag}(\sqrt{p_i})M_{n,t}\operatorname{diag}(\sqrt{p_i})\), with sign \(+1\) on its zero eigenspace.

The positive and negative unit weights are not equivalent:
\[
\|S_{n,1}\|=\frac{5n-1}{3n+1},\qquad \|S_{n,-1}\|=\frac{4n+1}{2n+1},\qquad \|S_{n,-1}\|>\|S_{n,1}\|.
\]
For the countably infinite graph with the same two hubs and infinitely many leaves, the corresponding normal Schur multiplier on \(B(\ell^2)\) has exact ordinary and completely bounded norms
\[
\boxed{\|S_{\infty,t}\|=\|S_{\infty,t}\|_{\mathrm{cb}}=1+\frac{4t^2}{1+t+4|t|}},\quad -1\le t\le1.
\]
It is contractive precisely at \(t=0\). In particular, the infinite limiting norms for \(t=1\) and \(t=-1\) are \(5/3\) and \(2\), respectively.

## Assumptions and scope
All edges have the same real amplitude \(t\), the diagonal amplitude is one, and every distance-two entry is deleted. The graph has two distinct adjacent singleton hub classes and a nonempty independent leaf class of size at least two. The finite conclusion concerns the complex matrix spectral norm, not a Schatten-four norm; complete boundedness means the supremum over every finite matrix amplification. The infinite conclusion concerns the bounded normal extension obtained by consistent finite corners. The theorem makes no assertion about complex edge weights or \(|t|>1\).

## Proof
**1. Self-adjoint Schur-norm duality.** For any finite real symmetric matrix \(M\), the Schur multiplier norm equals its completely bounded norm. The self-adjoint Schur norm characterization [1, Theorem 2.2] gives
\[
\|S_M\|=\min_{Q=Q^*,\ Q\pm M\succeq0}\ \max_i Q_{ii}.
\]
Dualizing the convex minimum over the probability simplex gives the equivalent formula
\[
\|S_M\|=\max_{p_i\ge0,\ \sum_i p_i=1}\operatorname{tr}\left|D_pMD_p\right|,
\qquad D_p=\operatorname{diag}(\sqrt{p_i}). \tag{1}
\]
For clarity, with positive \(p_i\), the inner minimization of \(\sum_i p_iQ_{ii}\) under \(Q\pm M\succeq0\) is \(\operatorname{tr}|D_pMD_p|\): congruence reduces it to minimizing \(\operatorname{tr}R\) under \(R\pm D_pMD_p\succeq0\). The choice \(R=|D_pMD_p|\) attains the minimum, and testing against the spectral sign proves the lower bound. Boundary vectors follow by continuity; convex minimax applies after restricting \(Q\) to a sufficiently large compact feasible sublevel set. The inner value is an infimum of affine functions of \(p\), so it is concave in \(p\).

**2. Symmetry and spectral reduction.** Averaging the concave objective in (1) over permutations of the leaves and exchange of the hubs does not decrease its value. Thus take \(p_1=p_2=s/2\) and \(p_{2+j}=(1-s)/n\), with \(0\le s\le1\). Write \(w=1-s\), \(a=a_t\), \(b=b_n\). In an orthonormal basis separating the hub antisymmetric vector, the leaf-contrast space, and the remaining hub-symmetric/leaf-constant two-plane, the Hermitian matrix \(D_pM_{n,t}D_p\) has eigenvalue \(s(1-t)/2\), eigenvalue \(w/n\) with multiplicity \(n-1\), and the block
\[
H(s)=\begin{pmatrix}as&t\sqrt{sw}\\t\sqrt{sw}&bw\end{pmatrix}.
\]
For \(-1\le t\le1\), the first two types are nonnegative. If \(\kappa=t^2-ab\le0\), then \(H(s)\succeq0\) at every \(s\), and the trace norm equals the trace, namely one. If \(\kappa>0\), the block is indefinite at \(0<s<1\), and its trace norm is \(\sqrt{(as-bw)^2+4t^2sw}\). Since the sum of the original diagonal eigenvalues is one,
\[
\operatorname{tr}|D_pM_{n,t}D_p|=1+\sqrt{(as-bw)^2+4t^2sw}-(as+bw).\tag{2}
\]

**3. Sharp scalar maximum, including equality.** For \(\kappa>0\), define \(q=a+b+2|t|\), \(c=2\kappa/q\), and \(s_*=(b+|t|)/q\in(0,1)\). The following exact identity holds for every \(s\in[0,1]\):
\[
\big(as+b(1-s)+c\big)^2-\big((as-b(1-s))^2+4t^2s(1-s)\big)
=4\kappa(s-s_*)^2.\tag{3}
\]
Both factors inside the comparison are nonnegative. Thus (3) gives \(\sqrt{(as-bw)^2+4t^2sw}\le as+bw+c\), with equality exactly at \(s=s_*\). Equation (2) consequently has maximum \(1+c\), proving the formula. Taking a vector \(v=(\sqrt{p_i})\), the spectral sign \(U\) of \(D_pMD_p\) satisfies \(\|U\|=1\) and \(\langle S_M(U)v,v\rangle=\operatorname{tr}|D_pMD_p|\), giving an actual norming matrix, not merely an upper bound.

**4. Positivity transition.** The symbol \(M_{n,t}\) itself has eigenvalues \(1\) on the \(n-1\) leaf contrasts and \(1-t\) on the antisymmetric hub line. Its remaining block is \(\begin{psmallmatrix}1+t&t\sqrt{2n}\\t\sqrt{2n}&1\end{psmallmatrix}\). In the parameter range, positivity is therefore equivalent to \(1+t-2nt^2\ge0\). Solving this quadratic gives the two asserted asymmetric thresholds. Substitution of \(t=\pm1\) yields the two distinct rational endpoint norms.

**5. Infinite-leaf limit.** Every finite coordinate compression involving the hubs and \(m\) leaves has norm bounded by the formula at \(m\), and these values increase to \(1+4t^2/(1+t+4|t|)\). The supremum of consistent finite compressions controls the operator and every matrix amplification on \(B(\ell^2)\). Conversely, those finite compressions embed in the infinite graph and approach the displayed limit. This proves both norms and their contractivity condition.

## Verification
The standalone Python 3 script `check.py` checks identity (3), parameter boundaries and endpoint simplifications with exact rational arithmetic over a systematic grid. It separately implements a Jacobi eigensolver and checks the stated trace norm against matrix spectra at explicit candidate maximizers, and against many nonsymmetric randomly sampled probability vectors. The script passed 22,110 supplementary assertions when executed for this package. The universal proof is Steps 1–5, not the finite checker. To reproduce, run `python check.py` with Python 3.10 or later; no third-party packages are required.

## Relationship to prior work
The October 11, 2026 work of González-Pérez, Parcet, Pérez García and Wang [2] concerns radial Schur multipliers on **trees** at intermediate Schatten exponents; a graph containing triangles and its sharp spectral-operator endpoint are not covered by its hypotheses. Christensen's self-adjoint Schur norm theorem [1] supplies the general variational framework used in Step 1, but gives no explicit split-graph phase diagram. Davidson and Donsig [3] establish transitive-symmetry Schur norm formulas, while \(K_{1,1,n}\) is nonvertex-transitive for \(n\ge2\). Existing exact radius-one star and weighted bipartite formulas involve bipartite hosts and therefore do not imply the signed triangular phase transition. Idempotent-only results such as Levene [4] could overlap the endpoint \(t=1\), which is not claimed as independently new. The all-parameter signed norm formula and infinite two-hub law are the claims of interest.

## Limitations
The real attenuation interval \([-1,1]\) is essential to the presented spectral decomposition because both elementary eigenvalue branches are nonnegative there. Complex phases, amplitudes outside this interval, and general multipartite size vectors are not classified. The finite-corner argument establishes a specific normal multiplier in the infinite case, not a classification of arbitrary infinite graph multipliers. Priority is assessed relative to the cited and searched literature, not independently certified; earlier equivalent weighted two-hub formulas under other terminology cannot be excluded absolutely.

## References
[1] E. Christensen, *The Schur multiplier norm and its dual norm*, arXiv:2505.24670, first posted 2025-05-30, https://arxiv.org/abs/2505.24670.

[2] A. González-Pérez, J. Parcet, J. Pérez García, S. Wang, *Radial Schur multipliers on trees and the failure of Fourier-Schur transference*, arXiv:2610.15881, first posted 2026-10-11, https://arxiv.org/abs/2610.15881.

[3] K. R. Davidson and A. P. Donsig, *Norms of Schur Multipliers*, arXiv:math/0506073, https://arxiv.org/abs/math/0506073.

[4] R. H. Levene, *Norms of idempotent Schur multipliers*, arXiv:1302.4849, https://arxiv.org/abs/1302.4849.

[5] *Sharp Schur-projection constants for looped complete bipartite graphs*, public technical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-schur-projection-constants-for-looped-complete-bipartite-g--3c44b45bcba2.

[6] *Exact endpoint Schur norms of radius-one balls on stars of arbitrary degree*, public technical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-endpoint-schur-norms-of-radius-one-balls-on-stars-of-arbit--708bab8a17cc.
