# Exact fastest-mixing weights on odd squared cycles and a fourfold spectral-gap gain

## Finding

For every odd integer \(n\ge7\), let \(G=C_n^2\) be the undirected graph on \(\mathbb Z/n\mathbb Z\) in which the allowed distinct-vertex moves are \(\pm1\) and \(\pm2\). Among **all** real symmetric entrywise-nonnegative row-stochastic transition matrices supported on the edges and loops of \(G\), the minimum second-largest eigenvalue modulus (SLEM) is attained by the explicitly specified circulant transition matrix below. Among circulant feasible matrices, that optimum is unique. Uniqueness of arbitrary nonsymmetric-in-space feasible matrices is **not asserted**.

Put
\[
 c_+=\cos(2\pi/n),\qquad c_-=-\cos(\pi/n),\qquad
 j=\lfloor(n+1)/4\rfloor,\qquad d=\cos(2\pi j/n),
\]
\[
 R=-2(c_++c_-)=2\bigl(\cos(\pi/n)-\cos(2\pi/n)\bigr),\qquad
 F(z)=2R(1-z)+4(1-z^2),
\]
\[
 E=F(c_+)=F(c_-),\qquad M=F(d).
\]
Then \(0<E<M\), and the exact optimal per-neighbor probabilities and optimal SLEM are
\[
 \boxed{a_*=\frac{2R}{E+M},\qquad b_*=\frac{2}{E+M},\qquad
 \mu_* =\frac{M-E}{M+E}.}
\]
The transitions to each of the two \(\pm1\) neighbors have probability \(a_*\), the transitions to each of the two \(\pm2\) neighbors have probability \(b_*\), and the remaining holding probability is
\[
 s_*=1-2(a_*+b_*)>0.
\]
Exactly three distinct Fourier-frequency types alternate at the optimum: the modes \(k=1\) and \(k=(n-1)/2\) have multiplier \(+\mu_*\), and \(k=j\) has multiplier \(-\mu_*\).

As \(n\to\infty\) through odd integers,
\[
 a_* =\frac{3\pi^2}{2n^2}+O(n^{-3}),\qquad
 b_* =\frac12-\frac{21\pi^2}{8n^2}+O(n^{-3}),
\]
\[
 s_* =\frac{9\pi^2}{4n^2}+O(n^{-3}),\qquad
 \mu_*=1-\frac{8\pi^2}{n^2}+O(n^{-3}).
\]
For the best symmetric walk restricted to **only** the \(\pm2\) moves and loops, write \(\mu_{(2)}\) for its SLEM. Then
\[
 \mu_{(2)}=\frac{\cos(2\pi/n)+\cos(\pi/n)}
 {2-\cos(2\pi/n)+\cos(\pi/n)},\qquad
 \boxed{\lim_{\substack{n\to\infty\\ n\text{ odd}}}\frac{1-\mu_*}{1-\mu_{(2)}}=4.}
\]
Thus a vanishing \(O(n^{-2})\) first-neighbor probability increases the optimal asymptotic spectral gap by a factor of four relative to using the distance-two cycle alone.

## Assumptions and scope

The objective is the SLEM \(\mu(P)=\|P-J\|_2\), with \(J=\mathbf1\mathbf1^{\mathsf T}/n\); all matrices \(P\) are real, symmetric, nonnegative, stochastic, and have zero off-diagonal entries outside distance-one and distance-two edges. A self-loop is permitted at every vertex. All edge probabilities may initially vary **independently** with the vertex and edge. The result proves the globally optimal value and existence of a circulant optimizer, plus uniqueness within the circulant subclass, not uniqueness of the unrestricted matrix. It does not optimize nonreversible kernels, total-variation mixing time at a specified finite horizon, or a prescribed positive lower bound on every transition.

## Proof

**1. Reduction from arbitrary edge probabilities.** Since symmetric stochastic matrices commute with \(J\), \(\mu(P)=\|P-J\|_2\). This norm is convex and invariant under permutations of vertices. Averaging a feasible matrix under the rotations and reflections of the cycle preserves symmetry, entrywise nonnegativity, row sums and support, and cannot increase \(\mu\). The averaged matrix has probabilities \(a\ge0\) on each \(\pm1\) edge, \(b\ge0\) on each \(\pm2\) edge and \(1-2a-2b\ge0\) on the diagonal. Therefore the full unrestricted optimum equals the optimum over these \((a,b)\).

**2. Fourier spectrum and a concave quadratic.** With \(c_k=\cos(2\pi k/n)\), \(1\le k\le(n-1)/2\), the nonconstant Fourier multipliers are
\[
 \lambda_k(a,b)=1-2a(1-c_k)-2b(1-\cos(4\pi k/n))
 =1-2a(1-c_k)-4b(1-c_k^2).
\]
The \(c_k\) decrease strictly from \(c_+\) to \(c_-\). Since \(R=-2(c_++c_-) >0\), the candidate ratio \(a=Rb\) gives \(\lambda_k=1-bF(c_k)\). The polynomial \(F\) is strictly concave, with vertex \(c_0=-(R/4)=(c_++c_-)/2\), and \(F(c_+)=F(c_-)=E\). Hence \(F(c_k)\ge E\) for every \(k\). Its largest sampled value occurs at the \(c_k\) nearest \(c_0\).

