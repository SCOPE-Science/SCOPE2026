# A rare fixed-point sign transition for distant descents of random involutions

## Finding

Fix an integer \(n\ge4\) and \(0\le k\le n\) with \(n-k\) even. Sample an involution \(\pi\) of \(\{1,\ldots,n\}\) uniformly, conditional on having exactly \(k\) fixed points, and put \(D_i=\mathbf1_{\{\pi(i)>\pi(i+1)\}}\). For all nonoverlapping position pairs \(1\le i<j-1\), \(j\le n-1\),

\[
\mathbb E[D_i]=\frac{n^2-k^2}{2n(n-1)},\qquad
\operatorname{Cov}(D_i,D_j)=\frac{(n-k)H_n(k)}{2n^2(n-3)(n-2)(n-1)^2},
\]

where

\[
H_n(x)=n^2(n-2)-n^2x+nx^2-(2n-3)x^3.
\]

For each \(n\), the polynomial \(H_n\) has exactly one zero \(\kappa_n\) in \((0,n)\). For every feasible \(k<n\), the covariance is positive when \(k<\kappa_n\), zero when \(k=\kappa_n\), and negative when \(k>\kappa_n\). At \(k=n\), every descent vanishes and the covariance is zero. The threshold has the expansion

\[
\boxed{\kappa_n=2^{-1/3}n^{2/3}-\frac{2^{1/3}}6n^{1/3}+\frac16+O(n^{-1/3}).}
\]

More precisely, if feasible integers \(k=k(n)\) satisfy \(k/n^{2/3}\to z\ge0\), then

\[
\lim_{n\to\infty}n^2\operatorname{Cov}(D_i,D_j)=\frac{1-2z^3}{2}
\]

uniformly in the choice of nonoverlapping positions at each \(n\). No fixed-position or growing-dimensional central limit theorem is asserted.

## Assumptions and scope

An involution is a permutation all of whose cycles have length one or two. The conditioning class contains exactly \(I(n,k)=n!/(k!2^rr!)\) permutations, with \(r=(n-k)/2\). A descent at \(i\) compares adjacent *images* in one-line notation. The result treats distinct descent positions separated by at least one intervening index. The threshold \(\kappa_n\) is a real root; feasible integer values must respect parity. In particular, an exact zero at a feasible \(k\) is not required for the sign to switch across available conditioning classes.

## Proof

Write \((x)_a=x(x-1)\cdots(x-a+1)\), with \((x)_0=1\). For two marked positions, classifying their involution edges as a mutual pair, one fixed/one attached outside, or both attached outside gives

\[
\mathbb P(D_i=1\mid k)=\frac{2r+2kr+2(r)_2}{(n)_2}
=\frac{n^2-k^2}{2n(n-1)}.
\]

To compute the joint probability for two nonoverlapping descents, mark the four distinct vertices \(i,i+1,j,j+1\). Every partial involution on these four vertices has \(f\) fixed marked vertices, \(e\) vertices partnered to distinct outside labels, and \(t\) internal pairs, satisfying \(f+e+2t=4\). There are 43 such partial patterns. Upon specifying the external partners, the probability of completing the partial pattern to an involution with \(k\) fixed points is

\[
\frac{I(n-4-e,k-f)}{I(n,k)}
=\frac{(k)_f 2^{e+t}(r)_{e+t}}{(n)_{4+e}},
\]

interpreted as zero for an impossible completion. Place the outside labels in the three disjoint intervals before, between and after the two adjacent pairs. Their sizes are \(A=i-1\), \(B=j-i-2\), and \(C=n-j-1\), with \(A+B+C=n-4\). In each partial pattern, assign outside endpoints injectively and count the fraction of partner choices satisfying *both* descents. The sum of these weighted assignment counts over each \((f,e,t)\) type is as follows, with \(v=n-4\):

| \((f,e,t)\) | Weighted external assignments for both descents |
| --- | --- |
| \((0,0,2)\) | \(2\) |
| \((0,2,1)\) | \(2(v)_2\) |
| \((0,4,0)\) | \((v)_4/4\) |
| \((1,1,1)\) | \(4v\) |
| \((1,3,0)\) | \((v)_3\) |
| \((2,0,1)\) | \(1\) |
| \((2,2,0)\) | \((v)_2\) |

Every unlisted type contributes zero. The seven formulas, including their independence of \(A,B,C\), follow by the finite partition of the 43 partial matching patterns and by the equal likelihood of each relative order of two distinct external partners in any one interval. This is a finite algebraic identity for *arbitrary* nonnegative interval sizes; the accompanying symbolic checker enumerates each pattern and proves every displayed polynomial identity, not just finitely many numerical cases.

Using \((n)_{4+e}=(n)_4(v)_e\) in the weighted sum, the joint descent probability becomes

