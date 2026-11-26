# Universal Fourier and fixed-target commutator spectra of triangular matrix algebras over finite chain rings

## Finding

Let \(R\) be a finite commutative chain ring with maximal ideal \((\pi)\), length \(\ell\ge1\), and residue field of cardinality \(q\). Thus \(|R|=q^\ell\). Let \(T_3(R)\) be the free \(R\)-module of all upper triangular \(3\times3\) matrices, including singular matrices. For \(u,v,w\in R\), let \(F_R(u,v,w)\) count **ordered** pairs \((X,Y)\in T_3(R)^2\) with
\[
XY-YX=\begin{pmatrix}0&u&w\\0&0&v\\0&0&0\end{pmatrix}.
\]
Set \(\nu(0)=\ell\), and for \(x\ne0\) set \(\nu(x)=i\) when \(x\in\pi^iR\setminus\pi^{i+1}R\). For \((i,j,k)\in\{0,\ldots,\ell\}^3\), define
\[
a(i,j,k)=\min\{i,j,k\},\qquad b(i,j,k)=\min\{\ell,\min(i+j,i+k,j+k,2k)-a(i,j,k)\},
\qquad E_\ell(i,j,k)=q^{8\ell+2a(i,j,k)+2b(i,j,k)}.
\]
Define the valuation-shell sum, including the zero shell, by
\[
H_\ell(i;z)=\begin{cases}
1,&i=\ell,\\
q^{\ell-i}\mathbf1_{z\in\pi^{\ell-i}R}-q^{\ell-i-1}\mathbf1_{z\in\pi^{\ell-i-1}R},&0\le i<\ell.
\end{cases}
\]
Then every fixed-target fiber is given by
\[
\boxed{F_R(u,v,w)=q^{-3\ell}\sum_{i,j,k=0}^{\ell} E_\ell(i,j,k)H_\ell(i;u)H_\ell(j;v)H_\ell(k;w).}\tag{1}
\]
It depends only on \(q,\ell\) and the three target valuations, independently of the characteristic or presentation of \(R\). For any generating additive character \(\psi:R\to\mathbb C^\times\), the unnormalized Fourier transform is
\[
\boxed{\widehat F_R(s,t,h)=\sum_{u,v,w\in R}F_R(u,v,w)\psi(su+tv+hw)=E_\ell(\nu(s),\nu(t),\nu(h)).}\tag{2}
\]
Its \(2\ell+1\) distinct positive values are precisely \(q^{8\ell+2j}\) for \(0\le j\le2\ell\). The convolution walk on the additive group \(R^3\) that uses the commutator of a uniform ordered pair as its increment has exact nontrivial spectral radius \(q^{-2}\). The trivial character has eigenvalue \(1\).

For \(q=2,\ell=2\), (1) gives ten distinct nonempty fiber sizes and a zero-target fiber of size \(630784\). The unnormalized Fourier values are \(2^{16},2^{18},2^{20},2^{22},2^{24}\), with multiplicities \(40,12,9,2,1\), respectively. In particular the zero frequency has value \(2^{24}=4^{12}=16777216\), the total number of ordered pairs. The example applies to both \(\mathbb Z/4\mathbb Z\) and \(\mathbb F_2[\epsilon]/(\epsilon^2)\).

## Assumptions and scope

The ring is nonzero; its ideals are \(R\supset\pi R\supset\cdots\supset\pi^\ell R=0\), with each successive quotient of size \(q\). A generating additive character is one whose kernel contains no nonzero ideal. Such a character exists: take an additive character nontrivial on the smallest nonzero ideal \(\pi^{\ell-1}R\), which exists by separation in the character group of a finite abelian group. Every nonzero ideal contains that ideal. We count the **additive** commutator, not a group commutator. Every target is attained: for \(X=E_{11}+E_{23}\), the three output entries are \(Y_{12}\), \(Y_{33}-Y_{22}\), and \(Y_{13}-Y_{12}\), respectively. The theorem applies also to fields (\(\ell=1\)); the distinct regime is \(\ell\ge2\).

## Proof

