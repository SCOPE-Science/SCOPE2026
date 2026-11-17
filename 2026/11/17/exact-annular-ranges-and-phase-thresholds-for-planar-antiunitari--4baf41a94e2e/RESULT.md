# Exact annular ranges and phase thresholds for planar antiunitaries

## Finding
Let \(H\) be a two-dimensional complex Hilbert space with its inner product linear in the first entry. Let \(A:H\to H\) be antiunitary: \(A\) is conjugate-linear and \(\|Ax\|=\|x\|\). For \(q\in\mathbb C\) with \(|q|\le1\), put
\[
W_q(A)=\{\langle Ax,y\rangle:\|x\|=\|y\|=1,\ \langle x,y\rangle=q\}.
\]
Define \(c=w(A)=\max_{\|x\|=1}|\langle Ax,x\rangle|\), \(s=\sqrt{1-c^2}\), \(r=|q|\), and \(d=\sqrt{1-r^2}\). Then \(0\le c,s,r,d\le1\), and the following formula is exact, including both boundary circles:
\[
\boxed{W_q(A)=\{z\in\mathbb C:R_-(r,c)\le |z|\le R_+(r,c)\}},
\]
where
\[
\boxed{R_-(r,c)=\max\{0,ds-rc\}},\qquad
\boxed{R_+(r,c)=\begin{cases}
1,&r\le c,\\
rc+ds,&r>c.
\end{cases}}
\]
Thus \(W_q(A)\) is a centered closed disk (possibly a singleton) exactly when \(r\ge s\); for \(r<s\) it has a genuine central hole, with a circle allowed as a limiting annulus. Its outer radius equals the operator norm \(1\) exactly when \(r\le c\). The two transition values \(s\) and \(c\) cross at \(c=1/\sqrt2\). Each value \(c\in[0,1]\) is realized by an antiunitary on \(\mathbb C^2\), so every phase regime in this formula occurs.

## Assumptions and scope
The result concerns exactly two complex dimensions and antiunitaries (surjective conjugate-linear isometries). It includes complex \(q\), not just real \(q\). The pairing convention matters: \(\langle u,\alpha v\rangle=\overline\alpha\langle u,v\rangle\). There is no extension here to arbitrary antilinear contractions or to higher-dimensional spaces. The word “annulus” includes the degeneracies \(R_-=0\) (disk) and \(R_-=R_+\) (circle).

## Proof
**Step 1: all self-overlap moduli occur.** The map \(f(x)=\langle Ax,x\rangle\), restricted to the unit sphere, has a zero. To see this directly, fix an orthonormal basis \(e_1,e_2\). If \(f(e_2)=0\) we are done. Otherwise \(f(e_1+te_2)\) is a nonconstant quadratic polynomial in \(\overline t\), so it has a complex root; the resulting nonzero vector can be normalized. The compact unit sphere also contains a maximizer of \(|f|\), of value \(c\). Since that sphere is connected, continuity of \(|f|\) implies
\[
\{|\langle Ax,x\rangle|:\|x\|=1\}=[0,c].
\]

**Step 2: exact constrained geometry at a fixed first vector.** Fix a unit \(x\) and write \(m=|\langle Ax,x\rangle|\). For \(r<1\), every permitted unit \(y\) has the form
\[
y=\overline q\,x+d v,\qquad \|v\|=1,\quad v\perp x.
\]
The complex line \(x^\perp\) has dimension one. Since \(A\) is an isometry, the component of \(Ax\) perpendicular to \(x\) has norm \(\sqrt{1-m^2}\). Therefore varying the phase of \(v\) makes the modulus of \(\langle Ax,y\rangle\) traverse the whole interval
\[
\left[\left|rm-d\sqrt{1-m^2}\right|,\quad rm+d\sqrt{1-m^2}\right].
\]
The same formula holds when \(r=1\), because \(d=0\) and then \(y=\overline q\,x\).

