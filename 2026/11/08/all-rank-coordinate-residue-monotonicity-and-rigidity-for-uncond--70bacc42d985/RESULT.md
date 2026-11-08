# All-rank coordinate residue monotonicity and rigidity for unconditional lattice sets

## Finding
Let \(\Lambda=\sum_{j=1}^{d}\mathbb Z b_j\) be a full-rank lattice with a chosen basis. A finite nonempty set \(A\subset\Lambda\) is an **absolute coordinate ideal** if for each \(\sum a_j b_j\in A\) and each integer vector \(z\) satisfying \(|z_j|\le|a_j|\) for every coordinate, \(\sum z_jb_j\in A\).

Let \(\varnothing\ne J\subseteq\{1,\ldots,d\}\), let \(q_j\) be any positive integers indexed by \(J\), set \(k=|J|\), and put \(\Gamma=\sum_{j\in J}q_j\mathbb Z b_j\). Write \(D_r=\#\{a+r\Gamma:a\in A\}\) for integers \(r\ge1\). Then
\[
\frac{D_r}{r^k}\ge\frac{D_s}{s^k}\qquad(1\le r<s).
\]
For each integer vector \(y\) in the complementary coordinates \(J^c\), let \(A_y\subset\mathbb Z^J\) be its coordinate section. Equality holds **exactly** when every nonempty \(A_y\) contains the entire box
\[
B_s=\left\{z\in\mathbb Z^J:|z_j|\le\left\lfloor\frac{s q_j}{2}\right\rfloor\ (j\in J)\right\}.
\]
In particular, this is an all-rank discrete-monotonicity theorem with a complete equality characterization for unconditional convex lattice bodies and, more generally, finite absolute coordinate ideals.

## Assumptions and scope
The basis is fixed; neither orthonormality nor unimodularity relative to an ambient integer-coordinate system is assumed. The subgroup is **coordinate** in this basis, but its positive index multipliers \(q_j\) can differ. Empty coordinate sections do not enter the equality criterion. Theorem includes all ranks \(1\le k\le d\); new high-rank cases are \(k\ge3\).

A compact convex set \(K\subset\mathbb R^d\) is unconditional in this basis if flipping the signs of any subset of its basis coordinates preserves \(K\). If \(a\in K\) and \(|z_j|\le|a_j|\) for all \(j\), each coordinate can be independently moved from \(a_j\) to \(z_j\) by a convex combination of the two sign choices. Thus \(A=K\cap\Lambda\) is a finite absolute coordinate ideal when nonempty. No nonempty-interior hypothesis is needed.

## Proof
**Step 1 (centered coset representatives).** For \(n\ge1\) choose, for each class modulo \(n\), an integer representative of minimum absolute value; for even \(n\), break the tie at \(n/2\) by choosing the positive representative. Its absolute value ranges from \(0\) to \(\lfloor n/2\rfloor\). Because each section \(A_y\) is an absolute coordinate ideal, a residue class modulo the product moduli \(n_j=rq_j\) meets \(A_y\) if and only if its centered representative belongs to \(A_y\). Coordinatewise shrinking cannot leave an absolute ideal, and signs are immaterial.

**Step 2 (a product-probability identity).** Let \(U_n\) denote the absolute value of a uniformly selected centered residue modulo \(n\). The variables \(U_{n_j}\) are taken independently. If \(Y\) is the finite set of complementary-coordinate indices of nonempty sections, then
\[
D_r=\biggl(\prod_{j\in J}rq_j\biggr)
 \sum_{y\in Y}\mathbb P\!\left((U_{rq_j})_{j\in J}\in A_y\right),
\]
where the section condition means the nonnegative absolute-coordinate representative belongs to \(A_y\). Hence
\[
\frac{D_r}{r^k}=\biggl(\prod_{j\in J}q_j\biggr)
 \sum_{y\in Y}\mathbb P\!\left((U_{rq_j})_{j\in J}\in A_y\right).
\]

**Step 3 (stochastic monotonicity).** For each integer \(t\ge0\), an elementary enumeration of centered residues gives
\[
\mathbb P(U_n\le t)=\min\left\{1,\frac{2t+1}{n}\right\}.
\]
Thus \(U_{rq_j}\) is stochastically no larger than \(U_{sq_j}\) whenever \(r<s\). Couple the two vectors with independent uniform quantiles, coordinate by coordinate, so that every first coordinate is at most its corresponding second coordinate. Since each nonnegative section is a coordinate order ideal, membership for the larger vector implies membership for the smaller. All summands in Step 2 are nonincreasing, proving the inequality.

**Step 4 (strictness and equality).** Fix a nonempty section \(A_y\). If it contains \(B_s\), the centered residue vectors for both moduli are always in this section, so each probability equals one. Conversely, suppose \(B_s\not\subseteq A_y\). Choose a missing nonnegative vector \(w\in B_s\) of minimal coordinate sum. As \(0\in A_y\), some coordinate \(j\) satisfies \(w_j\ge1\); by minimality, \(w-e_j\in A_y\). Since \(w\notin A_y\), the section of \(A_y\) in coordinate \(j\) with other coordinates fixed at \(w_{-j}\) is precisely the integer interval from \(0\) through \(w_j-1\). For \(t=w_j-1<\lfloor s q_j/2\rfloor\), the displayed cumulative-distribution formula gives a strict inequality
\[
\mathbb P(U_{rq_j}\le t)>\mathbb P(U_{sq_j}\le t).
\]
Replace the \(s\)-modulus absolute-value coordinate distributions by the \(r\)-modulus ones one at a time, choosing coordinate \(j\) first. Every replacement weakly increases probability of the downset. At the first replacement, the other coordinates have their \(s\)-modulus distributions, which assign positive probability to \(w_{-j}\). The conditional gap just displayed makes the first increase strict. Therefore the section contribution is strictly greater at \(r\) than at \(s\). Summing the nonnegative differences over sections gives exactly the stated equality condition. \(\square\)

## Verification
The included Python-standard-library program `verify_unconditional_residues.py` constructs finite absolute-coordinate ideals and lattice \(\ell_1\)-balls in dimensions one through four. It compares direct modular-coset enumeration with centered-residue enumeration, checks normalized inequalities and the complete equality-box criterion for moduli one through five, and reproduces an illustrative full-rank three-dimensional series.

Its output is
```
ABSOLUTE_IDEALS_OK cases=416 monotonic_pairs=1664 strict=1533 equal=131 formula_checks=2080
THREE_DIMENSIONAL_L1_COUNTS 1,7,19,22,25
EQUALITY_BOX_CHECKS 1664
```
For \(A=\{z\in\mathbb Z^3:\|z\|_1\le2\}\), \(\Gamma=\mathbb Z^3\), and moduli \(r=1,2,3,4,5\), the represented-coset counts are \(1,7,19,22,25\), respectively. These finite experiments do not establish the universal theorem; Steps 1–4 do.

## Relationship to prior work
Malikiosis introduced discrete monotonicity of normalized residue counts as a sufficient criterion in the geometry-of-numbers study of successive minima. Xue proved the inequality for **every** compact convex set and **every** subgroup of rank at most two in arbitrary ambient dimension (Theorem 1.1), and described its equality behavior (Remark 5.3). Those lower-rank conclusions are prior work. The present result supplies a distinct sufficient geometric structure, unconditionality plus a coordinate subgroup, which allows **all** ranks, including rank three and higher, and gives the explicit centered-box equality criterion. It does not imply Xue's unrestricted rank-two result, nor does that result imply the higher-rank cases here.

## Limitations
The subgroup must be generated by scaled elements of the chosen unconditionality basis; arbitrary skew subgroups are not treated. The result does not establish the full discrete monotonicity property for all convex bodies in rank three or higher. The argument proves a sufficient condition rather than an exact characterization of every body enjoying monotonicity. An equivalent theorem might occur in earlier work on absolute ideals, residue projections, or finite probability orders; independent historical-priority verification has not been performed.

## References
1. F. Xue, *The Discrete Monotonicity Property in Rank Two*, arXiv:2610.39026v1, first posted 2026-10-28, https://arxiv.org/html/2610.39026v1. In particular Theorem 1.1, Lemma 2.1 and Remark 5.3.
2. R.-D. Malikiosis, *A Discrete Analogue for Minkowski's Second Theorem on Successive Minima*, arXiv:1001.3729v1, first posted 2010-01-21, https://arxiv.org/pdf/1001.3729. In particular the discrete monotonicity formulation and its relation to successive minima.
