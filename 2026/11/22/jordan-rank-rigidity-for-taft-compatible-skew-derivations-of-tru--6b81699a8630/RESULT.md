# Jordan-rank rigidity for Taft-compatible skew derivations of truncated polynomial algebras

## Finding

Fix an integer \(m\ge2\), a field \(k\) containing a primitive \(m\)-th root \(\zeta\), and \(N\ge2\). Let \(A_N=k[x]/(x^N)\), with the specified automorphism \(\sigma(x)=\zeta x\). Consider all \(k\)-linear maps \(D:A_N\to A_N\) satisfying the skew Leibniz identity, the Taft commutation relation and the Taft nilpotence relation:
\[
D(ab)=D(a)b+\sigma(a)D(b),\qquad D\sigma=\zeta\sigma D,\qquad D^m=0.
\]
These are precisely the actions of the skew-primitive Taft generator for the *fixed* group-like generator action \(\sigma\), with the convention \(XG=\zeta GX\) and \(\Delta(X)=X\otimes1+G\otimes X\).

Write \(N=m\ell+r\), where \(0\le r<m\). Every such map is uniquely \(D=D_f\) with
\[
D_f(x^i)=[i]_{\zeta}x^{i-1}f(x^m),\qquad [i]_{\zeta}=1+\zeta+\cdots+\zeta^{i-1},
\]
where \(f(x^m)\) ranges over the \(\sigma\)-invariant polynomials of degree less than \(N\), subject only to the requirement that its constant coefficient is zero when \(r>0\). In particular, \(D_f^m=0\) is automatic from the other conditions.

For nonzero \(f(x^m)\), let \(s\) be the smallest exponent such that the coefficient of \(x^{ms}\) is nonzero. Then for every \(1\le j<m\), the rank of the \(j\)-th power is
\[
\rho_j(s)=\begin{cases}
(m-j)(\ell-js)+\min(r,m-j),&\ell\ge js,\\
0,&\ell<js.
\end{cases}
\]
Also \(\rho_0=N\) and \(\rho_m=0\). Thus **the full nilpotent Jordan partition of \(D_f\) is determined solely by \(s\)**: the number of blocks of size \(j<m\) is \(\rho_{j-1}-2\rho_j+\rho_{j+1}\), while the number of size-\(m\) blocks is \(\rho_{m-1}\). For nonzero \(D_f\), already the single rank
\[
\operatorname{rank}D_f=(m-1)(\ell-s)+r
\]
determines \(s\) and hence every Jordan block multiplicity. The zero map is separately identifiable by rank zero.

If \(k=\mathbb F_q\) and \(m\mid q-1\), put \(t=\lceil N/m\rceil\) and \(\varepsilon=0\) when \(r=0\), \(\varepsilon=1\) when \(r>0\). The complete linear-rank polynomial of these actions, with the fixed \(\sigma\), is
\[
\mathcal R_{m,N,q}(T)=1+\sum_{s=\varepsilon}^{t-1}(q-1)q^{t-1-s}T^{(m-1)(\ell-s)+r}.
\]
The sum is empty when its lower endpoint exceeds its upper endpoint. There are exactly \(q^{t-\varepsilon}\) actions. Distinct nonzero summands have distinct degrees, so the rank polynomial encodes the complete Jordan-profile frequency distribution.

For instance, \(m=3,N=10,q=7\) gives \(\mathcal R(T)=1+6T+42T^3+294T^5\); for valuation \(s=1\), the Jordan partition is \(3^2 2^1 1^2\), whereas valuations \(s=2,3\) give \(2^3 1^4\) and \(2^1 1^8\), respectively.

## Assumptions and scope

The field characteristic is arbitrary subject to the existence of a primitive \(m\)-th root, which forces the characteristic not to divide \(m\). These are unital algebra module actions with the group-like automorphism \(\sigma\) **fixed**; varying the group-like action and classifying actions up to algebra isomorphism are not claimed. No algebraic-closure hypothesis is used. Counts apply to finite fields with \(m\mid(q-1)\). The power-rank formulas count linear maps, not conjugacy orbits or abstract Taft modules up to isomorphism.

## Proof

**1. Reduction to the generator.** The skew Leibniz identity forces \(D(1)=0\), and induction gives \(D(x^i)=[i]_{\zeta}x^{i-1}D(x)\) for \(i\ge1\). The Taft commutation relation evaluated at \(x\) becomes \(\zeta D(x)=\zeta\sigma(D(x))\). Hence \(D(x)\) lies in the invariant span of \(1,x^m,x^{2m},\ldots\). Conversely an invariant polynomial \(f\) determines a unique skew derivation of the polynomial ring. It descends to the quotient precisely when
\[
D(x^N)=[N]_{\zeta}x^{N-1}f=0\pmod{x^N}.
\]
Since \([N]_{\zeta}=0\) exactly when \(m\mid N\), this is equivalent to the asserted constant-term restriction. Each permitted \(f\) satisfies \(D(f)=0\), because \([am]_{\zeta}=0\) for all \(a\). Thus \(D\sigma=\zeta\sigma D\) extends from the generator to the entire algebra, and the displayed forms are exhaustive.

