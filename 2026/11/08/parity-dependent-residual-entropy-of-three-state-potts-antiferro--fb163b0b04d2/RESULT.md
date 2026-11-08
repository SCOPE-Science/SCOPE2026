# Parity-dependent residual entropy of three-state Potts antiferromagnets on Mycielskian cycles

## Finding

For every integer \(n\ge4\), let \(G_n=\mu(C_n)\) be the ordinary Mycielskian of the cycle on \(n\) vertices. For the **zero-field, uniform, classical three-state antiferromagnetic Potts model** with coupling \(J>0\), the exact ground-state energy is

\[
E_0(G_n)=\begin{cases}0,&n\text{ even},\\ J,&n\text{ odd}.\end{cases}
\]

Let \(N_n\) denote the number of *labeled* ground-state spin configurations, with no quotient by graph automorphisms or color permutations. Let \(\rho_1,\rho_2,\rho_3\) be the three distinct positive roots of

\[
f(\rho)=\rho^3-5\rho^2+6\rho-1.
\]

For every \(k\ge2\), the exact multiplicities are

\[
\boxed{N_{2k}=6\sum_{i=1}^3\rho_i^k,\qquad N_{2k+1}=3(2k+1)a_k,}
\]

where the integer sequence \(a_k\) is defined for all \(k\ge0\) by

\[
a_0=4,\quad a_1=12,\quad a_2=44,\qquad
a_{k+3}=5a_{k+2}-6a_{k+1}+a_k,
\]

or equivalently by its exact generating function

\[
\boxed{\sum_{k\ge0}a_k y^k=\frac{4-8y+8y^2}{1-5y+6y^2-y^3}.}
\]

In particular, the exact counts for \(n=4,5,6,7,9\) are \(78,660,228,3192,\) and \(13716\), respectively. The \(n=5\) count is an existing finite-graph result and is **not** a separate novelty claim here. The result is the full parity-dependent formula for the infinite Mycielskian-cycle family.

The graphs have \(2n+1\) vertices. Their common per-vertex logarithmic ground-state growth rate exists along both parities and equals

\[
\lim_{n\to\infty}\frac{\log N_n}{2n+1}
=\frac14\log\rho_{\max}=0.29443130288084\ldots,
\qquad\rho_{\max}=3.24697960371747\ldots.
\]

The odd-cycle branch has an additional factor proportional to the cycle length, arising from the location of the unavoidable frustrated bond; this is a finite-size logarithmic entropy correction, not a thermodynamic phase transition claim.

## Assumptions and scope

Use vertices \(a_i,b_i\) for \(i\in\mathbb Z/n\mathbb Z\), plus an apex \(w\). The edges are \(\{a_i,a_{i+1}\}\), \(\{b_i,a_{i-1}\}\), \(\{b_i,a_{i+1}\}\), and \(\{b_i,w\}\), for each \(i\), giving exactly \(4n\) edges. Every site has a spin \(\sigma_v\in\{0,1,2\}\). The energy is

\[
H(\sigma)=J\sum_{\{u,v\}\in E(G_n)}\mathbf 1_{\{\sigma_u=\sigma_v\}}.
\]

There is no external field, no disorder, no boundary coupling beyond the edges specified above, and \(J>0\). Every spin configuration is counted individually, including those related by rotations, reflections, or global color permutations.

## Proof

**1. Minimum number of unsatisfied bonds.** The Mycielski construction raises chromatic number by one. For completeness: if a proper coloring of \(\mu(G)\) uses \(q\) colors and the apex receives color \(c\), then none of its cloned neighbors has color \(c\). Recolor each original vertex of color \(c\) by its clone's color. Every original edge remains properly colored, giving a \((q-1)\)-coloring of \(G\). Conversely, copy a proper coloring of \(G\) to the clones and give the apex one new color. Therefore \(\chi(\mu(G))=\chi(G)+1\).

For even \(n\), \(\chi(C_n)=2\), and hence \(G_n\) is properly three-colorable; its minimum energy is zero. For odd \(n\), \(\chi(C_n)=3\), so \(G_n\) is four-chromatic and every three-state spin assignment has at least one monochromatic edge. To attain exactly one, alternately color the original odd cycle with spins \(0\) and \(1\), leaving one monochromatic original edge; give all clones spin \(2\) and the apex spin \(0\). All other edges are unfrustrated. Thus the odd minimum is exactly \(J\).

**2. Nine-state transfer identity.** Put \(t\) for the formal weight of a monochromatic edge, so the zero-field Potts polynomial is \(Z_n(t)=\sum_\sigma t^{H(\sigma)/J}\). By color symmetry fix the apex to spin \(0\), then multiply by three. For \(a,b,c\in\{0,1,2\}\), define a transfer matrix indexed by ordered pairs of original-cycle spins as

\[
T(t)_{(a,b),(b,c)}
=t^{\mathbf1_{\{b=c\}}}\sum_{z=0}^{2}
t^{\mathbf1_{\{z=0\}}+\mathbf1_{\{z=a\}}+\mathbf1_{\{z=c\}}},
\]

with all entries not of this pair-transition form equal to zero. The term \(z\) is the independently summed clone spin, coupled to the apex and its two original-cycle neighbors; the prefactor counts one original-cycle bond. Each original and clone edge is counted exactly once around the cycle. It follows for every \(n\ge4\) that

