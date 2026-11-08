# Resistance-eccentricity tomography of three-path metric networks and its sharp path threshold

## Finding

Let \(G\) be a compact metrized graph comprising \(k\geq3\) distinct arcs of strictly positive lengths \(\ell_1,\ldots,\ell_k\), all joining the same two vertices \(A,B\), with resistance per unit arclength equal to one. Write \(R_G(X,Y)\) for the *effective electrical resistance*, not the intrinsic shortest-path distance. Put
\[
L=\sum_{i=1}^k\ell_i,\qquad
\rho=R_G(A,B)=\left(\sum_{i=1}^k\ell_i^{-1}\right)^{-1},\qquad
E=\max_{X\in G}R_G(A,X),\qquad m=\max_i\ell_i.
\]
Then
\[
\boxed{E=\frac{m^2}{4(m-\rho)}}.\tag{1}
\]
For \(k=3\), the three scalar observations \((L,\rho,E)\) uniquely determine the multiset of all three arc lengths. Explicitly,
\[
m=2E+2\sqrt{E(E-\rho)},\qquad
S=L-m,\qquad C=\rho^{-1}-m^{-1},\qquad
\{\ell_i: \ell_i\ne\text{a chosen longest arc}\}
=\left\{\frac{S\pm\sqrt{S^2-4S/C}}{2}\right\},\tag{2}
\]
where the last multiset includes any other arcs tied for longest. By contrast, for every \(k\geq4\) there exist nonisometric such networks with exactly the same \((L,\rho,E)\); this ambiguity occurs in continuous families.

At fixed total length, the terminal resistance eccentricity satisfies the *sharp* inequality
\[
\boxed{\frac{L}{4(k-1)}\leq E<\frac L4}.\tag{3}
\]
Equality on the left holds exactly when all the arc lengths are equal; the upper bound is the unattained supremum as one arc approaches length \(L\) and the others approach zero.

## Assumptions and scope

The point set \(G\) includes all interior points of all arcs. Effective resistance \(R_G(X,Y)\) is the voltage drop for unit current from \(X\) to \(Y\), with the specified resistance density along the arcs. The quantity \(E\) is the terminal-to-*any-point* maximum, not the endpoint-to-endpoint resistance and not the diameter of the resistance metric. \(A\) and \(B\) are the two common branch vertices; they are distinguishable as vertices of valence \(k\geq3\). Arc lengths may coincide. Isomorphism/isometry here permits permutation of arcs and interchange of \(A,B\). The theorem concerns exactly this two-terminal parallel-arc family; no reconstruction is asserted for arbitrary networks.

## Proof

**1. The resistance profile.** On arc \(i\), let \(X_i(x)\) be at arclength \(x\in[0,\ell_i]\) from \(A\). Deleting the interior of this arc leaves a parallel connection with resistance
\[
\sigma_i=\left(\sum_{j\ne i}\ell_j^{-1}\right)^{-1}
=\frac{\ell_i\rho}{\ell_i-\rho}.
\]
The direct segment from \(A\) to \(X_i(x)\) has resistance \(x\), in parallel with the path of resistance \(\sigma_i+\ell_i-x\). Series–parallel reduction therefore yields, also at the endpoints by continuity,
\[
R_G(A,X_i(x))=\frac{x(\sigma_i+\ell_i-x)}{\sigma_i+\ell_i}
=x-\frac{\ell_i-\rho}{\ell_i^2}x^2.\tag{4}
\]
The first equality may alternatively be obtained from the general edge-resistance formula in Baker–Faber, Theorem 10; the quadratic edge law is *not* claimed as new.

**2. Extremizers and the global law.** Since \(\rho\leq\ell_i/k\) is not true for each \(i\), one must treat shorter arcs separately. The derivative of (4) vanishes at
\[
x_i^*=\frac{\ell_i^2}{2(\ell_i-\rho)}.
\]
This point lies strictly inside arc \(i\) precisely when \(\ell_i>2\rho\). In that case the arcwise maximum is \(\ell_i^2/[4(\ell_i-\rho)]>\rho\); otherwise its maximum is attained at \(B\), with value \(\rho\). Every longest arc satisfies \(m\geq k\rho>2\rho\), because \(\sum_i\ell_i^{-1}\geq k/m\). For \(t>2\rho\), the derivative of \(t^2/(t-\rho)\) is \(t(t-2\rho)/(t-\rho)^2>0\). Thus precisely the longest arcs contain global resistance-farthest points and (1) follows. If several arcs tie for longest, each has exactly one global maximizer, at \(x_i^*\); no endpoint is globally farthest.

**3. Inverse three-arc theorem.** Equation (1) becomes \(m^2-4Em+4E\rho=0\). As \(m>2\rho\), its relevant root is \(m=2E+2\sqrt{E(E-\rho)}\), while the other root is less than \(2\rho\). If \(k=3\), the two remaining lengths \(u,v>0\) have sum \(S=L-m\) and reciprocal sum \(C=\rho^{-1}-m^{-1}\); hence \(uv=S/C\). They are therefore exactly the two roots of \(z^2-Sz+S/C=0\), giving (2), including repeated-root cases. The recovered unordered triple is an isometry invariant and completely describes the metrized theta graph.

