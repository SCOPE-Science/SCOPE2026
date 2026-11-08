# A seven-prime resonance in quintic–cubic Gabor tomography

## Finding

For a prime \(p\), let \(\zeta_p=e^{2\pi i/p}\) and consider the unimodular polynomial-phase window
\[
 g_{c,d,e}(x)=\zeta_p^{c x^5+d x^3+e x},\qquad x\in\mathbb F_p,
\]
with arbitrary \(c,d,e\in\mathbb F_p\). Analyze every complex \(p\)-by-\(p\) matrix against the \(p^2\) time–frequency shifts of the rank-one projector \(gg^*\), using the unnormalized window. The complete rank classification of this linear analysis operator \(\mathcal L_g\) is
\[
\operatorname{rank}\mathcal L_g=
\begin{cases}
 p,&p\in\{2,3\};\\
 5,&p=5,\ d=0;\\
 21,&p=5,\ d\ne0;\\
 7,&p=7,\ c=d=0;\\
 39,&p=7,\ c\ne0,\ d/c\in\{3,5,6\};\\
 43,&p=7\text{ in every other case};\\
 p,&p\ge11,\ c=d=0;\\
 p^2-p+1,&p\ge11,\ (c,d)\ne(0,0).
\end{cases}
\]
The coefficient \(e\) never affects the rank. The exceptional rank \(39\) occurs for exactly \(18\) of the \(49\) coefficient pairs \((c,d)\) at \(p=7\).

More precisely, put
\[
 (W_{a,b}h)(x)=\zeta_p^{-bx}h(x+a),\quad
 A_g(a,b)=\langle g,W_{a,b}g\rangle
   =\sum_{x\in\mathbb F_p}\overline{g(x)}g(x+a)\zeta_p^{-bx}.
\]
For \(p\ge11\) and \((c,d)\ne(0,0)\), and also for \(p=7\) outside the exceptional coefficient locus with \((c,d)\ne(0,0)\), the **only** ambiguity zeros are \((a,b)=(0,b)\) with \(b\ne0\). In this case, the kernel of \(\mathcal L_g\) is exactly the traceless diagonal matrix space, of dimension \(p-1\). On the exceptional \(p=7\) locus there are exactly four additional zeros,
\[
  (a,b)=(a,\pm ca),\qquad a\ne0,\quad d=5ca^2\pmod 7,
\]
so the kernel is the traceless diagonal space plus the four corresponding Weyl directions. In the affine-character cases, \(A_g(a,b)\ne0\) exactly when \(b=0\), hence the rank is \(p\).

For **every** unimodular window on \(\mathbb F_p\), the rank cannot exceed \(p^2-p+1\), because all its zero-translation, nonzero-modulation ambiguity coefficients vanish. Thus the full quintic–cubic family achieves the largest rank allowed by constant modulus at every prime \(p\ge11\), with a genuine isolated coefficient resonance at \(p=7\). The classification concerns the complex-linear operator span and is not a claim of complete nonlinear phase-retrieval uniqueness.

## Assumptions and scope

The space \(\operatorname{End}(\mathbb C^p)\) has its Hilbert–Schmidt inner product. For \(s,t\in\mathbb F_p\) let \(v_{s,t}=W_{s,t}g\), and define
\[
 \mathcal L_g(H)_{s,t}=\operatorname{tr}(H v_{s,t}v_{s,t}^*).
\]
We regard \(\mathcal L_g\) as a complex-linear map with the ordinary complex bilinear-in-\(H\) trace pairing; the convention only conjugates the matrix indices and does not affect rank. Frequencies are labeled using the displayed \(W_{a,b}\), so the Weyl kernel statements refer to exactly those labels. All finite fields are **prime fields**; no claim is made for extension fields or composite cyclic moduli.

## Proof

