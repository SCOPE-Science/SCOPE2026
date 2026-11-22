# Sharp squared-SLEM rigidity and equality cases for fastest mixing on paths

## Finding

For every integer \(n\ge3\), let \(P\) be any real symmetric, entrywise nonnegative, stochastic \(n\times n\) matrix whose entries vanish whenever \(|i-j|>1\). Let \(q_i=P_{i,i+1}=P_{i+1,i}\) for \(1\le i<n\), and set \(q_0=q_n=0\). Write \(P_*\) for the particular matrix with all off-diagonal path probabilities \(1/2\), and put

\[
\theta=\frac\pi n,\qquad c=\cos\theta,\qquad
s(P)=\left\|P-\frac{\mathbf1\mathbf1^{\mathsf T}}n\right\|_2.
\]

Define the normalized cosine mode and weighted edge deviations by

\[
y_j=\sqrt{\frac2n}\cos((j-\tfrac12)\theta),\quad
u_i=(q_i-\tfrac12)(y_i-y_{i+1})\quad (1\le i<n),\quad u_0=u_n=0.
\]

Then the following **sharp global stability inequality** holds without any irreducibility or aperiodicity restriction:

\[
\boxed{\quad s(P)^2\ \ge\ c^2+\sum_{j=1}^{n}(u_j-u_{j-1})^2.\quad}
\]

Equality holds **if and only if** the edge transition probabilities alternate:

\[
\boxed{\quad q_i=\tfrac12+(-1)^{i-1}t\quad(1\le i<n),\qquad -\tfrac12\le t\le\tfrac12.\quad}
\]

Every such alternating matrix has the exact contraction factor

\[
\boxed{\quad s(P(t))^2=c^2+4t^2\sin^2\theta.\quad}
\]

Consequently \(P_*\) is the **unique** fastest symmetric stochastic walk on the path. In addition, for each edge \(1\le i<n\),

\[
\boxed{\quad |q_i-\tfrac12|\le
\frac{\sqrt{i(n-i)}}{\sqrt8\sin(i\theta)\sin(\theta/2)}
\sqrt{s(P)^2-c^2}.\quad}
\]

If \(s(P)\le c+\varepsilon\), the final square root can be replaced by \(\sqrt{2c\varepsilon+\varepsilon^2}\). The square-root dependence on the excess contraction factor is optimal for every fixed \(n\ge3\), because the alternating family has

\[
s(P(t))-c=\frac{2\sin^2\theta}{c}t^2+O(t^4)
\qquad(t\to0).
\]

The coefficient \(1\) of the squared deviation term in the global inequality is also sharp, since every alternating matrix attains equality.

## Assumptions and scope

The matrix need only be symmetric, stochastic, nonnegative, and tridiagonal. Thus \(q_i\ge0\) and \(q_{i-1}+q_i\le1\) for all \(1\le i\le n\), and its diagonal entries are \(P_{ii}=1-q_{i-1}-q_i\). Disconnected or periodic boundary matrices are included. \(s(P)\) is the full second-largest eigenvalue modulus, equivalently the operator norm on the orthogonal complement of the constant vector. The norm and all quadratic forms use standard Euclidean normalization. The result is for the uniform invariant distribution and a path with unrestricted nonnegative edge probabilities; it does not assert an analogous inequality for arbitrary stationary masses, directed kernels, or non-path graphs.

## Proof

**1. A strict dual-slack identity.** The entries of \(y\) sum to zero and \(\|y\|_2=1\). The standard path walk \(P_*\) satisfies \(P_*y=cy\). Define

\[
z_j=\frac1n\left(c+\frac{\cos((2j-1)\theta)}c\right).
\]

For adjacent vertices, the elementary product-to-sum identity gives \((z_j+z_{j+1})/2=y_jy_{j+1}\). Also \(\sum_jz_j=c\). For diagonal entries,

\[
y_j^2-z_j=\frac{1-c}{nc}
\left(c-\cos((2j-1)\theta)\right)=:h_j.
\]

Since \(0<c<1\), one has \(h_1=h_n=0\) and \(h_j>0\) for every \(2\le j\le n-1\). Expanding \(y^{\mathsf T}Py\) and using symmetry and stochasticity therefore gives the **exact identity**

\[
y^{\mathsf T}Py-c=\sum_{j=2}^{n-1}h_jP_{jj}\ge0.
\]

This is the precise strict-slack consequence of the classical path dual certificate; it is valid for all feasible \(P\). Equality is equivalent to \(P_{jj}=0\) for all interior vertices, or \(q_{j-1}+q_j=1\) throughout the interior. Hence equality here holds exactly for the alternating family \(q_i=\frac12+(-1)^{i-1}t\), with \(-\frac12\le t\le\frac12\).

**2. The squared-SLEM stability inequality.** Because \(y\perp\mathbf1\) and \(P\) is symmetric and stochastic, all spectral values of \(P\) on \(\mathbf1^\perp\) lie in \([-s(P),s(P)]\). In particular \(y^{\mathsf T}P^2y\le s(P)^2\). Using the strict-slack identity and \(P_*y=cy\),

\[
\begin{aligned}
\|(P-P_*)y\|_2^2
&=\|Py-cy\|_2^2\\
&=y^{\mathsf T}P^2y-2c\,y^{\mathsf T}Py+c^2\\
&\le s(P)^2-c^2.
\end{aligned}
\]

