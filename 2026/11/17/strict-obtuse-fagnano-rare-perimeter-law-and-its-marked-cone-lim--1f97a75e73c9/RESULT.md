# Strict-obtuse Fagnano rare-perimeter law and its marked cone limit

## Finding
Let \(ABC\) be a nondegenerate Euclidean triangle with strictly obtuse angle \(A\), let \(a=|BC|\), \(b=|CA|\), \(c=|AB|\), and let \(h=bc\sin A/a\) be the altitude from \(A\) to \(BC\). Choose points \(X\in AB\), \(Y\in AC\), and \(Z\in BC\) independently and uniformly with respect to length on their respective sides. Write \(P=|X-Y|+|Y-Z|+|Z-X|\). The smallest possible perimeter in the closure is \(2h\), uniquely achieved by the degenerate configuration \((X,Y,Z)=(A,A,H)\), where \(H\) is the foot of the altitude.

Put \(p=h/c\), \(q=h/b\), and
\[g(k)=\sqrt{1+k^2-2k\cos A}-p-qk,\qquad I_A=\int_0^\infty\frac{dk}{g(k)^2}.\]
The integral is positive and finite and the **sharp small-excess law** is
\[\boxed{\displaystyle\Pr(P<2h+t)\sim\frac{8\sqrt h}{15abc}I_A\,t^{5/2}}\qquad(t\downarrow0).\]
In particular, its exponent \(5/2\) is distinct from the smooth, interior Fagnano minimizer in an acute triangle and the singular limiting geometry at a right angle.

A stronger **marked conditional law** also holds. Measure \(u=|AX|\), \(v=|AY|\) along the two sides emanating from the obtuse vertex, and let \(w\) be the signed distance of \(Z\) along \(BC\) from \(H\). Define
\[G(U,V)=\sqrt{U^2+V^2-2UV\cos A}-pU-qV,\quad \mathcal D=\{(U,V,W):U,V\ge0,\ G(U,V)+W^2<1\}.\]
Then \(\mathcal D\) has finite positive volume \(8I_A/15\), and the conditional law of \((u/t,v/t,w/\sqrt{ht})\) given \(P<2h+t\) converges **in total variation** to normalized Lebesgue measure on \(\mathcal D\). In this limiting law \(K=V/U\) has density \(g(k)^{-2}/I_A\) on \((0,\infty)\), independently of \(S=G(U,V)\sim\operatorname{Beta}(2,3/2)\) and \(J=W/\sqrt{1-S}\sim\operatorname{Uniform}[-1,1]\). The conditional normalized excess \((P-2h)/t\) converges to \(\operatorname{Beta}(5/2,1)\).

## Assumptions and scope
The triangle is fixed and *strictly* obtuse: \(\pi/2<A<\pi\). The three samples are independent and each is arclength-uniform along its specified side, **not** drawn from the full perimeter. The normalized probability has denominator \(abc\). All limits are for \(t\to0\) at a fixed triangle; none is asserted uniformly as \(A\downarrow\pi/2\). The normalized limiting variables are defined on the rare event, with arbitrary values on null coordinate sets where needed.

## Proof
**1. Geometry and coercivity.** Orient \(BC\) as a horizontal line and place \(H\) at horizontal coordinate zero and \(A\) at \((0,h)\). Write \(X=(\tau_B u,h-pu)\), \(Y=(\tau_C v,h-qv)\), \(Z=(w,0)\), where \(\tau_B<0<\tau_C\), \(\tau_B^2+p^2=\tau_C^2+q^2=1\). The perimeter is exactly
\[P=\sqrt{(h-pu)^2+(w-\tau_Bu)^2}+\sqrt{(h-qv)^2+(w-\tau_Cv)^2}+\sqrt{u^2+v^2-2uv\cos A}.\tag{1}\]
Since the first two lengths exceed their nonnegative vertical differences, \(P-2h\ge G(u,v)\). Moreover
\[p^2+q^2=\frac{(b^2+c^2)\sin^2 A}{a^2}<1\]
because \(\cos A<0\) implies \(a^2=b^2+c^2-2bc\cos A>b^2+c^2\). Using \(\cos A<0\) and Cauchy–Schwarz gives
\[G(u,v)\ge(1-\sqrt{p^2+q^2})\sqrt{u^2+v^2}.\tag{2}\]
Consequently \(G>0\) away from the origin, \(g(k)>0\) for \(k\ge0\), and \(P\ge2h\). Equality requires \(u=v=0\), and then \(P=2\sqrt{h^2+w^2}\), forcing \(w=0\). Hence the minimizer is unique, and any event \(P-2h<t\) has \(u,v=O(t)\). Since the configuration domain is compact and the unique minimizer has \(w=0\), a Taylor inequality for the two vertical distances yields \(w=O(\sqrt t)\). These bounds hold with constants depending only on the fixed triangle.

