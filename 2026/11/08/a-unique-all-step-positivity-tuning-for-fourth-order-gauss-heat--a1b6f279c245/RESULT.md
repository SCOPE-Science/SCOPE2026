# A unique all-step positivity tuning for fourth-order Gauss heat diffusion on a four-vertex path

## Finding

Let the four-vertex path have edge conductances \(a,b,c>0\), in vertex order \(1-2-3-4\). For the fourth-order two-stage Gauss--Legendre update
\[
T(h)=R(-hL),\qquad R(-x)=\frac{x^2-6x+12}{x^2+6x+12},\quad h\ge0,
\]
where \(L\) is the combinatorial weighted graph Laplacian, the following conditions are equivalent:

1. \(T(h)\) is entrywise nonnegative for every real \(h\ge0\).
2. \(a=c\) and \(b=2a\).

At the unique permitted conductance ratio \(a:b:c=1:2:1\), all sixteen entries are strictly positive at every \(h>0\). Outside that ray, at least one off-diagonal entry is negative for every sufficiently large \(h\). As an exact finite-step example, the unit-weight path has \(T(12)_{1,2}=-60/84973\).

## Assumptions and scope

The graph is precisely the simple four-vertex undirected path, with no extra edges and all three edge conductances strictly positive. The matrix \(L\) is the unnormalized, symmetric Laplacian. Step sizes are all real numbers \(h\ge0\); the claim concerns the **completed step**, not the two internal stages. Conductance scaling is absorbed into the step size. The graph is the smallest tree that is not a star, which makes it a natural minimal test for graph-specific positivity of a fourth-order implicit integrator.

## Proof

Put \(J=\mathbf1\mathbf1^\mathsf T/4\), \(G=L^\dagger=(L+J)^{-1}-J\), and denote the three edge resistances by \(x=1/a\), \(y=1/b\), \(z=1/c\). Exact elimination gives
\[
16G_{12}=-3x+4y+z,\qquad
16G_{23}=x-4y+z,\qquad
16G_{34}=x+4y-3z.
\]
These identities can also be obtained by centering the three edge-cut indicator vectors and summing their outer products weighted by the edge resistances.

Since \(R(-t)=1-12/t+O(t^{-2})\) as \(t\to+\infty\), spectral calculus on the positive nonzero eigenvalues of the connected graph yields
\[
T(h)=I-\frac{12}{h}G+O(h^{-2}),\qquad h\to+\infty.
\]
Consequently, all-step entrywise nonnegativity requires \(G_{12},G_{23},G_{34}\le0\). The three exact inequalities are
\[
4y\le3x-z,\quad x+z\le4y,\quad4y\le3z-x.
\]
The first two imply \(z\le x\), while the latter two imply \(x\le z\). Hence \(x=z\), and all inequalities force \(4y=2x\). Equivalently \(a=c\), \(b=2a\). If this condition fails, one of the three displayed Green entries is strictly positive; the corresponding entry of \(T(h)\) is strictly negative for all sufficiently large \(h\).

For sufficiency use a global conductance scaling to set \(a=c=1\), \(b=2\), and write \(t=ah>0\) for the original conductance scale. Define
\[
D(t)=(t^2+3t+3)(t^4+9t^3+30t^2+27t+9)>0.
\]
The four reflection-inequivalent off-diagonal entries are exactly
\[
\begin{aligned}
T_{12}(t)&=\frac{9t(t^3+5t^2+6t+3)}{D(t)},\\
T_{13}(t)&=\frac{3t^2(t^3+6t^2+15t+9)}{D(t)},\\
T_{14}(t)&=\frac{3t^3(2t^2+6t+3)}{D(t)},\\
T_{23}(t)&=\frac{9t(t^2+6t+6)}{D(t)}.
\end{aligned}
\]
Each is strictly positive for \(t>0\). Symmetry and path reflection cover the other off-diagonal entries. The scalar function \(R(-t)\) is strictly positive for every \(t\ge0\), because \(t^2-6t+12=(t-3)^2+3>0\) and its denominator is positive. Thus \(T(h)\) is positive definite, so its diagonal entries are strictly positive. At \(h=0\), \(T(0)=I\). This proves both directions and all boundaries.

For the explicit counterexample, direct rational elimination on \(P_4\) with \(a=b=c=1\) gives \(T(12)_{12}=-60/84973\).

## Verification

The included `verify_p4.py` uses exact symbolic identities and rational arithmetic, confirms the three entries of \(G\), the four rational expressions at the tuned weights, the normalization and entrywise signs at a selection of positive rational steps, the finite unit-weight counterexample, and 64 positive-integer price triples for the necessary Green-sign condition. Run `python verify_p4.py` with Python 3 and SymPy. The replay returned `VERIFY_OK 196`. These finite checks supplement the algebraic proof, not an exhaustive continuum argument.

## Relationship to prior work

Kirkland, Neumann and Shader (1997, Theorem 3.10 and preceding group-inverse formulas) characterize when the group inverse of an unweighted tree Laplacian is an M-matrix and develop weighted-tree pseudoinverse formulas. Their paper supplies earlier foundational Green-function sign geometry, including a weighted four-vertex example with a nonpositive-off-diagonal group inverse. The required large-step sign condition is therefore closely related to earlier known matrix theory; it is **not** presented here as new. What is established here additionally is the all-real-step positivity of the **fourth-order Gauss completed heat update** and the exact unique positive conductance ray that makes it possible, with explicit finite-step rational certificates.

Horváth (2005) analyzes Runge--Kutta positivity step-size thresholds; Lóczi and Ketcheson (2013) analyze absolute monotonicity of rational stability functions. Those are method-wide results and do not directly state the weighted four-vertex path all-step characterization. A published result on the \([2/2]\) Padé map for pure-birth chains concerns nonreversible generators and a different positivity phenomenon. The result is restricted to the stated graph and method; neither general RK positivity nor the broader weighted-tree inverse classification is claimed to be new.

## Limitations

The theorem does not classify weighted trees on five or more vertices, nor guarantee positivity of the internal Gauss stages. The tuning is exact rather than robust: every nonproportional positive perturbation of \(1:2:1\) eventually loses positivity, although the required timestep may be large. Priority beyond the accessible, inspected literature remains subject to independent specialist review; no independent audit has been performed.

## References

- L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651 (first public 2013-03-26). https://arxiv.org/abs/1303.6651
- S. J. Kirkland, M. Neumann and B. L. Shader, *Distances in Weighted Trees and Group Inverse of Laplacian Matrices*, SIAM J. Matrix Anal. Appl. **18** (1997), 827–841, especially Theorem 3.10. https://doi.org/10.1137/S0895479896298713
- Z. Horváth, *On the positivity step size threshold of Runge-Kutta methods*, Appl. Numer. Math. **53** (2005), 341–356. https://doi.org/10.1016/j.apnum.2004.08.026
