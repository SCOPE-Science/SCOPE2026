# Cut-size law for locally stable minority configurations on wheel graphs

## Finding
For every integer \(n\ge3\), let \(W_n=K_1\vee C_n\) be the labelled simple wheel with one hub and an \(n\)-vertex rim. Under synchronous binary *minority* updates (adopt the strict minority among open-neighbor opinions, retain the current opinion on a tie), define the fixed-point cut polynomial
\[
 Q_n(q)=\sum_{x:\,F(x)=x}q^{c(x)},\qquad
 c(x)=\#\{\{v,w\}\in E(W_n):x_v\ne x_w\}.
\]
Then the complete polynomial is
\[
 \boxed{Q_n(q)=2\sum_{z=\lceil n/3\rceil}^{\lfloor n/2\rfloor}
    \frac nz\binom{z}{n-2z}\,q^{n+z}.}\tag{1}
\]
Every listed coefficient is positive and there are no other fixed cut sizes. The global maximum cut size is \(n+\lfloor n/2\rfloor\). Fixed states with strictly suboptimal cuts exist exactly when \(n=6\) or \(n\ge8\); the other wheel lengths \(n=3,4,5,7\) have only globally maximum-cut fixed configurations. There are exactly four optimal configurations for even \(n\), and exactly \(2n\) for odd \(n\).

Let \(X_n\) be uniformly sampled among the fixed configurations, and let \(\rho>1\) be the real root of \(\rho^3-\rho-1=0\). Put
\[
 \mu=\frac{\rho+1}{2\rho+3}=0.411495588662\ldots,\qquad
 v=\frac{\rho(\rho+1)}{(2\rho+3)^3}=0.0170796290575\ldots.
\]
Then the fixed-state population, the central limit theorem for its cut size, and the mean/variance asymptotics are
\[
 Q_n(1)=2\operatorname{Perrin}(n)=2\rho^n+O(\rho^{-n/2}),\qquad
 \frac{c(X_n)-n(1+\mu)}{\sqrt{nv}}\ \Rightarrow\ N(0,1),
\]
\[
 \mathbb E\,c(X_n)=n(1+\mu)+o(1),\qquad
 \operatorname{Var}(c(X_n))=nv+o(1).
\tag{2}
\]
Thus a typical locally stable minority configuration cuts about \(1.411496n\) edges, versus an optimum of about \(1.5n\). The fraction of fixed configurations that are globally optimal is \(4/Q_n(1)\) for even \(n\) and \(2n/Q_n(1)\) for odd \(n\), hence tends to zero exponentially. The exact unweighted Perrin numbers and their cyclic maximal-independent-set interpretation are *known*; the mathematical content assessed here is the wheel-dynamical cut-size spectrum and its explicit typical-quality fluctuation law.

## Assumptions and scope
The rim vertices and hub are distinct, opinions are in \(\{0,1\}\), the update acts simultaneously, and a fixed point means \(F(x)=x\) from time zero. A tie causes no opinion change; the hub has \(n\) neighbors and each rim vertex has exactly three. No conclusions about nonfixed trajectories or their eventual periods are claimed. The cut is undirected, each edge counted once. Labels distinguish the \(n\) rim positions.

## Proof
**Local form.** Fix the hub opinion to zero by globally complementing opinions. At a rim vertex holding zero, minority retention is equivalent to both of its rim neighbors holding one. At a rim vertex holding one, minority retention is equivalent to at least one rim neighbor holding zero. Therefore every fixed rim word avoids cyclic substrings \(00\) and \(111\), and conversely those two exclusions ensure that all rim vertices remain fixed. Such a word consists cyclically of \(z\) occurrences of zero separated by runs of one or two ones, so \(\lceil n/3\rceil\le z\le\lfloor n/2\rfloor\). Since the zeros are isolated, the number of rim ones is at least the number of zeros, making the hub zero a minority or tie; consequently the hub stays fixed. This proves both necessity and sufficiency, including the even-\(n\) hub-tie case.

**Enumeration and cut size.** Exactly \(n-2z\) of the \(z\) runs of ones have length two. Choose those runs in \(\binom{z}{n-2z}\) ways around a distinguished zero; choosing the position of that zero gives \(n\) possibilities, and each labelled rim word is represented \(z\) times. Hence there are \(\frac nz\binom{z}{n-2z}\) words. Their cut contains \(n-z\) hub-to-rim edges and exactly \(2z\) rim-to-rim edges, totaling \(n+z\). Complementing all opinions gives a disjoint second family, proving (1).