\[
Z_n(t)=3\operatorname{tr}(T(t)^n).
\]

Let \(A=[t^0]T(t)\), \(B=[t^1]T(t)\). A direct exact integer determinant gives

\[
\det(\lambda I-A)
=\lambda^3(\lambda^6-5\lambda^4+6\lambda^2-1)
=\lambda^3\prod_{i=1}^{3}(\lambda^2-\rho_i).
\]

For even \(n=2k\), the zero-energy coefficient is \(3\operatorname{tr}(A^{2k})=6\sum_i\rho_i^k\). For odd \(n=2k+1\), the zero-energy coefficient vanishes and the coefficient of \(t\) is the ground-state multiplicity:

\[
[t]Z_{2k+1}(t)
=3(2k+1)\operatorname{tr}(BA^{2k}),
\]

because the trace of each of the \(2k+1\) first-order insertions is identical by cyclicity.

**3. Exact first-defect recurrence.** Set \(a_k=\operatorname{tr}(BA^{2k})\) and \(Q=A^6-5A^4+6A^2-I\). Direct integer matrix multiplication yields

\[
A^4Q=0,\quad\operatorname{tr}(BQ)=0,
\quad\operatorname{tr}(BA^2Q)=0.
\]

Consequently \(a_{k+3}=5a_{k+2}-6a_{k+1}+a_k\) for all \(k\ge0\): the first two instances follow from the trace identities and all subsequent instances from \(A^{2k}Q=0\). The initial traces are \(a_0=4\), \(a_1=12\), and \(a_2=44\). Multiplying the resulting generating series by its denominator gives the stated numerator \(4-8y+8y^2\). This proves the exact odd count for all odd cycle lengths in the domain.

**4. Growth law.** The cubic \(f\) has one root in each of the disjoint intervals \((0,1/2)\), \((1,2)\), and \((3,4)\); hence its three roots are distinct, real, and strictly positive. The largest root \(\rho_{\max}\) dominates the even expression. For odd lengths, the coefficient of \(\rho_{\max}^k\) in \(a_k\) is \(4.6901433961\ldots>0\), as follows from the simple-pole residue of the displayed rational generating function. Therefore both parities have the same exponential rate and the logarithmic limit follows after dividing by the \(2n+1\) vertices.

## Verification

`verify.py` constructs \(A,B\) directly from the local transfer definition using only integer arithmetic, computes the characteristic polynomial exactly, verifies the three matrix and trace identities, checks both recurrence sequences, and independently enumerates all spin configurations for \(n=4,5,6\). The separately implemented `bruteforce.cpp` exhaustively counts all \(3^{2n+1}\) configurations for \(n=4,5,6,7\) without using the transfer matrices. Both programs were executed successfully on these exact embedded sources. Run `python3 verify.py`, or build and run `c++ -O3 -std=c++17 bruteforce.cpp -o brute && ./brute`.

The finite enumerations corroborate the formulas but are not used as proofs for unbounded \(n\). The recurrence and exact transfer identities establish all cycle lengths stated.

## Relationship to prior work

The Mycielski chromatic-number increase is classical and underlies the unavoidable single odd-cycle frustration. General Potts/Tutte and weighted-coloring identities were established by Chang and Shrock and by Shrock and Xu. A prior exact computation on the eleven-vertex Grötzsch graph establishes the \(n=5\) specialization, while separate Ising results address a different, two-spin-state Hamiltonian on the Mycielskian-cycle family. None of these provides the all-length three-state parity recurrence, its odd first-defect generating function, or the common entropy rate by direct implication without a new transfer evaluation.

## Limitations

Only the uniform, three-state, zero-field, classical model on \(\mu(C_n)\) for integers \(n\ge4\) is classified. The result says nothing about arbitrary Mycielskians, magnetic-field dependence, finite-temperature transitions, or quantum spins. The count is labeled, not symmetry-reduced. The logarithmic growth rate concerns this graph sequence; no Euclidean lattice thermodynamic-limit interpretation is asserted. Broad general graph-polynomial frameworks encode these coefficients implicitly, so exact novelty depends on the absence of a previously evaluated equivalent cycle-family formula; historical unindexed tables and inaccessible manuscripts remain a priority risk. Independent scientific audit has not been performed.

## References

1. S.-C. Chang and R. Shrock, *Some Exact Results on the Potts Model Partition Function in a Magnetic Field*, arXiv:0907.0777v1 (public 2009-07-04), https://arxiv.org/abs/0907.0777.
2. R. Shrock and Y. Xu, *Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings*, arXiv:1009.1182v1 (public 2010-09-07), https://arxiv.org/abs/1009.1182.
3. G. J. Chang, L. Huang and X. Zhu, *Circular chromatic numbers of Mycielski's graphs*, Discrete Mathematics **205** (1999), 23–37, https://doi.org/10.1016/S0012-365X(99)00033-3.
4. A. D. Sokal, *The multivariate Tutte polynomial (alias Potts model) for graphs and matroids*, Surveys in Combinatorics (2005), arXiv:math/0503607, https://arxiv.org/abs/math/0503607.
