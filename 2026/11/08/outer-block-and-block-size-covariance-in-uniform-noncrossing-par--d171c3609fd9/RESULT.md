# Outer-block and block-size covariance in uniform noncrossing partitions

## Finding

For a uniformly random noncrossing partition of \([n]=\{1,\ldots,n\}\), let \(R_n\) denote the number of outer blocks and \(C_{n,r}\) the number of blocks of size \(r\). For every integer \(n\ge2\) and \(1\le r\le n\), define
\[
\mathrm{Cat}_n=\frac1{n+1}\binom{2n}{n},\qquad
M_{n,r}=\binom{2n-r-1}{n-r}.
\]
The exact mixed moment and covariance are
\[
\mathbb E[R_n C_{n,r}]=\frac{M_{n,r}}{\mathrm{Cat}_n}\left(3-\frac{2r}{n}\right),
\]
\[
\boxed{\operatorname{Cov}(R_n,C_{n,r})=
\frac{M_{n,r}}{\mathrm{Cat}_n}\,
\frac{2\bigl(3n-r(n+2)\bigr)}{n(n+2)}.}
\]
Thus the covariance is strictly positive for \(r=1\); for \(r=2\) it is negative when \(n=2,3\), zero when \(n=4\), and strictly positive when \(n\ge5\); for every feasible \(r\ge3\) it is strictly negative. These are all equality cases. In particular, for fixed \(r\ne3\),
\[
\operatorname{Cov}(R_n,C_{n,r})\longrightarrow\frac{3-r}{2^r},
\]
and the borderline case has the distinct scale
\[
 n\operatorname{Cov}(R_n,C_{n,3})\longrightarrow-\frac34.
\]
Equivalently, under the size-biased law that chooses a random partition together with a distinguished block of size \(r\), the expected number of outer blocks is exactly \(3-2r/n\). The size bias is by \(C_{n,r}\), not by the size of a uniformly chosen block.

## Assumptions and scope

A set partition is noncrossing if no two different blocks contain \(a<c\) and \(b<d\), respectively, with \(a<b<c<d\). A block \(B\) is *inner* if another block \(A\) has \(\min A<\min B\le\max B<\max A\); a block not inner is *outer*. For noncrossing partitions this is equivalent to the usual nesting definition. All Catalan objects are sampled equiprobably, without conditioning on their total number of blocks. The claim is finite-sample and includes all feasible cardinalities; no independence or distributional limit is asserted.

## Proof

Mark each size-\(r\) block by a variable \(u\), so the weight of a block of cardinality \(k\) is \(w_k(u)=u\) for \(k=r\) and \(1\) otherwise. Let \(C(z,u)\) be the ordinary generating function of these weighted noncrossing partitions, including the empty partition. The standard initial-block decomposition gives, as formal power series,
\[
 C(z,u)=1+\sum_{k\ge1}w_k(u)\bigl(zC(z,u)\bigr)^k
 =\frac1{1-zC(z,u)}+(u-1)\bigl(zC(z,u)\bigr)^r.
\tag{1}
\]
An *irreducible* noncrossing partition has its least and greatest labels in the same block. Its generating function is
\[
 I(z,u)=\sum_{k\ge1}w_k(u)z^k C(z,u)^{k-1}
 =1-\frac1{C(z,u)}.
\]
Every noncrossing partition is uniquely a sequence of irreducible components, one for each outer block. Hence, on marking outer blocks by \(s\), its bivariate generating function is
\[
 F(z;s,u)=\frac1{1-sI(z,u)}.
\tag{2}
\]
This identity distinguishes the outer-block statistic from the total block count.

At \(u=1\), put \(C(z)=C(z,1)\) and \(t=zC(z)\). Then \(C(z)=1+zC(z)^2\), so \(z=t(1-t)\) and \(C=1/(1-t)\). Implicit differentiation of (1), with \(s=u=1\) after differentiation, yields
\[
 C_u(z,1)=\frac{t^r(1-t)}{1-2t},
 \qquad F_s(z;1,1)=C^2-C=zC^3,
\]
\[
 F_{su}(z;1,1)=(2C-1)C_u(z,1)
 =\frac{t^r(1+t)}{1-2t}.
\tag{3}
\]
All manipulations hold in formal series around the origin; \(1-2t\) is invertible there. Residue change of variable \(z=t(1-t)\), \(dz=(1-2t)\,dt\), gives
\[
 [z^n]C_u(z,1)
 =[t^{n-r}](1-t)^{-n}=M_{n,r},
\tag{4}
\]
\[
\begin{aligned}
 [z^n]F_{su}(z;1,1)
 &=[t^{n-r}](1+t)(1-t)^{-n-1}\\
 &=\binom{2n-r}{n-r}+\binom{2n-r-1}{n-r-1}
 =\frac{3n-2r}{n}M_{n,r}.
\end{aligned}
\tag{5}
\]
The same Catalan coefficient formula, or Lagrange inversion applied to \(C=1+zC^2\), gives
\[
 [z^n]F_s(z;1,1)=[z^{n-1}]C^3
 =\frac{3n}{n+2}\,\mathrm{Cat}_n.
\tag{6}
\]
Because \([z^n]C(z,1)=\mathrm{Cat}_n\), equations (4), (5), and (6) give \(\mathbb E[C_{n,r}]=M_{n,r}/\mathrm{Cat}_n\), \(\mathbb E[R_n]=3n/(n+2)\), and the stated mixed moment. Subtracting the product of expectations proves the displayed covariance formula.