**Optimality and the exceptional lengths.** For any state with hub zero and \(k\) rim ones, there are \(k\) cut spokes, while the number of cut rim edges is at most \(2\min(k,n-k)\). Maximizing \(k+2\min(k,n-k)\) over \(0\le k\le n\) gives \(n+\lfloor n/2\rfloor\), which is attained by the alternating or near-alternating fixed states at \(z=\lfloor n/2\rfloor\). Their number follows by putting \(z=\lfloor n/2\rfloor\) in (1). A strictly smaller cut occurs precisely when \(\lceil n/3\rceil<\lfloor n/2\rfloor\), equivalently \(n=6\) or \(n\ge8\). Moreover, the spin flip of a single vertex changes the cut by \(\deg(v)-2(\#\text{cut edges incident to }v)\). Therefore the fixed states of minority dynamics are exactly the one-vertex-flip locally maximal cuts; ties are correctly treated as local maxima.

**Weighted transfer and distribution.** Assign a weight \(u\) to each zero in a cyclic rim word. In the ordered pair-state basis \(01,10,11\), the transfer matrix is
\[
 B(u)=\begin{pmatrix}0&u&1\\1&0&0\\0&u&0\end{pmatrix},
 \qquad \det(tI-B(u))=t^3-ut-u.
\]
Allowed transitions are exactly those preserving avoidance of \(00\) and \(111\), and every closed length-\(n\) walk encodes precisely one labelled cyclic word (the pair at each vertex is specified by that word). Thus
\[
 Q_n(q)=2q^n\operatorname{tr}(B(q)^n).
\tag{3}
\]
At \(u=1\), the trace has initial values \(3,0,2\) in degrees \(0,1,2\) and obeys \(R_n=R_{n-2}+R_{n-3}\); it is the classical Perrin sequence. The unique positive dominant eigenvalue \(\rho\) satisfies \(\rho^3-\rho-1=0\); the two other roots have modulus \(\rho^{-1/2}\), establishing the population asymptotic.

For \(u\) complex and sufficiently close to \(1\), the simple positive eigenvalue \(\lambda(u)\) of \(B(u)\) continues analytically and dominates the other roots uniformly. It satisfies \(\lambda(u)^3=u(\lambda(u)+1)\). Hence for real \(t\) near zero the moment generating function of the random zero count \(Z_n\) obeys
\[
 \log\mathbb E e^{tZ_n}
 =n\left[\log\lambda(e^t)-\log\rho\right]+O(\theta^n),
 \qquad 0<\theta<1,
\]
with an error analytic and uniform in a complex neighborhood of zero. Implicit differentiation yields
\[
 \left.\frac{d}{dt}\log\lambda(e^t)\right|_{t=0}=\mu,
 \qquad
 \left.\frac{d^2}{dt^2}\log\lambda(e^t)\right|_{t=0}=v>0.
\]
Substituting \(t=is/\sqrt{nv}\) into the characteristic function and expanding analytically to second order gives \(\exp(-s^2/2)+o(1)\) for each real \(s\); the Lévy continuity theorem proves the normal limit. Differentiating the analytic error gives \(\mathbb E Z_n=n\mu+o(1)\) and \(\operatorname{Var}Z_n=nv+o(1)\). Since \(c(X_n)=n+Z_n\), (2) follows. Finally the optimal counts are polynomial in \(n\), whereas the fixed total grows as \(2\rho^n\), proving exponential scarcity.

## Verification
Run `python3 checks/direct_census.py` to independently enumerate every binary state of the wheels for \(3\le n\le14\), update the hub and rim directly, and compute cut sizes; this checks (1) on all those sizes. Run `python3 checks/transfer_certificate.py` to check the Perrin recurrence to length 150 and 600 exact weighted-trace identities to length 100 for six integer fugacities, together with variance convergence at five lengths. Recorded outputs are `checks/direct_census.out` and `checks/transfer_certificate.out`. Both scripts are standard-library-only; finite tests do not establish the all-length theorem or the CLT independently of the proof above.

## Relationship to prior work
The unweighted sequence, its cycle maximal-independent-set interpretation, the Perrin recurrence, and even the *unweighted* binomial summands appearing in (1) are explicitly recorded in OEIS A001608; these ingredients are not claimed as original. Indeed the zero locations on the rim are precisely maximal independent sets of the underlying cycle, and the transfer construction is a standard method. The result instead identifies their exact cut-energy realization in *minority wheel dynamics*, characterizes the optimality gap and gives an explicit normal fluctuation law for the locally stable cut quality. Wacław and Burda (2008) study metastable states under random Gaussian spin-glass couplings on general graphs, rather than the uniformly anti-aligned wheel with the specified tie rule. Kaul and West (2008) study lengths of local-improvement sequences for bipartite cuts, rather than energy-resolved populations of their local optima on a wheel. The overlap assessment does not assert historical priority beyond the sources examined.

## Limitations
The Perrin total and the cyclic run-count formula are pre-existing mathematics, so the present findings should not be advertised as a new sequence or a new maximal-independent-set enumerator. The novelty assessment is qualified by possible prior specialized distributional work on maximal independent sets and locally optimal cuts. The result is for fixed configurations only, not basins, nontrivial cycles, arbitrary weights, other wheels, or independent scientific validation. The general theorem relies on the proof above, not on finite simulations.

## References
1. B. Wacław and Z. Burda, *Counting metastable states of Ising spin glasses on arbitrary graphs*, arXiv:0801.1224, first public version 2008-01-08; *Physical Review E* **77** (2008), 041114. https://arxiv.org/abs/0801.1224
2. H. Kaul and D. B. West, *Long local searches for maximal bipartite subgraphs*, *SIAM Journal on Discrete Mathematics* **22** (2008), 1138–1144. https://doi.org/10.1137/060666615
3. OEIS Foundation, *A001608: Perrin sequence*; entries documenting cycle maximal independent sets and the binomial summation. https://oeis.org/A001608
4. B. E. Sagan and V. R. Vatter, *Maximal and maximum independent sets in graphs with at most \(r\) cycles*, *Journal of Graph Theory* **53** (2006), 283–314. https://doi.org/10.1002/jgt.20186
