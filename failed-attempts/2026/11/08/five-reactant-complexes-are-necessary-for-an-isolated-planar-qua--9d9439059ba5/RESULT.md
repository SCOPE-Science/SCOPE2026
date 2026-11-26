# Five reactant complexes are necessary for an isolated planar quadratic zero-Jacobian equilibrium

## Finding

**Theorem (sharp reaction-complex minimum).** Let a directed mass-action reaction network have two species, strictly positive rate constants and reactant complexes of total molecularity at most two. Product complexes may have arbitrary finite molecularity. If the induced polynomial vector field has an **isolated equilibrium** in the strictly positive quadrant at which its full \(2\times2\) Jacobian is the zero matrix, then at least **five distinct reactant complexes carrying nonzero net vector-field coefficients**, hence at least **five directed reactions**, are necessary. Both bounds are attained by a network with exactly five reactions.

The same support lower bound holds for *every* planar polynomial vector field of total degree at most two with such an isolated zero-Jacobian equilibrium, even without chemical-kinetic sign conditions. It is a lower bound for the entire class, not a classification of all possible local phase portraits or a lower bound for a particular generic bifurcation unfolding.

## Assumptions and scope

Write \(F:\mathbb R^2\to\mathbb R^2\) for the autonomous right-hand side. A directed reaction \(\alpha X+\beta Y\to\gamma X+\delta Y\) with positive rate \(k\), nonnegative integer stoichiometric coefficients, and \(\alpha+\beta\le2\) contributes \(k(\gamma-\alpha,\delta-\beta)x^\alpha y^\beta\) to \(F\). Counting a reverse reaction, when present, requires a separate directed reaction. Several reactions with identical reactants may aggregate into a single vector coefficient; cancellation can only decrease the number of nonzero reactant monomials.

An equilibrium \(p=(a,b)\), \(a,b>0\), is *isolated* if some open neighborhood contains no other zero of \(F\). The assumption is \(F(p)=0\) and \(DF(p)=0_{2\times2}\). A zero eigenvalue *alone* is insufficient: both rows of the Jacobian must vanish. No stability or rate-parameter genericity is imposed.

## Proof

**1. Normal form and six coefficient slots.** The invertible positive scaling \(X=x/a\), \(Y=y/b\) sends \(p\) to \((1,1)\) without changing the set of exponent pairs of nonzero monomials or whether the full Jacobian vanishes. Reexpress the scaled vector field as \(G(X,Y)\). Because it has total degree at most two and both its constant and linear Taylor terms at \((1,1)\) vanish, there are vectors \(A,B,C\in\mathbb R^2\) such that

\[
G(1+u,1+v)=Au^2+Buv+Cv^2.
\]

Expanding into the original monomial basis gives

\[
\begin{split}
G(X,Y)={}&AX^2+BXY+CY^2\\
&+(-2A-B)X+(-B-2C)Y+(A+B+C).
\end{split}
\]

Thus the six vector-valued coefficients, in the order \(X^2,XY,Y^2,X,Y,1\), are \(A,B,C,-2A-B,-B-2C,A+B+C\).

**2. Sparsity forces a common vector direction.** The six scalar coefficient rows multiplying \((A,B,C)\) are

\[
(1,0,0),\quad(0,1,0),\quad(0,0,1),\quad(-2,-1,0),\quad(0,-1,-2),\quad(1,1,1).
\]

No two rows are proportional. If at most four monomial coefficients are nonzero, at least two of these vector coefficients vanish. The corresponding two independent linear equations on the three-vector \((A,B,C)\) leave at most a one-dimensional scalar kernel. Since the equations hold in each output coordinate, there exist a fixed vector \(w\in\mathbb R^2\) and real numbers \(\alpha,\beta,\gamma\) such that

\[
G(1+u,1+v)=w\,q(u,v),\qquad
q(u,v)=\alpha u^2+\beta uv+\gamma v^2.
\]

If \(w=0\) or \(q=0\), the field is identically zero and the equilibrium is not isolated. Otherwise, its zero set is exactly \(q=0\). Because \(q\) is a homogeneous quadratic form on \(\mathbb R^2\), the equilibrium is isolated only when \(q\) is definite; a nonzero real zero would produce an entire line of equilibria through \((1,1)\). Replacing \(q\) and \(w\) simultaneously by their negatives if necessary, take \(q\) positive definite, so \(\alpha>0\), \(\gamma>0\), and \(\beta^2<4\alpha\gamma\).

