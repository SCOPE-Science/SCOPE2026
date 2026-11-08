# Sharp central-edge capacity transition for fastest diffusion on even paths

## Finding

Let \(m\ge 2\) be an integer. On the path \(P_{2m}\), independently assign nonnegative conductances \(w_1,\ldots,w_{2m-1}\) to consecutive edges, subject to a total budget \(\sum_i w_i\le B\), where \(B>0\), and an upper capacity \(w_m\le u\) on its unique middle edge, where \(u>0\). Let \(L(w)\) be the combinatorial weighted Laplacian, and maximize its second-smallest eigenvalue \(\lambda_2(L(w))\). Define

\[
u_0=\frac{3Bm}{4m^2-1}.
\]

**Theorem (sharp bridge-capacity phase transition).** There is exactly one global optimizer over *all* independently assigned conductances, without an imposed reflection-symmetry assumption.

If \(u\ge u_0\), the capacity does not lower the unconstrained optimum and the optimum is

\[
\lambda_* = \frac{6B}{m(4m^2-1)},\qquad
w_i^*=\frac{\lambda_*}{2}i(2m-i),\quad 1\le i<2m.
\]

If \(0<u<u_0\), there is a unique real \(r>1/2\) satisfying

\[
\frac{B}{u}=1+\frac{2(m-1)r\bigl(r+(2m-1)/3\bigr)}{r+(m-1)/2}.
\tag{1}
\]

The unique optimum is then

\[
\lambda_* = \frac{2ur}{m\bigl(r+(m-1)/2\bigr)},\qquad w_m^*=u,
\]
\[
w_i^*=w_{2m-i}^*
=\lambda_*i\left(r+m-\frac{i+1}{2}\right),
\qquad 1\le i<m.
\tag{2}
\]

All optimal edge conductances are strictly positive. The cap has a positive shadow price precisely for \(u<u_0\); at \(u=u_0\) it is saturated but nonbinding, and for \(u>u_0\) it is slack. The optimizer remains symmetric even though competitors may be asymmetric. With \(m\) and \(B\) fixed, the small-cap behavior is

\[
\lambda_* = \frac{2u}{m}\left(1-\frac{(m-1)^2u}{B}+O(u^2)\right)
\qquad (u\downarrow0).
\]

For example, at \(m=3\), \(B=19\), and \(u=3\), the exact unique optimum is \((w_1,\ldots,w_5)=(3,5,3,5,3)\), with \(\lambda_*=1\). Without that cap the unique optimum has middle conductance \(171/35>3\).

## Assumptions and scope

The graph has \(2m\) ordered vertices \(1,\ldots,2m\). Edge \(i\) joins \(i\) and \(i+1\). All edge prices are one, vertex masses are one, and the Laplacian is unnormalized: \(L_{ii}=w_{i-1}+w_i\), \(L_{i,i+1}=L_{i+1,i}=-w_i\), with \(w_0=w_{2m}=0\). We optimize the continuous-time consensus/diffusion exponential rate \(\lambda_2\), not the discrete-time stochastic-matrix second eigenvalue modulus. The budget is an upper bound (not an exact-expenditure assumption). The results include \(u=u_0\); the nonbinding regime allows \(u\) larger than \(B\). The cap is strictly positive, and the theorem does not claim the same formula for odd paths, multiple caps, or nonunit costs.

## Proof

**1. A centered test vector.** Put \(a=m-1\). For any \(r\ge1/2\), set

\[
x_i=-\bigl(r+m-i\bigr)\quad(1\le i\le m),\qquad
x_{2m+1-i}=-x_i.
\]

Then \(\sum_i x_i=0\). Every nonmiddle edge has difference \(x_{i+1}-x_i=1\); the middle edge has difference \(2r\). Its squared norm is

\[
V_m(r)=2\sum_{k=0}^{m-1}(r+k)^2.
\]

For every admissible \(w\), the Rayleigh principle gives

\[
\lambda_2(L(w))\le\frac{x^\mathsf{T}L(w)x}{V_m(r)}
=\frac{\sum_i w_i+(4r^2-1)w_m}{V_m(r)}.
\tag{3}
\]

