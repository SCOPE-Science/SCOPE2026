# Valuation-threshold law for prime-cardinality Fourier spectra on biprime-power cycles

## Finding

Let \(p\) and \(q\) be distinct primes with \(p\ge3\), and let \(k\ge2\). Put \(Q=q^k\) and \(G=\mathbb Z_p\times\mathbb Z_Q\), a cyclic group of order \(pQ\). A \(p\)-element set \(A\subset G\) is **spectral** if there is an unordered \(p\)-element character set \(B\subset\widehat G\) whose restriction to \(A\) is an orthogonal basis of \(\mathbb C^A\).

Every spectral \(p\)-set is a coordinate transversal
\[
A_f=\{(i,f(i)):i\in\mathbb Z_p\},\qquad f:\mathbb Z_p\longrightarrow\mathbb Z_Q.
\]
For such a function define the congruence depth
\[
t(f)=\max\big\{0\le t\le k: f(i)\equiv f(j)\pmod{q^t}\ \text{for every }i,j\big\}.
\]
Under the canonical dual-coordinate identification, the **complete classification of spectral pairs** is
\[
\boxed{\ B_g\text{ is a spectrum of }A_f\quad\Longleftrightarrow\quad t(f)+t(g)\ge k.\ }
\]
In particular the exact number of unordered Fourier spectra of a set at depth \(t\) is
\[
\boxed{\ S(t)=q^{k+(p-1)t}.\ }
\]
All \(k+1\) depths occur, and the number of distinct spatial sets in depth \(t\) is
\[
\boxed{\ N_t=\begin{cases}
q^k\big(q^{(k-t)(p-1)}-q^{(k-t-1)(p-1)}\big),&0\le t<k,\\
q^k,&t=k.
\end{cases}\ }
\]
Consequently the exact number of ordered spectral pairs \((A,B)\)—with each component an unordered \(p\)-point set—is
\[
\boxed{\ \sum_{t=0}^{k}N_tS(t)=(k+1)q^{k(p+1)}-kq^{k(p+1)-(p-1)}.\ }
\]
For example, when \((p,q,k)=(3,2,2)\), the depth strata have \(48,12,4\) sets, respectively, and spectrum multiplicities \(4,16,64\). Hence there are exactly \(640\) ordered spectral pairs. The spectrum-count ratio between maximal and minimal depths is \(q^{k(p-1)}\).

## Assumptions and scope

We identify \(\mathbb Z_{pQ}\) with \(G\) by the Chinese remainder theorem. The characters on \(G\) are
\[
\chi_{\alpha,\beta}(i,j)=\exp(2\pi i\alpha i/p)\exp(2\pi i\beta j/Q),\qquad (\alpha,\beta)\in G.
\]
This is the dual-compatible identification; ordinary cyclic-frequency coordinates differ only by multiplication by units in the two CRT components, which preserves all counts and depth conditions. In particular no factorial is inserted when counting spectra: a set with one frequency in each first-coordinate residue class is uniquely specified by a function \(g\).

