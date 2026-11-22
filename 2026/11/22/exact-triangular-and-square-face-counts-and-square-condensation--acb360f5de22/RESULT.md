# Exact triangular and square face counts and square-condensation law for panhandle matroid polytopes

## Finding

Let \(2\le r\le p\) and \(t\ge2\) be integers, and let \(P_{r,p,t}\) be the standard Euclidean base polytope of the panhandle matroid \(\operatorname{Pan}_{r,p,p+t}\). All two-dimensional faces have intrinsic Euclidean area \(\sqrt3/2\) or \(2\), respectively for equilateral triangles and squares. The exact respective multiplicities are

\[
\begin{aligned}
Q_{r,p,t}&=\binom p2\binom t2\binom{p-2}{r-2},\\
T_{r,p,t}&=\binom p{r-1}\binom{p+t-r+1}3
+\binom p3\binom{p-3}{r-2}\\
&\quad+t\binom p2\binom{p-2}{r-2}
+t\binom p3\binom{p-2}{r-2}.
\end{aligned}
\]

Fix \(r\) and let \(p,t\to\infty\) with \(p/(p+t)\to\alpha\in(0,1)\). If a two-face is chosen uniformly from the finite set of two-faces, its square probability converges to

\[
\Phi_r(\alpha)=\frac{3(r-1)\alpha(1-\alpha)^2}{2+2(r-1)\alpha^2(1-\alpha)+3(r-1)\alpha(1-\alpha)^2}.
\]

For every \(r\ge2\), this limiting frequency is maximized at a **unique** fraction \(\alpha_r\in(0,1/3)\), characterized as the sole root in that interval of

\[
(r-1)\alpha_r^2(1-\alpha_r)+3\alpha_r-1=0.
\]

As \(r\to\infty\), the optimizers and optimal frequencies obey

\[
\alpha_r=(r-1)^{-1/2}+O(r^{-1}),\qquad
\max_{0<\alpha<1}\Phi_r(\alpha)=1-\frac{4}{3\sqrt{r-1}}+O(r^{-1}).
\]

Thus a natural sequence of increasingly high-rank panhandle polytopes has an asymptotic two-face distribution almost entirely concentrated on squares, even though all ranks also admit triangles.

## Assumptions and scope

Use the standard Euclidean metric inherited from orthonormal coordinates in \(\mathbb R^{p+t}\). The panhandle bases are precisely the \(r\)-subsets containing at most one element of the last \(t\) labels. Equivalently, as established by Hanely et al.,

\[
P_{r,p,t}=\left\{x\in[0,1]^{p+t}:\sum_{i=1}^{p+t}x_i=r,\quad \sum_{i=p+1}^{p+t}x_i\le1\right\}.
\]

All formulas are exact for the stated integer domain. The fixed-rank limit requires \(p,t\to\infty\) with a strictly interior ratio; the subsequent large-rank statement concerns the optimization of that already-defined limiting function, not an unproved simultaneous limit for arbitrary rank-growth sequences. Binomial coefficients outside their natural range are defined as zero.

## Proof

**All possible two-face shapes.** A previously established general theorem on matroid base polytopes says that each two-face in standard incidence coordinates is either an equilateral triangle or a square, with edge length \(\sqrt2\). Their intrinsic areas are \(\sqrt3/2\) and \(2\). We use this theorem as background, not as a new result.

**Face enumeration.** A nonempty face is the set where some of the displayed coordinate bounds and possibly the tail-cap inequality are tight. The face is determined by its vertices and, in its relative interior, by the unique set of nonconstant coordinates. We partition two-faces as follows.