If \(r>1/2\), this is bounded above by \([B+(4r^2-1)u]/V_m(r)\). If \(r=1/2\), it is bounded above by \(B/V_m(1/2)\) regardless of the central cap.

**2. Constructing eigenvectors and weights.** A weighted-path eigenvector satisfying \(L(w)x=\lambda x\) and \(\sum x_i=0\) obeys a telescoping flux identity:

\[
w_i(x_{i+1}-x_i)=-\lambda\sum_{j=1}^{i}x_j
\quad (1\le i<2m).
\tag{4}
\]

For the vector above, (4) uniquely forces, for \(1\le i<m\),

\[
w_i=w_{2m-i}=\lambda i\left(r+m-\frac{i+1}{2}\right),\qquad
w_m=\lambda\frac{m\bigl(r+a/2\bigr)}{2r}.
\tag{5}
\]

These are all positive. Their total is

\[
\sum_{i=1}^{2m-1}w_i
=w_m+\lambda m(m-1)\left(r+\frac{2m-1}{3}\right).
\tag{6}
\]

For \(r=1/2\), (5) becomes \(w_i=\lambda i(2m-i)/2\), and (6) gives \(\lambda=6B/[m(4m^2-1)]\). Its middle conductance is exactly \(u_0=3Bm/(4m^2-1)\). Hence when \(u\ge u_0\), this allocation is feasible, exhausts the budget, and makes \(x\) an eigenvector with eigenvalue \(\lambda_*\).

For \(0<u<u_0\), impose \(w_m=u\) in (5) to get the stated \(\lambda_*\). Equation (6) then becomes (1). The right side of (1), viewed as a function of \(r>0\), is strictly increasing: the derivative of \(r(r+d)/(r+a/2)\), where \(d=(2m-1)/3\), has positive numerator \(r^2+ar+ad/2\). At \(r=1/2\), it equals \(B/u_0\), and it tends to infinity with \(r\). Consequently (1) has one and only one solution \(r>1/2\) for \(u<u_0\), and (2) exhausts the budget and satisfies \(L(w)x=\lambda_*x\).

**3. Identifying the Fiedler eigenvalue.** The constructed vector is strictly increasing and has exactly one sign change: all its first \(m\) components are negative and its last \(m\) are positive. The off-diagonal entries of the resulting path Laplacian are strictly negative, so the symmetric Jacobi/Sturm oscillation theorem applies. For such an irreducible tridiagonal matrix, a nonzero-component eigenvector with exactly one sign change belongs to its second-smallest eigenvalue. Thus the constructed eigenvalue is exactly \(\lambda_2\), rather than merely some positive eigenvalue. Equivalently, the leading-principal-minor Sturm recurrence has exactly one sign variation before its final zero at \(\lambda_*\); see the exact verifier.

Multiplying \(L(w)x=\lambda_*x\) by \(x^\mathsf T\) makes the candidate attain the corresponding upper bound (3), for either \(r=1/2\) or \(r>1/2\). Global optimality is therefore proved for every admissible *asymmetric or symmetric* competitor.

**4. Uniqueness, including asymmetric competitors.** Suppose any admissible \(\widetilde w\) attains this same optimum. Equality in (3) is necessary. In the nonbinding phase, equality requires \(\sum_i\widetilde w_i=B\); in the binding phase it also requires \(\widetilde w_m=u\), because \(4r^2-1>0\). More importantly, equality in the Rayleigh principle makes the *same fixed* vector \(x\) an eigenvector of \(L(\widetilde w)\) with eigenvalue \(\lambda_*\). The telescoping identity (4) forces every individual \(\widetilde w_i\) uniquely, yielding (5). This proves uniqueness without symmetry reduction.

**5. Boundary and small-cap behavior.** The central weight of the unconstrained optimum is \(u_0\), so (1) has the boundary value \(r=1/2\) precisely at \(u=u_0\). At smaller \(u\), it forces \(r>1/2\) and a saturated cap. As \(u\downarrow0\), (1) yields \(r=B/[2(m-1)u]+O(1)\). Expanding \(\lambda_*=2u r/[m(r+(m-1)/2)]\) gives the claimed asymptotic law.

## Verification

