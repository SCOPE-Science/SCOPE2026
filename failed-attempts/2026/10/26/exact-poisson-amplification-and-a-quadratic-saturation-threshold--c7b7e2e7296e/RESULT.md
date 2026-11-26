# Exact Poisson amplification and a quadratic saturation threshold on rook graphs

## Finding

For integers \(2\le m\le n\), let \(R_{m,n}=K_m\mathbin{\square}K_n\) be the unweighted rook graph, let \(L\) denote its **unnormalized** combinatorial Laplacian, and let \(G=L^\dagger\). The sharp endpoint constant is
\[
\mathcal N(m,n):=\|G\|_{\ell^\infty\to\ell^\infty}=\|G\|_{\ell^1\to\ell^1}.
\]
For \(m\ge3\) it has the exact two-branch formula
\[
\boxed{\mathcal N(m,n)=\frac{2(m-1)}{m^2}+
\frac{2(m-1)}{m^2n^2(m+n)}
\bigl[m^2n-m^2-mn-n^2\bigr]_+,}\qquad [z]_+=\max\{z,0\}.
\]
For \(m=2\), the exceptional values are \(\mathcal N(2,2)=5/8\), \(\mathcal N(2,3)=47/90\); thereafter \(\mathcal N(2,n)=1/2\) for all \(n\ge4\). In particular \(\mathcal N(3,n)=4/9\) for every \(n\ge3\).

For every \(m\ge4\), put
\[
\rho_m=\frac m2\Bigl(m-1+\sqrt{(m-3)(m+1)}\Bigr).
\]
The endpoint norm is *exactly constant* in the second graph parameter whenever \(n\ge\lceil\rho_m\rceil\), namely
\[
\boxed{\mathcal N(m,n)=\frac{2(m-1)}{m^2}\quad (n\ge\lceil\rho_m\rceil).}
\]
For integers \(m\le n<\rho_m\) it strictly exceeds this plateau and equals
\[
\boxed{\mathcal N(m,n)=
\frac{2(m-1)(n-1)(m^2+mn+n^2)}{m^2n^2(m+n)}.}
\]
The cutoff is sharp: \(\rho_m\) is never an integer for \(m\ge4\). The positive Green-kernel support, and hence the form of the sign-pattern extremizers, changes exactly at the same cutoff. Over **all** \(m,n\ge2\), the sharp uniform bound is
\[
\boxed{\mathcal N(m,n)\le5/8,\qquad \text{equality only for }(m,n)=(2,2).}
\]

There are two distinguished large-size regimes. If \(m\to\infty\) and \(n/m\to r\in[1,\infty)\), then
\[
\boxed{m\mathcal N(m,n)\longrightarrow\frac{2(1+r+r^2)}{r(1+r)}.}
\]
At the quadratic aspect-ratio scale \(n/m^2\to\lambda\in(0,\infty)\), the *excess over the exact plateau* has the sharp crossover
\[
\boxed{m^3\left[\mathcal N(m,n)-\frac{2(m-1)}{m^2}\right]
\longrightarrow\frac{2(1-\lambda)_+}{\lambda^2}.}
\]
In particular the limiting excess has a corner at \(\lambda=1\), corresponding to the exact finite-size support transition.

## Assumptions and scope

The vertex set is \(\{1,\ldots,m\}\times\{1,\ldots,n\}\), with adjacent distinct vertices precisely when one coordinate agrees. Every graph edge has unit conductance. The norm on vertex functions is the **unnormalized** coordinate maximum norm \(\|f\|_\infty=\max_v|f(v)|\); the \(\ell^1\) norm is the ordinary sum of absolute values. The operator \(G\) acts on all real or complex vertex functions and annihilates constants. It provides the unique zero-mean solution \(u=Gf\) of \(Lu=f-\overline f\,\mathbf1\), where \(\overline f\) is the vertex average. Sharpness is for all bounded inputs \(f\), not for the different operator norm obtained by restricting the input domain to functions of mean zero.

The graph \(K_m\mathbin{\square}K_n\) is also the line graph of \(K_{m,n}\); interchanging \(m\) and \(n\) changes none of the conclusions. The claimed asymptotic limits are along arbitrary integer sequences satisfying the displayed scaling assumptions.

