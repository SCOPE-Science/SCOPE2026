# Integer-ratio smoothness thresholds in two-stage random sequential adsorption

## Finding

Let an infinite one-dimensional lattice be saturated first by irreversible random sequential adsorption (RSA) of rods covering \(K\) consecutive sites, and then by RSA of rods covering \(k\) consecutive sites in the remaining vacancies. The first stage ends before the second begins. For each fixed real \(L>1\), take the limits of expected covered-site fraction in the order: lattice length \(n\to\infty\), followed by \(k\to\infty\) with \(K=\lfloor Lk\rfloor\). The limit \(\Phi(L)\) exists for **every** \(L>1\), including ratios exceeding two.

Write
\[
E(z)=\exp\!\left(-2\int_0^z\frac{1-e^{-t}}t\,dt\right),\qquad
m_\infty=\int_0^\infty E(z)\,dz,
\]
and let \(C(y)\) be the expected number of unit rods in a separate finite *continuum* RSA interval of length \(y\). Then
\[
\boxed{\displaystyle
\Phi(L)=m_\infty+\frac{2}{L^2}\int_1^L C(y)
   \left(\int_0^\infty z e^{-zy/L}E(z)\,dz\right)dy.}
\]
The function \(\Phi\) is real analytic on each open interval \((m,m+1)\) for integer \(m\ge1\). At **every** integer \(m\ge2\), it has \(m-1\) continuous derivatives through \(m\), but its \(m\)-th one-sided derivatives have the strictly positive finite jump
\[
\boxed{\displaystyle
\Phi^{(m)}(m+)-\Phi^{(m)}(m-)=
\frac{2^m}{m^2(m-1)!}\,\int_0^\infty z e^{-z}E(z)\,dz>0.}
\]
Here derivatives at an integer are understood as the corresponding limits from the adjacent open intervals. Thus the first new multi-rod deposition channel appears as a discontinuity of the second derivative at ratio two, followed by third-, fourth-, and successively higher-order discontinuities at ratios three, four, and so on.

## Assumptions and scope

All rods are hard, nonoverlapping and immobile after acceptance. At each stage the next accepted placement is uniform among the currently admissible consecutive-site intervals; repeated attempts give the same accepted-placement law. The length \(n\) is sent to infinity **before** the rod lengths; both positive integers \(k\) and \(K\) grow with fixed ratio \(K/k\to L>1\). This is the *large-first, small-second* protocol (Model I), not simultaneous mixed-size adsorption. We study the expectation of final covered-site fraction, not its sample-to-sample fluctuations or adsorption time.

Define \(C(y)=0\) for \(0\le y<1\), \(C(y)=1\) for \(1\le y\le2\), and recursively for \(y>1\) by
\[
 C(y)=1+\frac{2}{y-1}\int_0^{y-1}C(v)\,dv.
\]
The formula at \(y=1\) is taken by continuity from the right. The recursion is the first-accepted-placement decomposition of finite-interval continuum RSA. It defines a finite, bounded-by-\(y\), continuous function on \([1,\infty)\) and is smooth between positive integers. For example, \(C(y)=1+2(y-2)/(y-1)\) on \((2,3)\).

## Proof

**1. Exact discrete first-stage decomposition.** For a first-stage rod length \(K\), write \(g_{K,\ell}\) for the expected number per original lattice site of maximal vacant gaps of \(\ell\) sites, where \(0\le\ell<K\). The exact gap formula (Pinsky, Theorem 2) is
\[
 g_{K,\ell}=2\int_0^1(1-s)s^\ell H_K(s)\,ds,
 \quad H_K(s)=\exp\!\left(2\sum_{j=1}^{K-1}\frac{s^j-1}{j}\right).
\]
Let \(M_k(\ell)\) be the mean *number of occupied sites*, rather than the number of rods, in RSA of \(k\)-rods on an interval of \(\ell\) sites. By conditioning on the first accepted placement,
\[
 M_k(\ell)=0\quad(\ell<k),\qquad
 M_k(\ell)=k+\frac2{\ell-k+1}\sum_{v=0}^{\ell-k}M_k(v)
 \quad(\ell\ge k).
\]
The first-stage covered fraction is \(m_K=K\int_0^1 H_K(s)\,ds\). The exact infinite-substrate two-stage coverage (Pinsky, Theorem 4) is therefore
\[
 m_{k,K;I}=m_K+\sum_{\ell=k}^{K-1}g_{K,\ell}M_k(\ell).
\]
These are exact identities, not numerical approximations.

