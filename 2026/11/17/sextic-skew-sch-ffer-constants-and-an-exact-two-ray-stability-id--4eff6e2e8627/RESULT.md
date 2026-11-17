# Sextic skew-Schäffer constants and an exact two-ray stability identity on real \(L^6\)

## Finding
Let \(X=L^6(\Omega,\mu;\mathbb R)\) have dimension at least two and \(\tau\ge0\). For unit vectors \(x,y\in X\), define
\[
\Phi_\tau(x,y)=\tfrac12\big(\|x+\tau y\|_6^6+\|\tau x-y\|_6^6\big),\qquad
\mathcal J_6(\tau)=\sup\Phi_\tau(x,y)^{1/6},\quad
\mathcal S_6(\tau)=\inf\Phi_\tau(x,y)^{1/6}.
\]
For \(\tau>0\), set
\[
A=15\tau^2(1+\tau^2),\quad B=6\tau(1-\tau^4),\quad
L=\frac{A+\sqrt{A^2+B^2}}2>0,\quad N=1+\tau^6+L,\quad c=1+\tau^2,
\quad\gamma=\frac B{2L}.
\]
Then the **closed, attained values** are
\[
\boxed{\mathcal J_6(\tau)=N^{1/6},\qquad \mathcal S_6(\tau)=cN^{-1/6}.}\tag{1}
\]
Their novelty here is accompanied by an **exact global nonnegative deficit** for arbitrary, not necessarily normalized, real \(x,y\in X\):
\[
\boxed{N(\|x\|_6^6+\|y\|_6^6)-\|x+\tau y\|_6^6-\|\tau x-y\|_6^6
=L\int_\Omega (x^2+y^2)(x^2-y^2-\gamma xy)^2\,d\mu.}\tag{2}
\]
Consequently, every unit upper extremizer has, almost everywhere, its pointwise pair \((x,y)\) on **exactly two mutually perpendicular real lines** \(y=sx\) and \(y=-x/s\), where
\[
s=\frac{\sqrt{\gamma^2+4}-\gamma}{2}>0.
\]
For \(\tau\ne1\), both branches must be used and their \(x\)-sixth-power masses are exactly \(1/(1+s^6)\) and \(s^6/(1+s^6)\), respectively. When \(\tau=1\), \(s=1\) and \(|x|=|y|\) almost everywhere, with arbitrary mass allocation between the two signs. Every such pair is extremizing.

There is also an exact **lower-endpoint deficit**. If \(u=x+\tau y\) and \(v=\tau x-y\), then
\[
\boxed{\|x+\tau y\|_6^6+\|\tau x-y\|_6^6-\frac{c^6}{N}(\|x\|_6^6+\|y\|_6^6)
=\frac L N\int_\Omega(u^2+v^2)(u^2-v^2-\gamma uv)^2\,d\mu.}\tag{3}
\]
The unit lower extremizers are exactly those for which \((x+\tau y,\tau x-y)\) lies on the same two-line cone almost everywhere; at \(\tau=1\), this means disjoint support. Both endpoint extremizers exist in every such \(X\).

As a quantitative consequence, let \(\mathscr C=\{(a,b)\in\mathbb R^2:a^2-b^2-\gamma ab=0\}\), and let \(d(z,\mathscr C)\) be Euclidean distance to this union of two lines. Put \(\kappa^2=1+\gamma^2/4\). Then every unit pair satisfies
\[
\boxed{N-\Phi_\tau(x,y)\ge L\kappa^2\int_\Omega (x^2+y^2)^2\,d((x,y),\mathscr C)^2\,d\mu.}\tag{4}
\]
The coefficient in the underlying pointwise distance inequality is optimal, with equality on the two eigenvector lines of the quadratic form. The coefficient is **not asserted to be the best** when globally restricted to two unit functions. At \(\tau=0\), both constants are one and every unit pair realizes both endpoints.

## Assumptions and scope
All scalar functions are real; the ambient measure space may be finite or infinite, atomic or nonatomic, provided that \(X\) has dimension at least two. There is no separability or probability normalization hypothesis. The two endpoints in (1) are for outer power exponent exactly six. The sharp pointwise stability statement is not a distance bound to the globally normalized set of extremizers. No assertion about complex \(L^6\) or exponents other than six is made.

## Proof
**Step 1: an exact scalar identity.** For real \(a,b\), binomial expansion yields
\[
(a+\tau b)^6+(\tau a-b)^6
=(1+\tau^6)(a^6+b^6)+A(a^4b^2+a^2b^4)+B(a^5b-ab^5).
\]
The defining positive root \(L\) obeys \(L^2-AL-B^2/4=0\). Expanding the square and using this single quadratic relation gives the polynomial identity
\[
N(a^6+b^6)-(a+\tau b)^6-(\tau a-b)^6
=L(a^2+b^2)(a^2-b^2-\gamma ab)^2.\tag{5}
\]
For \(\tau>0\), \(A>0\) and \(L>0\), so (5) gives a pointwise sharp upper bound on the \(\ell_6^2\)-operator norm of \(T_\tau=\begin{psmallmatrix}1&\tau\\\tau&-1\end{psmallmatrix}\), with \(\|T_\tau\|^6\le N\). The homogeneous quadratic \(a^2-b^2-\gamma ab\) has two distinct real perpendicular null lines because its slope roots have product \(-1\). At any nonzero vector on either null line (5) is equality, proving \(\|T_\tau\|^6=N\) exactly.

