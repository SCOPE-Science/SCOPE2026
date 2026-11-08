# Sharp positivity horizons for the \(\theta\)-method on complete bipartite heat networks

## Finding
Consider the heat equation \(\dot u=-Lu\) on an unweighted complete bipartite graph \(K_{p,q}\), where \(p,q\) are positive integers and \(N=p+q\ge3\), with combinatorial Laplacian \(L\). For a real parameter \(0\le\theta\le1\) and step \(h\ge0\), its \(\theta\)-method end-step map is
\[
T_{\theta,h}=(I+\theta hL)^{-1}(I-(1-\theta)hL).
\]
Here positivity means entrywise nonnegativity of \(T_{\theta,h}\), equivalently preservation of the nonnegative cone for every initial vector. The matrix always preserves constant vectors and total mass; positivity makes it a doubly stochastic transition matrix.

Put \(m=\min\{p,q\}\), \(M=\max\{p,q\}\), and \(\theta_c=(N-1)/N\). **The exact largest positivity-preserving step** is
\[
h_* = \begin{cases}
1/M,&\theta=0,\\[2mm]
\dfrac{E+\sqrt{E^2+4D\theta}}{2\theta D},&0<\theta<\theta_c,\\[3mm]
+\infty,&\theta_c\le\theta\le1,
\end{cases}
\qquad
E=m\theta+M(2\theta-1),\quad D=M(N-1-N\theta).
\]
Precisely, \(T_{\theta,h}\) is entrywise nonnegative **if and only if** \(0\le h\le h_*\). The convention \(h\le+\infty\) means all finite steps. Thus the *sharp unconditional-positivity parameter* is \(\theta_c\), strictly below backward Euler's \(\theta=1\), and depends only on the total vertex count.

For each fixed \(N\ge3\) and each \(0\le\theta<\theta_c\), the finite threshold \(h_*\) **strictly increases with the size of the smaller bipartition part**. Consequently the star \(K_{1,N-1}\) has the smallest admissible horizon and the most balanced complete bipartite graph has the largest; this comparison holds without rescaling the individual edge rates. For Crank--Nicolson, \(\theta=1/2\), the horizon is
\[
h_*^{\mathrm{CN}}=\frac{m+\sqrt{m^2+4M(N-2)}}{M(N-2)}.
\]
For \(N=4\), the star's Crank--Nicolson horizon is \(1\), versus \((1+\sqrt5)/2\) for \(K_{2,2}\). As \(N\to\infty\), the star and balanced horizons are respectively asymptotic to \(2/N\) and \(4/N\).

## Assumptions and scope
All graphs are simple, connected, complete bipartite and unweighted. Their edge conductances are exactly one. The Laplacian is \(L=\operatorname{diag}(\deg)-A\), not its normalized version. The equation \(\dot u=-Lu\) is interpreted on column vectors; the matrices are symmetric so row and column conventions agree. No source term, space discretization beyond this fixed graph, or stage positivity is asserted. Every positive integer pair \((p,q)\) with \(p+q\ge3\), every real \(\theta\in[0,1]\), and every real step \(h\ge0\) is covered, including boundary equality. A nonzero constant edge rate \(c\) would divide all displayed thresholds by \(c\), but no heterogeneous edge-rate claim is made.

## Proof
First take \(0<\theta\le1\), write \(t=\theta h\), and put \(R_t=(I+tL)^{-1}\). The resolvent identity gives
\[
T_{\theta,h}=\frac{R_t-(1-\theta)I}{\theta}.
\]
Since \(L\) is a connected graph Laplacian, \(I+tL\) is a nonsingular irreducible \(M\)-matrix for \(t>0\), hence \(R_t\) has strictly positive entries. Every off-diagonal entry of \(T_{\theta,h}\) is therefore strictly positive when \(h>0\); it remains only to check diagonal entries. The identity \(R_t\mathbf1=\mathbf1\) also proves mass conservation.

