# Exact stationary-state growth on three-row cyclic-dominance tori

## Finding

Consider the three-color, threshold-four Moore cellular automaton on the periodic \(3\times N\) lattice, with \(N\ge 3\). Write \(F_N\) for the total number of spatial configurations fixed by one simultaneous update. Let \(P,Q\) be the two monic polynomials of degree 18 specified below by their coefficient lists in descending powers. Then, for **every** integer \(N\ge3\),

\[
 F_N=6^N+\sum_{P(\alpha)=0}\alpha^N+2\sum_{Q(\beta)=0}\beta^N,
\]

where each complex root is included with algebraic multiplicity. The first counts are

\[
(F_3,F_4,F_5,F_6,F_7,F_8,F_9,F_{10})=
(2070,9636,67263,548688,4246827,35421972,292865328,2430735969).
\]

There is a unique Perron eigenvalue \(\lambda\) satisfying \(8.6245<\lambda<8.6246\), and it is the largest positive root of \(P\). One has
\[
F_N=\lambda^N(1+O(\rho^N)),\qquad 0<\rho<1,
\]
for a constant \(\rho\) independent of \(N\). In particular, the exponential growth rate of fixed configurations per column is \(\log\lambda\); their fraction among all \(27^N\) configurations tends to zero exponentially.

The exact polynomial specification is

```text
P descending coefficients:
[1,-18,121,-528,2397,-9207,21654,-54108,232146,-476280,-302535,1574640,1686177,728271,-39149487,77944680,-36137988,-25509168,19131876]
Q descending coefficients:
[1,3,13,-132,-717,-4320,-7695,-1134,134946,454653,898128,-164025,-3726648,-11081529,-11868849,-13463172,11691702,12754584,19131876]
```

Thus if \(\widetilde P(z)=z^{18}P(1/z)\), \(\widetilde Q(z)=z^{18}Q(1/z)\), the corresponding spatial fixed-point shift has rational dynamical zeta function
\[
\zeta(z)=\frac{1}{(1-6z)\widetilde P(z)\widetilde Q(z)^2}.
\]
For this last formula, the spatial shift is defined on the infinite three-row strip; its periods one and two are interpreted with repeated *neighbor positions*, not as an eight-distinct-neighbor finite torus. The displayed counts of actual finite Moore tori apply only for \(N\ge3\).

## Assumptions and scope

Write sites as \((r,j)\in\mathbb Z/3\mathbb Z\times\mathbb Z/N\mathbb Z\), with states \(s(r,j)\in\{0,1,2\}\). There are eight distinct Moore neighbors of each site when \(N\ge3\). The update changes color \(i\) to \(i+1\pmod3\) if and only if at least four neighbors have successor color, and otherwise preserves it. All configurations are counted as labeled configurations, not modulo translations, row permutations, or color rotations.

Define the ten column-count types
\[
\mathcal C=\{a=(a_0,a_1,a_2)\in\mathbb Z_{\ge0}^3:a_0+a_1+a_2=3\},\quad
w(a)=\frac{3!}{a_0!a_1!a_2!}.
\]
Columns of the same type may have different vertical orders; exactly \(w(a)\) vertical orders exist. All color subscripts below are understood modulo three.

## Proof

**1. Local stationary criterion.** For three consecutive columns with count types \(a,b,c\), a site in the middle column of color \(i\) sees exactly \(a_{i+1}+b_{i+1}+c_{i+1}\) successor-color neighbors: all three sites of the preceding column, all three of the following column, and the other two in its own column. The middle site itself is not of successor color. Consequently the middle column is fixed if and only if
\[
\forall i\in\{0,1,2\}\text{ with }b_i>0:\quad a_{i+1}+b_{i+1}+c_{i+1}\le3. \tag{1}
\]
This criterion depends only on the three *count types*, not on their internal vertical ordering.

