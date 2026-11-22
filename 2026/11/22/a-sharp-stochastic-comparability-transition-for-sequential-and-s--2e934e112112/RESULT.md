# A sharp stochastic-comparability transition for sequential and static parking on wheels

## Finding
For each integer \(n\ge3\), let \(W_{n+1}=K_1\vee C_n\) be a wheel with \(n\) rim vertices and one universal hub. In the **sequential** parking model, inspect the vertices in uniformly random order, accepting one exactly when none of its already accepted neighbors is adjacent to it. In the **static** model, choose uniformly from all inclusion-maximal independent vertex sets. Let \(X_n\) and \(Y_n\) be the respective cardinalities.

**Sharp classification.** With \(\le_{\mathrm{st}}\) denoting ordinary first-order stochastic order,
\[
\begin{array}{ll}
\mathcal L(X_n)=\mathcal L(Y_n), & n\in\{3,5,7\},\\
Y_n<_{\mathrm{st}} X_n, & n\in\{4,6\},\\
X_n\text{ and }Y_n\text{ are incomparable}, & n\ge8.
\end{array}
\]
Here strict order means stochastic domination with at least one strict tail inequality. In particular, the ordinary nine-vertex wheel \(W_9\) is the first wheel where these two natural occupancy laws are not comparable; the conclusion holds for every larger wheel.

The mechanism at \(n\ge8\) is sharp and two-sided:
\[
\Pr(X_n=1)=\frac1{n+1}>\frac1{M_n+1}=\Pr(Y_n=1),
\qquad \mathbb E X_n>\mathbb E Y_n,
\]
where \(M_n\) is the number of maximal independent sets of \(C_n\). Hence the sequential law is simultaneously more likely to suffer the rare one-vertex hub outcome **and** has a higher mean. The two CDFs must cross.

## Assumptions and scope
All graphs are finite, simple, undirected, and unweighted. A cycle \(C_n\) has \(n\ge3\) vertices. Each vertex receives one independent continuous arrival priority; the sequential algorithm accepts vertices in increasing priority order if unblocked. The static model weights maximal independent sets equally, **not** all independent sets equally. No independence between the two models is required to discuss stochastic comparison. There are no assertions for non-wheel graphs or for nonuniform arrival priorities. Here \(W_{n+1}\) has \(n+1\) total vertices; this convention avoids ambiguity in wheel indexing.

Put \(R_m\) for the greedy occupancy count on a path of \(m\) vertices, with \(R_0=R_{-1}=0\). Let \(S_n\) be greedy occupancy on \(C_n\), and let \(T_n\) be the cardinality of a uniform maximal independent set of \(C_n\).

## Proof
**1. Two exact finite-mixture identities.** The earliest priority on \(W_{n+1}\) falls at the hub with probability \(1/(n+1)\), giving exactly one accepted vertex. Otherwise the hub is immediately blocked, and the accepted rim vertex leaves an unblocked path of length \(n-3\). The remaining relative rim order is uniform. Therefore
\[
S_n\overset d=1+R_{n-3},\qquad
\mathcal L(X_n)=\frac1{n+1}\delta_1+\frac n{n+1}\mathcal L(S_n).
\]
The maximal independent sets of a wheel consist of the hub singleton and precisely the maximal independent sets of the rim. Consequently, if \(M_n=|\mathcal M(C_n)|\),
\[
\mathcal L(Y_n)=\frac1{M_n+1}\delta_1+\frac{M_n}{M_n+1}\mathcal L(T_n).
\]
For \(n\ge4\), no rim maximal independent set is a singleton; hence the displayed singleton probabilities are exact.

