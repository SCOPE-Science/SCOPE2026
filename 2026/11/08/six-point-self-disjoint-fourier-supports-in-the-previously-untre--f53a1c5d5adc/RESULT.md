# Six-point self-disjoint Fourier supports in the previously untreated prime class, sharp over \(\mathbb F_7^2\)

## Finding
Let \(G_p=\mathbb F_p^2\) with the standard coordinate pairing, and define
\[
\sigma_p=\min_{0\ne f:G_p\to\mathbb C}\big\{|\operatorname{supp}f|:\operatorname{supp}f\cap\operatorname{supp}\widehat f=\varnothing\big\}.
\]
For **every prime** \(p\equiv7\pmod{24}\), the explicit construction below yields
\[
\sigma_p\le6.
\]
At the first such prime this is optimal:
\[
\boxed{\sigma_7=6.}
\]
Equivalently, the \(49\times49\) Fourier character table of \(\mathbb F_7^2\), with the same coordinate labels for rows and columns, has a singular six-by-six principal submatrix but **no** singular principal submatrix of orders one through five. The size-six assertion is constructive, whereas the smaller-order exclusion has a self-contained exhaustive exact finite-field certificate.

## Assumptions and scope
For each odd prime \(p\), put \(\zeta=e^{2\pi i/p}\) and
\[
\widehat f(a,b)=\frac1p\sum_{(x,y)\in\mathbb F_p^2} f(x,y)\zeta^{ax+by}.
\]
The coordinate dot-product identification between the group and its dual is fixed. Signals are complex-valued; the support is the set of nonzero coefficients. The theorem covers primes \(p\equiv7\pmod{24}\) for the six-point upper bound and exactly \(p=7\) for the lower bound. It does not assert \(\sigma_p=6\) for all larger primes in that congruence class.

## Proof
**A uniform six-point construction.** For any prime \(p\equiv7\pmod{24}\), quadratic reciprocity gives \(\left(\frac{-3}{p}\right)=\left(\frac p3\right)=1\); hence choose \(t\in\mathbb F_p^\times\) with \(t^2=-3\). Define the nonzero coefficients of \(f\) on the six distinct sites
\[
S_t=\{(0,0),(0,1),(0,2),(t,1),(t,2),(t,3)\}
\]
by
\[
\begin{aligned}
f(0,0)&=-\zeta^3,&f(0,1)&=\zeta+\zeta^2,&f(0,2)&=-1,\\
f(t,1)&=\zeta^3,&f(t,2)&=-(\zeta+\zeta^2),&f(t,3)&=1.
\end{aligned}
\]
Here \(\zeta+\zeta^2\ne0\) since \(p\ge7\). Setting \(z=\zeta^b\), the unnormalized Fourier sum factorizes exactly:
\[
\begin{aligned}
p\widehat f(a,b)
&=-(z-\zeta)(z-\zeta^2)+\zeta^{at}z(z-\zeta)(z-\zeta^2)\\
&=(z-\zeta)(z-\zeta^2)(\zeta^{at+b}-1).
\end{aligned}
\]
At the four support points with second coordinate one or two, one of the first two factors vanishes; at \((0,0)\), the last factor vanishes; and at \((t,3)\), the last factor is zero because \(t^2+3=0\) in \(\mathbb F_p\). Thus \(\widehat f\) vanishes on \(S_t=\operatorname{supp}f\), proving \(\sigma_p\le6\).

**Exact exclusion of smaller supports at \(p=7\).** Write \(\omega=e^{2\pi i/7}\) and let \(H\) be the unnormalized character matrix indexed by \(G_7\),
\[
H_{(a,b),(x,y)}=\omega^{ax+by}.
\]
If a nonzero signal is supported on a set \(S\) and its Fourier transform vanishes on \(S\), then \(H_{S,S}\) has a nonzero kernel. Translating \(S\) by \(h\in G_7\) does not change singularity, since
\[
H_{x+h,y+h}=\omega^{h\cdot h}\omega^{h\cdot x}H_{x,y}\omega^{h\cdot y}.
\]
Therefore it suffices to check all principal sets \(S\) containing the origin and with \(1\le |S|\le5\): precisely
\[
\sum_{j=0}^{4}\binom{48}{j}=1+48+1128+17296+194580=213053
\]
sets.

