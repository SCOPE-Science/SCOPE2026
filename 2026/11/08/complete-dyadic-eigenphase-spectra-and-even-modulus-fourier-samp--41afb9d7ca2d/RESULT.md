# Complete dyadic eigenphase spectra and even-modulus Fourier sampling on reduced residues

## Finding

Let \(N\ge2\) be even, \(U_N=(\mathbb Z/N\mathbb Z)^\times\), and consider the unit-indexed principal compression of the **unitary** Fourier matrix, with positive Fourier sign,
\[
A_N=(N^{-1/2}e^{2\pi i xy/N})_{x,y\in U_N}.
\]
The following is an explicit complete complex-eigenvalue and eigenspace classification for **all even moduli**, complementing the previously established odd-modulus classification. The new local calculation is at powers of two.

For any integer \(k\ge1\), put \(q=2^k\), choose an odd residue \(b\), and define \(A_{q,b}\) by replacing the phase in the displayed matrix with \(e^{2\pi i bxy/q}\). The complete eigenvalues, with multiplicity, are:

* \(k=1\): \(-1/\sqrt2\) once.
* \(k=2\): \(0\) once; \(i^b\) once.
* \(k=3\): \(0\) twice; \(\varepsilon_b=\operatorname{sgn}\cos(\pi b/4)\) once; \(i\delta_b=i\operatorname{sgn}\sin(\pi b/4)\) once.
* \(k\ge4\): \(0\) with multiplicity \(2^{k-2}\); each of \(1,-1,i,-i\) with multiplicity \(2^{k-4}\).

For \(k\ge2\), put \((Tf)(x)=f(x+2^{k-1})\) on functions indexed by odd residues and \(K=(I-T)/2\). Then \(K\) is the positive-singular-value projector, \(P_0=I-K\), and the orthogonal projector onto each fourth-root eigenspace (with zero projector if its multiplicity vanishes) is
\[
P_\lambda=\frac14\sum_{j=0}^{3}\lambda^{-j}A_{q,b}^{j}K,\qquad\lambda\in\{1,-1,i,-i\}.
\]
Thus, for every \(k\ge2\), exactly half of the dyadic unit-indexed Fourier compression's singular values are one and half are zero. The exception \(q=2\) has a single singular value \(1/\sqrt2\). The dyadic complex eigenphases exhibit genuine separate regimes at \(2,4,8\), then become equally populated from \(16\) onward.

**Complete even-modulus assembly.** Write \(N=\prod_{j=0}^r q_j\), where \(q_0=2^k\) and the other \(q_j\) are odd prime powers. Let \(b_j\in U_{q_j}\) satisfy \(b_j(N/q_j)\equiv1\pmod {q_j}\). Then a simultaneous permutation of row and column indices identifies
\[
A_N\simeq\bigotimes_{j=0}^r A_{q_j,b_j}.
\]
The complete complex eigenvalue multiset therefore consists of all products of local eigenvalues, with product multiplicities added whenever numerical eigenvalues coincide. Its orthogonal eigenspace projectors are sums of the corresponding tensor products of local projectors.

For completeness, the published odd-prime-power local factors used in this assembly have the following explicit rule. If \(q=p^a\) for odd \(p\) and \(a\ge2\), zero has multiplicity \((p-1)p^{a-2}\), and each of \(1,-1,i,-i\) has multiplicity \((p-1)^2p^{a-2}/4\). For \(a=1\), put \(s=\left(\frac bp\right)\). The eigenvalue \(-1/\sqrt p\) occurs once. If \(p\equiv1\pmod4\), respective multiplicities at \(1,-1,i,-i\) are \((p-3+2s)/4,(p-3-2s)/4,(p-1)/4,(p-1)/4\); if \(p\equiv3\pmod4\), they are \((p-3)/4,(p-3)/4,(p-1+2s)/4,(p-1-2s)/4\). The odd factor formulas are background prior mathematics, not newly asserted as original here.

In particular, let \(r_2=1\) when \(k=1\), and \(r_2=2^{k-2}\) when \(k\ge2\). For the odd-prime-power factors put \(r_{p,1}=p-1\), \(r_{p,a}=(p-1)^2p^{a-2}\) for \(a\ge2\). Then
\[
\operatorname{rank}(A_N)=r_2\prod_{p^a\parallel N,\ p\text{ odd}}r_{p,a},\quad
\operatorname{nullity}(A_N)=\varphi(N)-\operatorname{rank}(A_N),\quad
\kappa_{\mathrm{nz}}(A_N)=\sqrt{\prod_{p^1\parallel N,\ p\text{ odd}}p}.
\]
Consequently an even-modulus unit-indexed principal Fourier matrix is invertible precisely when \(N\) is squarefree, in which case its full condition number equals \(\sqrt{N/2}\) if \(2\mid N\) (with the empty product interpreted as one). The last conclusion includes \(N=2\).

## Assumptions and scope

