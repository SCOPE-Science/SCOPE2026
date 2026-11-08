# A three-symbol prime-cylinder counterexample to Markov escape-rate monotonicity

## Finding

A conjecture in Agarwal--Cheriyath--Tikekar, *On Escape rate for subshift with Markov measure* (arXiv:2401.05118, concluding remarks), asserts that for **prime words of equal length** in a shift equipped with a Markov measure, smaller cylinder measure forces smaller escape rate. The conjecture fails already for **two length-two prime words on the three-symbol full shift**, with a strictly positive rational transition matrix. The alphabet size three is minimal for a strict reversal between length-two prime words.

More precisely, for the row-stochastic transition matrix
\[
P=\frac1{10}\begin{pmatrix}8&1&1\\3&3&4\\1&7&2\end{pmatrix},
\qquad
\pi=\left(\frac{14}{27},\frac5{18},\frac{11}{54}\right),
\]
with its stationary Markov measure \(\mu\) on \(\{1,2,3\}^{\mathbb N}\), the two words \(u=21\) and \(v=23\) are both prime, and
\[
\mu(C_{21})=\frac1{12}<\frac19=\mu(C_{23}),
\qquad
\rho(C_{21})>\rho(C_{23}).
\]
Here \(\rho(C)\) is the escape rate into the cylinder hole \(C\), defined below. In fact the corresponding survivor Perron roots satisfy
\[
r(B_{21})=\frac{3+\sqrt{34}}{10}<\frac9{10}<r(B_{23}).
\]

## Assumptions and scope

The underlying symbolic system is the one-sided full shift \(\Sigma=\{1,2,3\}^{\mathbb N}\), with shift map \(\sigma\). A row-stochastic transition matrix \(P\) and stationary row probability \(\pi\) define the stationary Markov probability \(\mu\) by \(\mu([i_0\cdots i_k])=\pi_{i_0}\prod_{j=0}^{k-1}P_{i_j i_{j+1}}\). The length-two cylinder \(C_{ij}\) comprises sequences whose first two coordinates are \(i,j\). A length-two word is *prime* when it has no nonempty proper prefix that is also a suffix, equivalently \(i\ne j\).

For a cylinder hole \(C\), define
\[
\rho(C)=-\lim_{n\to\infty}\frac1n\log\mu\left(\bigcap_{k=0}^{n-1}\sigma^{-k}(\Sigma\setminus C)\right),
\]
provided the limit exists. All entries of \(P\) in the example are strictly positive, so the Markov measure has full symbolic support and is mixing; both punctured matrices appearing below are irreducible and aperiodic. The result disproves the indicated conjecture; it does **not** challenge the spectral-radius formula established in the source paper.

## Proof

**Stationarity and hole measures.** Direct multiplication gives
\[
\pi P=\pi,\qquad \pi_1+\pi_2+\pi_3=1.
\]
The words \(21\) and \(23\) have distinct first and last symbols and hence have no proper self-overlap. Their cylinder measures are
\[
\mu(C_{21})=\pi_2P_{21}=\frac5{18}\frac3{10}=\frac1{12},
\qquad
\mu(C_{23})=\pi_2P_{23}=\frac5{18}\frac4{10}=\frac19.
\]

**Survivor operator and escape rate.** For \(i\ne j\), let \(B_{ij}\) equal \(P\), except that its \((i,j)\) entry is zero. If \({\bf1}\) denotes the all-ones column vector, the Markov property gives the exact finite-time survival identity
\[
\mu\left(\bigcap_{k=0}^{n-1}\sigma^{-k}(\Sigma\setminus C_{ij})\right)=\pi B_{ij}^{\,n}{\bf1}\qquad(n\ge1).
\]
Each of the two matrices below is irreducible and aperiodic, with at least one row sum strictly below one. By Perron--Frobenius, its positive spectral radius \(r(B_{ij})\) lies in \((0,1)\), and positivity of \(\pi\) and \({\bf1}\) implies
\[
\rho(C_{ij})=-\log r(B_{ij}).
\]
This also proves existence of the escape-rate limit without appealing to a formula from the earlier paper.

