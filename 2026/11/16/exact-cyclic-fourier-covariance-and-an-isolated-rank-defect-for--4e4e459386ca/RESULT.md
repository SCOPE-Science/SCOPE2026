# Exact cyclic Fourier covariance and an isolated rank defect for binary two-run codes

## Finding

A uniformly sampled labeled binary circle of length \(n\ge3\), with neither cyclic triple \(000\) nor \(111\), has an explicit Fibonacci–Lucas Fourier covariance spectrum. Its spin-coordinate covariance is singular **only** at length \(n=4\); the ranks for lengths \(3,4\), and every \(n\ge5\) are respectively \(3,3,n\). For \(n\to\infty\), all its Fourier eigenvalues converge uniformly to a rational frequency profile with a unique least-variance frequency \(0\), two maximizers at \(\pm\arccos(-\sqrt5/4)\), and sharp limiting squared condition ratio

\[
\boxed{\lim_{n\to\infty}\kappa_n=8+\frac{8\sqrt5}{3}.}
\]

This is a finite-circle result: a periodic block is sampled as one complete cyclic object, not as an independently concatenated linear codeword stream.

## Assumptions and scope

Let \(\mathcal W_n\) be all labeled words \(x=(x_0,\dots,x_{n-1})\in\{0,1\}^n\) satisfying \((x_i,x_{i+1},x_{i+2})\notin\{(0,0,0),(1,1,1)\}\) for every \(i\) modulo \(n\). Rotations are **not** identified. Pick \(x\) uniformly from \(\mathcal W_n\), and set \(s_i=2x_i-1\). Bit complementation implies \(\mathbb E s_i=0\). Define the positive semidefinite \(n\times n\) covariance \(K_n=(\mathbb E s_i s_j)\). The binary-coordinate covariance is exactly \(K_n/4\).

Set \(F_{-1}=1\), \(F_0=0\), \(F_1=1\), \(F_{m+1}=F_m+F_{m-1}\), and \(L_m=F_{m-1}+F_{m+1}\). For each integer \(m\ge0\) define

\[
H_0(m)=L_m,\qquad H_1(m)=-F_{m+1},\qquad H_2(m)=-F_{m-1}.
\]

The number of words is \(Z_n=L_n+2\cos(2\pi n/3)\), always positive. For each \(0\le d<n\), define

\[
C_n(d)=\frac{H_{d\bmod3}(n-d)+H_{(n-d)\bmod3}(d)}{Z_n},\quad
\lambda_{n,k}=\sum_{d=0}^{n-1}C_n(d)\cos(2\pi kd/n),\quad 0\le k<n.
\]

**Exact finite spectrum:** the complete eigenvalue multiset of \(K_n\) is \(\{\lambda_{n,k}:0\le k<n\}\), with multiplicity of repeated numerical values inherited from the displayed Fourier indices. The \(n=3\) spectrum is \(\{1/3,4/3,4/3\}\); the \(n=4\) spectrum is \(\{0,4/3,4/3,4/3\}\). For all \(n\ge5\), every \(\lambda_{n,k}>0\).

Writing \(\varphi=(1+\sqrt5)/2\), the limiting symbol is

\[
\mathcal S(\theta)=\frac{2/\sqrt5}{1+\sqrt5\cos\theta+2\cos^2\theta},\qquad
\sup_{0\le k<n}\left|\lambda_{n,k}-\mathcal S(2\pi k/n)\right|=O(n\varphi^{-n}).
\]

Consequently \(\lim\lambda_{\min}(K_n)=(3\sqrt5-5)/10\) and \(\lim\lambda_{\max}(K_n)=16\sqrt5/15\), proving the stated ratio. The finite-length extremizing Fourier index is **not** claimed to equal a fixed closed-form index for all \(n\).

## Proof

**(1) Complete-word trace.** Let states represent two consecutive bits in order \(00,01,10,11\), and use the allowed-pair transition matrix

\[
B=\begin{pmatrix}0&1&0&0\\0&0&1&1\\1&1&0&0\\0&0&1&0\end{pmatrix},\qquad T=\mathrm{diag}(-1,-1,1,1).
\]

Each closed walk of \(n\) pair transitions corresponds bijectively to one labeled \(n\)-cycle word, including periodic words. Thus \(Z_n=\mathrm{tr}(B^n)\), and \(\mathbb E(s_0s_d)=Z_n^{-1}\mathrm{tr}(TB^dTB^{n-d})\). Under the bit-complement involution, the even and odd two-dimensional state spaces are invariant under \(B\). On suitable normalized bases the restrictions are

\[
E=\begin{pmatrix}0&1\\1&1\end{pmatrix},\qquad
O=\begin{pmatrix}0&1\\-1&-1\end{pmatrix},\qquad O^3=I.
\]

The spin operator \(T\) interchanges the two spaces (up to an irrelevant common sign). Consequently

\[
\mathrm{tr}(B^n)=\mathrm{tr}(E^n)+\mathrm{tr}(O^n)=L_n+2\cos(2\pi n/3),
\]

\[
\mathrm{tr}(TB^dTB^{n-d})=\mathrm{tr}(O^dE^{n-d})+\mathrm{tr}(E^dO^{n-d}).
\]

The standard matrix powers of \(E\) have Fibonacci entries and give \(\mathrm{tr}(O^rE^m)=H_{r\bmod3}(m)\). This proves the finite correlation and Fourier formulas with all boundary cases, including \(d=0\) and \(m=0\).