**Step 3: the two scalar optimizations.** By Step 1, \(m\) varies through \([0,c]\). The unconstrained maximum of \(rm+d\sqrt{1-m^2}\) on \([0,1]\) is \(1\), attained at \(m=r\). Restricting to \(m\le c\), the maximum is therefore \(1\) if \(r\le c\), and otherwise \(rc+d\sqrt{1-c^2}=rc+ds\). The expression \(rm-d\sqrt{1-m^2}\) is nondecreasing, and vanishes exactly at \(m=d\) (with the endpoint cases interpreted continuously). Consequently the minimum of its absolute value on \([0,c]\) is \(0\) when \(d\le c\) and is \(ds-rc\) when \(d>c\). The equivalence \(d\le c\iff r\ge s\) yields the stated inner radius.

**Step 4: no radial gaps or missing boundary points.** For \(|q|<1\), the constrained pair space is homeomorphic to the unitary frame space \(U(2)\), hence is compact and connected; for \(|q|=1\), it is the connected compact unit sphere. Thus the set of attained moduli is a closed interval with the extrema computed in Step 3. Moreover simultaneous replacement \((x,y)\mapsto(e^{it}x,e^{it}y)\) preserves the constraint and multiplies the value by \(e^{-2it}\). Every attained modulus therefore gives its entire centered circle. This proves the exact closed annulus formula.

**Step 5: nonvacuity of every phase regime.** For \(0\le c\le1\), put \(s=\sqrt{1-c^2}\) and consider
\[
A_c(z_1,z_2)=(c\overline{z_1}+s\overline{z_2},\,-s\overline{z_1}+c\overline{z_2}).
\]
It is antiunitary and \(\langle A_cz,z\rangle=c(\overline{z_1}^{\,2}+\overline{z_2}^{\,2})\). Its numerical radius is exactly \(c\), making both thresholds effective for suitable choices of \(q\).

## Verification
The proof is analytic and covers all antiunitaries and all \(|q|\le1\), with no finite-test extrapolation. The accompanying standard-library script `checker.py` verifies rational endpoint identities and tests the complete constraints and radial inequalities on explicitly represented rotation-conjugation antiunitaries, including both degenerate endpoints. Run `python3 checker.py`. The resulting diagnostics are supplementary: they cannot certify the universal quantifiers independently.

For example, with \(c=3/5\), \(s=4/5\), and \((r,d)=(5/13,12/13)\), the annulus has inner radius \(33/65\) and outer radius \(1\). With the same antiunitary but \((r,d)=(4/5,3/5)\), the inner radius is \(0\) and the outer radius is \(24/25\).

## Relationship to prior work
Majumdar and Müller (2026) develop the \(q\)-numerical range of antilinear operators, prove the disk theorem for dimension at least three, and state the closed-annulus property in dimension two (Remark 6.7). Their Example 6.3 shows that the inner radius need not be zero. The present statement determines **both radii for every planar antiunitary**, the exact convexity threshold, and the threshold for attaining the norm as outer radius. In particular, the two-dimensional hole classification is not implied by the higher-dimensional disk theorem.

Kołaczek and Müller (2024) determine ordinary antilinear numerical-range geometry, corresponding here to \(|q|=1\). Their 2025 study concerns real-linear ordinary numerical ranges. Related linear-operator \(q\)-numerical-range inequalities do not apply by complex linearity to a general antiunitary. An earlier theorem on antiunitaries in dimension at least three has an analogous outer-radius envelope, but its universal disk conclusion leaves the two-dimensional inner-radius phenomenon unresolved.

## Limitations
No statement is made about a full classification of two-dimensional *nonisometric* antilinear operators or general real-linear maps. The result gives ranges, not a stability estimate for perturbations. A complete literature priority audit remains possible beyond the primary sources inspected; unindexed results on antiunitary \(q\)-numerical radii are a residual novelty risk. The self-review is not independent verification.

## References
1. A. Majumdar and V. Müller, *Some Generalized Numerical Ranges of Real-linear Operators on Hilbert Spaces*, arXiv:2610.16823v1 (first publicly submitted 2026-10-12), Section 6, particularly Example 6.3, Theorem 6.6 and Remark 6.7. https://arxiv.org/abs/2610.16823
2. D. Kołaczek and V. Müller, *Numerical Ranges of Antilinear Operators*, Integral Equations and Operator Theory 96 (2024), article 17, Section 2. https://doi.org/10.1007/s00020-024-02768-5
3. D. Kołaczek and V. Müller, *Real linear operators and numerical ranges*, arXiv:2508.04347v1 (2025), Sections 1 and 6. https://arxiv.org/abs/2508.04347
