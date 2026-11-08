# Prime-divisor thresholds and exact weakest-cycle counts in higher-dimensional twisted baker maps

## Finding
Let \(M\ge4\) be an integer, let \(p\) be its smallest prime divisor, and let \(n\ge1\). For the Saiki–Takahasi–Yorke twisted baker map in dimension \(M\), exclude its nonisolated fixed face and consider only primitive periodic points of least period \(n\). For such a point \(x\), define the weakest normalized return multiplier by
\[
\chi(x)=\min\{ |\lambda|^{1/n}:\lambda\in\operatorname{spec}(DF^n(x))\}.
\]
Then the sharp minimum over every primitive period is
\[
\boxed{\min_{\operatorname{per}(x)=n}\chi(x)
=2^{\frac1M\min\{1,p/n\}}.}
\]

The cutoff \(n=p\) is exact. For \(1\le n\le p\), every nontrivial primitive period-\(n\) point attains the common value \(2^{1/M}\). For \(n>p\), equality holds **precisely** for those primitive binary itineraries with exactly \(p\) right-branch symbols and at least one cyclically adjacent pair of right-branch symbols. Every such word is primitive, and the exact number of distinct minimizing period-\(n\) cycles is
\[
\boxed{\frac1n\left[\binom np-I(n,p)\right],\qquad
I(n,p)=\begin{cases}
0,&p<n<2p,\\
\displaystyle\frac np\binom{n-p-1}{p-1},&n\ge2p.
\end{cases}}
\]
Here \(I(n,p)\) counts circularly nonadjacent \(p\)-subsets of \(n\) marked sites. In particular, **every even dimension \(M\ge4\) has exactly one weakest-expanding primitive cycle of each period \(n\ge3\)**; when the smallest prime factor is three, the number of minimizing cycles is \(n-3\) for \(n\ge4\). For \(n\le p\), the minimizing-cycle count is \(1\) at \(n=1\), and \(n^{-1}\sum_{d\mid n}\mu(d)2^{n/d}\) for \(2\le n\le p\).

This theorem applies to **least periods**, rather than to an unrestricted list of iterate-fixed points. In composite dimension, each minimizing cycle with \(n>p\) has nonreal return eigenvalues; in prime dimension, its return spectrum is entirely real.

## Assumptions and scope
For \(M\ge4\) let \(X=[-1,1]\times[0,1]^{M-1}\) and
\[
F(x_1,\ldots,x_M)=
\begin{cases}
(1+2x_1,x_2,\ldots,x_M),&x_1<0,\\
(1-2x_M,x_1,\ldots,x_{M-1}),&x_1\ge0.
\end{cases}
\]
Exclude \(N=\{x\in X:x_1=-1\}\), the nonisolated fixed face. A primitive period-\(n\) point is a point in \(X\setminus N\) whose *least* positive return time is \(n\). The symbols \(L,R\) denote the indicated branches. Jacobians are evaluated along these actual itineraries; the established coding excludes periodic switching-face ambiguities. All quantities are exact for integer dimensions and integer periods. The degree of expansion is measured by the smallest **eigenvalue modulus**, not a singular value of the return matrix.

## Proof
**1. Symbolic periodic points.** Saiki, Takahasi and Yorke establish that binary words of length \(n\) containing an \(R\) correspond bijectively to isolated points of \(\operatorname{Fix}(F^n)\), and that no such point lies on the discontinuity face; the all-left periodic sequence yields the excluded face \(N\). In particular, the least geometric period equals the least cyclic word period. Every primitive binary word other than the one-letter \(L\) is therefore realized by one of the periodic points considered here.

