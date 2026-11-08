# Exact bounded-rank logical collision asymptotics for random monadic structures

## Finding
For each integer \(r\ge1\), put \(M=2^r\). Consider two independent structures on the same \(n\)-element labeled set, each with \(r\) named unary predicates, every predicate value at every element chosen independently with probability one-half. Let \(C_{M,n,k}\) be the probability that the structures satisfy the same first-order sentences of quantifier rank at most \(k\), in the language of equality and these unary predicates.

For each fixed integer \(k\ge1\), set
\[
F_k(x,y)=\sum_{j=0}^{k-1}\frac{(xy)^j}{(j!)^2}+
\left(e^x-\sum_{j=0}^{k-1}\frac{x^j}{j!}\right)
\left(e^y-\sum_{j=0}^{k-1}\frac{y^j}{j!}\right).
\]
For every \(M,n,k\), the **exact** collision probability is
\[
C_{M,n,k}=\frac{(n!)^2}{M^{2n}}[x^ny^n]F_k(x,y)^M. \tag{1}
\]
Fix any \(\alpha>0\), and let \(M=2^r\to\infty\) with positive integers \(n=n_M\) such that \(\alpha_M=n/M\to\alpha\). For \(t>0\), define the probability distribution on nonnegative integer pairs
\[
\pi_{k,t}(a,b)=\frac{t^{a+b}}{a!b! F_k(t,t)}\,
\mathbf1_{\{a=b<k\ \text{or}\ a,b\ge k\}}.
\]
Let \(t_M\) be the unique positive solution of
\[
\frac{t_M\partial_x F_k(t_M,t_M)}{F_k(t_M,t_M)}=\alpha_M,
\]
and let \(\Sigma_{k,t_M}\) be the \(2\times2\) covariance matrix of \(\pi_{k,t_M}\). Put
\[
I_k(\beta)=2\beta-2\beta\log(\beta/t)-\log F_k(t,t),\qquad
\frac{t\partial_xF_k(t,t)}{F_k(t,t)}=\beta.
\]
Then \(\det\Sigma_{k,t_M}>0\) and
\[
\boxed{\displaystyle C_{M,n,k}=(1+o(1))\,
\frac{\alpha_M}{\sqrt{\det\Sigma_{k,t_M}}}\,
\exp\bigl(-M I_k(\alpha_M)\bigr).} \tag{2}
\]
The relative error in (2) tends to zero for each fixed \(k\) and \(\alpha>0\) (equivalently it is locally uniform when \(\alpha_M\) stays in a fixed compact subset of \((0,\infty)\)).

For \(k=1\), letting \(S(n,j)\) denote the Stirling number of the second kind, (1) is also the finite sum
\[
C_{M,n,1}=M^{-2n}\sum_{j=0}^{\min(M,n)}\binom Mj (j!S(n,j))^2.
\]
In particular, at the **critical occupancy density** \(n=\lfloor M\log2\rfloor\),
\[
\boxed{\displaystyle C_{M,n,1}\sim
\frac{2^{-M}}{\sqrt{1-(\log2)^2}}}\qquad(M=2^r\to\infty). \tag{3}
\]
This specifies both exponential decay and its exact non-unit constant. Under independent Poissonization of the two sample sizes with respective means \(\beta M\), the analogous probability has the exact value \(\exp\{-M(2\beta-\log F_k(\beta,\beta))\}\). For rank one, the fixed-size exponential rate is strictly larger than its Poissonized counterpart for every \(\beta>0\) except \(\beta=\log2\), at which they coincide.

## Assumptions and scope
The language is **pure monadic first-order logic with equality**, without constants, functions, order, or extra quantifiers. There are \(r\) *named* unary predicates and \(M=2^r\) Boolean one-point types. The two structures have deterministic common size \(n\), independent predicate assignments, and are compared by sentences rather than pointwise agreement on their labeled domains. The integer \(k\) is held fixed in the asymptotic; the result does not assert uniformity for growing \(k\), or for vanishing/diverging \(n/M\). The empty-structure case \(n=0\) is covered by (1), but asymptotic (2) assumes \(\alpha>0\).

