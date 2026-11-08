# Second-order boundary–bulk covariance cancellation in uniform Motzkin paths

## Finding

Let a Motzkin path of length \(n\) be chosen uniformly from all paths with steps \(U=(1,1)\), \(D=(1,-1)\), and \(H=(1,0)\), beginning and ending at height zero and never going below zero. Write \(R_n\) for its number of horizontal steps **at height zero**, \(P_n\) for the number of occurrences of the **consecutive pair** \(UD\) at any height (sharp peaks), and \(H_n\) for its total number of horizontal steps. Then

\[
\boxed{\operatorname{Cov}(R_n,P_n)=-\frac{1}{n}+O(n^{-2}),\qquad \operatorname{Cov}(R_n,H_n)=2+O(n^{-1})}\qquad(n\to\infty).
\]

In particular, the first covariance is eventually strictly negative although its leading order and order-one asymptotic terms both vanish. By contrast, dependence on the total number of steps of the same horizontal type persists at positive order one. These assertions concern distinct statistics on the **same uniformly sampled path**.

## Assumptions and scope

The length \(n\) is an integer tending to infinity. No special weighting or independent-step approximation is used. Both covariances are ordinary centered covariances under the uniform probability measure on the \(n\)-th Motzkin family. The result gives the first nonzero asymptotic for the mixed ground-horizontal/sharp-peak covariance and a comparison covariance; it does not claim finite-length negativity for every \(n\) or any central limit theorem.

## Proof

Let \(M(z,w,v)\) mark path length by \(z\), all horizontal steps by \(w\), and strict \(UD\) pairs by \(v\). The first-return decomposition of a nonempty Motzkin path into either \(H\) followed by a path, or \(U\), an interior path, \(D\), and a following path, gives

\[
M=1+wzM+z^2(M+v-1)M.
\]

Indeed, the marked first-return block is a sharp peak precisely when its interior is empty, so its interior factor is \(M+v-1\). To mark **only height-zero** horizontal steps, introduce a variable \(u\), and let \(F(z,u,w,v)\) be the corresponding full series. Every path is a sequence of first-return blocks and ground-level horizontal steps, hence

\[
F=\frac{1}{1-uwz-z^2(M+v-1)}
 =\frac{M}{1-(u-1)wzM}.
\]

Here \(M\) in the last fraction retains the arguments \((z,w,v)\). Put \(M=M(z,1,1)\) and \(\Delta=(1-3z)(1+z)\). Solving the quadratic and differentiating gives

\[
M=\frac{1-z-\sqrt{\Delta}}{2z^2},\qquad
M_v\big|_{w=v=1}=\frac{z^2M}{\sqrt\Delta},\qquad
M_w\big|_{w=v=1}=\frac{zM}{\sqrt\Delta}.
\]

Subscripts denote ordinary partial derivatives. The coefficient series for the six unnormalized expectations are therefore

\[
\begin{array}{c|l}
\text{sum over paths} & \text{ordinary generating function} \\
1&M\\
R_n&zM^2\\
P_n&z^2M/\sqrt\Delta\\
R_nP_n&2z^3M^2/\sqrt\Delta\\
H_n&zM/\sqrt\Delta\\
R_nH_n&zM^2+2z^2M^2/\sqrt\Delta.
\end{array}
\]

For each row \(X\), let \(S_{X,n}\) be the coefficient of its displayed generating function. All moments are \(S_{X,n}/S_{1,n}\); in particular \(S_{1,n}\) is the \(n\)-th Motzkin number.

We now extract coefficients at the unique dominant singularity \(z=1/3\). Set \(t=\sqrt{1-3z}\). The other radical singularity \(z=-1\) has strictly larger modulus. For fixed nonintegral \(\alpha\), transfer of a power singularity, as follows from the gamma ratio and Stirling's expansion, gives

\[
[z^n](1-3z)^\alpha
=\frac{3^n n^{-\alpha-1}}{\Gamma(-\alpha)}
\left(1+\frac{\alpha(\alpha+1)}{2n}
+\frac{\alpha(\alpha+1)(\alpha+2)(3\alpha+1)}{24n^2}
+O(n^{-3})\right).
\]

Terms analytic at \(1/3\) contribute no comparable algebraic-power corrections, and the next omitted half-integer power gives the stated error. Combining this transfer with the Laurent expansions in \(t\) yields the exact table below. The table entry \((a,b,c)\) means \(S_{X,n}=3^n a n^{-q}/\sqrt\pi\,(1+b/n+c/n^2+O(n^{-3}))\), where \(q=3/2\) in the first two rows and \(q=1/2\) in the remaining rows.

