# A five-point resonance in weighted polyanalytic Fock evaluation orthogonality

## Finding

Consider the positive reproducing kernel
\[
K_\tau(z,w)=e^{z\overline w}\left[L_2^0(|z-w|^2)+\tau\right],\qquad L_2^0(s)=1-2s+\frac{s^2}{2},\quad \tau\ge0.
\]
Let \(M(\tau)\) be the largest cardinality of a set \(X\subset\mathbb C\) of distinct sites for which the reproducing kernels \(K_\tau(\cdot,z)\), \(z\in X\), are pairwise orthogonal. Then
\[
M(\tau)=\begin{cases}
5,&\tau=3/5,\\
4,&\tau\in\{1/3,1/2,7/9\},\\
3,&0\le\tau\le1,\ \tau\notin\{1/3,1/2,3/5,7/9\},\\
1,&\tau>1.
\end{cases}
\]
At the five-point resonance, all maximizing configurations are translates and rotations or reflections of the regular pentagon of circumradius \(2/\sqrt5\). At the three other four-point resonances, the four-point realizations are the two-distance shapes described in the proof. The theorem concerns mutually orthogonal *single-site evaluation kernels*, not arbitrary tight frames or sampling systems.

## Assumptions and scope

We use the Gaussian measure \(\pi^{-1}e^{-|z|^2}\,dA(z)\). Write \(\mathcal F_{(k)}\) for the true level-\(k\) polyanalytic Fock reproducing-kernel Hilbert space, whose kernel is \(e^{z\overline w}L_{k-1}^0(|z-w|^2)\). For \(\tau>0\), \(K_\tau\) is the kernel of the space \(\mathcal F_{(3)}\oplus\mathcal F_{(1)}\), with the analytic summand weighted by reciprocal norm factor \(1/\tau\); at \(\tau=0\) retain only \(\mathcal F_{(3)}\). This construction is positive definite because its two summand kernels are positive definite. Its diagonal values are \((1+\tau)e^{|z|^2}\), so all point kernels are nonzero. Orthogonality is measured in this weighted Hilbert space and every set of sites must be finite and distinct.

## Proof

**Kernel-zero reduction.** By the reproducing property, the inner product of two point kernels vanishes precisely when \(K_\tau(z,w)=0\). Since the exponential never vanishes, this occurs exactly when the squared Euclidean separation \(s=|z-w|^2\) is a root of
\[
P_\tau(s)=1+\tau-2s+s^2/2.
\]
For \(\tau>1\), this quadratic is strictly positive. For \(\tau=1\), it has the sole root \(2\), so there can be an equilateral triple but not four equidistant planar points. For \(0\le\tau<1\) its two positive roots are
\[
u=2-\sqrt{2(1-\tau)},\qquad v=2+\sqrt{2(1-\tau)},\quad 0<u<v.
\]
Thus \(X\) is a planar two-distance set whose squared-distance ratio is \(t=v/u>1\). The two root sum and product identities give
\[
 u=\frac4{1+t},\qquad \tau=\frac{8t}{(1+t)^2}-1.\tag{1}
\]
For all \(0\le\tau\le1\), an equilateral triple of squared side length \(u\) exists, proving \(M(\tau)\ge3\).

**Exhaustive four-site condition.** To avoid assuming a classification for the finite boundary, color each edge of four labelled vertices *long* or *short*. Up to vertex permutation there are eleven graphs of long edges. Normalize the short squared distance to \(1\) and the long squared distance to \(t>1\). After setting \(p_0=0\), put
\[
 G_{ij}=\frac{d_{0i}+d_{0j}-d_{ij}}2\quad (1\le i,j\le3),
\]
where \(d_{ii}=0\), \(d_{ij}\in\{1,t\}\) for distinct vertices. The necessary and sufficient condition for a planar realization is that \(G\) be positive semidefinite and have rank at most two. In particular \(\det G=0\).

The following table gives one representative long-edge graph for each isomorphism class; edges are denoted \(ij\). Its last column is the polynomial \(4\det G\), evaluated symbolically with the above definition.

| Long edges | \(4\det G\) |
|---|---|
| none | \(2\) |
| \(01\) | \(-t(t-3)\) |
| \(01,02\) | \(-t^2+4t-1\) |
| \(03,12\) | \(-2t^2(t-2)\) |
| \(01,02,12\) | \(-t^2(t-3)\) |
| \(01,02,03\) | \(3t-1\) |
| \(01,03,12\) | \(-(t+1)(t^2-3t+1)\) |
| \(01,02,03,12\) | \(-t(t^2-4t+1)\) |
| \(02,03,12,13\) | \(2(2t-1)\) |
| \(01,02,03,12,13\) | \(t(3t-1)\) |
| all six | \(2t^3\) |

