# Exact commutator fibers of two rank-one idempotents over finite fields

## Finding

Let \(k=\mathbb F_q\) be any finite field, including characteristic two. Let \(\mathcal P_q\subset M_2(k)\) be the set of rank-one idempotents, and for a prescribed matrix \(C\) put
\[
F_q(C)=\#\{(P,Q)\in\mathcal P_q^2:PQ-QP=C\}.
\]
For a nonzero, traceless, invertible, nonscalar \(C\), let \(e(C)\) be the number of one-dimensional \(k\)-subspaces invariant under \(C\); thus \(e(C)\in\{0,2\}\) for odd \(q\), and \(e(C)=1\) for even \(q\). Define the scalar-root count
\[
\rho_q(t)=\#\{a\in k:a(1-a)=t\}.
\]
Then the complete prescribed-target law is
\[
F_q(C)=\begin{cases}
2q(q+1),&C=0,\\
4q,&C\ne0,\ \operatorname{tr}C=\det C=0,\\
(q+1-e(C))\rho_q(\det C),&\operatorname{tr}C=0,\ \det C\ne0,\ C\text{ nonscalar},\\
0,&\text{otherwise}.
\end{cases}
\]
The scalar-root count is explicit. For odd \(q\), with \(\chi_q\) the quadratic character extended by \(\chi_q(0)=0\),
\[
\rho_q(t)=1+\chi_q(1-4t).
\]
For \(q=2^f\),
\[
\rho_q(t)=\begin{cases}2,&\operatorname{Tr}_{k/\mathbb F_2}(t)=0,\\0,&\operatorname{Tr}_{k/\mathbb F_2}(t)=1.\end{cases}
\]
In particular, a nonzero scalar target in characteristic two, though traceless, is not representable.

The exact number of distinct commutator targets is
\[
\boxed{\#\{C:F_q(C)>0\}=\begin{cases}
\dfrac{q^2(q+1)+q(\chi_q(-1)-1)}{2},&q\text{ odd},\\[2mm]
1+\dfrac{q(q^2-1)}{2},&q\text{ even}.
\end{cases}}
\]
Thus the image size has a congruence-class correction in odd characteristic: it equals \(q^2(q+1)/2\) for \(q\equiv1\pmod4\), and \(q^2(q+1)/2-q\) for \(q\equiv3\pmod4\). Every ordered pair is counted, and \(\sum_C F_q(C)=q^2(q+1)^2\).

## Assumptions and scope

The field has order \(q=p^f\) for arbitrary prime \(p\) and positive integer \(f\). Each pair \((P,Q)\) is ordered; both matrices must have rank exactly one, not merely be idempotent. The commutator is the additive matrix commutator \(PQ-QP\), not the group commutator. Matrices \(C\) range over all \(M_2(k)\), without similarity-quotienting. A nonzero traceless singular matrix is automatically nilpotent of rank one. Every nonzero traceless invertible matrix is nonscalar unless the characteristic is two, where nonzero scalar matrices must be excluded explicitly.

## Proof

**1. Normal form and the scalar equation.** A rank-one idempotent \(P\) determines an ordered decomposition \(k^2=L\oplus M\) into image and kernel lines. There are exactly \(q(q+1)\) such decompositions: \(q+1\) choices of \(L\), then \(q\) complementary lines \(M\). In the associated basis, \(P=\operatorname{diag}(1,0)\). Any rank-one idempotent \(Q\) has trace one and determinant zero, and is therefore exactly of the form
\[
Q=\begin{pmatrix}a&b\\c&1-a\end{pmatrix},\qquad a(1-a)=bc.
\]
Indeed, Cayley--Hamilton gives \(Q^2-Q+(\det Q)I=0\), so trace one and determinant zero are both necessary and sufficient for idempotency, and the nonzero trace makes the rank exactly one. Direct multiplication gives
\[
[P,Q]=\begin{pmatrix}0&b\\-c&0\end{pmatrix},\qquad \det[P,Q]=bc=a(1-a).
\]
For any fixed \(P\), there are therefore exactly \(\rho_q(\det C)\) suitable \(Q\) if \(C\) has zero diagonal in the \(L\oplus M\) decomposition, and none otherwise. The zero-diagonal condition is intrinsically \(C(L)\subseteq M\) and \(C(M)\subseteq L\).

