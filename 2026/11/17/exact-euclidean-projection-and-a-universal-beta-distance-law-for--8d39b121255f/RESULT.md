# Exact Euclidean projection and a universal beta distance law for sparse-paving matroid polytopes

## Finding

Let \(n\ge4\), \(2\le k\le n-2\), and let \(M\) be a rank-\(k\) sparse-paving matroid on \([n]\). Its circuit-hyperplanes (equivalently, nonbases of cardinality \(k\)) form a family \(\mathcal H\) of size \(\lambda\). The standard hypersimplex and matroid base polytope are
\[
\Delta_{n,k}=\{x\in[0,1]^n:\sum_{i=1}^n x_i=k\},\qquad
P(M)=\operatorname{conv}\{\mathbf1_B:B\text{ is a basis of }M\}.
\]
Set \(x(H)=\sum_{i\in H}x_i\), \(t_H(x)=x(H)-k+1\), \(a_+=\max\{a,0\}\), and
\[
\delta_{n,k}=\sqrt{\frac{n}{k(n-k)}}.
\]

**Theorem (metric projection).** Every \(x\in\Delta_{n,k}\) has at most one circuit-hyperplane with \(t_H(x)>0\). If none exists, its unique nearest point in \(P(M)\) is \(x\). Otherwise, for the unique such \(H\) and \(t=t_H(x)>0\), the unique Euclidean nearest point \(y=\Pi_{P(M)}x\) is
\[
y_i=\begin{cases}
x_i-t/k,&i\in H,\\
x_i+t/(n-k),&i\notin H.
\end{cases}
\]
In particular, the **global point-to-polytope distance formula** is
\[
\boxed{\operatorname{dist}_2(x,P(M))=\delta_{n,k}\max_{H\in\mathcal H}(t_H(x))_+.}
\]
If \(\mathcal H\ne\varnothing\), then
\[
\boxed{d_H(\Delta_{n,k},P(M))=\delta_{n,k},}
\]
and the complete set of farthest points is exactly \(\{\mathbf1_H:H\in\mathcal H\}\). These statements remain valid when \(P(M)\) is not full-dimensional. For \(\mathcal H=\varnothing\), the projection is the identity and the Hausdorff gap is zero.

**Theorem (exact intrinsic-volume distance profile).** Assume \(\lambda\ge1\), and let \(X\) be uniform with respect to intrinsic \((n-1)\)-dimensional Euclidean volume on \(\Delta_{n,k}\). Write \(D=\operatorname{dist}_2(X,P(M))\) and let \(A(m,j)\) be the Eulerian number counting permutations of \(m\) elements with \(j\) descents. With
\[
p=\frac{\lambda\binom{n-2}{k-1}}{A(n-1,k-1)},
\]
we have, for every real \(0\le u\le1\),
\[
\boxed{\mathbb P(D>u\delta_{n,k})=p(1-u)^{n-1}.}
\]
Thus \(\mathbb P(D=0)=1-p\), and conditional on \(D>0\), the random variable \(D/\delta_{n,k}\) is exactly \(\operatorname{Beta}(1,n-1)\): its density is \((n-1)(1-u)^{n-2}\) on \(0<u<1\). This conditional law depends only on \(n\), not the rank, number, or arrangement of the missing bases. For every real \(s>0\),
\[
\mathbb E[D^s]=p\delta_{n,k}^{s}\frac{\Gamma(s+1)\Gamma(n)}{\Gamma(n+s)}.
\]

## Assumptions and scope

All distances use the unscaled Frobenius/standard Euclidean norm on \(\mathbb R^n\), restricted to the affine hyperplane \(\sum_i x_i=k\). No connectedness assumption is imposed on the sparse-paving matroid. The standard sparse-paving structure means that distinct \(H,J\in\mathcal H\) obey \(|H\cap J|\le k-2\), and the base polytope has the exact inequality description
\[
P(M)=\Delta_{n,k}\cap\bigcap_{H\in\mathcal H}\{x:x(H)\le k-1\}.
\]
These matroid-polytope properties are established combinatorial background, not new conclusions. Uniform random volume means the normalized Euclidean Hausdorff measure on the hypersimplex's affine hull. In the degenerate \(\lambda=0\) case, the conditional distribution given \(D>0\) is undefined and is not asserted.