**1. Bilinear pairing.** Write \(X=(A,B,C,x,y,z)\) and \(Y=(D,E,F,x',y',z')\) in diagonal and \((12),(23),(13)\) coordinates. Multiplication gives
\[
\begin{aligned}
[X,Y]_{12}&=(A-B)x'-(D-E)x,\\
[X,Y]_{23}&=(B-C)y'-(E-F)y,\\
[X,Y]_{13}&=(A-C)z'-(D-F)z+xy'-x'y.
\end{aligned}
\]
Thus the frequency-weighted output is \(X^{\mathsf T}B(s,t,h)Y\) for the alternating pairing whose nonzero upper-triangular entries in the coordinates \((d_1,d_2,x,y,z,C)=(A-B,B-C,x,y,z,C)\) are
\[
B_{d_1,x}=s,\quad B_{d_2,y}=t,\quad B_{d_1,z}=B_{d_2,z}=h,\quad B_{x,y}=h.\tag{3}
\]
The last coordinate is free and (3) makes sense also in characteristic two.

**2. Kernel profile, with no lifted valuation assumptions.** Put \((i,j,k)=(\nu(s),\nu(t),\nu(h))\) and \(a=\min(i,j,k)\). If \(a=\ell\), the entire form is zero and \(b=\ell\). Otherwise let \(L=\ell-a\) and \(R'=R/\pi^L R\). Multiplication by \(\pi^a\) identifies the additive module \(R'\) with \(\pi^aR\). The coefficients therefore factor uniquely as \(\pi^a\) times frequencies \((s',t',h')\) in \(R'\), with valuations \((i',j',k')=(i-a,j-a,k-a)\), where zero now has valuation \(L\). The kernel of the original pairing is the inverse image in \(R^6\) of the kernel of the normalized pairing in \((R')^6\), with \(q^{6a}\) lifts per vector.

At least one normalized frequency is a unit, so we can split off a unit alternating block, on the corresponding coordinate pair. Explicitly, for pivot vectors \(e,f\) with pairing \(p\) a unit, subtract suitable multiples of \(e,f\) from each other vector to make it pair to zero with both. This is an invertible change of basis, with no division by two. The matrix on the three remaining nonfree coordinates has the following entries up to sign:

- If \(h'\) is a unit, use the pivot \((d_1,z)\). The remaining \((x,y)\) entry is unchanged and equals \(h'\): neither \(x\) nor \(y\) pairs with \(z\). Thus the second block is a unit block.
- If \(s'\) is a unit and \(h'\) is not, pivot on \((d_1,x)\). The remaining pairs on \((d_2,y,z)\) have entries \(t',h',\pm(h')^2/s'\). Their ideal is \((t',h')\).
- Otherwise \(t'\) is a unit. Pivoting on \((d_2,y)\) leaves entries \(s',h',\pm(h')^2/t'\) on \((d_1,x,z)\), generating \((s',h')\).

The three-coordinate complement has at most one nonzero alternating block. Indeed, select an entry of minimal valuation generating the ideal of entries; that entry divides every other one. Subtracting pivot-vector multiples then clears both pivot pairings, leaving a single coordinate with zero alternating self-pairing. If all entries were zero, use the zero block. After scaling the unit part of the pivot, this gives a block \(\pi^c\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\) with
\[
c=\min\{L,i'+j',i'+k',j'+k',2k'\},
\]
as seen by setting the relevant unit valuation to zero in each case. This calculation uses only the chain ring \(R'\), including when some of the original products are zero due to truncation. Since \(a+c=b(i,j,k)\), and a block with exponent \(c\) over \(R'\) has kernel of size \(q^{2c}\), the normalized kernel has size \(q^{2c+2L}\): there is one unit block, one exponent-\(c\) block, and two free coordinates. Restoring lifts yields
\[
|\ker B(s,t,h)|=q^{6a+2c+2L}=q^{2(\ell+a+b)}.\tag{4}
\]
The same formula holds for the all-zero frequency.

**3. Fourier transform and inversion.** By the generating property, \(\sum_X\psi(X^{\mathsf T}BY)\) equals \(q^{6\ell}\) if \(BY=0\), and zero otherwise: a nonzero coordinate of \(BY\) would give a nontrivial character as its corresponding \(X\) coordinate varies. Summing over \(Y\) gives (2) by (4). All additive characters are \(z\mapsto\psi(xz)\), since the map from \(x\in R\) is injective and both sets have the same cardinality. For frequency ideal \(\pi^iR\), summing the inverse character against \(z\) gives \(q^{\ell-i}\) when \(z\in\pi^{\ell-i}R\) and zero otherwise. Subtraction of the sum over the next ideal gives \(H_\ell(i;z)\), independent of the sign in the character. The singleton frequency zero gives \(H_\ell(\ell;z)=1\). Grouping Fourier inversion over these shells in all three coordinates proves (1).

**4. Spectral levels and sharp radius.** At zero frequency \(a+b=2\ell\); at a nonzero frequency \(a\le\ell-1\) and \(b\le\ell\). If \(h=0\), then \(k=\ell\), so \(a+b=i+j\): \(i+j\) is the minimum of the four sums in the definition of \(b\) and \(i+j-a=\max(i,j)\le\ell\). All levels \(0,\ldots,2\ell\) are attained this way, in particular \(2\ell-1\) at \(i=\ell-1,j=\ell\). Dividing by \(q^{12\ell}\) gives the walk eigenvalues and the exact nontrivial radius.

## Verification

The standard-library `verify.py` directly counts kernels of the six-coordinate frequency matrix, including all 64 frequencies of each of the two order-four rings, and compares the resulting counts against the formula. It separately enumerates ordered matrix pairs and checks the inverted fibers over \(\mathbb F_2\). The tests are finite and do not replace the chain-ring argument. In the order-four example, the multiplicities can also be checked by counting the three frequency valuations: the shells of valuations \(0,1,2\) have sizes \(2,1,1\), and summing their product sizes by the value of \(a+b\) gives \(40,12,9,2,1\). Substituting the same shell sums in (1) gives distinct fiber counts \(147456,221184,270336,294912,344064,368640,393216,466944,565248,630784\).

## Relationship to prior work

Fosner, Liang, Wei and Xiao [1] study Lie products, centralizing traces and triangular algebras, rather than fixed-target counts. Choosuwan, Jitman and Udomkavanich [2] count determinant fibers, which are a related but different counting problem. The previously reported exact field fibers [3] are the \(\ell=1\) specialization and are not claimed as new. The triangular two-by-two chain-ring count [4] concerns commuting tuples, not the three-coordinate fixed-target map. The contribution is the explicit kernel/Fourier profile, full fixed-target distribution and sharp spectral radius in the non-field regime, using standard alternating pairings and character orthogonality. A broader prior bilinear counting result may imply this specialization; historical priority is not certified.

## Limitations

The result does not address non-chain local rings, noncommutative coefficient rings, larger triangular algebras, group commutators, or scheme-theoretic fiber geometry. The shell formula is explicit but is not a minimal list of distinct fiber counts for every \((q,\ell)\). The finite diagnostics are not formal verification or expert attestation.

## References

1. A. Fosner, X. Liang, F. Wei, Z. Xiao, *Centralizing traces and Lie triple isomorphisms on generalized matrix algebras*, [arXiv:1411.6122](https://arxiv.org/abs/1411.6122).
2. P. Choosuwan, S. Jitman, P. Udomkavanich, *Determinants of Matrices over Commutative Finite Principal Ideal Rings*, [arXiv:1605.06826](https://arxiv.org/abs/1605.06826).
3. *Exact fibers of the Lie commutator on three-by-three triangular matrices*, [public research record](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-exact-fibers-of-the-lie-commutator-on-three-by-three-triangular--ab8c2df75df2/RESULT.md).
4. *Two-pole commuting-tuple and clique enumerators for triangular algebras over finite chain rings*, [public research record](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-two-pole-commuting-tuple-and-clique-enumerators-for-triangular-a--8fae3394a05c/RESULT.md).
