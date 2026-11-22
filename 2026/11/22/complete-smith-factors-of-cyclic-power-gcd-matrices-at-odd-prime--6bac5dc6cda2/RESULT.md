# Complete Smith factors of cyclic power-GCD matrices at odd prime-square order

## Finding

Let \(p\ge3\) be a prime and \(a\ge1\) an integer. Index an integer matrix by \(\mathbb Z/p^2\mathbb Z\), with entries
\[
G_{p,a}(x,y)=\gcd(x-y,p^2)^a,
\]
where the gcd is positive and \(\gcd(0,p^2)=p^2\). Put
\[
X=p^a,\quad v=X-1,\quad u=Xv,\quad c=X+p,\quad
\alpha=vc,\quad\beta=vc+p^2.
\]
Then \(G_{p,a}\) is nonsingular and its **entire integral Smith normal form**, with positive invariant factors in divisibility order, is
\[
\boxed{\operatorname{SNF}(G_{p,a})=
\operatorname{diag}\!\left(1,
\underbrace{v,\ldots,v}_{p-1},
\underbrace{u,\ldots,u}_{p(p-2)},
pu,
\underbrace{uc,\ldots,uc}_{p-2},
\frac{X}{p}\alpha\beta\right).}
\]
The diagonal contains exactly \(p^2\) entries, and every successive entry divides the next. In particular, the \(p\)-primary cokernel is
\[
\operatorname{coker}(G_{p,a})[p^\infty]\cong
(\mathbb Z/p^a\mathbb Z)^{p(p-2)}\oplus
(\mathbb Z/p^{a+1}\mathbb Z)^p,
\]
and the rank of \(G_{p,a}\) modulo \(p\) is exactly \(p\).

For instance, at \(p=3\) and \(a=1\) the invariant factors are
\[
1,2,2,6,6,6,18,36,252.
\]
Thus its integer cokernel contains substantial torsion at primes different from the matrix's defining prime.

## Assumptions and scope

All indices are residue classes, and entrywise gcds are evaluated on integer representatives; changing representatives does not change their gcd with \(p^2\). The prime is odd, the exponent is any positive integer, and the matrix includes **all** \(p^2\) residue classes. Smith equivalence means left/right multiplication by unimodular integer matrices. Repetition in the displayed diagonal denotes multiplicity, not exponentiation.

## Proof

**1. Three-valued kernel and rational determinant.** Order the indices in \(p\) blocks according to residue modulo \(p\), each of size \(p\). The matrix entry is \(X^2\) on the diagonal, \(X\) for two distinct indices in one block, and \(1\) across different blocks. With \(J_m\) denoting the all-ones \(m\)-square matrix, this is exactly
\[
G_{p,a}=uI_{p^2}+v(I_p\otimes J_p)+J_{p^2}.
\tag{1}
\]
The rational vector space splits into within-block sum-zero vectors (dimension \(p(p-1)\)), vectors constant on blocks and of total sum zero (dimension \(p-1\)), and global constants (dimension one). The respective eigenvalues are \(u\), \(u+pv=\alpha\), and \(u+pv+p^2=\beta\). Hence
\[
\det G_{p,a}=u^{p(p-1)}\alpha^{p-1}\beta\ne0.
\tag{2}
\]
No use of rational diagonalization alone is made to infer the integral Smith factors.

**2. All primes away from \(p\).** Fix a prime \(\ell\ne p\). Averaging over a block, or over all blocks, is permitted in \(\mathbb Z_\ell\), because \(p\) is a unit. Thus the three spaces in step 1 are a direct sum of free \(\mathbb Z_\ell\)-modules, and (1) is equivalent over \(\mathbb Z_\ell\) to
\[
\operatorname{diag}\left(\underbrace{u,\ldots,u}_{p(p-1)},
\underbrace{\alpha,\ldots,\alpha}_{p-1},\beta\right).
\tag{3}
\]
We shall compare its valuations with the proposed ordered factors after treating \(\ell=p\).

**3. Exactly \(p\) unit factors at \(p\).** Let \(m=p(p-1)\). Choose one distinguished index from each of the \(p\) residue blocks, leaving \(m\) indices. Write \(R\) for the \(m\)-by-\(p\) zero-one block-incidence matrix (each row has one \(1\)). Set \(W=vI_p+J_p\). After simultaneously permuting rows and columns, equation (1) gives the block matrix
\[
\begin{pmatrix}
P&WR^{\mathsf T}\\
RW&uI_m+RWR^{\mathsf T}
\end{pmatrix},\qquad P=uI_p+W.
\tag{4}
\]
Modulo \(p\) we have \(u\equiv0\), \(v\equiv-1\), and hence \(P\equiv J_p-I_p\). The matrix \(J_p-I_p\) is invertible modulo \(p\): it acts by \(-1\) on the sum-zero space and by \(p-1\equiv-1\) on constants. Consequently the integral \(p\)-adic Smith reduction may pivot on \(P\), yielding \(p\) unit Smith factors and the Schur complement
\[
S=u\left(I_m+RW P^{-1}R^{\mathsf T}\right).
\tag{5}
\]
Indeed, \(W-WP^{-1}W=uWP^{-1}\), proving (5). Moreover, \(WP^{-1}\equiv I_p\pmod p\). Therefore the bracket in (5) reduces to
\[
I_m+RR^{\mathsf T}=
\operatorname{diag}\left(I_{p-1}+J_{p-1},\ldots,I_{p-1}+J_{p-1}\right)
\pmod p.
\tag{6}
\]
There are \(p\) blocks. Each block has exactly one zero eigenvalue and \(p-2\) unit eigenvalues over \(\mathbb F_p\), because its action on constants is multiplication by \(p\) and on the complementary sum-zero space is the identity. Hence exactly \(p(p-2)\) Smith factors of \(S\) have \(p\)-adic valuation \(a\), and the remaining \(p\) have valuation at least \(a+1\). Here \(u=p^a v\) and \(p\nmid v\).

