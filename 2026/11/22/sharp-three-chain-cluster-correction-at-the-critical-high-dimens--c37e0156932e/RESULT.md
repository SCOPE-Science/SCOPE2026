# Sharp three-chain cluster correction at the critical high-dimensional order threshold

## Finding
For the number \(W_{n,d}\) of three-element chains among \(n\) independent uniform \(d\)-dimensional cube points, we establish an exact finite-dimensional second factorial cumulant, a Poisson approximation at the critical dimension, and a sharp positive leading overlap correction. Write
\[
M=\binom n3,\qquad p=6^{1-d},\qquad \lambda_{n,d}=Mp,
\]
\[
q_1=8\cdot20^{-d}+4\cdot30^{-d}+16\cdot40^{-d}+8\cdot120^{-d},\quad
q_2=6\cdot12^{-d}+12\cdot24^{-d},
\]
\[
N_1=3M\binom{n-3}{2},\qquad N_2=3M(n-3).
\]
Set \(N_1=0\) when \(n=3,4\). For every \(n\ge3\), integer \(d\ge1\),
\[
\boxed{\mathbb E[(W_{n,d})_2]-\lambda_{n,d}^2 =N_1(q_1-p^2)+N_2(q_2-p^2)-Mp^2.}
\]
If \(d=d_n\) is integer-valued and \(\lambda_{n,d_n}\to\lambda\in(0,\infty)\), let \(\delta=3\log20/\log6-5\), which is strictly positive because \(20^3>6^5\). Then
\[
\boxed{d_{\mathrm{TV}}(\mathcal L(W_{n,d_n}),\operatorname{Poisson}(\lambda_{n,d_n}))=O(n^{-\delta}),}
\]
and, more sharply for the factorial cumulant,
\[
\boxed{\mathbb E[(W_{n,d_n})_2]-\lambda_{n,d_n}^2\sim2n^5 20^{-d_n}.}
\]
In particular \(\Pr(W_{n,d_n}\ge1)\to1-e^{-\lambda}\). The slow polynomial exponent is approximately \(0.0158500\); this quantifies residual dependence caused by triples sharing one extreme point.

## Assumptions and scope
The coordinates of \(X_1,\dots,X_n\) are independent continuous uniform random variables on \([0,1]\), across points and coordinates. A triple forms a chain if its three points can be permuted to satisfy coordinatewise increasing inequalities; ties have probability zero. The integer-dimensional critical condition is formulated via the exact mean \(\lambda_{n,d_n}\) and permits subsequences because \(d_n\) lies in the integers. We do not assert convergence for all integer choices at an unadjusted real-valued critical center.

## Proof
**Single triples.** On the first coordinate any specified ordering of three distinct points occurs with probability \(1/6\). In each subsequent coordinate it is preserved with probability \(1/6\), independently, so \(\Pr(\text{specified triple is a chain})=6^{1-d}=p\).

**Two triples sharing exactly one point.** For each triple prescribe an orientation (six choices each). If the common point has ranks \(i,j\in\{1,2,3\}\) in the two chains, the number of total orders on the union of five labels consistent with both orientations is
\[
L_{ij}=\binom{i+j-2}{i-1}\binom{6-i-j}{3-i}.
\]
Indeed the elements below the shared point can be interleaved in the first factor's number of ways, and the elements above it in the second factor's number of ways. For any fixed \(i,j\), four choices order the two private labels of each triple. The matrix of \(L_{ij}\) is
\[
\begin{pmatrix}6&3&1\\3&4&3\\1&3&6\end{pmatrix}.
\]
Each consistent orientation pair has per-coordinate probability \(L_{ij}/5!\); its probability across \(d\) coordinates is \((L_{ij}/120)^d\). Distinct pairs of orientation prescriptions give disjoint chain outcomes. Summing gives the exact overlap-one probability \(q_1\) above. Its leading term is \(8\cdot20^{-d}\), the eight shared-minimum or shared-maximum orientation pairs.

**Two triples sharing exactly two points.** Consider their union of four distinct labels. Among the 36 oriented-chain pairs, 18 disagree on the shared pair and are impossible; 12 yield exactly one compatible total order and six yield exactly two. Each total order has probability \(1/24\) per coordinate; thus the exact joint probability is \(q_2=12\cdot24^{-d}+6\cdot12^{-d}\). This count also follows by placing the private vertex of each chain into the three slots determined by the common ordered pair. Disjoint triples have independent chain indicators.

