# Sharp universal temporal-order boundary for finite nested state-dependent delays

## Finding

For each integer \(i\geq3\), let \(\nu_i\in(1/2,1)\) be the unique solution of
\[
\sum_{k=1}^{i-1}\nu_i^k=1.
\]
For the switched negative-feedback delay model described below, the published sufficient condition \(q<\nu_i\), where \(q\) is the normalized Lipschitz product, is **the optimal universal strict temporal-order condition** within the contraction regime \(0<q<1\):

1. For every admissible equation and history with \(q<\nu_i\), the delayed-argument function at nesting depth \(i\) is strictly increasing.
2. For every \(q=\nu_i\), an admissible zero-forcing, linear-response example has a nondegenerate interval on which that delayed-argument function is **constant**.
3. For every \(\nu_i<q<1\), an admissible example of the same form has an interval on which it is **strictly decreasing**.

For both kinds of witness, **all** finite nested-delay trajectories and the uniquely defined implicit-delay trajectory nevertheless coincide globally with the constant-delay trajectory; the implicit delayed argument remains strictly increasing. Thus the finite-depth loss of temporal ordering is independent of trajectory invisibility. The statement concerns a universal guarantee, not an if-and-only-if criterion for an individual history.

## Assumptions and scope

The ambient system of Bolduc-St-Aubin, Subramanian and Krauskopf is the absolutely continuous solution of
\[
h'(t)=-\operatorname{sign}(h(t-\tau(t)))+F(t),
\]
with a constant reference delay \(\bar\tau>0\), measurable forcing bounded by \(c>0\), and a sign-preserving \(\eta\)-Lipschitz response \(\Psi\). For a history \(\varphi\) on \([-2\bar\tau,0]\), define recursively
\[
\tau_1(t)=\bar\tau,\qquad
\tau_{j+1}(t)=\bar\tau+\Psi(h(t-\tau_j(t))),
\qquad d_j(t)=t-\tau_j(t).
\]
Let \(g\) be the constant-delay reference solution, and write
\[
L=\max\{L_\varphi,1+c\},\qquad q=\eta L.
\]
The source's invisibility hypotheses are \(\eta(1+c)<1\), \(\eta L_\varphi<1\), \(\eta|\varphi(s)|<\bar\tau\) on the history, and \(\eta|g(t)|<\bar\tau\) for subsequent times. They imply \(0<q<1\), existence and uniqueness in the stated solution class, and coincidence of all nested and implicit trajectories with \(g\). Temporal order of reactions (TOR) means that \(d_j\) is **strictly** increasing.

The universal positive direction \(q<\nu_i\Rightarrow\mathrm{TOR}\) is Theorem 5.1 of the source and is **not** claimed as new. The new assertion is its precise optimality, including the equality case, **inside the dynamically invisible regime**. The witnesses use \(\bar\tau=1\), \(c=1\) as a valid forcing envelope, actual forcing \(F\equiv0\), and \(\Psi(u)=\eta u\).

## Proof

**Step 1 (a separated finite orbit of the nesting map).** Fix \(i\geq3\) and any \(q\in[\nu_i,1)\), set \(\eta=q/2\), and let \(\varepsilon=\sigma=1/100\). On \([-2,0]\), introduce the affine baseline \(b(s)=\varepsilon+\sigma(s+1)\). Put \(y_1=-1\) and
\[
y_{j+1}=-1-\eta b(y_j),\qquad 1\leq j\leq i-2.
\]
In terms of \(w_j=y_j+1\), this is \(w_1=0\) and \(w_{j+1}=-\eta\varepsilon-\eta\sigma w_j\), so
\[
w_j=-\frac{\eta\varepsilon}{1+\eta\sigma}
\bigl(1-(-\eta\sigma)^{j-1}\bigr).
\]
The \(i-1\) points \(y_1,\ldots,y_{i-1}\) are therefore distinct, all lying strictly inside \((-2,0)\), and all within \(1/200\) of \(-1\).

