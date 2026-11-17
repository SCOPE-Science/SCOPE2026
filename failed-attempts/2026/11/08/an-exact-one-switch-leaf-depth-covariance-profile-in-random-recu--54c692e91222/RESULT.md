# An exact one-switch leaf–depth covariance profile in random recursive trees

## Finding

Fix an integer \(n\ge3\). In a uniformly random recursive tree \(T_n\), let \(X_{n,d}\) be the number of vertices at distance \(d\) from the root and let \(L_n\) be the total number of leaves. Then the covariance generating polynomial is exactly

\[
C_n(z):=\sum_{d=0}^{n-1}\operatorname{Cov}(X_{n,d},L_n)z^d
=\frac{n-2}{2(n-1)!}\,z(1-z)\prod_{r=2}^{n-2}(z+r).
\tag{1}
\]

An empty product is one, in particular when \(n=3\). This specifies every finite-sample covariance without asymptotic approximation.

For an equivalent probabilistic form, let \(Y_n\) be a sum of independent Bernoulli variables with respective probabilities \(1/r\) for integers \(3\le r\le n-1\), with the empty sum equal to zero. Write \(q_{n,j}=\Pr(Y_n=j)\), setting the probability to zero outside its support. Then, for every integer \(0\le d\le n-1\),

\[
\operatorname{Cov}(X_{n,d},L_n)
=\frac{n-2}{4}\bigl(q_{n,d-1}-q_{n,d-2}\bigr).
\tag{2}
\]

In particular, the covariances at positive depths start strictly positive, have at most one zero, and end strictly negative. Their signs never change back from negative to positive. The sign-switch location is the mode of a natural Poisson-binomial random variable, not an arbitrary empirical cutoff.

## Assumptions and scope

Start with a root labeled one. Independently for each integer \(k\in\{2,\ldots,n\}\), attach vertex \(k\) to a uniformly random parent in \(\{1,\ldots,k-1\}\). The tree is rooted at label one. A vertex is a leaf exactly when its number of children is zero, including the newest vertex. Tree depth is graph distance from the root. All expectations are over these independent parent choices. For \(n\ge2\), the root is not a leaf. At depth zero, \(X_{n,0}=1\) deterministically, hence its covariance is zero. At \(n=2\) all leaf counts are deterministic and all covariances are zero; the nondegenerate assertion concerns \(n\ge3\).

## Proof

Define the random polynomials

\[
Z_n(z)=\sum_{v\in T_n}z^{\operatorname{depth}(v)},\qquad
U_n(z)=\sum_{v\text{ a leaf}}z^{\operatorname{depth}(v)},\qquad L_n=U_n(1).
\]

Write \(A_n(z)=\mathbb E[Z_n(z)]\), \(B_n(z)=\mathbb E[U_n(z)]\), and \(D_n(z)=\mathbb E[Z_n(z)L_n]\). Condition on the current tree and let \(P\) be the uniform parent of the next vertex. If \(t=z^{\operatorname{depth}(P)}\) and \(b\) is the indicator that \(P\) is currently a leaf, then

\[
Z_{n+1}=Z_n+zt,\quad U_{n+1}=U_n+zt-bt,\quad L_{n+1}=L_n+1-b.
\]

Conditional uniformity gives \(\mathbb E[t\mid T_n]=Z_n/n\), \(\mathbb E[bt\mid T_n]=U_n/n\), and \(\mathbb E[b\mid T_n]=L_n/n\). Multiplying the first and third update identities and taking expectations yields the **exact** polynomial recurrences

\[
\begin{aligned}
A_{n+1}&=(1+z/n)A_n,\\
B_{n+1}&=(1-1/n)B_n+(z/n)A_n,\\
D_{n+1}&=(1+(z-1)/n)D_n+(1+z/n)A_n-(z/n)B_n.
\end{aligned}
\tag{3}
\]

At \(n=2\), the tree is deterministic and \(A_2=D_2=1+z\), \(B_2=z\), and \(L_2=1\). The first two recurrences imply, by induction,

\[
A_n(z)=\prod_{r=1}^{n-1}\frac{z+r}{r},\qquad
(1+z)B_n(z)=zA_n(z),\qquad \mathbb E[L_n]=n/2.
\tag{4}
\]

The middle equation is a polynomial identity: no evaluation at a singular complex point is needed. Put \(C_n=D_n-(n/2)A_n\). Substituting (3)–(4) gives

\[
C_{n+1}=\frac{n+z-1}{n}C_n+
\frac{z(1-z)}{2n(1+z)}A_n,\qquad C_2=0.
\tag{5}
\]