**2. A weighted 100-state transfer.** Index a matrix \(B\) by ordered pairs \((a,b)\in\mathcal C^2\), and set
\[
B_{(a,b),(b',c)}=\begin{cases}w(c),&b=b'\text{ and (1) holds},\\0,&\text{otherwise}.\end{cases} \tag{2}
\]
A length-\(N\) closed walk of (2) corresponds to a cyclic column-count sequence satisfying every stationary constraint. Its weight is the product of the \(w\)-multiplicities of the columns. Conversely every ordered fixed configuration contributes to exactly one such weighted closed walk with a specified starting column. Hence
\[
F_N=\operatorname{tr}(B^N)\quad(N\ge3). \tag{3}
\]
Equation (3) holds as a formal spatial-shift periodic-point count for all positive \(N\), subject to the distinct-neighbor qualification above.

**3. Exact spectral identity.** Enumerating \(\mathcal C\) lexicographically and evaluating the explicit indicator (2) gives a 100-state integer matrix with 496 nonzero entries. An exact symbolic determinant computation, reproduced from the construction in the accompanying program, yields
\[
\det(XI_{100}-B)=X^{45}(X-6)P(X)Q(X)^2. \tag{4}
\]
No numerical spectral approximation enters (4); the verification program generates the matrix from (1), calculates its characteristic polynomial in exact integers, and compares *every* coefficient with the claimed factorization. Taking powers of the eigenvalues in (4) and using (3) proves the all-\(N\) formula. Newton's identities alternatively give a finite linear recurrence and the rational spatial zeta function by \(\det(I-zB)^{-1}\).

**4. Sharp exponential rate.** The directed support graph of \(B\) has precisely two recurrent strongly connected components: one of size 72, and a singleton with self-loop weight six. Every other component is acyclic. The size-72 component has a self-loop and is strongly connected, so its nonnegative adjacency matrix is primitive. Its characteristic polynomial is \(X^{18}P(X)Q(X)^2\). The Perron eigenvalue is simple; since the roots of \(Q\) have even multiplicity, that eigenvalue must be a root of \(P\). Exact sign and Sturm calculations show that \(P\) has precisely one real root greater than eight, located strictly between \(8.6245\) and \(8.6246\). Therefore it exceeds the singleton eigenvalue six and is the unique dominant eigenvalue of the full matrix. Perron–Frobenius theory proves the stated asymptotic with exponentially small relative error.

## Verification

The standalone Python program `verify_strip.py` reconstructs all ten count types and all 496 weighted transitions, checks graph recurrence and the exact 100-by-100 characteristic polynomial (4), computes weighted walk traces through \(N=10\), independently enumerates all ordered configurations of the genuine \(3\times3\) and \(3\times4\) Moore tori, and certifies the Perron-root interval by rational signs and Sturm root counts. It uses Python 3.10+ with SymPy. The two independent finite enumerations give \(F_3=2070\) and \(F_4=9636\); these are consistency checks on, not replacements for, the all-length transfer proof. Running the supplied code produces four `VERIFY_OK` lines.

## Relationship to prior work

Muñoz and Nuño (2026) define this exact three-color Moore-threshold dynamics, investigate symmetry-resolved temporal periods and sample fixation basins on larger square tori and a rectangular torus; they do not give a three-row stationary-state zeta or exact all-width counts in the inspected full text. Fisch, Gravner and Griffeath's cyclic cellular automata provide the original threshold-dynamics context. Jen (1988) and Banks–Djirar (1992) describe general graph/transfer methods for counting cellular-automaton fixed points. Formula (2) uses that established kind of method rather than claiming transfer enumeration itself as new. The specific count-compression, factorization (4), all-width explicit sequence and exact growth constant are the object-specific contribution.

## Limitations

The theorem is about time-fixed configurations on width-three **periodic** strips at three colors and threshold four, not about convergence to fixation, temporal cycles, wider strips, spatially twisted boundaries, or stochastic initial states. Neither the sampled basin percentages in the motivating paper nor the fixed count implies a global attraction statement. Full priority against unindexed enumerations is not guaranteed. The spectral-polynomial certificate requires the stated SymPy dependency; the proof's local-to-transfer reduction is independent of software.

## References

- F. J. Muñoz and J. C. Nuño, *Symmetry-resolved periods in a cyclic-dominance automaton: separating intrinsic from lattice-induced periodicity*, arXiv:2610.37990v1 (27 October 2026), https://arxiv.org/html/2610.37990v1.
- R. Fisch, J. Gravner and D. Griffeath, foundational cyclic cellular automata papers cited in Muñoz–Nuño, including the box-neighborhood threshold formulation; see references 9–10 in https://arxiv.org/html/2610.37990v1.
- E. Jen, *Cylindrical cellular automata*, Communications in Mathematical Physics **118** (1988), 569–590, DOI:10.1007/BF01221109.
- S. P. Banks and S. Djirar, *Fixed Points and Shift Cycles in Cellular Automata*, ACSE Research Report 459 (1992), https://eprints.whiterose.ac.uk/id/eprint/79286/.
