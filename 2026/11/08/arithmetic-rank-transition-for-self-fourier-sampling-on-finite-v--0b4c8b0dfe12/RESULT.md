# Arithmetic rank transition for self-Fourier sampling on finite Veronese cones

## Finding
Let \(q\ge3\) be an odd prime power, \(F=\mathbb F_q\), and
\[
V=\{vv^{\mathsf T}:v\in F^2\setminus\{0\}\}\subset\operatorname{Sym}_2(F),\qquad |V|=(q^2-1)/2.
\]
Fix a nontrivial additive character \(\psi:F\to\mathbb C^\times\). For symmetric matrices written as triples \((a,b,c)\) corresponding to \(\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)\), use the nondegenerate determinant-polar pairing
\[
B((a,b,c),(d,e,f))=af+cd-2be.
\]
Define the unnormalized self-Fourier matrix \(T_{X,Y}=\psi(B(X,Y))\) for \(X,Y\in V\). Put \(H=(F^\times)^2\), \(h=(q-1)/2\), and let \(\eta\) be the quadratic character of \(F^\times\). For every multiplicative character \(\chi:H\to\mathbb C^\times\), define its Gauss period
\[
 A_\chi=\sum_{t\in H}\chi(t)\psi(t),\qquad G=\sum_{t\in F^\times}\eta(t)\psi(t).
\]
**Complete singular spectrum:**
\[
\begin{array}{c|c}
\text{singular value}&\text{multiplicity}\\\hline
\frac12|qG-1|&1\\
\frac12|q-G|&q\\
\sqrt q\,|A_\chi|&q+1\quad\text{for each }\chi\ne\mathbf1\text{ on }H.
\end{array}
\]
Rows with equal values have their multiplicities added, and zero values are retained. In particular,
\[
\dim\ker T=(q+1)\#\{\chi\in\widehat H\setminus\{\mathbf1\}:A_\chi=0\}.
\]
This gives an exact scalar-period reduction of a matrix with \((q^2-1)/2\) rows and columns. Every odd **prime-field** instance is invertible for every choice of nontrivial \(\psi\). By contrast, for every prime \(p\equiv1\pmod4\), taking \(q=p^2\) and the **specified trace character**
\[
\psi_0(z)=\exp\!\left(\frac{2\pi i}{p}\operatorname{Tr}_{\mathbb F_{p^2}/\mathbb F_p}(z)\right)
\]
yields the infinite-family obstruction
\[
\dim\ker T\ \ge\ (p^2+1)(p-1)/2.
\]
For \(q=25\) the trace-character matrix has exactly \(52\) zero singular values, hence rank \(260\) out of \(312\).

## Assumptions and scope
The characteristic is odd and the pairing is the **polar form of the determinant**, not an unspecified matrix dot product. The image \(V\) consists of actual nonzero symmetric rank-one squares \(vv^{\mathsf T}\); unlike the full nonzero determinant-zero cone, it contains only the square-class scalar multiples of projective rank-one points. Its size is \((q^2-1)/2\), since \(v\) and \(-v\) give the same matrix. The spectral identity holds over every odd prime power and every nontrivial additive character. The subfield lower bound holds for the displayed trace character (and its scalar multiples by square elements); it is **not** asserted for arbitrary additive characters over \(\mathbb F_{p^2}\).

## Proof
**Projective-scalar parametrization.** Choose one representative \(v_i\in F^2\setminus\{0\}\) of each projective point \(i\in\mathbb P^1(F)\), so there are \(q+1\) representatives. Every element of \(V\) has a unique expression \(X_{i,s}=s v_iv_i^{\mathsf T}\) with \(s\in H\). Indeed, rescaling \(v_i\) rescales its square matrix by an element of \(H\); uniqueness holds after representatives are fixed. The elementary determinant-polar identity gives
\[
B(X_{i,s},X_{j,t})=st\det(v_i,v_j)^2.
\]
It equals zero precisely when \(i=j\).

