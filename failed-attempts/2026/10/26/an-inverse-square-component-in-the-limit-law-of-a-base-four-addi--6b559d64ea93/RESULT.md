# An inverse-square component in the limit law of a base-four additive complement

## Finding

Let
\[
A=\left\{\sum_{j\geq0}\epsilon_j4^j:\epsilon_j\in\{0,1\},\text{ finitely many nonzero}\right\},\qquad B=2A,
\]
and let \(A(n)=\#(A\cap[0,n])\), \(B(n)=\#(B\cap[0,n])\). Every nonnegative integer has exactly one representation as an element of \(A\) plus an element of \(B\). For an integer \(k\geq1\), choose \(J_k\) uniformly from \(\{1,\ldots,4^k\}\), and put
\[
R_k=\frac{A(J_k)B(J_k)}{J_k}.
\]
Independently, let \((\epsilon_j)_{j\geq1}\) be independent fair binary variables,
\[
S=\sum_{j=1}^{\infty}\epsilon_j4^{-j},\quad F(u)=\Pr(S\leq u),\quad G(u)=F(u/2),
\quad U\sim\operatorname{Unif}(0,1),\quad H=\frac{F(U)G(U)}{U}.
\]

**Theorem.** With the probability measures on the real line equipped with their \(1\)-Wasserstein metric, one has
\[
W_1\big(\mathcal L(R_k),\mathcal L(H)\big)=O(k2^{-k}).
\]
The law of \(H\) is absolutely continuous, has support exactly \([1,3/2]\), and contains the following **explicit subprobability component of mass \(2/3\)**:
\[
\boxed{\quad 2t^{-2}\mathbf 1_{(1,3/2)}(t)\,dt.\quad}
\]
Equivalently its density is at least \(2/t^2\) almost everywhere on \((1,3/2)\), and its remaining mass is exactly \(1/3\), also absolutely continuous.

A complete density and an effectively approximable distribution function are available. Let
\[
C=\left\{\sum_{j=1}^{\infty}\epsilon_j4^{-j}:\epsilon_j\in\{0,1\}\right\},
\quad\mathcal G=\{(a,b): (a,b)\text{ is a connected-component gap of }(0,1)\setminus(C\cup2C)\}.
\]
For each gap \(I=(a,b)\), the two Cantor distribution functions are constant on \(I\); write \(c_I=F(a)G(a)>0\). An exact version of the law is
\[
\boxed{\quad f_H(t)=\frac1{t^2}\sum_{I=(a,b)\in\mathcal G}
 c_I\,\mathbf1_{(c_I/b,c_I/a)}(t),\qquad t>0,\quad}
\]
interpreted almost everywhere. For every integer \(L\geq1\) and \(t>0\), there is an explicitly rational, depth-\(L\) number \(P_L(t)\) (when \(t\) is rational) such that
\[
\boxed{\quad 0\leq\Pr(H\leq t)-P_L(t)\leq2^{-L}.\quad}
\]
All formulas concern this particular standard digit complement. No claim is made for arbitrary additive-complement pairs.

## Assumptions and scope

All sets contain \(0\); counting functions count \(0\). The uniform random choice includes \(4^k\) itself. Distribution functions \(F,G\) refer to the continuous Bernoulli Cantor measures on \(C\) and \(2C\). Endpoint values of the density are immaterial. The error constant in the Wasserstein estimate is absolute. The precise \(1\)-Wasserstein distance is \(\inf\mathbb E|X-Y|\) over couplings of the two real probability laws.

The source motivating the counting-ratio question is Yang and Zhao, *On additive complements in natural numbers*, arXiv:2609.13900v1, posted 2026-09-12, with primary MSC2020 including \(11B13\). The digit construction and sharp \(3/2\) extremum are previously known; **only the distributional theorem, inverse-square subcomponent, and quantitative/certified CDF statements are advanced here**.

## Proof

**1. Unique sums and finite counting measures.** In base four each digit \(0,1,2,3\) has a unique decomposition as a digit in \(\{0,1\}\) and a digit in \(\{0,2\}\), without carry. Hence \(A+B=\mathbb Z_{\geq0}\) uniquely. Fix \(k\), set \(N=4^k\), and define the finite random sums
\[
S_k=\sum_{j=1}^k\epsilon_j4^{-j},\quad
F_k(u)=\Pr(S_k\leq u),\quad G_k(u)=\Pr(2S_k\leq u).
\]
For integer \(1\leq n<N\), direct order-preserving reversal of the \(k\) binary digits yields
\[
\frac{A(n)}{2^k}=F_k(n/N),\qquad\frac{B(n)}{2^k}=G_k(n/N).
\]
For \(n=N\), the first equality has an extra \(2^{-k}\) from the newly available element \(N\), while the second still holds. Thus the normalized counting functions differ by at most \(2^{-k}\) from these finite CDFs at all sampling points.

**2. Uniform Cantor approximation.** The tail of \(S-S_k\) belongs to \([0,4^{-k}/3]\). Adjacent distinct values of \(S_k\) are separated by at least \(4^{-k}\); their atoms have mass \(2^{-k}\). The interval where \(S_k\leq u<S\) therefore contains at most one such atom, giving
\[
0\leq F_k(u)-F(u)\leq2^{-k},\qquad
0\leq G_k(u)-G(u)\leq2^{-k}.
\]
The analogous statement for \(2S_k\) uses its tail bound \(2\cdot4^{-k}/3\) and atom spacing at least \(2\cdot4^{-k}\). The mass of either Cantor measure in any interval of length \(N^{-1}\) is at most \(2\cdot2^{-k}\), since the interval meets at most two level-\(k\) prefix-cylinder supports (and each has mass \(2^{-k}\)).

**3. Quantitative coupling.** Couple \(J_k=\lceil NU\rceil\) with uniform \(U\), and put \(x=J_k/N\). The preceding estimates give, for an absolute constant \(C\),
\[
\left|\frac{A(J_k)}{2^k}-F(U)\right|
+\left|\frac{B(J_k)}{2^k}-G(U)\right|\leq C2^{-k}.
\]
Using \(0\leq F,G\leq1\) and \(x\geq U\), we obtain
\[
\left|R_k-\frac{F(U)G(U)}U\right|
\leq \frac{C'2^{-k}}x+H\frac{x-U}{x}.
\]
Here \(H\) is bounded, as shown in step 4 below. Since \(\mathbb E(1/x)=\sum_{j=1}^N1/j\) and
\(\mathbb E((x-U)/x)=\frac1{2N}\sum_{j=1}^N1/j\), taking expectations proves the stated \(O(k2^{-k})\) bound for the exhibited coupling and hence for \(W_1\).

**4. Exact support bound.** Unique addition implies \(A(n)B(n)\geq n+1\). To bound above, index the first \(2^k\) members of \(A\) by
\(a_v=\sum_{j\geq0}\epsilon_j4^j\), where \(v=\sum_{j\geq0}\epsilon_j2^j\) and \(0\leq v<2^k\). The elementary digit inequality
\[
v^2\leq3a_v
\]
follows by induction on the highest occupied binary position: if \(v=2^j+w\) with \(0\leq w<2^j\), then \(v^2\leq3\cdot4^j+w^2\leq3(4^j+a_w)\). In the block \([4^k,4^{k+1})\), each increase in \(A(n)B(n)\) occurs at \(n=4^k+a_v\) or \(n=2(4^k+a_v)\), and the ratio at either such point is
\[
\frac{2^k(2^k+v+1)}{4^k+a_v}
\leq\frac{2^k(2^k+v)}{4^k+v^2/3}+2^{-k}
\leq\frac32+2^{-k}.
\]
The middle bound uses \(4^k+a_v\geq4^k\); the last uses \(\frac32(4^k+v^2/3)-2^k(2^k+v)=(2^k-v)^2/2\geq0\). Between successive increases the numerator is fixed and the ratio decreases. Thus \(R(n)\in[1,3/2+o(1)]\) as \(n\to\infty\); by step 2, \(1\leq F(u)G(u)/u\leq3/2\) for every \(0<u\leq1\). In particular \(H\) is bounded, completing the step-3 justification.

**5. Absolutely continuous gap formula.** The compact sets \(C\) and \(2C\) are Lebesgue null: their depth-\(L\) cylinder covers have total lengths at most \(1/(3\cdot2^L)\) and \(2/(3\cdot2^L)\), respectively. Thus the complement of their union occupies full measure in \((0,1)\) and is the countable union of disjoint open gaps \(I=(a,b)\). On each such gap, \(F\) and \(G\) are constant, with strictly positive product \(c_I\). The change of variables \(t=c_I/u\) from the uniform variable \(u\in(a,b)\) has density \(c_I/t^2\) on \((c_I/b,c_I/a)\). Summing over the gaps proves the exact density formula and shows that there is no atom or singular part.

**6. Two explicit gap families.** For every \(j\geq0\), direct inspection of the Cantor digits gives the disjoint gaps
\[
I_j^{(1)}=\left(\frac{4^{-j}}3,\frac{4^{-j}}2\right),\qquad
I_j^{(2)}=\left(\frac{2\cdot4^{-j}}3,4^{-j}\right).
\]
Their products are respectively \(c_{I_j^{(1)}}=4^{-j}/2\) and \(c_{I_j^{(2)}}=4^{-j}\). Each maps under \(u\mapsto c_I/u\) onto the **entire** interval \((1,3/2)\). Their combined density is therefore
\[
\frac1{t^2}\sum_{j=0}^{\infty}\left(\frac{4^{-j}}2+4^{-j}\right)
=\frac2{t^2},\quad 1<t<\frac32.
\]
Their total original-interval length is \(\sum_{j\geq0}\left(4^{-j}/6+4^{-j}/3\right)=2/3\). Every remaining gap gives an absolutely continuous positive contribution, hence the law has the asserted subcomponent and exactly \(1/3\) remaining mass. Because this component already has strictly positive density on all of \((1,3/2)\), the topological support is exactly \([1,3/2]\).

**7. Exact CDF enclosure.** At level \(L\), write every \(L\)-digit nonnegative prefix as \(a/4^L\), where \(a=\sum_{j=0}^{L-1}\epsilon_j4^j\). Cover \(C\) by intervals
\([a/4^L,(a+1/3)/4^L]\) and cover \(2C\) by intervals \([2a/4^L,(2a+2/3)/4^L]\). Let \(\mathcal G_L\) be the gaps of their finite union within \((0,1)\). Every member is an actual gap of \(C\cup2C\). Its constant \(c_I\) is rational and obtained by counting the level-\(L\) cylinders entirely to its left. Define
\[
P_L(t)=\sum_{I=(a,b)\in\mathcal G_L}
 \big(b-\max\{a,c_I/t\}\big)_+,
\quad z_+=\max\{z,0\}.
\]
The omitted subset lies inside the covering cylinders, whose total lengths are at most \(2^{-L}\). Its contribution to any event \(\{H\leq t\}\) lies between zero and \(2^{-L}\). This proves the uniform certified CDF enclosure.

## Verification

The standalone `verify.py` implements exact integer enumeration of the digit complements through \(4^6\), checks uniqueness of representations and the lower product inequality, reconstructs rational endpoints and CDF bounds of all depth-\(L\) Cantor gaps for \(1\leq L\leq8\), and checks the two explicit gap families at each depth. It uses exact `Fraction` arithmetic. Execution produced:

`VERIFY_OK unique_representation=4096_at_depth6 exact_macro_gaps=all_depths_1_to_8`

At depth eight, exact rational lower/upper CDF enclosures are: at \(t=11/10\), \([134349/720896,102871/540672]\); at \(t=5/4\), \([85037/163840,514057/983040]\); and at \(t=7/5\), \([406125/458752,19121/21504]\). These numerical intervals follow from the exact rational gap computation and the proved omitted-area bound, not from Monte Carlo sampling. The infinite limiting and absolute-continuity claims depend on the mathematical argument above, not finite enumeration.

## Relationship to prior work

Yang–Zhao (2026, arXiv:2609.13900v1) studies universal limsup conditions for counting products of additive complements, proving a \(4/3\) threshold. Chen–Fang (2011) establishes existence of examples with upper ratio \(3/2\) and repeated small excess; Ma (2022, arXiv:2205.04128v1) treats flexible digit constructions and upper ratios. Zhang (arXiv:2610.29963v1, posted 2026-10-21) explicitly analyzes this very base-four digit pair and proves its upper limit is \(3/2\), including a direct finite-digit inequality. Those known results establish the example and its extremal ratio; **they do not state the distributional identity, inverse-square density contribution of mass \(2/3\), Wasserstein rate, or gap-based certified CDF** established here. The elementary digit inequality in step 4 is a reconstruction of known sharpness reasoning, not a claimed novelty.

The formula is a consequence of the full gap decomposition and cannot be deduced from a limsup value alone. A broad result on additive tilings or Cantor distribution functions could nevertheless already imply part or all of this theorem without using the same terminology. The complete 2011 Chen–Fang paper could not be inspected, and independent priority verification remains outstanding.

## Limitations

The theorem treats the specific pair \(A,2A\); it does not characterize the laws of general additive complements, supply an elementary closed formula for the entire residual density of mass \(1/3\), or assert a central limit theorem. The series representation is exact and the CDF approximations have a uniform error certificate, but efficient complexity bounds for arbitrary requested precision are not optimized.

## References

1. Q.-H. Yang and L. Zhao, *On additive complements in natural numbers*, arXiv:2609.13900v1 (first posted 2026-09-12), https://arxiv.org/abs/2609.13900.
2. Y.-G. Chen and J.-H. Fang, *On additive complements, II*, Proc. Amer. Math. Soc. 139 (2011), 881–883, DOI:10.1090/S0002-9939-2010-10652-4. Full text not inspected.
3. F.-Y. Ma, *A Note on Additive Complements*, arXiv:2205.04128v1 (2022), https://arxiv.org/abs/2205.04128.
4. Z. Zhang, *A Sharp Bound for Additive Complements*, arXiv:2610.29963v1 (first posted 2026-10-21), https://arxiv.org/abs/2610.29963. This later paper is cited for its known digit-sharpness proof, not for source eligibility or the new distributional conclusion.