**2. Counting the rim sets.** A maximal independent set of \(C_n\) has cyclic distances \(2\) or \(3\) between successive selected vertices. If there are \(k\) selected vertices, exactly \(n-2k\) of the \(k\) distances are \(3\). Counting cyclic gap lists with a marked selected vertex, then unmarking, gives
\[
a_{n,k}=\frac nk\binom{k}{n-2k},\qquad
M_n(z)=\sum_{k=\lceil n/3\rceil}^{\lfloor n/2\rfloor}a_{n,k}z^k,
\quad M_n=M_n(1).
\]
The counts are integers. The polynomials satisfy \(M_n(z)=z(M_{n-2}(z)+M_{n-3}(z))\), with formal initial values \(M_0(z)=3\), \(M_1(z)=0\), \(M_2(z)=2z\); in particular the total counts are the Perrin numbers. Explicitly,
\[
M_3=3,\ M_4=2,\ M_5=5,\ M_6=5,\ M_7=7,
\quad M_8=10,\ M_9=12,\ M_{10}=17.
\]
Induction using \(M_n=M_{n-2}+M_{n-3}\) gives \(M_n>n\) for every \(n\ge8\): the first three values \(n=8,9,10\) work; if the three-step induction hypothesis holds, \(M_n>(n-2)+(n-3)>n\). Therefore, for every \(n\ge8\),
\[
\Pr(X_n\le1)-\Pr(Y_n\le1)
=\frac1{n+1}-\frac1{M_n+1}>0.
\]
Thus \(Y_n\) cannot be stochastically dominated by \(X_n\) in the direction that would make \(X_n\) the larger variable.

**3. Mean of the sequential rim count.** Conditioning on the first accepted vertex of a path gives the exact recurrence
\[
m\,\mathbb E R_m=m+2\sum_{j=0}^{m-2}\mathbb E R_j \quad(m\ge1).
\]
Its ordinary generating function is
\[
\sum_{m\ge0}(\mathbb ER_m)z^m=\frac{1-e^{-2z}}{2(1-z)^2}.
\]
Coefficient extraction yields, for every \(n\ge3\),
\[
\mathbb E S_n=\frac{1-e^{-2}}2n+\varepsilon_n,
\qquad
\varepsilon_n=\frac12\sum_{j=n-1}^\infty(n-2-j)\frac{(-2)^j}{j!}.
\]
For \(n\ge20\), taking absolute values, the successive positive summands in the error bound have ratios at most \(4/n\). Hence
\[
|\varepsilon_n|\le \frac{2^{n-1}}{2(n-1)!(1-4/n)}<10^{-9}.
\]
The last inequality follows by monotonicity of the displayed bound for \(n\ge20\) and evaluation at \(n=20\). Since the positive Taylor truncation \(\sum_{j=0}^6 2^j/j!>22/3\) implies \((1-e^{-2})/2>19/44\), we get
\[
\boxed{\mathbb E S_n>0.43n \qquad(n\ge20).}
\]