The only roots strictly larger than one are \(t=2\), \(t=(3+\sqrt5)/2\), \(t=3\), and \(t=2+\sqrt3\). All corresponding matrices \(G\) have rank exactly two and are positive semidefinite: each has positive diagonal and all three order-two principal minors positive. The numbers of distinct graph classes realizing these four ratios, respectively, are \(1,1,2,2\). For example the \(t=2\) case is a square, the golden-ratio case is four vertices of a regular pentagon, and the two \(t=3\) types are (i) a point at the center of an equilateral triangle and (ii) a rhombus with one long diagonal. The remaining two types are supplied by the displayed Gram matrices at \(t=2+\sqrt3\). This checks sufficiency without depending on any planar drawings. The table is reproducible by `checker.py`, which exhausts all \(2^6=64\) colorings modulo the \(24\) vertex permutations and verifies the eleven integer polynomial identities.

Substituting these four values of \(t\) into (1) yields, respectively,
\[
\tau=7/9,\quad 3/5,\quad 1/2,\quad 1/3.\tag{2}
\]
Therefore a four-site mutually orthogonal family exists exactly at the four parameters in (2).

**Five-site upper bound and rigidity.** The classical planar two-distance theorem states that any such set has at most five points and that any five-point set is similar to a regular pentagon [2, 3]. The long-to-short squared-distance ratio of a regular pentagon equals \((3+\sqrt5)/2\). By (1), a five-site configuration therefore forces \(\tau=3/5\). Conversely at \(\tau=3/5\), the two root distances are \(u=2-2/\sqrt5\) and \(v=2+2/\sqrt5\). The five sites
\[
 z_j=\frac2{\sqrt5}\,e^{2\pi i j/5},\qquad j=0,1,2,3,4,
\]
have exactly those pairwise squared distances; hence their point kernels are pairwise orthogonal. The classical rigidity theorem then supplies uniqueness up to plane isometry. All six-point configurations are excluded by the same theorem. Together with the four-site classification and the three-site lower bound, this proves every case of the stated phase diagram.

## Verification

A standalone standard-library Python checker (`checker.py`) enumerates all \(64\) long/short colorings of a four-vertex complete graph, verifies exactly that they fall into eleven vertex-isomorphism classes, calculates all eleven Gram-determinant polynomials over the integers, checks the six PSD realizations at the candidate ratios, and checks all ten squared distances for the pentagon. Run `python3 checker.py` from the artifact directory. The recorded output was `PASS: 64/64 edge colorings, 11/11 exact determinant identities, 6 feasible four-point graph shapes, four exact parameter resonances, and 10/10 regular-pentagon squared distances.` The finite checker is a reproducibility aid: the infinite cardinality bound and five-site rigidity are cited mathematical theorems, not inferred from numerical experiments.

## Relationship to prior work

Fulsche and Hagger [1, §3, (3.1)–(3.3)] provide the true-level Laguerre Fock kernels and discuss their zero circles. Harborth and Piepmeyer [2] give the planar four-site two-distance shapes and the unique five-point pentagon. Nozaki and Shinohara [3, §4.4] give a second full-text account of the five-site maximality and rigidity. Those results are acknowledged as premises; the asserted finding is the **complete \(\tau\)-dependent orthogonal-evaluation capacity for this positive two-level Fock mixture** and the rational resonance spectrum. Other orthogonal Fock-sampling systems and the full order-three polyanalytic kernel \(e^{z\bar w}L_2^1(|z-w|^2)\) have different kernels and are not identified with the family here.

## Limitations

Only the nonnegative weight family \(\tau\ge0\), with the displayed Gaussian normalization, is treated. There is no assertion that these finite orthogonal evaluation families form frames for the infinite-dimensional space, nor any general stability bound under perturbations. Although two-distance geometry and the constituent kernel formulas are known, priority for their exact combination into this parameter phase diagram has not been independently established; closely related sources should be considered before publication. Independent mathematical audit has not been performed.

## References

[1] R. Fulsche and R. Hagger, *Quantum Harmonic Analysis for Polyanalytic Fock Spaces*, arXiv:2308.11292, first public 22 August 2023; *Journal of Fourier Analysis and Applications* 30 (2024), article 63. https://arxiv.org/abs/2308.11292 ; https://doi.org/10.1007/s00041-024-10124-9

[2] H. Harborth and L. Piepmeyer, *Two-Distance Sets and the Golden Ratio*, in *Applications of Fibonacci Numbers* (1993), pp. 279–288. https://doi.org/10.1007/978-94-011-2058-6_27

[3] H. Nozaki and M. Shinohara, *On a Generalization of Distance Sets*, arXiv:0906.0199, especially Proposition 4.16. https://arxiv.org/abs/0906.0199 ; https://ar5iv.labs.arxiv.org/html/0906.0199