**(2) Rank rigidity.** For any random vector, a coefficient vector \(a\) belongs to \(\ker K_n\) precisely when \(\sum_i a_is_i\) is constant over all admissible words. At \(n=3\) the displayed three positive eigenvalues give full rank; at \(n=4\), every allowed word contains two zeros and two ones, so the constant Fourier mode is null, while the other three eigenvalues are positive. For every \(n\ge5\), choose admissible words differing only at site \(0\): fix \(x_{n-1}=0,x_1=1,x_2=0,x_{n-2}=1\). Choose the interior path from \(x_2\) to \(x_{n-2}\) to alternate if its number of vertices is even, and to start with two zeros before alternating if its number of vertices is odd. The resulting path has no triple run, and both assignments \(x_0=0,1\) preserve admissibility. Rotation gives such a pair differing at every individual coordinate. Hence every vector with constant dot product on the entire code must have every coefficient zero, proving \(K_n\) positive definite.

**(3) Exponential uniform symbol.** The Perron eigenvalue of \(E\) is \(\varphi\), its other eigenvalue is \(-1/\varphi\), and \(O^3=I\). For fixed displacement \(d\), the infinite-volume two-point sequence is

\[
c_d=\frac{v^{\mathsf T}O^dv}{\varphi^d v^{\mathsf T}v},\qquad v=(1,\varphi)^{\mathsf T},\qquad c_{-d}=c_d.
\]

It satisfies \(c_0=1\), \(c_1=-1/\sqrt5\), and the recurrence \(c_{d+2}+\varphi^{-1}c_{d+1}+\varphi^{-2}c_d=0\) for \(d\ge0\). The two-sided Fourier sum \(\sum_{d\in\mathbb Z}c_de^{-id\theta}\) simplifies, by summing this geometric recurrence, to \(\mathcal S(\theta)\) above. The exact trace representation shows, uniformly for \(0\le d<n\),

\[
C_n(d)=c_d+c_{n-d}+O(\varphi^{-n}),
\]

where the error follows from the bounded powers of \(O\), the subdominant eigenvalue of \(E\), and \(Z_n=\varphi^n+O(1)\). Replacing the truncated sums by the two-sided sum at the mesh points \(\theta=2\pi k/n\) incurs another \(O(\varphi^{-n})\) term. Summing the uniform errors gives \(O(n\varphi^{-n})\) uniformly in \(k\).

**(4) Sharp extrema.** On \(u=\cos\theta\in[-1,1]\), the denominator \(Q(u)=2u^2+\sqrt5u+1\) has its unique minimum \(3/8\) at \(u=-\sqrt5/4\), and its unique maximum \(3+\sqrt5\) at \(u=1\). This gives \(\max\mathcal S=16\sqrt5/15\) at precisely the conjugate nonalternating frequencies and \(\min\mathcal S=(3\sqrt5-5)/10\) at frequency zero. Uniform convergence together with density of the frequency mesh proves the extrema and the ratio. No finite test is used as an infinite proof.

## Verification

Run `python3 check.py` using only the Python standard library. It exhaustively enumerates the eligible circles for \(3\le n\le17\), checks word counts and every rational lag covariance against the closed formula, checks finite Fourier positivity/rank, and compares selected longer spectra to the limiting symbol. The packaged checker executes 185 assertions. The exact trace derivation and rank-witness construction, rather than enumeration, establish all lengths.

## Relationship to prior work

Classical constrained-code spectral analyses by Gallopoulos, Heegard and Siegel, and by Centers and collaborators, give general transition-matrix methods for stationary or cyclostationary **streams**. Those methods conceptually subsume the limiting stationary spectral calculation, which is not claimed as independently novel. The 2020 article's finite-length model concatenates codewords with bridging patterns; it is not the uniform single-periodic-word distribution here.

The published four-gram-profile census for the same simultaneous triple prohibition counts **distinct read histograms** via Eulerian circulations; its full result does not evaluate positionwise covariance or the isolated fourth-order Fourier kernel. Classical majority-rule enumeration likewise addresses word counts. The present finite circular correlation formula, its all-length rank classification, and the sharp nonalternating covariance-conditioning limit are the contribution assessed here.

## Limitations

Only the uniform labeled binary ensemble with both cyclic constant triples prohibited is treated; linear words, nonuniform fugacity, longer run bounds, joint multiple-coordinate observations, and the finite-index exact location of spectral extrema are outside the claim. The stationary limiting rational symbol is derivable from pre-existing transfer-matrix PSD theory; its novelty is not asserted on its own. Historical priority of the **particular finite-ring spectral specialization** is provisional. The finite checks do not constitute an exhaustive search of mathematical literature, and independent validation has not been performed.

## References

1. Centers, Tan, Hareedy and Calderbank, *Power Spectra of Constrained Codes with Level-Based Signaling: Overcoming Finite-Length Challenges*, arXiv:2010.04878v1, first public 10 October 2020. https://arxiv.org/abs/2010.04878
2. Gallopoulos, Heegard and Siegel, *The Power Spectrum of Run-Length-Limited Codes*, IEEE Transactions on Communications (1989).
3. Nguyen, Cai, Immink and Kiah, *Capacity-Approaching Constrained Codes with Error Correction for DNA-Based Data Storage*, arXiv:2001.02839v1, first public 9 January 2020. https://arxiv.org/abs/2001.02839
4. *Exact four-gram profile capacity of binary circular words with runs of length at most two* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-four-gram-profile-capacity-of-binary-circular-words-with-r--ffb8b64cf1bb/RESULT.md
5. Agur, Fraenkel and Klein, *The Number of Fixed Points of the Majority Rule*, Discrete Mathematics 70 (1988), 295–302.
