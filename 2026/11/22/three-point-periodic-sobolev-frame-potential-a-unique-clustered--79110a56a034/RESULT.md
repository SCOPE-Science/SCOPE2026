# Three-point periodic Sobolev frame potential: a unique clustered optimum

## Finding
Let \(H\) be the real, mean-zero, periodic Sobolev Hilbert space on the circle of circumference one, with norm \(\|f\|_H^2=\int_0^1|f'(t)|^2\,dt\). For three distinct sites \(X=\{x_1,x_2,x_3\}\subset\mathbb T\), let \(k_x\in H\) be the representer of point evaluation, \(f(x)=\langle f,k_x\rangle_H\). Define the three-site frame potential

\[
\mathcal F(X)=\sum_{i,j=1}^3|\langle k_{x_i},k_{x_j}\rangle_H|^2.
\]

Then, over all triples of distinct sites,

\[
\boxed{\min_X\mathcal F(X)=\frac5{216}.}
\]

Equality holds **if and only if**, up to circle rotation and reflection, \(X=\{0,1/6,1/3\}\). Its consecutive cyclic gaps are \((1/6,1/6,2/3)\). The equally spaced design has \(\mathcal F=11/432>5/216\): the minimizing design halves the sum of the three squared off-diagonal correlations. The normalized unit-vector frame potential is \(10/3\) at the optimum, versus \(11/3\) at equal spacing.

In addition, the full Gram spectrum at the optimizer is

\[
\boxed{\left\{\frac19,\frac{5+\sqrt3}{72},\frac{5-\sqrt3}{72}\right\}.}
\]

## Assumptions and scope
The circle is \(\mathbb T=\mathbb R/\mathbb Z\) with normalized arclength measure. Functions are real and periodic with mean zero and square-integrable weak derivative. The sites are three *distinct* points, each sampled once with equal, unweighted evaluation energy. The frame potential is the squared Hilbert--Schmidt norm of the \(3\times3\) evaluation Gram matrix, not its operator norm. Kernel vectors are not normalized unless expressly indicated. Reflections and rotations are the only geometric identifications used.

## Proof
**Kernel normalization.** The unique mean-zero periodic Green kernel for \(-d^2/dt^2\) is

\[
K(t)=\frac12\bigl(\{t\}^2-\{t\}+\tfrac16\bigr),\qquad K(0)=\frac1{12}.
\]

Indeed, in distributions \(-K''=\delta_0-1\), so periodic integration by parts gives \(\int_0^1f'(u)\,\partial_uK(u-x)\,du=f(x)\) whenever \(\int_0^1f=0\). Thus \(k_x(u)=K(u-x)\) and \(\langle k_x,k_y\rangle_H=K(x-y)\). Also \(K(t)=K(1-t)\) for \(0\le t\le1\).

**Reduction to a constrained quartic.** Order the sites cyclically and denote the positive consecutive gaps by \(a,b,c\), so \(a+b+c=1\). The three unordered pair correlations are \(K(a),K(b),K(c)\). With

\[
w(t)=K(t)^2=\frac14(t^2-t+\tfrac16)^2,
\]

we have exactly

\[
\mathcal F(X)=\frac1{48}+2\,[w(a)+w(b)+w(c)].\tag{1}
\]

**Global critical-point analysis.** Since the expression is continuous on the closed simplex, its minimum exists. On its boundary at least one gap is zero; then \(w(0)=1/144\), so the sum of the three \(w\)'s is at least \(1/144>1/864\), the value at \((a,b,c)=(1/6,1/6,2/3)\). Thus every minimizer lies in the positive simplex.

At an interior critical point, the Lagrange equations require \(w'(a)=w'(b)=w'(c)\), where

\[
w'(t)=t^3-\frac32t^2+\frac23t-\frac1{12}.
\]

For distinct \(u,v\), the equality \(w'(u)=w'(v)\) implies

\[
u^2+uv+v^2-\frac32(u+v)+\frac23=0.\tag{2}
\]

If \(a,b,c\) were all distinct, subtracting the equations (2) for \((a,b)\) and \((a,c)\) would give \((b-c)(a+b+c-3/2)=0\), contradicting \(a+b+c=1\). Hence at least two gaps coincide. Permute them as \(a=b=t\) and \(c=1-2t\). The stationarity condition factors **exactly** as

\[
w'(t)-w'(1-2t)=\frac{(3t-1)^2(6t-1)}6=0.
\]

The only candidate shapes are therefore the equilateral gaps \((1/3,1/3,1/3)\) and the permutations of \((1/6,1/6,2/3)\). Their off-diagonal half-potentials are, respectively,

\[
3w(1/3)=\frac1{432},\qquad 2w(1/6)+w(2/3)=\frac1{864}.
\]

The latter is strictly smaller, and the boundary is strictly worse. Equation (1) proves the sharp value and *all* equality cases.

**Spectrum and normalized correlation gain.** At \(X=\{0,1/6,1/3\}\) the Gram matrix is

\[
G=\begin{pmatrix}
1/12&1/72&-1/36\\
1/72&1/12&1/72\\
-1/36&1/72&1/12
\end{pmatrix}.
\]

The antisymmetric vector \((1,0,-1)\) has eigenvalue \(1/9\). On the symmetric two-dimensional subspace, the eigenvalues are \((5\pm\sqrt3)/72\). Therefore \(\operatorname{tr}G^2=5/216\). All evaluation representers have squared norm \(1/12\), so after unit normalization the frame potential is \(144\mathcal F\); the three unordered squared normalized correlations have sum \(1/6\) at the optimizer and \(1/3\) at equal spacing.

## Verification
The accompanying `VERIFY.py` runs using Python 3 standard libraries only. It checks the kernel and exact rational constants, the optimizer's Gram invariants, the factored stationary equation, and all strictly positive rational three-gap partitions with denominators from 3 through 144. This finite enumeration is corroborative: the analytic stationary-point and boundary arguments above prove the theorem for every real configuration. The exact checker reports 487452 rational assertions.

Run `python3 VERIFY.py` from a directory containing the standalone file.

## Relationship to prior work
The classical frame-potential principle of Benedetto and Fickus and its later treatments by Carrizo--Heineken, Ambrus, and Bodmann--Haas motivate this objective. Ambrus's theorem describes unrestricted unit vectors: three unit vectors in a sufficiently large Hilbert space can be orthogonal, with potential 3. The normalized evaluation vectors here are restricted to a fixed translation orbit of a periodic Sobolev Green kernel; their sharp minimum is instead \(10/3\). The unrestricted theorem does not determine the orbit-constrained minimum or its sites. Bodmann--Haas primarily study Gram manifolds of finite-dimensional Parseval frames, not the non-idempotent three-point Green matrices here. Aravkin--Bell--Burke--Pillonetto explain the relevance of RKHS Gram matrices to sampling and estimation, but do not classify this frame potential's node geometry. A historically unindexed equivalent of the quartic three-gap minimization remains possible.

## Limitations
The exact classification is for three equal-weight point-evaluation vectors in the mean-zero periodic first-order Sobolev space, not for arbitrary numbers of sites, unequal weights, distinct Sobolev exponents, or noise-aware posterior covariance criteria. Minimizing the frame potential does **not** assert minimizing the largest Gram eigenvalue, its smallest eigenvalue, or the condition number. The result is an analytic mathematical statement with self-review only; no independent audit has been performed.

## References
1. I. Carrizo and S. Heineken, *Critical Pairs of Sequences of a Mixed Frame Potential*, arXiv:1210.5488, first public version 2012-10-19. https://arxiv.org/abs/1210.5488
2. A. Y. Aravkin, B. M. Bell, J. V. Burke and G. Pillonetto, *The connection between Bayesian estimation of a Gaussian random field and RKHS*, arXiv:1301.5288, first public version 2013-01-22. https://arxiv.org/abs/1301.5288
3. G. Ambrus, *A short proof for the characterisation of tight frames*, arXiv:1403.7382, first public version 2014-03-28. https://arxiv.org/abs/1403.7382
4. B. G. Bodmann and J. Haas, *Frame potentials and the geometry of frames*, arXiv:1407.1663, first public version 2014-07-07. https://arxiv.org/abs/1407.1663
5. J. J. Benedetto and M. Fickus, *Finite Normalized Tight Frames*, Advances in Computational Mathematics 18 (2003), 357--385, DOI:10.1023/A:1021323312367.
