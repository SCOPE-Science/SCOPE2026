# A unique outer-to-center cut migration in four-site weighted heat approximation

## Finding

On a four-vertex path with consecutive positive conductances \((a,b,a)\), the worst discontinuity for finite-time graph-heat approximation changes location exactly once when the central link is weaker than the two equal outer links. More precisely, for \(a,b,t>0\) and the counting-\(\ell^1\) norm, define
\[
 V(f)=\sum_{i=1}^{3}|f_{i+1}-f_i|,\qquad
 H_t=\exp(-tL_{a,b}),\qquad
 K_{a,b}(t)=\sup_{V(f)>0}\frac{\|f-H_tf\|_1}{V(f)}.
\]
Let \(r=b/a\), \(u=at\), \(d=\sqrt{1+r^2}\), and \(\lambda_\pm=1+r\pm d\). Then the exact, attained sharp constant is
\[
 K_{a,b}(t)=\max\{C_o(r,u),C_m(r,u)\},
\]
where
\[
 \begin{aligned}
 C_o(r,u)&=2-\frac{1+e^{-2u}}2
 -\frac{(1+r/d)e^{-\lambda_-u}+(1-r/d)e^{-\lambda_+u}}2,\\
 C_m(r,u)&=2-(1+1/d)e^{-\lambda_-u}-(1-1/d)e^{-\lambda_+u}.
 \end{aligned}
\]
Here \(C_o\) is the error of either one-vertex end cut, and \(C_m\) is the error of the two-versus-two central cut, normalized by their single unit jump.

If \(r\ge1\), \(C_m(r,u)>C_o(r,u)\) for every \(u>0\). If \(0<r<1\), a unique \(u_*(r)>0\) solves \(C_m(r,u_*)=C_o(r,u_*)\), with
\[
 C_o>C_m\quad(0<u<u_*),\qquad C_m>C_o\quad(u>u_*).
\]
Before the crossover, only an outer cut can realize the sharp norm; after it, only the middle cut does. At the crossover all three single-edge steps are extremal. At every positive time, **all** nonconstant equality signals are constant-plus-nonzero-multiple of a single step across one maximizing edge: sums of two nonzero steps are never equality cases. The transition has the asymptotics
\[
 u_*(r)\sim\sqrt{\frac{6(1-r)}r}\quad(r\uparrow1),
 \qquad r u_*(r)\longrightarrow\log3\quad(r\downarrow0).
\]

## Assumptions and scope

The vertices \(1,2,3,4\) form a path with edge conductances \((a,b,a)\). The Laplacian acts by \((Lf)_i=\sum_{j\sim i}c_{ij}(f_i-f_j)\), with no vertex-mass normalization. The heat matrix is symmetric, strictly positive and doubly stochastic for every \(t>0\). The error uses the **counting** norm \(\|g\|_1=\sum_{i=1}^4|g_i|\) rather than stationary-probability-normalized \(\ell^1\); variation uses unweighted jumps, not conductance-weighted jumps. A nonconstant extremizer has \(V(f)>0\). There are no claims about larger or asymmetrically weighted paths.

## Proof

**Step 1: exact reduction to cuts.** For \(j=1,2,3\), let \(s^{(j)}_i=\mathbf1_{i>j}\). Every real vector has the exact representation \(f=f_1\mathbf1+\sum_{j=1}^3d_js^{(j)}\), where \(d_j=f_{j+1}-f_j\) and \(V(f)=\sum_j|d_j|\). Because \(H_t\mathbf1=\mathbf1\), the triangle inequality gives
\[
 \|f-H_tf\|_1\le\sum_j|d_j|\|(I-H_t)s^{(j)}\|_1\le
 \left(\max_j\|(I-H_t)s^{(j)}\|_1\right)V(f).
\]
For any strictly positive symmetric doubly stochastic matrix \(H\), a cut \(S\) obeys \(\|\mathbf1_S-H\mathbf1_S\|_1=2\sum_{i\in S,k\notin S}H_{ik}\). Thus a maximizing cut attains the global bound, and reflection makes the outer two cut coefficients equal. Moreover \((I-H)s^{(j)}\) is **strictly negative** on \(i\le j\), and **strictly positive** on \(i>j\). For any pair \(j<k\), coefficients of equal sign create opposite-signed terms at a coordinate with \(j<i\le k\), while coefficients of opposite sign create opposite-signed terms at a coordinate with \(i\le j\). Thus a vector with at least two nonzero jumps has a strict coordinatewise triangle inequality somewhere, proving the stated complete equality classification.

**Step 2: the two exact branches.** Scale time by \(u=at\) and put \(r=b/a\). Mirror symmetry splits the generator into the even block \(\bigl(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\bigr)\) and the odd block
\[
 A_r=\begin{pmatrix}1&-1\\-1&1+2r\end{pmatrix}.
\]
The odd eigenvalues are \(\lambda_\pm=1+r\pm\sqrt{1+r^2}\); the even eigenvalues are \(0,2\). The \((1,1)\)-entry of \(e^{-uA_r}\) is \(\bigl[(1+r/d)e^{-\lambda_-u}+(1-r/d)e^{-\lambda_+u}\bigr]/2\), and \((1,1)e^{-uA_r}(1,1)^{\mathsf T}=(1+1/d)e^{-\lambda_-u}+(1-1/d)e^{-\lambda_+u}\). The end-cut leakage is \(2(1-(H_t)_{11})\); the middle-cut leakage is \(2-(1,1)e^{-uA_r}(1,1)^{\mathsf T}\). These equal the two displayed formulas.