Both \(\alpha=v(X+p)\) and \(\beta=\alpha+p^2\) have valuation exactly one at \(p\) (the oddness of \(p\) ensures \(\nu_p(X+p)=1\), including \(a=1\)). By (2), \(\nu_p(\det G_{p,a})=ap(p-1)+p\). Therefore all the remaining \(p\) factors have valuation **exactly** \(a+1\). The complete local valuation sequence at \(p\) is
\[
\underbrace{0,\ldots,0}_{p},\quad
\underbrace{a,\ldots,a}_{p(p-2)},\quad
\underbrace{a+1,\ldots,a+1}_{p}.
\tag{7}
\]

**4. Global invariant factors.** Form the claimed positive integer sequence
\[
1,\quad v^{[p-1]},\quad u^{[p(p-2)]},\quad pu,\quad(uc)^{[p-2]},\quad (X/p)\alpha\beta,
\tag{8}
\]
where superscript \([r]\) in (8) means *repeat the integer \(r\) times*, not raise it to a power. Consecutive divisibility follows from \(v\mid u\), \(u\mid pu\), \(p\mid c\), and
\[
\frac{(X/p)\alpha\beta}{uc}=\frac\beta p\in\mathbb Z.
\]
The product of (8) is the determinant in (2). Its valuations at \(p\) agree with (7): \(v\) is a unit, \(u\) has valuation \(a\), and both \(pu\) and \(uc\), as well as the last factor, have valuation \(a+1\).

For \(\ell\ne p\), note the crucial coprimalities
\[
\gcd(v,\beta)\mid p^2,\qquad\gcd(c,\beta)\mid p^2,
\tag{9}
\]
which follow from \(\beta=vc+p^2\). If \(\ell\mid\beta\), then \(v,c\) are \(\ell\)-units, so (8) has just one nonunit local factor, namely its last factor, with valuation \(\nu_\ell(\beta)\), matching (3). If \(\ell\nmid\beta\), the valuations of (8) consist of one zero, \(p(p-1)\) copies of \(\nu_\ell(v)=\nu_\ell(u)\), and \(p-1\) copies of \(\nu_\ell(vc)=\nu_\ell(\alpha)\). These are already nondecreasing, and agree with (3). This establishes equality of every local Smith valuation at every prime, so the integral Smith form is exactly (8). \(\square\)

## Verification

Run the independent finite arithmetic checks with `python3 check.py` (Python 3 standard library only). The checker constructs the original gcd-difference matrix, verifies every entry against (1), derives the proposed integer factors, and independently performs elementary row/column operations over \(\mathbb Z/\ell^M\mathbb Z\) for each prime \(\ell\) dividing the final invariant factor. It compares the resulting local Smith valuation lists—not merely determinant or numerical eigenvalues—with those predicted. Cases include \(p=3\) with \(a=1,2,3,4\), \(p=5\) with \(a=1,2\), and \(p=7\) with \(a=1\). All \(4499\) grouped exact assertions passed on those cases.

The modular calculations check examples; steps 1–4 above, especially the integral \(p\)-adic Schur reduction, are the proof for the infinitely many admissible \((p,a)\).

## Relationship to prior work

GCD/LCM-matrix divisibility results of Haukkanen–Korkee and Hong concern entries of the form \(\gcd(x_i,x_j)^a\) for a set of positive integers. They do not state the Smith form for the distinct *cyclic-difference* kernel \(\gcd(x-y,p^2)^a\). Telloni–Williams give explicit Smith forms for certain circulant polynomial matrices over a polynomial ring, not this fixed integer cyclic power-GCD matrix. The companion-ring framework of Noferini–Williams is also relevant, but its general reduction and torus-knot examples do not give the explicit invariant-factor family above. The present calculation makes the full integer cokernel explicit; the rational spectrum (2) and any largest-invariant-factor calculation alone do not determine this list.

## Limitations

The theorem is restricted to odd primes, complete residue sets modulo the prime square, and integer powers \(a\ge1\). It does not assert a formula for \(p=2\), for incomplete index subsets, or for the kernel modulo \(p^k\) when \(k\ge3\). Full integer Smith factors cannot be inferred merely by diagonalizing the circulant over the complex numbers. The literature comparison is not a proof of historical priority; an implicit specialization of more general Smith-form theory remains a residual risk. No independent mathematical audit is claimed.

## References

- P. Haukkanen and I. Korkee, “Notes on the divisibility of GCD and LCM matrices,” *International Journal of Mathematics and Mathematical Sciences*, 2005:6 (2005), 925–935, https://doi.org/10.1155/IJMMS.2005.925 (first published 25 May 2005).
- S. Hong, “Divisibility properties of power GCD matrices and power LCM matrices,” *Linear Algebra and its Applications* **428** (2008), 1001–1008, https://doi.org/10.1016/j.laa.2007.08.037.
- A. I. Telloni and G. Williams, “Smith forms of circulant polynomial matrices,” *Linear Algebra and its Applications* **458** (2014), 559–572, https://doi.org/10.1016/j.laa.2014.06.032 (open preprint: https://repository.essex.ac.uk/9703/1/TelloniWilliams-SmithFormsCirculants.pdf).
- V. Noferini and G. Williams, “Matrices in companion rings, Smith forms, and the homology of 3-dimensional Brieskorn manifolds,” arXiv:1908.07331 (2019), https://arxiv.org/abs/1908.07331.