**2. Monomial cocycle and its cycle exponents.** The two branch matrices act on the standard basis as
\[
J_Le_1=2e_1,\quad J_Le_j=e_j\ (j>1),\qquad
J_Re_M=-2e_1,\quad J_Re_j=e_{j+1}\ (j<M).
\]
Fix a length-\(n\) itinerary with \(k\ge1\) occurrences of \(R\), and let \(A=DF^n(x)\). The matrix \(A\) is signed monomial: its underlying permutation sends the coordinate labelled \(j\) to \(j+k\) modulo \(M\). Put \(d=\gcd(M,k)\) and \(\ell=M/d\). The permutation has exactly \(d\) cycles of length \(\ell\), indexed by the coordinate residue classes modulo \(d\). If \(E_0,\ldots,E_{d-1}\) are the total base-two exponents of the weights carried by each permutation cycle, then
\[
\det(zI-A)=\prod_{h=0}^{d-1}\left(z^\ell-(-1)^{k/d}2^{E_h}\right),
\qquad\sum_{h=0}^{d-1}E_h=n.
\]
Every eigenvalue from cycle \(h\) has modulus \(2^{E_h/\ell}\), and hence
\[
\log_2\chi(x)=\frac{\min_h E_h}{\ell n}.
\]
For completeness, the sign in the cycle polynomial is the sign of \(k/d\) complete coordinate wraps; the exponents are sums of exactly the factors of two contributed by the successive branch matrices. This is also the signed-cycle factorization previously established for this map; here we refine it by locating every factor within its permutation residue class.

**3. Arithmetic lower bound.** At the \(r\)-th right-branch application, for \(r=0,\ldots,k-1\), the unique input coordinate receiving the factor two is one coordinate shifted by \(-r\) modulo \(M\). Its residue modulo \(d\) therefore cycles through all \(d\) residue classes exactly \(k/d\) times. Left-branch factors can only increase the nonnegative exponents. It follows that
\[
E_h\ge k/d\quad\text{for all }h.
\]
If \(d=1\), the unique cycle contains every coordinate and \(E_0=n\), so \(\log_2\chi(x)=1/M\) exactly. If \(d>1\), then \(d\) is a nontrivial divisor of \(M\), hence \(k\ge d\ge p\). Therefore
\[
\log_2\chi(x)\ge\frac{k/d}{(M/d)n}=\frac{k}{Mn}\ge\frac{p}{Mn}.
\]
Combining the two cases yields the claimed global lower bound.

**4. Sharpness and exact equality cases.** For \(1\le n\le p\), a primitive word cannot have \(\gcd(M,k)>1\): necessarily \(k\ge p\), forcing \(k=n=p\), the nonprimitive all-right word, except for the trivial one-letter case. Thus all actual primitive points have \(d=1\) and attain exponent \(1/M\); the word \(L^{n-1}R\) gives existence for every period \(n\) (with its evident interpretation at \(n=1\)).

For \(n>p\), the word \(L^{n-p}R^p\) has \(p\) right symbols, is primitive, and has a cyclic adjacent-right pair. There are exactly \(p\) permutation cycles, one right-step factor two in each. Every left step occurs in a single residue class, so one of the other classes has exponent exactly one. The weakest normalized multiplier is thus \(2^{p/(Mn)}\), strictly smaller than \(2^{1/M}\). This establishes sharpness.

Conversely, equality at \(n>p\) rules out \(d=1\). The inequality \(k/(Mn)\le p/(Mn)\) then forces \(k=p\) and \(d=p\). With exactly \(p\) right visits, the \(p\) intervals of left visits lying cyclically between successive right visits contribute to distinct residue classes. Writing their lengths as \(g_1,\ldots,g_p\), the cycle exponents are, up to ordering, exactly \(E_h=1+g_h\). The least exponent equals one precisely when some gap length vanishes, i.e. when two right symbols are adjacent in cyclic order. This proves the full minimizer characterization.

