# Exact optimal randomized Kaczmarz sampling on mirrored adjacent-coordinate paths

## Finding
Fix an integer \(n\ge 3\) and real numbers \(a,b>0\) satisfying \(a+b=1\). In \(\mathbb R^n\) consider the \(2(n-1)\) unit measurement rows
\[
u_{i,\pm}=\sqrt a\,e_i\pm\sqrt b\,e_{i+1},\qquad 1\le i<n.
\]
For every probability vector \(w=(w_{i,\pm})\) on these rows, let
\[
S(w)=\sum_{i=1}^{n-1}\sum_{\sigma\in\{+,-\}}w_{i,\sigma}u_{i,\sigma}u_{i,\sigma}^{\mathsf T},\qquad
\Lambda_n(a,b)=\max_w\lambda_{\min}(S(w)).
\]
Define \(c=\min\{a,b\}\), \(d=\max\{a,b\}\), and \(r=c/d\). Then the exact optimum is
\[
\boxed{\Lambda_n(a,b)=\left[\frac1c+n-2+c\left(1-(-r)^{n-2}\right)\right]^{-1}.}
\]
For \(a\le b\), set \(Q=1/\Lambda_n(a,b)\) and
\[
q_1=\frac1a,\qquad q_i=1-(-a/b)^{n-i}\quad(2\le i<n).
\]
The row probabilities \(w_{i,+}=w_{i,-}=q_i/(2Q)\) attain the optimum. For \(a>b\), reverse their edge order, replacing \(q_i\) by the corresponding \(q_{n-i}\) computed with \(c\) in place of \(a\). When \(a\ne b\), this is the **unique** optimal probability vector: both signs of every adjacent-coordinate pair have strictly positive probability. At \(a=b=1/2\), an optimum supported on exactly \(\lceil n/2\rceil\) of the \(n-1\) adjacent-coordinate pairs exists, and the optimal value becomes \(1/[2\lceil n/2\rceil]\).

Equal row probabilities instead achieve \(\Lambda_{\mathrm{unif}}=c/(n-1)\). The exact ratio of optimal to uniform worst-case one-step expected-squared-error reduction is \((n-1)/(cQ)\), which tends to \(n-1\) when \(c\downarrow0\) for each fixed \(n\). In particular the potential acceleration factor over equal sampling is unbounded as the problem dimension grows.

## Assumptions and scope
The linear system containing these rows is consistent, and standard randomized Kaczmarz independently selects one unit row with the fixed distribution \(w\) at each iteration. The criterion is the **sharp worst-case conditional one-step mean-squared Euclidean-error contraction factor**, equal to \(1-\lambda_{\min}(S(w))\), not the exact finite-horizon or asymptotic mean-square exponent of the induced stochastic matrix product. The optimization is over **all** probabilities on individual signed rows; neither within-pair balancing nor equal edge probabilities is assumed.

Every \(a,b>0\) with \(a+b=1\) is covered, including \(a=b\); zero endpoint parameters are excluded because the measurement frame then loses rank. All dimensions \(n\ge3\) are covered. The parameters \(a,b\) are squared coordinate amplitudes, not edge weights of a graph Laplacian.

## Proof
**1. Reduction to a spectral maximin problem.** For a current error \(z\), a Kaczmarz projection along a unit measurement row \(u\) replaces \(z\) by \(z-uu^{\mathsf T}z\). Orthogonality of that projection gives
\[
\mathbb E\big[\|z^+\|_2^2\mid z\big]=\|z\|_2^2-z^{\mathsf T}S(w)z.
\]
Taking the worst nonzero \(z\) proves that maximizing the guaranteed one-step decrease is precisely maximizing \(\lambda_{\min}(S(w))\). Write \(p_i=w_{i,+}+w_{i,-}\). The diagonal entries of \(S(w)\) are
\[
S_{jj}=a p_j+b p_{j-1},\qquad p_0=p_n=0,
\]
and its only possible nonzero off-diagonal entries are
\[
S_{i,i+1}=\sqrt{ab}\,(w_{i,+}-w_{i,-}).
\]

**2. Exact universal dual bound.** First suppose \(0<a\le b\), and put \(r=a/b\). Define
\[
y_1=1/a,\quad y_2=0,\quad y_j=1-(-r)^{j-2}\ (3\le j\le n).
\]
These entries are nonnegative, including at \(a=b\). Direct substitution shows
\[
a y_i+b y_{i+1}=1\quad(1\le i<n),\qquad
\sum_{j=1}^n y_j=Q:=\frac1a+n-2+a\big(1-(-r)^{n-2}\big).
\]
For **every** probability distribution \(w\), irrespective of within-pair asymmetry,
\[
\sum_{j=1}^n y_j S_{jj}(w)
=\sum_{i=1}^{n-1}p_i(a y_i+b y_{i+1})=1.
\]
Because every diagonal entry of a real symmetric matrix is at least its least eigenvalue, \(1\ge Q\lambda_{\min}(S(w))\). Thus \(\Lambda_n(a,b)\le1/Q\) without any symmetry assumption.

