# A sharp finite-to-infinite inverse-valence boundary in a memristive Lozi map

## Finding
Consider the real three-dimensional map of Wang, Gu, Rong, Xu and Zhang (2022)
\[
F_{a,b,k}(x,y,z)=(1-a|x|+y,\;bx+ky\sin z,\;z+y),
\qquad a,b>0,\quad k\geq0.
\]
Put \(c=b/a\). Fix an arbitrary target \(q=(X,Y,Z)\in\mathbb R^3\), and let \(N_q(T)\) count its *distinct* one-step real antecedents \((x,y,z)\) with \(0\leq y\leq T\). The following trichotomy holds for every such target.

**Subcritical coupling.** If \(0\leq k<c\), the entire inverse fiber \(F_{a,b,k}^{-1}(q)\) is finite, and \(F_{a,b,k}\) is a proper map \(\mathbb R^3\to\mathbb R^3\).

**Supercritical coupling.** If \(k>c\), every target has infinitely many distinct real antecedents, all but finitely many regular, and
\[
N_q(T)=\frac2\pi T+O_q(1)\qquad(T\to\infty).
\]
In particular the map is surjective and nonproper. The leading density is independent of the target and of the three parameters within this regime.

**Critical coupling.** If \(k=c\), define \(C_+=c(1-X)\) and \(C_-=-c(1-X)\) and the integers
\[
r_+(q)=\begin{cases}2&Y>C_+,\\1&Y=C_+,\\0&Y<C_+,\end{cases}\qquad
r_-(q)=\begin{cases}2&Y<C_-,\\1&Y=C_-,\\0&Y>C_- .\end{cases}
\]
Then
\[
N_q(T)=\frac{r_+(q)+r_-(q)}{2\pi}T+O_q(1).
\]
Thus a critical target has infinitely many antecedents exactly when \(Y\geq C_+\) or \(Y\leq C_-\); otherwise its inverse fiber is finite. On each equality sheet \(Y=C_+\) or \(Y=C_-\), its remote one-root-per-period antecedents are singular; remote two-root branches on sheets satisfying strict inequalities are regular. In particular, the critical map is nonproper.

At \(k=c\), when \(\delta=Y-C_+>0\), let \(u_j\to+\infty\) denote consecutive solutions of \(\sin(Z-u_j)=-1\). The two antecedents on the positive-\(x\) sheet adjacent to each \(u_j\) have memory coordinates
\[
y_{j,\pm}=u_j\pm\sqrt{\frac{2\delta}{c u_j}}+O(u_j^{-1}).
\]
An analogous square-root splitting holds on the negative-\(x\) sheet when \(C_--Y>0\), centered at consecutive maxima \(\sin(Z-u_j)=1\). All assertions concern one-step inverse fibers in the full real state space, not invariant attractors or bounded physical operating ranges.

## Assumptions and scope
All parameters and states are real; \(a,b>0\), \(k\geq0\), and \(q=(X,Y,Z)\) is arbitrary and fixed when counting. The absolute-value kink at \(x=0\) is allowed; regularity refers to points \(x\ne0\) where the Jacobian determinant is nonzero. The count is by distinct points, not multiplicity, and uses the unbounded *literal* memory coordinate \(z\in\mathbb R\), not memory modulo \(2\pi\). The condition \(0\le y\le T\) is a counting cutoff, not a restriction on all admissible initial states. Any antecedents with negative \(y\) form a finite set because \(y\ge X-1\).

## Proof
**1. Exact scalar reduction.** Write \(u=y\) in the equation \(F_{a,b,k}(x,y,z)=(X,Y,Z)\). The first and third coordinates force
\[
a|x|=u+1-X,\qquad z=Z-u,\qquad u\ge X-1.
\]
For either sign \(\sigma=\pm1\), put
\[
x=\frac{\sigma(u+1-X)}a,\quad
H_\sigma(u)=\sigma c(u+1-X)+ku\sin(Z-u).
\]
Then the second coordinate is precisely \(H_\sigma(u)=Y\). Every solution \(u>X-1\) gives exactly one antecedent on that sheet. The two sheets coincide at \(u=X-1\), which can only affect the finite-count constant. Each \(H_\sigma\) is real-analytic and nonconstant (its linear slope is nonzero when \(k=0\)); consequently it has finitely many zeros on every compact interval. In particular, all possible infinite fibers must come from \(u\to+\infty\).

**2. Subcritical properness.** For \(u\ge0\), the inverse equation implies
\[
|Y|\ge(c-k)u-c|1-X|.
\]
If \(k<c\), this bounds \(u\) at every fixed target. If the target varies over a compact set, the bound is uniform; the lower bound \(u\ge X-1\), and the expressions for \(x,z\), then bound every antecedent. The inverse image of a compact set is therefore closed and bounded, hence compact. The analytic scalar equations yield finite fibers.

