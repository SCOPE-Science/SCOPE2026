# Sharp Fourier-algebra norm gaps for valuation-orbit idempotents

## Finding

Let \(G\) be a finite abelian group with a strict subgroup chain
\[
G=H_0\supset H_1\supset\cdots\supset H_k,
\qquad [H_j:H_{j+1}]=q\ge2
\quad(0\le j<k).
\]
The *radial sets* relative to this chain are precisely the unions of the disjoint layers \(H_j\setminus H_{j+1}\) for \(0\le j<k\), together with the optional last layer \(H_k\). With normalized Fourier transform \(\widehat f(\chi)=|G|^{-1}\sum_{x\in G}f(x)\overline{\chi(x)}\), define \(\|f\|_{A(G)}=\sum_{\chi\in\widehat G}|\widehat f(\chi)|\).

**Sharp gap and equality theorem.** Let \(E\) be a nonempty radial set and \(f=\mathbf1_E\). If \(q\ge3\), then either \(E=H_j\) for some \(0\le j\le k\), and \(\|f\|_{A(G)}=1\), or
\[
\boxed{\|f\|_{A(G)}\ge 2\left(1-\frac1q\right),}
\]
with equality if and only if \(E=H_j\setminus H_{j+1}\) for some \(0\le j<k\). In particular the displayed bound is the exact smallest nonunit norm, independently of the depth \(k\).

If \(q=2\), the norm-one nonempty radial sets are exactly the subgroup balls \(H_j\) and the single shells \(H_j\setminus H_{j+1}\). Every other nonempty radial set satisfies
\[
\boxed{\|f\|_{A(G)}\ge\frac32.}
\]
For \(k\ge2\), equality holds exactly for the following two sets for some \(0\le j\le k-2\):
\[
\boxed{E=H_j\setminus H_{j+2},\qquad
E=(H_j\setminus H_{j+1})\cup H_{j+2}.}
\]
For \(k=1\), no nonempty radial set has norm exceeding one. The empty set has norm zero in all cases.

**Complete computable norm formula.** For \(e_0,\ldots,e_k\in\{0,1\}\), specify \(E\) by membership \(e_j\) on \(H_j\setminus H_{j+1}\) (\(j<k\)) and \(e_k\) on \(H_k\). Put \(\Delta_j=e_j-e_{j-1}\) for \(1\le j\le k\), and
\[
\mu=e_0+\sum_{j=1}^k\Delta_jq^{-j}.
\]
Then
\[
\boxed{
\|\mathbf1_E\|_{A(G)}=\mu+(q-1)\sum_{s=1}^k q^{s-1}
\left|\sum_{j=s}^k\Delta_jq^{-j}\right|.}
\]
This is an exact rational formula requiring at most quadratic arithmetic work in the chain depth; it also determines every nonzero Fourier coefficient by its annihilator shell.

**Valuation-orbit case.** Take \(G=(\mathbb Z/p^k\mathbb Z)^d\), \(H_j=p^jG\), for prime \(p\), positive integers \(d,k\). Then \(q=p^d\) and these layers are exactly the \(\mathrm{GL}_d(\mathbb Z/p^k\mathbb Z)\)-orbits. Thus the exceptional binary gap \(3/2\) occurs only for \(p=2,d=1\); all other cases have the sharp gap \(2(1-p^{-d})\).

## Assumptions and scope

All assertions concern finite abelian groups, genuine nested subgroups of common integer index \(q\), complex characters, the probability-normalized Fourier transform, and unweighted indicators that are constant on the prescribed layers. They do not concern arbitrary nonradial indicators, nonabelian groups, or infinite-depth limits. The spectral norm is the \(\ell^1\) sum of all Fourier coefficients, not a normalized average of their absolute values. The last subgroup may contain more than one element; the formula and proof do not assume it is trivial.

## Proof

