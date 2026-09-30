# Generalized packing-covering conjecture through redundancy fifteen

## Result

Let \(C\) be an \([n,k]_q\) linear code over an arbitrary finite field, with redundancy \(\rho=n-k\le 15\). For every
\[
1\le t\le \min\{k,\rho\},
\]
its \(t\)-th generalized Hamming weight and generalized covering radius satisfy
\[
\boxed{d_t(C)\le 2R_t(C)+2.}
\]
Equivalently, the generalized packing radius
\[
\delta_t(C)=\left\lfloor\frac{d_t(C)-1}{2}\right\rfloor
\]
satisfies
\[
\boxed{\delta_t(C)\le R_t(C).}
\]
Thus the generalized packing-covering conjecture holds for every linear code of redundancy at most fifteen over every finite field.

This extends the redundancy-fourteen theorem of Essayag and Zabokritskiy (2026). Their paper explicitly identifies the first binary parameter triple not excluded by their reductions as
\[
\rho=15,\qquad t=3,\qquad R_3(C)=6,
\]
with their general dimension estimate giving \(k\le 78\). The argument below resolves that remaining triple by replacing an averaged generalized-weight estimate with a small finite-geometric multiplicity bound.

## Background used

Write \(r=R_t(C)\). The following facts are taken from Essayag--Zabokritskiy, arXiv:2609.19098:

1. A counterexample must satisfy \(d_t(C)\ge 2r+3\).
2. Their reductions exclude the conjecture failure when \(t=1\), \(t=2\), \(r=t\), \(t\ge \rho-4\), \(k\le 5t-2\), \(3r\ge 2\rho\), the four pairs
   \((t,r)\in\{(3,4),(3,5),(4,5),(4,6)\}\), or \(q\ge r\).
3. Under a failure, with
   \[
   a=\rho-2r+t-2,\qquad b=\rho-2r-1,
   \]
   one has
   \[
   d_a(C^\perp)\ge k+b.
   \]
4. Their shortening estimate gives the finite dimension cap
   \[
   K(q,\rho,t,r)=
   \min_{a<h\le\rho}
   \left\lfloor
   \frac{(q^h-q^{h-a})h-b(q^h-1)}{q^{h-a}-1}
   \right\rfloor.
   \]
5. The generalized sphere-covering inequality is
   \[
   V_{q^t}(n,r)=\sum_{i=0}^{r}\binom ni(q^t-1)^i\ge q^{t\rho}.
   \]

For \(\rho=15\), applying exactly the same reductions leaves only prime-power alphabets
\[
q\in\{2,3,4,5,7,8\}.
\]
The finite arithmetic from the displayed cap excludes every reduced tuple except
\[
(q,t,r)=(2,3,6).
\]
The complete integer check is reproduced in `artifacts/verify_rho15.py`.

## Binary line-cap lemma

We need one elementary finite-geometric observation.

**Lemma.** Let \(g_1,\ldots,g_N\in\mathbb F_2^6\), with repetitions and zero vectors allowed. If every two-dimensional linear subspace of \(\mathbb F_2^6\) contains at most four of the \(g_j\), counted with multiplicity, then
\[
N\le 64.
\]

**Proof.** Let \(z\) be the multiplicity of the zero vector. Then \(0\le z\le4\). For a nonzero vector \(x\), let \(m_x\) be its multiplicity, put \(c=4-z\), and let
\[
M=\max_{x\ne0}m_x.
\]
If \(M=0\), there is nothing to prove. Otherwise choose \(p\ne0\) with \(m_p=M\). The other 62 nonzero vectors split into 31 disjoint pairs \(\{x,x+p\}\). Each pair together with \(p\) is the set of nonzero vectors of a two-dimensional subspace, so
\[
m_x+m_{x+p}\le c-M.
\]
Hence
\[
N\le z+M+31(c-M).
\]
We also have the trivial bound
\[
N\le z+63M.
\]
Taking the smaller bound and checking the finitely many integer pairs \(0\le z\le4\), \(1\le M\le4-z\), gives maximum values
\[
64,\ 64,\ 34,\ 4,\ 4
\]
for \(z=0,1,2,3,4\), respectively. Thus \(N\le64\). \(\square\)

## Resolving the remaining triple

Assume for contradiction that a binary code \(C\) has
\[
\rho=15,\qquad t=3,\qquad r=R_3(C)=6
\]
and violates the conjecture. Then
\[
d_3(C)\ge 2r+3=15.
\]
For the dual-weight consequence above,
\[
a=15-12+3-2=4,\qquad b=15-12-1=2,
\]
so
\[
\boxed{d_4(C^\perp)\ge k+2.}
\]

Choose nine coordinate positions whose columns in a full-rank parity-check matrix of \(C\) are independent, shorten \(C^\perp\) on those positions, and puncture the forced-zero coordinates. The resulting binary code \(D\) has dimension six, length \(N\le k+6\), and
\[
d_4(D)\ge k+2.
\]
Let \(G\in\mathbb F_2^{6\times N}\) be a full-row-rank generator matrix of \(D\), with columns \(g_1,\ldots,g_N\).

