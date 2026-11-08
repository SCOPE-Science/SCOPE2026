# An exact periodic-orbit census for reversible finite-field waves on cycles

## Finding
Let \(n\geq3\), let \(\mathbb F_q\) be a finite field of characteristic \(p\), and let \(S\) rotate the coordinates of \(\mathbb F_q^n\) cyclically. Set \(A=S+S^{-1}\) and define the reversible synchronous wave
\[
T(u,v)=(Au-v,u),\qquad (u,v)\in\mathbb F_q^n\times\mathbb F_q^n.
\]
For every integer \(k\geq1\), put \(g=\gcd(n,k)\), and let \(\nu_p(a)\) denote the exponent of \(p\) dividing a positive integer \(a\). Define
\[
\delta_p(n,k)=
\begin{cases}
\bigl(1+\mathbf1_{2\mid g}\bigr)\mathbf1_{\nu_p(n)=\nu_p(k)},&p\ne2,\\
\mathbf1_{k\text{ odd}},&p=2\text{ and }n\text{ odd},\\
0,&p=2\text{ and }n\text{ even}.
\end{cases}
\]
Then the exact fixed-point population of the \(k\)th iterate is
\[
\boxed{\#\operatorname{Fix}(T^k)=q^{\,2\gcd(n,k)-\delta_p(n,k)}.}
\]
The least positive integer \(L\) with \(T^L=I\) is exactly
\[
\boxed{L=\begin{cases}pn,&p\ne2,\\2n,&p=2,\ n\text{ odd},\\n,&p=2,\ n\text{ even}.\end{cases}}
\]
For every \(k\mid L\), the number of points with *least* period \(k\) equals
\[
\boxed{P_k=\sum_{d\mid k}\mu(k/d)q^{\,2\gcd(n,d)-\delta_p(n,d)}},
\]
with exactly \(P_k/k\) distinct temporal orbits. For \(k\nmid L\), there are no points of least period \(k\). In particular, the order loses a factor of two in characteristic two exactly on even cycles; the fixed-point populations simultaneously exhibit a resonance correction at one or two spatial characters.

## Assumptions and scope
The cycle is the **simple** undirected graph \(C_n\), with \(n\ge3\); it has two distinct neighbors at every vertex. All arithmetic is in the finite field \(\mathbb F_q\), and no field restriction beyond prime-power \(q=p^f\), \(f\ge1\), is needed. The phase space consists of ordered pairs of consecutive configurations, not a single binary configuration. The second component updates by copying the first, and the minus sign is essential except in characteristic two. All stated fixed points are immediate, not asymptotic; the system is bijective, so it has no transient states. The inverse is \(T^{-1}(u,v)=(v,Av-u)\).

## Proof
Work over an algebraic closure \(K\) of \(\mathbb F_q\), which leaves matrix ranks unchanged. Identify the position module with \(R=K[z,z^{-1}]/(z^n-1)\); rotation is multiplication by \(z\). The time update acts on the free rank-two \(R\)-module with matrix \(\left(\begin{smallmatrix}z+z^{-1}&-1\\1&0\end{smallmatrix}\right)\). Equivalently, writing \(t\) for its action, this module is \(R[t]/((t-z)(t-z^{-1}))\), with basis \(1,t\) over \(R\). The change of basis is invertible over every extension field.

Write \(n=p^\alpha n_0\) with \(p\nmid n_0\). Since \(z^n-1=(z^{n_0}-1)^{p^\alpha}\), the position ring splits into local factors \(R_\zeta=K[\epsilon]/(\epsilon^s)\), with \(z=\zeta+\epsilon\), \(s=p^\alpha\), indexed by the \(n_0\) distinct roots \(\zeta^{n_0}=1\).

If \(\zeta\ne\zeta^{-1}\), the difference \(z-z^{-1}\) is a unit in \(R_\zeta\); the Chinese remainder theorem in \(t\) diagonalizes the temporal action into multiplications by \(z\) and \(z^{-1}\) on separate copies of \(R_\zeta\). Let \(\beta=\nu_p(k)\). If \(\zeta^k\ne1\), neither contributes fixed vectors. If \(\zeta^k=1\), the polynomial \((\zeta+\epsilon)^k-1\) has zero of order precisely \(p^\beta\) in \(\epsilon\), giving \(2\min(s,p^\beta)\) fixed dimensions. The same conclusion holds for the second, inverse, branch.

At a resonant root \(\zeta=\zeta^{-1}\), necessarily \(\zeta=\pm1\) (only \(\zeta=1\) in characteristic two), put \(y=t-\zeta\). Directly from \((t-z)(t-z^{-1})=0\) one obtains the exact local identity \(y^2=\epsilon^2t/z\). The factor \(t/z\) is a unit. If \(s=1\), multiplication by \(y\) is a single nilpotent Jordan block of size two. For \(s>1\), its kernel has dimension two: in the basis \(1,t\), the determinant of multiplication by \(y\) is a unit times \(\epsilon^2\), and its reduction modulo \(\epsilon\) has rank one, giving elementary divisors \(1,\epsilon^2\) over the local principal ideal ring. The identity for \(y^2\) gives the maximal block sizes: for odd \(p\) (thus odd \(s\)), they are \(s+1\) and \(s-1\) (with the zero-size block omitted when \(s=1\)); for \(p=2\) and \(s\ge2\), they are \(s,s\). This follows since \(y^{2j}=\epsilon^{2j}(t/z)^j\) and \(y^{2j+1}=\epsilon^{2j}(t/z)^j y\), with the last nonzero odd power detected by its \(t\)-coefficient.

When \(\zeta^k=1\), the nilpotent kernel of \(t^k-1\) on any Jordan block of size \(h\) is of dimension \(\min(h,p^\beta)\), because \(k=p^\beta k_0\) with \(p\nmid k_0\). Thus the resonant contribution is \(2\min(s,p^\beta)-1\) exactly when \(p\ne2\) and \(\beta=\alpha\), or when \(p=2,s=1,\beta=0\); otherwise it is \(2\min(s,p^\beta)\). If \(\zeta^k\ne1\), it contributes zero.

There are exactly \(h=\gcd(n_0,k/p^\beta)\) roots \(\zeta\) of \(z^{n_0}-1\) with \(\zeta^k=1\). The baseline sum is \(2h\min(p^\alpha,p^\beta)=2\gcd(n,k)\). For odd \(p\), \(\zeta=1\) always contributes one defect when \(\alpha=\beta\), and \(\zeta=-1\) contributes a second precisely when \(n,k\) are both even (equivalently \(2\mid g\)). In characteristic two, a single defect occurs exactly when \(n\) and \(k\) are both odd. This proves the displayed dimension formula; \(q\) raised to this dimension counts the fixed vectors.

The dimension is \(2n\) precisely when all \(n_0\) spatial roots contribute, \(p^\beta\ge p^\alpha\), and no resonance defect survives. These are exactly the stated divisibility conditions for \(L\); hence the displayed \(L\) is the **least** global period. Finally, fixed-point populations of powers are sums of primitive-period populations indexed by divisors. Möbius inversion proves the formula for \(P_k\), including its orbit quotient.

## Verification
The accompanying `verify_matrix.py` constructs the \(2n\)-dimensional update over prime fields and calculates \(\dim\ker(T^k-I)\) using exact modular Gaussian elimination. It verifies 1,235 triples \((n,p,k)\) for \(3\le n\le12\), \(p\in\{2,3,5,7\}\), and all \(1\le k\le L\), including \(T^L=I\). `verify_enumeration.py` independently applies the update to every state on selected small cycles and checks 103,788 configurations and 36 fixed-point totals. The two scripts use only Python's standard library; captured exact outputs are supplied. These finite checks support, but do not replace, the general proof.

## Relationship to prior work
Classical reversible second-order cellular automata are treated by Macfarlane (2004), including matrix equivalents for three binary rules; the reported objects are weights of patterns evolved from selected seeds, not the all-initial-pair finite-ring fixed-point spectra, arbitrary-field formula, or characteristic-two ring parity transition here. Steeb and Hardy (2007) give the general reversible subtraction construction and a different wave rule containing a center term, without this exact census. Schumacher and Werner (2004) analyze structural reversibility of quantum cellular automata and finite periodic boundaries, without addressing this classical finite-field orbit census. These works motivate and partly subsume the reversible *construction*, not the stated counting formulas.

## Limitations
The theorem applies only to the two-time-level linear nearest-neighbor wave and simple cycles; it does not classify general nonlinear second-order rules, open paths, or graph Laplacian waves with other coefficients. Finite computational tests do not establish the theorem independently. A full text of Macfarlane (2004) was not accessible at preparation time, although its abstract and full bibliographic details were examined; hidden equivalent finite-ring orbit formulas in that source or unindexed literature remain a genuine originality risk. No independent expert audit was conducted.

## References
- A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, Journal of Physics A 37 (2004), 10791–10814. DOI: 10.1088/0305-4470/37/45/006.
- W.-H. Steeb and Y. Hardy, *One-Dimensional Cellular Automata, Conservation Laws and Partial Differential Equations*, Zeitschrift für Naturforschung A 62 (2007), 569–572. DOI: 10.1515/zna-2007-10-1103.
- B. Schumacher and R. F. Werner, *Reversible quantum cellular automata*, preprint dated 2004-05-28, arXiv:quant-ph/0405174v1.
- A. Nobe and F. Yura, *On reversibility of cellular automata with periodic boundary conditions*, Journal of Physics A 37 (2004), 5789–5804. DOI: 10.1088/0305-4470/37/22/006.