**Step 2: normed functions and sharp attainment.** Integrate (5). Hölder's inequality guarantees integrability of every term, producing (2). For unit \(x,y\), its left side is \(2(N-\Phi_\tau(x,y))\), so the upper bound is \(N\). Choose disjoint unit functions \(f,g\in X\), which exist whenever \(\dim X\ge2\). Write
\[
\alpha=(1+s^6)^{-1/6},\qquad \beta=s(1+s^6)^{-1/6},\qquad
x=\alpha f+\beta g,\qquad y=s\alpha f-\beta g/s.
\]
These functions both have sixth-power norm one and satisfy the quadratic cone equation pointwise. Thus \(\Phi_\tau(x,y)=N\), proving upper attainment. Conversely, nonnegativity in (2) forces that equation almost everywhere. For \(\tau\ne1\), the unit constraints force \(U+V=1\), \(s^6U+s^{-6}V=1\) for the sixth-power \(x\)-masses on each branch, giving \(U=1/(1+s^6)\) and \(V=s^6/(1+s^6)\). For \(\tau=1\), the two branch ratios have absolute value one, so the unit constraints impose no branch split. The converse is direct.

**Step 3: infimal identity and attainment.** The matrix satisfies \(T_\tau^2=cI\). Apply the scalar identity (5) to \(T_\tau(a,b)/c\), multiply by \(c^6/N\), and integrate. The result is exactly (3). It implies \(\Phi_\tau(x,y)\ge c^6/N\) on unit pairs. For the upper-extremizing pair \(x_+,y_+\) constructed above, the disjoint-support form makes both \(x_++\tau y_+\) and \(\tau x_+-y_+\) have norm \(N^{1/6}\): the two output norms coincide because the two input coordinate patterns are quarter-turn partners under \(T_\tau\). Consequently
\[
x_-=(x_++\tau y_+)/N^{1/6},\qquad y_-=(\tau x_+-y_+)/N^{1/6}
\]
are unit functions and \(T_\tau(x_-,y_-)=(c/N^{1/6})(x_+,y_+)\), establishing the exact lower endpoint and its attainment. Equality in (3) is equivalent to the stated transformed-cone condition, completing its classification.

**Step 4: sharp pointwise stability.** The quadratic form \(q(a,b)=a^2-b^2-\gamma ab\) corresponds to a real symmetric trace-zero matrix with eigenvalues \(\pm\kappa\). An orthogonal change of coordinates turns it into \(\kappa(r^2-t^2)\), with its zero cone consisting of \(r=\pm t\). The distance \(d\) to this cone obeys \(2d^2=(|r|-|t|)^2\), while
\[
q^2=\kappa^2(|r|-|t|)^2(|r|+|t|)^2
\ge 2\kappa^2(r^2+t^2)d^2.
\]
The coefficient is attained for nonzero pairs along either eigenvector of the quadratic form. Substitution in (2), followed by dividing by two for unit functions, proves (4). At \(\tau=0\), \(T_0\) is the diagonal sign involution, so both endpoints equal one without using the definitions involving \(L^{-1}\).

## Verification
The file `sextic_check.py` symbolically verifies the sextic expansion, reduces the square identity to the defining quadratic for \(L\), and checks the scaled involution exactly. It also runs 3,000 finite floating-point identities, seven explicit two-atom upper/lower optimizers and three pointwise sharpness probes. Run `python sextic_check.py` with SymPy installed. Those finite computations are consistency tests only; the identity (5) and its integrated consequences are the proofs for all real parameters and measure spaces.

## Relationship to prior work
Xu and Liu (2026), Theorem 3.2 and Remark 3.3, already established the **general** reduction of the real \(L^p\) skew Schäffer and skew James constants to the norm of \(T_\tau\), together with a one-variable maximization, so that reduction and the abstract product relation are **not new**. Their paper gives elementary constants at the endpoint exponents, \(p=2\), and \(\tau=1\), but does not evaluate the sextic maximization to the closed radical (1), provide the full sextic identities (2)–(3), or classify all sextic norming pairs and the two-ray stability modulus. Rao et al. (2025) introduce the skew James invariant and basic Banach-space relations but do not obtain the stated real \(L^6\) structural identity. An accessible published quartic finding gives a distinct fourth-power two-ray rigidity and stability law, and another gives a large-\(p\) asymptotic for the same matrix; neither determines this exact exponent-six polynomial and extremizers. The theorem is an explicit algebraic completion of a natural exact invariant, **not** a new definition or a reformulation of the general reduction.

## Limitations
The proof concerns only real functions and the sixth power; the parameter \(\tau=0\) is degenerate. An older equivalent sextic Clarkson-type or matrix-norm polynomial certificate could have been missed despite targeted searches. The dependence on Xu and Liu's general norm reduction for historical context is explicit; the calculations and proofs here are self-contained. The pointwise sharpness of (4) is not claimed to be the global best constant under unit normalization. No independent external audit or absolute priority certification has been performed.

## References
1. Y. Xu and Q. Liu, *Skew Schäffer Type Constants*, arXiv:2610.03050v1, 2 October 2026, https://arxiv.org/html/2610.03050v1 .
2. Z. Rao, Q. Liu, Q. Wu, Z. Yin and Q. Ni, *The skew James type constant in Banach spaces*, arXiv:2504.00827v1, 31 March 2025, https://arxiv.org/html/2504.00827v1 .
3. J. A. Clarkson, *Uniformly convex spaces*, Transactions of the American Mathematical Society **40** (1936), 396–414 (general historical background on \(L^p\) power inequalities).