All Fourier matrices are normalized by \(1/\sqrt N\) (not by \(1/\sqrt{\varphi(N)}\)), and use positive sign. A twist \(b\) in a local matrix must be a unit modulo its prime power. The index set is precisely the invertible residues, not an arbitrary Fourier mask. Simultaneous row and column permutations preserve eigenvalues. The formula for \(\kappa_{\mathrm{nz}}\) is the ratio of largest to smallest **positive** singular values; the usual inverse condition number is infinite for singular matrices.

## Proof

**1. A local exact Gram identity in characteristic two.** Fix \(q=2^k\), \(k\ge2\), and any odd \(b\). The prime-power Ramanujan sum over odd residues is
\[
c_q(t)=\sum_{u\in U_q}e^{2\pi iut/q}=\begin{cases}
q/2,&q\mid t,\\-q/2,&q/2\mid t\text{ and }q\nmid t,\\0,&q/2\nmid t.
\end{cases}
\]
The identity follows by subtracting the even-residue character sum from the full geometric sum, so it holds without any analytic approximation. Let \(h=q/2\), \((Tf)(x)=f(x+h)\), and \((Rf)(x)=f(-x)\). Since \(b\) is invertible, it permutes the unit residues, whence direct matrix multiplication gives
\[
AA^*=A^*A=K=(I-T)/2,\qquad A^2=KR.
\]
The involutions \(T\) and \(R\) commute (because \(-h=h\pmod q\)). Thus \(K\) is an orthogonal projector of rank \(2^{k-2}\) and \(A\) is normal. The operator vanishes on \(\ker K\) and is unitary on \(\operatorname{ran}K\); \(A^4=(KR)^2=K\) there and on the whole space. Therefore the only nonzero eigenvalues are fourth roots of unity, each with modulus one. Finite Fourier inversion on the cyclic fourth-root spectrum yields the stated \(P_\lambda\), while \(P_0=I-K\). These are mutually orthogonal since \(A\) is normal. This also proves the dyadic rank, nullity, and singular values.

**2. The exceptional low powers.** At \(q=2\), the matrix has the sole entry \(2^{-1/2}e^{\pi i b}=-2^{-1/2}\). At \(q=4\), all odd squares are one modulo four; therefore \(\operatorname{tr}A=i^b\). Since \(\operatorname{rank}K=1\), this trace is the unique nonzero eigenvalue. At \(q=8\), again every odd square is one modulo eight, giving
\[
\operatorname{tr}A=\frac4{\sqrt8}e^{\pi ib/4}
=\varepsilon_b+i\delta_b.
\]
Moreover \(\operatorname{tr}(A^2)=\operatorname{tr}(KR)=0\): a diagonal entry of \(KR\) would require \(x\equiv-x\pmod {q/2}\), impossible for an odd \(x\) when \(q\ge8\). Rank two and the zero square trace force one real and one imaginary fourth-root eigenvalue. Comparing traces identifies precisely \(\varepsilon_b\) and \(i\delta_b\).

**3. Four equal phase multiplicities at all higher dyadic levels.** If \(k\ge4\), pair every odd residue \(x\) with \(x+2^{k-2}\). The difference of their squares is \(2^{k-1}x+2^{2k-4}\), congruent to \(2^{k-1}\pmod {2^k}\). Therefore the two diagonal Fourier phases differ by minus one, so \(\operatorname{tr}A=0\). The preceding fixed-point calculation gives \(\operatorname{tr}A^2=0\). As the nonzero eigenvalues are fourth roots and zero eigenvalues contribute nothing, \(\operatorname{tr}A=0\) implies equality of the positive/negative real multiplicities and equality of the positive/negative imaginary multiplicities; \(\operatorname{tr}A^2=0\) makes the total real and imaginary multiplicities equal. Since the positive-singular-value rank is \(2^{k-2}\), each fourth-root multiplicity is exactly \(2^{k-4}\).

**4. The odd local factors, reconstructed for completeness.** Let \(q=p^a\), \(p\) odd, and define \(A_{q,b}\) analogously. For \(a\ge2\), the standard Ramanujan identity is \(c_q(t)=\varphi(q)\) for \(q\mid t\), \(-p^{a-1}\) for \(p^{a-1}\mid t\) but \(q\nmid t\), and zero otherwise. Consequently \(A^*A=AA^*=K\), the orthogonal projection subtracting the mean separately within each fiber of unit residues modulo \(p^{a-1}\). This has rank \((p-1)^2p^{a-2}\), and \(A^2=KR\), where \(R\) reflects residues. Negation has no fixed unit fiber modulo \(p^{a-1}\), giving \(\operatorname{tr}A^2=0\); the diagonal trace vanishes by summing the primitive linear phases over the last digit (here invertibility of \(2bx\) uses odd \(p\)). Hence each fourth-root multiplicity is one quarter of the rank, and the kernel has dimension \((p-1)p^{a-2}\). If \(a=1\), then \(K=I-J/p\), the constant vector is a \(-1/\sqrt p\) eigenvector, and on the mean-zero orthogonal complement \(A^2=R\) and \(A^4=I\). Trace of \(R\) there equals \(-1\), while the classical positive-sign quadratic Gauss sum gives \(\operatorname{tr}(A\mid_{\mathbf1^\perp})=\left(\frac bp\right)\) for \(p\equiv1\pmod4\) or \(i\left(\frac bp\right)\) for \(p\equiv3\pmod4\). Solving these trace and dimension equations recovers the listed integer multiplicities. These arguments verify the needed known odd-factor identities rather than assuming a black-box numerical result.

