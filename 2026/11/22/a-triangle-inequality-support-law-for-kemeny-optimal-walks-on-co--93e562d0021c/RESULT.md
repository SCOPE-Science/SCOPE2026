# A triangle-inequality support law for Kemeny-optimal walks on complete tripartite graphs

## Finding
Let \(a,b,c\) be any positive integers, put \(N=a+b+c\), and consider every irreducible symmetric nonnegative row-stochastic transition matrix \(P\) supported on the complete tripartite graph \(K_{a,b,c}\), with holding probabilities allowed. Here the zero-target Kemeny constant is \(\mathcal K(P)=\sum_{i=2}^{N}(1-\lambda_i(P))^{-1}\), counting eigenvalues with multiplicity. There is exactly **one** global minimizer, even among matrices whose edge probabilities are not constant on graph-automorphism orbits.

Relabel the three parts so that \(a\le b\le c\), and define the total transition mass between the parts by
\[
 X=\max\{0,(a+b-c)/2\},\qquad Y=b-X,\qquad Z=a-X.
\]
The unique optimal probability on an edge between the \(a\)- and \(b\)-parts is \(X/(ab)\), between the \(b\)- and \(c\)-parts it is \(Y/(bc)\), and between the \(c\)- and \(a\)-parts it is \(Z/(ca)\). All diagonal entries are the residual row sums.

The edges connecting the two smaller parts are **deleted if and only if** \(c\ge a+b\). If \(c<a+b\), all edges remain, and every vertex has zero holding probability. If \(c>a+b\), only the largest part has holding, equal to \(1-(a+b)/c\). At equality there is no holding, but the smaller-part edge class is still deleted. The optimal value is
\[
 \mathcal K_*=
 \begin{cases}
 N-3+\dfrac{12abc}{N[2(ab+bc+ca)-(a^2+b^2+c^2)]},&c<a+b,\\[5pt]
 a+b-1+\dfrac{c(c-1)}{a+b}+\dfrac{c}{N},&c\ge a+b.
 \end{cases}
\]
The two branches agree at \(c=a+b\). The conventional recurrence-inclusive definition of Kemeny's constant adds \(1\) and has identical optimizers.

## Assumptions and scope
All part sizes are positive integers; no edge conductances or probabilities are prescribed except for graph support, symmetry, stochasticity, and nonnegativity. An irreducible kernel can be periodic (no aperiodicity is required). Holding probabilities are permitted. The theorem concerns ordinary, not weighted, Kemeny constant, with uniform stationary distribution induced by symmetric stochasticity.

## Proof
**Strict convexity and orbit reduction.** Let \(J\) be the all-ones matrix of order \(N\) and \(M(P)=I-P+J/N\). For each symmetric stochastic irreducible \(P\), \(M(P)\) is positive definite and \(\mathcal K(P)=\operatorname{tr}(M(P)^{-1})-1\). On this domain trace-inverse is strictly convex: for nonzero symmetric perturbation \(H\), its second directional derivative is \(2\operatorname{tr}(M^{-1}HM^{-1}HM^{-1})>0\). The feasible connected domain is convex (and its boundary has infinite objective if disconnected). Thus a unique optimum exists. Averaging any optimizer over the graph automorphism group preserves feasibility and cannot increase the objective; uniqueness makes the optimum constant on the three cross-part edge orbits.

**Three-variable reduction.** Let \(X,Y,Z\) be total weights between parts \(ab,bc,ca\). The constraints are
\[
 X,Y,Z\ge0,\quad X+Z\le a,\quad X+Y\le b,\quad Y+Z\le c.
\]
Connectivity requires the three-part weighted graph to be connected. The vertex-contrast Laplacian eigenvalues are \((X+Z)/a\) with multiplicity \(a-1\), \((X+Y)/b\) with multiplicity \(b-1\), and \((Y+Z)/c\) with multiplicity \(c-1\). The remaining two positive eigenvalues have sum
\(S=(X+Z)/a+(X+Y)/b+(Y+Z)/c\) and product \(NQ/(abc)\), where \(Q=XY+YZ+ZX\). Therefore
\[
 F(X,Y,Z)=\frac{a(a-1)}{X+Z}+\frac{b(b-1)}{X+Y}+\frac{c(c-1)}{Y+Z}+\frac{abc}{N}\frac{S}{Q}.
\]
For a singleton part, the corresponding zero-multiplicity summand is interpreted as zero. In the connected domain denominators are positive.

