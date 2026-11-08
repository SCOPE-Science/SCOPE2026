# Joint ternary valuations of central and threefold binomial coefficients

## Finding

For each integer \(r\geq0\) and \(0\leq n<3^r\), let
\[
X(n)=\nu_3\!\left(\binom{2n}{n}\right),\qquad
Y(n)=\nu_3\!\left(\binom{3n}{n}\right),
\qquad P_r(u,v)=\sum_{n=0}^{3^r-1}u^{X(n)}v^{Y(n)}.
\]
Then the **entire joint distribution**, at every ternary depth, is specified by
\[
\boxed{\sum_{r\geq0} P_r(u,v)z^r=
\frac{1-uz}{1-(1+u)(1+v)z+u(1+v+v^2)z^2}.}
\]
Equivalently, \(P_0=1\), \(P_1=1+v+uv\), and for every \(r\geq0\),
\[
P_{r+2}=(1+u)(1+v)P_{r+1}-u(1+v+v^2)P_r.
\]
For \(r\geq1\), the pairs \((X(n),Y(n))\) attained are **exactly**
\[
\{(0,j):0\leq j\leq r\}\ \cup\
\{(i,j):1\leq i,j\leq r\};
\]
there are \(r^2+r+1\) such pairs. Each coefficient in the joint polynomial is positive on that set and zero outside it.

For uniformly sampled \(n\in\{0,\ldots,3^r-1\}\), put \(t=3^{-r}\). The exact moments are
\[
\begin{aligned}
\mathbb EX&=\frac r2-\frac{1-t}{4}, & \mathbb EY&=\frac r2+\frac{1-t}{4},\\
\operatorname{Var}(X)&=\frac r2-\frac7{16}+\frac t2-\frac{t^2}{16},&
\operatorname{Var}(Y)&=\frac r6+\frac{1-t^2}{16},\\
\operatorname{Cov}(X,Y)&=\frac{(1-t)(3-t)}{16}.
\end{aligned}
\]
Thus the covariance is **positive at every positive depth but stays bounded**, tending to \(3/16\), while each variance grows linearly. In fact,
\[
\left(\frac{X-r/2}{\sqrt r},\frac{Y-r/2}{\sqrt r}\right)
\ \xrightarrow{\ d\ }\ \mathcal N\!\left(0,\begin{pmatrix}\tfrac12&0\\0&\tfrac16\end{pmatrix}\right).
\]
Consequently the Gaussian limits are independent even though the finite-depth valuations have positive covariance.

## Assumptions and scope

Here \(\nu_3\) denotes the exponent of three dividing a positive integer, the binomial coefficients are ordinary integer coefficients, \(r\) ranges over **all** nonnegative integers, and zero is included as an index. The generating function is a formal series in \(z\) with coefficients in \(\mathbb Z[u,v]\). The distributional limit is taken with respect to uniform counting measure on the indicated ternary interval. The case \(r=0\) is one index \(n=0\) and obeys the same generating and moment formulas.

## Proof

**Step 1: An exact digital identity.** Write \(n=\sum_{j=0}^{r-1}d_j3^j\), where \(d_j\in\{0,1,2\}\). Start with carry \(a_0=0\) and set
\[
a_{j+1}=\left\lfloor\frac{2d_j+a_j}{3}\right\rfloor\in\{0,1\},
\qquad e_j=2d_j+a_j-3a_{j+1}\in\{0,1,2\}.
\]
The final carry \(a_r\) is the highest ternary digit of \(2n\). Kummer's carry theorem implies \(X(n)=\sum_{j=0}^{r-1}a_{j+1}\). By Legendre's factorial formula \(\nu_3(m!)=(m-s_3(m))/2\), the identity
\(Y(n)=[s_3(2n)]/2\) holds, since \(s_3(3n)=s_3(n)\) and
\(\nu_3\binom{3n}{n}=\nu_3((3n)!)-\nu_3((2n)!)-\nu_3(n!)\).
Summing \(2d_j+a_j=e_j+3a_{j+1}\) and adding the final digit \(a_r\) yields \(s_3(2n)=2\sum_jd_j-2\sum_ja_{j+1}\). Therefore
\[
Y(n)=\sum_{j=0}^{r-1}(d_j-a_{j+1}),\qquad X(n)+Y(n)=s_3(n).
\]
The latter digit-sum equality is a classical factorial identity and is **not** presented as an original theorem.

