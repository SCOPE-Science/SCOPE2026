# Fourier-support and characteristic separation for finite-field Jordan-product graphs

## Finding

Let \(q\) be a prime power, \(n\ge2\), \(M=M_n(\mathbb F_q)\), and \(N=n^2\). The additive Jordan-product graph is
\[
\mathcal J_{n,q}=\{(X,Y,XY+YX):X,Y\in M\}\subset M^3.
\]
Write \(S_C(X)=CX+XC\), \(\nu(C)=\dim_{\mathbb F_q}\ker S_C\), and use the nondegenerate pairing \(\langle A,X\rangle=\operatorname{tr}(AX)\). For any nontrivial additive character \(\psi\), its unnormalized Fourier multiplier at \((A,B,C)\in M^3\) is nonzero **if and only if** \(A,B\in\operatorname{im}S_C\). More precisely, if \(S_C(X_0)=-B\) and both conditions hold, then
\[
\widehat{\mathbf 1_{\mathcal J}}(A,B,C)
=q^{N+\nu(C)}\psi(\operatorname{tr}(AX_0)).
\]
Therefore additive convolution \(T_{\mathcal J}\) on the \(q^{3N}\)-dimensional complex function space has singular values \(q^{N+j}\), with multiplicities
\[
\operatorname{mult}(q^{N+j})
=q^{2(N-j)}\#\{C\in M:\nu(C)=j\},\qquad 0\le j\le N;
\]
a zero singular value occupies all remaining dimensions. The following finite, explicit partition-product formula determines every multiplicity at arbitrary \(n,q\).

