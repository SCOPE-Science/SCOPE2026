# Genus \(15\) and exact collision moments in a plane-filling pencil

## Finding

Let \(q\) be an odd prime power with characteristic different from \(3\) and \(7\). In the plane-filling pencil of Asgarli and Ghioca,
\[
 C_k:\quad X^2(X^qY-XY^q)+Y^2(Y^qZ-YZ^q)+(Z^2+kX^2)(Z^qX-ZX^q)=0,\qquad k\in\mathbb F_q,
\]
put \(N_k=\#\{t\in\mathbb F_q^\times:t^7+kt^3-1=0\}\). These are the numbers of rational singular points of \(C_k\).

The normalization of the geometrically integral degree-nine plane collision curve
\[
\mathcal B:\quad x^3y^3(x+y)(x^2+y^2)+x^2+xy+y^2=0
\]
has **geometric genus \(15\)**. It is birational over \(\mathbb F_q\) to the smooth projective model \(H\) of the cyclic Kummer curve
\[
 t^7=-\frac{s^2+s+1}{s^3(s+1)(s^2+1)}.
\]
If, in addition, \(7\nmid(q-1)\), then \(\#H(\mathbb F_q)=q+1\) and the **exact second factorial moment** of rational singularities across the pencil is
\[
 \boxed{\sum_{k\in\mathbb F_q}N_k(N_k-1)=q-\gcd(3,q-1)-\gcd(4,q-1).}
\]
Equivalently, since \(\sum_kN_k=q-1\),
\[
 \boxed{\sum_{k\in\mathbb F_q}N_k^2=2q-1-\gcd(3,q-1)-\gcd(4,q-1).}
\]
A further bound, valid for all the indicated characteristics even when \(7\mid(q-1)\), is
\[
  \boxed{\#\mathcal B(\mathbb F_q)\ge q+1-30\sqrt q-13.}
\]
The error coefficient \(30\) comes from the exact geometric genus \(15\), rather than the plane-degree arithmetic-genus coefficient \(56\) used in the original estimate; the additive \(13\) accounts for possible discrepancies at singular points of the plane model.

The factorial moment counts **ordered pairs of distinct rational singular points on the same member**. It is not a count of distinct singular members or of geometric singularities over extensions.

## Assumptions and scope

All fields have odd cardinality and characteristic \(p\ge5\) with \(p\ne7\). The geometric-genus and Kummer-model statements hold with no restriction on \(q-1\). Exact moment and point-count formulas require \(\gcd(7,q-1)=1\). At other field orders no elementary moment formula is asserted; the Kummer curve still governs the collision count. The source theorem establishes the rational-singularity root parametrization, which is used here without re-claiming it.

## Proof

**From the rational-singularity criterion to a collision curve.** Asgarli--Ghioca, Theorem 1.2, gives \(N_k\) as above. The rational parameter map is
\[
 \kappa(t)=t^{-3}-t^4,\qquad t\in\mathbb F_q^\times.
\]
For distinct nonzero \(x,y\), the equality \(\kappa(x)=\kappa(y)\) is equivalent to
\[
 (y-x)\bigl(x^3y^3(x+y)(x^2+y^2)+x^2+xy+y^2\bigr)=0.
\]
Thus the off-diagonal collision locus is an open subset of \(\mathcal B\), precisely the curve used in Section 2 of the motivating source for bounding the number of smooth-at-rational-points pencil members. On the dense open chart \(x\ne0\), set \(t=x\) and \(s=y/x\). Then
\[
 \frac{\mathcal B(t,st)}{t^2}=t^7s^3(1+s)(1+s^2)+(1+s+s^2),
\]
which yields the asserted Kummer function field. Conversely \((t,s)\mapsto(x,y)=(t,st)\) is a rational inverse on dense opens. Hence normalization and the smooth Kummer model are isomorphic.

**Genus.** Over an algebraic closure in characteristic not \(2,3,7\), the rational function \(R(s)=-(s^2+s+1)/(s^3(s+1)(s^2+1))\) has exactly seven distinct zero/pole locations on \(\mathbb P^1_s\), with respective valuations
\[
 1,\ 1,\ -3,\ -1,\ -1,\ -1,\ 4.
\]
The two simple zeros are the roots of \(s^2+s+1\); the fourth-order zero is at infinity; the poles are at \(0,-1\), and the roots of \(s^2+1\). All locations are distinct, and every valuation is coprime to \(7\). The Kummer extension of function fields is therefore separable of degree seven, geometrically connected, and totally ramified at exactly these seven places, unramified elsewhere. Riemann--Hurwitz gives
\[
 2g(H)-2=7(-2)+7(7-1)=28,\qquad g(H)=15.
\]
The plane curve has arithmetic genus \(28\), hence normalization defect \(\sum_P\delta_P=28-15=13\). At any rational singular point the difference between its one contribution to \(\#\mathcal B(\mathbb F_q)\) and the count of rational branches over it is at most its geometric \(\delta\)-invariant, since \(\delta_P\ge r_P-1\) for the number \(r_P\) of geometric branches (and \(\delta_P\ge1\) for a singular point). Nonrational singular points have no rational preimage. Thus \(\big|\#\mathcal B(\mathbb F_q)-\#H(\mathbb F_q)\big|\le13\). The Hasse--Weil bound for the smooth genus-fifteen curve gives \(\#H(\mathbb F_q)\ge q+1-30\sqrt q\), proving the advertised explicit bound.

**Point count and moment.** Suppose \(\gcd(7,q-1)=1\). Above every \(s\in\mathbb P^1(\mathbb F_q)\) outside the branch locus, the value \(R(s)\) is a nonzero rational element with exactly one seventh root in \(\mathbb F_q\). Above every rational branch point there is a single totally ramified point, necessarily rational. Thus every rational base point has exactly one rational preimage, proving \(\#H(\mathbb F_q)=q+1\).

For the collision pairs, \(s=y/x\) must satisfy \(s\in\mathbb F_q^\times\), \(s\ne1\), and \(s^3\ne1\), \(s^4\ne1\) (to avoid zero/pole parameters and to keep \(x,y\ne0\)). For each such \(s\), \(t^7=R(s)\) has exactly one solution. In \(\mathbb F_q^\times\), the sets \(\{s:s^3=1\}\) and \(\{s:s^4=1\}\) intersect only at \(1\), since \(\gcd(3,4)=1\). Inclusion-exclusion therefore gives
\[
 (q-2)-(\gcd(3,q-1)-1)-(\gcd(4,q-1)-1)
 =q-\gcd(3,q-1)-\gcd(4,q-1).
\]
Every ordered distinct pair \((x,y)\) in the same \(\kappa\)-fiber occurs exactly once in this count. The formula for \(\sum N_k^2\) follows from \(\sum N_k=q-1\).

## Verification

Run `python verify_symbolic.py` and `python verify_counts.py` from the extracted package. The first verifies the collision polynomial factorization and the Kummer birational identity symbolically, plus the seven prescribed valuations and Riemann--Hurwitz arithmetic. The second enumerates rational singularity multiplicities directly for seventeen prime fields and three quadratic extensions, comparing independent ordered-pair counts; it checks the exact formulas whenever \(\gcd(7,q-1)=1\). These finite calculations corroborate but do not replace the field-uniform algebraic proof.

## Relationship to prior work

Asgarli--Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072v1, Theorem 1.2 and Section 2, provide the defining pencil, its root criterion, and the **same degree-nine collision curve**. Their Lemma 2.1 proves geometric irreducibility and their Theorem 1.4 uses a Hasse--Weil estimate based on its plane degree. The collision curve's existence, irreducibility, and its role in the original argument are *prior work*. The contribution here is the explicit Kummer birational model, exact geometric genus, the exceptional congruence-regime point count, and the exact singularity-pair moment. Neither original Section 2 nor its final higher-degree section states those refinements. Standard Kummer theory and Riemann--Hurwitz are used, not claimed as new.

## Limitations

The theorem concerns the specific \(r=2\) pencil, not all plane-filling curves. It does not solve the geometric smoothness conjecture for the pencil, determine the number of distinct rationally singular parameters, or classify rational singularity types; the latter has separate previous treatments. The exact moment formula excludes \(7\mid(q-1)\), and all statements exclude characteristics \(2,3,7\). The original collision curve is typically singular as a plane model: genus \(15\) refers to its **normalization**, not its arithmetic genus. Historical priority beyond inspected sources remains uncertain; no independent mathematical audit has been performed.

## References

- S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072v1 (first public July 6, 2023), especially Theorem 1.2, Lemma 2.1 and the proof of Theorem 1.4.
- Standard Kummer function-field ramification and the Riemann--Hurwitz formula (used as standard results, not as priority claims).
