# Parity reversal of equal-width escape gates in postcritical zigzag maps

## Finding
For each integer \(m\ge2\), take the postcritical member \(Z_{\lambda_m}(x)=\operatorname{dist}(\lambda_m x,2\mathbb Z)\) of the zigzag family on \([0,1]\), and open any one of its \(m\) complete monotone laps as a hole. All these holes have the same Lebesgue length, but their finite-time survival probabilities exhibit an exact, all-time parity reversal. For even \(m\), the leftmost hole has strictly *smaller* survivor mass than each other full-lap hole at every horizon \(n\ge2\); for odd \(m\), it has strictly *larger* survivor mass. The other \(m-1\) holes are equi-surviving at every horizon. The complete escape rates, survivor entropies and Hausdorff dimensions are explicit as detailed below. These are statements about this concrete postcritical family; the general Markov-hole escape formalism is known.

## Assumptions and scope
Let \(m\ge2\) be any integer. Define the real slope \(\lambda_m\in(m,m+1)\) by
\[
\lambda_m=\begin{cases}
\frac{m+\sqrt{m^2+4}}2,&m\text{ even},\\
\frac{m+1+\sqrt{(m+1)^2-4}}2,&m\text{ odd}.
\end{cases}
\]
Thus \(Z_{\lambda_m}(1)=1/\lambda_m\). Let \(H_j=(j/\lambda_m,(j+1)/\lambda_m)\) for \(0\le j<m\), where the hole is **open**. For each integer \(n\ge1\), let
\[
S_j(n)=\operatorname{Leb}\{x\in[0,1]:Z_{\lambda_m}^t(x)\notin H_j\text{ for }0\le t<n\}.
\]
The full survivor is \(K_j=\{x:Z_{\lambda_m}^t(x)\notin H_j\text{ for every }t\ge0\}\), a compact invariant set. Set \(\rho_j\) by
\[
\rho_j=\begin{cases}
m-1,&m\text{ even},\ j=0,\\
\frac{m-1+\sqrt{(m-1)^2+4}}2,&m\text{ even},\ 1\le j<m,\\
m,&m\text{ odd},\ j=0,\\
\frac{m+\sqrt{m^2-4}}2,&m\text{ odd},\ 1\le j<m.
\end{cases}
\]
Here \(\rho_j\ge1\) and \(\rho_j<\lambda_m\).

**Theorem.** For all \(n\ge1\), the values \(S_j(n)\) are equal for \(1\le j<m\), and \(S_j(1)=1-1/\lambda_m\) for every \(j\). For every \(n\ge2\),
\[
\begin{cases}S_0(n)<S_j(n)&m\text{ even},\\ S_0(n)>S_j(n)&m\text{ odd},\end{cases}\qquad1\le j<m.
\]
There are positive constants depending on \(m,j\) such that \(S_j(n)=\Theta((\rho_j/\lambda_m)^n)\) as \(n\to\infty\), and
\[
-\lim_{n\to\infty}\frac1n\log S_j(n)=\log\frac{\lambda_m}{\rho_j},\qquad
h_{\rm top}(Z_{\lambda_m}|_{K_j})=\log\rho_j,\qquad
\dim_H K_j=\frac{\log\rho_j}{\log\lambda_m}.
\]
In particular the entire survival law of the leftmost hole is geometric:
\[
S_0(n)=\left(1-\frac1{\lambda_m}\right)\begin{cases}
((m-1)/\lambda_m)^{n-1},&m\text{ even},\\
(m/\lambda_m)^{n-1},&m\text{ odd}.
\end{cases}
\]

## Proof
**Postcritical Markov partition.** Put \(\lambda=\lambda_m\). Besides the full laps \(I_i=[i/\lambda,(i+1)/\lambda]\), \(0\le i<m\), there is the terminal partial lap \(I_m=[m/\lambda,1]\). Its length is \((\lambda-m)/\lambda>0\). Every full lap maps affinely onto \([0,1]\), with derivative absolute value \(\lambda\). By the defining quadratic equation, when \(m\) is even, the terminal lap maps onto \([0,1/\lambda]=I_0\); when \(m\) is odd, it maps onto \([1/\lambda,1]=I_1\cup\cdots\cup I_m\). This proves that the partition is exactly Markov. The branch endpoints form a finite forward-invariant set.

**Finite-time transfer identity.** Remove the forbidden full lap \(I_j\) (Lebesgue-distinct from the open hole only at endpoints), and label the \(m\) remaining intervals by \(B_j=\{0,\dots,m\}\setminus\{j\}\). Define an \(m\times m\) \(0\)-\(1\) matrix \(A_j\) with \((A_j)_{ik}=1\) if the image of \(I_i\) contains \(I_k\), and 0 otherwise. Let \(\ell_j\) be the positive vector of lengths of the allowed intervals. Every legal itinerary of length \(n\) ends in a specified allowed interval and is mapped affinely to it under \(n-1\) iterates, with inverse length factor \(\lambda^{-(n-1)}\). Different itinerary interiors are disjoint. Thus, including the case \(n=1\),
\[
S_j(n)=\lambda^{-(n-1)}\mathbf1^{\mathsf T}A_j^{n-1}\ell_j.
\]
Endpoints form a null set and do not change the identity.