Its prefactor \(M_{n,r}/\mathrm{Cat}_n\) is strictly positive, so the sign is precisely that of \(3n-r(n+2)\). For \(r=1\) it equals \(2n-2>0\); for \(r=2\) it equals \(n-4\); and for \(r\ge3\) it is strictly negative. This proves every finite-size assertion without finite enumeration. For each fixed \(r\), factorial ratios yield \(M_{n,r}/\mathrm{Cat}_n\sim n/2^{r+1}\). Substitution proves the displayed limits; when \(r=3\) the sign factor is exactly \(-6\), and the extra factor of \(n\) yields the limit \(-3/4\).

## Verification

A standalone standard-library Python program, `verify.py`, generates every set partition by restricted-growth strings, checks noncrossing by forbidden interlacing, and counts outer and size-\(r\) blocks independently. It exhaustively verifies the Catalan counts, all three moment identities, the covariance, and signs for every feasible \((n,r)\) through \(n=9\), enumerating \(4862\) noncrossing partitions at that largest size. Additional floating-point diagnostics check the stated fixed-size limits over selected sizes through \(n=1100\). It passed \(263\) exact equalities/sign checks and bounded asymptotic diagnostics in total. These checks corroborate the formal proof but do not replace it. Reproduce with `python3 verify.py`.

## Relationship to prior work

Bergerson, Miller, Pliml, Reiner, Shearer, Stanton and Switala (2011) counted noncrossing partitions with one distinguished size-\(r\) block, yielding \(M_{n,r}\) and a refinement by the **total** number of blocks. Arizmendi (2012) develops related block-size enumeration. Li (2014 repository release; thesis dated 2013) derives the **marginal outer-block law** and explicitly poses the broader joint size-resolved outer/total block problem (Question 5.1.3). Kortchemski and Marzouk (2015) develop a tree representation and general weighted models. Kargin (2019) studies covariance **between size-class counts**, not covariance with the number of outer components. A separate published result on covariance between block-size count and the **total** number of blocks in **unrestricted set partitions** uses a different ensemble and statistic. The present finite outer-block cross-moment and complete sign classification are not asserted in the inspected comparisons. Broad tree generating-function methods could imply the result without stating it; absence of a matching search result is not proof of mathematical priority.

## Limitations

The result does not give the full joint distribution or a multivariate limit theorem for all outer and inner size counts. Fixed-size asymptotics do not imply uniformity for \(r\) growing with \(n\). Existing enumerative generating functions and general ordered-tree formulas may encode the covariance implicitly; priority requires further specialist inspection. Computational checks are exhaustive only through \(n=9\).

## References

- M. Bergerson, A. Miller, A. Pliml, V. Reiner, P. Shearer, D. Stanton and N. Switala, *Note on 1-Crossing Partitions*, Ars Combinatoria 99 (2011), 83–87. Public article dated 2011-04-30. https://combinatorialpress.com/article/ars/Volume%2099/volume-99-paper-9.pdf
- O. Arizmendi, *Statistics of blocks in k-divisible non-crossing partitions*, arXiv:1201.6576 (initial posting 2012-01-31). https://arxiv.org/abs/1201.6576
- B. Li, *Asymptotic Distributions for Block Statistics on Non-crossing Partitions*, University of Waterloo thesis (2013), public repository record dated 2014-01-23. https://uwspace.uwaterloo.ca/items/feaced88-b45e-42c7-9e48-33938562f7c9
- I. Kortchemski and C. Marzouk, *Simply generated non-crossing partitions*, arXiv:1503.09174 (2015-03-31). https://arxiv.org/abs/1503.09174
- V. Kargin, *Limit theorems for statistics of non-crossing partitions*, arXiv:1907.00632 (2019-07-01). https://arxiv.org/abs/1907.00632