An induction in (5) yields

\[
C_n(z)=\frac{(n-2)z(1-z)}{2(1+z)(n+z-1)}A_n(z).
\]

Canceling the factors present in \(A_n\) proves (1), as a polynomial identity valid for all complex \(z\).

Next, the probability generating polynomial of \(Y_n\) is

\[
\mathbb E[z^{Y_n}]
=\prod_{r=3}^{n-1}\left(1-\frac1r+\frac zr\right)
=\frac{2}{(n-1)!}\prod_{r=2}^{n-2}(z+r).
\]

Thus \(C_n(z)=(n-2)z(1-z)\mathbb E[z^{Y_n}]/4\), and comparison of coefficients proves (2). All coefficients \(q_{n,j}\) on the support are positive. The generating polynomial has only real negative zeros, so Newton's inequalities make these coefficients strictly log-concave at their interior indices. Therefore successive ratios \(q_{n,j}/q_{n,j-1}\) are strictly decreasing: the sequence has a single modal index or two adjacent equal modal indices, never a longer plateau. The differences in (2) are consequently positive first, possibly zero once, and then negative. Finally \(q_{n,0}>0\) and \(q_{n,n-3}>0\), giving the required strictly positive first and strictly negative last covariances. This proves the sign classification for every finite \(n\).

## Verification

The independent standard-library program \(verify.py\) enumerates all \((n-1)!\) parent-choice sequences for each integer \(2\le n\le10\), computing every depth histogram and leaf total directly. It compares their exact rational mixed moments with (1). Separately it executes the three unconditioned moment recurrences through size 65 and checks polynomial coefficients, endpoint signs, sign monotonicity, and selected structural sums for sizes 3–250. The completed program reports 4,687 exact comparisons passed. These finite calculations independently detect algebraic and indexing mistakes but are **not** used to infer the theorem for arbitrary tree size; that follows from (3)–(5) and the real-rootedness argument above. Reproduce with `python3 verify.py` from these two files in the same directory.

## Relationship to prior work

The classical random-recursive-tree profile \(X_{n,d}\) and its exact and asymptotic level–level covariances have been studied by van der Hofstad–Hooghiemstra–Van Mieghem and by Drmota–Hwang. Janson's 2005 depth-congruence results concern grouped depth counts and their asymptotic distributions; his 2004 degree-distribution article treats counts indexed by outdegree. These previously studied margins do not themselves supply the mixed covariance of **total leaves** with **every individual depth level**. Our theorem specifically resolves that mixed profile and its unique sign transition.

Two specializations of (1) are known separately: its degree-one coefficient is \(\operatorname{Cov}(X_{n,1},L_n)=(n-2)/(2(n-1))\), where \(X_{n,1}\) is the root degree, and its derivative at one is \(\operatorname{Cov}(\sum_d dX_{n,d},L_n)=-(n-2)/4\), involving total path length. They are checks and consequences **not claimed independently as novel**. A prior explicit formula for the entire leaf–level covariance polynomial would subsume this finding even if stated in another basis.

## Limitations

This is an exact covariance and sign theorem, not a joint distribution, central limit theorem, stochastic domination claim, or inference result. The proof is for uniform recursive trees with independent uniform parent choices, not preferential attachment, Hoppe trees, binary search trees, or plane-oriented recursive trees. Finite enumeration alone establishes nothing about all orders. Although the closest inspected sources and accessible prior records have no dominating mixed-profile statement, an implicit extraction from historical mixed-moment generating functions cannot be ruled out without broader expert assessment; independent validation has not been performed.

## References

1. S. Janson, *Congruence properties of depths in some random trees*, arXiv:math/0509471, publicly available September 21, 2005. https://arxiv.org/html/math/0509471v1
2. R. van der Hofstad, G. Hooghiemstra, P. Van Mieghem, *On the covariance of the level sizes in random recursive trees*, accessible manuscript: https://www.nas.ewi.tudelft.nl/people/Piet/papers/covarRSA.pdf
3. M. Drmota and H.-K. Hwang, *Profiles of random trees: correlation and width of random recursive trees and binary search trees*, *Advances in Applied Probability*, DOI:10.1239/aap/1118858628. https://doi.org/10.1239/aap/1118858628
4. S. Janson, *Asymptotic degree distribution in random recursive trees*, *Random Structures & Algorithms*, DOI:10.1002/rsa.20046. https://doi.org/10.1002/rsa.20046
5. B. Lodewijks, *On joint properties of vertices with a given degree or label in the random recursive tree*, arXiv:2204.09032. https://arxiv.org/abs/2204.09032