**1. Reduction to the outermost occupied layer.** If \(E\neq\varnothing\), let \(j\) be the smallest index with \(e_j=1\). Then \(E\subseteq H_j\). A function supported on a subgroup \(H\le G\) has the *same* Fourier-algebra norm whether computed on \(G\) or on \(H\): every character of \(H\) has \([G:H]\) extensions to \(G\), and each corresponding Fourier coefficient is divided by \([G:H]\). Hence we may replace \(G\) by \(H_j\). Denote it by \(H\), and let \(U=H_{j+1}\), so \([H:U]=q\). The radial indicator has the form
\[
f=\mathbf1_{H\setminus U}+\mathbf1_F,
\quad F\subseteq U,
\quad \mu=|F|/|U|.
\]
If \(F=U\), then \(E=H\), with norm one. If \(F=\varnothing\), then \(E=H\setminus U\).

**2. Exact one-step character identity.** On the \(q\) characters of \(H\) trivial on \(U\), the Fourier coefficients are respectively \(((q-1)+\mu)/q\) for the trivial character and \((\mu-1)/q\) for the other \(q-1\) characters. Every nontrivial character \(\eta\) of \(U\) has \(q\) extensions to \(H\), all with Fourier coefficient \(\widehat{\mathbf1_F}^{\,U}(\eta)/q\). Summing absolute values yields the exact recursion
\[
\boxed{\|\mathbf1_E\|_{A(H)}=c_q+\|\mathbf1_F\|_{A(U)}-c_q\mu,\qquad c_q=2(1-q^{-1}).}
\tag{1}
\]
This also gives \(\|\mathbf1_{H\setminus U}\|_{A(H)}=c_q\), while \(\|\mathbf1_H\|_{A(H)}=1\).

**3. The nonbinary gap and rigidity.** Suppose \(q\ge3\) and \(F\) is nonempty and proper in \(U\). For any nonempty indicator \(g\), Fourier inversion gives \(\|g\|_A\ge\|g\|_\infty=1\). For the proper indicator \(g=\mathbf1_F\), its complement \(1-g\) is also nonempty. Because their nonzero-frequency coefficients are negatives and their zero-frequency coefficients are \(\mu\) and \(1-\mu\), respectively,
\[
\|g\|_A-\|1-g\|_A=2\mu-1,
\quad\text{hence}\quad\|g\|_A\ge2\mu.
\]
Substitute into (1):
\[
\|\mathbf1_E\|_A\ge c_q+(2-c_q)\mu
=c_q+\frac{2\mu}{q}>c_q.
\]
Thus all nonball radial sets have norm at least \(c_q\), and equality forces \(F=\varnothing\), i.e. one shell. This includes all depths and proves the complete nonbinary equality classification.

**4. The binary gap and rigidity.** For \(q=2\), the same identity becomes
\[
\|\mathbf1_E\|_A=1+\|\mathbf1_F\|_{A(U)}-\mu.
\]
For nonempty proper \(F\), the two basic indicator estimates give
\[
\|\mathbf1_F\|_{A(U)}-\mu\ge\max\{1-\mu,\mu\}\ge\frac12.
\]
Equality requires simultaneously \(\mu=1/2\) and \(\|\mathbf1_F\|_{A(U)}=1\). Since \(F\) is radial relative to the remaining constant-index-two chain, half the points of \(U\) have membership one only in the following two cases: its outer shell \(U\setminus H_{j+2}\) is entirely selected with all deeper layers omitted, or the whole next subgroup \(H_{j+2}\) is selected with the outer shell omitted. Indeed the outer shell and the next subgroup each occupy exactly half of \(U\); no other choices can have total density one half, as is seen by considering these two halves and the all-or-nothing membership on the outer shell. In both cases \(F\) is a coset of the index-two subgroup \(H_{j+2}\) (or the subgroup itself), so its \(A(U)\)-norm is exactly one. These yield precisely the two equality families above. When \(F=\varnothing\), the shell is the nonzero coset of \(U\) in \(H\), also norm one; when \(F=U\), it is a subgroup ball. No other binary norm-one cases exist.

