# Sharp Lipschitz-to-variance norms on diameter-three trees and the branch-imbalance transition

## Finding

Let \(D_{a,b}\) be the finite unit-edge double-star tree obtained by attaching \(a\ge 1\) leaves to one endpoint and \(b\ge1\) leaves to the other endpoint of a central edge. Each vertex has mass \(1/N\), where \(N=a+b+2\). Equip functions modulo constants with the norm \(\|[f]\|_{\mathrm{Lip}}=\max_{uv\in E}|f(u)-f(v)|\), and consider the centered inclusion \(J[f]=f-N^{-1}\sum_v f(v)\) into real \(L^2\) of the vertex probability space. Write \(A=\max(a,b)\) and \(B=\min(a,b)\). Then

\[
\boxed{\|J\|^2=\operatorname{spr}(D_{a,b})=
\frac{N(A+4B+1)-\Delta(A,B)}{N^2},\quad
\Delta(A,B)=\begin{cases}
(2B+1-A)^2,&A\le 2B+1,\\
(A+2B+1)\bmod 2,&A\ge 2B+1.
\end{cases}}
\]

The two branches agree at \(A=2B+1\); modulo two means the integer remainder zero or one. There is a **sharp optimizer transition**: all extremizers are fully polarized when \(A\le2B+1\); both polarized and partially mixed extremizers occur at \(A=2B+2\); and all extremizers are partially mixed when \(A\ge2B+3\).

More precisely, label the hub with \(A\) leaves by \(u\), the other by \(v\). Up to translation and global sign change, every maximizer has \(f(u)=0\), \(f(v)=1\), every leaf at \(v\) equal to \(2\), and precisely \(k\) of the \(A\) leaves at \(u\) equal to \(-1\), with the remaining \(A-k\) equal to \(1\). The admissible \(k\) are exactly the integers \(0\le k\le A\) nearest to \((A+2B+1)/2\). Every such choice is a maximizer. There are two possible values of \(k\) precisely when \(A\ge2B+2\) is even; otherwise \(k\) is unique. Leaves within either class can be permuted freely.

Among **all diameter-three trees on \(N\ge4\) vertices**, the largest such squared norm occurs uniquely (up to graph isomorphism) for the balanced double star \(D_{\lceil(N-2)/2\rceil,\lfloor(N-2)/2\rfloor}\), and equals

\[
\boxed{\max_{\operatorname{diam}(T)=3,\,|V(T)|=N}\|J_T\|^2
=\frac94-\frac4N-\frac{9\mathbf 1_{\{N\mathrm{\ odd}\}}}{4N^2}.}
\]

Thus the sharp approach to the diameter-based bound \(9/4\) has deficit \(4/N\), with a parity correction. These are exact statements for every indicated integer parameter, not asymptotic guesses.

## Assumptions and scope

The graphs are finite, unweighted, undirected trees with their graph-distance metric, and the probability measure is the uniform **vertex** measure, not edge arclength. The functions are real. The functional is the actual centered \(L^2\) embedding norm of the finite Lipschitz function space, not a matrix-eigenvalue spread. The claim applies to every diameter-three tree because such a tree has exactly two adjacent non-leaf vertices and is some \(D_{a,b}\) with \(a,b\ge1\).

## Proof

**1. Every maximizing edge increment saturates.** Fix one hub at value zero and parameterize all functions by the independent increments along the \(a+b+1\) edges. The Lipschitz unit ball becomes a cube \([-1,1]^{a+b+1}\). For any one edge, holding all other increments fixed and varying its increment by \(t\) shifts the values of one nonempty proper vertex component of size \(r\) by \(t\). The coefficient of \(t^2\) in the resulting uniform variance is \(r(N-r)/N^2>0\). Hence variance is strictly convex separately in each increment and cannot attain its maximum at a point with any increment in \((-1,1)\). All maximizers therefore have every edge increment in \(\{-1,1\}\).

**2. Reduce to a two-integer problem.** Global sign reversal makes the hub increment \(+1\); translate so the hub with \(a\) leaves is zero and the other hub is one. Of its \(a\) leaves, let \(k\) have value \(-1\), so the other \(a-k\) have value \(+1\). Of the other hub's \(b\) leaves let \(j\) have value \(+2\), so the remaining \(b-j\) have value zero. For integer \(0\le k\le a\), \(0\le j\le b\), the sum and sum of squares are exactly

\[
S=a+1-2k+2j,\qquad Q=a+1+4j,
\]

so the variance is \(V(k,j)=(NQ-S^2)/N^2\).

**3. Prove complete saturation of the smaller branch.** Assume \(a\ge b\), possible by relabeling. Along any simultaneous increment \((k,j)\mapsto(k+1,j+1)\) the sum \(S\) is unchanged, while \(Q\) rises by four. Thus a maximizer has \(k=a\) or \(j=b\). On the face \(k=a\), the exact change when \(j\) increases by one is

