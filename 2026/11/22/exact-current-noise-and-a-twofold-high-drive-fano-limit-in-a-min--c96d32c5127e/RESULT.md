# Exact current noise and a twofold high-drive Fano limit in a minimally active constrained exclusion ring

## Finding

Consider the three-particle constrained exclusion process on a periodic seven-site ring. For every rate \(q>0\), use the local moves \(010\to001\) at rate \(q\) and \(001\to010\) at rate \(1\), with all other three-site patterns unchanged. Let \(Q_t\) be the total signed number of moves during \([0,t]\), counting each clockwise move as \(+1\) and each reverse move as \(-1\), summed over all seven bonds. Start from the unique stationary distribution. Define the mean signed current and its long-time variance density by
\[
J(q)=\lim_{t\to\infty}\frac{\mathbb E Q_t}{7t},\qquad
V(q)=\lim_{t\to\infty}\frac{\operatorname{Var}(Q_t)}{7t}.
\]
Put
\[
R(q)=q^3+q^2+q+2,
\]
\[
P(q)=8q^9+30q^8+55q^7+39q^6+33q^5+89q^4+103q^3+55q^2+34q+4.
\]
Then, for every real \(q>0\), the **exact stationary current noise** is
\[
\boxed{V(q)=\frac{2(q+1)P(q)}{7(2q+1)^3R(q)^3}.}
\]
The mean current is
\[
J(q)=\frac{2(q^2-1)}{7(2q+1)R(q)}.
\]
In particular, the noise density is strictly positive, \(V(1)=8/105\), and in the strongly forward-biased limit
\[
\lim_{q\to\infty}q^2 J(q)=\frac17,\qquad
\lim_{q\to\infty}q^2 V(q)=\frac27,\qquad
\boxed{\lim_{q\to\infty}\frac{V(q)}{J(q)}=2.}
\]
The last ratio is defined for the positive-current regime \(q>1\); it concerns signed total-hop counting, not an unqualified single-bond counting convention.

## Assumptions and scope

Sites form \(\mathbb Z/7\mathbb Z\), each site contains zero or one particle, and precisely three particles are present. Each allowed local update is triggered by its own continuous-time exponential clock. The two moves are reverses at the same three-site location. The parameter \(q\) is any strictly positive real. In this below-half-filled sector the finite chain is irreducible and has a unique stationary law. The order of limits is long observation time \(t\to\infty\) first, followed by the strong-bias limit \(q\to\infty\). Time is measured in units of the reverse-hop rate. A variance of the sum of signed hops is being computed, not a site-occupation variance or the number of *all* jumps disregarding their direction.

The seven-site, three-particle system is the first below-half-filled ring accommodating three particles, and is a natural minimal benchmark for the clustering-driven decline of mean transport reported in the motivating literature. The exact mean-current behavior itself is not asserted to be new.

## Proof

Rotation of a configuration preserves both the generator and the counted current, so the tilted process closes exactly on the five cyclic rotation classes. In lexicographic order, choose representatives
\[
0000111,\quad0001011,\quad0001101,\quad0010011,\quad0010101.
\]
All five orbits have seven physical configurations. Define the column generator \(G\), with a transition placed in row destination and column source. Direct application of the two local updates gives
\[
G=\begin{pmatrix}
-1&q&0&0&0\\
1&-q-1&0&q&0\\
0&0&-q-1&1&q\\
0&1&q&-q-2&q\\
0&0&1&1&-2q
\end{pmatrix}.
\]
Its column sums vanish. Its normalized stationary column vector is
\[
\pi=\frac1{R(q)}\begin{pmatrix}
q^3\\q^2\\3q/(2q+1)\\q\\(q+2)/(2q+1)
\end{pmatrix}.
\]
Direct substitution proves \(G\pi=0\), \(\mathbf1^\mathsf T\pi=1\), and positivity for every \(q>0\). These facts also exhibit the unique stationary orbit law.

