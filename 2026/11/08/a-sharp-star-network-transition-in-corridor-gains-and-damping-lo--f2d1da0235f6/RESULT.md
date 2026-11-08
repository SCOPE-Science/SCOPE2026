# A sharp star-network transition in corridor gains and damping loss

## Finding

In an explicitly specified, homogeneous, linear metapopulation recruitment model, adding a single positive two-way corridor strictly increases the Perron growth factor but can **decrease** the population-projection damping ratio. There is a sharp hub-degree transition: for every star with at least four leaves, the addition of any one leaf-to-leaf corridor decreases the damping ratio for *every* self-recruitment ratio above the stated nonoscillatory threshold. For a three-leaf star, the effect reverses exactly once as self-recruitment grows; for a two-leaf star it always improves the damping ratio.

More precisely, let \(m\ge 2\), let \(G_m=K_{1,m}\) have center \(0\) and leaves \(1,\ldots,m\), and let \(G_m^+\) be obtained by adding the undirected edge \(\{1,2\}\). Let \(A_m,A_m^+\) denote their unweighted symmetric adjacency matrices. Fix \(c\ge\sqrt m\) and a common \(s\) satisfying \(0<s\le 1/(c+m)\), and form the matrices
\[
C_m=s(cI+A_m),\qquad C_m^+=s(cI+A_m^+).
\]
Both are nonnegative, primitive, and column-substochastic; thus they may be interpreted as a simplified matrix of expected successful settlement fractions with constant local retention and equal symmetric corridor effects, while unused settlement probability represents mortality or loss. Multiplying both by an arbitrary positive fecundity factor does not affect their damping ratios.

For a primitive matrix \(C\), write \(\rho(C)\) for its Perron eigenvalue and \(\mathcal D(C)=\rho(C)/\max_{\lambda\in\sigma(C),\,\lambda\ne\rho(C)}|\lambda|\) for its damping ratio, eigenvalues counted with multiplicity. Then \(\rho(C_m^+)>\rho(C_m)\) always. The complete damping-ratio comparison within this star family is:

1. \(m=2\): \(\mathcal D(C_m^+)>\mathcal D(C_m)\) for all \(c\ge\sqrt2\).
2. \(m=3\): there is a unique \(c_*=4.245360630265\ldots>\sqrt3\) such that the new ratio is smaller for \(\sqrt3\le c<c_*\), equal at \(c=c_*\), and larger for \(c>c_*\).
3. \(m\ge4\): \(\mathcal D(C_m^+)<\mathcal D(C_m)\) strictly for every \(c\ge\sqrt m\).

The exceptional value \(c_*\) is characterized exactly below by the real roots of \(x^3-x^2-3x+1\). Hence *five habitats are the minimum within this star family for a permanent damping-ratio loss throughout the entire specified self-recruitment regime*. The quantifier is about stars, not all connected graphs.

## Assumptions and scope

This is a deterministic linear, density-independent recruitment/settlement model: one-step expected abundance evolves by multiplying by the nonnegative primitive matrix \(C\), optionally with a common positive fecundity multiplier. All pre-existing corridor weights and local retention strengths remain fixed when the additional corridor is created, so the intervention increases total available recruitment for its two endpoints rather than reallocating a fixed global budget. The bound on \(s\) ensures all column sums are at most one. A damping-ratio reduction means the slowest asymptotic non-Perron mode decays *relative to the Perron mode* more slowly; it does not assert a particular finite-time norm bound or nonlinear ecological outcome.

## Proof

Put \(r=\sqrt m\). The eigenvalues of \(A_m\) are \(r,-r\), and \(0\) with multiplicity \(m-1\). Thus for \(c\ge r\), the largest sub-Perron eigenvalue modulus of \(cI+A_m\) is \(c\), and
\[
\mathcal D(C_m)=\frac{c+r}{c}.
\]
The scalar \(s\) cancels.

For \(m\ge3\), split leaf coordinates into the pair \(\{1,2\}\) and its remaining \(m-2\) leaves. On vectors constant in each of the three groups \(\{0\},\{1,2\},\{3,\ldots,m\}\), the adjacency action of \(A_m^+\) has the quotient matrix
\[
Q_m=\begin{pmatrix}0&2&m-2\\1&1&0\\1&0&0\end{pmatrix},\qquad
f_m(x)=\det(xI-Q_m)=x^3-x^2-mx+m-2.
\]
The orthogonal complementary modes give the eigenvalue \(-1\) once, from leaf antisymmetry on the new edge, and \(0\) with multiplicity \(m-3\), from zero-sum differences among untouched leaves. All eigenvalues are real, because the complete adjacency matrix is symmetric.

The signs \(f_m(-r)=-2<0\), \(f_m(-1)=2m-4>0\), \(f_m(0)=m-2>0\), \(f_m(1)=-2<0\), and \(f_m(r)=-2<0\), together with positive leading coefficient, show that the three simple cubic roots satisfy
\[
-r<\gamma_m<-1<0<\beta_m<1<r<\alpha_m.
\]
In particular the eigenvalues of \(cI+A_m^+\) are nonnegative when \(c\ge r\); the largest non-Perron one is \(c+\beta_m\). Therefore
\[
\mathcal D(C_m^+)=\frac{c+\alpha_m}{c+\beta_m},
\qquad
\mathcal D(C_m^+)<\mathcal D(C_m)
\iff c(\alpha_m-\beta_m-r)<r\beta_m.
\tag{1}
\]
By strict Perron-Frobenius monotonicity, the added positive edge strictly increases the Perron eigenvalue for each connected graph and all \(s>0\).