**Interior triangle regime.** Suppose \(c<a+b\). Put \(X=(a+b-c)/2\), \(Y=(b+c-a)/2\), \(Z=(c+a-b)/2\). All are positive and all three row constraints are tight. Set \(g_X=-\partial_X F\), and similarly \(g_Y,g_Z\). An explicit differentiation gives the capacity multipliers
\[
 u_a=(g_X+g_Z-g_Y)/2=1-\frac1a+\frac{bc}{NQ^2}(3aY-Q),
\]
with \(u_b,u_c\) obtained by cyclically permuting the part labels and corresponding edge variables. We verify they are strictly positive. Write \(a=X+Z\), \(b=X+Y\), \(c=Y+Z\), so \(3aY-Q=2aY-XZ\). If \(2aY\ge XZ\), then \(u_a\ge1-1/a\), strictly positive when \(a\ge2\). If \(2aY<XZ\), then \(Y<XZ/(2a)\le a/8\) and
\[
 Q^2-bc(XZ-2aY)=Y\{XZ(3a-Y)+3a^2Y+2aY^2\}>0.
\]
Consequently \(u_a>1-1/a-1/N>0\) for \(a\ge2\). If \(a=1\), then \(X+Z=1\), \(XZ\le1/4\), and the integer inequalities \(b,c\ge1\) give \(Y=(b+c-1)/2\ge1/2\); hence \(2aY-XZ>0\) and again \(u_a>0\). The same proof applies cyclically. These nonnegative multipliers certify stationarity and complementary slackness for every constraint. Strict convexity proves global uniqueness.

**Imbalanced regime, including equality.** Suppose \(c\ge a+b\), put \(s=a+b\), and take \(X=0,Y=b,Z=a\). The \(a\)- and \(b\)-constraints are tight, whereas the \(c\)-constraint has slack \(c-s\). Differentiation of the same \(F\) at this point yields
\[
 g_X=2,\qquad g_Y=g_Z=f,
\qquad f-1=\frac{c^2(s+c-1)-s(s+c)}{s^2(s+c)}>0.
\]
Indeed \(s\ge2,c\ge s\): the numerator is increasing in \(c\) and equals \(s^2(2s-3)>0\) at \(c=s\). Set the capacity multipliers \(u_a=u_b=f,u_c=0\) and the nonnegativity multiplier at \(X=0\) equal to \(2f-2>0\); all other multipliers vanish. These satisfy stationarity and complementary slackness, so strict convexity again proves the proposed kernel is uniquely optimal. Direct substitution in \(F\) gives both displayed value formulas and their equality at \(c=s\).

## Verification
The accompanying standard-library program `check.py` reconstructs the three-part spectral expression and its exact rational gradient, verifies feasibility and Karush–Kuhn–Tucker multipliers for every ordered triple \(1\le a\le b\le c\le18\), and independently constructs full stochastic matrices and rationally inverts \(M(P)\) for small graph orders. It reports 7,989 successful exact-rational checks. These finite tests check implementations and examples; the inequalities above prove the universal assertion.

## Relationship to prior work
Agharkar, Patel, and Bullo (2014) formulate reversible Kemeny optimization as a convex problem, and Patel, Agharkar, and Bullo (2015) provide the expanded formulation. Neither inspected paper gives this complete-tripartite part-size threshold or the optimizer classification. Previously known exact fastest-mixing laws concern a different eigenvalue objective; general convexity alone does not imply the displayed active-set formula. A separately obtained classification of symmetric Kemeny-optimal walks on complete split graphs concerns a different graph family and does not imply this tripartite result.

## Limitations
The theorem does not cover four or more vertex parts, prescribed nonuniform stationary measures, additional edge prices, directed or nonsymmetric walks, or aperiodicity requirements. The mathematical novelty assessment is based on the cited material and indexed comparisons, not a comprehensive literature-priority certification. No independent audit has been carried out.

## References
- P. Agharkar, R. Patel, F. Bullo, *Robotic surveillance and Markov chains with minimal first passage time*, IEEE Conference on Decision and Control, 2014, pp. 6603–6608, DOI: 10.1109/CDC.2014.7040425. Public full text: https://motion.me.ucsb.edu/pdf/2014b-apb-conference.pdf.
- R. Patel, P. Agharkar, F. Bullo, *Robotic Surveillance and Markov Chains With Minimal Weighted Kemeny Constant*, IEEE Transactions on Automatic Control 60 (2015), pp. 3156–3167, DOI: 10.1109/TAC.2015.2426317. Public full text: https://motion.me.ucsb.edu/pdf/2014b-pab.pdf.
- S. Boyd, P. Diaconis, L. Xiao, *Fastest mixing Markov chain on a graph*, SIAM Review 46 (2004), pp. 667–689, DOI: 10.1137/S0036144503423264.