The orthogonal-basis condition is equivalent to
\[
\sum_{a\in A}\chi_{b-b'}(a)=0\quad\text{for every distinct }b,b'\in B.
\]
All frequencies and spatial sites are distinct; coefficient weights are uniformly \(1\), and the restriction matrix is normalized by \(p^{-1/2}\) when discussing unitarity. The theorem does not concern weighted frames, larger spectral sets, or noncyclic groups with shared prime factors.

## Proof

**1. Two elementary cyclotomic facts.** Put \(\zeta_m=e^{2\pi i/m}\). First, a sum of \(p\) (repetitions allowed) \(Q\)-th roots of unity cannot vanish: reducing in \(\mathbb Z[\zeta_Q]\) modulo \((1-\zeta_Q)\) sends each root to \(1\) and gives \(p\not\equiv0\pmod q\), because \(\mathbb Z[\zeta_Q]/(1-\zeta_Q)\cong\mathbb F_q\). This also handles the case \(q=2\).

Second, the minimal polynomial of \(\zeta_p\) over \(K=\mathbb Q(\zeta_Q)\) is
\[
\Phi_p(X)=1+X+\cdots+X^{p-1}.
\]
Indeed \(\mathbb Q(\zeta_p,\zeta_Q)=\mathbb Q(\zeta_{pQ})\), whose degree over \(K\) is \(\varphi(pQ)/\varphi(Q)=p-1\). Therefore, for every \(\alpha\not\equiv0\pmod p\) and \(c_i\in K\),
\[
\sum_{i=0}^{p-1} c_i\zeta_p^{\alpha i}=0\quad\Longleftrightarrow\quad c_0=\cdots=c_{p-1}.
\]
The implication holds because the only degree-at-most-\(p-1\) relation is a scalar multiple of \(\Phi_p\).

**2. Every spectral \(p\)-set is a transversal.** Suppose \(A\subset G\) has \(p\) elements and possesses two distinct orthogonal restricted characters. Let their difference be \((\alpha,\beta)\). If \(\alpha=0\), the corresponding Fourier sum is a sum of \(p\) \(Q\)-th roots and cannot be zero, by Step 1. Hence \(\alpha\ne0\). Group the \(p\) terms by first coordinate to write
\[
0=\sum_{i=0}^{p-1}\zeta_p^{\alpha i}c_i,\qquad c_i=\sum_{(i,j)\in A}\zeta_Q^{\beta j}.
\]
Step 1 forces all \(c_i\) equal. They cannot all equal zero, since then their sum would be a vanishing sum of \(p\) \(Q\)-th roots. Thus each \(c_i\ne0\), so each first-coordinate residue occurs at least once among the \(p\) spatial points. Exactly one point occurs in each residue, and \(A=A_f\) for a unique \(f\). Conversely every transversal is spectral, by the \(p\) characters \(\{(\alpha,0):\alpha\in\mathbb Z_p\}\).

**3. Exact Fourier zeros of a transversal.** Write
\[
F_f(\alpha,\beta)=\sum_{i\in\mathbb Z_p}\zeta_p^{\alpha i}\zeta_Q^{\beta f(i)}.
\]
For \(\alpha=0\), \(\beta\ne0\), Step 1 gives \(F_f(0,\beta)\ne0\). For \(\alpha\ne0\), Step 1 gives
\[
F_f(\alpha,\beta)=0\iff
\zeta_Q^{\beta f(i)}\text{ is independent of }i
\iff \beta(f(i)-f(0))\equiv0\pmod Q\quad\forall i.
\]
By definition of \(t(f)\), the annihilator of these differences in \(\mathbb Z_Q\) is exactly \(q^{k-t(f)}\mathbb Z_Q\). Thus the entire nontrivial zero set is
\[
\{(\alpha,\beta):\alpha\ne0,\ \beta\in q^{k-t(f)}\mathbb Z_Q\}.
\]
(The zero frequency itself is not a Fourier zero.) This holds also for \(t(f)=0\) and \(t(f)=k\).

**4. The threshold law.** If \(B\) is a spectrum for \(A_f\), its restriction matrix is square unitary after normalization, so its transpose is unitary as well. Therefore \(B\) is also a spectral \(p\)-set and, by Step 2, is a transversal \(B_g\). Its pairwise frequency differences have nonzero first coordinate. By Step 3, all these differences lie in the zero set if and only if
\[
g(i)-g(j)\in q^{k-t(f)}\mathbb Z_Q\quad\forall i,j.
\]
This is equivalent to \(t(g)\ge k-t(f)\), namely the asserted symmetric inequality \(t(f)+t(g)\ge k\). Conversely, this inequality makes all distinct restricted characters orthogonal and hence a basis.

**5. Counting exactly.** Fix \(t=t(f)\). To build any permissible \(g\), choose \(g(0)\) freely from \(Q\) residues and choose each of the remaining \(p-1\) values congruent to it modulo \(q^{k-t}\), giving \(q^t\) choices per value. Hence
\[
S(t)=Q(q^t)^{p-1}=q^{k+(p-1)t}.
\]
For \(t<k\), to count \(f\) of exact depth \(t\), choose \(f(0)\) in \(Q\) ways, choose every other value modulo \(q^t\) identically, and exclude those also identical modulo \(q^{t+1}\). This yields
\[
N_t=Q\big(q^{(k-t)(p-1)}-q^{(k-t-1)(p-1)}\big).
\]
For \(t=k\), \(f\) is constant, giving \(N_k=Q\). Multiplying \(N_tS(t)\), every \(t<k\) contributes \(q^{k(p+1)}-q^{k(p+1)-(p-1)}\), and \(t=k\) contributes \(q^{k(p+1)}\). Summation gives the total stated in the Finding. Every depth has a positive count, completing the classification. \(\square\)

## Verification

The accompanying standalone `CHECK.py` uses only Python's standard library and **exact integer polynomial arithmetic**. It constructs cyclotomic polynomials by division, checks Fourier vanishing by exact remainders, independently enumerates all \(p\)-element spatial and frequency subsets for \((p,q,k)=(3,2,2)\) and three smaller cases, and confirms that precisely the transversals are spectral. It also checks all transversal pairs for \((3,2,3)\) and \((5,2,2)\), including the valuation compatibility condition and total counts. To reproduce, run `python CHECK.py` from the directory containing the file. The passing terminal marker is `ALL_EXACT_CHECKS_PASSED`. These finite tests are supplementary; Steps 1–5 establish the general theorem.

## Relationship to prior work

Kolountzakis and Malikiosis (2017) prove the spectral-to-tiling implication for cyclic groups of order a product of two prime powers, including the groups here, using vanishing sums of roots of unity. Malikiosis (2022) develops broader structural tools for spectral pairs in finite cyclic groups. Recent square-free cyclic Fuglede research (Somlai, 2026; Tan and Zhang, 2026) motivates asking for more quantitative information about the possible Fourier bases.

Those results establish existence or broad structural properties of spectra. The present claim instead gives the complete **pairwise compatibility relation**, exactly \(k+1\) possible basis multiplicities, all stratum sizes, and the total incidence count for the stated prime-cardinality family. The basic spectrality of transversals and cyclotomic lemmas are not claimed as new. Exhaustive full-text access to every recent preprint was not available, so publication priority is not independently established.

## Limitations

The classification is confined to \(p\)-element spatial sets in the cyclic group of order \(p q^k\), with distinct primes and \(k\ge2\). It concerns uniform orthogonal exponential bases, not weighted or approximately tight frames, condition numbers outside the orthogonal case, or arbitrary composite cyclic groups. No result for multiple distinct prime-power factors is asserted. An older equivalent incidence enumeration under cyclotomic-mask, Hadamard-submatrix, or tiling-complement terminology remains a specific originality risk.

## References

- G. Somlai, *Fuglede's Conjecture on Cyclic Groups of Square-Free Order: The Case of Rapidly Growing Prime Factors*, arXiv:2607.26534, first public July 29, 2026. https://arxiv.org/abs/2607.26534
- H. Tan and Y. Zhang, *Fuglede's Conjecture for Cyclic Groups of Square-free Order*, arXiv:2610.02218 (2026). https://arxiv.org/abs/2610.02218
- M. N. Kolountzakis and R. D. Malikiosis, *Fuglede's conjecture on cyclic groups of order \(p^nq\)*, Discrete Analysis 2017:12, DOI 10.19086/da.2071. https://doi.org/10.19086/da.2071
- R. D. Malikiosis, *On the structure of spectral and tiling subsets of cyclic groups*, Forum of Mathematics, Sigma 10 (2022), DOI 10.1017/fms.2022.14. https://doi.org/10.1017/fms.2022.14