For \(m\ge4\), let \(q=2/5\). Direct substitution gives
\[
f_m(q)=\frac{75m-262}{125}>0,
\qquad
f_m(r+q)=\frac{2(50m-20r-131)}{125}>0.
\]
The second numerator is already positive at \(r=2\), and increases strictly as \(r\) increases from \(2\). Since \(f_m\) is positive on \((0,\beta_m)\), negative on \((\beta_m,\alpha_m)\), and positive above \(\alpha_m\), these inequalities force
\[
0<\alpha_m-r<\frac25<\beta_m.
\]
Thus \(\alpha_m-\beta_m-r<0\), making (1) strict for all \(c\ge r\).

For \(m=3\), exact rational sign tests imply \(\alpha_3>217/100\) and \(\beta_3<39/125\); also \(\sqrt3<1733/1000\). Consequently \(\alpha_3-\beta_3-\sqrt3>1/8>0\), and (1) is equivalent to
\[
c<c_*:=\frac{\sqrt3\,\beta_3}{\alpha_3-\beta_3-\sqrt3}.
\]
Furthermore \(\alpha_3<109/50\), \(\sqrt3>17/10\), and \(\beta_3>3/10\), giving \(\alpha_3-\sqrt3-\beta_3<9/50<\beta_3\), so \(c_*>\sqrt3\). Thus there is precisely one crossing in the admissible range. Numerical root isolation only evaluates the displayed algebraic expression; it is not used to prove uniqueness.

For \(m=2\), the new graph is a triangle, with adjacency spectrum \(2,-1,-1\), and
\[
\mathcal D(C_2^+)=\frac{c+2}{c-1}>
\frac{c+\sqrt2}{c}=\mathcal D(C_2)
\]
for every \(c\ge\sqrt2\), since the cross-multiplied difference is \(c(3-\sqrt2)+\sqrt2>0\). This proves all cases.

## Verification

The standalone file `verify.py` requires only Python 3 standard-library modules. Run `python3 verify.py` after extracting it alongside this document. It checks the exact rational sign inequalities, independently diagonalizes the actual adjacency arrays by Jacobi rotations over a wide finite range, evaluates the cubic roots, checks the exceptional crossing, and checks the substochastic scaling constraints. During preparation it printed `PASS 752 finite/exact checks; m=3 crossing= 4.245360630265`.

For the five-patch witness \(m=4,c=2\), before adding the edge the Perron eigenvalue of the unscaled matrix is \(4\) and the damping ratio is \(2\). Afterwards its Perron eigenvalue is \(4.342923082777\ldots\), while its damping ratio is \(1.757782096989\ldots\). Both Perron factors scale by the same allowed \(s\); neither damping ratio changes. The proof above, not these samples, establishes the entire integer and real parameter domain.

## Relationship to prior work

Shima, Noonburg and Phillips (2010) explicitly use the damping ratio of a spatial connectivity matrix as a summary of metapopulation connectivity and study changing larval traits, stressors and advection. Their full text defines the ratio and its spatial-convergence interpretation but does not develop a uniform-self-recruitment star family under a single new leaf corridor. Stott and colleagues (2010) discuss primitive population-projection matrices, while Stott (2016) surveys perturbation of transient dynamics; neither supplies the all-star comparison. Eldan, Rácz and Schramm (2015) prove a Braess-type effect for the *normalized Laplacian spectral gap* in random graphs. Their spectral objective is not the Perron/subdominant modulus ratio of the unnormalized, self-retaining population matrix here; no general implication yields this exact three-case classification. These are related mechanisms, not evidence of absolute novelty.

## Limitations

The graphs are undirected stars with equal symmetric edge weights; only one edge between two leaves is added. Local retention is homogeneous and the admissible regime is \(c\ge\sqrt m\), not arbitrary smaller retention. The column-substochastic interpretation requires the common scaling \(s\). A larger connectivity matrix may have changed eigenvectors and transient amplitudes; damping ratios capture only asymptotic relative spectral decay. Nothing here establishes nonlinear ecological persistence, an empirical management policy, or novelty against every possible earlier graph-spectrum treatment. The published-source comparison is limited to the inspected literature, and historical-priority verification by an independent specialist remains open.

## References

- Shima, J. S., Noonburg, E. G. and Phillips, N. E. (2010), *Life history and matrix heterogeneity interact to shape metapopulation connectivity in spatially structured environments*, Ecology 91, 1215–1224. First online 2010-04-01. DOI: https://doi.org/10.1890/08-2058.1. Author-hosted full text: https://biology.fau.edu/directory/noonburg/pdf1.pdf
- Stott, I., Townley, S., Carslake, D. and Hodgson, D. J. (2010), *On reducibility and ergodicity of population projection matrix models*, Methods in Ecology and Evolution 1, 242–252. https://doi.org/10.1111/j.2041-210X.2010.00032.x
- Eldan, R., Rácz, M. and Schramm, T. (2015), *Braess's paradox for the spectral gap in random graphs and delocalization of eigenvectors*. https://arxiv.org/abs/1504.07669 (first submitted 2015-04-28).
- Stott, I. (2016), *Perturbation analysis of transient population dynamics using matrix projection models*, Methods in Ecology and Evolution 7, 666–678. https://doi.org/10.1111/2041-210X.12543