The accompanying complete `CHECK.cpp` enumerates every one of these sets, and performs Gaussian elimination **without numerical approximation** in the prime field \(\mathbb F_{1000000093}\). It proves primality by trial division, checks that \(w=993004909\) has exact order seven in that field, and constructs the reduction of \(H\) under \(\omega\mapsto w\). Every one of the \(213053\) reduced principal matrices has nonzero determinant (the program checks their full rank). This implies the corresponding complex determinant is nonzero: since \(\Phi_7(w)=0\), the map \(\mathbb Z[\omega]\to\mathbb F_{1000000093}\), \(\omega\mapsto w\), is a well-defined ring homomorphism; a zero cyclotomic-integer determinant would necessarily reduce to zero. Hence no complex principal minor of orders one through five is singular. Combined with the displayed six-point signal (take \(t=2\) at \(p=7\)), this proves \(\sigma_7=6\).

## Verification
Save the included `CHECK.cpp` alongside this file and execute

```sh
c++ -O2 -std=c++17 CHECK.cpp -o check
./check
```

The code has no nonstandard dependencies. Its successful output includes `CHECK_OK exact_principal_minors=213053 prime=1000000093 primitive_root=993004909`. It individually reports nonsingular-minor counts \(1,48,1128,17296,194580\) at sizes one through five, respectively, and independently verifies the six-point witness in the same exact coefficient field. The computer calculation certifies only the **finite exclusion at \(p=7\)**. The construction for every prime \(p\equiv7\pmod{24}\) is the preceding algebraic proof and does not rely on the finite enumeration. The exact computational certificate is reproducible, but no external independent audit is claimed.

## Relationship to prior work
Zhou's 2026 analysis of self-disjoint Fourier supports poses the prime-square problem and constructs a support of size \(2p-2\) when \(p\equiv3\pmod4\); it explicitly does not determine the minimum in two dimensions. A separate publicly available four-point theorem completely solves the class \(p\equiv3\pmod8\) by a square-root-of-\(-2\) construction. The primes treated here satisfy \(p\equiv7\pmod8\), so that earlier theorem and its construction do not imply the six-point claim or the sharp \(p=7\) result. Caragea and Lee study principal Fourier minors in cyclic groups, for which the group structure and character matrix differ from the elementary Abelian \(\mathbb F_p^2\) case. Exact low-order *non-principal* minor classifications do not supply the five-by-five principal nonsingularity asserted here.

## Limitations
The six-point construction is not proved minimal for primes \(p>7\); different coordinate pairings or real-valued coefficient restrictions are not treated. The small-order nonsingularity claim is computer-assisted and depends on the supplied compiler-readable, finite exact-arithmetic enumeration. It does not follow from sampled numerical eigenvalues or testing a subset of candidates. No equivalence with unresolved cyclic-root counting conjectures is asserted. An unindexed earlier six-point construction or a more general principal-minor theorem remains a residual originality risk.

## References
1. W. Zhou, *On number of cyclic \(n\)-roots and disjointness of Fourier supports*, arXiv:2608.06335 (initial public posting 2026-08-06), particularly Section 2.3 and Proposition 3. https://arxiv.org/abs/2608.06335
2. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793 (2024), cyclic-group results. https://arxiv.org/abs/2409.09793
3. *Sharp four-point self-disjoint Fourier supports on \(\mathbb F_p^2\) for \(p\equiv3\pmod8\)* (2026 publicly indexed mathematical record), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-four-point-self-disjoint-fourier-supports-on-mathbb-f-p-2--7b34d464851b