**1. Weyl diagonalization.** The \(p^2\) Weyl operators \(W_{a,b}\) form an orthogonal basis of \(\operatorname{End}(\mathbb C^p)\), with squared Hilbert–Schmidt norm \(p\). Conjugating each \(W_{a,b}\) by \(W_{s,t}\) multiplies it by a character of \((s,t)\). Expanding the projectors \(v_{s,t}v_{s,t}^*\) in this basis and using orthogonality of those characters shows that the positive squared singular values of \(\mathcal L_g\) are
\[
 p|A_g(a,b)|^2\quad\text{for all }(a,b)\text{ with }A_g(a,b)\ne0.
\]
Consequently \(\operatorname{rank}\mathcal L_g=\#\{(a,b):A_g(a,b)\ne0\}\) and its kernel is the span of the Weyl operators at the zero ambiguity indices. As \(|g(x)|=1\),
\[
 A_g(0,b)=\sum_x\zeta_p^{-bx}=p\mathbf1_{b=0},
\]
giving the universal upper bound.

**2. Cyclotomic vanishing and permutation polynomials.** For a function \(P:\mathbb F_p\to\mathbb F_p\), write \(n_u=\#\{x:P(x)=u\}\). Then
\[
\sum_x\zeta_p^{P(x)}=\sum_{u=0}^{p-1}n_u\zeta_p^u.
\]
The minimal polynomial of \(\zeta_p\) over \(\mathbb Q\) is \(1+X+\cdots+X^{p-1}\). Thus the sum vanishes exactly when all \(n_u\) are equal, which (because they sum to \(p\)) means that \(P\) is a permutation of \(\mathbb F_p\). This exact equivalence avoids numerical tests of near-zero complex numbers.

**3. Symmetric derivative.** Put \(f(x)=cx^5+dx^3+ex\). For \(a\ne0\) and odd \(p\), substitute \(y=x+a/2\). A binomial expansion gives
\[
 f(x+a)-f(x)-bx
 =5ca\,y^4+\left(\frac52ca^3+3da\right)y^2-by+C,
\]
where \(C\) does not depend on \(y\). Therefore the ambiguity coefficient vanishes precisely when
\[
 P(y)=A y^4+B y^2+D y,
 \qquad A=5ca,\quad B=\frac52ca^3+3da,\quad D=-b
\]
permutes \(\mathbb F_p\). Addition of \(C\) does not change the permutation property.

**4. The quartic obstruction for primes at least eleven.** Suppose \(p\ge11\), \(A\ne0\), and \(P(y)=Ay^4+By^2+Dy\) is a permutation. For every integer \(1\le m\le p-2\), it must satisfy \(\sum_y P(y)^m=\sum_y y^m=0\pmod p\). Recall \(\sum_y y^r=-1\) when \(r>0\) is divisible by \(p-1\), and zero for all other \(r>0\).

If \(p\equiv1\pmod4\), choose \(m=(p-1)/4\). The highest power of \(P^m\) is \(y^{p-1}\), with coefficient \(A^m\), and all other positive exponents are smaller. The power-sum identity gives \(-A^m=0\), impossible.

If \(p\equiv3\pmod4\), choose \(m=(p+1)/4\). In \(P^m\) the highest exponent is \(p+1\), and the unique way to obtain exponent \(p-1\) is to replace one quartic factor by one quadratic factor. Its coefficient is \(mA^{m-1}B\). Thus the power-sum identity forces \(B=0\). Now put \(t=(p+5)/4\). Because \(p\ge11\), \(p+5<2(p-1)\). In \((Ay^4+Dy)^t\), the only exponent divisible by \(p-1\) is \(p-1\), obtained by replacing exactly two quartic factors with linear factors. Its coefficient is \(\binom t2 A^{t-2}D^2\). The binomial coefficient is nonzero modulo \(p\), so \(D=0\). But \(Ay^4\) takes equal values at \(y\) and \(-y\), contradicting injectivity. Hence **none** of the displayed quartics is a permutation over a prime field of order at least eleven.

When \(c=0,d\ne0\), the derivative instead has a nonzero quadratic leading coefficient \(3da\) for every \(p\ge5\); a nonconstant quadratic polynomial over an odd prime field is not a permutation. This proves the generic rank \(p^2-p+1\) for \(p\ge11\).

**5. Exact seven-prime exception.** For \(p=7\), \(A=5ca\ne0\). If \(P(y)=Ay^4+By^2+Dy\) permutes \(\mathbb F_7\), then \(\sum_yP(y)^2=0\), and its only exponent divisible by six has coefficient \(2AB\); hence \(B=0\). The equation \(\sum_y P(y)^3=0\) reduces to
\[
 A^3+3AD^2=0\pmod7,
 \qquad (D/A)^2=2\pmod7,
\]
so \(D/A\in\{3,4\}\). These two possibilities are sufficient: the value lists of \(y^4+3y\) and \(y^4+4y\), for \(y=0,1,\ldots,6\), are respectively
\[
(0,4,1,6,2,3,5),\qquad(0,5,3,2,6,1,4),
\]
which are both permutations. The equation \(B=0\) is exactly \(d=5ca^2\pmod7\); it has two nonzero solutions \(a\) if and only if \(d/c\in\{3,5,6\}\), and otherwise none. For each such \(a\), the two permutation values \(D/A=3,4\) are exactly \(b=\pm ca\). Therefore the exceptional parameter locus has exactly four additional ambiguity zeros, proving ranks \(39\) and \(43\), respectively. The \(c=0,d\ne0\) cubic case has nonpermuting quadratic differences and rank \(43\).

**6. Small primes and linear cases.** For \(p=5\), the identity \(x^5=x\) on \(\mathbb F_5\) makes the quintic coefficient a linear phase. If \(d\ne0\), every nonzero-shift difference is a genuine quadratic, so exactly \(p-1\) ambiguity entries vanish, giving rank \(21\); if \(d=0\), the window is an additive character and has rank \(5\). For \(p=3\), both \(x^3\) and \(x^5\) coincide with \(x\) as functions; for \(p=2\) they do as well, so all windows are additive characters and have rank \(p\). More generally, whenever the phase is affine-linear, its ambiguity is supported precisely on \(b=0\). These cases complete the classification.

## Verification

The accompanying standard-library checker `check.py` uses only exact integer counts. For every \((c,d)\) over each prime \(p\in\{2,3,5,7,11,13,17,19\}\), it compares the predicted full set of ambiguity zeros with the exact root-count criterion for all \((a,b)\). Additional instances are checked at primes \(23,29,31,37\). In particular, the complete rank distributions across coefficient pairs are
\[
\begin{array}{c|l}
 p& \text{rank: number of coefficient pairs}\ (c,d)\\\hline
 3&3:9\\
 5&5:5,\ 21:20\\
 7&7:1,\ 39:18,\ 43:30\\
 11&11:1,\ 111:120\\
 13&13:1,\ 157:168\\
 17&17:1,\ 273:288\\
 19&19:1,\ 343:360
\end{array}
\]
The checks are finite corroboration. The quartic power-sum argument proves the all-prime assertion independently of enumeration.

## Relationship to prior work

Hall, Rao and Donovan [1] analyze cubic Alltop-type functions by the stronger requirement that their derivatives yield planar functions. Their result does not classify the **zero set** of the Gabor ambiguity of quintic–cubic deformations. Bojarovska and Flinth [2] derive the general Gabor lifting/ambiguity criterion and observe the known noninjectivity of Alltop cubic sequences; that criterion is an explicit ingredient above, not claimed as new. General permutation-polynomial theory, including Hermite's criterion and Dickson's low-degree classifications, is likewise classical; Fan [3] surveys these classifications. The distinction here is a complete, parameter-wise lifting-rank and kernel theorem for the quintic–cubic family, including the exceptional small-prime resonance. Lüke's 1996 paper [4] studies bounds for correlations of polynomial-phase sequences, but its complete text could not be inspected, leaving an explicit historical-priority risk.

## Limitations

No claim is made of a new permutation-polynomial criterion, of novel quadratic Gauss-sum evaluations, or of full nonlinear phase-retrieval injectivity. In particular, the traceless diagonal kernel persists in the maximal-rank regimes, so the corresponding linear lift is **never** injective on all matrices. No explicit complete positive singular-value distribution or uniform condition number is asserted for the quartic exponential sums. The result is for prime-field cyclic phase windows and not for general prime powers. An independently verified literature-wide historical-priority determination or an independent mathematical audit has not been performed.

## References

1. J. L. Hall, A. Rao, D. Donovan, *Planar Difference Functions*, arXiv:1205.3310v1 (first posted 2012-05-15), https://arxiv.org/abs/1205.3310.
2. I. Bojarovska, A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1 (first posted 2015-03-19), https://arxiv.org/abs/1503.05800.
3. X. Fan, *Permutation Polynomials of Degree 8 over Finite Fields of Odd Characteristic*, arXiv:1905.04202v1 (first posted 2019-05-10), especially the discussion of Dickson's degree-at-most-five classification and Hermite's criterion, https://arxiv.org/abs/1905.04202.
4. H. D. Lüke, *Large families of polynomial phase sequences with low correlation*, European Transactions on Telecommunications 7 (1996), 235–238, DOI:10.1002/ett.4460070303 (abstract and bibliographic metadata inspected; complete text unavailable).