**2. Scaling each ingredient.** The known parking limit gives \(m_K\to m_\infty\). The recurrence for \(M_k\), after division by \(k\) and Riemann-sum approximation, gives
\[
 \frac{M_k(\lfloor ky\rfloor)}k\longrightarrow C(y)
\]
for every \(y>1\), by induction on the successive strips \((j,j+1)\). Specifically the base strip \((1,2)\) has one rod, and the next strip inherits convergence from the already established smaller arguments via the displayed recurrence; convergence is locally uniform away from the integer strip boundaries. The bound \(0\le M_k(\ell)\le\ell\) controls the omitted boundary layers.

For \(\ell/K\to a\in(0,1]\), substitute \(s=e^{-z/K}\) into the exact gap integral. Then
\[
 K^2g_{K,\ell}\longrightarrow
 2\int_0^\infty z e^{-az}E(z)\,dz=:G(a).
\]
Indeed \(H_K(e^{-z/K})\to E(z)\), \(K(1-e^{-z/K})\to z\), and \((e^{-z/K})^\ell\to e^{-az}\). On every compact interval \(a\ge a_0>0\), the integrand is dominated by a constant multiple of \(z e^{-a_0z/2}\), using \(0<H_K\le1\); truncation and dominated convergence give the stated uniformity. In the two-stage sum, \(\ell/K\ge k/K\to1/L>0\), so this uniformity applies. There are asymptotically \(k\,dy\) gaps with \(\ell/k\in[y,y+dy]\), and \(K^2\sim L^2k^2\); hence the gap sum converges by a bounded Riemann sum to
\[
 \frac1{L^2}\int_1^L C(y)G(y/L)\,dy,
\]
which is the claimed all-ratio formula. The exact choice of floor at \(K=\lfloor Lk\rfloor\) does not change the limit.

**3. The integer smoothness hierarchy.** Differentiate the finite-interval RSA recursion away from integers:
\[
 (y-1)C'(y)+C(y)=1+2C(y-1).
\]
The base jump in the *function* at \(1\) is \(\Delta C(1)=1\). Inductively, \(C\) is continuous at every integer \(m\ge2\), and its first discontinuous derivative there is the derivative of order \(m-1\). Differentiate the above identity \(m-2\) times, take right-minus-left limits at \(y=m\), and use continuity of all lower derivatives. With \(d_m=\Delta C^{(m-1)}(m)\),
\[
 (m-1)d_m=2d_{m-1},\quad d_1=1,
 \qquad\Longrightarrow\qquad d_m=\frac{2^{m-1}}{(m-1)!}.
\]
This method of steps also proves piecewise analyticity of \(C\). Define the smooth, positive kernel
\[
 w(L,y)=\frac{2}{L^2}\int_0^\infty z e^{-zy/L}E(z)\,dz.
\]
For \(L\) near a fixed integer \(m\ge2\), differentiation of \(\Phi(L)=m_\infty+\int_1^L w(L,y)C(y)\,dy\) by the Leibniz rule shows that derivatives below order \(m\) match across \(m\). The sole possible jump in the \(m\)-th derivative comes from the boundary term \(w(m,m)C^{(m-1)}(m\pm)\); all other terms contain lower continuous derivatives or smooth integrals. Because
\[
 w(m,m)=\frac{2}{m^2}\int_0^\infty z e^{-z}E(z)\,dz,
\]
its jump is \(w(m,m)d_m\), exactly the expression in the Finding. The integral is strictly positive and finite. Analyticity follows on each open interval by the same method of steps and differentiation of the exponentially convergent kernel integrals.

**4. The first threshold and consistency with the prior small-ratio formula.** Put
\[
 \Psi(L)=m_\infty+\frac2L\int_0^\infty (e^{-z/L}-e^{-z})E(z)\,dz.
\]
When \(1<L\le2\), \(C(y)=1\) throughout the integration range; performing the inner \(y\)-integral gives \(\Phi(L)=\Psi(L)\), the previously derived Theorem 8 expression. When \(L>2\), \(C(y)>1\) on \((2,L)\), and \(\Phi(L)>\Psi(L)\). As \(L\downarrow2\) from above, \(C(2+h)=1+2h+O(h^2)\) and the kernel is smooth, so
\[
 \Phi(L)-\Psi(L)
 =\frac12\!\left(\int_0^\infty z e^{-z}E(z)\,dz\right)(L-2)^2
 +O((L-2)^3).
\]
This independently recovers the \(m=2\) derivative jump.