**Strict parity ordering.** Each allowed full-lap row of \(A_j\) consists entirely of ones. The terminal row has only a single 1 directed to full lap 0 for even \(m\), and ones to every state except full lap 0 for odd \(m\). After identifying the common terminal state and matching all allowed full states, the matrices for \(j\ge1\) coincide, as do their length vectors. For even \(m\), the matrix of hole 0 has the terminal row identically zero, while the other matrix has one additional terminal-to-full edge. For odd \(m\), the matrix of hole 0 has an all-ones terminal row, while the other matrix lacks exactly its terminal-to-full-0 edge. In both cases the common full rows ensure strictly positive survivor contributions from the extra edge after every \(n\ge2\), and all other contributions are nonnegative. This proves the claimed strict inequality and the equi-survival of the non-leftmost holes. Because the matrix for hole 0 has constant column sum \(m-1\) (even) or \(m\) (odd), multiplying the transfer identity proves its exact geometric law.

**Perron roots and exponential rates.** With hole 0 removed, the surviving spectral radius is \(m-1\) for even \(m\), and \(m\) for odd \(m\). If \(j\ge1\), write \(f=m-1\) for the number of surviving full laps and collect their common right-eigenvector coordinate \(u\), with terminal coordinate \(v\). In either parity the top block of eigenvalue equations is \(ru=fu+v\). For even \(m\), the terminal equation is \(rv=u\); hence \(r^2-fr-1=0\). For odd \(m\), it is \(rv=(f-1)u+v\); hence \(r^2-(f+1)r+1=0\). The specified positive roots give exactly the formula for \(\rho_j\). The submatrix on the accessible recurrent component is primitive unless \(\rho_0=1\), the trivial one-cycle case. Positivity of \(\ell_j\) and a positive top-row contribution give \(S_j(n)=\Theta((\rho_j/\lambda)^n)\), including \(\rho_0=1\). Since forbidding a nonempty whole full lap reduces the spectral radius of the original primitive Markov matrix, \(\rho_j<\lambda\); equivalently this follows directly from the explicit quadratic inequalities.

**Entropy and dimension.** Legal infinite itineraries form the finite-type symbolic survivor with adjacency matrix \(A_j\). Its exponential word-growth rate is \(\rho_j\). Since each valid length-\(n\) cylinder is an interval with diameter at most \(\lambda^{-(n-1)}\), the upper dimension bound follows from a cylinder cover. For the opposite bound when \(\rho_j>1\), use the Perron eigenvector Markov measure on its irreducible recurrent component: cylinder probabilities are bounded by constants times \(\rho_j^{-n}\), while diameters are comparable to \(\lambda^{-n}\). A uniform bounded-overlap estimate for equal-length one-dimensional Markov cylinders yields the Frostman lower bound \(\log\rho_j/\log\lambda\). For \(\rho_j=1\) the upper bound already forces dimension zero. The endpoints of Markov intervals and their preimages form a countable exceptional collection, with eventually periodic boundary itineraries; they add zero dimension and no positive orbit-complexity growth. Thus topological entropy of the compact survivor is the subshift entropy, \(\log\rho_j\), and its Hausdorff dimension is as claimed.

## Verification
Run the self-contained `check.py` with Python 3, NumPy. It independently computes \(A_j\) and its eigenvalues for \(2\le m\le8\), tests every hole and each finite horizon \(2\le n\le7\), and checks the transfer-matrix survival formula by direct geometric construction of interval preimages for \(2\le m\le5\) and \(1\le n\le4\). The observed output ends with `VERIFY_OK cases=56 escape_spectra=all_m_2_to_8 finite_order=all_n_2_to_7`. These finite checks corroborate but do not replace the all-integer proof.

## Relationship to prior work
Kumar's 2026 construction introduces the same zigzag maps and proves their exactness and entropy \(\log\lambda\); it does not treat open equal-lap holes. Haritha and Agarwal (2018) establish general finite-type/transition-matrix methods for open Markov systems, including examples where equal-area holes have different escape rates. Bandtlow and Rugh (2015/2018) establish general continuity of survivor entropy under moving holes. Those methodological and qualitative insights are prior work. The statement here is the explicit all-horizon parity reversal and complete escape/entropy/dimension classification at the postcritical metallic slopes \(\lambda_m\); it is not a claim to a new general transfer theorem. Literature comparison did not identify an identical family-level classification, but historical priority is not independently certified.

## Limitations
The holes must be entire open full laps and the slope must be exactly \(\lambda_m\). A different slope or an arbitrary translated hole need not have this Markov graph. The result is a deterministic one-dimensional statement, not a theorem for stochastic holes, noisy trajectories, arbitrary distributions, or unrelated interval families. There is no independent scientific validation or exhaustive proof of historical novelty.

## References
1. Vinod Kumar P B, *The entropy spectra of chaotic maps of an interval*, first public arXiv posting 2026-10-29, https://arxiv.org/abs/2610.39443 (Proposition 5.1).
2. C. Haritha and N. Agarwal, *Product of Expansive Markov Maps with Hole*, arXiv:1806.07192 (finite-type transition matrices and escape-rate examples).
3. O. F. Bandtlow and H. H. Rugh, *Entropy-continuity for interval maps with holes*, arXiv:1510.06043; Ergodic Theory and Dynamical Systems 38 (2018), 2036–2061.