**3. Supercritical phase count.** If \(k>c\), uniformly as \(u\to+\infty\),
\[
\frac{H_\sigma(u)-Y}{u}
=\sigma c+k\sin(Z-u)+\frac{\sigma c(1-X)-Y}{u}.
\]
The unperturbed equation \(\sin(Z-u)=-\sigma c/k\) has exactly two simple roots in every interval of length \(2\pi\). The roots are separated from the critical values \(\pm1\). On small fixed disjoint neighborhoods of these roots the derivative of \(H_\sigma(u)/u\) converges uniformly to \(-k\cos(Z-u)\), so the implicit/monotonicity argument supplies exactly one simple zero in each neighborhood for all sufficiently high cells. On the complement the unperturbed function stays a positive distance from zero; hence there are no other remote roots. Two roots per period on each sheet give \(4/(2\pi)=2/\pi\) antecedents per memory unit, with a uniformly bounded boundary-cell error. The two sheets are distinct at large \(u\). Because every target has remote roots, the map is onto and nonproper.

**4. Critical phase count.** Set \(k=c\). The scalar functions become exactly
\[
H_+(u)=C_++cu[1+\sin(Z-u)],\qquad
H_-(u)=C_--cu[1-\sin(Z-u)].
\]
For sufficiently large \(u>0\), the positive-sheet equation has no solution if \(Y<C_+\), and precisely one solution per remote negative-sine extremum if \(Y=C_+\). If \(\delta=Y-C_+>0\), the equation is
\[
cu[1+\sin(Z-u)]=\delta.
\]
Away from small neighborhoods of the minima, its left side grows linearly, ruling out roots. At a minimum \(u_j\), set \(u=u_j+s\); the exact equation is \(c(u_j+s)(1-\cos s)=\delta\). For large \(j\), every root has \(|s|=O(u_j^{-1/2})\), and on this scale the left side is strictly decreasing for negative \(s\) and increasing for positive \(s\). Hence there are exactly two solutions per minimum, with
\[
s=\pm\sqrt{\frac{2\delta}{cu_j}}+O(u_j^{-1}).
\]
The negative sheet is identical after interchanging sine minima and maxima and replacing \(\delta\) by \(C_--Y\). This gives the stated coefficients \(r_+,r_-\) and an \(O(1)\) counting discrepancy from the finitely many initial cells and two cutoff end-cells. If both \(r_+\) and \(r_-\) vanish, neither sheet has remote roots, so the fiber is finite.

**5. Regularity and the sharp global boundary.** Away from the kink \(x=0\), the derivative has determinant
\[
\det DF_{a,b,k}=-b-a\operatorname{sgn}(x)k[\sin z-y\cos z]
=-a\sigma H_\sigma'(u).
\]
The remote supercritical roots are simple, as are both branches of the critical strict-inequality folds; critical equality roots are the exact sine extrema and satisfy \(H_\sigma'(u)=0\). The target \((X,Y,Z)=(1,0,0)\) has infinitely many critical antecedents, proving nonproperness at equality. Combining with Step 2 proves that \(k=b/a\) is the sharp global properness boundary.

## Verification
The standalone Python file `lozi_inverse_check.py` checks the Jacobian identity with symbolic algebra, reconstructs 100 supercritical inverse points for each of two targets, verifies four distinct critical count patterns by high-cell root isolation, and checks the square-root fold displacement at increasing memory indices. Its final output is `ALL DIAGNOSTICS PASS`. Finite computations are corroborative only; the all-parameter and all-target assertions follow from the analytic proof above. The source map equation and published primary MSC are read directly from the publisher's full-text HTML.

## Relationship to prior work
Wang, Gu, Rong, Xu and Zhang (2022) introduced this exact memristor-based Lozi map, proved it has no fixed points when \(b\ne0\), computed its Jacobian and studied forward dynamics, numerical multistability and hyperchaos. It did not provide a real inverse-fiber census or a global properness threshold. Lozi's 2023 survey reproduces this map and reports forward-dynamical uses, without an inverse-fiber counting theorem. Existing indexed studies of infinite ancestor multiplicity for *other* cosine-memristive models do not imply this map's nonzero finite/infinite coupling boundary or its target-dependent equality diagram. Standard local inverse-function arguments alone do not yield the global fiber census; the exact elimination and control of all high phase cells are required here.

## Limitations
The theorem does not classify cycles, attractors, dynamics on bounded invariant regions or physical trajectories. Infinite antecedents are generally located at unbounded \(y,|x|,|z|\), so they do not mean infinitely many plausible predecessors under a fixed compact operating constraint. No statement is made about injectivity in the proper regime or the exact finite number of preimages for every individual target. Prior-art coverage is assessed against inspected sources and index searches; unindexed equivalent results are possible. No independent mathematical audit has been performed.

## References
1. J. Wang, Y. Gu, K. Rong, Q. Xu and X. Zhang, *Memristor-Based Lozi Map with Hidden Hyperchaos*, Mathematics **10** (2022), 3426, first published 2022-09-21. https://doi.org/10.3390/math10193426
2. R. Lozi, *Survey of Recent Applications of the Chaotic Lozi Map*, Algorithms **16** (2023), 491, published 2023-10-22, Section 3.3.1. https://doi.org/10.3390/a16100491