**2. Nilpotence.** From \(D(f)=0\), induction gives, whenever \(i\ge j\),
\[
D^j(x^i)=\left(\prod_{h=0}^{j-1}[i-h]_{\zeta}\right)x^{i-j}f^j.
\]
For \(i<j\), this is zero. Among any \(m\) consecutive integers one is divisible by \(m\), and \([i]_{\zeta}\) vanishes exactly for such integers. Therefore \(D^m=0\) on every monomial, without an additional polynomial restriction.

**3. All power ranks.** Write \(f=x^{ms}u(x^m)\), where \(u(0)\neq0\). For \(1\le j<m\), the scalar product in step 2 is nonzero exactly when \(i\bmod m\in\{j,\ldots,m-1\}\). In that case \(D^j(x^i)\) has lowest nonzero monomial degree \(i-j+jms\), and vanishes in \(A_N\) exactly when this degree is at least \(N\). Distinct eligible \(i\)'s give distinct lowest monomial degrees, so the corresponding images are linearly independent. Setting \(h=i-j\), the eligible values are precisely
\[
0\le h<N-jms,\qquad h\bmod m\in\{0,\ldots,m-j-1\}.
\]
Because \(N-jms=m(\ell-js)+r\), a division into complete residue blocks and a terminal remainder yields exactly \(\rho_j(s)\). This also proves the boundary case \(\ell<js\): then \(N-jms<0\) because \(0\le r<m\), and no monomial survives.

**4. Jordan and enumeration.** A nilpotent matrix with ranks \(\rho_j\) has the claimed second-difference Jordan multiplicities, from the identity that each block of length \(b\) contributes \(\max(b-j,0)\) to \(\rho_j\). For \(j=1\), \(s\le\ell\) for every permitted nonzero parameter, giving \(\rho_1=(m-1)(\ell-s)+r\), strictly decreasing in \(s\). Over \(\mathbb F_q\), the \(t\) invariant coefficients have one forced zero when \(r>0\); for each permitted \(s\), the leading coefficient has \(q-1\) choices, while the \(t-1-s\) higher coefficients are arbitrary. Summing their disjoint counts proves the rank polynomial and total count.

## Verification

Run `python checker.py` from the directory containing the standalone checker. The checker reconstructs the matrices from the skew-Leibniz rule, tests the relation and nilpotence, computes the ranks of all powers by elimination, and compares them against both the formulas and exact finite-field coefficient counts. Its deterministic suite exhausts **6,581 compatible parameter assignments across 55 finite settings** with prime fields \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11}\), orders \(m\in\{2,3,4,5,6\}\), and tested quotient lengths from \(2\) to \(12\) where the parameter-space bound applies. The expected terminal marker is `TAFT_JORDAN_VERIFIED`.

This is a finite independent check of examples; the universal claim rests on the proof, not the computation.

## Relationship to prior work

Montgomery and Schneider (2001), Lemma 2.1 and Theorem 2.2, explicitly classify skew derivations on \(m\)-dimensional algebras \(k[u]/(u^m-\beta)\), with order-\(m\) automorphism, including the \(N=m\) boundary of the present setting. Centrone and Yasumura (2020) give a general framework for Taft actions via gradings and skew derivations, including explicit treatments of upper-triangular matrix algebras. Their results motivate the fixed-scaling action, and are not presented as discoveries here. The assertion isolated here is the all-truncation, all-power Jordan-rank stratification and its exact finite-field multiplicity law, which the inspected cited statements do not directly provide. A stronger general classification elsewhere could subsume this specialization; no absolute priority claim is made.

## Limitations

The scaling automorphism is fixed; arbitrary Taft actions can have other group-like actions. The rank formula does not count isomorphism classes of Hopf module algebras. Some mathematical statements about equivalent \(q\)-differential modules may exist outside inspected and indexed sources. Primary literature inspection was strongest for the 2020 paper and the directly relevant 2001 theorem; this is not an independent publication-priority certification. No independent audit has been performed.

## References

- S. Montgomery and H.-J. Schneider, *Skew derivations of finite-dimensional algebras and actions of the double of the Taft Hopf algebra*, Tsukuba J. Math. 25 (2001), 337–358. https://doi.org/10.21099/tkbjm/1496164292 ; open text: https://tsukuba.repo.nii.ac.jp/record/17192/files/10.pdf
- L. Centrone and F. Yasumura, *Actions of Taft's algebras on finite dimensional algebras*, J. Algebra 560 (2020), 725–744, publicly online June 10, 2020. https://doi.org/10.1016/j.jalgebra.2020.06.007 ; open PDF: https://ricerca.uniba.it/retrieve/e0c74100-7ce3-4c5f-bc4e-34f517b31c27/action%20of%20Taft_s%20algebra.pdf
- Z. Cline, *On actions of Drinfel'd doubles on finite dimensional algebras*, first posted May 25, 2018, arXiv:1805.10340. https://arxiv.org/abs/1805.10340
- S. Crawford, J. Gaddis and R. Won, *Actions of Taft Algebras on Noetherian Down-Up Algebras*, first posted September 26, 2024, arXiv:2409.17890. https://arxiv.org/abs/2409.17890