**2. Uniform local expansion.** In the scaling \(u=tU\), \(v=tV\), \(w=\sqrt{ht}\,W\), expansion of (1) on any fixed bounded set gives
\[\frac{P-2h}{t}=G(U,V)+W^2+O(\sqrt t).\tag{3}\]
The bound (2) and the preceding coercivity bound confine the scaled rare-event sets to one common bounded set for all sufficiently small \(t\). Thus their indicators converge almost everywhere to the indicator of \(\mathcal D\), since its boundary is a null set. The original sampling measure is \(du\,dv\,dw/(abc)\), and the scaling Jacobian is \(\sqrt h\,t^{5/2}\). Dominated convergence proves the probability asymptotic and \(L^1\) convergence of the normalized conditional densities, which is precisely total-variation convergence.

**3. Exact limiting volume.** Substitute \(V=kU\) with \(U,k\ge0\). Then \(G(U,V)=U g(k)\) and \(dU\,dV=U\,dU\,dk\). The \(W\)-interval has length \(2\sqrt{1-Ug(k)}\) when \(0<U<1/g(k)\); therefore
\[\begin{aligned}
\operatorname{vol}(\mathcal D)
&=\int_0^\infty\int_0^{1/g(k)}2U\sqrt{1-Ug(k)}\,dU\,dk\\
&=2\,B(2,3/2)\int_0^\infty g(k)^{-2}\,dk
=\frac8{15}I_A.
\end{aligned}\]
The integral is finite since \(g(0)=1-p>0\), \(g(k)/k\to1-q>0\), and \(g\) is positive and continuous. Multiplying the limiting volume by \(\sqrt h/(abc)\) proves the claimed coefficient.

**4. Conditional markings.** Change variables further to \(S=Ug(k)\) and \(J=W/\sqrt{1-S}\). The Jacobian factors, producing density proportional to \(g(k)^{-2}S\sqrt{1-S}\) on \(k>0,0<S<1,-1<J<1\). This is exactly the stated independent product law; in particular \(S\) has the \(\operatorname{Beta}(2,3/2)\) law. Because the limiting deficit function \(G(U,V)+W^2\) is homogeneous of degree one under \((U,V,W)\mapsto(rU,rV,\sqrt r W)\), its sublevel volume is proportional to \(r^{5/2}\). This yields \(\operatorname{Beta}(5/2,1)\) for the normalized conditional excess. Continuity of (3) and the total-variation statement give convergence of the original markings.

## Verification
The standalone `check_obtuse_fagnano.py` evaluates the one-dimensional coefficient integral and independently computes rare-event probabilities from the **exact** Euclidean perimeter formula using 1,048,576 Sobol points per threshold. For \(A=120^\circ\) and \(b=c=1\), the limiting coefficient is \(1.3179485337782688\). At \(t=0.025,0.01,0.004,0.0016\), the observed coefficient divided by its limit was respectively \(0.90451,0.95924,0.98307,0.99313\). These are finite-resolution diagnostics, not a substitute for the analytic proof.

Run using `python check_obtuse_fagnano.py` with NumPy and SciPy installed. The proof itself uses no numerical assumption or computation.

## Relationship to prior work
Alkoumi and Schlenk, *Shortest closed billiard orbits on convex tables* (public arXiv version of 22 August 2014), Proposition 4.1(ii), identify the singular two-bounce minimizer for obtuse triangles and its length \(2h\). This fact provides the deterministic baseline; their proposition does not give the independent side-uniform perimeter distribution, its \(5/2\) rare-event coefficient, or the conditional shape law. Classical Fagnano theory treats acute triangles; the three regimes are geometrically distinct. Existing studies of random inscribed triangles concern area, containment and other metrics and do not directly supply this small-perimeter law.

## Limitations
Historical priority remains provisional, especially for terminology from random billiards, stochastic polygon geometry, and singular variational asymptotics. Independent mathematical and bibliographic validation has not been performed. The coefficient is an explicit convergent quadrature rather than a claimed elementary closed form; no right-angle or moving-angle uniformity is proved. Numerical checks only support the written proof.

## References
1. N. Alkoumi and F. Schlenk, *Shortest closed billiard orbits on convex tables*, arXiv:1408.5255 (first public version 2014-08-22), Proposition 4.1(ii), https://arxiv.org/abs/1408.5255.
2. Fagnano's classical minimum-perimeter inscribed-triangle problem (acute case; standard background).