\[
\begin{aligned}
\mathbb E[D_iD_j]\,=\,\frac{1}{(n)_4}\bigl[&8(r)_2+16(r)_3+4(r)_4\\
&+16k(r)_2+8k(r)_3\\
&+2(k)_2r+4(k)_2(r)_2\bigr].
\end{aligned}
\]

Substitute \(r=(n-k)/2\), subtract the square of the one-point probability, and cancel factors to obtain exactly \((n-k)H_n(k)/[2n^2(n-3)(n-2)(n-1)^2]\). Since the interval parameters have disappeared, the formula holds at every nonoverlapping pair, including pairs at the endpoints.

For \(n\ge4\),

\[
H_n'(x)=-n^2+2nx-3(2n-3)x^2<0\qquad(x\in\mathbb R),
\]

because its quadratic discriminant is \(4n^2(10-6n)<0\) and its leading coefficient is negative. Also \(H_n(0)=n^2(n-2)>0\) and \(H_n(n)=-2n^2(n-1)^2<0\). This proves the unique root and all finite sign claims, taking account of the factor \(n-k\).

For the root expansion write \(n=t^3\) and substitute \(\kappa_n=a t^2+b t+c+O(t^{-1})\) into \(H_n(\kappa_n)=0\). Successive coefficients of \(t^9,t^8,t^7\) give \(a=2^{-1/3}\), \(b=-1/(6a)=-2^{1/3}/6\), and \(c=1/6\). A Taylor/mean-value estimate using \(H_n'(\kappa_n)\asymp -t^7\) bounds the remaining root error by \(O(t^{-1})\). For \(k/n^{2/3}\to z\), divide the exact covariance expression by \(n^{-2}\); its numerator has \(H_n(k)=n^3(1-2z^3+o(1))\), yielding the claimed limit.

## Verification

Run `python verify.py` with Python 3 and SymPy installed. It checks all 43 four-marked-vertex partial patterns symbolically in three arbitrary interval variables; establishes the exact joint probability/covariance identity by symbolic cancellation; exhaustively compares all feasible classes of involutions at \(n=4,\ldots,10\) with every nonoverlapping position pair; and checks the root expansion coefficients. A successful run prints four `PASS` lines and reports 618 exact exhaustive assertions in 30 conditioning classes. Enumeration is an independent finite diagnostic, not a substitute for the all-\(n\) algebraic proof.

## Relationship to prior work

Reutenauer's descent-set/cycle-type scalar-product enumeration (1989), developed further by Gessel and Reutenauer, is a broad exact framework and in principle determines finite descent statistics for any cycle structure. The present contribution is the simplified *position-independent covariance formula under a fixed-point-count involution class* and, especially, the explicit \(n^{2/3}\) sign threshold and its two correction orders. Guo and Zeng (2005) study the unrestricted and fixed-point-free involution descent-number distributions, not this conditioned two-point covariance. Kim (2017) establishes two-point descent formulas for fixed-point-free involutions, so the \(k=0\) specialization here is already known and is not claimed as novel. Kim and Lee (2018) establish a general conjugacy-class CLT for the total descent number; its leading variance asymptotics do not identify this rare conditioning threshold for a specified nonlocal pair. These comparisons do not establish historical priority against every possible specialization of the general descent-set enumeration.

## Limitations

The proof concerns exactly two nonoverlapping ordinary descents and exact fixed-point-count conditioning on involutions. Adjacent descents, unrestricted random permutations and mixed cycle structures are outside its scope. The asymptotics use a one-parameter sequence of feasible fixed-point counts, not an unconditioned law or a limit theorem for an entire descent process. Existing general cycle-type/descent-set enumerators can imply finite instances; implicit previous derivations of the sign transition remain a priority risk. No independent audit has been performed.

## References

1. C. Reutenauer, *Number of Permutations with Given Descent Set and Cycle Structure*, Séminaire Lotharingien de Combinatoire B21h (1989), https://www.mat.univie.ac.at/~slc/s/sc21reutenauer.pdf .
2. V. J. W. Guo and J. Zeng, *The Eulerian Distribution on Involutions is Indeed Unimodal*, arXiv:math/0504195, first public version 2005-04-10, https://arxiv.org/abs/math/0504195 .
3. G. B. Kim, *Distribution of Descents in Matchings*, arXiv:1710.03896 (2017), https://arxiv.org/abs/1710.03896 .
4. G. B. Kim and S. Lee, *Central Limit Theorem for Descents in Conjugacy Classes of \(S_n\)*, arXiv:1803.10457 (2018), https://arxiv.org/abs/1803.10457 .
5. J. Fulman, *The Distribution of Descents in Fixed Conjugacy Classes of the Symmetric Groups*, Journal of Combinatorial Theory A (1998), https://doi.org/10.1006/jcta.1998.2893 .
