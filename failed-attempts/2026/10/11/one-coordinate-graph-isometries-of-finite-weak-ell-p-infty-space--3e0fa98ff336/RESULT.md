# One-coordinate graph isometries of finite weak \(\ell_{p,\infty}\) spaces
## Finding
Let \(p>0\), \(n\ge 1\), and equip \(\mathbb C^n\) with the finite weak-Lorentz quasi-norm \(\|x\|_{p,\infty,n}=\max_{1\le k\le n} k^{1/p}x_k^*\), where \(x_1^*\ge\cdots\ge x_n^*\) is the decreasing rearrangement of the coordinate moduli. For \(u\in\mathbb C^n\), define \(G_u(x)=(x_1,\ldots,x_n,\sum_{j=1}^n u_jx_j)\in\mathbb C^{n+1}\). If \(u_1^*\ge\cdots\ge u_n^*\) rearranges \((|u_j|)\), then \(G_u\) is a linear isometry from \(\ell_{p,\infty}^n\) into \(\ell_{p,\infty}^{n+1}\) if and only if \(\sum_{k=1}^n k^{-1/p}u_k^*\le (n+1)^{-1/p}\). Equivalently, the appended functional has exact operator gauge \(\sup_{\|x\|_{p,\infty,n}\le1}|\sum_j u_jx_j|=\sum_{k=1}^n k^{-1/p}u_k^*\), and the graph is isometric exactly when this gauge does not exceed \((n+1)^{-1/p}\). For \(n\ge2\), such an isometry fails to preserve disjointness of coordinate vectors exactly when at least two coefficients \(u_j\) are nonzero. Among isometric graph maps, the largest possible common overlap \(\min_j|u_j|\) is \((n+1)^{-1/p}/\sum_{k=1}^n k^{-1/p}\), attained when all coefficient moduli are equal; at \(n=2\) this recovers the coefficient in Fang--Gao--Huang--Sukochev, Remark 1.1.

This gives a complete coefficient-region description for the canonical one-extra-coordinate family of non-surjective weak-\(\ell_p\) isometries. In particular, it identifies the two-dimensional example in the cited source as the balanced extremizer of a dimension-free pattern rather than an isolated construction.

## Assumptions and scope
Fix \(p>0\) and an integer \(n\ge1\). For \(x\in\mathbb C^n\), write \(x_1^*\ge\cdots\ge x_n^*\ge0\) for the decreasing rearrangement of \((|x_j|)\), and set
\[
\|x\|_{p,\infty,n}=\max_{1\le k\le n} k^{1/p}x_k^*.
\]
For \(u=(u_1,\ldots,u_n)\in\mathbb C^n\), let \(u_1^*\ge\cdots\ge u_n^*\) rearrange \((|u_j|)\), define \(\phi_u(x)=\sum_{j=1}^n u_jx_j\), and let \(G_u(x)=(x,\phi_u(x))\). The statement concerns exactly this identity-coordinate graph family; it does not classify arbitrary nonsurjective isometries between weak-Lorentz sequence spaces.

## Proof
First compute the exact functional gauge. If \(\|x\|_{p,\infty,n}\le1\), then \(x_k^*\le k^{-1/p}\). The rearrangement inequality therefore gives
\[
|\phi_u(x)|\le \sum_{k=1}^n u_k^*x_k^*\le \sum_{k=1}^n k^{-1/p}u_k^*.
\]
Choose a permutation \(\pi\) for which \(|u_{\pi(k)}|=u_k^*\), and choose phases so that \(u_{\pi(k)}x_{\pi(k)}\ge0\) with \(|x_{\pi(k)}|=k^{-1/p}\). Then \(\|x\|_{p,\infty,n}=1\) and equality holds. Hence
\[
\sup_{\|x\|_{p,\infty,n}\le1}|\phi_u(x)|=\sum_{k=1}^n k^{-1/p}u_k^*.
\]