**3. Identifying the middle contact without numerical enumeration.** Put \(x=\pi/(2n)\), so \(c_0=-\sin(3x)\sin(x)\). For \(n\equiv1\pmod4\), \(j=(n-1)/4\), \(c_j=\sin x\), while \(c_{j+1}=-\sin(3x)\); the midpoint of those values is \(-\sin x\cos(2x)\), which is at most \(c_0\) because \(\sin(3x)\le\cos(2x)\) for \(n\ge7\). The preceding midpoint is positive, so \(c_j\) is nearest. For \(n\equiv3\pmod4\), \(j=(n+1)/4\), \(c_j=-\sin x\), and its next right neighbor is \(-\sin(5x)\). Their midpoint is \(-\sin(3x)\cos(2x)\), at most \(c_0\) since \(\sin x\le\cos(2x)\); the preceding midpoint is positive. Again \(c_j\) is nearest. The strict containment \(c_-<d<c_+\) and strict concavity imply \(M>E>0\).

**4. Equioscillation and feasibility.** Choose \(b_*=2/(E+M)\) and \(a_*=Rb_*\). The two endpoint modes obey \(\lambda_1=\lambda_{(n-1)/2}=1-b_*E=\mu_*\); the middle mode obeys \(\lambda_j=1-b_*M=-\mu_*\). Every other multiplier lies between these extremes, proving \(\mu(P_*)=\mu_*\).

It remains to verify the nonnegative diagonal, rather than assume it. Set \(C=\cos(\pi/n)\) and note \(R=2(1-C)(1+2C)\), \(E=8(1-C)(1+C)^2\), and \(d^2=(1-C)/2\). Direct expansion yields
\[
 E+M-4(1+R)=4(1-C)\bigl[\tfrac12+2C+2C^2-(1+2C)d\bigr].
\]
Since \(|d|=\sin(\pi/(2n))<1/2\) and \(C>0\), the bracket exceeds \(C+2C^2>0\). Thus \(2(a_*+b_*)=4(1+R)/(E+M)<1\). In particular all five transitions are strictly positive.

**5. A global lower bound and circulant uniqueness.** Let \((a',b')\) be any other feasible circulant choice. The difference of multipliers factors as
\[
 \lambda(c;a',b')-\lambda(c;a_*,b_*)
 =(1-c)\bigl[-2(a'-a_*)-4(b'-b_*)(1+c)\bigr].
\]
The bracket is affine in \(c\). If the alternative had SLEM strictly less than \(\mu_*\), its multiplier differences would be strictly negative at both \(c_-\) and \(c_+\), but strictly positive at the interior \(d\), impossible for an affine function. With SLEM at most \(\mu_*\), the same inequalities are nonstrict. An affine function nonpositive at both endpoints cannot be nonnegative at their strict interior point unless it vanishes at all three. The two coefficients therefore agree exactly. This proves the unique circulant optimum and, using step 1, the unrestricted global optimum value.

**6. Sharp asymptotics and fourfold gain.** Write \(t=\pi/n\). Taylor expansion gives \(R=3t^2+O(t^4)\), \(E=16t^2+O(t^4)\), and \(M=4+5t^2+O(t^3)\) (the sign of \(d=\pm\sin(t/2)\) affects only order \(t^3\)). Consequently \(b_*=1/2-21t^2/8+O(t^3)\), \(a_*=3t^2/2+O(t^3)\), \(s_*=9t^2/4+O(t^3)\), and \(\mu_*=1-8t^2+O(t^3)\). Since \(n\) is odd, steps \(\pm2\) alone induce an ordinary \(n\)-cycle by relabeling vertices. Its one-parameter optimum, obtained by balancing the largest positive and negative Fourier multipliers, is exactly the displayed \(\mu_{(2)}=1-2t^2+O(t^4)\). Taking the ratio of spectral gaps yields four.

## Verification

The accompanying standalone `verify.py` reconstructs the spectral expressions independently, solves the finite circulant minimax problem with a linear program for 48 odd orders from 7 to 101, checks full stochastic matrices for orders up to 31, tests independently assigned noncirculant edge probabilities on five small orders, and compares the asymptotics at three larger orders. It passed 1,651 assertions in the reviewed package. These finite checks do **not** prove the infinite-family result; the proof above supplies that conclusion.

## Relationship to prior work

Boyd, Diaconis and Xiao establish the general symmetric fastest-mixing Markov chain formulation as a convex semidefinite program. Boyd, Diaconis, Parrilo and Xiao prove that graph automorphism averaging preserves optimality and derive an exact one-orbit solution on simple cycles, along with Cartesian-product and distance-transitive examples. Those results provide the general framework and the one-jump comparison. The distinct contribution here is the two-edge-orbit **square of every odd cycle**, its sharp three-mode contacts, explicit finite-size weights, strict positive holding probability, and fourfold asymptotic gap advantage. Their edge-transitive theorem does not supply this two-orbit solution by direct substitution. Published research could nevertheless contain an equivalent specialization in different notation; this possibility has not been eliminated by a search.

## Limitations

This is an exact SLEM theorem, not a bound for every notion of mixing time. The unconstrained full-matrix optimizer need not be unique; only its existence and the unique circulant optimizer are proved. The result excludes even orders and higher jump lengths. An accessible primary source treating general symmetry and the ordinary cycle has been inspected, but a separately identified thesis chapter on cycle mixing could not be accessed in full; unindexed equivalent results are a residual priority for independent literature review. Scientific review is not an independent certification.

## References

1. S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI: 10.1137/S0036144503423264. Full text: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/SIREV042326-1.pdf.
2. S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM J. Optimization 20 (2009), 792–819, DOI: 10.1137/070689413, first arXiv submission 2007-09-06, arXiv:0709.0955. Full text: https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf. Relevant material: Theorem 2.1, Section 3.1 and equations (3.3)–(3.4).
