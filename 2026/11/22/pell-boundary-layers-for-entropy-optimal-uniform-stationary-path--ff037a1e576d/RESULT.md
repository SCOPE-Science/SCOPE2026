# Pell boundary layers for entropy-optimal uniform-stationary path walks

## Finding

For each integer \(n\ge2\), let \(\mathcal P_n\) be the convex set of symmetric stochastic \(n\times n\) matrices supported on the diagonal and the two immediate off-diagonals. Thus a chain in \(\mathcal P_n\) is a reversible birth–death walk on the \(n\)-vertex path with uniform stationary law and permitted holding. Its stationary entropy rate is
\[
H(P)=-\frac1n\sum_{i,j=1}^n P_{ij}\log P_{ij},\qquad 0\log0:=0.
\]
There is one entropy maximizer \(P^{(n)}\), with strictly positive permitted entries. Let \(h_0=5\), \(h_1=19\), and
\[
h_{k+2}=4h_{k+1}-h_k,\qquad
 t_k=\frac{h_k-5(-1)^k}{h_k+(-1)^k}\quad(k\ge1).
\]
For each *fixed* \(k\), its diagonal and edge entries satisfy the exact limits
\[
\lim_{n\to\infty}P^{(n)}_{kk}=\frac{t_k^2}{3},\qquad
\lim_{n\to\infty}P^{(n)}_{k,k+1}=\frac{t_kt_{k+1}}3.
\]
The corresponding entries at the reflected right endpoint have the same limits. In particular,
\[
\lim_{n\to\infty}(P^{(n)}_{11},P^{(n)}_{12},P^{(n)}_{23},P^{(n)}_{34})
=\left(\frac{16}{27},\frac{11}{27},\frac5{16},\frac{41}{121}\right).
\]
The edge corrections alternate around the bulk value \(1/3\), are nonzero at every fixed endpoint distance, and have the sharp far-from-boundary expansion
\[
\frac{t_kt_{k+1}}3-\frac13=(-1)^{k+1}\frac{2(1-\vartheta)}{A}\vartheta^k+O(\vartheta^{2k}),
\qquad A=\frac{5+3\sqrt3}{2},\quad\vartheta=2-\sqrt3.
\] Writing \(H_n=H(P^{(n)})\), the maximum entropy has the precise surface correction
\[
\boxed{\lim_{n\to\infty}n(\log3-H_n)=C:=4\sum_{k=1}^{\infty}\log t_k
=0.873382433026828\ldots>0.}
\]
The series converges absolutely. In fact, with \(\vartheta=2-\sqrt3\),
\[
n(\log3-H_n)=C+O(n\vartheta^{n/2}).
\]
These assertions concern *entropy-rate* optimality with an imposed uniform stationary distribution; they do not claim optimal spectral mixing rates or the unconstrained maximal-entropy walk.

## Assumptions and scope

The path has unit adjacency support: transitions are allowed only from a site to itself or either neighboring site. Self-loops at all sites are permitted, and no lower bound on probabilities is imposed in defining \(\mathcal P_n\). All logarithms are natural. Each matrix is symmetric and row stochastic, so the stationary law is uniform. The finite maximizers exist for every \(n\ge2\); limiting entry claims hold for fixed distance \(k\) from an endpoint, not for a growing \(k\) without further qualification.

## Proof

**1. Unique strictly positive maximizer and scaling equations.** Set \(x_i=P_{i,i+1}=P_{i+1,i}\), with \(x_0=x_n=0\), and \(d_i=P_{ii}=1-x_{i-1}-x_i\). The feasible polytope is compact, and \(H\) is strictly concave in its permitted matrix entries; hence its maximizer is unique. A strictly positive feasible matrix exists, for example by taking every edge probability small and every holding probability positive. If a permitted entry were zero at a maximizer, interpolating toward such an interior matrix would give a positive infinite one-sided entropy derivative. Thus all permitted entries are positive at the maximum.

Differentiating the entropy with respect to an interior edge variable yields
\[
n\frac{\partial H}{\partial x_i}=\log\frac{d_id_{i+1}}{x_i^2}.
\]
Consequently \(x_i^2=d_id_{i+1}\). Put \(v_i=\sqrt{d_i}>0\), together with \(v_0=v_{n+1}=0\). Then the unique maximizer is determined by
\[
v_i(v_{i-1}+v_i+v_{i+1})=1\quad(1\le i\le n),
\qquad P^{(n)}_{ii}=v_i^2,\quad P^{(n)}_{i,i+1}=v_iv_{i+1}.
\tag{1}
\]
Uniqueness follows already from strict concavity. Since \(v_i\le1\) and at most two neighbors are present, \(1\le v_i(v_i+2)\); therefore every \(v_i\) lies in the uniform interval \([\sqrt2-1,1]\). At the maximizer the product form and stochastic row sums also give
\[
H_n=-\frac2n\sum_{i=1}^n\log v_i.
\tag{2}
\]