\[
N^2\bigl(V(a,j+1)-V(a,j)\bigr)=4(2a+b-2j)>0
\quad(0\le j<b),
\]

because \(a\ge b\). Therefore **every** maximizer is on \(j=b\).

**4. Solve the remaining integer square.** On \(j=b\),

\[
N^2V(k,b)=N(a+4b+1)-(a+2b+1-2k)^2.
\]

The minimizing integers \(k\) are precisely those nearest \((a+2b+1)/2\), truncated to \([0,a]\). If \(a\le2b+1\), the unique best integer is \(k=a\) and the residual square is \((2b+1-a)^2\). If \(a\ge2b+1\), the nearest even integer to \(a+2b+1\) lies within the admissible interval and the residual square is its parity, zero or one. This gives the formula, all equality cases, the tie at \(a=2b+2\), and the strict transition at \(a=2b+3\). If \(a+2b+1\) is odd and its half lies strictly below \(a\), there are exactly two admissible nearest integers, as claimed.

**5. Prove the unique fixed-order balancing law.** Put \(s=a+b=N-2\) and let the larger leaf count \(a\) increase from \(\lceil s/2\rceil\) to \(s-1\), with \(b=s-a\). On the fully polarized branch the spread is the continuous concave quadratic

\[
F_0(a)=\frac{9s+2}{4(s+2)}-\frac{9(a-s/2)^2}{(s+2)^2},
\]

strictly decreasing for \(a\ge s/2\). Its transition occurs at \(a=(2s+1)/3\), where it meets with matching derivative the decreasing affine function \(F_1(a)=(4s-3a+1)/(s+2)\). On the mixed branch the actual integer spread is \(F_1(a)-\epsilon(a)/(s+2)^2\), where \(\epsilon(a)\in\{0,1\}\) is alternating in \(a\). Each integer increment reduces \(F_1\) by \(3/(s+2)\), whereas changing \(\epsilon\) can add at most \(1/(s+2)^2\), so the discrete sequence remains strictly decreasing there. At the crossover, the continuous envelope is strictly decreasing and the discrete parity correction is nonpositive. Hence the unique maximizing unordered pair is the most balanced pair. Substituting it gives the asserted \(9/4-4/N\) upper envelope and the odd-\(N\) correction \(9/(4N^2)\). A tree has diameter three if and only if it is such a proper double star, finishing the classification.

## Verification

The standalone standard-library checker `check_double_star.py` independently enumerates all signed edge-increment configurations for \(1\le a,b\le8\), checking both exact variance and **all** predicted maximizing profiles (64 pairs). It also compares the closed formula against direct integer \((k,j)\)-maximization on 6,400 parameter pairs, verifies exact fixed-order balancing through \(s=300\), and checks the transition and parity ties through \(b=99\). Run `python check_double_star.py`; expected final marker: `ALL_DOUBLE_STAR_LIPSCHITZ_SPREAD_CHECKS_OK`. All universal assertions above are supplied by the symbolic argument, not inferred from these finite checks.

## Relationship to prior work

Alon, Boppana and Spencer introduced the graph-metric Lipschitz spread and established the integer-extremizer principle and its role in product isoperimetry [1, §2]. Their existence theorem is a starting point but gives no two-parameter formula for double stars, no complete optimizer counts and no imbalance transition. Addario-Berry, Janson and McDiarmid [2, §1] discuss graph-spread values on paths, complete graphs and product graphs and study random-graph spread. They provide no diameter-three-tree classification. The identity between the spread and the squared centered Lipschitz-to-\(L^2\) embedding norm is a direct reformulation, not claimed as novel. The new claim is the sharp finite classification, its equality cases, and the fixed-order envelope. The closest independently indexed mathematical result on double stars considered a different graph invariant (fractional zero forcing), not this extremal variance; it has no implication for the stated norms.

## Limitations

The formulas do not address nonuniform vertex masses, weighted edges, edge-arclength spread, longer trees, nonlinear target spaces, or other diameter classes. The mathematical proof establishes the stated infinite families, but the novelty assessment cannot exclude an equivalent unindexed or inaccessible earlier computation. No independent mathematical audit is claimed.

## References

[1] N. Alon, R. Boppana and J. Spencer, *An Asymptotic Isoperimetric Inequality*, Geometric and Functional Analysis 8 (1998), 411–436, DOI: 10.1007/s000390050062. Author-hosted full text: https://web.math.princeton.edu/~nalon/PDFS/iso7.pdf .

[2] L. Addario-Berry, S. Janson and C. McDiarmid, *On the spread of random graphs*, first public arXiv preprint on 2009-02-06, arXiv:0902.1156 (later revision 2012). https://arxiv.org/abs/0902.1156 .

[3] M. Sammer and P. Tetali, *Concentration on the Discrete Torus Using Transportation*, Combinatorics, Probability and Computing 18 (2009), 835–860, DOI: 10.1017/S0963548309990319 (abstract and bibliographic comparison only).