**5. The complete formula.** The identity
\[
\mathbf1_E=e_0\mathbf1_G+\sum_{j=1}^k\Delta_j\mathbf1_{H_j}
\]
is pointwise exact, since the sum telescopes on each layer. On the trivial character the coefficient is \(\mu\). For a nontrivial character belonging to the annihilator shell \(H_s^\perp\setminus H_{s-1}^\perp\), with \(1\le s\le k\), the coefficient is
\[
\sum_{j=s}^k\Delta_jq^{-j}.
\]
The shell contains exactly \((q-1)q^{s-1}\) characters because \([G:H_s]=q^s\). Summation of absolute values gives the displayed formula. For the terminal subgroup \(H_k\), the Fourier coefficients vanish outside \(H_k^\perp\), consistent with the formula. Finally, the standard elementary reduction of nonzero vectors over the local principal ideal ring \(\mathbb Z/p^k\mathbb Z\) by invertible matrices shows that each valuation shell is one general-linear orbit and has index \(p^d\) relative to the next ball.

## Verification

The standalone program `check.py` enumerates every binary layer-membership vector at depths \(1\) through \(7\) for \(q\in\{2,3,4,5,7,9,16\}\), evaluates the exact rational norm formula, and checks the gap and all asserted equality classes. It also computes the independent direct complex discrete Fourier transform on ten small groups, including both cyclic prime powers and rank-two prime-power modules. Its recorded outcome is **3,556 exact rational cases plus 104 direct Fourier cases passed**. These are supplemental tests of the formulas and equality statements, not a substitute for the all-depth proof above. Run `python3 check.py` with the Python standard library only.

## Relationship to prior work

Vujičić (arXiv:2609.35740v1, first posted September 28, 2026), Sections 2 and 3.1, identifies the valuation shells as orbit-hypergroup layers and studies the corresponding central Fourier algebras and amenability. This supplies the natural symmetry class; the inspected theorem statements do not determine sharp small idempotent norms. Green and Sanders (2008) and Sanders (2020) provide general quantitative coset-ring and Fourier-algebra norm theory. Their statements do not distinguish the present common-index-shell gap, the binary exception, or the exact equality families. The nonzero shell Fourier transform itself is an immediate consequence of classical subgroup-character orthogonality, and is not claimed new. The claimed addition is the all-depth exact lower-end norm classification, with explicit equality cases and the full layer-bit norm formula.

## Limitations

The result is proved for radial \(0\)-\(1\) functions on a finite common-index abelian subgroup chain. General nonradial idempotents may have lower or different norms; the result does not imply a new universal gap for all idempotents. It makes no claim of infinite-depth convergence, nonabelian extensions, or an amenability characterization. Saeki's 1968 small-idempotent work and later broader idempotent classifications remain possible sources of equivalent consequences; the exact shell-chain statement was not located in the inspected sources. Independent validation has not been performed.

## References

- A. Vujičić, *The Fourier Algebra of Certain Compact Orbit Hypergroups*, arXiv:2609.35740v1, first public September 28, 2026, https://arxiv.org/abs/2609.35740 .
- B. Green and T. Sanders, *A quantitative version of the idempotent theorem in harmonic analysis*, Annals of Mathematics **168** (2008), 1025–1054, https://doi.org/10.4007/annals.2008.168.1025 .
- T. Sanders, *Bounds in Cohen's Idempotent Theorem*, Journal of Fourier Analysis and Applications **26** (2020), article 25, https://doi.org/10.1007/s00041-020-09732-y .
- S. Saeki, *On norms of idempotent measures. II*, Proc. Amer. Math. Soc. **19** (1968), 367–371, https://doi.org/10.1090/S0002-9939-1968-0228931-8 .
