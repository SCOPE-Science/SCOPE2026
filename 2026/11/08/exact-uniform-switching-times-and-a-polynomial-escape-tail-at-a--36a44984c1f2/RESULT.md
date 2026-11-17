# Uniform conditional switching and terminal boundary layer at a negative-doubling hole

## Finding and relation to the known survival law

Let
\[
T(x)=\begin{cases}1-2x,&0\leq x<1/2,\\2-2x,&1/2<x\leq1,\end{cases}
\qquad H=(2/5,3/5),
\]
and let \(X_0\) have Lebesgue-uniform distribution on \([0,1]\), \(X_j=T^j(X_0)\), and \(E_n=\{X_j\notin H:0\leq j<n\}\), \(n\geq1\). Endpoint conventions are irrelevant to all stated probability laws. Write
\(I_0=(0,1/5)\), \(I_1=(1/5,2/5)\), \(I_2=(3/5,4/5)\), and \(I_3=(4/5,1)\).

The formula
\[
\Pr(E_n)=\frac{4(n+1)}{5\,2^n}
\tag{1}
\]
**is not new**: it is the \(a=2/5\) case (after a one-step horizon index shift) of the exact 26 October 2026 result *Exact escape-time phase transition for symmetric negative-doubling holes* [1], which also establishes the sharp transition at \(a=1/3\) and the corresponding conditional escape hazard. Equation (1) is included as necessary normalization for the **distinct conditioned spatial and switching-time laws** proved here.

Define \(J_n\) as the least \(j\in\{0,\ldots,n-1\}\) with \(X_j\in I_1\cup I_2\), or \(J_n=n\) if no such visit occurs. The following conditional laws are exact:

1. For every \(n\geq1\) and \(0\leq j\leq n\),
\[
\boxed{\Pr(J_n=j\mid E_n)=\frac1{n+1}.}
\tag{2}
\]
In particular \(J_n/n\) converges weakly, conditioned on \(E_n\), to uniform distribution on \([0,1]\).

2. Put \(\nu_{\mathrm{out}}=(\delta_0+\delta_1)/2\) and \(\nu_{\mathrm{in}}=(\delta_{1/3}+\delta_{2/3})/2\). At each fixed \(0\leq\theta<1\),
\[
\boxed{\mathcal L(X_{\lfloor\theta n\rfloor}\mid E_n)\ \Rightarrow\ (1-\theta)\nu_{\mathrm{out}}+\theta\nu_{\mathrm{in}}.}
\tag{3}
\]

3. At the terminal observed time, \(\mathcal L(X_{n-1}\mid E_n)\) is the mixture of *uniform interval distributions* on \(I_0,I_1,I_2,I_3\) with respective masses
\[
\boxed{\frac{(1,n,n,1)}{2(n+1)}.}
\tag{4}
\]
Writing \(\nu_*\) for the uniform probability on \(I_1\cup I_2\),
\[
\boxed{\|\mathcal L(X_{n-1}\mid E_n)-\nu_*\|_{\mathrm{TV}}=\frac1{n+1}.}
\tag{5}
\]
This nonatomic terminal limit differs from the atomic limit (3) at every fixed macroscopic fraction \(\theta<1\).

For comparison, at the other natural zero-entropy boundary \(H=(1/3,2/3)\), the already known survival law is \(4/(3\,2^n)\) [1]; a two-branch argument also shows the terminal conditional position is uniform on \((0,1/3)\cup(2/3,1)\) for every \(n\). The new contribution is **not** the escape exponent, its exact tail, or the hazard, but (2)--(5), including the singular time-to-terminal boundary layer.

## Assumptions and boundaries

The map is defined on the interval, not the circle; the open hole is removed at each observation time \(0,\ldots,n-1\). The initial measure is Lebesgue measure on all of \([0,1]\), not normalized on the safe set, and the conditioning event is \(E_n\). All assertions are insensitive to endpoint orbits of zero Lebesgue mass. Convergence in (3) is weak; (5) is total variation. No claim of a general parameter-neighborhood theory, nonuniform initial law, or positive-doubling analogue is made.

## Proof

**Four-cell dynamics.** The images under \(T\) of \(I_0,I_1,I_2,I_3\) are, respectively, \((3/5,1)\), \((1/5,3/5)\), \((2/5,4/5)\), and \((0,2/5)\). Hence the positive-length safe transitions are
\[
I_0\to I_2,I_3,\qquad I_1\to I_1,\qquad I_2\to I_2,\qquad I_3\to I_0,I_1.
\]
The matrix, with rows indexed by source cells, is
\[
A=\begin{pmatrix}0&0&1&1\\0&1&0&0\\0&0&1&0\\1&1&0&0\end{pmatrix}.
\tag{6}
\]
Each indicated branch is affine with slope of absolute value two and covers the entire destination cell. Thus every admissible \(n\)-cell itinerary corresponds to an interval of initial conditions of *equal length* \(1/(5\,2^{n-1})\); different itinerary interiors are disjoint.