The eigenspaces of \(L\) decompose orthogonally into the constants (eigenvalue \(0\)), zero-sum vectors supported on the part of size \(p\) (eigenvalue \(q\), dimension \(p-1\)), zero-sum vectors supported on the part of size \(q\) (eigenvalue \(p\), dimension \(q-1\)), and the part-contrast direction (eigenvalue \(N\), dimension one). For a vertex in the part of size \(p\), the associated projector diagonal weights are \(1/N\), \((p-1)/p\), and \(q/(pN)\). Therefore the diagonal resolvent entries at vertices in the smaller and larger parts, respectively, are
\[
r_m(t)=\frac1N+\frac{m-1}{m(1+Mt)}+\frac{M}{mN(1+Nt)},
\]
\[
r_M(t)=\frac1N+\frac{M-1}{M(1+mt)}+\frac{m}{MN(1+Nt)}.
\]
Their difference simplifies exactly to
\[
r_m(t)-r_M(t)=\frac{t(m-M)(1+(N-1)t)}{(1+mt)(1+Mt)(1+Nt)}\le0.
\]
Thus it is necessary and sufficient that the smaller-part diagonal satisfies \(r_m(t)\ge1-\theta\), with tied requirements if \(m=M\).

An equivalent expression, obtained by collecting the common denominator in \(r_m\), is
\[
r_m(t)=\frac{1+Nt+Mt^2}{(1+Mt)(1+Nt)}.
\]
Indeed the numerator expands from the eigenspace expression, and has value \(1\) at \(t=0\). Subtracting \(1-\theta\) yields the exact sign identity
\[
r_m(t)-(1-\theta)=\frac{\theta+[m\theta+M(2\theta-1)]t-M(N-1-N\theta)t^2}{(1+Mt)(1+Nt)}
=\frac{\theta+Et-Dt^2}{(1+Mt)(1+Nt)}.
\]
For \(\theta<\theta_c\), one has \(D>0\); the concave quadratic starts at \(\theta>0\), tends to \(-\infty\), and its two roots have opposite signs. Its unique positive root is \((E+\sqrt{E^2+4D\theta})/(2D)\). Since \(t=\theta h\), the claimed finite threshold and exact equivalence follow. For \(\theta\ge\theta_c\), the spectral expression gives \(r_m(t)>1/N\ge1-\theta\) for all finite \(t\ge0\), so positivity is unconditional. If \(\theta<\theta_c\), \(r_m(t)\to1/N<1-\theta\) as \(h\to\infty\), proving sharpness of the parameter cutoff.

At \(\theta=0\), \(T_{0,h}=I-hL\). Its off-diagonal entries are nonnegative and the smallest diagonal is \(1-Mh\), so the exact threshold is \(1/M\).

For the balance-ordering assertion at a fixed \(N\) and fixed \(0<\theta<\theta_c\), write the numerator of the sign identity as
\[
F_m(t)=\theta+[m\theta+(N-m)(2\theta-1)]t-(N-m)(N-1-N\theta)t^2.
\]
For each admissible consecutive pair of smaller-part sizes, \(m\) and \(m+1\), and every \(t>0\),
\[
F_{m+1}(t)-F_m(t)=(1-\theta)t+(N-1-N\theta)t^2>0.
\]
Both \(F_m\) and \(F_{m+1}\) have exactly one positive root and are positive below it. Hence the root, and therefore \(h_*\), strictly grows with \(m\). For \(\theta=0\), the same assertion follows from \(h_*=1/(N-m)\). The Crank--Nicolson formula follows by substituting \(\theta=1/2\) into \(E,D\); in this case \(E=m/2\) and \(D=M(N-2)/2\). Finally, applying the explicit formula to \((m,M)=(1,N-1)\) and to \((\lfloor N/2\rfloor,\lceil N/2\rceil)\) gives the two asymptotics by elementary division by \(N\).

