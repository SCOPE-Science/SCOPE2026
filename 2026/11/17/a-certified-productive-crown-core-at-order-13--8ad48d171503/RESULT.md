# An explicit thousand-ary, height-35 productivity certificate for crown cores of order at least 13

## Finding

For each integer \(n\ge13\), consider the crown biadjacency matrix \(C_n=J_n-I_n\). Attach to every core vertex a complete rooted tree with exactly 1000 children at each nonterminal level and height 35, denoting the resulting bipartite graph by \(T_{C_n}(1000^{[35]})\). For the complex operator Schur-multiplier norm,
\[
\big\|T_{C_n}(1000^{[35]})\big\|_{\bullet}
>2+\frac{7053468}{1625\cdot5606050}>2
>\|C_n\|_{\bullet}=2-\frac2n.
\]
Thus these explicit attachments certify productivity of every crown core of order at least 13. The contribution is the **quantitative construction at branching 1000 and height 35 for orders 13 and 14**, not the first proof of productivity at those orders or a new smallest-order cutoff. A separate published certificate already establishes productivity for every order at least 12, with branching 10000 and height 100. Another earlier certificate gives branching 1000 and height 12 for every order at least 15. The present witness supplies an intermediate, strictly smaller attachment bound in both resources than the order-12 construction for the previously unaddressed order-13/14 parameter pair; it does not improve the order-12 structural cutoff.

## Definitions and scope

The graph is finite and bipartite, with incidence matrix viewed as a zero–one multiplier on bounded operators between the corresponding two Hilbert spaces. Its norm is
\(\|M\|_{\bullet}=\sup_{\|X\|\le1}\|M\circ X\|\).
The notation \(1000^{[35]}\) means 35 levels of downward edges beyond the original core vertices at depth zero. The construction is not claimed to have minimal branching, minimal height, minimal graph size, or the exact multiplier norm. The tree-attachment trace-norm formula is imported explicitly from Levene [1], Theorem 3.8 and equation (3.2); no enumeration of the enormous attached graph is necessary.

## Proof

At \(n=13\) take \(R=1000\), \(h=35\), and the 36 positive integers

```
u = [1000, 730, 691, 653, 617, 583, 551, 520, 491,
     463, 436, 410, 386, 363, 340, 319, 298, 279,
     260, 242, 224, 207, 191, 175, 160, 145, 130,
     116, 103, 89, 76, 63, 50, 38, 25, 12]
```

Set the depth weights \(x_j=u_j^2\), and put
\[
S=\sum_{j=0}^{35}u_j^2=5606050,\qquad
H=\sum_{j=1}^{34}u_ju_{j+1}=4330856.
\]
The singular values of the normalized 13-crown incidence matrix are \(12/13\) once and \(1/13\) twelve times. In the tree norm formula [1], each positive-depth tridiagonal trace norm is at least twice the magnitude of its first off-diagonal entry, by pinching onto a principal two-by-two corner. A chain at depth \(\ell\in\{1,\ldots,34\}\) has \(13R^\ell-13R^{\ell-1}\) copies, and its relevant off-diagonal entry is \(u_\ell u_{\ell+1}/(13R^\ell)\). Thus the sum of their contributions is bounded below by \(2(R-1)H/R=1998H/1000\).

The same trace-norm pinching of the two leading coordinates of the 13 depth-zero singular blocks yields the fully explicit lower bound
\[
S\big\|T_{C_{13}}(1000^{[35]})\big\|_{\bullet}\ge
\frac{\sqrt{(12u_0^2)^2+4(u_0u_1)^2}+12\sqrt{(u_0^2)^2+4(u_0u_1)^2}}{13}
+\frac{1998}{1000}H.
\]
Here the two integer radicands are, respectively, \(146131600000000\) and \(3131600000000\). Their strict integer square-root floors are \(12088490\) and \(1769632\). Substituting these *strict lower bounds* and the exact sums gives
\[
S\big\|T_{C_{13}}(1000^{[35]})\big\|_{\bullet}
>\frac{12088490+12\cdot1769632}{13}
  +\frac{1998}{1000}\cdot4330856
=2S+\frac{7053468}{1625}.
\]
Division by \(S>0\) proves the stated strict bound at order 13. For any \(n\ge13\), choose 13 row and 13 column indices in \(C_n\) and all the trees attached to these selected core vertices. Their incidence submatrix is \(T_{C_{13}}(1000^{[35]})\), so Schur-multiplier norm monotonicity under matrix compression yields the same lower bound. Finally, transitivity and the singular spectrum of \(J_n-I_n\) give \(\|C_n\|_{\bullet}=2-2/n<2\); hence the productivity criterion of [1] is satisfied. \(\square\)

## Exact check and limitations

Run the accompanying unchanged `check_certificate.py` using Python 3's standard library. It verifies all 36 positive entries, both integer sums, the strict integer square-root inequalities, and the exact rational excess \(7053468/1625\). The numerical facts can be checked independently with integer arithmetic. The program does not prove the imported tree norm formula, and a finite numerical experiment is not used to infer any infinite theorem: extension to all \(n\ge13\) follows from the displayed submatrix argument.

The conclusion is a particular constructive resource bound, not the optimal productivity threshold in \(n\), the best height at branching 1000, or an exact norm. The preceding order-12 result does not imply the present smaller branching/height instance, but it *does* already imply the qualitative productivity of all orders \(n\ge13\). Therefore the sole possible originality here is this explicit quantitative witness, and its value is the substantially reduced attachment size for the two intermediate orders, rather than a claim that 13 is a new productive family cutoff. Possible other parameter-specific certificates remain a historical-priority risk.

## References and precise comparison

1. R. H. Levene, *A half-line of Schur idempotent norms*, arXiv:2611.08419v1 (2026-11-05), especially equation (3.2), Theorem 3.8 and Definition 4.2, https://arxiv.org/html/2611.08419v1. This source supplies the general multiplier trace-norm formula and productivity criterion, with numerical discussion of a 15-crown but not the integer witness above.
2. *Twelve-vertex crown sides form a productive Schur core*, published research record (2026-11-17), https://github.com/Resultary/2026/blob/main/2026/11/17/SCOPE-twelve-vertex-crown-sides-form-a-productive-schur-core--d24f02729fc3/RESULT.md. This proves qualitative productivity already for \(n\ge12\) using branching 10000 and height 100, thereby superseding any claim that the family cutoff 13 is new.
3. *Certified productivity of crown-graph cores for Schur idempotents*, published research record (2026-11-17), https://github.com/Resultary/2026/blob/main/2026/11/17/SCOPE-certified-productivity-of-crown-graph-cores-for-schur-idempotent--1904e223ddd1/RESULT.md. This supplies branching 1000 and height 12 for \(n\ge15\). Its larger core-size restriction does not imply the order-13/14 certificate above.

These publications share a calendar publication date; no claim of individual intra-day priority is made.