The standalone `verify.py` uses only Python standard-library exact rational arithmetic and prints `VERIFY_OK 9911`. It checks rational capacity-boundary and saturated-cap designs for \(m=2,\ldots,16,20,25\), with multiple rational values of \(r\) and \(u\). Each case verifies the full budget, positive weights, middle capacity, all entries of the eigenvector identity, the Rayleigh identity, and the prefix-flux reconstruction. It additionally builds the characteristic-polynomial Sturm sequence using exact integers/rationals and checks that the proposed eigenvalue has exactly one eigenvalue below it. These finite checks do not replace the infinite-family proof in this document.

Run `python3 verify.py` with Python 3. No third-party package, network access, data download, or external artifact is needed. The concrete six-vertex example is checked exactly.

## Relationship to prior work

Fiedler's *Absolute algebraic connectivity of trees* (1990) and Wan et al.'s 2008 tree-edge allocation theory treat maximizing the spectral gap subject to a **total edge-weight budget**. They motivate the unconstrained \(u\ge u_0\) portion, and their equal-increment eigenvector structure is recovered in that phase. Neither established result in the inspected material gives the joint feasible region with an independently **capped central edge**, its sharp threshold \(u_0\), the saturated-cap allocation (1)–(2), and global uniqueness against asymmetric allocations.

Shakeri et al. (arXiv:1510.06785, first publicly posted 2015-10-22) identify threshold regimes in a different budgeted algebraic-connectivity design: weighted interlinks between fixed network layers. Its model does not contain this jointly redesignable path with a single upper-capacity bridge, and its threshold does not imply (1). Shafi, Arcak and El Ghaoui (2010) present general semidefinite formulations for Laplacian eigenvalue constraints; these give an optimization framework, not the closed path-cap phase diagram. Kirkland and Neumann (2004) analyze varying a single edge weight while others are fixed; that does not directly settle the simultaneous global allocation under a total budget. See the access limitation below.

A related exact cycle-edge *price* optimization (an available prior mathematical record) optimizes a weighted cost function and may delete an expensive closing edge; it does not impose a physical upper bound on the central edge of an even path. A priced double-star spectral-gap formula has a different tree and no hard central capacity. These are different feasible sets and do not imply the present cap threshold or optimizer.

## Limitations

This result is for equal vertex masses and unit edge expenditure prices on even paths with exactly one centrally located hard cap. General trees, off-center bottlenecks, several capacities, and random-walk mixing objectives are not classified. The general convex SDP formulation is already known; the claimed new content is its exact full-parameter solution and uniqueness in this constrained family. The full text of Kirkland and Neumann (2004) could not be obtained through accessible lawful sources, so an uncatalogued equivalent treatment remains a publication-priority risk. No independent mathematical audit has been performed.

## References

1. M. Fiedler, "Absolute algebraic connectivity of trees," *Linear and Multilinear Algebra* **26** (1990), 85–106. https://doi.org/10.1080/03081089008817967
2. Y. Wan, S. Roy, X. Wang, A. Saberi, T. Yang, M. Xue and B. Malek, "On the Structure of Graph Edge Designs that Optimize the Algebraic Connectivity," *47th IEEE Conference on Decision and Control* (2008), 805–810. https://doi.org/10.1109/CDC.2008.4738734 . Lawful full text: https://skoge.folk.ntnu.no/prost/proceedings/cdc-2008/data/papers/0353.pdf
3. H. Shakeri, N. Albin, F. D. Sahneh, P. Poggi-Corradini and C. Scoglio, "Maximizing Algebraic Connectivity in Interconnected Networks," arXiv:1510.06785 (first version 2015-10-22). https://arxiv.org/abs/1510.06785
4. S. Y. Shafi, M. Arcak and L. El Ghaoui, "Designing Node and Edge Weights of a Graph to Meet Laplacian Eigenvalue Constraints," *Allerton Conference* (2010). https://people.eecs.berkeley.edu/~elghaoui/Pubs/SAE_Allerton_2010.pdf
5. S. J. Kirkland and M. Neumann, "On algebraic connectivity as a function of an edge weight," *Linear and Multilinear Algebra* **52** (2004), 17–33. https://doi.org/10.1080/0308108031000119663
6. T. Kolokolnikov, "Maximizing algebraic connectivity for certain families of graphs," arXiv:1412.6147 (2014-12-17). https://arxiv.org/abs/1412.6147
