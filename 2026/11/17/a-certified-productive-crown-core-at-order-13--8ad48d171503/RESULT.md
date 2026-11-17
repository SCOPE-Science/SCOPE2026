# A certified productive crown core at order 13

## Finding

For each integer \(n\ge13\), the bipartite crown core with incidence matrix \(C_n=J_n-I_n\) is **productive**: its graph formed by attaching a complete rooted 1000-ary tree of height 35 to each core vertex satisfies
\[
\|T_{C_n}(1000^{[35]})\|_{\bullet}
>2+\frac{7053468}{1625\cdot5606050}>2.
\]
The crown's own Schur norm is \(\|C_n\|_{\bullet}=2-2/n<2\). This gives explicit productivity parameters \((R_0,h_0)=(1000,35)\) for every \(n\ge13\). No analogous assertion is made for \(n\le12\).

## Assumptions and scope

Graphs are finite bipartite graphs identified with their zero–one incidence matrices; \(\|G\|_{\bullet}\) is the operator norm of entrywise multiplication by the incidence matrix on bounded Hilbert-space operators. The core \(C_n\) is the bipartite complement of a perfect matching, with \(n\) vertices on each side. In \(T_{C_n}(1000^{[35]})\), every vertex at depth strictly less than 35 receives 1000 children; the original core vertices have depth zero. The proof uses the finite-tree norm formula, Definition 3.7 and Theorem 3.8 of Levene [1].

## Proof

First work at \(n=13\), and denote the common branching number by \(R=1000\) and the tree height by \(h=35\). Take the positive integer vector

```
u = [1000, 730, 691, 653, 617, 583, 551, 520, 491, 463, 436, 410, 386, 363, 340, 319, 298, 279, 260, 242, 224, 207, 191, 175, 160, 145, 130, 116, 103, 89, 76, 63, 50, 38, 25, 12]
```

and the nonnegative depth weights \(x_j=u_j^2\) for \(0\le j\le35\). Their sum and the adjacent product sum excluding the first edge are
\[
S=\sum_{j=0}^{35}u_j^2=5606050,\qquad
H=\sum_{j=1}^{34}u_ju_{j+1}=4330856.
\]

The 13 singular values of the normalized core incidence matrix are \(12/13\) once and \(1/13\) twelve times, because \(J_{13}-I_{13}\) has eigenvalues \(12,-1,\ldots,-1\). Levene's Theorem 3.8 and equation (3.2) yield \(\|T_{C_{13}}(1000^{[35]})\|_{\bullet}\ge F(x)/S\).

For each positive depth \(1\le\ell\le34\), the trace norm of the tridiagonal chain \(Q_\ell\) is at least \(2c_\ell\), by pinching onto its first two coordinates, where \(c_\ell=u_\ell u_{\ell+1}/(13R^\ell)\). Its multiplicity is \(13R^\ell-13R^{\ell-1}\). Therefore these depths contribute to \(F(x)\) at least \(2(R-1)H/R=1998H/1000\).

At depth zero the same pinching of each core singular-value block to its leading two coordinates gives
\[
F(x)\ge
\frac{1}{13}
\left(\sqrt{(12u_0^2)^2+4(u_0u_1)^2}
+12\sqrt{(u_0^2)^2+4(u_0u_1)^2}\right)
+\frac{1998}{1000}H.
\]
The two radicands are exact integers
\[
(12u_0^2)^2+4(u_0u_1)^2=146131600000000,
\]
\[
(u_0^2)^2+4(u_0u_1)^2=3131600000000.
\]
Rather than use approximations, take their exact integer square-root floors \(12088490\) and \(1769632\), respectively. Both floors are strict; this is verified by squaring them as in the standalone checker. Substitution yields the strict inequality
\[
F(x)>\frac{12088490+12(1769632)}{13}+\frac{1998}{1000}(4330856)
=2(5606050)+\frac{7053468}{1625}.
\]
Thus \(\|T_{C_{13}}(1000^{[35]})\|_{\bullet}>2+7053468/(1625\cdot5606050)>2\).

For \(n\ge13\), select 13 row and 13 column core indices and their entire attached trees. This is an induced copy of \(T_{C_{13}}(1000^{[35]})\) inside \(T_{C_n}(1000^{[35]})\). Restriction to a submatrix cannot increase the Schur multiplier norm, hence the same strict bound holds for all \(n\ge13\). Finally \(\|C_n\|_{\bullet}=2-2/n\) by its normalized singular-value sum, so Levene's Definition 4.2 applies.

## Verification

Run `python3 check_certificate.py` with Python 3 standard library. It checks the 36 integer entries, both sums, both strict square-floor comparisons, the exact rational surplus and its positivity. The code checks the finite arithmetic, not Levene's analytical trace-norm formula, which is an explicit cited premise. No enumeration of the enormous graph is attempted.

## Relationship to prior work

Levene [1], Section 6, reports numerical evidence for productivity of the 15-crown at branching 1000 and height 12, but explicitly states that this experiment was not certified. An existing exact certificate for all crown orders at least 15 establishes a stronger bound at height 12, and is not repeated here. The present statement crosses a previously uncovered structural boundary by proving productivity already at order 13 (and thereby at 14), at the cost of height 35. The core norm, induced-subgraph argument, pinching technique and tree-weight formula are sourced from [1]; the contribution is this distinct, verified 13-crown witness and its improved family cutoff. The threshold 13 is not claimed optimal.

## Limitations

The certificate gives a strict lower bound, not the exact multiplier norm, a best possible branching parameter, or a classification of the small cores. It is conditional on the established tree norm formula in [1]; direct exhaustive verification of the constructed finite matrix is computationally impractical. Possible independent earlier certificates with different terminology are a publication-priority risk.

## References

[1] Rupert H. Levene, *A half-line of Schur idempotent norms*, arXiv:2611.08419v1 (first posted 2026-11-05), Sections 3–6, especially equation (3.2), Definition 3.7, Theorem 3.8, Definition 4.2 and Section 6. https://arxiv.org/html/2611.08419v1
