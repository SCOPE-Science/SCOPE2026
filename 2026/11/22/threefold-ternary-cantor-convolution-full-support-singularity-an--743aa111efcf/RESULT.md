# Threefold ternary Cantor convolution: full support, singularity, and exact collision dimension

## Finding
Let \(C\subset\mathbb Z_3\) consist of all \(3\)-adic integers with digits in \(\{0,1\}\), and let \(X_1,X_2,X_3\) be independent random elements of \(C\), each with independent equiprobable binary digits. Write \(\mu\) for the law of \(X_1+X_2+X_3\). Then \(\mu\) is nonatomic, singular with respect to normalized Haar measure on \(\mathbb Z_3\), and has **full topological support** \(\mathbb Z_3\). Under \(\mu\), almost every \(3\)-adic integer has digit frequencies
\[
 (f_0,f_1,f_2)=\left(\frac{11}{40},\frac{14}{40},\frac{15}{40}\right),
\]
whereas under Haar measure all three frequencies are \(1/3\).

Define \(A_k=\{\sum_{j=0}^{k-1}\epsilon_j3^j:\epsilon_j\in\{0,1\}\}\) and
\[
R_k(t)=\#\{(a,b,c)\in A_k^3:a+b+c\equiv t\pmod{3^k}\},\qquad
E_k=\sum_{t\bmod 3^k}R_k(t)^2.
\]
The exact collision-energy sequence is
\[
E_0=1,\qquad E_1=22,\qquad E_{k+2}=26E_{k+1}-90E_k\quad(k\ge0).
\]
Consequently the \(L^2\) (correlation) dimension defined through \(3\)-adic residue cylinders is
\[
D_2(\mu)=\lim_{k\to\infty}\frac{-\log\bigl(\sum_{t\bmod3^k}\mu(t+3^k\mathbb Z_3)^2\bigr)}{k\log3}
=\log_3\left(\frac{64}{13+\sqrt{79}}\right)=0.9766281250\ldots<1.
\]
In particular the cylinder-level \(\chi^2\) divergence from Haar grows exponentially with exact rate \(3(13+\sqrt{79})/64>1\).

## Assumptions and scope
All indices \(k\) are integers \(k\ge0\). The \(3\)-adic digits are ordered from least significant to most significant. In \(R_k\), the three summands are **ordered** and each of the \(2^k\) elements of \(A_k\) is counted once. Residues \(t\) range through \(\mathbb Z/3^k\mathbb Z\). For \(k=0\), the ring has one class and \(A_0=\{0\}\). The probability measure \(\mu\) is the additive threefold convolution of the fair binary-digit Cantor measure, not the uniform distribution on its support.