Fix any two-dimensional subspace \(W\le\mathbb F_2^6\) and put \(U=W^\perp\). Since \(\dim U=4\), the codewords \(uG\) with \(u\in U\) form a four-dimensional subcode of \(D\). A coordinate \(j\) vanishes identically on this subcode exactly when
\[
g_j\in U^\perp=W.
\]
Therefore the number of generator columns lying in \(W\), counted with multiplicity, is at most
\[
N-d_4(D)\le N-(k+2)\le4.
\]
The line-cap lemma gives
\[
N\le64.
\]
Since \(d_4(D)\le N\),
\[
k+2\le N\le64,
\]
and hence
\[
\boxed{k\le62},\qquad \boxed{n=k+15\le77}.
\]

Now apply the generalized sphere-covering inequality with \(q^t=8\) and \(r=6\). Since the left side is increasing in \(n\),
\[
2^{45}\le V_8(n,6)\le V_8(77,6).
\]
But exact integer evaluation gives
\[
V_8(77,6)
=\sum_{i=0}^6\binom{77}{i}7^i
=28{,}229{,}190{,}167{,}564
<35{,}184{,}372{,}088{,}832
=2^{45},
\]
a contradiction. Therefore the remaining binary triple cannot be a counterexample.

## Completion of the redundancy-fifteen case

For \(\rho=15\), the standard reductions leave the finite parameter set
\[
3\le t\le10,\quad
 t+1\le r\le\left\lfloor\frac{12+t}{2}\right\rfloor,\quad
3r<30,\quad q<r,
\]
with the four auxiliary-code pairs removed. Since \(r\le9\), only \(q\in\{2,3,4,5,7,8\}\) occur. Exact evaluation of the Essayag--Zabokritskiy dimension cap and their binomial covering criterion gives:

| \(q\) | reduced tuples | excluded by \(K\le5t-2\) | excluded by binomial criterion | remaining |
|---:|---:|---:|---:|---:|
| 2 | 13 | 2 | 10 | 1 |
| 3 | 13 | 2 | 11 | 0 |
| 4 | 13 | 2 | 11 | 0 |
| 5 | 13 | 0 | 13 | 0 |
| 7 | 7 | 0 | 7 | 0 |
| 8 | 3 | 0 | 3 | 0 |

The sole remaining row is exactly \((q,t,r)=(2,3,6)\), resolved above. Combining this with the already proved \(\rho\le14\) theorem establishes the claimed \(\rho\le15\) result over every finite field.

## Significance

The improvement is one redundancy unit, but it closes the first explicit obstruction left by the current strongest uniform theorem. The new ingredient is not a new covering construction: it is an integrality-sensitive refinement of the generalized-weight shortening step. In the exceptional binary case, the averaged support estimate only yields \(k\le78\); viewing zeros of four-dimensional subcodes as two-dimensional subspaces of \(\mathbb F_2^6\) converts the same dual-weight hypothesis into a line-multiplicity constraint and sharpens the bound to \(k\le62\), strong enough for the exact sphere-covering contradiction.

## Reproducibility

`artifacts/verify_rho15.py` uses Python's standard library only. It independently reproduces the finite \(\rho=15\) tuple reduction, identifies the unique leftover tuple, verifies the line-cap case bounds, and checks the final exact sphere-volume inequality. `artifacts/verify_rho15.txt` contains its output.

## Limitations

- This does not prove the generalized packing-covering conjecture beyond redundancy fifteen.
- The argument is specially tailored to the binary residual triple \((\rho,t,r)=(15,3,6)\). At redundancy sixteen several parameter families remain after the same reductions.
- The line-cap lemma is elementary and is not claimed as a new finite-geometry theorem by itself; the new claim is the redundancy-fifteen consequence and the associated sharpening of the exceptional dimension cap.
- No sharpness is claimed for the intermediate bound \(k\le62\).
- Originality is asserted only to the best of our knowledge. The motivating preprint is very recent, so near-simultaneous discovery or a subsequent revision remains a material priority risk.

## References

1. Isaac Barouch Essayag and Aryeh Lev Zabokritskiy (Yohananov), *Auxiliary Codes and the Generalized Packing-Covering Conjecture*, arXiv:2609.19098v1 (2026). https://arxiv.org/abs/2609.19098
2. Wenjun Yu and Moshe Schwartz, *On the Generalized Packing and Covering Radii of Codes*, arXiv:2609.14477v1 (2026). https://arxiv.org/abs/2609.14477
3. Dor Elimelech, Marcelo Firer, and Moshe Schwartz, *The generalized covering radii of linear codes*, IEEE Transactions on Information Theory 67 (2021), 8070--8085. https://doi.org/10.1109/TIT.2021.3115433
4. Victor K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418. https://doi.org/10.1109/18.133259
