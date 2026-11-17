# A weighted two-degree spectral law for finite-rank harmonic Bergman Toeplitz commutators

## Finding

Two analytic monomial Toeplitz factors can converge strongly to zero while their finite-rank commutator retains a macroscopic, explicitly distributed family of singular values. For each fixed radial beta weight, the singular-value distribution under **simultaneous growth of both symbol degrees** converges to an explicit continuous profile; its \(p\)-th Schatten mass grows linearly with the smaller degree for every \(p>0\). In the ordinary harmonic Bergman space, the exact finite-degree operator norm also has a sharp global supremum \(2/(3\sqrt3)\).

## Assumptions and scope

Let \(\mathbb D\) be the open unit disk, let \(dA(z)=\pi^{-1}dx\,dy\), and choose \(\alpha>-1\), \(\beta=\alpha+1>0\). Equip the disk with probability measure
\[
dA_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha\,dA(z).
\]
Write \(h^2_\alpha\) for the complex Hilbert space of square-integrable complex-valued harmonic functions. Let \(P_{h,\alpha}\) be the corresponding orthogonal projection. For integers \(j\ge1\), put
\[
T_j=P_{h,\alpha}M_{z^j}|_{h^2_\alpha},\qquad
\mu_k=\int_{\mathbb D}|z|^{2k}\,dA_\alpha(z)
=\frac{\Gamma(\beta+1)\Gamma(k+1)}{\Gamma(k+\beta+1)}\quad(k\ge0).
\]
All operators use the full harmonic space, not the analytic Bergman subspace. The index \(k\) below is an integer, and \(m>n\ge1\). Set \(M=m+n\). An orthonormal basis is \(e_k=z^k/\sqrt{\mu_k}\) for \(k\ge0\), and \(e_{-k}=\overline z^{\,k}/\sqrt{\mu_k}\) for \(k\ge1\).

## Proof

**1. Exact orthogonal coefficient formula.** On the displayed basis, multiplication and harmonic projection yield
\[
T_d e_j=\begin{cases}
\sqrt{\mu_{j+d}/\mu_j}\,e_{j+d},&j\ge0,\\
\sqrt{\mu_{-j}/\mu_{-j-d}}\,e_{j+d},&j\le-d,\\
\mu_d/\sqrt{\mu_{-j}\mu_{j+d}}\,e_{j+d},&-d<j<0.
\end{cases}
\]
Every coefficient is real and nonnegative. Since powers commute on the analytic subspace and on antianalytic modes remaining antianalytic after both multiplications, the commutator \(C_{m,n}=[T_m,T_n]\) vanishes outside \(e_{-k}\), \(1\le k<M\). Direct substitution gives \(C_{m,n}e_{-k}=c_{m,n}(k)e_{M-k}\), with
\[
 c_{m,n}(k)=\begin{cases}
\sqrt{\frac{\mu_{M-k}}{\mu_k}}
\left(\frac{\mu_n}{\mu_{n-k}}-\frac{\mu_m}{\mu_{m-k}}\right),&1\le k\le n,\\[2mm]
\mu_m\left(\frac{1}{\mu_{k-n}}\sqrt{\frac{\mu_k}{\mu_{M-k}}}
-\frac{1}{\mu_{m-k}}\sqrt{\frac{\mu_{M-k}}{\mu_k}}\right),&n<k<m,\\[2mm]
\sqrt{\frac{\mu_k}{\mu_{M-k}}}
\left(\frac{\mu_m}{\mu_{k-n}}-\frac{\mu_n}{\mu_{k-m}}\right),&m\le k<M.
\end{cases}
\]
There is no overlap or gap in the three cases. The output basis vectors are pairwise different, so the singular values, including possible zero coefficients, are precisely \(|c_{m,n}(k)|\) for \(1\le k<M\), padded with zeros. Since their range is analytic and they annihilate the analytic space, \(C_{m,n}^2=0\). For every \(p>0\),
\[
\|C_{m,n}\|_{\mathcal S_p}^p=\sum_{k=1}^{M-1}|c_{m,n}(k)|^p.
\]