**4. Mean of the static rim count.** Let \(\lambda_1(z),\lambda_2(z),\lambda_3(z)\) be the three roots of \(\lambda^3-z\lambda-z=0\), analytically continued near \(z=1\). The recurrence and its initial values give \(M_n(z)=\sum_{j=1}^3\lambda_j(z)^n\). Let \(\rho=\lambda_1(1)\) be the positive real root of \(\rho^3-\rho-1=0\), with nonreal roots \(\zeta,\overline\zeta\). Elementary rational substitution shows
\[
1.32<\rho<1.33,\qquad |\zeta|^2=1/\rho,
\qquad |\zeta|/\rho=\rho^{-3/2}<2/3.
\]
Differentiating the cubic yields
\[
c(\lambda):=\left.\frac{\lambda'(z)}{\lambda(z)}\right|_{z=1}
=\frac{\lambda^2}{3\lambda^2-1}.
\]
The root bounds imply \(0<c(\rho)<0.413\) and \(|c(\zeta)|\le1/(3-\rho)<0.6\). Since \(\mathbb ET_n=M_n'(1)/M_n(1)\), for \(n\ge20\),
\[
\frac{\mathbb ET_n}{n}
\le\frac{0.413+1.2(2/3)^n}{1-2(2/3)^n}
\le\frac{0.413+1.2(2/3)^{20}}{1-2(2/3)^{20}}
<0.42.
\]
The inequalities are strict, and the spectral trace identity controls the entire error term rather than postulating an asymptotic approximation.

**5. Positive wheel mean gap for all large sizes.** The mixtures in step 1 give
\[
\mathbb EX_n=\frac{1+n\mathbb ES_n}{n+1},\qquad
\mathbb EY_n=\frac{1+M_n\mathbb ET_n}{M_n+1}\le\mathbb ET_n.
\]
For \(n\ge44\), steps 3 and 4 imply
\[
\mathbb EX_n-\mathbb EY_n
>0.43n-0.43-0.42n=0.01n-0.43>0.
\]
For every \(8\le n\le43\), the accompanying checker proves the same strict inequality by **exact rational arithmetic**, evaluating the first-choice path recurrence and the integer cycle-set count formula (not a floating-point asymptotic). In that finite range the smallest gap is \(799/24570>0\), attained at \(n=12\). Thus \(\mathbb EX_n>\mathbb EY_n\) for every \(n\ge8\). A larger mean excludes stochastic dominance of \(Y_n\) over \(X_n\). Combined with the singleton-probability obstruction in step 2, neither first-order stochastic direction can hold.

**6. Small wheels and sharpness.** The exact mixture formulas give equality of the cardinality laws at \(n=3,5,7\). At \(n=4\) the sequential size-one probability is \(1/5\), whereas the static probability is \(1/3\), with all remaining mass at size two. At \(n=6\) the sequential mass vector at sizes \((1,2,3)\) is \((1/7,2/7,4/7)\), while the static vector is \((1/6,1/2,1/3)\). Thus sequential strictly dominates static for \(n=4,6\). Every integer \(n\ge3\) is covered.

## Verification
Run `python verify.py` using Python 3 and its standard library in the extracted package directory. It performs 455 exact assertions, including an independent enumeration of all vertex orders and maximal independent sets for wheels with \(3\le n\le6\) rim vertices, path-law normalization checks, complete rational CDF checks through \(n=43\), exact rational mean comparisons for \(8\le n\le43\), and rational verification of the constants used in the all-size spectral and factorial-tail bounds. The infinite classification comes from the displayed proof, not from the finite enumeration. All dependent computations can be reproduced from the single bundled script without external data.

For an explicit first incomparable case, at \(n=8\), the sequential probabilities at cardinalities \((1,3,4)\) are \((1/9,64/135,56/135)\), and the static probabilities are \((1/11,8/11,2/11)\). The first CDF difference is positive, whereas the difference at cardinality three is negative.

## Relationship to prior work
Higuita-Diaz, López and Roldán-Correa (2026) formulate the sequential/static comparison, prove path and cycle dominance, exhibit earlier non-comparable connected graphs and conjecture sequential domination on graphs of maximum degree at most three. Their wheel-independent counterexamples show that incomparability is possible, not the exact classification of the wheel family. The wheel has one vertex of unbounded degree as \(n\to\infty\), so this result does not refute the bounded-degree conjecture. Perrin-number enumeration of cycle maximal independent sets is classical, including the work of Bisdorff and Marichal (2008). The path greedy-occupancy generating function and its leading density are also classical; neither is claimed as new. Two published mathematical records derive individual cycle greedy-MIS laws and exact uniformity exceptions, and another gives an exact wheel greedy-mixture law and asymptotic variance inflation; these are credited as inputs and do **not** compare the wheel's static and sequential cardinality laws or imply the strict all-order mean inequality without an additional argument. The contribution claimed here is solely the sharp wheel **first-order stochastic-comparability classification**, including its proof for every finite size.

## Limitations
This is a self-review, not an independent audit or a claim of exhaustive priority. Related indexed and unindexed work could contain an equivalent comparison. No structural classification is asserted for arbitrary graphs, multi-hub joins or other parking rules. The finite exact checker confirms only finitely many instances; the rational analytic estimates handle the infinite remainder.

## References
1. R. Higuita-Diaz, L. López and A. Roldán-Correa, *Stochastic Dominance in Discrete Parking Processes on Graphs*, arXiv:2611.14718v1, first public 10 November 2026. https://arxiv.org/html/2611.14718
2. R. Bisdorff and J.-L. Marichal, *Counting non-isomorphic maximal independent sets of the n-cycle graph*, Journal of Integer Sequences 11 (2008). https://cs.uwaterloo.ca/journals/JIS/VOL11/Marichal/marichal.html
3. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, Random Structures & Algorithms 64 (2024), 986–1015. https://doi.org/10.1002/rsa.21200
4. P. L. Krapivsky, *Large deviations in one-dimensional random sequential adsorption*, Physical Review E 102 (2020), 062108. https://doi.org/10.1103/PhysRevE.102.062108
5. *Rare-hub variance inflation in random greedy adsorption on clique-joined cycles*, publicly indexed mathematical result, 8 November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-rare-hub-variance-inflation-in-random-greedy-adsorption-on-cliqu--2dd1f414a75b
6. *Exact uniformity and a local likelihood-ratio obstruction for greedy independent sets on cycles*, publicly indexed mathematical result, 18 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-uniformity-and-a-local-likelihood-ratio-obstruction-for-gr--9a6d94e819c5
