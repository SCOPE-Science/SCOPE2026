# Sharp sixth moments and two-level rigidity in finite Poisson first chaos

## Finding

Let \(n\ge2\), \(\lambda>0\), and let \(Z_1,\ldots,Z_n\) be independent Poisson random variables, each of mean \(\lambda\). For nonzero \(a\in\mathbb R^n\), put
\[
F_a=\sum_{i=1}^n a_i(Z_i-\lambda),\qquad
K_{n,\lambda}(a)=\frac{\mathbb E F_a^6}{(\mathbb E F_a^2)^3}.
\]
Define \(U_\lambda=15+25/\lambda+1/\lambda^2\). For even \(n\), define
\[
L_{n,\lambda}=15+\frac{15}{n\lambda}+\frac{1}{n^2\lambda^2}.
\]
For odd \(n\), define the following finite algebraic prescription. For each integer \(1\le k\le (n-1)/2\), let \(\ell=n-k\), and let \(t_{k,\ell}>1\) be the **unique** root above one of
\[
P_{k,\ell,\lambda}(t)=
(1+20\lambda k)t^3-(1+10\lambda k)t^2
 +(1+10\lambda\ell)t-(1+20\lambda\ell).
\]
Set \(D_{k,\ell}=kt_{k,\ell}^2+\ell\) and
\[
H_{k,\ell,\lambda}=15+
\frac{15(kt_{k,\ell}^4+\ell)}{\lambda D_{k,\ell}^2}+
\frac{10(kt_{k,\ell}^3-\ell)^2}{\lambda D_{k,\ell}^3}+
\frac{kt_{k,\ell}^6+\ell}{\lambda^2 D_{k,\ell}^3}.
\]
For odd \(n\) put \(L_{n,\lambda}=\min_{1\le k\le(n-1)/2} H_{k,n-k,\lambda}\). This is an **exact finite algebraic formula**, not a residual continuous variational problem. Then, for every nonzero \(a\),
\[
\boxed{L_{n,\lambda}\le K_{n,\lambda}(a)\le U_\lambda.}
\]
Every value in the closed interval occurs. Maximal equality holds exactly when \(a\) has one nonzero coordinate. For even \(n\), minimal equality holds exactly when all coordinate magnitudes agree and precisely half the coefficients are positive and half negative. For odd \(n\), minimal equality holds exactly for nonzero scalar multiples and coordinate permutations of the vectors having \(k\) entries equal to \(t_{k,n-k}\) and \(n-k\) entries equal to \(-1\), for those \(k\) realizing the explicitly defined finite minimum. In particular, every odd-dimensional minimizer has two different nonzero coefficient magnitudes; an equal-magnitude coefficient vector can never minimize.

## Assumptions and scope

The coefficient field is real; the Poisson means are identical and strictly positive; the variables are independent; and the moment exponent is six. All assertions are uniform in the integer \(n\ge2\) and real parameter \(\lambda>0\). The function space is the real first centered Poisson chaos of these \(n\) independent variables, viewed as a subspace of \(L^6\). No normalization of the coefficients is needed because \(K_{n,\lambda}\) is homogeneous of degree zero. The lower odd-dimensional formula involves at most \((n-1)/2\) specified real cubic roots and a finite comparison of their values; no claim that a particular \(k\) always wins is needed or made.

## Proof

**1. Exact moment identity.** Write \(s_j=\sum_i a_i^j\). The cumulant generating function is
\[
\log\mathbb E e^{zF_a}=
\lambda\sum_i(e^{z a_i}-1-z a_i).
\]
Thus \(\kappa_1=0\), \(\kappa_j=\lambda s_j\) for every integer \(j\ge2\), and the moment–cumulant formula yields
\[
\mathbb EF_a^2=\lambda s_2,\quad
\mathbb EF_a^6=15\lambda^3s_2^3+15\lambda^2s_2s_4
+10\lambda^2s_3^2+\lambda s_6.
\]
Normalize \(s_2=1\). The objective becomes
\[
J(a)=15+\frac{15}{\lambda}s_4+
\frac{10}{\lambda}s_3^2+\frac{1}{\lambda^2}s_6.
\tag{1}
\]

**2. Sharp maximum.** On the unit Euclidean sphere, \(s_4\le1\), \(s_6\le1\), and \(|s_3|\le\sum_i|a_i|^3\le1\). Therefore \(J(a)\le U_\lambda\), and equality in \(s_4\le1\) forces exactly one nonzero coordinate. That coordinate attains \(U_\lambda\).

**3. Even-dimensional minimum.** Hölder or power-mean inequalities give \(s_4\ge1/n\) and \(s_6\ge1/n^2\). Dropping the nonnegative \(s_3^2\) term gives the stated lower bound. Equality in both power-mean inequalities forces \(|a_i|=1/\sqrt n\) for every \(i\), and \(s_3=0\) forces exactly \(n/2\) signs of each kind. Such coefficients exist precisely for even \(n\).

**4. No zero coordinates at a minimum.** A global minimum exists by compactness of the Euclidean unit sphere. Suppose \(a_h=0\). Choose a nonzero coordinate \(a_j\) with \(s_3 a_j^3\ge0\), possible because \(\sum_j s_3 a_j^3=s_3^2\ge0\). Perturb \(a_j\) to \(a_j\sqrt{1-\varepsilon^2}\) and \(a_h\) to \(\varepsilon|a_j|\), preserving \(s_2=1\). In the expansion of (1), the coefficient of \(\varepsilon^2\) is
\[
-\frac{30}{\lambda}a_j^4
-\frac{30}{\lambda}s_3a_j^3
-\frac{3}{\lambda^2}a_j^6<0.
\]
This contradicts minimality. Thus all coordinates of every minimizer are nonzero.