## Proof

**1. Disjoint violations.** For distinct \(H,J\in\mathcal H\), their intersections have size at most \(k-2\). Every \(x\in\Delta_{n,k}\) satisfies
\[
x(H)+x(J)=x(H\cup J)+x(H\cap J)\le k+|H\cap J|\le2k-2.
\]
Hence no two inequalities \(x(H)\le k-1\) are simultaneously strictly violated.

**2. The unique hyperplane projection is feasible for all other inequalities.** Suppose \(t=x(H)-k+1>0\). Since \(x(H)=k-1+t\) and \(0\le x_i\le1\), every \(i\in H\) has \(x_i\ge t\). Also \(x(H^c)=1-t\), so every \(j\in H^c\) has \(x_j\le1-t\). Define \(y\) by the displayed coordinate formula. Its entries lie in \([0,1]\), \(\sum_i y_i=k\), \(y(H)=k-1\), and \(y(H^c)=1\). For each distinct circuit-hyperplane \(J\),
\[
y(J)\le |H\cap J|+y(H^c)\le(k-2)+1=k-1.
\]
Therefore \(y\in P(M)\). The Euclidean normal within \(\sum_i z_i=k\) of the halfspace \(z(H)\le k-1\) is proportional to \(\mathbf1_H/k-\mathbf1_{H^c}/(n-k)\). Thus \(x-y\) is the outward normal, and \(y\) is the **orthogonal projection of \(x\)** onto that halfspace in the common affine hyperplane. As \(P(M)\) lies in this halfspace and contains \(y\), \(y\) is also the unique nearest point in \(P(M)\). Finally,
\[
\|x-y\|_2^2=t^2\left(\frac1k+\frac1{n-k}\right)=\delta_{n,k}^2 t^2.
\]
This proves the global metric formula, including the case of no violation.

**3. Sharp Hausdorff distance and equality.** Since \(x(H)\le k\) for \(x\in\Delta_{n,k}\), each violation size is at most one. The upper bound \(D\le\delta_{n,k}\) is attained by every missing vertex \(x=\mathbf1_H\). Equality forces \(x(H)=k\), hence every coordinate in \(H\) equals one, every coordinate outside equals zero, and \(x=\mathbf1_H\). The nearest-point uniqueness follows from Euclidean projection onto a nonempty closed convex set. Since \(P(M)\subseteq\Delta_{n,k}\), the directed and symmetric Hausdorff distances coincide here.

**4. Corner pyramids and their exact volumes.** Fix \(H\in\mathcal H\). The excised cap
\[
C_H=\{x\in\Delta_{n,k}:x(H)>k-1\}
\]
is the relatively open part of a pyramid with apex \(\mathbf1_H\) and base \(F_H=\{x\in\Delta_{n,k}:x(H)=k-1\}\). The base is the orthogonal Cartesian product \(\Delta(k,k-1)\times\Delta(n-k,1)\), so its intrinsic \((n-2)\)-volume is
\[
\frac{\sqrt{k(n-k)}}{(k-1)!(n-k-1)!}.
\]
The apex-to-base height is \(\delta_{n,k}\). The pyramid volume is therefore
\[
\operatorname{vol}_{n-1}(C_H)=\frac{\sqrt n}{(n-1)(k-1)!(n-k-1)!}
=\frac{\sqrt n}{(n-1)!}\binom{n-2}{k-1}.
\]
The standard intrinsic hypersimplex volume is
\[
\operatorname{vol}_{n-1}(\Delta_{n,k})=\frac{\sqrt n}{(n-1)!}A(n-1,k-1).
\]
The cap interiors are disjoint by Step 1. Consequently their total uniform-volume probability is \(p\), which also verifies \(0<p\le1\) for \(\lambda\ge1\).