| \(X\) | \(a\) | \(b\) | \(c\) |
|---|---|---|---|
| \(1\) | \(3\sqrt3/2\) | \(-39/16\) | \(2665/512\) |
| \(R\) | \(3\sqrt3\) | \(-75/16\) | \(8785/512\) |
| \(P\) | \(\sqrt3/6\) | \(-7/16\) | \(-23/512\) |
| \(RP\) | \(\sqrt3/3\) | \(-43/16\) | \(1489/512\) |
| \(H\) | \(\sqrt3/2\) | \(-15/16\) | \(505/512\) |
| \(RH\) | \(\sqrt3\) | \(-3/16\) | \(-3455/512\) |

In particular, the quotient expansions give

\[
\begin{split}
\mathbb E R_n&=2-\frac{9}{2n}+O(n^{-2}),\\
\mathbb E P_n&=\frac n9+\frac29+O(n^{-1}),\\
\mathbb E H_n&=\frac n3+\frac12+O(n^{-1}),\\
\mathbb E(R_nP_n)&=\frac{2n}{9}-\frac1{18}+O(n^{-1}),\\
\mathbb E(R_nH_n)&=\frac{2n}{3}+\frac32+O(n^{-1}).
\end{split}
\]

The leading \(n\) and constant terms in \(\mathbb E(R_nP_n)-\mathbb E R_n\,\mathbb E P_n\) cancel **exactly**. Keeping the complete second correction \(c/n^2\) in all the relevant rows, the coefficient of \(1/n\) in this difference simplifies to \(-1\). In the horizontal comparison the constant is instead \(3/2-(-1/2)=2\), proving both assertions with the quoted remainders. The exact cancellation, including the \(-1\) coefficient, is verified by rational symbolic arithmetic in the accompanying checker.

## Verification

Run `python3 verify_motzkin.py` with Python 3 and SymPy available. The checker independently enumerates every Motzkin path through length 12 and compares six moment sums with recursive generating-function coefficients; it then checks 250 exact integer-coefficient recurrences, a formal singular-expansion coefficient table, and the two rationally simplified covariance constants. In the supplied execution all **1,106 assertions** passed. For \(n=250\), the exact finite covariance computations give \(n\operatorname{Cov}(R_n,P_n)\approx-0.99306922\) and \(\operatorname{Cov}(R_n,H_n)\approx1.97628161\). Finite computations are corroboration; the proof of the asymptotic is the generating-function and transfer argument above.

## Relationship to prior work

Sapounakis and Tsikouras (2005) enumerate Motzkin peaks and height-resolved peak statistics, supplying the classical first-return context but not the mixed ground-horizontal/strict-sharp-peak covariance or its \(-1/n\) cancellation. Brennan and Mavhungu (2010) analyze mean Motzkin sharp peaks and low peaks; their accessible author-upload text and abstract establish a close thematic match, although a complete independent comparison with that article was not possible. Ding and Du (2011) count humps \(UH^*D\), a related but distinct statistic, not a mixed covariance with ground-level horizontals. Oste and Van der Jeugt (2015) enumerate horizontal steps by level: their polynomial contains the marginal ground-horizontal and total-horizontal information, so the comparison covariance is **not presented as novel by itself**. Its commuting height-weight polynomial does not track adjacency \(UD\), which is indispensable for the surviving sharp mixed-covariance term. The same paper notes a noncommuting word enumerator which could in principle be processed to recover any finite pattern count; it does not give the mixed covariance or its singular asymptotics. A general continued-fraction or multivariate transfer framework might yield this value after additional specialization, and priority from such an implicit derivation is not excluded.

## Limitations

The result is asymptotic and does not assert finite-size sign for every admissible length; the leading negative term ensures negativity for all sufficiently large lengths. The \(O(n^{-2})\) remainder is not optimized beyond its order. A direct all-literature priority guarantee is impossible: the 2010 sharp-peak paper was accessible in part, and earlier broad enumerations or general simply-generated-tree limit methods may implicitly recover the constant. The exact second-order coefficient is a consequence of the displayed finite generating functions but is not an independent generic covariance theorem for other excursion models. No independent audit is claimed.

## References

1. A. Sapounakis and P. Tsikouras, *Counting peaks and valleys in \(k\)-colored Motzkin paths*, Electronic Journal of Combinatorics **12** (2005), R16. Published 2005-03-18. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v12i1r16/pdf/
2. C. Brennan and S. Mavhungu, *Peaks and Valleys in Motzkin Paths*, Quaestiones Mathematicae **33** (2010), 171–188. https://doi.org/10.2989/16073606.2010.491177
3. Y. Ding and R. R. X. Du, *Counting Humps in Motzkin paths*, 2011 preprint. https://arxiv.org/abs/1109.2661
4. R. Oste and J. Van der Jeugt, *Motzkin paths, Motzkin polynomials and recurrence relations*, Electronic Journal of Combinatorics **22** (2015), P2.8. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v22i2p8/pdf