**Step 3: strictly one crossover.** Set \(\Delta_r(u)=C_m(r,u)-C_o(r,u)\). Elementary algebra or the four-by-four resolvent yields
\[
 \mathcal L\{\Delta_r\}(s)=
 \frac{2\bigl[(r-1)s(s+2)+r\bigr]}
 {s(s+2)\bigl(s^2+2(1+r)s+2r\bigr)},\qquad s>0.
\]
Define the positive kernels
\[
 g_r(u)=\frac{e^{-\lambda_-u}-e^{-\lambda_+u}}{2d}
 =e^{-(1+r)u}\frac{\sinh(du)}d,
 \qquad q(u)=\frac{1-e^{-2u}}2,
 \qquad h_r=q*g_r.
\]
Inverting the Laplace transform gives the **positive-convolution identity**
\[
 \Delta_r(u)=2\bigl[(r-1)g_r(u)+rh_r(u)\bigr].
\]
If \(r\ge1\), positivity of \(g_r,h_r\) gives \(\Delta_r(u)>0\) for every positive \(u\). If \(0<r<1\), write
\[
 \frac{\Delta_r(u)}{2g_r(u)}=r-1+rR_r(u),\qquad
 R_r(u)=\frac{h_r(u)}{g_r(u)}
 =\int_0^u q(v)\frac{g_r(u-v)}{g_r(u)}\,dv.
\]
The logarithm \(\ell(u)=\log g_r(u)\) has strictly negative second derivative \(\ell''(u)=-d^2/\sinh^2(du)\). Therefore, for each fixed \(0<v<u\), \(\partial_u\log[g_r(u-v)/g_r(u)]=\ell'(u-v)-\ell'(u)>0\). The integral's positive integrand and expanding domain prove \(R_r\) strictly increasing. At zero \(R_r(u)\sim u^2/6\); at infinity, \(h_r(u)\to1/(4r)>0\) while \(g_r(u)\to0\), so \(R_r(u)\to\infty\). Hence the equation \(R_r(u)=(1-r)/r\) has exactly one positive solution, with the claimed signs.

**Step 4: limiting thresholds.** The small-time expansion \(R_r(u)=u^2/6+O(u^3)\), uniform for \(r\) near one, gives \(u_*(r)\sim\sqrt{6(1-r)/r}\) as \(r\uparrow1\). For \(r\downarrow0\) and fixed \(x>0\), the odd eigenvalues satisfy \(\lambda_-=r+O(r^2)\), \(\lambda_+=2+O(r)\); consequently \(g_r(x/r)\to e^{-x}/2\) and \(rh_r(x/r)\to(1-e^{-x})/4\). Thus \(rR_r(x/r)\to(e^x-1)/2\). Strict monotonicity of \(R_r\) pins the root at \(r u_*(r)\to\log3\).

## Verification

A standalone reproducibility script is embedded as `verify_weighted_path.py`, requiring Python 3, NumPy and SciPy. It compares the analytical cut coefficients against **independently computed** matrix exponentials for 200 randomly selected positive ratios and times, tests 4,000 real-input variation inequalities, and checks crossover signs and both asymptotic regimes. All tests passed in the saved-run execution. The infinite-time and all-parameter statements follow from the proof, not numerical sampling.

## Relationship to prior work

Chafaï and Joulin (first public 2010-11-10) developed birth–death gradient intertwining and sharp Lipschitz/Wasserstein semigroup bounds; those are distinct from the counting-\(\ell^1\) identity-defect norm relative to graph-edge variation. Castro and Grünbaum (published 2013-03-02) developed spectral representations of birth–death transition probabilities but not this explicit extremal cut migration. A published four-vertex weighted-path theorem treats the sharp **Lipschitz norm of the semigroup itself**, on a different asymmetric conductance cone. Its norm is not \(\|I-H_t\|_{BV\to\ell^1}\), and its parameter cone excludes the present symmetric weak-middle-link regime. The ordinary unweighted-path BV approximation theorem gives only the equal-conductance case \(r=1\), with no migration. Comparisons are at the level of asserted norms and hypotheses, not merely paper titles.

## Limitations

Only a four-vertex path with two equal outer conductances is classified. The norm is counting \(\ell^1\), the input seminorm is unweighted adjacent variation, and the heat generator is the unnormalized combinatorial weighted Laplacian. We do not classify asymmetrically weighted paths or higher node counts, or claim historical-priority certification outside the inspected sources.

## References

1. D. Chafaï and A. Joulin, *Intertwining and commutation relations for birth-death processes*, arXiv:1011.2331, first public 2010-11-10, https://arxiv.org/abs/1011.2331 (2013 Bernoulli version inspected at https://arxiv.org/pdf/1011.2331).
2. M. M. Castro and F. A. Grünbaum, *On a Seminal Paper by Karlin and McGregor*, SIGMA 9 (2013), 020, published 2013-03-02, https://sigma-journal.com/2013/020/sigma13-020.pdf.
3. *A unique heat-gradient migration and two transient amplification peaks on a weighted four-vertex path*, public mathematical finding dated 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-unique-heat-gradient-migration-and-two-transient-amplification--ecbe5ad031f6.