Put \(s=(n+1)^{-1/p}\). Suppose the displayed sum is at most \(s\), and let \(N=\|x\|_{p,\infty,n}\). Then \(|\phi_u(x)|\le sN\). For every \(1\le k\le n\), the appended coordinate is at most \(Nk^{-1/p}\), while among the original coordinates at most \(k-1\) are strictly larger than that threshold. Thus the \(k\)-th largest coordinate of \(G_u(x)\) is at most \(Nk^{-1/p}\). For \(k=n+1\), the appended coordinate itself is at most \(sN\), so the smallest of all \(n+1\) target coordinates is at most \(sN\). Therefore \(\|G_u(x)\|_{p,\infty,n+1}\le N\). Adding a coordinate cannot decrease any of the first \(n\) decreasing rearrangement values, so the reverse inequality holds and \(G_u\) is an isometry.

Conversely, suppose \(G_u\) is an isometry. Use the phase-aligned extremizer above. Every one of its \(n\) original coordinate moduli is at least \(n^{-1/p}>s\). If \(|\phi_u(x)|>s\), then all \(n+1\) target coordinate moduli exceed \(s\), forcing \((n+1)^{1/p}(G_u(x))_{n+1}^*>1\), contradicting isometry. Hence \(\sum_{k=1}^n k^{-1/p}u_k^*\le s\), proving necessity.

For distinct coordinate vectors \(e_i,e_j\), the supports of \(G_u(e_i)\) and \(G_u(e_j)\) meet in the last coordinate exactly when both \(u_i\) and \(u_j\) are nonzero, giving the disjointness criterion. Finally, if \(c=\min_j|u_j|\), then \(u_k^*\ge c\) for every \(k\), so isometry implies
\[
c\sum_{k=1}^n k^{-1/p}\le(n+1)^{-1/p}.
\]
Equality is attained by taking every \(|u_j|\) equal to the resulting upper bound. For \(n=2\), this is \(3^{-1/p}/(1+2^{-1/p})\), exactly the coefficient displayed in the focal source.

## Verification
The argument is symbolic and valid for every real \(p>0\); no convexity or triangle inequality is used. The necessity test uses an explicit norm-one phase-aligned vector. The sufficiency step is a rank-counting argument for decreasing rearrangements, so it covers the quasi-Banach range \(0<p\le1\) as well as \(p>1\). Boundary equality is included throughout.

## Relationship to prior work
Fang, Gao, Huang and Sukochev explicitly restrict their weak-\(L_p\) isometry analysis to surjective maps because disjointness preservation can fail without surjectivity. Their Remark 1.1 gives the case \(n=2\), using the equal coefficient \(3^{-1/p}/(1+2^{-1/p})\), but does not give the coefficient-region criterion above. The earlier symmetric-sequence-space isometry theorem of Aminov and Chilin concerns surjective isometries, so it does not imply this nonsurjective graph classification. The Lorentz/Marcinkiewicz sequence-space geometry literature supplies relevant rearrangement background but, in the inspected material, addresses geometric structure, duality, and complemented subspaces rather than this graph-isometry boundary.

## Limitations
The result classifies only graph maps that retain the first \(n\) coordinates unchanged and append one linear functional. It does not classify arbitrary nonsurjective weak-\(\ell_p\) isometries, multiple-coordinate extensions, or noncommutative weak-\(L_p\) embeddings. The functional gauge used in the proof is a standard finite rearrangement computation; the new content claimed here is the exact graph-isometry equivalence, its disjointness boundary, and the balanced sharp overlap within this canonical family.

## References
1. K. Fang, Y. Gao, J. Huang, F. Sukochev, *Extreme points of the unit ball and isometries of noncommutative quasi-Banach Marcinkiewicz spaces*, arXiv:2610.01043v1 (2026), especially Section 1.2 and Remark 1.1.
2. B. R. Aminov, V. I. Chilin, *Isometries and Hermitian operators on complex symmetric sequence spaces*, Siberian Advances in Mathematics 27 (2017), 239--252, DOI 10.3103/S1055134417040022.
3. M. Ciesielski, G. Lewicki, *Sequence Lorentz Spaces and Their Geometric Structure*, Journal of Geometric Analysis 29 (2019), 1929--1952, DOI 10.1007/s12220-018-0069-4.