For the odd factors the orthogonal spectral projectors are likewise explicit: for \(a\ge2\), \(P_0=I-K\) and \(P_\lambda=\tfrac14\sum_{j=0}^3\lambda^{-j}A^jK\); for \(a=1\), letting \(Q\) project onto constants and \(E=I-Q\), use \(P_{-1/\sqrt p}=Q\) and \(P_\lambda=\tfrac14\sum_{j=0}^3\lambda^{-j}A^jE\).

**5. Chinese-remainder spectral transfer.** For pairwise coprime prime powers \(q_j\mid N\), the CRT identity for all integer \(x,y\) is
\[
e^{2\pi i xy/N}=\prod_j e^{2\pi i b_j x_jy_j/q_j},
\qquad b_j(N/q_j)\equiv1\pmod {q_j}.
\]
It follows by writing the CRT idempotents and noting that the normalized factors \(q_j^{-1/2}\) multiply to \(N^{-1/2}\). Mapping a unit \(x\pmod N\) to its CRT residue tuple permutes rows and columns **identically**, giving the stated tensor product up to unitary permutation similarity. Tensor products of normal matrices are normal, their eigenvalue multisets are products, and tensor products of their orthogonal projectors give the full complex spectral resolution. The rank factors; the local nonzero singular moduli are one for all repeated prime factors (including powers of two with \(k\ge2\)), \(1/\sqrt2\) at the isolated factor two, and \(1,1/\sqrt p\) at an odd first-power factor. This proves the rank, nullity, nonsingularity criterion, and positive-singular-value conditioning formula for every even \(N\).

## Verification

`CHECKER.py` implements local exact structural matrix checks and numerical diagonalization, plus exact CRT phase congruences for even composite moduli. Use Python 3 with NumPy installed (`python CHECKER.py`). The tested cases included dyadic levels \(2\) through \(128\), multiple odd twists, larger trace identities through \(2^{11}\), and 27 composite even moduli through \(120\). The tests confirm the predicted eigenspectra and projectors at the sampled scales. No finite numerical test is used as proof of the universal claims; the proof is the algebraic block calculation above.

## Relationship to prior work

The discrete Fourier transform of arithmetic even functions and the Ramanujan-sum identities are classical harmonic-arithmetic tools. Tóth and Haukkanen studied Fourier action on the much smaller subspace of functions constant on gcd classes; that does not specify the eigenphase spectrum of the full space of functions supported on units. A published classification already gives the corresponding **odd-modulus** unit-indexed compression, including its local projectors. Its exact odd local formulas are used as established input and rederived in Step 4. The new calculation concerns the **excluded dyadic prime-power local factor**, the exceptional complex phases at \(4\) and \(8\), their projector structure, and the consequent full even-modulus tensor classification. General work on Fourier principal minors establishes other nonsingularity statements but not these complex eigenphase multiplicities. The adjacent stronger overlap risk is another, as yet unidentified, general result on reduced-residue Fourier operators including the dyadic case.

## Limitations

The statement is restricted to unit-indexed principal Fourier compressions and positive-sign normalization. It does not assert that arbitrary even-order principal minors have this spectrum or that all singular Fourier minors possess a pseudoinverse of this form. The theorem supplies an explicit finite arithmetic spectral algorithm, not a unique closed formula for every coincident product eigenphase without factoring the modulus. Independent mathematical validation and exhaustive historical priority verification have not been performed; the complete text of one older plausible Fourier-submatrix report was unavailable.

## References

1. L. Tóth and P. Haukkanen, *The discrete Fourier transform of \(r\)-even functions*, arXiv:1009.5281v1 (first publicly posted 2010-09-27), https://arxiv.org/html/1009.5281v1.
2. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793v1 (first publicly posted 2024-09-15), https://arxiv.org/html/2409.09793v4.
3. *Complete eigenphase spectrum of primitive-index Fourier minors over odd moduli*, publicly archived 2026-10-11, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-complete-eigenphase-spectrum-of-primitive-index-fourier-minors-o--e9c768339b6f/RESULT.md.
4. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Fourier matrices*, technical report TW470 (2006), subsequently *Linear Algebra and its Applications* 429 (2008), 1587–1605, https://www.cs.kuleuven.be/publicaties/rapporten/tw/TW470.abs.html (complete report inaccessible in this comparison).