**5. Exactly two coefficient levels.** A vector whose nonzero coefficients all have the same sign cannot minimize: changing the sign of any one coordinate strictly decreases \(s_3^2\) and leaves the other terms unchanged. At a constrained stationary point of (1), differentiating \(J-\mu(s_2-1)\) and dividing by \(a_i\ne0\) gives
\[
q(a_i):=\frac{6}{\lambda^2}a_i^4
+\frac{60}{\lambda}a_i^2+\frac{60}{\lambda}s_3a_i=2\mu.
\]
Summing the undivided stationarity equations after multiplying by \(a_i\) shows \(\mu>0\). The function \(q\) is strictly convex on the whole real line, because
\[
q''(x)=\frac{72}{\lambda^2}x^2+\frac{120}{\lambda}>0.
\]
Since \(q(0)=0<2\mu\) and \(q(x)\to\infty\) as \(|x|\to\infty\), the equation \(q(x)=2\mu\) has exactly one positive and one negative real solution. Every minimizer therefore has \(k\) positive coordinates of one magnitude and \(\ell=n-k\) negative coordinates of one magnitude, with both multiplicities positive. Global sign reversal allows \(k\le\ell\). Writing the positive value as \(t b\) and the negative value as \(-b\), with \(b=(kt^2+\ell)^{-1/2}\), gives \(J=H_{k,\ell,\lambda}(t)\), the displayed formula with \(t\) in place of its root.

**6. Exact one-variable minimization.** Put \(D=kt^2+\ell\). Direct differentiation yields
\[
\frac{d}{dt}H_{k,\ell,\lambda}(t)=
\frac{6k\ell\,t(t+1)P_{k,\ell,\lambda}(t)}{\lambda^2D^4}.
\tag{2}
\]
For \(k\le\ell\), expand
\[
P_{k,\ell,\lambda}(t)=
(t-1)(t^2+1)+10\lambda\bigl[k(2t^3-t^2)+\ell(t-2)\bigr].
\]
For \(0<t<1\), \(2t^3-t^2\le t\), so the bracket is at most \((k+\ell)t-2\ell\le k-\ell\le0\). Thus \(P(t)<0\) on \((0,1)\). For \(t\ge1\),
\[
P'(t)=3t^2-2t+1+10\lambda\bigl[k(6t^2-2t)+\ell\bigr]>0.
\]
If \(k<\ell\), then \(P(1)=10\lambda(k-\ell)<0\) and \(P(t)\to\infty\), yielding a unique root \(t>1\) at which \(H\) attains its unique global minimum. If \(k=\ell\), the sole root is \(t=1\). This proves the cubic description and every possible equality family. Taking the least of the finitely many admissible multiplicities proves the odd-dimensional formula. The finite comparison deliberately remains explicit in the definition, without assuming an unproved universal winning multiplicity.

**7. Full interval.** The ratio is continuous on the connected sphere \(\{a\in\mathbb R^n:s_2=1\}\) for every \(n\ge2\). Its image is therefore an interval, and the attained endpoints show it is exactly the claimed closed interval.

## Verification

Running `python check_poisson6.py` (Python 3 with SymPy) checks the polynomial derivative identity exactly, reconstructs the sixth central moment by a separate Bell-cumulant recurrence for hundreds of rational coefficient examples, and tests endpoint witnesses and finite diagnostics. The computational checks are not the proof of the arbitrary-dimensional optimization; that proof is Steps 1–7 above. For illustration, when \(n=3\) and \(\lambda=1\), the one cubic gives \(t=1.1431182544\ldots\) and \(L_{3,1}=20.2739483813\ldots\), while \(U_1=41\).

## Relationship to prior work

The Poisson Fock-space construction and finite-atom first chaos are classical; see Last and Penrose (2009). Privault (2012) gives general Poisson-integral moment identities from which Step 1 is a specialization. Dirksen (2012) proves broad two-sided \(L^p\) comparisons for Poisson stochastic integrals and independently centered summands, but his comparison constants are not the exact finite-dimensional direction-dependent endpoints. The contribution here is the **global sharp coefficient optimization**, two-level rigidity, even/odd equality geometry, and finite cubic procedure in all odd dimensions. No claim is made that the cumulant formula itself is new.

## Limitations

For odd \(n\), the exact answer is a minimum over finitely many explicitly specified cubic values; it is not asserted that the closest-to-balanced multiplicity wins for every parameter. The coefficient-level classification follows analytically but has not been independently audited. This result does not address unequal Poisson intensities, complex coefficients, higher chaos orders, or general noninteger exponents. A not-indexed equivalent coefficient-optimization theorem remains a bibliographic risk.

## References

1. G. Last and M. D. Penrose, *Poisson process Fock space representation, chaos expansion and covariance inequalities*, arXiv:0909.3205, first posted 2009-09-17. https://arxiv.org/abs/0909.3205
2. N. Privault, *Moments of Poisson stochastic integrals with random integrands*, arXiv:1204.4854, first posted 2012-04-22. https://arxiv.org/abs/1204.4854
3. S. Dirksen, *Itô isomorphisms for \(L^p\)-valued Poisson stochastic integrals*, arXiv:1208.3885, first posted 2012-08-19. https://arxiv.org/abs/1208.3885