**Character blocks.** Fourier-expand the scalar coordinate \(t\in H\) in the orthonormal multiplicative character basis \(\{\chi(t)/\sqrt h\}\). For an input proportional to \(\chi(t)\), the output is proportional to \(\chi(s)^{-1}\) and is determined by the \((q+1)\)-square block with entries
\[
K_\chi(i,j)=\begin{cases}
 h,&i=j,\ A_{\mathbf1},&i\ne j,
\end{cases}\qquad\text{if }\chi=\mathbf1,
\]
whereas for \(\chi\ne\mathbf1\),
\[
K_\chi(i,j)=\begin{cases}0,&i=j,\\
 A_\chi\,\chi(\det(v_i,v_j)^2)^{-1},&i\ne j.
\end{cases}
\]
The identity for \(\chi\ne\mathbf1\) follows from the substitution \(u=st\det(v_i,v_j)^2\in H\). The scalar-character output sectors are mutually orthogonal, so the singular values of the full matrix are exactly the union of the singular values of the blocks.

**Nontrivial block orthogonality.** For \(\chi\ne\mathbf1\), the function \(\mu(z)=\chi(z^2)\) is a nontrivial multiplicative character of \(F^\times\). Set \(M_\chi(i,i)=0\), and \(M_\chi(i,j)=\mu(\det(v_i,v_j))^{-1}\) for \(i\ne j\). Its diagonal Gram entries equal \(q\). For distinct projective points \(i,k\), the cross-ratio map
\[
 j\longmapsto\det(v_k,v_j)/\det(v_i,v_j)
\]
is a bijection from \(\mathbb P^1(F)\setminus\{i,k\}\) to \(F^\times\); summing \(\mu\) over that range gives zero. Hence
\[
M_\chi M_\chi^*=qI_{q+1}.
\]
Every singular value of \(K_\chi=A_\chi M_\chi\) therefore equals \(\sqrt q\,|A_\chi|\), with multiplicity \(q+1\), including when \(A_\chi=0\).

**Trivial block.** Here \(K_{\mathbf1}=(h-A_{\mathbf1})I_{q+1}+A_{\mathbf1}J_{q+1}\). The constant line has eigenvalue \(h+qA_{\mathbf1}\), and its orthogonal complement has eigenvalue \(h-A_{\mathbf1}\), with multiplicities \(1\) and \(q\). Since \(A_{\mathbf1}=(-1+G)/2\), these equal \((qG-1)/2\) and \((q-G)/2\). The quadratic Gauss-sum identity \(|G|=\sqrt q\) implies neither is zero. This proves the complete spectrum and exact kernel formula.

**Every prime field is injective.** For \(F=\mathbb F_p\), write \(\psi(t)=\zeta_p^{ct}\) with \(c\in\mathbb F_p^\times\), and let \(\chi\) be any character of \(H\), whose values belong to \(\mathbb Q(\zeta_h)\), \(h=(p-1)/2\). Since \(\gcd(p,h)=1\), the polynomial \(\Phi_p(z)=1+\cdots+z^{p-1}\) is irreducible over \(\mathbb Q(\zeta_h)\). If \(A_\chi=0\), the polynomial \(\sum_{t\in H}\chi(t)z^{ct\bmod p}\) would be a multiple of \(\Phi_p\), but it has constant coefficient zero and at least one nonzero coefficient. This is impossible. Thus all nontrivial blocks, as well as the trivial one, are invertible.

**An infinite quadratic-field obstruction.** Let \(p\equiv1\pmod4\), \(F=\mathbb F_{p^2}\), and choose \(\psi_0\) as in the statement. The trace-zero line is \(L_0=\{z:\operatorname{Tr}(z)=0\}=u\mathbb F_p\), with \(u^p=-u\). If \(u\ne0\), then \(u^{p-1}=-1\), so
\[
 u^{(p^2-1)/2}=(-1)^{(p+1)/2}=-1.
\]
Consequently \(L_0\setminus\{0\}\) has **no squares**, while \(\mathbb F_p^\times\subset H\). The group \(H/\mathbb F_p^\times\) has order \((p+1)/2\). Take any nontrivial character \(\chi\) of this quotient, pulled back to \(H\). On each line \(t\mathbb F_p^\times\subset H\), the character is constant, while
\[
 \sum_{a\in\mathbb F_p^\times}\psi_0(at)=-1
\]
since \(\operatorname{Tr}(t)\ne0\). Summing over the quotient gives \(A_\chi=-\sum_{H/\mathbb F_p^\times}\chi=0\). There are exactly \((p-1)/2\) such nontrivial characters, and their mutually independent blocks each have dimension \(q+1\), proving the kernel lower bound.