**2. Counting compatible decompositions.** Since a commutator is traceless, \(F_q(C)=0\) for nontraceless targets. If \(C=0\), every \(P\) is compatible, and \(\rho_q(0)=2\), giving \(2q(q+1)\). If \(C=\lambda I\ne0\), compatibility would imply \(C(L)\subseteq M\) while \(C(L)=L\), an impossibility; such a target can have trace zero only in characteristic two.

Suppose next \(\operatorname{tr}C=0\), \(\det C\ne0\), and \(C\) is nonscalar. Cayley--Hamilton gives \(C^2=-(\det C)I\). Consequently, for every line \(L\) not invariant under \(C\), the unique compatible complementary line is \(M=C(L)\); conversely every compatible decomposition occurs this way. The count of compatible \(P\) is \(q+1-e(C)\). For odd characteristic, \(C\) has either two or zero rational eigenspaces, because its characteristic polynomial \(X^2+\det C\) has distinct roots in a splitting field. For characteristic two, a nonscalar traceless invertible \(C\) has a unique invariant line: its characteristic polynomial has a repeated root in \(k\), while it is not scalar.

If \(C\ne0\) is traceless and singular, its kernel and image equal a line \(K\), and \(C^2=0\). Compatible decompositions are exactly \(L=K\), \(M\ne K\), or \(L\ne K\), \(M=K\). Each family has \(q\) members, so the number of compatible \(P\) is \(2q\); as \(\rho_q(0)=2\), the fiber has \(4q\) elements. This proves the complete piecewise fiber formula.

**3. Evaluating scalar roots.** In odd characteristic, \(a(1-a)=t\) is equivalent to \((2a-1)^2=1-4t\), hence it has \(1+\chi_q(1-4t)\) roots. In characteristic two it becomes \(a^2+a=t\), whose image is the absolute-trace-zero subspace: the map has kernel \(\{0,1\}\), and its trace vanishes because \(\operatorname{Tr}(a^2)=\operatorname{Tr}(a)\). Hence it has precisely two roots when the trace vanishes and none otherwise.

**4. Counting image targets.** The trace-zero determinant strata are elementary. For odd \(q\) and any \(t\ne0\), the number of \(C\) with \(\operatorname{tr}C=0\) and \(\det C=t\) equals \(q(q+\chi_q(-t))\): writing \(C=\left(\begin{smallmatrix}x&y\\z&-x\end{smallmatrix}\right)\), solve \(yz=-t-x^2\) and count the values of \(x\) for which the right side vanishes. There are \(q^2-1\) nonzero nilpotent targets. The nonzero determinant values attained by \(a(1-a)\) are in bijection with squares \(\delta=1-4t\) including zero but excluding one; there are \((q-1)/2\) such values. The elementary quadratic Jacobi sum gives
\[
\sum_{t\ne0:\,1-4t\text{ square}}\chi_q(-t)=\frac{\chi_q(-1)-1}{2}.
\]
For completeness: rewrite the sum as \(\sum_{\delta\text{ square},\delta\ne1}\chi_q(\delta-1)\), separate \(\delta=0\), and use \(\sum_x\chi_q(x)\chi_q(1-x)=-\chi_q(-1)\). The latter follows by completing the square and counting \((u,v)\) with \((v-u)(v+u)=1\), which has exactly \(q-1\) solutions. Adding the zero matrix, the \(q^2-1\) nonzero nilpotents, and the attainable invertible strata gives the stated odd-characteristic image cardinality.

For \(q=2^f\), the nonzero nilpotent targets again number \(q^2-1\). For each nonzero \(t\), exactly \(q^2\) trace-zero matrices have determinant \(t\); precisely one is scalar (the unique scalar square root of \(t\)), and the remaining \(q^2-1\) are nonscalar. There are \(q/2-1\) nonzero absolute-trace-zero determinant values, giving \(1+(q^2-1)+(q/2-1)(q^2-1)=1+q(q^2-1)/2\) represented targets.