## Proof
**1. Logical reduction.** For each Boolean type \(s\in\{0,1\}^r\), let \(N_s\) and \(N'_s\) be the counts of elements of that type in the two structures. The standard monadic Ehrenfeucht–Fraïssé theorem with equality gives
\[
\mathcal A\equiv_k\mathcal B\quad\Longleftrightarrow\quad
\min(N_s,k)=\min(N'_s,k)\ \text{for every }s.
\]
Indeed a discrepancy below the threshold is witnessed by a sentence asserting the exact number of elements of type \(s\) (quantifier rank at most \(k\)); conversely, a duplicator may match fresh elements within their one-point types for \(k\) rounds whenever all the capped counts coincide. This known equivalence is Proposition 3 in Carreiro–Facchini–Venema–Zanasi, not a new theorem here.

**2. Coefficient identity.** An ordered assignment of \(n\) labeled elements to the \(M\) one-point types having count vector \((a_1,\ldots,a_M)\) occurs in \(n!/\prod a_i!\) ways; the second assignment independently has counts \((b_1,\ldots,b_M)\). At a single type, the permitted pairs are exactly \(a=b<k\), or \(a,b\ge k\). Its exponential bivariate generating function is \(F_k\). Multiplying over all types, extracting the double degree \((n,n)\), and dividing by \(M^{2n}\) proves (1). At \(k=1\), both samples must use exactly the same set of \(j\) types; there are \(\binom Mj\) choices and \(j!S(n,j)\) surjections for each sample, yielding the stated sum.

**3. Unique saddle.** At diagonal \((t,t)\), the distribution \(\pi_{k,t}\) is symmetric in the two coordinates. Its single-coordinate mean \(\mu_k(t)\) equals \(t\partial_x\log F_k(t,t)\). The derivative of \(2\mu_k(t)\) with respect to \(\log t\) is the variance of \(A+B\) under \(\pi_{k,t}\), which is strictly positive since both \((0,0)\) and \((k,k)\) have positive mass. As \(t\downarrow0\), \(\mu_k(t)\to0\); as \(t\to\infty\), \(\mu_k(t)\to\infty\) (e.g. both coordinates of the double-tail conditional law have diverging means). Thus each \(\beta>0\) determines a unique saddle \(t\). The covariance is strictly positive definite: \((0,0),(k,k),(k+1,k),(k,k+1)\) are supported, and their difference vectors include the coordinate unit vectors.

**4. Two-dimensional local limit at the saddle.** Let \((A_i,B_i)\), for \(1\le i\le M\), be independent with law \(\pi_{k,t_M}\). Exponential tilting gives the *exact* identity
\[
[x^ny^n]F_k(x,y)^M=F_k(t_M,t_M)^M t_M^{-2n}
\Pr\left\{\sum_i(A_i,B_i)=(n,n)\right\}.
\]
The sum is centered at \((n,n)\) by the saddle equation. Its covariance is \(M\Sigma_{k,t_M}\). The support's difference lattice is all of \(\mathbb Z^2\), because the differences between \((k,k)\), \((k+1,k)\), and \((k,k+1)\) are the two unit vectors. Consequently the modulus of its characteristic function is strictly below one on the compact torus outside any neighborhood of the origin. Since \(t_M\to t(\alpha)>0\), this gap is uniform on compact sets away from zero, and all third moments are uniformly bounded. Fourier inversion, a second-order Taylor expansion of the characteristic function at the origin, and Gaussian dominated convergence on the scale \(M^{-1/2}\) now yield the **aperiodic lattice local central limit theorem**
\[
\Pr\left\{\sum_i(A_i,B_i)=(n,n)\right\}
=\frac{1+o(1)}{2\pi M\sqrt{\det\Sigma_{k,t_M}}}.
\]
No unproved global saddle-point analyticity or unbounded-support enumeration is needed. Stirling's formula \(n!=(1+o(1))\sqrt{2\pi n}(n/e)^n\) substituted in (1) gives (2), with the prefactor \(n/M\) and rate \(I_k\) as displayed.

**5. Rank-one critical point.** Here \(F_1(x,y)=1+(e^x-1)(e^y-1)\). The diagonal saddle equation is
\[
\beta=\frac{t e^t(e^t-1)}{1+(e^t-1)^2}.
\]
The equality \(t=\beta\) holds exactly when \(e^t-1=1\), or \(t=\beta=\log2\). At this value, \(F_1(t,t)=2\), and direct calculation under \(\pi_{1,t}\) gives
\[
\Sigma_{1,t}=\begin{pmatrix}t&t^2\\t^2&t\end{pmatrix},
\quad \det\Sigma_{1,t}=t^2(1-t^2),\quad I_1(t)=\log2.
\]
The derivative of the optimized rate is \(I'_1(\beta)=2\log(t(\beta)/\beta)\), so it vanishes at \(\beta=\log2\). With \(n=\lfloor M\log2\rfloor\), \(\beta_M=\log2+O(M^{-1})\), giving \(M I_1(\beta_M)=M\log2+o(1)\). Applying (2) proves (3). Finally, \(u\mapsto\log F_k(e^u,e^u)-2\beta u\) is strictly convex (its second derivative is the variance of \(A+B\)). It is minimized at the saddle; comparison with \(u=\log\beta\) shows \(I_k(\beta)\ge2\beta-\log F_k(\beta,\beta)\). In rank one, equality holds precisely when \(\beta=\log2\), as already solved.

## Verification
The accompanying standalone `verify.py` compares the bivariate coefficient identity against independently enumerated Boolean type-count signatures for all \(48\) triples \((M,n,k)\) with \(M\in\{2,4,8\}\), appropriate \(0\le n\le5\), and \(k\in\{1,2,3\}\). For rank one, it also independently checks the Stirling-number expression. Exact arithmetic uses rational numbers throughout these finite tests. At \(M=32,64,128,256\), numerical evaluation of the exact rank-one Stirling sum checks convergence of \(2^M C_{M,\lfloor M\log2\rfloor,1}\) toward the constant \((1-(\log2)^2)^{-1/2}\); this is corroborative, not the proof of an infinite asymptotic. The universal theorem rests on Steps 1–5.

## Relationship to prior work
Carreiro, Facchini, Venema and Zanasi (arXiv:1809.03262, first public 10 September 2018; journal DOI below) give the foundational rank-\(k\) equivalence criterion for monadic structures, and this is **not** claimed as original. Dupuis, Nuzman and Whiting (2007) provide broad sample-path large-deviation principles for colored occupancy; their results might cover the qualitative existence of a large-deviation exponential rate for a related event, but do not state the particular double-collision coefficient asymptotic, its local-limit prefactor, or the \(\log2\) fixed-size/Poissonized contact point in the inspected material. The new assertion is the full explicit fixed-size probability (1)–(3), particularly the non-unit sharp constant and its logical interpretation. A broad matching statement under different nomenclature has not been ruled out exhaustively.

## Limitations
No independent mathematical audit has been performed. The argument assumes independent uniform unary assignments, deterministic equal domain sizes, fixed positive quantifier rank, and positive limiting sample-to-type ratio. It does not cover dependent predicates, relational symbols of arity above one, growing rank, or uniform estimates as the density approaches zero or infinity. Related general occupancy large-deviation theorems may imply portions of the logarithmic rate but not automatically the exact prefactor. Finite numerical checks are not proofs of the all-parameter statements.

## References
1. F. Carreiro, A. Facchini, Y. Venema, F. Zanasi, *Model Theory of Monadic Predicate Logic with the Infinity Quantifier*, arXiv:1809.03262 (first submitted 10 September 2018); *Archive for Mathematical Logic* 61 (2022), 465–502, DOI: 10.1007/s00153-021-00797-0, §3.2, Definition 11 and Proposition 3.
2. P. Dupuis, C. Nuzman, P. Whiting, *Large deviations principle for occupancy problems with colored balls*, *Journal of Applied Probability* 44 (2007), 115–141, DOI: 10.1239/jap/1175267167.