## Proof

Write \(E_q=J_q/q\) and \(P_q=I_q-E_q\) for the constant and mean-zero orthogonal projections on \(\mathbb R^q\). Tensor decomposition gives
\[
L=mP_m\otimes I_n+nI_m\otimes P_n,
\quad
G=\frac1mP_m\otimes E_n+\frac1nE_m\otimes P_n+
\frac1{m+n}P_m\otimes P_n.
\tag{1}
\]
The three summands have pairwise orthogonal ranges, and their nonzero eigenvalues invert exactly those of \(L\); therefore (1) is the Moore--Penrose inverse, not merely a candidate generalized inverse. If \(v=(i,j)\), \(w=(k,\ell)\), let \(a=\mathbf1_{i=k}-1/m\) and \(b=\mathbf1_{j=\ell}-1/n\). The exact matrix entry is
\[
G(v,w)=\frac{a+b}{mn}+\frac{ab}{m+n}.
\tag{2}
\]
For a fixed \(v\), four orbits of \(w\) occur: diagonal \(D\), same first coordinate with differing second coordinate \(R\), same second coordinate with differing first coordinate \(C\), and differing in both coordinates \(F\). Put \(Z=m^2n^2(m+n)\). Substitution in (2) gives
\[
\begin{aligned}
D&=(m^2n^2+m^2n-m^2+mn^2-mn-n^2)/Z,\\
R&=(mn^2-mn-m^2-n^2)/Z,\\
C&=(m^2n-m^2-mn-n^2)/Z,\\
F&=-(m^2+mn+n^2)/Z.
\end{aligned}
\tag{3}
\]
The respective multiplicities are \(1,n-1,m-1,(m-1)(n-1)\). Since \(G\mathbf1=0\), every row sums to zero. Also \(D>0\) by (1), \(F<0\) by (3), and
\[
R-C=\frac{n-m}{mn(m+n)}\ge0.
\tag{4}
\]
Consequently the absolute row sum is exactly
\[
\mathcal N(m,n)=2\bigl[D+(n-1)[R]_++(m-1)[C]_+\bigr].
\tag{5}
\]
All rows have this sum by vertex transitivity, and symmetry of \(G\) makes the \(\ell^1\) norm identical. Choosing \(f(w)=\operatorname{sgn}G(v,w)\) on nonzero entries attains (5), proving sharpness over real inputs as well as complex inputs.

For \(m\ge3\), \(n\ge m\), the numerator of \(R\) is \((m-1)n^2-mn-m^2\). This is increasing in \(n\ge m\), where its minimum is \(m^2(m-3)\ge0\). Thus \(R\ge0\) and direct cancellation in (3) gives
\[
D+(n-1)R=\frac{m-1}{m^2}.
\tag{6}
\]
Inserting (6) in (5) proves the principal positive-part formula. For \(m=2\), (3) gives \(R<0\) exactly at \(n=2,3\), and \(C<0\) at every \(n\ge2\); (5) gives the three claimed exceptional formulas.

For \(m=3\), the numerator of \(C\) is \(-(n-3)^2\), proving the constant \(4/9\). For \(m\ge4\), the numerator of \(C\) equals \(-n^2+(m^2-m)n-m^2\), whose roots are
\[
\rho_m^\pm=\frac m2\Bigl(m-1\pm\sqrt{(m-3)(m+1)}\Bigr).
\]
The smaller root is below \(m\) and the larger root \(\rho_m\) exceeds \(m\). Therefore \(C>0\) precisely for \(m\le n<\rho_m\), and \(C<0\) for \(n>\rho_m\). The discriminant is \(m^2((m-1)^2-4)\). For integer \(m\ge4\), if \((m-1)^2-4\) were an integer square \(s^2\), then \((m-1-s)(m-1+s)=4\), whose only nonnegative integer solution with same-parity factors is \(m=3\); contradiction. Hence \(\rho_m\) is irrational and the sharp integer cutoff is \(\lceil\rho_m\rceil\). When \(C>0\), adding its contribution to (6) and simplifying proves the rational three-factor formula above. For \(m\ge3\) (and for \(m=2,n\ge4\)), an extremizing input can be chosen with unit modulus, positive sign on the union of the root's row and column when \(C>0\), and on the root's row alone when \(C<0\); the sign is opposite elsewhere. At \(m=2,n\in\{2,3\}\), only the diagonal kernel entry is positive, so the extremizer has a single positive vertex. At zero kernel entries either sign is permissible. Thus the same cutoff is an actual extremizer-support transition, not just an algebraic reformulation.