**Exact reversed spectral ordering.** The two punctured matrices are
\[
B_{21}=\frac1{10}\begin{pmatrix}8&1&1\\0&3&4\\1&7&2\end{pmatrix},
\qquad
B_{23}=\frac1{10}\begin{pmatrix}8&1&1\\3&3&0\\1&7&2\end{pmatrix}.
\]
Their monic characteristic polynomials, computed by determinant expansion, factor or evaluate as
\[
\begin{aligned}
\det(zI-B_{21})&=\frac{(10z-7)(20z^2-12z-5)}{200},\\
\det(zI-B_{23})&=z^3-\frac{13}{10}z^2+\frac{21}{50}z-\frac3{50},\\
\det\!\left(\frac9{10}I-B_{23}\right)&=-\frac3{500},\\
\det(I-B_{23})&=\frac3{50}.
\end{aligned}
\]
The first matrix has eigenvalues \(7/10\) and \((3\pm\sqrt{34})/10\), so its Perron root is \((3+\sqrt{34})/10<9/10\), using \(\sqrt{34}<6\). The characteristic polynomial of the second matrix changes sign on \((9/10,1)\), giving a real eigenvalue strictly inside that interval; its spectral radius is therefore strictly greater than \(9/10\). Applying the decreasing function \(-\log\) yields
\[
\rho(C_{21})=-\log r(B_{21})> -\log r(B_{23})=\rho(C_{23}),
\]
despite the strict reverse ordering of hole measures. This completes the counterexample.

**Sharp alphabet-size observation for length two.** For a stationary Markov chain on a two-symbol alphabet, the only prime length-two words are \(12\) and \(21\). Stationarity forces \(\pi_1P_{12}=\pi_2P_{21}\), hence those cylinders have equal measure. Thus a **strict** measure ordering between prime length-two holes is impossible for any two-symbol stationary Markov chain. The three-symbol example is alphabet-minimal at length two; no claim is made about optimal denominators or longer words.

## Verification

The standalone standard-library program `check.py` checks each row sum, stationarity, both exact cylinder probabilities, the two characteristic polynomials using independent rational matrix determinant arithmetic, and the strict rational test values at \(z=9/10\) and \(z=1\). It also checks finite-time survivor probabilities by two equivalent exact rational recurrences. Run it with `python3 check.py` in the same directory. Exact finite computations are supporting reproducibility checks; the arbitrary-time survival identity and spectral comparison are proved above.

## Relationship to prior work

Agarwal, Cheriyath and Tikekar [1] derive Markov escape rates from punctured transition operators and, in their concluding remarks, conjecture monotonicity of escape rate in the cylinder measure when both words are prime. They exhibit a reversal only after one word ceases to be prime and provide equal-measure examples distinguishing escape rates; neither type refutes their stated strict prime--prime conjecture. The present example contradicts that conjecture with *both* length-two words prime and strictly different measures. The punctured-matrix formula itself is standard and credited.

Bonanno, Cristadoro and Lenci [2] analyze prime-word escape rates in Bernoulli shifts with product measures, where a prime word's escape rate at a fixed length depends only on its cylinder probability. Their conclusion does not apply to this genuinely nonproduct Markov measure (its rows differ). Earlier work by Cheriyath and Agarwal [3] studies holes and position sensitivity for specific expansive Markov systems; no stronger prime--prime comparison theorem in that source was used here. An exact published theorem or indexed counterexample subsuming the specific strict prime--prime reversal would supersede the present originality claim; none was identified in the sources inspected.

## Limitations

The theorem is an explicit counterexample and the accompanying alphabet-minimality statement for **length two**; it does not classify all stochastic matrices, all word lengths, or dynamical realizations other than the symbolic full shift. It assumes the stationary Markov measure and single length-two cylinder holes. Novelty cannot be inferred solely from a failed literature search; equivalent examples or stronger results in unindexed literature remain possible. The algebra and reasoning have been checked in the same review process, but there has been no independent mathematical audit.

## References

[1] N. Agarwal, H. Cheriyath, S. N. Tikekar, *On Escape rate for subshift with Markov measure*, arXiv:2401.05118, first public preprint 2024-01-10; subsequently *Journal of the Australian Mathematical Society* (2026), DOI 10.1017/S144678872610158X. https://arxiv.org/abs/2401.05118

[2] C. Bonanno, G. Cristadoro, M. Lenci, *Maximal escape rate for shifts*, arXiv:2112.14248. https://arxiv.org/abs/2112.14248

[3] H. Cheriyath, N. Agarwal, *Product of expansive Markov maps with hole*, *Discrete and Continuous Dynamical Systems* 39 (2019), 5743--5774, DOI 10.3934/dcds.2019252. https://doi.org/10.3934/dcds.2019252
