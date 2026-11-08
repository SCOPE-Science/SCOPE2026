# Quantized-phase cyclic Gabor bases: an exact parity-code spectral law

## Finding
Fix integers \(p,q\ge2\), write \(N=2p\), and choose a window on \(\mathbb Z_N\) with entries
\[
 g(j)=N^{-1/2}\exp(2\pi i x_j/q),\qquad x_j\in\mathbb Z_q.
\]
Form the square synthesis matrix \(G\) whose \(2p\) columns are \(M_{2\ell}T_k g\), \(0\le\ell<p\), \(k=0,1\), with \((T_kg)(j)=g(j-k)\) and \((M_sg)(j)=\exp(2\pi i sj/N)g(j)\), indices cyclic. Put \(A=\lambda_{\min}(GG^*)\) and \(B=\lambda_{\max}(GG^*)\), allowing \(A=0\) when the system is not a basis.

Write \(c_r=x_r-x_{r+p}\pmod q\) for \(0\le r<p\), and define
\[
 k_0=c_0+c_{p-1}\pmod q,\qquad
 k_r=c_r-c_{r-1}\pmod q\quad(1\le r<p).
\]
Then the entire frame-operator spectrum consists of the \(p\) pairs
\[
 \boxed{1\pm|\cos(\pi k_r/q)|},\qquad 0\le r<p,
\]
so \(A=1-\max_r|\cos(\pi k_r/q)|\) and \(B=2-A\).

For independent uniform \(x_j\in\mathbb Z_q\), the exact distribution of \(A\) for every real \(t\) is as follows. Set
\[
 K_t=\{k\in\{0,\ldots,q-1\}:1-|\cos(\pi k/q)|>t\},\quad
 h_t=|K_t|,\quad d_t=\sum_{k\in K_t}(-1)^k.
\]
Then
\[
 \boxed{\mathbb P(A>t)=\begin{cases}
 (h_t/q)^p,&q\text{ odd},\\
 (h_t^p+d_t^p)/q^p,&q\text{ even}.
 \end{cases}}
\]
In particular, the exact probability of a basis is
\[
 \boxed{\mathbb P(A>0)=\frac{(q-1)^p+(-1)^p(\gcd(q,2)-1)}{q^p}.}
\]

For deterministic choice of all \(q\)-ary phases, the best possible lower frame bound is
\[
 \boxed{\max A=\begin{cases}
 1-\sin(\pi/(2q)),&q\text{ odd},\\
 1,&q\text{ even and }(2\mid p\text{ or }4\mid q),\\
 1-\sin(\pi/q),&q\equiv2\pmod4\text{ and }p\text{ odd}.
 \end{cases}}
\]
Thus a phase-alphabet Gabor **orthonormal basis** exists exactly when \(q\) is even and either \(p\) is even or \(4\mid q\). In particular, binary phase windows cannot even produce a basis when \(p\) is odd, whereas four phases permit an orthonormal basis for every \(p\ge2\).

The number of distinct ratio vectors \((c_0,\ldots,c_{p-1})\in\mathbb Z_q^p\) attaining this deterministic optimum is \(2^p\) for odd \(q\), exactly \(2\) for even \(q\) in the orthonormal-basis regime, \(3^p+1\) for \(q\equiv2\pmod4\), odd \(p\), \(q\ge6\), and \(2^p\) in the degenerate case \(q=2\), odd \(p\), where all windows have \(A=0\). For each ratio vector there are \(q^p\) windows, so division by \(q^p\) gives the probability that a random window attains the best bound.

## Assumptions and scope
All phases are precisely \(q\)-th roots of unity; no amplitude randomness or perturbation is allowed. The random statement takes the \(2p\) exponents independently and uniformly in \(\mathbb Z_q\). All synthesis columns have unit Euclidean norm. The lower bound uses the unweighted square family of \(p\) even modulations and exactly two translations \(0,1\). A zero lower bound means singularity, not a positive frame bound.