## Proof
**1. Carries and weighted digit matrices.** At digit \(j\), the raw sum of the three independent binary digits is \(s\in\{0,1,2,3\}\) with respective multiplicities \(1,3,3,1\). Starting from carry \(c\in\{0,1\}\), the output digit is \(d\equiv s+c\pmod3\) and the next carry is \(c'=\lfloor(s+c)/3\rfloor\). These are the only possible carries: \(s+c\le4\). Define the integer matrices \(M_d\) with incoming carry indexing rows and outgoing carry indexing columns. Direct enumeration gives
\[
M_0=\begin{pmatrix}1&1\\0&3\end{pmatrix},\qquad
M_1=\begin{pmatrix}3&0\\1&1\end{pmatrix},\qquad
M_2=\begin{pmatrix}3&0\\3&0\end{pmatrix}.
\]
For the least-to-most-significant digit expansion \(t=\sum_{j=0}^{k-1}d_j3^j\), the exact fiber count is
\[
R_k(t)=(1,0)M_{d_0}\cdots M_{d_{k-1}}\binom11.
\]
The initial row prescribes carry zero, and the final all-one column counts either outgoing carry, because congruence modulo \(3^k\) ignores the carry beyond position \(k-1\). This identity is an exact weighted automaton for every \(k\), not an asymptotic approximation.

**2. Full support and non-atomicity.** Every output digit \(d\in\{0,1,2\}\) can be formed with carry zero from a fixed choice of three digits: \(000\), \(100\), or \(110\). Thus any prescribed finite output digit word has a realization with no carry, hence positive cylinder probability. All cylinders meet the support, so \(\operatorname{supp}\mu=\mathbb Z_3\). The original fair Cantor measure gives zero mass to every singleton, since each successive input-digit cylinder has mass \(2^{-k}\). By conditioning on \(X_2+X_3\), \(\Pr(X_1+X_2+X_3=x)=0\) for every \(x\), so \(\mu\) is nonatomic.

**3. Exact energy recurrence.** The tensor-square transfer matrix \(T=\sum_{d=0}^2M_d\otimes M_d\), in carry-pair order \((0,0),(0,1),(1,0),(1,1)\), is
\[
T=\begin{pmatrix}
19&1&1&1\\12&6&0&3\\12&0&6&3\\10&1&1&10
\end{pmatrix}.
\]
By squaring the product expression for \(R_k\) and summing independently over its \(k\) digits,
\[
E_k=(1,0,0,0)T^k(1,1,1,1)^\mathsf T.
\]
With \(w_0=(1,1,1,1)^\mathsf T\), exact multiplication gives
\[
Tw_0=(22,21,21,22)^\mathsf T,\quad
T^2w_0=(482,456,456,482)^\mathsf T,
\]
and the **vector identity** \(T^2w_0=26Tw_0-90w_0\). Multiplying this identity by any \(T^k\) and taking the first coordinate proves the recurrence, including its initial values. Its characteristic roots are \(\lambda_\pm=13\pm\sqrt{79}\), where \(\lambda_+>\lambda_->0\). The coefficient of \(\lambda_+^k\) in \(E_k\) is \((22-\lambda_-)/(\lambda_+-\lambda_-)>0\); hence \(E_k\sim c\lambda_+^k\). Every input triple among the \(8^k\) finite triples has probability \(8^{-k}\), so \(\mu(t+3^k\mathbb Z_3)=R_k(t)/8^k\). Therefore \(\sum_t\mu(t+3^k\mathbb Z_3)^2=E_k/64^k\), which gives the stated dimension. For Haar measure each such cylinder has mass \(3^{-k}\), hence the cylinder \(\chi^2\) divergence is \(3^kE_k/64^k-1\), with the asserted exponential base.

**4. Almost-sure digit frequencies and singularity.** After normalization by eight, the carry transition matrix is
\[
Q=\frac18(M_0+M_1+M_2)=\frac18\begin{pmatrix}7&1\\4&4\end{pmatrix}.
\]
It is irreducible and aperiodic and has stationary distribution \(\pi=(4/5,1/5)\). The stationary probability for output digit \(d\) is \(\pi M_d(1,1)^\mathsf T/8\), yielding exactly \(11/40,14/40,15/40\). The ordinary finite-state Markov-chain ergodic theorem, applied to the joint carry and digit transitions, gives almost-sure convergence of each output digit's empirical frequency to these constants even though the initial carry is zero. Under normalized Haar measure on \(\mathbb Z_3\), digits are iid uniform and the frequencies converge to \((1/3,1/3,1/3)\). The two mutually exclusive full-measure events prove \(\mu\perp\mathrm{Haar}\). Together with the preceding step this is full-support singular continuity.

## Verification
Run `python3 check.py` using the accompanying standalone checker (Python standard library only). It verifies the three carry matrices from binomial multiplicities; the tensor-square matrix and the **exact, infinite-depth vector identity**; rational stationary probabilities; transfer-energy recurrence through depth nine; every output fiber and full support through depth eight; and independent three-summand direct enumeration through depth four. The executed checker printed `VERIFY_OK 9993 finite and exact checks`. The all-depth mathematical conclusions rest on the exact vector identity and the ergodic theorem, not on finite enumeration.

## Relationship to prior work
Abram and Lagarias, *p-adic path set fractals and arithmetic* (first publicly submitted October 9, 2012), Theorem 1.3 and section 4.2, construct finite automata for **Minkowski sumsets** of \(p\)-adic path sets. Their unweighted support theorem and carry construction motivate the question but do not imply the particular weighted threefold convolution's stationary digit law, exact energy recurrence or correlation dimension. Their paper discusses dimensions of sets, which must not be substituted for dimensions of the convolution measure. Abram and Lagarias's work on multiplicative intersections concerns a different operation. Nazarov–Peres–Shmerkin investigate real Cantor convolutions at incommensurable contraction scales, which is not this equal-scale \(3\)-adic problem. Prior unpublished or differently phrased weighted-carry calculations might contain an equivalent formula, so historical priority is not independently certified.

## Limitations
The theorem is specific to three fair \(\{0,1\}\)-digit summands over \(\mathbb Z_3\); no classification for all convolution orders, biases, primes, or shifted/multiplied factors is claimed. It establishes the correlation dimension, not an independent formula for entropy/Hausdorff dimension of \(\mu\). The analytic singularity proof is self-contained apart from the standard finite-state ergodic theorem and Haar digit law. The literature comparison is bounded and is not a proof that no earlier equivalent exists; independent audit has not been performed.

## References
1. W. Abram and J. C. Lagarias, *p-adic path set fractals and arithmetic*, arXiv:1210.2478 (first submitted 2012-10-09), Theorem 1.3 and §4.2. https://arxiv.org/html/1210.2478v4
2. W. Abram and J. C. Lagarias, *Intersections of multiplicative translates of 3-adic Cantor sets*, arXiv:1308.3133 (first submitted 2013); J. Fractal Geom. 1 (2014), 349–390. https://arxiv.org/abs/1308.3133
3. F. Nazarov, Y. Peres and P. Shmerkin, *Convolutions of Cantor measures without resonance*, arXiv:0905.3850 (first submitted 2009). https://arxiv.org/abs/0905.3850