1. **Rank-one coordinate triangles, with no tail coordinate fixed to one.** Three coordinates are free. If \(a\) of them lie in the head, there are \(\binom pa\binom t{3-a}\) choices for those coordinates and \(\binom{p-a}{r-1}\) ways to fix the selected head coordinates. Their contribution is
   \[
   \sum_{a=0}^{3}\binom pa\binom t{3-a}\binom{p-a}{r-1}
   =\binom p{r-1}\binom{p+t-r+1}{3}.
   \]
   The equality follows by choosing the fixed \(r-1\) head coordinates first (Vandermonde's identity).

2. **Rank-two coordinate triangles, with no tail coordinate fixed to one.** Three coordinates are free, of which at most one may lie in the tail. Either all three are head coordinates, giving \(\binom p3\binom{p-3}{r-2}\), or two are head and one is tail, giving \(t\binom p2\binom{p-2}{r-2}\). The other potential rank-two coordinate triangles are cut off by the tail cap and cease to be two-dimensional faces.

3. **Triangles with one tail coordinate fixed to one.** All other tail coordinates are fixed to zero and exactly three head coordinates are free. Their residual head rank is one or two. This contributes
   \[
   t\binom p3\left(\binom{p-3}{r-2}+\binom{p-3}{r-3}\right)
   =t\binom p3\binom{p-2}{r-2}.
   \]

4. **Squares on the tight tail cap.** In a square, two head and two tail coordinates are free, with residual rank one in each block; all other tail coordinates are zero and exactly \(r-2\) of the remaining head coordinates are one. This gives
   \[
   \binom p2\binom t2\binom{p-2}{r-2}
   \]
   squares. Each is the orthogonal Cartesian product of two segments of length \(\sqrt2\), hence has area \(2\).

These are exhaustive: when the cap is slack on a relative interior, a two-face has exactly three free coordinates and residual rank one or two. When it is tight, two free coordinates are needed in each nontrivial head/tail factor to obtain a square; if one block is fixed, three free coordinates in the other block produce one of the triangles already listed. Any two-face with all its tail coordinates fixed at zero or a single one is included in the three-coordinate cases. Distinct choices give distinct faces because they have different fixed/nonconstant coordinate patterns. Summing the three triangle contributions and the squares proves the finite formulas.

**Proportional limit.** Put \(N=p+t\) and \(k=r-1\). For fixed \(r\) and \(p/N\to\alpha\), the two counts have asymptotic expansions

\[
\begin{aligned}
T_{r,p,t}&=\frac{\alpha^{r-1}N^{r+2}}{6(r-1)!}
\left(1+k\alpha^2(1-\alpha)+o(1)\right),\\
Q_{r,p,t}&=\frac{\alpha^{r-1}N^{r+2}}{4(r-1)!}
\left(k\alpha(1-\alpha)^2+o(1)\right).
\end{aligned}
\]

Their ratio gives \(\Phi_r\). Direct differentiation, simplifying only by positive denominators for \(0<\alpha<1\), yields that the sign of \(\Phi_r'(\alpha)\) equals the sign of

\[
1-3\alpha-k\alpha^2(1-\alpha).
\]

This expression decreases strictly on \((0,1/3)\), from a positive to a negative value, and is negative on \([1/3,1)\). Thus the unique root is the unique global maximum. Its defining equation implies \(\alpha_r\sqrt{k}\to1\), and the bound \(\alpha_r=k^{-1/2}+O(k^{-1})\) follows by expansion. Finally

\[
\frac{1-\Phi_r(\alpha)}{\Phi_r(\alpha)}
=\frac{2\{1+k\alpha^2(1-\alpha)\}}{3k\alpha(1-\alpha)^2}.
\]

For \(\alpha=c/\sqrt{k}\) this is \(\frac{2}{3\sqrt{k}}(c+c^{-1})+O(k^{-1})\). The unique minimizing \(c\) is one, giving the displayed sharp leading deficit \(4/(3\sqrt{k})\).

## Verification

The accompanying self-contained `verify_panhandle_two_faces.py` uses integer and rational arithmetic to generate all bases, intersect the original supporting hyperplanes, compute affine face ranks, and independently count their polygons. It exactly matches the formulas for eight cases: \((p,t,r)=(2,2,2),(3,2,2),(3,3,2),(3,3,3),(4,2,2),(4,3,2),(4,3,3),(4,3,4)\). It also checks the two binomial simplifications across 315 parameter triples. Run `python3 verify_panhandle_two_faces.py`; the expected completion marker is `PANHANDLE_TWO_FACE_EXACT_PASS`. These finite checks corroborate but do not replace the all-parameter proof.

For example, at \((p,t,r)=(4,3,3)\), the complete two-face spectrum comprises \(124\) equilateral triangles and \(36\) squares, in exact agreement with independent face enumeration.

## Relationship to prior work

Hanely et al. (first posted 2022-01-28) give the panhandle matroid's basis definition and the exact box–hyperplane–cap inequality description (their Proposition 4.4), and study its Ehrhart theory. Pegel (2012, Theorem 2.17, citing BGW 2003) establishes the universal triangle/square restriction for **all** matroid base polytopes. An, Jung and Kim (first posted 2017-01-02) characterize faces of lattice-path matroid polytopes, providing a general combinatorial framework. Ferroni and Schröter (first posted 2023-10-09, Theorem 2.5 and related examples) derive general face-count formulas for split matroids and explicitly count square faces in a different sparse-paving family. In particular, the unrefined two-face count is within the broader reach of their machinery; it is not asserted as independent of it.

The present specific contribution is the evaluated triangle/square multiplicity pair for panhandles, and especially the sharp **rank-dependent optimal square-frequency law**, its unique head-fraction optimizer and the high-rank square-condensation rate. These are not stated in the inspected sources, although they are potentially derivable by specializing more general face-decomposition methods; historical priority therefore remains provisional.

## Limitations

No claim is made that the triangle/square shape theorem itself is new. The asymptotics apply in the ordered fixed-rank then large-rank sense stated above. Finite computation cannot prove all-dimensional enumeration. Published general face enumeration results might permit a different derivation of parts of the formulas, and an unindexed specialization of the exact optimization result remains possible. This result has received no independent mathematical audit.

## References

- D. Hanely, J. L. Martin, D. McGinnis, D. Miyata, G. D. Nasr, A. R. Vindas-Meléndez, M. Yin, *Ehrhart Theory of Paving and Panhandle Matroids*, arXiv:2201.12442, first posted 2022-01-28. https://arxiv.org/abs/2201.12442
- L. Ferroni, B. Schröter, *Face enumeration for split matroid polytopes*, arXiv:2310.05487, first posted 2023-10-09. https://arxiv.org/abs/2310.05487
- S. An, J. Jung, S. Kim, *Facial structures of lattice path matroid polytopes*, arXiv:1701.00362, first posted 2017-01-02. https://arxiv.org/abs/1701.00362
- C. Pegel, *Matroid Polytopes*, Bachelor's thesis, Universität Bremen, 2012, Theorem 2.17. https://www.iazd.uni-hannover.de/fileadmin/iazd/Pegel/thesis-matroid-polytopes.pdf