Set \(\delta_i=q_i-1/2\). Since \(P-P_*=-\sum_{i=1}^{n-1}\delta_i(e_i-e_{i+1})(e_i-e_{i+1})^{\mathsf T}\), its product with \(y\) has components \(((P-P_*)y)_j=u_{j-1}-u_j\), where \(u_i=\delta_i(y_i-y_{i+1})\). Thus the squared norm in the last display is precisely \(\sum_j(u_j-u_{j-1})^2\).

If the global inequality is an equality, equality must hold in the strict-slack identity, since \(c>0\). Hence all interior diagonals vanish and the edge probabilities alternate. Conversely, step 3 shows that every alternating walk achieves equality.

**3. Exact spectrum on the equality family.** Let \(v_0=n^{-1/2}\mathbf1\), and for \(1\le r<n\) put

\[
v_r(j)=\sqrt{\frac2n}\cos((j-\tfrac12)r\theta).
\]

These vectors form an orthonormal cosine basis and \(P_*v_r=\cos(r\theta)v_r\). Direct use of the path tridiagonal entries, including both endpoints, shows for \(1\le r<n\) that

\[
(P(t)-P_*)v_r=-2t\sin(r\theta)v_{n-r}.
\]

Thus each pair \((v_r,v_{n-r})\), with \(1\le r<n/2\), spans an invariant subspace whose matrix is

\[
\begin{pmatrix}
\cos(r\theta)&-2t\sin(r\theta)\\
-2t\sin(r\theta)&-\cos(r\theta)
\end{pmatrix}.
\]

Its eigenvalues are \(\pm\sqrt{\cos^2(r\theta)+4t^2\sin^2(r\theta)}\). When \(n\) is even, the unpaired mode \(v_{n/2}\) has eigenvalue \(-2t\); the constant mode has eigenvalue \(1\). Since \(|2t|\le1\), the largest nonconstant absolute eigenvalue comes from \(r=1\), and is \(\sqrt{c^2+4t^2\sin^2\theta}\). Also \((P(t)-P_*)y=-2t\sin\theta\,v_{n-1}\), so the squared deviation is \(4t^2\sin^2\theta\). This proves equality for the entire stated family, including the boundary weights.

**4. Inverse near-optimality.** All edge-mode differences are strictly positive:

\[
y_i-y_{i+1}=\sqrt{\frac8n}\sin(i\theta)\sin(\theta/2).
\]

Let \(R=(P-P_*)y\). Its components sum to zero, while \(\sum_{j=1}^iR_j=-u_i\). Applying Cauchy–Schwarz to the centered indicator of the first \(i\) vertices gives

\[
|u_i|\le \sqrt{\frac{i(n-i)}n}\,\|R\|_2.
\]

Substituting the expression for \(y_i-y_{i+1}\) and step 2 yields the displayed coordinate estimate. For \(s(P)\le c+\varepsilon\), use \(s(P)^2-c^2\le2c\varepsilon+\varepsilon^2\). Finally, the exact alternating spectral formula has a nonzero quadratic coefficient at \(t=0\); hence no global \(O(\varepsilon)\) edge-deviation bound is possible even when \(n\) is fixed.

## Verification

The accompanying standalone `verify_path_stability.py` evaluates 4,899 stochastic path matrices: 21 alternating parameters for each size \(3\le n\le20\), 250 additional random feasible kernels at each size, and the two-vertex boundary family. It independently checks stochasticity, the strict-slack identity, spectral normalization, the squared-SLEM inequality, equality on alternating kernels, and every coordinate bound. This finite numerical test is not a proof of the all-size theorem; all universal steps are justified above by exact trigonometric and spectral identities. It uses NumPy and a fixed pseudorandom seed.

## Relationship to prior work

Boyd, Diaconis, and Xiao formulate symmetric fastest mixing as a semidefinite program (2004). Boyd, Diaconis, Sun, and Xiao explicitly prove that transition probability \(1/2\) on each edge optimizes SLEM for a path (2006), using a cosine dual certificate. Fill and Kahn (2011 preprint) establish much stronger comparisons of the *distributions* from a specified starting vertex across times, but do not give the present global squared-SLEM deviation inequality. The finding here neither rediscovers the known optimal chain nor claims the general dual-certificate method as new: it is the all-feasible **sharp quadratic inverse estimate**, equality-case characterization, and quantitative edge recovery, with optimal square-root excess-rate scaling. The published literature may contain a differently phrased equivalent stability result; absence in the inspected sources does not prove global priority.

## Limitations

The result is an exact, self-contained inequality for symmetric path kernels with uniform equilibrium, not for nonreversible walks or arbitrary graphs. The explicit edge bound is generally conservative at fixed graph size, although the squared quadratic form's coefficient is attained exactly and the excess-rate exponent cannot be improved. The closest full-text primary papers were inspected at the relevant propositions, not every paper in the surrounding literature. Independent verification has not been performed.

## References

1. S. Boyd, P. Diaconis, and L. Xiao, “Fastest Mixing Markov Chain on a Graph,” *SIAM Review* 46 (2004), 667–689, DOI: [10.1137/S0036144503423264](https://doi.org/10.1137/S0036144503423264). First published electronically 2004-10-29, as stated in the original article.
2. S. Boyd, P. Diaconis, J. Sun, and L. Xiao, “Fastest Mixing Markov Chain on a Path,” *American Mathematical Monthly* 113 (2006), 70–74, [author manuscript](https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/ConvergeRates/DiaconisFastest.pdf), DOI: [10.1080/00029890.2006.11920281](https://doi.org/10.1080/00029890.2006.11920281).
3. J. A. Fill and J. Kahn, “Comparison inequalities and fastest-mixing Markov chains,” preprint posted 2011-09-28, [arXiv:1109.6075](https://arxiv.org/abs/1109.6075), especially Section 4.
