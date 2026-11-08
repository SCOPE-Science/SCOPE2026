# A spectral trust-decay threshold for permanent missing ties despite unanimous opinion limits

## Finding
Consider the synchronous adaptive-confidence Hegselmann–Krause (HK) rule of Li, Luo and Porter. For each integer \(n\ge3\), an explicit family of initial opinion profiles on the connected path with \(2n\) vertices admits a **sharp spectral threshold** at \(\delta=\lambda_n\) for its central tie to be receptive for the first time. Below or at the threshold, the central tie is permanently absent even though **every opinion converges to \(1/2\)**. Above the threshold, the first reception time is exactly
\[
T=\left\lfloor\frac{\log(1/c_0)}{\log(\delta/\lambda_n)}\right\rfloor+1.
\]
Here \(c_0\) is the common initial dyadic confidence, and \(\lambda_n\) is the Perron root of an explicit \((n-1)\)-by-\((n-1)\) nonnegative tridiagonal matrix. It satisfies
\[
\frac{n-2}{n-1}\le\lambda_n<1.
\]
Thus **every** decay parameter \(0\le\delta<1\), however close to one, admits such a permanently absent tie for a sufficiently long connected path. Already the six-vertex path has the sharp threshold \(\lambda_3=1/2\), with initial opinions \((0,1/2,1,0,1/2,1)\) and any \(1/2<c_0<1\).

## Assumptions and scope
Fix \(n\ge3\) and the *original* path graph on vertices \(1,\ldots,2n\), with edges between successive vertices. At integer time \(t\ge0\), an edge \(ij\) is receptive precisely when \(|x_i(t)-x_j(t)|<c_{ij}(t)\). Every vertex synchronously averages its own opinion and the opinions of its receptive graph neighbors, with equal weights. Every edge confidence is simultaneously updated by
\[
c_{ij}(t+1)=\begin{cases}
c_{ij}(t)+\gamma(1-c_{ij}(t)),&\text{if receptive at }t,\\
\delta c_{ij}(t),&\text{otherwise},
\end{cases}
\]
where \(0<\gamma\le1\), \(0\le\delta<1\), and all edges initially have the same \(c_0\in(0,1)\). This is the synchronous adaptive-confidence HK rule, not the asynchronous Deffuant–Weisbuch rule. Opinions lie in \([0,1]\).

Write \(m=n-1\), and define the symmetric tridiagonal \(m\times m\) matrix \(B_n\) by its diagonal entries \(1/6\) in positions \(1,m\) and \(1/3\) at all other positions, with adjacent off-diagonal entries \(1/3\) and all others zero. Let \(\lambda_n=\rho(B_n)\), and take its strictly positive Perron eigenvector \(y=(y_1,\ldots,y_m)\) normalized so that \(\sum_i y_i=1\). Set
\[
u_1=0,\qquad u_{i+1}=u_i+y_i\quad(1\le i\le m),
\]
so \(u_n=1\) and all internal adjacent gaps are positive. Choose
\[
\max_{1\le i<n}y_i<c_0<1,
\]
and initialize the opinions to the *repeated* vector \((u_1,\ldots,u_n,u_1,\ldots,u_n)\). Such \(c_0\) exists because \(m\ge2\), all components of \(y\) are positive, and they sum to one.