**Step 2 (realizing independent extremal slopes without changing the iterates).** Assign slopes \(v_j=-2\) for \(1\leq j\leq i-2\) and \(v_{i-1}=+2\). Choose \(\rho>0\) small enough that the intervals \([y_j-5\rho,y_j+5\rho]\) are disjoint and contained in \((-2,0)\), and \(\rho<1/1000\). Define \(\varphi=b\) outside these intervals. Within the interval centered at \(y_j\), put \(u=s-y_j\) and define
\[
\varphi(y_j+u)=
\begin{cases}
b(y_j)+v_ju,& |u|\leq\rho,\\[2pt]
b(y_j)+\operatorname{sign}(u)\left[v_j\rho+
\dfrac{5\sigma-v_j}{4}(|u|-\rho)\right],&\rho<|u|\leq5\rho.
\end{cases}
\]
The outer piece matches \(b\) at \(|u|=5\rho\). Its slope is \((5\sigma-v_j)/4\), of magnitude less than \(2\). Hence \(\varphi\) is continuous and exactly \(2\)-Lipschitz, has \(\varphi(y_j)=b(y_j)\) and derivative \(\varphi'(y_j)=v_j\), and obeys \(M:=\|\varphi\|_\infty<1\). In particular, the marked points are *unchanged* as nested arguments at \(t=0\), despite the local slope modifications. This geometric separation is why all depths can be realized.

**Step 3 (global admissibility and invisibility).** Let \(g\) solve \(g'(t)=-\operatorname{sign}(g(t-1))\) with the above history, and take \(c=1\). The method of steps gives its unique global solution with \(|g'|\leq1\) almost everywhere. Furthermore
\[
|g(t)|\leq 1+M\qquad(t\geq0).
\]
To see the upper bound, for \(t<1\) it follows directly from \(|g'|\leq1\). If \(t\geq1\) and \(g(t)>1+M\), then \(g(t-1)\geq g(t)-1>M\), so \(g'=-1\) almost everywhere wherever the upper barrier is exceeded. Such an excursion cannot start from below the barrier. The lower bound is symmetric. Since \(\eta=q/2<1/2\) and \(M<1\), we have \(\eta|g(t)|\leq(q/2)(1+M)<1\) for every \(t\). Also \(L_\varphi=2\) and \(\eta(1+c)=\eta L_\varphi=q<1\). Therefore **every** hypothesis of the source's global invisibility theorem holds. All finite nested and implicit trajectories equal \(g\), all delays lie in \((0,2)\), and the implicit delayed argument preserves TOR.

**Step 4 (exact temporal-order derivative).** For sufficiently small \(t\geq0\), the first \(i-1\) delayed arguments belong to the history subintervals where \(\varphi\) has the prescribed slopes. The nested delayed-argument recurrence is then
\[
d_1(t)=t-1,\qquad d_{j+1}(t)=t-1-\eta\varphi(d_j(t)).
\]
Its derivatives \(D_j=d'_j(t)\) are constant on a common positive-length interval and satisfy
\[
D_1=1,\qquad D_{j+1}=1-\eta v_jD_j.
\]
For the first \(i-2\) steps, \(v_j=-2\), hence
\[
D_{i-1}=1+q+\cdots+q^{i-2}.
\]
At the final step, \(v_{i-1}=+2\), giving the exact identity
\[
\boxed{D_i=1-\sum_{k=1}^{i-1}q^k.}
\]
At \(q=\nu_i\), this derivative is identically zero on the interval: \(d_i\) has a genuine plateau and is not strictly increasing. For every \(q>\nu_i\) with \(q<1\), it is strictly negative: \(d_i\) reverses temporal order. The construction is continuous at equality and does not rely on a numerical trajectory.

**Step 5 (sharpness).** Theorem 5.1(i) of the motivating paper states that \(q<\nu_i\) suffices for strict TOR for all admissible histories. Steps 1–4 supply counterexamples for every \(q\geq\nu_i\) still below the invisibility threshold \(q=1\). These two directions establish the asserted optimal universal boundary. For depth \(i=2\), \(\nu_2=1\), so no such counterexample exists within \(q<1\); this is why the new sharpness statement starts at \(i=3\).

## Verification

The accompanying standalone `verify.py` reconstructs the finite separated orbits, every breakpoint of the piecewise-linear history, its \(2\)-Lipschitz bound and its amplitude bound, and the exact delayed-argument slopes using Python rational arithmetic. It checks representative above-threshold examples at depths \(3\) through \(7\), plus below-threshold comparison cases through depth \(8\). The execution output is `VERIFY_OK exact_rational_checks=345 witness_depths=3..7 additional_below_threshold=3..8`. The **all-depth** statement and the irrational equality cases follow from the explicit algebraic construction in the proof; the finite checks are corroboration, not an exhaustive proof.

## Relationship to prior work

Bolduc-St-Aubin, Subramanian and Krauskopf establish dynamic invisibility of nested delays (Theorem 1.1), the sufficient TOR thresholds \(\nu_i\) (Theorem 5.1), their monotone convergence to \(1/2\) (Proposition 5.2), and a numerical high-slope example where intermediate delayed arguments decrease (Figure 2). Those results **do not by themselves show that each \(\nu_i\) is sharp**, or that equality can produce an interval of constant delayed argument. The present result adds the exact, all-depth realizability statement. Earlier examples at the separate contraction boundary \(q=1\) concern loss of trajectory invisibility, not the failure of strict TOR at \(q<1\).

Walther's earlier algebraic-delay work concerns implicit delay and temporal-order reversal in other models. Its available abstract does not cover this finite-depth universal threshold construction; the full work was not accessible for detailed comparison.

## Limitations

The result is about universal guarantees within the specified switched system class and its permitted Lipschitz histories. It does not assert that every individual history with \(q\geq\nu_i\) loses TOR, nor does it identify a threshold for smooth non-switching feedback, parameter-dependent forcing, or delayed responses outside the contraction regime. The witness histories are continuous and piecewise linear, as allowed by the source theorem; they are not required to be differentiable at their finitely many corners. Historical priority beyond the inspected literature is provisional. Independent scientific validation has not been performed.

## References

1. S. Bolduc-St-Aubin, P. Subramanian and B. Krauskopf, *Dynamic invisibility of implicit and nested state-dependent delays in a class of externally forced delay equations*, arXiv:2610.39281v1 (first submitted 29 October 2026), especially Theorems 1.1 and 5.1, Proposition 5.2 and Section 5. https://arxiv.org/html/2610.39281v1
2. H.-O. Walther, *Algebraic-Delay Differential Systems, State-Dependent Delay, and Temporal Order of Reactions*, J. Dynam. Differential Equations **21** (2009), 195–232, DOI:10.1007/s10884-009-9129-6 (abstract inspected; full text unavailable).