**5. Exact tail by homothety.** Inside \(C_H\), Step 2 gives \(D=\delta_{n,k} t_H(x)\). For \(0\le u<1\), the superlevel cap \(\{x\in\Delta_{n,k}:t_H(x)>u\}\) is the homothetic image \(u\mathbf1_H+(1-u)C_H\), with volume exactly \((1-u)^{n-1}\operatorname{vol}_{n-1}(C_H)\). The superlevel caps remain disjoint. Dividing their sum of volumes by \(\operatorname{vol}_{n-1}(\Delta_{n,k})\) proves the claimed tail for \(0\le u<1\); the value at \(u=1\) is zero by Step 3. Differentiating conditional survival yields the beta density. Integrating its moments with the Euler beta integral gives the gamma-function formula. None of these arguments requires \(P(M)\) to be full-dimensional.

## Verification

The standalone `check_sparse_paving_metric.py` runs exact rational tests across 69 sparse-paving missing-basis families on \(4\le n\le9\), checking 2,220 points (including missing vertices and interiors of every tested excised corner). Each test verifies unique-constraint violation, the claimed projection vector's entire feasible inequality system, the exact distance, the normal direction, and the Eulerian/binomial cap-volume ratio bound. A separate constrained Euclidean quadratic-program solver computes 180 projections independently; its maximum coordinate-vector discrepancy from the exact formula is below \(6.5\cdot10^{-7}\). The script prints `SPARSE_PAVING_METRIC_PASS exact_points=2220 families=69 constructed_families=69 qp=180 max_qp_gap=6.47e-07 n=4..9`. Run `python check_sparse_paving_metric.py` with Python 3, NumPy, and SciPy. These finite tests support, but do not constitute, the all-dimensional proof above.

## Relationship to prior work

Ferroni's circuit-hyperplane relaxation results and Hanely–Martin–McGinnis–Miyata–Nasr–Vindas-Meléndez–Yin's 2022 hypersimplex-slicing theory establish the sparse-paving vertex truncation and its Ehrhart geometry. Ferroni and Schröter study valuative properties and face enumeration of split and sparse-paving matroid polytopes. A separately published exact Euclidean **surface-area** formula for these clipped polytopes establishes the same cap-base decomposition and its disjointness. These results supply the geometric setting; the cap volume and Eulerian hypersimplex volume are prior ingredients. The **pointwise Euclidean nearest-point map throughout the hypersimplex**, complete farthest-point classification, and exact conditional beta **distance** distribution are the conclusions claimed here, rather than the cap-volume formula alone. Generic algorithms for projecting onto matroid base polytopes do not themselves state this explicit pointwise and probabilistic specialization. Published sources and targeted database searches did not reveal an equivalent combined statement; historical priority remains subject to discovery of earlier terminology or unpublished notes.

## Limitations

The source distribution is uniform Euclidean volume on the *hypersimplex*, not uniform on the matroid base polytope, and the metric is the standard, unweighted Euclidean norm. The formula does not extend without proof to paving matroids that are not sparse paving, arbitrary generalized permutohedra, nonlinear metrics, or all points outside the hypersimplex. The conditional beta law applies only when at least one circuit-hyperplane is missing. An earlier equivalent observation derived from familiar polytope-cap theory or implicit in numerical matroid projection work remains a bibliographic possibility. No independent mathematical audit has been performed.

## References

1. L. Ferroni, *Matroids are not Ehrhart positive*, arXiv:2105.04465, first public version May 10, 2021; circuit-hyperplane relaxation and sparse-paving constructions.
2. D. Hanely, J. L. Martin, D. McGinnis, D. Miyata, G. D. Nasr, A. R. Vindas-Meléndez, and M. Yin, *Ehrhart Theory of Paving and Panhandle Matroids*, arXiv:2201.12442, first public version January 28, 2022, especially the hypersimplex-slicing analysis; authorized author open copy: https://jeremymartinmath.github.io/papers/EhrhartPaving.pdf.
3. L. Ferroni and B. Schröter, *Valuative invariants for large classes of matroids*, arXiv:2208.04893 (2022), §§3–4, 7.
4. L. Ferroni and B. Schröter, *Face enumeration for split matroid polytopes*, arXiv:2310.05487 (2023), especially its sparse-paving face-count formula.
5. *Euclidean surface area of sparse-paving matroid base polytopes depends only on their nonbases*, public mathematical research record, November 2026; a surface-area rather than projection or distance-law result.