## Proof
**1. Exact difference dynamics.** If all edges of an \(n\)-vertex path are receptive, its opinion update is multiplication by the self-inclusive path averaging matrix \(P_n\): each endpoint averages itself and its sole neighbor, and each interior vertex averages itself and its two neighbors. Let \(d_i=u_{i+1}-u_i\) denote consecutive differences. Direct subtraction of adjacent rows of \(P_n\) gives
\[
\begin{aligned}
d_1'&=\tfrac16d_1+\tfrac13d_2,\\
d_i'&=\tfrac13(d_{i-1}+d_i+d_{i+1})\quad(2\le i\le m-1),\\
d_m'&=\tfrac13d_{m-1}+\tfrac16d_m.
\end{aligned}
\]
The interior line is empty for \(n=3\). Therefore \(d'=B_nd\). Since \(d(0)=y\), whenever the two halves evolve independently with all their internal edges receptive,
\[
d_i(t)=\lambda_n^t y_i,\qquad u_n(t)-u_1(t)=\lambda_n^t.
\]

**2. Spectral facts and consensus.** The matrix \(B_n\) is symmetric, nonnegative, irreducible, and has positive diagonal. Perron–Frobenius gives \(y_i>0\) and a unique positive Perron vector up to scaling. Its row sums are one in interior rows and \(1/2\) at the two endpoint rows. Multiplying \(B_n y=\lambda_n y\) by the all-ones row yields
\[
\lambda_n=1-\frac{y_1+y_m}{2\sum_i y_i}<1.
\]
The Rayleigh quotient of the all-ones vector equals \((m-1)/m\), so \(\lambda_n\ge(n-2)/(n-1)>0\). Reflection of coordinates commutes with \(B_n\); Perron uniqueness makes \(y_i=y_{m+1-i}\). Hence \(u_i+u_{n+1-i}=1\). The self-inclusive averaging matrix \(P_n\) also commutes with reflection and preserves constant vectors, so the same pairing identity holds for \(u(t)=P_n^t u\). Since its total span equals \(\lambda_n^t\to0\), every component converges to \(1/2\).

**3. Induction until the first central reception.** At time zero, all internal edges are receptive because \(y_i<c_0\), while the central edge is not because its opinion gap is \(1>c_0\). Suppose that the central edge has been unreceptive at all times before \(t\). The two repeated blocks then evolve identically by \(P_n\). Their internal opinion gaps are \(\lambda_n^t y_i<c_0\) while their confidences have grown to
\[
1-(1-c_0)(1-\gamma)^t\ge c_0.
\]
Thus the induction is internally consistent. The central gap and its confidence at time \(t\) are exactly
\[
\Delta_{n,n+1}(t)=\lambda_n^t,\qquad c_{n,n+1}(t)=c_0\delta^t.
\]
The central edge becomes receptive at the **first** integer \(t\) satisfying \(\lambda_n^t<c_0\delta^t\). For \(\delta\le\lambda_n\), the inequality never holds, including equality of the two decay rates because \(c_0<1\). In that case the preceding identities hold for every \(t\), the central confidence tends to zero, each internal confidence tends to one, and both blocks converge to the same opinion \(1/2\).

For \(\delta>\lambda_n\), division by positive \(\lambda_n^t\) gives \(t>\log(1/c_0)/\log(\delta/\lambda_n)\). The displayed strict-integer formula for \(T\) follows; all prior steps remain governed by the independent-block dynamics. No claim is made about the trajectory after its first central reception.

**4. Uniform availability of permanent ties.** For any fixed \(\delta<1\), choose \(n\) so large that \((n-2)/(n-1)>\delta\). Then \(\lambda_n>\delta\), and the previous construction gives an all-agent consensus at \(1/2\) with the central original graph edge missing from the effective graph at every time. For \(n=3\),
\[
B_3=\begin{pmatrix}1/6&1/3\\1/3&1/6\end{pmatrix},\quad \lambda_3=1/2,\quad y=(1/2,1/2),
\]
which gives the advertised six-agent example.

## Verification
The standalone `verify.py` implements the published update verbatim on a path. It checks the six-agent example using exact rational arithmetic for \(\delta=0,1/5,2/5,1/2\), including 60 consecutive steps per value, and verifies first-reception times for \(\delta=3/5,4/5,9/10\). It independently constructs positive eigenvectors numerically for \(3\le n\le11\), checks the tridiagonal eigenrelation, the spectral lower bound, symmetry, and simulated first-reception behavior on both sides of the threshold. Numerical checks stop before floating-point consensus rounding can imitate a reception event; all infinite-time assertions are proved above.

Execute `python3 verify.py` with Python 3 and its standard library; the expected output begins with `VERIFY_OK`.

## Relationship to prior work
Li, Luo and Porter established convergence and eventual effective-graph stabilization for their adaptive-confidence HK model and reported, principally through simulation, that agents with the same limiting opinion can become permanently unreceptive. In the discussion of their 2024 arXiv revision, they specifically identify the influence of model parameters and initial conditions on these missing ties as further theoretical questions. Their theorems do **not** give this constructed spectral threshold, a precise first-reception clock, or the existence statement for every \(\delta<1\).

The Perron–Frobenius method and analysis of fixed linear averaging matrices are classical; no novelty is attributed to these ingredients in isolation. This theorem combines them with the **particular adaptive trust-update rule and strict receptiveness test** to establish the stated nonlinear-network boundary. The published work on equally spaced fixed-confidence HK agents concerns different interactions and does not imply the adaptive missing-edge construction. A related published result about a nonfreezing proximity graph addresses another model without the present dyadic confidence recursion.

## Limitations
The sharp \(\delta=\lambda_n\) boundary applies to the explicitly specified repeated-Perron-profile family on the \(2n\)-vertex path. It is **not** a universal transition for arbitrary initial opinions, graphs, or update rules. The first-reception formula for \(\delta>\lambda_n\) says nothing about subsequent permanent receptiveness. The exact common-limit equality is established for this symmetric family and is not asserted to hold on an open set of arbitrary opinion profiles. The model is deterministic and synchronous. A conclusive publication-priority determination has not been established.

## References
- Grace J. Li, Jiajie Luo, and Mason A. Porter, *Bounded-Confidence Models of Opinion Dynamics with Adaptive Confidence Bounds*, arXiv:2303.07563, first version 14 March 2023; revision 3 dated 27 July 2024, Sections 2.2, 3.1 and 6.2, https://arxiv.org/html/2303.07563v3 ; journal DOI https://doi.org/10.1137/23M1558951.
- Peter Hegarty and Edvin Wedin, *The Hegselmann-Krause dynamics for equally spaced agents*, arXiv:1406.0819 (2014), https://arxiv.org/abs/1406.0819.