## Verification
The accompanying standalone `verify.py` reconstructs complete bipartite Laplacians and inverts \(I+\theta hL\) by exact rational Gaussian elimination. For all \(1\le p,q\le5\) with \(p+q\ge3\), seven rational \(\theta\)-values and seven rational steps, it verifies the spectral resolvent matrix formula, mass conservation, off-diagonal positivity, the quadratic sign criterion, and the identity of the limiting diagonal vertex class: **1,176 exact full-matrix instances**. The checker also verifies the Euler endpoint and strict balance-ordering sign comparison on sizes through \(N=39\), plus exact Crank--Nicolson boundary comparisons at \(N=4\). Execute `python verify.py` with the Python standard library. These finite checks do not establish the all-size theorem; the proof above does.

## Relationship to prior work
The general Runge--Kutta monotonicity and positivity-radius problem is classical, including Horváth's 1998 positivity study. The exact Crank--Nicolson threshold and partition-minimum ordering have also already been derived for **all complete multipartite graphs** (a family strictly including \(K_{p,q}\)). Thus the \(\theta=1/2\) specialization and its partition extremality are reproduced for consistency and **not claimed as new**. Fallat and Tsatsomeros (2002), Lemma 2.2 and Section 4, give the Cayley-transform identity and investigate positivity classes of \(M\)-matrices. A later published resolvent-return law evaluates the exact Crank--Nicolson positivity criterion for a general reversible finite Markov chain in terms of resolvent return diagonals, including complete graphs and two-state chains. The algebra reducing this problem to diagonal resolvent entries is **not** claimed as new.

Bonnans and Tan (2011) study necessary and sufficient monotonicity conditions for \(\theta\)-schemes on diffusion grids and explicitly evaluate a heat-equation case. The accessible abstract identifies that scope; its full text was not retrievable and no whole-document noncoverage conclusion is claimed. Here the specifically assessed contribution is a **complete bipartite heat network for the entire continuous \(\theta\)-family**, with a closed radical step frontier across all \(\theta\), including sharp finite-to-unconditional transition and the partition-order comparison at all finite-horizon \(\theta\). The generic diagonal-resolvent method and the previously evaluated Crank--Nicolson slice are not claimed original. Neither the reversible-chain diagonal criterion alone nor the cited grid-diffusion abstract gives those displayed graph-family evaluations without the projector and comparison calculations above.

## Limitations
The formula is not a bound for arbitrary graphs with the same degree sequence, nor does it cover unequal edge rates or normalized Laplacians. Stage positivity is not inferred from end-step positivity. No claim of independence, publication priority against all literature, or external certification is made. The 2011 diffusion-grid report is a plausible partially inaccessible source: although its reported objects differ from complete bipartite networks, an unknown graph specialization or mathematically equivalent calculation cannot be excluded without full-text inspection. More general unpublished or unindexed semigroup literature could also contain an equivalent formula. These access/priority risks do not affect the self-contained proof.

## References
1. J. Frédéric Bonnans and Xiaolu Tan, *Monotonicity condition for the \(\theta\)-scheme for diffusion equations*, INRIA Research Report 7778, public record dated 2011-10-21, HAL identifier `inria-00634417`, https://www.econbiz.de/10009325717 .
2. Zoltán Horváth, *Positivity of Runge--Kutta and Diagonally Split Runge--Kutta Methods*, Applied Numerical Mathematics 28 (1998), 309--326, DOI: 10.1016/S0168-9274(98)00050-6.
3. Shaun M. Fallat and Michael J. Tsatsomeros, *On the Cayley Transform of Positivity Classes of Matrices*, Electronic Journal of Linear Algebra 9 (2002), 190--196, DOI: 10.13001/1081-3810.1086, https://journals.uwyo.edu/index.php/ela/article/download/173/173 .
4. *A resolvent-return law for Crank--Nicolson positivity on reversible Markov chains*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a .