**Exact order-\(25\) boundary.** For the canonical trace character on \(\mathbb F_{25}\), the complete Gauss-sum pairing table in Garcia--Karaali--Katz (2018 preprint, Table 1) shows that among nontrivial \(\chi\) on \(H\), precisely the two characters of order three have \(A_\chi=0\). (The order-four character cancellations in that table concern the *difference*, not the sum, of the two extending Gauss sums.) Therefore \(\dim\ker T=2(25+1)=52\) and \(\operatorname{rank}T=312-52=260\). The numerical checker independently reproduces this rank; the exact prior Gauss table and the block proof, not numerical tolerance, justify exactness.

## Verification
Run `python verify_half_veronese.py` with Python 3 and NumPy installed. The checker constructs finite fields from prime modular arithmetic and explicit quadratic extensions, generates the Veronese points, independently assembles the full Fourier matrix, computes its numerical singular values, and compares them with all scalar-period predictions, **including multiplicities and zero levels**. Full-matrix tests pass for field sizes \(3,5,7,9,11,25\), with observed maximal absolute discrepancy below \(5\times10^{-14}\), and confirm the exact predicted nullity \(52\) for \(q=25\). A further check for \(q=169\) verifies the algebraically predicted six vanishing character periods (hence a kernel of dimension at least \(1020\)) without constructing a \(14280\)-square matrix. The explicit all-field proof, rather than finite numerical experiments, establishes the universal claims.

## Relationship to prior work
Iosevich and Koh (arXiv:0804.4505v1) and Koh and Yeom (arXiv:1601.07677v1) study finite-field quadratic-surface restriction, Fourier coefficients, and cone averaging. These furnish natural harmonic-analytic background but neither states the present **square self-Fourier sampling** singular spectrum for the proper square-scalar half of a conic. Garcia, Karaali, and Katz (arXiv:1807.07648v4, Section 6.3) **already give the index-two compressed Fourier Gauss-sum criterion**, prove the prime-field noncancellation, and tabulate the \(\mathbb F_{25}\) Gauss sums. Those scalar facts are explicitly **not** claimed new. The additional result is the projective Veronese block diagonalization, its all-field complete sampling spectrum and exact kernel multiplicities, and the resulting infinite family of high-dimensional sampling obstructions. Previously studied restricted coordinate-character frames on Veronese cones select different Fourier frequencies and do not determine the present square operator. A result about the complete nonzero cone or about its nonsingular complement also cannot by itself determine the spectrum of its square-scalar half without an extra symmetry decomposition.

## Limitations
The general singular values are expressed through finite Gauss periods, not uniform elementary radicals; the displayed formula is nevertheless exact for each finite field and additive character. For arbitrary nonprime fields, some periods may vanish, and no universal injectivity assertion is made. The quadratic-extension obstruction requires the specified trace character (or a square-scaled version), and the lower bound need not exhaust the kernel for every prime. Beyond \(q=25\), no exact nullity classification is claimed for quadratic extensions. The full historical-priority comparison remains bounded, and independent mathematical validation has not been carried out.

## References
1. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1, first made public 2008-04-28.
2. D. Koh and S. Yeom, *Restriction of averaging operators to algebraic varieties over finite fields*, arXiv:1601.07677v1, first posted 2016-01-28 (see particularly Section 4 on cones).
3. S. R. Garcia, G. Karaali and D. J. Katz, *An improved uncertainty principle for functions with symmetry*, arXiv:1807.07648v4, first posted 2018-07-19; especially Theorem 6.7, Corollary 6.9, Table 1.