**2. Explicit positive half-line solution.** The Pell-type recurrence has the closed form
\[
h_k=\frac{5+3\sqrt3}{2}(2+\sqrt3)^k+
\frac{5-3\sqrt3}{2}(2-\sqrt3)^k.
\]
It is strictly increasing with \(h_k\ge5(2+\sqrt3)^k\) and satisfies the invariant
\[
h_{k-1}^2-4h_{k-1}h_k+h_k^2=6\quad(k\ge1).
\tag{3}
\]
In particular \(t_k>0\), and
\[
t_k-1=\frac{-6(-1)^k}{h_k+(-1)^k}=O(\vartheta^k),\qquad\vartheta=2-\sqrt3.
\tag{4}
\]
For \(k\ge2\), set \(a=h_{k-1}\), \(b=h_k\), \(c=4b-a\), and \(s=(-1)^k\). Substituting
\[
t_{k-1}=\frac{a+5s}{a-s},\quad t_k=\frac{b-5s}{b+s},\quad t_{k+1}=\frac{c+5s}{c-s}
\]
into \(t_{k-1}+t_k+t_{k+1}-3/t_k\), clearing denominators, and using \(a^2-4ab+b^2=6\) and \(s^2=1\) gives zero identically. At the left boundary \(t_1=4/3\), \(t_2=11/12\), and \(t_1(t_1+t_2)=3\). Thus
\[
v_k^{(\infty)}=\frac{t_k}{\sqrt3}\quad(k\ge1),\qquad v_0^{(\infty)}=0,
\]
is an exact positive half-line solution of (1), approaching the bulk constant \(1/\sqrt3\). Direct multiplication gives \(t_1^2/3=16/27\), \(t_1t_2/3=11/27\), \(t_2t_3/3=5/16\), and \(t_3t_4/3=41/121\). More generally, for odd \(k\), cross-multiplication gives \(t_kt_{k+1}>1\) exactly when \(h_{k+1}-h_k>4\), which holds; for even \(k\), the same calculation gives \(t_kt_{k+1}<1\) because \(h_{k+1}>h_k\). Hence every limiting edge transition lies strictly above \(1/3\) for odd \(k\) and strictly below it for even \(k\). Expanding the closed form of \(h_k\) in (4) gives \(t_k-1=(-1)^{k+1}(6/A)\vartheta^k+O(\vartheta^{2k})\), and multiplying consecutive terms yields the sharp edge expansion in the finding.

**3. Both finite-path boundary layers converge to the half-line solution.** Write \(y_i=\log v_i\) and
\[
F_i(y)=e^{2y_i}+\sum_{j:\,|j-i|=1,\;1\le j\le n}e^{y_i+y_j}-1.
\]
The positive solution of (1) is characterized by \(F(y)=0\). Define the two-end comparison vector
\[
\widetilde y_i=-\frac12\log3+\log t_i+\log t_{n+1-i},\qquad1\le i\le n.
\tag{5}
\]
By (4), the right correction to the left half-line profile is bounded by a constant times \(\vartheta^{\lfloor n/2\rfloor-1}\) throughout the left half of the path, and symmetrically for the other half. Each individual half-line profile exactly solves the relevant local equations, including its own terminal boundary equation. Since exponentials have uniformly bounded derivatives over the bounded range of these profiles, it follows that
\[
\|F(\widetilde y)\|_\infty=O(\vartheta^{n/2}).
\tag{6}
\]
For clarity, the Jacobian has
\[
(DF(y))_{ii}=2e^{2y_i}+\sum_{j\sim i}e^{y_i+y_j},\qquad
(DF(y))_{ij}=e^{y_i+y_j}\quad(j\sim i),
\]
with other entries zero. Its diagonal dominance margin is exactly \(2e^{2y_i}\). The actual positive solution obeys \(v_i\ge\sqrt2-1\), while every entry of the comparison vector has \(e^{\widetilde y_i}=t_it_{n+1-i}/\sqrt3\ge(11/12)^2/\sqrt3>\sqrt2-1\). Thus every Jacobian on the line segment joining \(y\) and \(\widetilde y\), and their average Jacobian, has diagonal dominance margin at least \(2(\sqrt2-1)^2\). The maximum-row argument for a strictly diagonally dominant matrix gives the inverse \(\ell^\infty\)-norm bound \([2(\sqrt2-1)^2]^{-1}\). Applying the fundamental theorem of calculus to \(F(y)-F(\widetilde y)\) therefore gives
\[
\max_i|y_i-\widetilde y_i|=O(\vartheta^{n/2}).
\tag{7}
\]
For fixed \(k\), the term \(\log t_{n+1-k}\) in (5) tends to zero, proving the asserted left and reflected-right entry limits. Equation (4) supplies the alternating geometric boundary profile.

