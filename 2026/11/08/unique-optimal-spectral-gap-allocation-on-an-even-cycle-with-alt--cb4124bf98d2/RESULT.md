# Unique optimal spectral-gap allocation on an even cycle with alternating edge prices

## Finding

**Theorem.** Fix an integer \(m\ge2\), a budget \(B>0\), and two prices \(c_0,c_1>0\). Number the vertices of the simple cycle \(C_{2m}\) by \(0,1,\ldots,2m-1\) modulo \(2m\); edge \(\{i,i+1\}\) has price \(c_0\) if \(i\) is even and \(c_1\) if \(i\) is odd. Assign an *independent* nonnegative conductance \(w_i\) to each of the \(2m\) edges, with \(\sum_i c_{i\bmod 2}w_i\le B\), and let \(L(w)\) be the unnormalized weighted graph Laplacian. Write

\[
\gamma=\cos(\pi/m),\qquad s=\sin(\pi/m),\qquad D=c_0+c_1+2\gamma\sqrt{c_0c_1}.
\]

Then the **unique** optimizer of \(\lambda_2(L(w))\) over all \(2m\) *independently chosen* conductances is the strictly positive period-two allocation

\[
\boxed{
 w_{2j}=\frac{B}{mD}\left(1+\gamma\sqrt{\frac{c_1}{c_0}}\right),\qquad
 w_{2j+1}=\frac{B}{mD}\left(1+\gamma\sqrt{\frac{c_0}{c_1}}\right),\quad 0\le j<m.
}
\]

Its optimum is

\[
\boxed{\lambda_2^{\max}=\frac{2Bs^2}{mD}.}
\]

For the four-cycle \(m=2\), both parity classes receive exactly the same conductance \(B/[2(c_0+c_1)]\), regardless of unequal prices. For every \(m\ge3\), unequal prices yield unequal optimal conductances; the cheaper parity receives more. With the prices fixed and \(m\to\infty\), the ratio of optimal conductances tends to \(\sqrt{c_1/c_0}\), and the optimal spectral gap obeys

\[
\lambda_2^{\max}\sim\frac{2\pi^2B}{m^3(\sqrt{c_0}+\sqrt{c_1})^2}.
\]

For instance, on \(C_6\) with \((c_0,c_1,B)=(4,1,1)\), the unique optimal conductances are \((w_{\mathrm{even}},w_{\mathrm{odd}})=(5/84,2/21)\) and the optimum is \(1/14\), versus \(1/15\) when all six conductances are equal under the same cost budget.

## Assumptions and scope

The graph is a simple undirected cycle with at least four vertices. Edge rates may be zero, but prices are strictly positive, budget strictly positive, and vertex masses all equal to one. The result maximizes the second-smallest eigenvalue of the *combinatorial* Laplacian, equivalently the exponential \(L^2\)-convergence rate for the continuous-time symmetric diffusion \(\dot x=-L(w)x\). It does **not** optimize discrete-time SLEM, total effective resistance, finite-time mixing, or vertex-weighted Laplacian gaps. The optimization is over all \(2m\) independent rates, not only the period-two subfamily.

## Proof

**1. Reduce to a two-band eigenvalue problem without assuming periodicity of the unknown optimum.** The function \(w\mapsto\lambda_2(L(w))=\min_{x\perp\mathbf 1,\|x\|=1}\sum_iw_i(x_i-x_{i+1})^2\) is concave in \(w\). Rotating rates by two vertices preserves prices and the objective. Averaging all \(m\) two-step rotations preserves feasibility and cannot decrease \(\lambda_2\). Hence an optimum *exists* with \(w_{2j}=a\) and \(w_{2j+1}=b\), although this observation alone does not establish uniqueness among arbitrary rates. If either \(a\) or \(b\) vanishes, the cycle disconnects into \(m\) edges and its spectral gap is zero; thus an optimum has \(a,b>0\) and uses the full budget \(m(c_0a+c_1b)=B\).

For a period-two cycle, the Bloch modes with wave number \(k=2\pi\ell/m\), \(0\le\ell<m\), give the two eigenvalues