**5. Total mass.** There are exactly \(q(q+1)\) rank-one idempotents and therefore \(q^2(q+1)^2\) ordered pairs. Every pair is mapped to exactly one target, establishing the displayed global mass identity independently of the target calculations.

## Verification

The self-contained program `scripts/check_commutator.py` enumerates every rank-one idempotent by rank-one outer products and every ordered pair of these matrices, forms literal commutators, and checks the displayed formula against **all** target matrices for \(q\in\{2,3,4,5,7,8,9,11\}\). It implements extension fields explicitly for \(q=4,8,9\), with irreducible defining polynomials, verifies multiplicative inverses, and independently evaluates rational invariant lines and scalar-root counts. It also checks the closed image-cardinality formula in every tested field. Run from the package root with `python scripts/check_commutator.py` and compare stdout with `checks/checker_output.txt`. The concluding marker is `ALL_PROJECTION_COMMUTATOR_CHECKS_PASS`.

These finite checks corroborate, but do not replace, the proof for arbitrary prime-power \(q\). No claim about higher-dimensional matrix algebras, constrained symmetric projections, or arbitrary finite rings is made.

## Relationship to prior work

Khurana, Lam and Shomron (arXiv:1003.5420, initially public 2010-03-29) give a general determinantal identity for two-by-two additive matrix commutators. Specializing their determinant identity to rank-one idempotents yields the necessary relation \(\det[P,Q]=a(1-a)\) with \(a=\operatorname{tr}(PQ)\), but does not enumerate compatible first idempotents, individual target fibers, or the image size.

Drnovšek, Radjavi and Rosenthal (2002, DOI 10.1016/S0024-3795(01)00533-X) provide characterization criteria for matrices that are commutators of idempotents. The full original text was not accessible for a complete theorem-by-theorem comparison; the accessible review states existence conditions, not target-wise finite-field multiplicities. This is a residual historical-priority limitation, not a claim of a full-text negative check.

Khurana and Lam (arXiv:1808.02308, Theorems A--E and Sections 2--5) establish invertibility and ring-theoretic criteria for commutators of idempotents but not the enumerative distribution. Drnovšek (arXiv:2311.16724, Theorems 2.1--2.2) develops existence criteria, including compatible square roots for a fixed projector decomposition; his theorem does not sum over all projectors and roots in finite fields. Earlier work on sums of two idempotents (arXiv:0907.4436) concerns addition rather than the commutator map. No mathematical priority beyond the specified counting theorem is claimed.

## Limitations

The theorem treats only **ordered pairs of rank-one idempotents of order two** and all finite fields; arbitrary idempotent ranks in higher dimensions and group commutators are outside its scope. The image-size formulas count matrices, not similarity classes. The general determinant identity and existence theorems are established prior results. An inaccessible plausible original characterization paper and an unidentified general convolution/counting theorem could conceivably provide equivalent multiplicities. Historical priority has not been independently certified; the mathematical proof and exhaustive computations have not received an independent audit.

## References

1. D. Khurana, T. Y. Lam, N. Shomron, *A quantum-trace determinantal formula for matrix commutators, and applications*, arXiv:1003.5420, first submitted 2010-03-29. https://arxiv.org/abs/1003.5420
2. R. Drnovšek, H. Radjavi, P. Rosenthal, *A characterization of commutators of idempotents*, Linear Algebra and its Applications 347 (2002), 91--99. DOI: 10.1016/S0024-3795(01)00533-X. https://doi.org/10.1016/S0024-3795(01)00533-X
3. D. Khurana, T. Y. Lam, *Commutators and Anti-Commutators of Idempotents in Rings*, arXiv:1808.02308, 2018-08-07. https://arxiv.org/abs/1808.02308
4. R. Drnovšek, *On commutators of idempotents*, arXiv:2311.16724, 2023-11-28. https://arxiv.org/abs/2311.16724
5. C. de Seguins Pazzis, *On linear combinations of two idempotent matrices over an arbitrary field*, arXiv:0907.4436, 2009-07-25. https://arxiv.org/abs/0907.4436
