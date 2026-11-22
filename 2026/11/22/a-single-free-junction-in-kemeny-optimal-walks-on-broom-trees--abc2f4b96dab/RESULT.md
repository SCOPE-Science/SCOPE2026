# A single free junction in Kemeny-optimal walks on broom trees

## Finding

Let \(B_{m,L}\) be the tree formed by joining \(m\ge2\) leaves to a root \(r\), and attaching to the same root a path \(r,v_1,\ldots,v_L\) with \(L\ge3\). Its vertex count is \(N=m+L+1\). Among all irreducible symmetric row-stochastic matrices supported on this tree and its diagonal, the zero-target Kemeny sum

\[
\mathcal K(P)=\sum_{j=2}^{N}\frac{1}{1-\lambda_j(P)}
\]

has the following **unique** global minimizer. This normalization excludes the additional unit sometimes included for recurrence at the starting state.

Set

\[
c_0=N-1,\qquad c_j=(L-j+1)(m+j)\quad(1\le j\le L),
\]
\[
E=\sum_{\substack{2\le j\le L\\j\ \mathrm{even}}}c_j,
\qquad O=\sum_{\substack{3\le j\le L\\j\ \mathrm{odd}}}c_j.
\]

Both \(E\) and \(O\) are positive. Define

\[
x=\frac{\sqrt{c_1}}{m\sqrt{c_0}+\sqrt{c_1}},\qquad
z=\frac{\sqrt E}{\sqrt E+\sqrt O},\qquad a=\frac{1-x}{m}.
\]

Each of the \(m\) leaf-root edges has transition weight \(a\). The first path edge \(r v_1\) has weight \(x_1=x\); for \(2\le j\le L\), edge \(v_{j-1}v_j\) has weight \(x_j=z\) if \(j\) is even and \(x_j=1-z\) if \(j\) is odd. Diagonal transition probabilities fill the remaining row sums. Precisely the root and the path vertices \(v_2,\ldots,v_{L-1}\) have zero holding; **\(v_1\) has strictly positive holding** \(1-x-z\), and all leaves have positive holding.

The minimum is

\[
\boxed{\mathcal K_*=
\frac{(m\sqrt{c_0}+\sqrt{c_1})^2+(\sqrt E+\sqrt O)^2}{N}.}
\]

For each fixed \(L\ge3\), \(x\sim\sqrt L/m\) as \(m\to\infty\), but the other path weights converge to constants strictly between zero and one.

## Assumptions and scope

Symmetric stochastic means \(P=P^\top\), \(P\mathbf1=\mathbf1\), all entries nonnegative, and off-diagonal entries vanish outside the specified edges. Each edge is allowed to have its own probability, without an imposed symmetry assumption. Irreducibility requires strictly positive probabilities on every edge because the support graph is a tree. Holding probabilities may vanish. All assertions hold for integers \(m\ge2,L\ge3\) exactly.

## Proof

**1. Tree reduction and global convexity.** Write \(w_e=P_{ij}=P_{ji}\) for each edge and \(L_w=I-P\). For any weighted tree, the resistance identity gives

\[
N\mathcal K(P)=\sum_{\{u,v\}}R_{uv}
=\sum_{e\in E(B_{m,L})}\frac{s_e(N-s_e)}{w_e},
\]

where \(s_e\) is the vertex count on either side of edge \(e\). For each root-leaf edge the coefficient is \(c_0=N-1\); the coefficient for path edge \(v_{j-1}v_j\) is \(c_j=(L-j+1)(m+j)\). Hence

\[
N\mathcal K=m\frac{c_0}{a}+\sum_{j=1}^{L}\frac{c_j}{x_j}.
\]

The feasible set is described by nonnegative edge probabilities and vertex-capacity inequalities. Each summand \(c_e/w_e\) is strictly convex for \(w_e>0\); the objective is strictly convex on the positive orthant. Permuting the root leaves preserves both objective and constraints, so strict convexity forces their optimal weights to agree. Therefore it suffices to solve the displayed \(L+1\)-variable problem, while global uniqueness applies to all independently adjustable edges.

**2. Candidate and its strictly free junction.** Write the root constraint as \(ma+x_1\le1\), the path constraints as \(x_j+x_{j+1}\le1\) for \(1\le j<L\), and the endpoint constraints as \(a\le1\), \(x_L\le1\). The stated candidate saturates the root constraint, saturates every path constraint from \(j=2\) onward, but strictly satisfies \(x_1+x_2<1\).

Indeed \(x_1+x_2<1\) is equivalent, after taking positive square roots, to

\[
F:=m^2c_0 O-c_1 E>0.
\]

For either parity, express \(L=2h\) (\(h\ge2\)) or \(L=2h+1\) (\(h\ge1\)). The finite sums are

\[
\begin{array}{ll}
L=2h:&E=\frac{h(2h^2+3hm+3h+1)}3,\quad
O=\frac{h(h-1)(2h+3m+5)}3,\\
L=2h+1:&E=\frac{h(h+1)(2h+3m+4)}3,\quad
O=\frac{h(2h^2+3hm+6h+1)}3.
\end{array}
\]

Substitution \(m=2+u\) and \(h=h_0+v\) (\(h_0=2\) in the even case and \(h_0=1\) in the odd case) expands \(F\) into a polynomial in \(u,v\) with strictly positive constant and only nonnegative remaining coefficients. The accompanying algebraic verifier constructs these **exact rational polynomials** and checks every coefficient; this is an identity in arbitrary nonnegative \(u,v\), not finite extrapolation. Thus \(F>0\) for every claimed parameter pair.