\[
 a+b\pm\sqrt{a^2+b^2+2ab\cos k}.
\]

At \(k=0\), the lower branch is zero. Among all nonzero wave numbers, its smallest value occurs at \(k=2\pi/m\) (or its conjugate); consequently

\[
\lambda_2=a+b-\sqrt{(a+b)^2-4ab s^2},\qquad s=\sin(\pi/m).
\tag{1}
\]

For \(m=2\), the same formula reads \(\lambda_2=2\min(a,b)\).

**2. Solve the exact two-rate optimization.** Put \(\lambda=\lambda_2>0\), \(u=a/\lambda\), \(v=b/\lambda\), \(\gamma=\cos(\pi/m)\) and \(s^2=1-\gamma^2\). Squaring (1) gives

\[
4s^2uv-2(u+v)+1=0.
\]

Set \(U=2s^2u-1\) and \(V=2s^2v-1\). Then \(UV=\gamma^2\). Both are nonnegative: indeed \(\lambda=4abs^2/(a+b+\sqrt{(a+b)^2-4abs^2})\le(a+b)s^2\), so \(U+V=2s^2(a+b)/\lambda-2\ge0\); their product is nonnegative. Therefore

\[
\frac{c_0a+c_1b}{\lambda}
=\frac{c_0+c_1+c_0U+c_1V}{2s^2}
\ge\frac{c_0+c_1+2\gamma\sqrt{c_0c_1}}{2s^2}
=\frac{D}{2s^2}.
\tag{2}
\]

For \(m\ge3\), equality in the arithmetic-geometric mean inequality holds only for \(U=\gamma\sqrt{c_1/c_0}\), \(V=\gamma\sqrt{c_0/c_1}\). For \(m=2\), \(\gamma=0\) and positivity of the prices forces \(U=V=0\). In both cases (2), together with the saturated budget, gives the displayed candidate and optimum. Conversely, these positive values satisfy the squared equation, and \(u+v\ge1\) places \(\lambda\) on the lower branch of (1), so they really attain equality. Uniqueness **within** the period-two subfamily follows as well.

**3. Certify a global bound and uniqueness among all independent rates.** Let \(a,b\) be the displayed optimal two rates, and \(\lambda=\lambda_2(L(a,b))\). If \(m\ge3\), set \(k=2\pi/m\), \(R=a+b-\lambda>0\), and

\[
 f_{2j}=e^{ikj},\qquad f_{2j+1}=q e^{ikj},\qquad
 q=\frac{a+b e^{ik}}{R}.
\]

The Bloch equation and (1) imply \(|q|=1\) and \(L(a,b)f=\lambda f\). In particular, \(\sum_i f_i=0\), the two real coordinate vectors of \(f\) lie in \(\mathbf1^\perp\), and \(\sum_i|f_i|^2=2m\). Write \(t=\sqrt{c_0/c_1}\). Direct substitution of the displayed optimal \(a,b\) into the chord lengths gives

\[
 |f_{2j+1}-f_{2j}|^2=\frac{4s^2t^2}{t^2+2\gamma t+1},\qquad
 |f_{2j+2}-f_{2j+1}|^2=\frac{4s^2}{t^2+2\gamma t+1}.
\tag{3}
\]

Thus the squared edge difference divided by its edge price is the *same positive constant* \(\alpha\) for every edge. In the special four-cycle case \(m=2\), take instead \(f=(1,q,-1,-q)\), where \(q=e^{i\phi}\) and \(\tan(\phi/2)=t\), so \(0<\phi<\pi\). This is a \(\lambda\)-eigenvector at the equal-rate optimum, has zero sum, and has squared chord lengths \(4c_0/(c_0+c_1)\) and \(4c_1/(c_0+c_1)\), again with common edge difference divided by edge price \(\alpha\).

For *any* feasible rate vector \(w\), applying the variational characterization to the real and imaginary parts of this fixed complex vector \(f\) gives