**Step 2: Weighted transition matrix and generating function.** In carry state zero the digits \(0,1,2\) induce respectively \((a',\Delta X,\Delta Y)=(0,0,0),(0,0,1),(1,1,1)\); in state one, they induce \((0,0,0),(1,1,0),(1,1,1)\). Thus, with rows indexed by the old carry and columns by the new carry,
\[
M(u,v)=\begin{pmatrix}1+v&uv\\1&u(1+v)\end{pmatrix},
\qquad P_r(u,v)=(1,0)M(u,v)^r\binom11.
\]
Its trace equals \((1+u)(1+v)\) and determinant equals \(u(1+v+v^2)\). Cayley–Hamilton gives the stated recurrence. As \(P_0=1\), \(P_1=1+v+uv\), the rational generating function follows, including its numerator \(1-uz\).

**Step 3: Exact attainable pairs.** Every increment \(\Delta X\) and \(\Delta Y\) is either zero or one, so \(0\leq X,Y\leq r\). If \(X>0\), its first carry is created by digit \(2\) from state zero; that digit contributes one to \(Y\). Hence \(Y\geq1\). Conversely, in least-significant-first digit order, \(j\) digits \(1\) followed by zeros realize \((0,j)\). For \(1\leq y\leq x\leq r\), concatenate \(y\) digits \(2\), then \(x-y\) digits \(1\), and pad with zeros: the resulting pair is \((x,y)\). For \(1\leq x<y\leq r\), concatenate \(y-x\) digits \(1\) and then \(x\) digits \(2\), padding with zeros: the result is \((x,y)\). These constructions prove both positivity and exhaustiveness; their length never exceeds \(r\).

**Step 4: Exact moments.** With independent uniform digits \(d_j\), the carry process satisfies
\[
\mathbb E(a_{j+1}\mid a_j)=\frac{1+a_j}{3},
\quad \mathbb Ea_i=\frac{1-3^{-i}}2,
\quad \operatorname{Cov}(a_i,a_j)=3^{-(j-i)}\frac{1-3^{-2i}}4 \ \ (1\leq i<j).
\]
The last formula follows from \(\mathbb E(a_j\mid a_i)-\mathbb Ea_j=3^{-(j-i)}(a_i-\mathbb Ea_i)\), an identity obtained by iterating the affine conditional expectation. Summing gives the displayed \(\mathbb EX\) and \(\operatorname{Var}(X)\). Also \(\operatorname{Cov}(a_i,d_j)=3^{-(i-j)}\) for \(0\leq j<i\) and zero for \(j\geq i\): the immediate covariance is \(1/3\), and every later carry transition contracts covariance by \(1/3\). Hence \(\operatorname{Cov}(X,s_3(n))=\mathbb EX\). Since \(X+Y=s_3(n)\) and \(\operatorname{Var}(s_3(n))=2r/3\), the stated formulas for \(\mathbb EY\), \(\operatorname{Var}(Y)\) and \(\operatorname{Cov}(X,Y)\) follow by substitution. The formula is also valid at \(r=0\).

**Step 5: The joint central limit theorem.** For real \(s,t\) near zero, set \(u=e^s,v=e^t\). The matrix \(M(e^s,e^t)\) has simple dominant eigenvalue \(\lambda_+(s,t)\) equal to three at the origin; the second eigenvalue equals one at the origin. Spectral decomposition shows
\[
3^{-r}P_r(e^s,e^t)=c(s,t)\bigl(\lambda_+(s,t)/3\bigr)^r+O(\rho^r)
\]
locally uniformly near the origin for some \(\rho<1\), with \(c(0,0)=1\) analytic. Direct differentiation of the characteristic polynomial
\(\lambda^2-(1+e^s)(1+e^t)\lambda+e^s(1+e^t+e^{2t})=0\)
shows
\[
\log\!\bigl(\lambda_+(s,t)/3\bigr)=\frac{s+t}{2}+\frac{s^2}{4}+\frac{t^2}{12}+O((|s|+|t|)^3).
\]
Substitute \(s=i\alpha/\sqrt r,t=i\beta/\sqrt r\), subtract the centering phases and let \(r\to\infty\). The characteristic function tends to \(\exp(-\alpha^2/4-\beta^2/12)\), proving the asserted independent Gaussian limit by the continuity theorem. The finite covariance nonetheless tends to the strictly positive constant \(3/16\).

## Verification

The companion `verify.py` uses **exact integer arithmetic** and independently checks the digital formula against factorial valuations for every \(n\) at levels \(0\leq r\leq9\), amounting to 29,524 index checks. It compares the two-state recurrence's complete coefficient tables with independently computed direct frequencies, checks the exact support and all moment identities as rational numbers, and checks 301 actual integer binomial pairs. Run `python3 verify.py` without third-party dependencies. Observed output:

```text
VERIFY_OK levels=0..9 direct_indices=29524 integer_binomial_cases=301 joint_polynomials=PASS support=PASS exact_moments=PASS
```

These are finite consistency checks; the unbounded statements rest on the preceding proof.

## Relationship to prior work

Kummer's carry theorem and Legendre's valuation formula supply classical ingredients. Barat and Grabner (2001), *Distribution of Binomial Coefficients and Digital Functions*, gives broad digital-function asymptotics and a general moment/correlation apparatus (particularly its Remark 5, Section 3, and Section 5 on multinomial extensions); its measured population consists of binomial coefficients throughout Pascal's triangle. It does not state the exact paired valuation distribution for the fixed proportional coefficients \(\binom{2n}{n}\) and \(\binom{3n}{n}\), nor the support and bounded covariance asserted here. Spiegelhofer and Wallner (first publicly posted 2016) study row-wise numbers of binomial coefficients with a prescribed valuation, rather than the present paired index functions. Straub, Moll, and Amdeberhan's generalized central-binomial valuations use a different coefficient family, not the proportional pair. The classical product \(\binom{2n}{n}\binom{3n}{n}=(3n)!/(n!)^3\) and its digit-sum identity are expressly treated as known; it does not individually determine the two factors' joint frequencies.

## Limitations

The theorem concerns the prime three and the specified two coefficients only. No other prime, multi-factor extension, local limit theorem, or rate of Gaussian convergence is claimed. The Gaussian convergence is qualitative. The proof is mathematical and the verification finite. Published digital-function frameworks might encompass this calculation implicitly; absence of an explicitly identical theorem in the examined sources is not proof of historical uniqueness. Independent audit has not been performed.

## References

1. G. Barat and P. J. Grabner, *Distribution of Binomial Coefficients and Digital Functions*, J. London Math. Soc. **64** (2001), 523–547. DOI: https://doi.org/10.1112/S0024610701002630. Author-accessible text: https://www.math.tugraz.at/~grabner/Publications/Binomial.pdf.
2. L. Spiegelhofer and M. Wallner, *An Explicit Generating Function Arising in Counting Binomial Coefficients Divisible by Powers of Primes*, arXiv:1604.07089, first posted April 24, 2016: https://arxiv.org/abs/1604.07089.
3. A. Straub, V. H. Moll, and T. Amdeberhan, *The \(p\)-adic valuation of \(k\)-central binomial coefficients*: https://arminstraub.com/downloads/pub/centralbinomials.pdf.
4. E. E. Kummer, classical theorem on prime valuations of binomial coefficients and base-prime carries (1852); cited in References 1–2.