**3. Nonnegative optimality multipliers.** Set \(g_j=c_j/x_j^2\). Give the root capacity multiplier \(\lambda_0=c_0/a^2>0\) and the first path junction multiplier \(\lambda_1=0\). The root and first-path stationarity equations hold by \(c_1/x_1^2=c_0/a^2\). For subsequent junctions define recursively

\[
\lambda_j=g_j-\lambda_{j-1}\quad(2\le j\le L).
\]

Let \(S_E(k)=\sum_{i=1}^{k}c_{2i}\) and \(S_O(k)=\sum_{i=1}^{k}c_{2i+1}\) (empty sums vanish). Since \(z/(1-z)=\sqrt{E/O}\), the recursion gives

\[
\lambda_{2k}=\frac{S_E(k)O-E S_O(k-1)}{O z^2},
\quad
\lambda_{2k+1}=\frac{E S_O(k)-S_E(k)O}{O z^2}.
\]

For both parities \(L=2h\) and \(L=2h+1\), replacing \(h\) by \(k+d\) in these numerator polynomials yields **nonnegative rational coefficients** as polynomials in \(m,k,d\). The explicit exact coefficient computations are reproducible in `VERIFY.py`, and the factored odd-junction expressions show strict positivity for every interior odd junction. The even-junction expressions likewise have strictly positive coefficients for every interior even junction. At the final endpoint the numerator cancels because the full even/odd sums are exactly \(E,O\), so \(\lambda_L=0\). Every interior multiplier \(\lambda_j\) with \(2\le j<L\) is strictly positive. The root and all saturated junctions therefore satisfy complementary slackness, while the free first junction and free endpoint have zero multipliers. The edge positivity constraints are inactive.

These conditions prove global optimality by convexity, and strict convexity proves uniqueness. Substituting \(a,x_1,z\) into the tree sum and applying the two-term Cauchy--Schwarz identity gives the stated optimum value.

**4. Large-hub limit.** With \(L\) fixed, \(c_0=m+L\) and \(c_1=L(m+1)\), whence \(x_1\sim\sqrt L/m\). Both \(E\) and \(O\) grow linearly in \(m\) with strictly positive coefficients because \(L\ge3\); thus \(z\) converges to a number in \((0,1)\). This proves the contrasting allocation scales.

## Verification

Run `python VERIFY.py` with Python 3, SymPy and NumPy. The symbolic stage verifies exact sum formulas, the strictly positive first-junction certificate and the nonnegative coefficients in every family of KKT multiplier expressions. It treats \(m,h,k,d\) as indeterminates, not sampled bounds. Finite diagnostics independently evaluate all vertex constraints and multipliers for 216 pairs \((m,L)\) with \(2\le m\le13\), \(3\le L\le20\), including direct eigenvalue trace checks for the smallest cases. Those finite diagnostics supplement, but do not replace, the parameter-uniform polynomial proof.

As a concrete smallest instance \((m,L)=(2,3)\), the cut coefficients are \(c_0=5,c_1=9,c_2=8,c_3=5\). Then \(x_1=3/(2\sqrt5+3)\), \(z=\sqrt8/(\sqrt8+\sqrt5)\), and the holding probability at \(v_1\) is strictly positive.

## Relationship to prior work

Catral, Kirkland, Neumann and Sze study Kemeny's spectral and perturbative formulas, providing the basic objective. Patel, Agharkar and Bullo (2015) formulate reversible Markov-chain Kemeny minimization with fixed support and stationary law as a convex/semidefinite optimization problem, but their primary text gives no all-size explicit optimal broom-tree weights or junction-activity classification. Durastante, Gnazzo and Meini (2026) develop general reversible optimization algorithms rather than this exact tree-family solution. Ciardo, Dahl and Kirkland study Kemeny constants on trees with prescribed size/diameter under the natural degree-normalized random walk, not optimized uniform-stationary transition weights. Boyd, Diaconis and Xiao optimize the second-largest eigenvalue modulus, which does not imply optimality for this inverse-spectral-sum objective.

## Limitations

This is a closed-form result for one natural tree family, not a general classification of optimal Kemeny walks on all trees. Symmetric stochasticity fixes the stationary law to be uniform; nonreversible chains and nonuniform stationary masses are not covered. The objective is the zero-target Kemeny sum, which differs by an additive unit from a commonly used return-time convention. Publication priority is not certified: inaccessible or unindexed equivalent formulations remain possible, especially in the general convex Kemeny-optimization literature. No independent mathematical audit has been performed.

## References

- M. Catral, S. Kirkland, M. Neumann and N.-S. Sze (2010), *The Kemeny Constant for Finite Homogeneous Ergodic Markov Chains*, https://mural.maynoothuniversity.ie/id/eprint/2185/.
- R. Patel, P. Agharkar and F. Bullo (2015), *Robotic Surveillance and Markov Chains with Minimal Weighted Kemeny Constant*, https://motion.me.ucsb.edu/pdf/2014b-pab.pdf.
- F. Durastante, M. Gnazzo and B. Meini (2026), *Kemeny's constant minimization for reversible Markov chains via structure-preserving perturbations*, https://link.springer.com/article/10.1007/s10543-026-01152-6.
- L. Ciardo, S. Dahl and S. Kirkland (2020), *On Kemeny's Constant for Trees with Fixed Order and Diameter*, https://arxiv.org/abs/2003.08286.
- S. Kirkland and Z. Zeng (2016), *Kemeny's Constant and an Analogue of Braess' Paradox for Trees*, https://doi.org/10.13001/1081-3810.3222 (full primary text not successfully accessed).
- S. Boyd, P. Diaconis and L. Xiao (2004), *Fastest Mixing Markov Chain on a Graph*, https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.