**3. A definite shifted quadratic needs five monomials.** Expanding \(q(X-1,Y-1)\), the coefficients of \(X^2\), \(Y^2\), and the constant monomial are respectively \(\alpha\), \(\gamma\), and \(q(-1,-1)=\alpha+\beta+\gamma>0\). These three slots are nonzero. If \(\beta=0\), then the linear coefficients \(-2\alpha\) and \(-2\gamma\) are also nonzero, giving at least five. If \(\beta\ne0\), the mixed term \(XY\) is nonzero, while at least one of the two linear coefficients \(-2\alpha-\beta\) and \(-2\gamma-\beta\) must be nonzero: simultaneous vanishing would give \(\alpha=\gamma\), \(\beta=-2\alpha\), and \(q(u,v)=\alpha(u-v)^2\), which is not definite. Again there are at least five nonzero coefficient slots, contradicting the assumption of four or fewer. Therefore \(G\) and hence \(F\) have at least five nonzero reactant monomials. Since a directed mass-action reaction contributes to exactly one reactant monomial, there are at least five distinct reactant complexes and at least five reactions.

**4. Sharpness by five positive-rate reactions.** Consider the network

\[
\varnothing\xrightarrow{1}X+Y,\quad
X\xrightarrow{2}\varnothing,\quad
Y\xrightarrow{2}\varnothing,\quad
2X\xrightarrow{1}3X,\quad
2Y\xrightarrow{1}3Y.
\]

Its complete mass-action equations are

\[
\dot x=1-2x+x^2=(x-1)^2,\qquad
\dot y=1-2y+y^2=(y-1)^2.
\]

The only zero in \(\mathbb R^2\) is \((1,1)\), which is strictly positive, isolated, and satisfies \(DF(1,1)=0_{2\times2}\). All five rates are positive, the five reactant complexes \(\varnothing,X,Y,2X,2Y\) are distinct, and each reactant has molecularity at most two. Thus both lower bounds are sharp. \(\square\)

## Verification

The standalone `verify.py` checks exactly, using rational symbolic arithmetic, that each pair of the six coefficient rows is independent, that all induced two-vanishing-slot kernels are one-dimensional, and that the five reactions give precisely the displayed polynomial field, whose unique equilibrium and full zero Jacobian are immediate by factorization. Run `python verify.py` with SymPy installed. The finite symbolic calculation supplements, but does not replace, the universal argument above.

## Relationship to prior work

Yeung and Erban (2026), arXiv:2610.06130v1, classify the realizable geometric types of strongly nonhyperbolic positive equilibria for planar quadratic chemical networks. In Section 4 they explicitly raise optimization of the number of reactions, and exhibit a five-reaction realization. Their example establishes the *upper bound* of five for existence, but does not prove that four reactions are impossible. The new contribution is the *universal, sharp lower bound*, valid even before chemical coefficient constraints are imposed.

Banaji, Boros and Hofbauer (2024), DOI 10.1007/s11071-024-10068-1, characterize generic bifurcations in small quadratic networks and prove that four-reaction networks cannot unfold a generic cusp. Their Theorems 35–36 concern parameter unfoldings, and a cusp has a simple zero eigenvalue; neither theorem states the exclusion of an **isolated equilibrium with the entire Jacobian zero** at a fixed parameter vector. The present support argument addresses that different and stronger degeneracy directly. No claim is made about optimality for each of the nine individual phase-portrait classes, or about other types of bifurcation.

## Limitations

The bound uses exactly two chemical species, reactant molecularity at most two, a strictly positive isolated equilibrium, and the vanishing of the entire Jacobian. It is not a statement about equilibrium branches with a nonzero or merely nilpotent Jacobian, boundary equilibria, higher-order reactants, or higher-dimensional networks. Products of more than two molecules are permitted; indeed the sharp example uses products \(3X\) and \(3Y\). It is not an assertion that five reactions suffice for every possible local geometric class. Priority beyond the primary sources identified in the accompanying review remains subject to independent literature assessment.

## References

1. Norm Yeung and Radek Erban, *Classification of strongly non-hyperbolic critical points of planar second-order chemical reaction systems*, arXiv:2610.06130v1 (first posted October 5, 2026), https://arxiv.org/html/2610.06130v1, especially Section 4.
2. Murad Banaji, Balázs Boros, and Josef Hofbauer, *Bifurcations in planar, quadratic mass-action networks with few reactions and low molecularity*, *Nonlinear Dynamics* 112 (2024), 21425–21448, DOI:10.1007/s11071-024-10068-1, especially Theorems 35–36.