For a monic irreducible \(f\in\mathbb F_q[t]\), write \(d=\deg f\) and \(f^-(t)=(-1)^df(-t)\). For a partition \(\lambda\), let \(\lambda'_i\) be its column lengths, \(m_r(\lambda)\) its multiplicity of part \(r\), and put
\[
\begin{split}
\langle\lambda,\mu\rangle&=\sum_{i\ge1}\lambda'_i\mu'_i,\\
 c_d(\lambda)&=q^{d\langle\lambda,\lambda\rangle}
 \prod_{r\ge1}\prod_{i=1}^{m_r(\lambda)}(1-q^{-di}).
\end{split}
\]
The empty partition has denominator one. Partition the monic irreducibles into fixed points and two-cycles under \(f\mapsto f^-\). Define the formal power series
\[
\begin{split}
\mathcal Z_q(u,z)
={}&\prod_{\{f\}:f=f^-}
 \sum_{\lambda}\frac{u^{d|\lambda|}z^{d\langle\lambda,\lambda\rangle}}{c_d(\lambda)}\\
&\times\prod_{\{f,g\}:g=f^-\ne f}
 \sum_{\lambda,\mu}
 \frac{u^{d(|\lambda|+|\mu|)}z^{2d\langle\lambda,\mu\rangle}}{c_d(\lambda)c_d(\mu)}.
\end{split}
\]
Every coefficient in \(u\) is a finite computation, and
\[
\boxed{\displaystyle
\sum_{C\in M_n(\mathbb F_q)}z^{\nu(C)}
=|\mathrm{GL}_n(\mathbb F_q)|\,[u^n]\mathcal Z_q(u,z).}
\]
In particular, a fully explicit formula for convolution rank is
\[
\operatorname{rank}T_{\mathcal J}
=q^{2N}|\mathrm{GL}_n(\mathbb F_q)|
 [u^n]\mathcal Z_q(u,q^{-2}).
\]

The least positive singular value equals \(q^N\) when \(q\) is odd, and \(q^{N+n}\) when \(q\) is even. The largest is \(q^{2N}\) in both cases. Thus the **sharp** supported condition number is
\[
\boxed{\kappa^+(T_{\mathcal J})=
\begin{cases}q^{N},&q\text{ odd},\\q^{N-n},&q\text{ even}.\end{cases}}
\]
For each fixed \(n\), the Fourier-support density tends to one along odd prime powers \(q\to\infty\), but tends to zero along even prime powers. Quantitatively, the odd-characteristic density is at least \(1-N/q\); the even-characteristic density is at most \(q^{-2n}\).

For \(n=2\) and odd \(q\), the exact \(\nu(C)\)-strata are
\[
\begin{array}{c|cccc}
j&0&1&2&4\\\hline
\#\{C:\nu(C)=j\}&q^4-2q^3+q&q(q^2-1)&q^3-1&1.
\end{array}
\]
Consequently,
\[
\boxed{\operatorname{rank}T_{\mathcal J}
=(q^4-2q^3+q)q^8+q(q^2-1)q^6+(q^3-1)q^4+1.}
\]
For \(n=2\) and even \(q\), the corresponding strata have multiplicities \(q^4-q\) at \(j=2\) and \(q\) at \(j=4\), hence rank \(q+(q^4-q)q^4\). This even-characteristic part agrees with the commutator case because \(XY+YX=XY-YX\) there; it is included to make the characteristic separation exact, not asserted as a new commutator formula.

## Assumptions and scope

All matrices are over the finite field \(\mathbb F_q\), and \(n\ge2\). No parity, primality or genericity assumption is imposed except where the displayed characteristic-dependent formulas say so. Additive convolution is **unnormalized**: \((Tf)(g)=\sum_{h\in M^3}\mathbf1_{\mathcal J}(h)f(g-h)\). The Fourier transform uses a fixed nontrivial additive character and the nondegenerate trace pairing on each matrix factor. In characteristic two, "alternating" conventions for forms are not involved: \(S_C\) is simply the matrix anticommutator operator.

## Proof

**1. Exact Fourier support and phase.** Expand the Fourier sum and sum over \(Y\) first:
\[
\sum_{X,Y}\psi(\operatorname{tr}(AX+BY+CXY+CYX))
=q^N\sum_{X:S_C(X)=-B}\psi(\operatorname{tr}(AX)).
\]
This uses \(\operatorname{tr}(CXY+CYX)=\operatorname{tr}((CX+XC)Y)\) and additive-character orthogonality. The solution set, if nonempty, is \(X_0+\ker S_C\). The trace-adjoint identity
\(\operatorname{tr}(A S_C(X))=\operatorname{tr}(S_C(A)X)\)
shows \((\ker S_C)^\perp=\operatorname{im}S_C\). A second orthogonality sum proves the claimed necessary and sufficient support condition and multiplier. There are exactly \(q^{2(N-\nu(C))}\) supported pairs \((A,B)\) for each \(C\), proving all singular-value multiplicities and rank reduction.

**2. Nullity via primary modules.** Regard \(M\) as \(\operatorname{End}_{\mathbb F_q}(V)\) and let \(V_C\) be the \(\mathbb F_q[t]\)-module on which \(t\) acts by \(C\). Then
\[
\ker S_C=\{X:CX=X(-C)\}
\simeq\operatorname{Hom}_{\mathbb F_q[t]}(V_{-C},V_C).
\]
In the rational-canonical decomposition, a block \(\mathbb F_q[t]/(f^a)\) and one \(\mathbb F_q[t]/(g^b)\) have a Hom space of dimension \(d\min(a,b)\) precisely when \(f=g\) and \(d=\deg f\), and otherwise have zero Hom space. Applying this after \(f\mapsto f^-\) yields
\[
\nu(C)=\sum_f (\deg f)\langle\lambda_f,\lambda_{f^-}\rangle.
\]
For a pair of distinct involution orbits the two ordered contributions add to twice the cross pairing. For fixed irreducibles the contribution is the ordinary centralizer partition square.

**3. Exact spectral enumerator.** The centralizer group of a primary similarity class of partition \(\lambda\) and irreducible degree \(d\) has order \(c_d(\lambda)\). A rational-canonical collection of partitions therefore represents exactly \(|\mathrm{GL}_n|/\prod_f c_{\deg f}(\lambda_f)\) matrices. Grouping its \(z^{\nu(C)}\) weight over fixed and paired irreducible orbits gives the displayed bivariate product. At coefficient \(u^n\), only irreducibles of degree at most \(n\) and partitions of size at most \(n\) enter, so the formula is genuinely finite coefficientwise. It computes the support-weighted distribution, not merely the number of anticommuting matrix pairs.

**4. Extreme levels and characteristic separation.** When \(q\) is odd, \(C=I\) makes \(S_C=2I\), hence \(\nu(C)=0\). When \(q\) is even, \(S_C(X)=CX-XC\). Rational-canonical blocks imply \(\dim\ker S_C\ge n\), with equality for cyclic matrices. In both cases \(\nu(C)\le N\); it reaches \(N\) at \(C=0\). This proves the extremal singular values. In odd characteristic, \(\det S_C\) is a nonzero polynomial of total degree \(N\) in the \(N\) entries of \(C\) because it takes value \(2^N\) at \(I\). The finite-field zero estimate shows at most \(Nq^{N-1}\) singular \(S_C\)'s; every nonsingular one contributes all \(q^{2N}\) pairs of frequencies. In characteristic two, \(\nu(C)\ge n\) for all \(C\), giving the stated density upper bound. These estimates are meaningful for fixed \(n\), with no claim that the displayed lower bound is positive at small field size.

**5. The exact two-by-two census.** In odd characteristic, for \(C\ne0\), \(\nu(C)=2\) when \(\operatorname{tr}C=0\), \(\nu(C)=1\) when \(\det C=0\) but \(\operatorname{tr}C\ne0\), and \(\nu(C)=0\) otherwise. This follows by splitting into distinct eigenvalues, nonzero Jordan blocks, and the nilpotent Jordan block; equivalently \(\det S_C=4\det(C)(\operatorname{tr}C)^2\), with the kernel dimensions checked at each intersection. Exactly \(q^3-1\) nonzero matrices have trace zero. The matrices of rank one and nonzero trace number \(q(q^2-1)\), by counting presentations \(uv^{\mathsf T}\) with \(v^{\mathsf T}u\ne0\). The remaining nonzero matrices have \(\nu=0\), while \(C=0\) has \(\nu=4\). If \(q\) is even, \(S_C\) is a commutator and all nonscalar two-by-two matrices have centralizer dimension two, while all scalar ones have dimension four. Substitute these counts into the Fourier-support formula.

## Verification

The accompanying standard-library Python script `check_jordan_graph.py` independently builds each matrix operator \(S_C\), computes ranks by finite-field elimination, and compares the predicted singular-support counts in dimensions two and three. For field sizes \(q=2,3,4\) in dimension two, the kernel distributions match the stated closed formulas. It evaluates 36 direct Fourier character sums at each of \(q=2,3\), independently of the rank-only counts, and checks exact zeros and nonzero magnitudes. In dimension three, exhaustive kernel distributions at \(q=2\) and \(q=3\) are respectively \(\{3:412,5:98,9:2\}\) and \(\{0:7722,1:3510,2:5148,3:2730,4:468,5:104,9:1\}\). Run `python3 check_jordan_graph.py`; success ends in `ALL_JORDAN_GRAPH_TESTS_OK`. The finite checks are supplementary; the proof is algebraic for all prime powers and dimensions.

## Relationship to prior work

The rational-canonical and centralizer counting inputs are classical, as described by Rodriguez-Villegas and Britnell–Wildon. The geometry of anticommuting pairs and their block fibres has been treated by Chen–Wang; a 2021 mathematical discussion gives polynomial pair counts, a three-dimensional anticommutator-kernel census, and a pair-count Euler product. These results concern vanishing anticommutators or class enumerations. They are not claimed as new here. The subject here is the distinct Fourier multiplier at **all three independent frequency matrices**, its complete singular spectrum, the mixed-negative-primary partition product, and the odd/even spectral-support-density separation. A general bilinear-graph Fourier argument and the existing block tables are potential routes to portions of the result; no claim of absolute historical priority is made.

## Limitations

No independent mathematical review is represented. The theorem does not provide an elementary factored polynomial for the total convolution rank in each arbitrary dimension; instead, it provides a finite coefficient-extraction formula. The characteristic-dependent asymptotic statement holds for fixed dimension as the residue-field order increases. Historical coverage may extend beyond the accessible literature, especially through general bilinear graph or partition-enumerator results. The same-model correctness and originality conclusions are bounded assessments, not external certification.

## References

1. F. Rodriguez-Villegas, *Counting colorings on varieties*, arXiv:math/0612664v1, first publicly submitted 2006-12-21, https://arxiv.org/abs/math/0612664.
2. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811v1, first publicly submitted 2010-01-06, https://arxiv.org/abs/1001.0811.
3. X. Chen and W. Wang, *Anti-commuting varieties*, arXiv:1805.00378v1, first publicly submitted 2018-05-01, https://arxiv.org/abs/1805.00378.
4. Mathematical discussion, *Number of 3 by 3 anticommuting matrices over finite fields*, MathOverflow question 404817 and answers posted 2021-09-26 and 2021-10-09, https://mathoverflow.net/questions/404817/.