**4. Four-arm obstruction, then every higher arm count.** The two positive length multisets
\[
\left\{5,1,2,3\right\},\qquad
\left\{5,\frac32,\frac94+\frac34\sqrt{\frac{15}{7}},\frac94-\frac34\sqrt{\frac{15}{7}}\right\}
\tag{5}
\]
are different, with common total \(L=11\), maximum \(m=5\), and total conductance \(\rho^{-1}=1/5+11/6=61/30\). Thus their \(E\) values agree by (1). More than an isolated pair exists: with the shorter-arc sum \(6\) and reciprocal sum \(11/6\) fixed, set one of the three shorter lengths to \(t\); the other two are roots of a continuously varying quadratic. Near \(t=3/2\), its roots are distinct, strictly positive, and less than \(5\), giving a nonconstant continuous family with the same data. Appending the same \(k-4\) sufficiently short positive arcs to both four-arm examples preserves equality of \(L\), total conductance, and longest length, hence of \(E\), proving nonidentifiability for all \(k\geq4\).

**5. Sharp total-length bounds.** The maximal arc has length \(m\). Parallel reduction of the remaining arcs gives \(\sigma_m\leq L-m\), strictly when \(k\geq3\). Hence \(\rho=m\sigma_m/(m+\sigma_m)<m(L-m)/L\), and (1) gives \(E<L/4\). Let one arc tend to \(L\) while the rest tend to zero; then \(m\to L\), \(\rho\to0\), and \(E\to L/4\).

For the lower bound, if \(m\geq L/(k-1)\), then \(E>m/4\geq L/[4(k-1)]\). Otherwise \(L/k\leq m<L/(k-1)\), and \(s=L-(k-1)m\) lies in \((0,m]\). Among positive \(k\)-tuples of sum \(L\) bounded above by \(m\), convexity of \(t\mapsto1/t\) shows that \(\sum_i\ell_i^{-1}\) is maximized at the extremal tuple \((m,\ldots,m,s)\): each feasible tuple is majorized by this extremal tuple. Therefore
\[
\rho\geq\frac{ms}{m+(k-1)s},\qquad
E\geq\frac{m(m+(k-1)s)}{4(m+(k-2)s)}.
\]
The second expression is at least \(L/[4(k-1)]\) because after multiplication by positive denominators the difference of numerators is exactly
\[
(k-1)m(m+(k-1)s)-((k-1)m+s)(m+(k-2)s)
=(k-2)s(m-s)\geq0.
\]
For \(k\geq3\) this vanishes in the nondegenerate regime precisely at \(s=m\), forcing all arcs equal. Conversely equal arcs have \(\rho=L/k^2\) and \(E=L/[4(k-1)]\), proving sharpness and rigidity.

## Verification

The companion `verify_resistance_theta.py` uses exact rational Kirchhoff solves on independently subdivided three-node resistor networks, checks the derived quadratic against those solves on 120 cases, and tests the global bound and longest-arc reconstruction on 8,000 randomized cases (including 1,000 theta inversions). It also checks the explicit unequal four-arm counterexample. The observed completion line is:

`VERIFY_OK exact_nodal_cases=120 random_global_bounds=8000 inverse_theta_cases=1000 four_arm_counterexample=1`

The proof above is analytic and applies to every positive real arc-length tuple, not only the finite test set. Running the verifier requires only Python 3's standard library.

## Relationship to prior work

Baker and Faber established the general metrized-graph effective-resistance concept and edgewise quadratic formula (Theorems 9–10); (4) specializes that formula and is prior art. The present result concerns **three global unlabeled scalar observations**, the exact inverse threshold between three and four parallel arcs, a continuous nonuniqueness family, and the sharp fixed-length resistance-eccentricity inequality with its equality case. These statements do not appear in the inspected full text of Baker–Faber. Other work on resistance diameters of finite combinatorial graphs concerns different observables and sampling of vertices, not the same terminal-to-continuum-point maximum. Related metric-theta distance work uses intrinsic shortest-path distance, not effective electrical resistance. This statement makes no claim of a new series–parallel law; historical priority of the inverse classification requires further independent literature review.

## Limitations

Assumes perfect measurements and a known graph family with the two common terminals specified; it is not a stable inverse-recovery theorem under noise, nor a general-network tomography result. The three observations are sufficient for all positive three-arc lengths but not in general for four or more arcs. The upper bound in (3) is not attained by a nondegenerate network. The independent verification is finite and does not certify the proof.

## References

1. Matthew Baker and Xander Faber, *Metrized graphs, electrical networks, and Fourier analysis*, first arXiv submission 2004-07-25, arXiv:math/0407428. https://arxiv.org/abs/math/0407428 . Particularly §6, Theorems 9–10 (effective resistance, edgewise quadratic profile).
2. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66. https://web.stanford.edu/~boyd/papers/eff_res.html . Optimization of total pairwise effective resistance on discrete graphs; a distinct objective from the terminal eccentricity here.