**2. Simultaneous-degree profile.** Take any sequences of integers with \(m_j>n_j\to\infty\) and \(m_j/n_j\to\lambda>1\), and put \(L=\lambda+1\). Define \(f_{\beta,\lambda}\) continuously on \([0,L]\) by
\[
f_{\beta,\lambda}(t)=
\begin{cases}
\left(\frac{t}{L-t}\right)^{\!\beta/2}
\left[(1-t)^\beta-\left(\frac{\lambda-t}{\lambda}\right)^\beta\right],&0\le t\le1,\\[2mm]
\left(\frac{L-t}{t}\right)^{\!\beta/2}
\left(\frac{t-1}{\lambda}\right)^\beta
-\left(\frac{t}{L-t}\right)^{\!\beta/2}
\left(\frac{\lambda-t}{\lambda}\right)^\beta,&1\le t\le\lambda,\\[2mm]
\left(\frac{L-t}{t}\right)^{\!\beta/2}
\left[\left(\frac{t-1}{\lambda}\right)^\beta-(t-\lambda)^\beta\right],&\lambda\le t\le L.
\end{cases}
\]
At \(t=0,L\), define the displayed expressions by their zero limits. At \(t=1,\lambda\), neighboring formulas agree; thus the function is continuous. The gamma ratio yields
\[
\mu_q=\Gamma(\beta+1)q^{-\beta}(1+O(q^{-1}))\qquad(q\to\infty).
\]
On every compact subinterval avoiding the four transition points \(0,1,\lambda,L\), insert this expansion into the exact formulas and obtain, uniformly for \(k/n_j\) in that interval,
\[
c_{m_j,n_j}(k)-f_{\beta,\lambda}(k/n_j)\longrightarrow0.
\]
Every \(T_d\) is a contraction (compression of multiplication by \(z^d\)), hence \(|c_{m,n}(k)|\le\|[T_m,T_n]\|\le2\). The transition neighborhoods contain at most a proportion \(O(\delta)\) of the indices, while both coefficients and the limiting profile are uniformly bounded. Removing these neighborhoods, using the uniform interior asymptotics and then letting \(\delta\downarrow0\), proves for **every continuous \(\varphi:[0,2]\to\mathbb R\)**
\[
\frac{1}{n_j}\sum_{k=1}^{m_j+n_j-1}\varphi(|c_{m_j,n_j}(k)|)
\longrightarrow\int_0^L\varphi(|f_{\beta,\lambda}(t)|)\,dt.
\]
The right-hand side is finite. Choosing \(\varphi(s)=s^p\) proves, for every fixed real \(p>0\),
\[
\boxed{\quad\frac{1}{n_j}\|C_{m_j,n_j}\|_{\mathcal S_p}^p
\longrightarrow \int_0^{\lambda+1}|f_{\beta,\lambda}(t)|^p\,dt>0.\quad}
\]
Strict positivity follows because for any \(0<t<1\), \((1-t)<(\lambda-t)/\lambda\), hence the first branch of \(f_{\beta,\lambda}\) is strictly negative. As an operator statement, the commutator has nonvanishing liminf of its operator norm along every such degree sequence.

**3. The strong/norm dichotomy.** On each fixed analytic basis vector \(e_q\), \(\|T_d e_q\|=\sqrt{\mu_{q+d}/\mu_q}\to0\) as \(d\to\infty\). On each fixed antianalytic basis vector \(e_{-q}\), eventually \(d>q\) and \(\|T_d e_{-q}\|=\mu_d/\sqrt{\mu_q\mu_{d-q}}\to0\). Their norms are uniformly at most one, so density of finite basis combinations implies \(T_d\to0\) strongly. Products of two uniformly bounded strongly-null sequences also converge strongly to zero. Thus \(C_{m_j,n_j}\to0\) strongly although its operator norm cannot tend to zero (by step 2).