For the universal bound, the case \(m=2\) has values \(5/8,47/90,1/2\); the case \(m=3\) has value \(4/9\). For \(m\ge4\), the plateau branch is at most \(3/8\). The other branch can be written as
\[
\frac{2(m-1)}{m^2}\left(1-\frac1n\right)
\left(1+\frac{m^2}{n(m+n)}\right)
\le \frac{3(m-1)}{m^2}\le\frac9{16}<\frac58,
\]
since \(n\ge m\ge4\). Thus the global maximum is \(5/8\), uniquely at the four-cycle \(R_{2,2}\).

If \(n/m\to r\in[1,\infty)\) as \(m\to\infty\), the positivity numerator for \(C\) is eventually positive, so the rational non-plateau expression gives the first scaling limit after division by powers of \(m\). For the second limit, put \(n/m^2\to\lambda\in(0,\infty)\) into the positive-part formula: the numerator of \(C\), divided by \(m^4\), tends to \(\lambda-\lambda^2\), while its denominator, divided by \(m^8\), tends to \(\lambda^3\). Since \(m^3(m-1)/m^4\to1\), continuity of \([\,\cdot\,]_+\) gives the stated crossover, including the critical case \(\lambda=1\). Each of these steps holds for arbitrary integer sequences with the specified limits.

## Verification

The standalone standard-library script `verify.py` calculates independent orbit entries using rational arithmetic, checks zero-row sums, four-orbit sign inequalities, exact norms and integer cutoffs over parameter grids, and independently inverts \(L+J/(mn)\) over the rational numbers for seven small product graphs. It then checks \(G=(L+J/(mn))^{-1}-J/(mn)\) entry by entry. Execute `python3 verify.py` from the directory containing this file and the script. These finite checks are reproducibility tests, *not* a substitute for the general proof above. The scaling limits follow from the displayed exact identities, not numerical experiments.

## Relationship to prior work

Ellis (2003), Sections 2 and 4, derives general spectral Green-function identities for Cartesian products of regular graphs; those foundational tensor-inversion principles subsume (1) as a kernel computation. Beveridge (2015) establishes general discrete Green-function representations in terms of hitting times and spectral data. Fontan and Altafini (2021) show that off-diagonal entries of a Laplacian pseudoinverse can have mixed signs. These mathematical facts are prior work and are not claimed as new. The asserted contribution here is the **explicit induced endpoint-norm phase diagram**, exact finite quadratic aspect-ratio plateau, sharp sign-mask transition, universal bound and two asymptotic crossover laws for the rook-graph family. General formulas for Green matrices do not explicitly state these sharp nonlinear absolute-row-sum consequences. Full historical priority is not independently established.

## Limitations

The results apply to unweighted rook graphs and the unnormalized combinatorial Laplacian. They do not classify Green norms for arbitrary Cartesian products, do not describe the norm restricted to a mean-zero unit ball, and do not cover edge weights, normalized graph Laplacians, or \(\ell^p\) norms for interior exponents. The root threshold need not be optimal for other graph families. Prior generic Green formulas are explicitly acknowledged; novelty of the endpoint phase diagram is subject to a broader independent literature audit.

## References

1. R. B. Ellis, *Discrete Green's functions for products of regular graphs*, arXiv:math/0309080, originally submitted 2003-09-04, Sections 2 and 4. https://arxiv.org/abs/math/0309080
2. A. Beveridge, *A Hitting Time Formula for the Discrete Green's Function*, arXiv:1505.06989, first submitted 2015-05-26, Sections 1, 4 and 5. https://arxiv.org/abs/1505.06989
3. A. Fontan and C. Altafini, *On the properties of Laplacian pseudoinverses*, arXiv:2109.14587, originally submitted 2021-09-29, introduction and signed-Laplacian results. https://arxiv.org/abs/2109.14587