## Verification

The included `CHECK.py` recomputes the finite-interval discrete recurrence, the exact first-stage gap integrals, the all-ratio continuum expression, and the restricted \(L\le2\) expression. Representative values are \(m_\infty\approx0.747597920253\), \(\Phi(2)\approx0.852335031343\), \(\Phi(2.5)\approx0.866054359924\), \(\Phi(3)\approx0.877826189789\), and \(I:=\int_0^\infty ze^{-z}E(z)dz\approx0.157618375844\). The derivative jumps for ratios \(2\), \(3\), \(4\) are approximately \(0.157618375844\), \(0.070052611486\), \(0.026269729307\). Discrete finite-rod computations converge toward the corresponding continuum values. These checks are diagnostic; the proof of existence and of every integer jump is the preceding analytic argument, not the finite computations.

Run `python CHECK.py` with Python 3, NumPy and SciPy installed. The script uses bounded numerical integration and finite recurrences; it does not claim numerical verification of an infinite statement.

## Relationship to prior work

Pinsky, *A new look at some aspects of one-dimensional random sequential adsorption and its continuum limit* (arXiv:2608.04730v1, August 5, 2026) establishes the exact discrete gap law (Theorem 2), the staged finite-rod formula (Theorem 4), and the continuum ratio \(1<L\le2\) formula (Theorem 8). That paper explicitly poses the behavior for \(L>2\) as further study. The new statement here is the **all-fixed-ratio limit plus complete integer-order differentiability classification and exact jump coefficients**; the basic gap law and \(L\le2\) result are not asserted as new.

Hassan, Schmidt, Blasius and Kurths, *Jamming coverage in competitive random sequential adsorption of a binary mixture* (arXiv:cond-mat/0110036), treat continuously competing arrival species, a different deposition protocol, and explicitly focus on size ratios at most two in their explicit formula. Reeve and Wattis, *Random sequential adsorption with two components: asymptotic analysis and finite size effects*, analyze competitive binary polymer binding for different length regimes; their numerical recurrences and asymptotic discussion, including the small-short-species-arrival regime, do not establish the sequential fixed-ratio continuum function or the integer-order smoothness hierarchy. The standard single-length parking limit and finite-interval recurrence are classical inputs. Exact finite discrete formulas do not by themselves give the all-ratio scaling theorem or the differentiability hierarchy without the limiting and regularity arguments given here.

## Limitations

The order of the two limits is essential and no assertion is made for simultaneous growth of substrate and rod lengths. Only the sequential Model I protocol is addressed; its simultaneously mixed Model II counterpart is not solved. The result concerns expected terminal coverage only. The integer-order jump formula is an analytic singularity, not a discontinuity in the covered fraction itself, and does not predict finite-size singularities. Possible equivalent earlier formulations under different adsorption terminology remain a bibliographic risk; no independent validation or external scientific audit is claimed.

## References

1. R. G. Pinsky, *A new look at some aspects of one-dimensional random sequential adsorption and its continuum limit*, arXiv:2608.04730v1 (first public August 5, 2026), especially Theorems 1, 2, 4 and 8 and the open-ratio remark, https://arxiv.org/pdf/2608.04730.
2. M. K. Hassan, J. Schmidt, B. Blasius and J. Kurths, *Jamming coverage in competitive random sequential adsorption of a binary mixture*, arXiv:cond-mat/0110036v2 (2001), https://arxiv.org/pdf/cond-mat/0110036.
3. L. Reeve and J. A. D. Wattis, *Random sequential adsorption with two components: asymptotic analysis and finite size effects*, https://nottingham-repository.worktribe.com/OutputFile/751795.
4. A. Rényi, *On a one-dimensional problem concerning random space-filling*, Publications of the Mathematical Institute of the Hungarian Academy of Sciences 3 (1958), 109–127 (classical one-size parking problem).