**4. Exact entropy surface constant.** Sum (5) and use (7), the exponential tail in (4), and (2):
\[
\sum_{i=1}^n\log v_i=-\frac n2\log3+2\sum_{k=1}^\infty\log t_k+O(n\vartheta^{n/2}).
\]
Hence
\[
n(\log3-H_n)=4\sum_{k=1}^\infty\log t_k+O(n\vartheta^{n/2}).
\]
Absolute convergence follows from (4). Positivity does not rely on numerical evaluation: for each odd \(k\), \(t_kt_{k+1}>1\), since direct cross multiplication reduces this to \(h_{k+1}-h_k>4\). The latter holds by the increasing recurrence from \(h_1=19\). Every pair in the infinite product therefore exceeds one; so the limiting logarithmic sum is positive. Evaluating the rapidly convergent explicit series gives the stated decimal.

## Verification

The included `verify.py` uses exact rational arithmetic to check the Pell recurrence and the first boundary entries, and symbolic polynomial reduction to verify the central half-line identity under invariant (3). It also solves the finite-dimensional positive scaling equations for several path sizes and checks stochasticity, reflection, the entropy identity, and convergence numerically. Run `python verify.py` with Python 3, NumPy, SciPy, and SymPy installed. The scripts are supplementary finite checks; the infinite-dimensional limits and global finite-dimensional optimization are proved above.

## Relationship to prior work

The entropy-rate variational principle for reversible chains and its general stationary equations appear in Van der Straeten (2009) and Chliamovitch–Dupuis–Chopard (2015). The former treats globally positive transition matrices and spin models; the latter develops two- and three-state inference and numerical procedures. The special contribution here is an explicit *uniform-stationary, sparse nearest-neighbor* path boundary solution, including its Pell recurrence and the limiting surface entropy term. Diaconis–Wood (2012) studies typical random doubly stochastic tridiagonal matrices rather than this entropy optimizer. Boyd–Diaconis–Sun–Xiao (2006) minimizes spectral mixing modulus on paths, a different criterion leading to different conductances. General stationary-law and Luce-score optimization methods (including later literature) may offer alternate derivations of the finite scaling equations, but the explicit endpoint constants and all-size asymptotics require the additional half-line analysis given here.

## Limitations

Only symmetric, uniformly stationary, nearest-neighbor *discrete-time* chains with holding are optimized. The result does not apply to nonuniform stationary masses, directed walks, forbidden loops, or arbitrary sparse graphs without new arguments. The geometric error bound is sufficient to prove the surface term, not asserted to be the sharp finite-size correction. Publication priority remains subject to fuller access to historical work on tridiagonal doubly stochastic matrices and possible earlier equivalent matrix-scaling boundary solutions.

## References

1. E. Van der Straeten, *Maximum entropy estimation of transition probabilities of reversible Markov chains*, arXiv:0910.3829, first public 20 October 2009. https://arxiv.org/abs/0910.3829
2. G. Chliamovitch, A. Dupuis, B. Chopard, *Maximum Entropy Rate Reconstruction of Markov Dynamics*, Entropy **17** (2015), 3738–3751. https://doi.org/10.3390/e17063738
3. P. Diaconis and P. M. Wood, *Random doubly stochastic tridiagonal matrices*, Random Structures & Algorithms **42** (2013), 403–437, publicly available journal page from 3 August 2012. https://doi.org/10.1002/rsa.20452
4. S. Boyd, P. Diaconis, J. Sun, L. Xiao, *Fastest Mixing Markov Chain on a Path*, American Mathematical Monthly **113** (2006), 70–74. https://www.web.stanford.edu/~boyd/papers/fmmc_path.html
5. P. Bolzern, P. Colaneri, G. De Nicolao, *Maximum entropy reconstruction of discrete-time Markov chains under partial information*, arXiv:2611.02982 (2026); comparison based on accessible abstract. https://arxiv.org/abs/2611.02982