**3. Attaining the bound.** Let
\[
q_1=1/a,\qquad q_i=1-(-r)^{n-i}\quad(2\le i<n).
\]
Every \(q_i\ge0\), and the finite geometric sum gives \(\sum_{i=1}^{n-1}q_i=Q\). Set \(w_{i,+}=w_{i,-}=q_i/(2Q)\). The off-diagonal entries of \(S\) then vanish. Its first diagonal entry is \(1/Q\), and every diagonal entry from the third through the last equals \(1/Q\), since
\[
bq_{j-1}+a q_j=1\quad(3\le j\le n),\qquad q_n:=0.
\]
The second diagonal entry is \((b/a+a q_2)/Q\), which is at least \(1/Q\) because \(b\ge a\). Thus \(\lambda_{\min}(S)=1/Q\), attaining the upper bound. The case \(a>b\) follows by reversing the coordinate order, which interchanges the two squared amplitudes.

**4. Uniqueness away from balance.** If \(a<b\), then \(y_j>0\) for every \(j\ne2\), and the equality case in Step 2 forces \(S_{jj}=1/Q\) for all such \(j\). Since \(S-(1/Q)I\) is positive semidefinite, any zero diagonal in that difference forces the entire corresponding row and column to vanish. Every adjacent pair of coordinates touches an index other than \(2\), so all \(S_{i,i+1}=0\) and therefore \(w_{i,+}=w_{i,-}\). The conditions at coordinates \(1,n,n-1,\ldots,3\) uniquely determine the edge masses: the first is \(p_1=1/(aQ)\), the last is \(p_{n-1}=1/(bQ)\), and backward substitution in the remaining equalities yields precisely \(p_i=q_i/Q\). As \(r<1\), all \(q_i>0\). Reversal proves the same statement for \(a>b\).

**5. Balanced support transition.** At \(a=b=1/2\), the formula yields \(Q=2\lceil n/2\rceil\). The weights \(q_i\) above are either \(0\) or \(2\), with exactly \(\lceil n/2\rceil\) positive entries. They define a minimum edge cover of the coordinate path and hence a sparse optimal sampler. This is an existence statement, not a claim that every balanced optimum is sparse or unique.

**6. Equal sampling and the sharp gain.** Equal probabilities \(w_{i,\pm}=1/[2(n-1)]\) give diagonal information matrix entries \(a/(n-1)\), \(1/(n-1)\) at interior coordinates, and \(b/(n-1)\), with all off-diagonal entries zero. Therefore \(\Lambda_{\mathrm{unif}}=c/(n-1)\). Since \(cQ\to1\) as \(c\downarrow0\) at fixed \(n\), the reduction ratio approaches \(n-1\) exactly.

## Verification
The standalone `verify.py` checks the closed primal and dual certificates, geometric-sum normalization, the balanced minimum edge-cover support, and exact individual-row projector summation using rational amplitudes. It uses only Python's standard-library `fractions.Fraction`. The checked finite parameter grid and its counts are reported in `VERIFICATION.md`. These checks are reproducible spot checks; the proof above applies to infinitely many real parameters and all integer dimensions \(n\ge3\).

## Relationship to prior work
Dai–Soltanalian–Pelckmans (2014) establish the unrestricted Kaczmarz probability-design semidefinite program and discuss its numerical and approximate solution. The present claim specializes that already-known criterion to a concrete finite frame family and evaluates the optimum, **all unbalanced optimal row weights**, the exceptional sparse balanced support, and the sharp uniform-sampling comparison in exact closed form. Their inspected main theorems and numerical examples do not state these formulas.

Chen–Powell (2014/2015) study Kaczmarz bounds and optimal distributions over subspace families, including globally invariant choices and tight frames. Their unrestricted-subspace theory does not specify the E-optimal design within this fixed, nonisotropic, signed path frame. Agaskar–Wang–Lu (2014) investigate exact mean-square errors and optimized sampling; only the abstract could be accessed here, so a potential more specialized comparison with that paper remains a priority risk.

## Limitations
No assertion is made about minimizing the **exact** asymptotic mean-square exponent, residual convergence on inconsistent systems, adaptive or time-varying sampling, arbitrarily varied adjacent-pair angles, or the uniqueness of the balanced optimum. The calculated gain concerns the worst-case per-step guaranteed **decrease** in squared error, not a ratio of contraction factors \(1-\Lambda\). The external-literature comparison is not an exhaustive priority proof; one plausible primary paper was not available in full text.

## References
- L. Dai, M. Soltanalian, K. Pelckmans, *On the Randomized Kaczmarz Algorithm* (first public February 12, 2014), arXiv:1402.2863, https://arxiv.org/abs/1402.2863. Examined PDF, Sections II–V.
- X. Chen, A. M. Powell, *Fusion frames and randomized subspace actions* (first public March 24, 2014), arXiv:1403.6190, https://arxiv.org/abs/1403.6190. Examined PDF, Sections 4–6.
- A. Agaskar, C. Wang, Y. M. Lu, *Randomized Kaczmarz algorithms: Exact MSE analysis and optimal sampling probabilities*, GlobalSIP 2014, https://doi.org/10.1109/GlobalSIP.2014.7032145. Abstract inspected; full text was not accessible.