\[
\lambda_2(L(w))\sum_i|f_i|^2
\le\sum_i w_i|f_i-f_{i+1}|^2
=\alpha\sum_i c_{i\bmod2}w_i
\le\alpha B.
\tag{4}
\]

At the candidate, equality holds throughout because \(f\) is an eigenvector and the budget is saturated. Hence (4) globally certifies its optimality, without assuming two-periodicity of a competitor.

If another feasible \(w\) attains equality, both real and imaginary parts of \(f\) must lie in the \(\lambda\)-eigenspace of \(L(w)\), since their individual Rayleigh deficits are nonnegative and sum to zero. Thus \((L(w)-L(a,b))f=0\). At each vertex this yields

\[
(w_{i-1}-w_{i-1}^*)(f_i-f_{i-1})+(w_i-w_i^*)(f_i-f_{i+1})=0.
\]

For \(m\ge3\), the phase of \(q\) lies strictly between \(0\) and \(k\); for \(m=2\), \(0<\phi<\pi\). Thus each vertex and its two neighbors map to three distinct points on the unit circle. Two chords from one point to two different points on a circle are real-linearly independent. The last displayed equality therefore forces both adjacent weight differences to vanish. The optimizer is globally unique. Strict positivity of its displayed conductances is immediate.

Finally, the four-cycle exception and the large-\(m\) asymptotics follow by substituting \(\gamma=0\) and by \(s\sim\pi/m\), \(\gamma\to1\), respectively.

## Verification

The standalone script `verify.py`, using only Python's standard library, evaluates 48 rational parameter cases at \(m\in\{2,3\}\), checks the exact budget, band polynomial and normalized dual edge energies, and verifies positive semidefiniteness of \(L-\lambda(I-J/(2m))\) by all 1,872 principal minors. It prints `EXACT_VERIFY_OK parameter_cases=48 principal_minors=1872 dual_energy_checks=48`. These checks are finite examples; the preceding proof supplies every integer \(m\ge2\) and all positive real prices and budgets.

## Relationship to prior work

Göring, Helmberg and Wappler (first publicly posted September 2, 2005) introduced an SDP dual embedding interpretation for unpriced absolute algebraic connectivity, but did not evaluate the two-price cycle family. Sun, Boyd, Xiao and Diaconis (published online November 2, 2006) formulated the *full positive edge-price* continuous-time Markov-process optimization. Their Section 5.3 evaluates cycles for equal prices and shows that optimal cycle embeddings have dimension at most two with arbitrary prices; it explicitly describes the general unequal-price cycle as more complicated. The present result is an evaluated two-price family within their general framework, with a closed form and uniqueness even without assuming period-two conductances. It does not claim the general convex formulation or the basic cycle band spectrum as new. Earlier work on special one-exceptional-price four-cycles and on alternating vertex-mass stochastic kernels uses different parameter and objective families and does not logically imply this all-even-cycle classification.

## Limitations

The theorem requires exactly alternating edge prices and a linear global budget, not arbitrary independent edge prices or per-edge upper bounds. The cost asymmetry concerns transition rates of a *continuous-time* symmetric process, not a discrete-time stochastic kernel with specified holding probabilities. The novelty assessment is based on the inspected full-text sources, indexed literature and relevant accessible records; equivalent unindexed or unpublished results may exist. Independent external mathematical validation has not been performed.

## References

1. F. Göring, C. Helmberg, M. Wappler, *Embedded in the Shadow of the Separator*, preprint publicly posted 2005-09-02, https://optimization-online.org/2005/09/1202/ ; full text https://www-user.tu-chemnitz.de/~helmberg/GoeHelWap_R07_SIOPT.pdf .
2. J. Sun, S. Boyd, L. Xiao, P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, https://doi.org/10.1137/S0036144504443821 ; open author PDF https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf .
3. A. Ghosh, S. Boyd, *Upper Bounds on Algebraic Connectivity via Convex Optimization*, Linear Algebra and its Applications 418 (2006), 693–707, https://stanford.edu/~boyd/papers/eigbounds_laplacian.html .