For each physical update with increment \(d\in\{-1,1\}\) and rate \(r\), form a tilted matrix \(G_s\) by multiplying its destination entry by \(e^{sd}\), while retaining the *untilted* negative exit rate on the diagonal. This includes transitions that return to the same rotation class: they contribute \(r(e^{sd}-1)\) to that class's diagonal tilt. Thus \(G_0=G\). Write \(B=\partial_sG_s|_{s=0}\) and \(C=\partial_s^2G_s|_{s=0}\). The exact matrices, with the same ordering, are
\[
B=\begin{pmatrix}
0&q&0&0&0\\-1&0&0&q&0\\0&0&0&-1&q\\0&-1&q&0&q\\0&0&-1&-1&q-1
\end{pmatrix},\quad
C=\begin{pmatrix}
0&q&0&0&0\\1&0&0&q&0\\0&0&0&1&q\\0&1&q&0&q\\0&0&1&1&q+1
\end{pmatrix}.
\]
For \(q>0\), the Perron eigenvalue \(\lambda(s)\) of this finite tilted generator is analytic around zero. Standard finite-state additive-functional perturbation identities give
\[
\lambda_1=\lambda'(0)=\mathbf1^\mathsf T B\pi,
\]
\[
G u=(\lambda_1 I-B)\pi,\qquad \mathbf1^\mathsf T u=0,
\qquad
\lambda_2=\lambda''(0)=\mathbf1^\mathsf T(C\pi+2Bu).
\]
The normalization specifies a unique solution \(u\) because zero is a simple eigenvalue. Matrix multiplication and rational elimination yield
\[
\lambda_1=\frac{2(q^2-1)}{(2q+1)R(q)},\qquad
\lambda_2=\frac{2(q+1)P(q)}{(2q+1)^3R(q)^3}.
\]
In a stationary finite irreducible Markov additive process these derivatives equal, respectively, \(\lim_{t\to\infty}\mathbb E Q_t/t\) and \(\lim_{t\to\infty}\operatorname{Var}(Q_t)/t\). Dividing by seven proves the displayed theorem. The numerator coefficients of \(P\) are all positive, establishing \(V(q)>0\). Substitution gives \(V(1)=8/105\). Taking the leading polynomial degrees in the two rational functions yields both \(q^{-2}\) coefficients and their ratio \(2\).

The proof is an exact all-parameter calculation; it does not infer an infinite-time claim from finite simulation or finite temporal enumeration. The separate 35-state computation in the verification artifact checks that quotienting by rotation has not lost any counted self-orbit jump.

## Verification

Run `python check.py` with Python 3 and SymPy. The script enumerates all 35 physical states and their signed transitions, independently constructs the five-orbit matrices, verifies the stationary vector, solves the exact symbolic tilted-generator perturbation equations, and algebraically checks both closed rational functions and strong-drive limits. It also independently solves the unreduced 35-state tilted problem at the exact parameter values \(q=1/2\) and \(q=2\). The checker passes these computations. The symbolic identities in the proof, rather than numerical samples, establish the theorem for every \(q>0\).

## Relationship to prior work

Großkinsky, Schütz and Zahra [1] introduced and investigated exactly this local kinetic constraint, its phase separation and clustering, and its faster-is-slower mean current. Their Figure 2 includes exact finite-three-particle **mean** current curves for the seven- and eight-site rings. The mean expression above is therefore supporting normalization, not an independent priority claim. The present object is the second scaled cumulant of the signed current and its twofold high-drive current-noise ratio; no formula or bound for that observable was found in their inspected main text, figures or reference discussion.

Schütz and Zahra [2] study the same constrained dynamics specifically at half filling, where reversible components and area-weighted stationary measures arise. A seven-site ring with three particles is below half filling, is irreducible, and has nonzero mean current for \(q\ne1\); half-filled equilibrium area fluctuations do not imply the stated signed-current noise. Causer, Garrahan and Lamacraft [3] investigate related classical stochastic Fredkin dynamics and trajectory large deviations, prominently activity and metastable sectors; this is important adjacent theory but not identified as the same directed seven-site counted process. A finite-state tilted-generator algorithm is established general mathematics, and is not itself claimed as original.

## Limitations

The exact formula applies only to this seven-site, three-particle constrained ring, with one common forward rate and unit reverse rate. It does not prove a universal noise ratio for larger systems, a thermodynamic-limit phase transition, or convergence of the entire count process to a compound-Poisson law. The number \(2\) refers to the long-time variance-to-mean ratio of the **total signed** hop count at strong forward bias, and does not by itself identify a burst-size distribution. The mean current and the qualitative faster-is-slower effect were established in prior work. The inspected relevant portions of [2] concern half-filled equilibrium area moments, not the below-half-filled signed-current variance; an unindexed equivalent finite-state calculation cannot be categorically excluded. Independent scientific validation remains outstanding.

## References

1. S. Großkinsky, G. Schütz and A. Zahra, *Long-range correlations in a locally constrained exclusion process*, arXiv:2503.12632, first submitted 2025-03-16. https://arxiv.org/abs/2503.12632 ; preprint full text https://arxiv.cnoctave.top/pdf/2503.12632 .
2. G. M. Schütz and A. Zahra, *Mixed Order Phase Transition in a Locally Constrained Exclusion Process*, arXiv:2509.14467, first submitted 2025-09-17; Journal of Statistical Physics 193, 63 (2026). https://arxiv.org/abs/2509.14467 .
3. L. Causer, J. P. Garrahan and A. Lamacraft, *Slow dynamics and large deviations in classical stochastic Fredkin chains*, Physical Review E 106, 014128 (2022), arXiv:2202.06989. https://arxiv.org/abs/2202.06989 .