**Second factorial cumulant.** There are \(M=\binom n3\) triple indicators. The numbers of ordered pairs of distinct triples sharing exactly one or two labels are \(N_1\) and \(N_2\); all other distinct pairs are disjoint and independent. Since \(\lambda=Mp\), subtracting \(\lambda^2\) from the second factorial moment gives the displayed exact formula, including the necessary missing diagonal contribution \(-Mp^2\).

**Poisson approximation.** Apply the standard local-dependency Arratia–Goldstein–Gordon bound to the triple indicators, with each triple's neighborhood consisting of intersecting triples. Disjoint triples depend on disjoint input points; therefore the conditional-error term is zero. The two neighborhood sums satisfy
\[
b_1=O(n^5 6^{-2d}),\quad
b_2=O(n^5 20^{-d}+n^4 12^{-d}).
\]
Consequently (for ordinary total variation, half the variation norm used in the original theorem)
\[
d_{\mathrm{TV}}(\mathcal L(W_{n,d}),\operatorname{Poisson}(\lambda))
\le b_1+b_2.
\]
In the critical regime \(\lambda_{n,d_n}\to\lambda\in(0,\infty)\), \(d_n=3\log n/\log6+O(1)\). Thus \(n^5 20^{-d_n}=\Theta(n^{-\delta})\), while \(n^4 12^{-d_n}=o(n^5 20^{-d_n})\) and \(n^5 6^{-2d_n}=o(n^5 20^{-d_n})\). This proves the claimed total-variation estimate and the limit for existence of a chain.

**Sharp second-factorial correction.** In the exact cumulant identity,
\[
q_1=8\cdot20^{-d}(1+o(1)),\qquad N_1\sim n^5/4,
\]
so \(N_1q_1\sim2n^5 20^{-d}\). Every other term is smaller: \(N_2q_2=O(n^4 12^{-d})\), \((N_1+N_2+M)p^2=O(n^5 6^{-2d})\), and the next one-overlap contribution is \(O(n^5 30^{-d})\). Thus the constant \(2\) and scale \(n^5 20^{-d}\) follow by strict asymptotic comparison. This is an asymptotic for the factorial cumulant, *not* a matching lower bound for total variation.

## Verification
The standalone script `checker.py` verifies the exact overlap formulas and all finite first and second factorial moments against a full enumeration of independent coordinate permutations for \((n,d)=(3,1),(4,1),(5,1),(3,2),(4,2),(5,2),(4,3)\). It also checks the inequalities defining the critical exponents and prints exact-formula ratios at increasing finite sizes. The enumeration is a finite cross-check, not a proof for unbounded \(n,d\); the combinatorial and analytic arguments above establish those claims.

## Relationship to prior work
Bollobás and Brightwell (1995) established the critical scale for existence of fixed-length chains in growing-dimensional random orders, including three-element chains. Their published abstract describes one-sided threshold behavior, not this particular factorial-cumulant formula; the complete article could not be inspected, so implicit coverage remains a substantive priority risk. Bhattacharjee, Ilienko, Jin and Molchanov (2026), especially the introduction and Theorems 2.6 and 10.2/Corollary 10.3, analyze non-Pareto point counts and their Gaussian/stable/Poisson limits, corresponding to the two-point comparability threshold, not three-chain counts. Arratia, Goldstein and Gordon (1989) provide the general Poisson approximation theorem applied here; that theorem itself is not claimed as new. The finite overlap enumeration, exact second factorial cumulant, and sharp slow critical correction are the subject of this result.

## Limitations
The claim treats exactly three-point chains and product-independent continuous coordinates. It does not establish a sharp total-variation leading constant, nor a universal distributional correction beyond the exact second factorial cumulant. The Bollobás–Brightwell 1995 full text was not accessible at the time of comparison; its possible prior treatment of the full three-chain critical law remains unresolved, and earlier combinatorial overlap identities may exist. No independent validation has been performed.

## References
1. C. Bhattacharjee, A. Ilienko, B. Jin, I. Molchanov, *From Gaussian to stable and back: Non-Pareto points in growing dimension*, arXiv:2611.01096v1 (publicly submitted 2026-10-31), https://arxiv.org/abs/2611.01096.
2. B. Bollobás and G. Brightwell, *Random high-dimensional orders*, Advances in Applied Probability 27 (1995), 161–184, https://doi.org/10.2307/1428102.
3. R. Arratia, L. Goldstein, L. Gordon, *Two moments suffice for Poisson approximations: The Chen–Stein method*, Annals of Probability 17 (1989), 9–25, https://doi.org/10.1214/aop/1176991491.
