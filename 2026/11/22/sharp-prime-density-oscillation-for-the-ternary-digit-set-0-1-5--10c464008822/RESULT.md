# Sharp prime-density oscillation for the ternary digit set \(\{0,1,5\}\)

## Finding
Let \(D=\{0,1,5\}\), \(S_D=\{\sum_{j\ge0}d_j3^j:d_j\in D,\ d_j=0\text{ eventually}\}\), \(A_D(X)=\#\{0\le n\le X:n\in S_D\}\). For the strictly positive continuous one-periodic function characterized by \(A_D(X)=X\Psi_D(\log_3 X)+O(1)\), the exact range is
\[
\min_{u\in\mathbb R}\Psi_D(u)=\frac58,\qquad \max_{u\in\mathbb R}\Psi_D(u)=\frac34.
\]
The lower endpoint is attained at integer phases \(u\equiv0\pmod1\); the upper endpoint at \(u\equiv\log_3(2/3)\pmod1\). If \(\pi_D(X)\) counts representable primes and \(\pi(X)\) all primes, then
\[
\liminf_{X\to\infty}\frac{\pi_D(X)}{\pi(X)}=\frac58,\qquad
\limsup_{X\to\infty}\frac{\pi_D(X)}{\pi(X)}=\frac34.
\]

## Assumptions and scope
The base is exactly three and digits are exactly \(D=\{0,1,5\}\). An expansion uses finitely many nonzero digits, uniquely. Results concern real \(X\to\infty\), all phases, and the usual rational primes; no claim is made for other digit sets. We use the known asymptotic and arithmetic-weight transfer for this digit system [1]. The proof below independently certifies the new sharp extremal bounds.

## Proof
**Finite-state model.** The carry state set is \(K=\{-3,-2,-1,0\}\). For input trit \(a\in\{0,1,2\}\), set \(d_0=0,d_1=1,d_2=5\) and \(h_a(c)=(a+c-d_{[a+c]_3})/3\). Let the \(4\times4\) matrix \(T_a\) act on columns \(v\) by \((T_av)(c)=v(h_a(c))\). The word \(021\) sends all four states to zero. Hence, for independent uniformly distributed low trits, the carry Markov chain has a unique stationary law, exponentially approached from every starting state. Direct rational matrix multiplication gives the stationary row \(\rho=(0,1/8,1/4,5/8)\), in the order \((-3,-2,-1,0)\); indeed \(\rho(T_0+T_1+T_2)/3=\rho\).

For the Boolean column \(e(c)=\mathbf1_{c=0}\), the possible vectors \(T_{a_m}\cdots T_{a_1}e\) form a finite set \(V\) of exactly fourteen elements. Put \(w(v)=8\rho v=v(-2)+2v(-1)+5v(0)\). The limiting scaled counting function \(F(t)=\lim_{N\to\infty}3^{-N}A_D(3^Nt)\) for \(0\le t\le1\) exists by the carry coupling (and by [1]). For each vector \(v\in V\), define its normalized cylinder cumulative function \(H_v(t)\), with \(H_v(0)=0\), \(H_v(1)=w(v)\), and
\[
H_v((a+t)/3)=\frac{1}{3}\left(\sum_{j=0}^{a-1}w(T_jv)+H_{T_av}(t)\right)\quad(0\le t\le1,\ a=0,1,2).
\]
By the stationary law and the most-significant-digit cylinder decomposition, \(H_e(t)=8F(t)\). These functions are continuous: each normalized cylinder has mass at most \(8\cdot3^{-m}\), tending uniformly to zero with depth.

**Exact extremal barriers.** For all fourteen reachable Boolean states, define the integers \(L_v\) and \(U_v\) by the following finite certificate (state bits are ordered \((-3,-2,-1,0)\)):

| State | \(w(v)\) | \(L_v\) | \(U_v\) |
|---|---:|---:|---:|
| 0000 | 0 | -5 | 0 |
| 0001 | 5 | 0 | 0 |
| 0010 | 2 | -3 | 0 |
| 0011 | 7 | 0 | 1 |
| 0100 | 1 | -4 | 0 |
| 0110 | 3 | -2 | 0 |
| 0111 | 8 | 0 | 2 |
| 1000 | 0 | -5 | 0 |
| 1001 | 5 | 0 | 0 |
| 1011 | 7 | 0 | 1 |
| 1100 | 1 | -4 | 0 |
| 1101 | 6 | 0 | 1 |
| 1110 | 3 | -2 | 0 |
| 1111 | 8 | 0 | 2 |

The supplied proof checker computes every one of the \(42\) transitions and verifies, for \(a=0,1,2\),
\[
3L_v\leq\sum_{j<a}(w(T_jv)-5)+L_{T_av},\qquad
3U_v\geq\sum_{j<a}(w(T_jv)-6)+U_{T_av}.
\]
Since \(L_v\leq0\leq U_v\), recursion on finite ternary endpoints and continuity imply \(L_v\leq H_v(t)-5t\) and \(H_v(t)-6t\leq U_v\) for every \(0\le t\le1\). For the root \(e=0001\), the two first-digit branches \(a=1,2\) satisfy the stronger exact checks
\[
\sum_{j<a}(w(T_je)-5)+L_{T_ae}\geq0,\qquad
\sum_{j<a}(w(T_je)-6)+U_{T_ae}\leq0.
\]
Hence \(5t\leq8F(t)\leq6t\) for all \(1/3\leq t\leq1\). The root first-level cylinder weights are \(w(T_0e)=5\) and \(w(T_1e)=7\), so \(F(1/3)=5/24\) and \(F(2/3)=1/2\), giving equality at \(5/8\) and \(3/4\). By the scaling identity \(F(t)=t\Psi_D(\log_3t)\) of [1], and periodicity of \(\Psi_D\), this interval covers every phase and proves the sharp full range.

**Primes.** The prime-transfer theorem in [1] gives \(\pi_D(X)/\pi(X)=\Psi_D(\log_3X)+O(1/\log X)\). Its hypotheses hold because \(D\) is a complete residue system modulo three and \(\gcd(D)=1\). Every phase occurs along \(X=3^{m+u}\) as \(m\to\infty\), proving both limits.

## Verification
Run \(`python3 proof_check.py`\). The checker uses exact integer and rational arithmetic to independently reconstruct the carry maps and stationary distribution, exhaustively enumerate the fourteen reachable states, verify all \(84\) lower/upper Bellman inequalities and four root inequalities, and check the equality values. Eight finite digit-count diagnostics are supplementary and are not substituted for the infinite recursive argument.

## Relationship to prior work
Zhou [1] supplies the general periodic-counting asymptotic, prime-transfer theorem, scaling measure and the carry table for this exact digit set, as well as a zero-synchronizing word. Zhou does **not** determine the sharp image, global minima/maxima, extremal phases or resulting exact liminf/limsup of prime proportions. These depend here on a nontrivial fourteen-state extremal certificate. The theory of self-affine digit sets in Lagarias--Wang [2] and general tile-measure algorithms [3] is related but does not in the inspected accessible material identify these sharp constants; full comparison with their historical full texts remains a risk.

## Limitations
This sharp result treats only the motivating ternary digit set; it does not establish general extremal laws for arbitrary complete residue digit sets. The primary analytic prime-transfer theorem is used as a cited premise rather than rederived in full. Historical broader tile literature may contain a different derivation of the same numerical bounds. The proof and finite certificate have not undergone independent external mathematical audit.

## References
[1] Nian Hong Zhou, *Periodic counting, carry synchronization, and primes in nonstandard numeration systems*, arXiv:2611.07446v1, first public 2026-11-05. https://arxiv.org/abs/2611.07446

[2] Jeffrey C. Lagarias and Yang Wang, *Integral Self-Affine Tiles in R^n. I. Standard and Nonstandard Digit Sets*, J. London Math. Soc. 54 (1996), 161–179, https://doi.org/10.1112/jlms/54.1.161.

[3] Jean-Pierre Gabardo and Xiaojiang Yu, *Natural Tiling, Lattice Tiling and Lebesgue Measure of Integral Self-Affine Tiles*, J. London Math. Soc. 74 (2006), 184–204, https://doi.org/10.1112/S0024610706022915.
