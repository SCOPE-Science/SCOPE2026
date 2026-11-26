# Exact fastest mixing and edge-orbit transitions on tripartite graphs with two equal parts

## Finding

For any integers \(p,q\ge2\), let \(G=K_{p,p,q}\), the complete tripartite graph with independent parts \(A,B,C\) of sizes \(p,p,q\). Consider every symmetric nonnegative row-stochastic transition matrix \(P\) supported on the graph (self-loops are allowed), and minimize its second-largest eigenvalue modulus
\[
\mu(P)=\left\|P-\frac{\mathbf 1\mathbf 1^{\mathsf T}}{2p+q}\right\|_2.
\]
There exists a globally optimal chain invariant under within-part permutations and interchange of \(A\) and \(B\). Write \(x\) for the probability on each \(A\)-to-\(B\) edge and \(y\) for the probability on each edge from \(A\cup B\) to \(C\). All optimal invariant weights and the **global** optimal SLEM \(\mu_*(p,q)\) are precisely as follows; interval endpoints are included:

| Parameter regime | \(\mu_*(p,q)\) | Optimal \(y\) | All optimal \(x\) |
|---|---|---|---|
| \(2\le q\le p/2\) | \(\frac{2p-q}{6p}\) | \(\frac1{2p}\) | \(\frac{2p-q}{3p^2}\) |
| \(p/2\le q\le p\) | \(\frac{p}{3p+2q}\) | \(\frac2{3p+2q}\) | \(\frac2{3p+2q}\) |
| \(p\le q\le2p\) | \(\frac q{4p+q}\) | \(\frac2{4p+q}\) | \([\frac{2(2p-q)}{p(4p+q)},\frac2{4p+q}]\) |
| \(2p\le q\le4p\) | \(\frac q{4p+q}\) | \(\frac2{4p+q}\) | \([0,\frac{4p-q}{p(4p+q)}]\) |
| \(q\ge4p\) | \(1-\frac{2p}{q}\) | \(\frac1q\) | \(0\) |

At shared endpoints, adjoining rows give exactly the same optimal weights and value. The equal-part edge orbit is positive in **every** invariant optimum for \(q<2p\), optional (zero and positive both permitted) for \(2p\le q<4p\), and absent in **every** invariant optimum for \(q\ge4p\). Moreover, **every unrestricted global optimizer** uses at least one edge between \(A\) and \(B\) when \(q<2p\), while **every unrestricted global optimizer** puts zero weight on **all** such edges when \(q\ge4p\). When \(2p\le q<4p\), unrestricted optimizers exist both with and without positive weights on that entire edge orbit. This also classifies all invariant optimal holdings, because their values are determined by the weights. The all-equal-part case \(q=p\) agrees with the known edge-transitive complete tripartite solution; the substantive contribution is the full imbalanced classification and the nonunique optimizer intervals.

## Assumptions and scope

The graph is simple, undirected, and complete between distinct independent parts. The parameters \(p,q\) range over integers at least two, so every spectral subspace used below is nonempty. Matrix entries may be zero on allowed graph edges. All diagonal holding probabilities must be nonnegative. Stationarity is uniform by symmetry. Global optimality of the value and existence of the displayed chains are asserted without requiring every unrestricted optimizer to respect graph automorphisms. Uniqueness or classification among symmetry-breaking optimizers is **not** asserted.

## Proof

**Reduction by symmetry.** Let \(N=2p+q\) and \(J=\mathbf 1\mathbf 1^{\mathsf T}/N\). Since \(P\mapsto\|P-J\|_2\) is convex and invariant under conjugation by graph automorphisms, averaging any feasible \(P\) over within-part permutations and the interchange \(A\leftrightarrow B\) yields an invariant feasible chain of no larger SLEM. All such invariant chains are parametrized by \(x,y\ge0\), with holding probabilities
\[
h_A=h_B=1-px-qy,\qquad h_C=1-2py.
\]
Consequently feasibility is exactly \(px+qy\le1\) and \(2py\le1\).

**Full spectrum.** Express \(P=I-L\). The Laplacian has eigenvalue zero on constants. On the \(A\)-versus-\(B\) constant contrast the Laplacian eigenvalue is \(E_0=2px+qy\). On the within-part zero-sum subspaces of \(A\) and \(B\) it is \(E_1=px+qy\), of total multiplicity \(2(p-1)\). On the within-\(C\) zero-sum subspace it is \(E_2=2py\), of multiplicity \(q-1\). Finally, on the constant contrast of \(A\cup B\) against \(C\), it is \(E_3=(2p+q)y\). These mutually orthogonal subspaces have dimensions totaling \(N\). Therefore
\[
\mu(x,y)=\max_{0\le j\le3}|1-E_j|,
\quad(E_0,E_1,E_2,E_3)=(2px+qy,px+qy,2py,(2p+q)y).
\]
In particular, \(\mu(x,y)\le t\) is equivalent to the eight linear inequalities \(1-t\le E_j\le1+t\), together with feasibility.

**Sharp lower bounds.** For any feasible candidate with \(\mu(x,y)\le t\), the inequalities \(E_0\le1+t\) and \(E_1\ge1-t\) give \(px\le2t\) and therefore \(qy\ge1-3t\).

When \(q\le p/2\), combine this with \(y\le1/(2p)\) to obtain \(t\ge(2p-q)/(6p)\). When \(p/2\le q\le p\), instead combine \(qy\ge1-3t\) with \(E_3\le1+t\), i.e. \(y\le(1+t)/(2p+q)\), to obtain \(t\ge p/(3p+2q)\).