**Switching-time law.** Until the first visit to an inner cell \(I_1\cup I_2\), a safe path alternates deterministically between \(I_0\) and \(I_3\). Once in either inner cell it stays there along its unique safe transition. For each \(j=0,\ldots,n\), exactly two admissible paths have first entry at \(j\), with \(j=n\) meaning none within the horizon. Consequently there are \(2(n+1)\) equal-length initial cylinders. Counting their measures reproduces the *previously established* (1) and normalizing gives (2), independent of \(n\). The weak uniform limit for \(J_n/n\) follows from uniform Riemann sums.

**Macroscopic conditional spatial law.** Conditioned on \(J_n=j\), the two paths are related by reflection \(x\mapsto1-x\), yielding equal paired weights. At time \(t=\lfloor\theta n\rfloor\), if \(j>t\) then the state follows the surviving outer alternating branches for another \(j-t\) steps, so inverse contraction by \(1/2\) bounds its distance from the outer two-cycle \(\{0,1\}\) by a constant times \(2^{-(j-t-1)}\). If \(j\le t\), the state remains in an inner self-branch for \(n-1-t\) subsequent safe steps, and is within a constant times \(2^{-(n-1-t)}\) of one of the two fixed points \(1/3,2/3\). For fixed \(\theta<1\), the \(O(1)\)-width transition layer in \(j\) has conditional probability tending to zero; \(\Pr(J_n\le t\mid E_n)=(t+1)/(n+1)\to\theta\). Paired reflection weights then prove (3).

**Terminal law.** The exact terminal cell-path count is
\[
\mathbf1^\top A^{n-1}=(1,n,n,1),\qquad n\ge1,
\tag{7}
\]
as follows either by induction from (6) or by direct path classification. For each terminal cell, all admissible initial cylinder restrictions are mapped affinely *onto the whole terminal cell*. Pushing their equal-length uniform masses forward therefore gives a uniform distribution on that cell, not merely a cell probability. Dividing (7) by \(2(n+1)\) proves (4). The total mass assigned to the two outer cells is \(1/(n+1)\); the inner-cell density rescales by the complementary amount. Therefore the total variation distance to the equally weighted inner-cell limit is exactly \(1/(n+1)\), proving (5).

**Comparison boundary.** For hole \((1/3,2/3)\), the two safe intervals alternate under the only surviving full branches, giving exactly two length-\(n\) cylinders of length \(1/(3\,2^{n-1})\), and both terminal cells are uniformly occupied with equal mass. This agrees with the established tail formula [1] and gives the stated terminal distribution.

## Verification

The accompanying immutable `verify_escape.py` independently iterates exact-rational inverse-image interval unions for both holes and checks the survival identities for each \(1\le n\le25\); it also checks terminal matrix counts, switching counts and total-variation distances. A further independent audit enumerated all admissible paths for each \(1\le n\le16\), obtaining exactly two paths for every \(J_n\) and terminal counts \((1,n,n,1)\). These bounded computations support but do not replace the all-horizon argument above.

## Prior work and originality boundary

[1] *Exact escape-time phase transition for symmetric negative-doubling holes*, first published 26 October 2026, https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-exact-escape-time-phase-transition-for-symmetric-negative-doubli--ca3ad35b54de . Its full result and proof establish \(\Pr(E_n)=4(n+1)/(5\,2^n)\) under the present time-index convention, the exact \((1/3,2/3)\) law and the corresponding hazard. These parts are **covered** and are explicitly excluded from the originality claim. However, its theorem and proof give scalar Lebesgue survival probabilities and do not state a uniform *conditional first-entry time*, position at fractional horizons, or a terminal uniform interval law; scalar tails alone do not determine these conditional path and spatial distributions.

[2] Y. Ding, W. Steiner and Y. Sun, *Open dynamical systems in topologically expansive decreasing Lorenz maps*, arXiv:2610.03327v1, 2 October 2026, https://arxiv.org/abs/2610.03327 . This supplies symbolic survivor and entropy/dimension classifications, not the exact conditioned position laws (2)--(5) in its accessible statements. Full primary text was not retrievable during the independent comparison; it is a remaining priority risk.

[3] P. Glendinning and N. Sidorov, *The doubling map with asymmetrical holes*, arXiv:1302.2486, https://arxiv.org/abs/1302.2486 . The positive-doubling orientation differs from the present map.

General conditionally invariant, quasi-stationary and transfer-operator literature may contain equivalent descriptions under other terminology, so historical priority for (2)--(5) is a best-of-knowledge assessment only. The phase-transition novelty and known escape formulas of [1] are not asserted anew. No independent expert or formal certification is claimed.