**5. Primitive-orbit enumeration.** Among \(n\)-letter cyclically indexed binary words with \(p\) right symbols, there are \(\binom np\) in total. If \(n<2p\), none can avoid adjacent right symbols. If \(n\ge2p\), count words with no cyclic adjacent rights by marking a right symbol and distributing at least one left symbol into each of the \(p\) following gaps. The \(n\) choices of marked starting position and \(\binom{n-p-1}{p-1}\) positive compositions count each resulting word \(p\) times, giving \(I(n,p)=n\binom{n-p-1}{p-1}/p\). Finally, a periodic word with exactly prime \(p\) right symbols can be a proper power only by repeating a one-right-symbol block exactly \(p\) times. For \(n>p\), such a repeated block has positive gaps between every consecutive right pair, so it is not a minimizer. Therefore every minimizing word is primitive, and division by \(n\) counts geometric cycles. For \(n\le p\), the usual Möbius count of primitive binary words gives the separate small-period formula. The real/nonreal assertion follows because a minimizing word has \(k=p\): its permutation-cycle length is \(M/p\), equal to one precisely when \(M\) is prime; if it is larger, at least one eigenvalue is nonreal.

## Verification
The analytical argument proves the statements for **all** \(M\ge4\) and all \(n\ge1\); it uses no numerical extrapolation. The dependency-free Python file `check_extremal.py` exhausts primitive binary words for dimensions \(2\le M\le12\) and periods \(1\le n\le10\), builds the complete signed monomial derivative, and compares the predicted minimum and exact number of attaining **points** in each of 110 dimension–period cases. It also constructs 1,440 physical periodic points by solving the affine fixed-point systems over exact rational arithmetic, checks their actual branch inequalities, and verifies their returns. It reports a PASS message. Run `python3 check_extremal.py` from the extracted package directory. Finite checks corroborate but cannot replace the all-dimensional proof.

## Relationship to prior work
The originating paper of Saiki, Takahasi and Yorke establishes the map, its binary coding, simultaneous density of real- and nonreal-spectrum periodic points, and nonuniform periodic-point expansion: the infimum of the weakest normalized multiplier over periodic points in any open set is one. It does **not** give a sharp minimum at prescribed least period. The publicly available note *Exact real-spectrum residue law for the twisted baker map* supplies a signed-cycle characteristic polynomial and exact real/nonreal proportions, but not the arithmetic optimization of its cycle exponents or the complete least-period minimizer count. An earlier three-dimensional result gives the special threshold \(n>3\), the minimum \(2^{1/n}\), and \(n-3\) minimizing cycles, which this theorem recovers; that existing special case is not claimed as new. The genuinely additional information here is the exact **all-higher-dimensional** least-prime-divisor threshold, including composite dimensions, and the complete extremal-word and orbit census. Takahasi's 2024 paper on the Dyck shift and heterochaos baker maps treats a different partially hyperbolic family.

## Limitations
The theorem is specific to the stated noninvertible twisted baker family and excludes its nonisolated fixed face. It optimizes **periodic return eigenvalue modulus**, not singular values, arbitrary nonperiodic Lyapunov exponents, or periodic points of other baker constructions. The dimension-three arithmetic and its cycle count are known prior special cases. Similar signed-permutation cocycles could yield equivalent formulas elsewhere; the inspected sources cannot establish universal novelty or independent validation. The source's symbolic-coding result is used for exact realization of primitive words, while the multiplier minimization and counting argument are independently reconstructed here.

## References
1. Y. Saiki, H. Takahasi, and J. A. Yorke, *The twisted baker map*, arXiv:2202.04304, first posted 9 February 2022, revision 3 of 13 January 2023, especially Lemmas 2.1–2.6, Theorems A–D, and Appendix A. https://arxiv.org/abs/2202.04304
2. *Exact real-spectrum residue law for the twisted baker map*, publicly available mathematical research record dated 11 October 2026, identifier `f1bd1c74fb3b`, especially the full characteristic-polynomial factorization and its stated limitations.
3. H. Takahasi, *Distributions of periodic points for the Dyck shift and the heterochaos baker maps*, arXiv:2409.01261, first posted 2 September 2024. https://arxiv.org/abs/2409.01261