When \(p\le q\le4p\), the inequalities \(E_2\ge1-t\) and \(E_3\le1+t\) imply \(2py\ge1-t\) and \((2p+q)y\le1+t\); eliminating \(y\) gives \(t\ge q/(4p+q)\).

When \(q\ge4p\), nonnegative holding on \(A\) gives \(y\le1/q\). Together with \(E_2\ge1-t\), this implies \(t\ge1-2p/q\). Thus the stated values are lower bounds for **every** feasible chain, by symmetry averaging.

**Exact attainment and every invariant optimizer.** In the first regime, set \(y=1/(2p)\) and \(x=(2p-q)/(3p^2)\). Then \(E_0=1+t\), \(E_1=1-t\); the other two modes and both holdings satisfy the required bounds exactly when \(q\le p/2\). Equality in the lower-bound chain forces these two weights uniquely.

In the second regime, set \(x=y=2/(3p+2q)\). The modes \(E_0,E_3\) equal \(1+t\), the mode \(E_1\) equals \(1-t\), and the remaining mode and holdings obey the constraints for \(p/2\le q\le p\). Equality in all lower-bound inequalities forces both weights.

In the third and fourth displayed regimes together, \(p\le q\le4p\), equality in the bound involving \(E_2,E_3\) forces \(y=2/(4p+q)\). Substituting into the conditions \(|1-E_0|,|1-E_1|\le q/(4p+q)\), \(x\ge0\), and \(px+qy\le1\), gives precisely
\[
\begin{split}
\frac{2(2p-q)}{p(4p+q)}\le x\le\frac2{4p+q},&\quad p\le q\le2p,\\
0\le x\le\frac{4p-q}{p(4p+q)},&\quad2p\le q\le4p.
\end{split}
\]
All endpoints and intermediate points satisfy every mode constraint and both holding constraints. Hence these intervals are **necessary and sufficient** for invariant optimality.

Finally, if \(q\ge4p\), the lower bound forces \(y=1/q\). Feasibility \(px+qy\le1\) then forces \(x=0\); the four Laplacian modes become \(1,1,2p/q,1+2p/q\). Their deviations are at most \(1-2p/q\) precisely when \(q\ge4p\). This also proves uniqueness in that regime. For any unrestricted globally optimal matrix, symmetrization attains an invariant optimum. The orbit average of nonnegative \(A\)-to-\(B\) edge weights vanishes only if **each** such weight was originally zero. Thus the forced-zero assertion when \(q\ge4p\) applies to all unrestricted optimizers. Conversely, an averaged optimal \(x>0\) when \(q<2p\) implies the original matrix has at least one positive \(A\)-to-\(B\) edge. In the intermediate region, the two displayed invariant endpoint chains witness existence of optimizers with and without these edges. All boundary matches follow by substitution. \(\square\)

## Verification

Run `python verify.py` with the versions specified in `requirements.txt`. The included checker performs rational evaluations of all four spectral expressions at both optimizer-interval endpoints and midpoints, independently solves the unreduced two-parameter minimax linear program with SciPy on a parameter sample, and diagonalizes assembled full stochastic matrices in NumPy. Its recorded output is `verification_output.txt`.

The recorded successful check was `VERIFY_OK exact_endpoint_and_midpoint_cases=2478 independent_lp_instances=257 full_dense_eigensystems=52 phase_boundary_cases=40`. Finite computations check the formulas and implementation but are not substitutes for the infinite-parameter proof above.

## Relationship to prior work

Boyd, Diaconis, and Xiao (2004) introduce the fastest symmetric Markov mixing objective and solve the complete bipartite case. Boyd, Diaconis, Parrilo, and Xiao (2009), Section 5.4.2, provide a general spectral block decomposition and semidefinite formulation for arbitrary complete multipartite graphs, but do not state the four-threshold closed form or classify optimizer intervals for \(K_{p,p,q}\). The spectral decomposition, the convex symmetrization principle, and the balanced edge-transitive case are **not** claimed as new.

Jafarizadeh (2010) gives analytical solutions for path-like and cycle-like multipartite networks in which all displayed vertex parts have equal size. A three-part cycle with all equal part sizes is the balanced special case, but not the imbalanced family with independent classes of sizes \(p,p,q\) and \(p\ne q\). The new content is the joint treatment of arbitrary imbalance, exact transition points at ratios \(1/2,1,2,4\), and the complete interval of optimal probabilities on the edge orbit between the equal parts.

## Limitations

The theorem addresses symmetric stochastic matrices with a uniform stationary law, not arbitrary reversible laws, directed walks, mixing time under another metric, or symmetry-breaking optimizer uniqueness. Formula results are exact; evidence of originality is limited to the cited and searched accessible literature, and an overlooked equivalent statement remains possible. No independent external audit is represented as having occurred.

## References

1. S. Boyd, P. Diaconis, and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI:10.1137/S0036144503423264. Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf, especially Section 7.1.
2. S. Boyd, P. Diaconis, P. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (publicly submitted 2007-09-06), SIAM J. Optimization 20 (2009), 792–819, DOI:10.1137/070689413. Full text: https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf, especially Section 5.4.2.
3. S. Jafarizadeh, *Fastest Mixing Markov Chain on Symmetric K-Partite Network*, arXiv:1008.2588v1 (2010), https://arxiv.org/pdf/1008.2588, especially Section III.