## Proof
**Fourier-fiber normalization.** Orthogonality of the \(p\) even characters gives \(\sum_{\ell=0}^{p-1}\exp(2\pi i\ell(j-j')/p)=p\) if \(j\equiv j'\pmod p\), and zero otherwise. After pairing coordinates \(r,r+p\), the frame operator decomposes into two-dimensional blocks \(S_r=v_rv_r^*+w_rw_r^*\), with
\[
 v_r=2^{-1/2}(\omega^{x_r},\omega^{x_{r+p}})^T,\quad
 w_r=2^{-1/2}(\omega^{x_{r-1}},\omega^{x_{r+p-1}})^T,\quad
 \omega=e^{2\pi i/q},
\]
where the indices in \(w_r\) are modulo \(2p\). Both vectors have norm one; hence the eigenvalues of \(S_r\) are \(1\pm|\langle v_r,w_r\rangle|\). For \(r\ge1\), their inner-product modulus is \(|\cos(\pi(c_r-c_{r-1})/q)|\). For \(r=0\), the cyclic wrap exchanges the two coordinates of the preceding pair, and the modulus is instead \(|\cos(\pi(c_0+c_{p-1})/q)|\). This proves the full spectrum and normalization.

**Exact finite-alphabet law.** The \(p\) ratios \(c_r\) are independent uniform residues because the pairs \((x_r,x_{r+p})\) are disjoint. The integer map \(c\mapsto k\) displayed above has determinant of absolute value \(2\): indeed \(k_r=c_r-c_{r-1}\) reconstructs every \(c_r\) from \(c_0\), and \(k_0=2c_0+\sum_{r=1}^{p-1}k_r\). For odd \(q\) it is a bijection, so the \(k_r\) are independent uniform residues. For even \(q\) its image is exactly the even-parity code \(\{k:\sum_r k_r\equiv0\pmod2\}\), and each codeword has precisely two preimages. The number of words with every letter in \(K_t\) and even parity is \((h_t^p+d_t^p)/2\). Dividing by the image size \(q^p/2\) proves the distribution formula. At \(t=0\), \(K_0=\{1,\ldots,q-1\}\); for even \(q\) its signed sum is \(-1\), yielding the stated exact basis probability.

**Sharp deterministic design.** The nearest \(q\)-th roots of unity to the antipode force the pointwise bound \(|\cos(\pi k/q)|\ge\sin(\pi/(2q))\) when \(q\) is odd, with equality precisely for \(k=(q\pm1)/2\). All choices of these optimal letters are feasible because \(c\mapsto k\) is bijective; this gives \(2^p\) optimal ratio vectors. For even \(q\), the sole letter giving zero inner-product modulus is \(k=q/2\). Its repetition in every fiber has even total parity exactly when \(p\) is even or \(4\mid q\), and then there are exactly two ratio preimages. Otherwise \(q\equiv2\pmod4\) and \(p\) is odd. Every feasible word must then contain a letter at least one unit away from \(q/2\), giving \(\max_r|\cos(\pi k_r/q)|\ge\sin(\pi/q)\). Replacing one antipodal letter by \(q/2+1\) corrects parity and attains the bound. For \(q\ge6\), optimal words have only the letters \(q/2-1,q/2,q/2+1\), and an odd number of deviations. There are \((3^p+1)/2\) such words, each with two preimages, giving \(3^p+1\) ratio vectors. At \(q=2\), odd \(p\), the bound is zero for every ratio vector, as the exact basis probability already shows. This exhausts equality cases.

## Verification
`CHECK.py` enumerates every ratio vector for \(2\le q\le8\) and \(2\le p\le5\), compares the exact survival counts, basis counts, deterministic optimum and optimal-vector counts with the formulas, and independently constructs full synthesis matrices for additional random configurations up to \(p=7\). Run `python CHECK.py` with the dependency in `REQUIREMENTS.txt`. The saved checker output is `QUANTIZED_GABOR_TESTS_PASSED 1630`. Exhaustive finite checks do not prove the all-parameter theorem; the algebraic argument above does.

## Relationship to prior work
Asipchuk, De Carli and Rodriguez (arXiv:2605.16139, first posted 2026-05-15) prove general block-equivalence of finite Gabor frames with a modulation subgroup. Their Fourier-block framework implies the availability of small blocks, but does not assert the twisted parity code, the exact finite-alphabet law or the sharp phase-quantization design threshold. Salanevich and Strachan (arXiv:2509.01325, first posted 2025-09-01) study stability of finite random Gabor frames with other quantitative objectives; their inspected results do not determine these exact finite-alphabet probabilities. Continuous uniform phase-window statistics for the same shift geometry give independence rather than the even-alphabet parity constraint, and do not imply this discrete law.

## Limitations
The phase alphabet is uniform and exactly finite. The distribution need not survive nonuniform phase probabilities, varying amplitudes, other translation sets or other modulation subgroups. The deterministic best lower bound is evaluated only within this restricted alphabet and sampling geometry. The comparison with prior work is not an independent publication-priority certification; possible equivalent older formulations under coding-theoretic terminology remain a residual risk.

## References
1. O. Asipchuk, L. De Carli and L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139, initial public version 2026-05-15, revised 2026-10-24, https://arxiv.org/abs/2605.16139 .
2. P. Salanevich and N. Q. D. Strachan, *Robustness to noise and erasures of Gabor frames in finite dimensions*, arXiv:2509.01325, initial public version 2025-09-01, https://arxiv.org/abs/2509.01325 .