**4. Exact unweighted norm.** When \(\alpha=0\), \(\beta=1\), \(\mu_q=(q+1)^{-1}\). The coefficients in step 1 simplify to
\[
c_{m,n}(k)=\begin{cases}
\frac{(n-m)k}{(m+1)(n+1)}\sqrt{\frac{k+1}{M-k+1}},&1\le k\le n,\\[2mm]
\frac{n(2k-M)}{(m+1)\sqrt{(k+1)(M-k+1)}},&n\le k\le m,\\[2mm]
\frac{(m-n)(M-k)}{(m+1)(n+1)}\sqrt{\frac{M-k+1}{k+1}},&m\le k<M.
\end{cases}
\]
The first magnitude increases with \(k\); the third decreases; and the middle magnitude is smallest at \(k=M/2\) and increases toward each endpoint, since \(|2k-M|/\sqrt{(k+1)(M-k+1)}\) is increasing with the distance from \(M/2\). The endpoint magnitudes at \(k=n,m\) agree, giving the exact formula
\[
\boxed{\quad\|C_{m,n}\|=\frac{n(m-n)}{(m+1)^{3/2}\sqrt{n+1}}\quad}.
\]
Writing \(r=m/n>1\), this is strictly less than \((r-1)r^{-3/2}\); the latter has global maximum \(2/(3\sqrt3)\) at \(r=3\). Taking \(m=3n\) and letting \(n\to\infty\) attains this value only in the limit, proving
\[
\boxed{\quad\sup_{m>n\ge1}\|C_{m,n}\|=\frac2{3\sqrt3}\quad}
\]
with no maximizing finite integer pair. The same supremum applies to unequal positive degree pairs in either order, since reversing the order changes only the sign.

## Verification

All basis-action and moment-ratio identities were derived directly from the orthogonal projection formula; no finite experiment substitutes for the limiting gamma-ratio proof. Supplementary `CHECKER.py` independently computes each two-step matrix coefficient and checks the three-branch formula for beta parameters \(0.4,1,2,3.5\), \(2\le m\le23\), \(1\le n<m\), and each relevant input index; it also checks the unweighted exact norm for \(2\le m\le40\), \(1\le n<m\). The auxiliary code uses only the standard Python library and reports finite diagnostics, not an exhaustive proof over parameters or dimensions.

## Relationship to prior work

Cui–Huang–Lu–Zu [1] give an algebraic classification of all finite-rank commutators with bounded harmonic symbols on the **unweighted** harmonic Bergman space, including their square-zero property. The present work does not claim that square-zero or finite rank is new. Dong–Zhou [2, Remark 4.8] already identify canonical coefficient/range forms of the **unweighted** two-monomial commutator and credit Chen–Koo–Lee [3] for an earlier direct coefficient derivation. Accordingly, the ordinary-weight exact norm is presented as a supporting sharp consequence rather than a new rank or coefficient classification. The principal new assertion is the **weighted beta-family, simultaneously growing two-degree empirical singular-value law and the resulting positive Schatten-mass density**, including strong-versus-norm separation; the cited prior results do not contain that limiting claim. A related existing analysis for a fixed first degree and a growing second degree concerns a different asymptotic regime, which does not give the present proportional-degree limit.

## Limitations

The result covers radial beta weights and analytic **monomial pairs** with a degree ratio converging to a fixed number strictly greater than one. It neither classifies general analytic symbols nor treats ratios tending to one or infinity; those are separate scaling regimes. For a general beta weight, the explicit integral of the limiting profile is not evaluated in closed form, and an exact finite-degree norm formula is claimed only at the unweighted parameter. The publication-priority comparison cannot exclude an equivalent historical reformulation under different terminology; independent mathematical verification has not been performed.

## References

[1] P. Cui, Z. Huang, Y. Lu and C. Zu, *Finite-rank Toeplitz commutators on the harmonic Bergman space*, arXiv:2611.08988v1 (first posted 2026-11-06), Theorem 1.1, Corollary 3.1, Section 3. https://arxiv.org/abs/2611.08988

[2] X.-T. Dong and Z.-H. Zhou, *Ranks of Commutators and Generalized Semicommutators of Quasihomogeneous Toeplitz Operators*, arXiv:1411.0213v3 (first posted 2014-11-02), Remark 4.8. https://arxiv.org/abs/1411.0213

[3] Y. Chen, H. Koo and Y. J. Lee, *Ranks of commutators of Toeplitz operators on the harmonic Bergman space*, Integral Equations and Operator Theory **75** (2013), 31–38, DOI:10.1007/s00020-012-2020-6, cited in [1,2].
