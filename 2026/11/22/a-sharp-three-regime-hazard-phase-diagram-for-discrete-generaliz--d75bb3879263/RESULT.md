# A sharp three-regime hazard phase diagram for discrete generalized Burr–Hatke lifetimes

## Finding

The two-parameter discrete generalized Burr–Hatke (DGBH) law of Yousof, Chesneau, Hamedani and Ibrahim has a complete, exact infinite-support failure-hazard classification. Write its parameters as \(0<\pi<1\), \(\beta>0\), and set \(t=-\log\pi>0\). Define, for integer \(k\geq0\),
\[
 B_k=\log\frac{(k+2)^2}{(k+1)(k+3)},\qquad
 D_k(\beta)=(k+2)^\beta-2(k+1)^\beta+k^\beta.
\]
For \(\beta>1\), put \(T_k(\beta)=B_k/D_k(\beta)\). Then \(T_1>T_2>\cdots>0\), with \(T_k\to0\), and
\[
 h(k+1)\begin{cases}>h(k)&\text{if }t>T_k,\\=h(k)&\text{if }t=T_k,\\<h(k)&\text{if }0<t<T_k.\end{cases}
\]
Thus the only possible strict sign patterns of successive hazard increments are all negative; all positive; negative followed by positive; or positive, then negative, then positive. Equalities occur precisely at the thresholds above.

There exists a **unique** critical exponent \(\beta_c>1\), defined by
\[
 \frac{3^{\beta_c}-2^{\beta_c+1}+1}{2^{\beta_c}-2}
 =\frac{\log(9/8)}{\log(4/3)},
 \qquad \beta_c=1.065266334860508687\ldots.
\]
For \(1<\beta<\beta_c\), the thresholds satisfy \(T_2<T_0<T_1\) and \(T_1>T_2>T_3>\cdots\). In the **nonempty exact region**
\[
 T_0(\beta)<-\log\pi<T_1(\beta),
\]
the hazard rises from count zero to one, drops from one to two, and then rises **strictly at every subsequent step**. Thus \(h(0)<h(1)>h(2)<h(3)<h(4)<\cdots\). This is a count-one peak followed immediately by a count-two trough, not a globally unimodal (upside-down) hazard. For \(\beta\geq\beta_c\), all thresholds decrease from \(T_0\) onward, and no two-turn hazard occurs. For \(0<\beta\leq1\), the hazard decreases strictly everywhere.

At \(\beta=\beta_c\) and \(t=T_0=T_1\), exactly **three consecutive hazard values coincide**: \(h(0)=h(1)=h(2)<h(3)<h(4)<\cdots\). This is the unique parameter point with three consecutive equal hazard values. Numerically \(t=3.108189731764025646\ldots\), or \(\pi=0.044681768157389969\ldots\).

For every fixed \(\beta>1\), the late-turn threshold obeys
\[
 T_k(\beta)\sim\frac{1}{\beta(\beta-1)k^\beta}.
\]
As \(t\downarrow0\), the first post-decline (nondecreasing) hazard step occurs at an index \(m(t)\) satisfying \(m(t)t^{1/\beta}\to[\beta(\beta-1)]^{-1/\beta}\). This precisely locates the delayed bathtub minimum under coarse near-unity survival parameters.

## Assumptions and scope

For integer \(k\geq0\), the DGBH distribution is defined by the proper survival tail
\[
 S(k)=\Pr(X>k)=\frac{\pi^{(k+1)^\beta}}{k+2},\qquad S(-1)=1.
\]
The discrete failure hazard is \(h(k)=\Pr(X=k\mid X\geq k)=1-S(k)/S(k-1)\). All results concern the entire nonnegative integer support, not a truncated display. The parameter inequalities \(0<\pi<1\) and \(\beta>0\) are strict. At equality boundaries the sign rule above, rather than a strict-shape label, is authoritative.

The complete practical classification for \(\beta>1\) is: if \(t\geq\max\{T_0,T_1\}\), all hazard steps are nonnegative; if \(t<T_0\), they start negative and eventually become positive; and the only other possible nonmonotone regime is \(1<\beta<\beta_c\) with \(T_0<t<T_1\), where the signs are positive, negative, then positive at every subsequent step. The same sign rule determines every exact tie (including ties at \(T_k\) for \(k\geq2\)).

## Proof

**1. Exact comparison.** Taking the ratio of consecutive survival tails gives
\[
 1-h(k)=\frac{k+1}{k+2}\exp\{-t[(k+1)^\beta-k^\beta]\}.
\]
Consequently
\[
 \log\frac{1-h(k+1)}{1-h(k)}=B_k-tD_k(\beta).
\]
For \(0<\beta\leq1\), the power \(x\mapsto x^\beta\) is concave or linear, so \(D_k\leq0\), while \(B_k>0\); hence \(h(k+1)<h(k)\) for every \(k\). For \(\beta>1\), \(D_k>0\), giving the stated exact comparison.

**2. Strict decrease of all tail thresholds.** Define the triangular weight \(w(u)=u\) for \(0\leq u\leq1\), \(w(u)=2-u\) for \(1\leq u\leq2\), and zero otherwise. The second-difference identities yield
\[
 D_k(\beta)=\beta(\beta-1)\int_0^2w(u)(k+u)^{\beta-2}\,du,
 \qquad B_k=\int_0^2\frac{w(u)}{(k+1+u)^2}\,du.
\]
For each \(k\geq0\), the ratio \(D_{k+1}(\beta)/D_k(\beta)\) is **strictly increasing in \(\beta>1\)**. Indeed, after cancelling the common positive factor, its logarithmic derivative is the difference between expectations of \(\log x\) under densities proportional to \(w(x-k-1)x^{\beta-2}\) and \(w(x-k)x^{\beta-2}\). The first shifted triangular density dominates the second in the monotone-likelihood-ratio order: their base-weight quotient is zero to the left of the overlap, strictly increases as \((x-k-1)/(k+2-x)\) over the overlap, and is infinite to the right. Therefore the expectation difference is strictly positive, including at \(k=0\) by integrability.

For integer \(k\geq1\), set
\[
 d_k=\int_0^2\frac{w(u)}{k+u}\,du
 =\lim_{\beta\downarrow1}\frac{D_k(\beta)}{\beta-1}.
\]
Let \(\mu_k\) be the probability distribution on \((0,2)\) with density \(w(u)/[d_k(k+u)]\). Then
\[
 \frac{B_k}{d_k}=\mathbb E_{\mu_k}\left[\frac{k+U}{(k+1+U)^2}\right].
\]
The function \(x/(x+1)^2\) decreases strictly for \(x>1\). Moreover \(\mu_{k+1}/\mu_k\) is proportional to \((k+u)/(k+1+u)\), strictly increasing in \(u\). Thus \(\mu_{k+1}\) stochastically dominates \(\mu_k\), and shifting the function's argument by one proves \(B_{k+1}/d_{k+1}<B_k/d_k\). From the preceding strict increase in \(\beta\),
\[
 \frac{B_{k+1}}{B_k}
 <\frac{d_{k+1}}{d_k}
 <\frac{D_{k+1}(\beta)}{D_k(\beta)},\qquad k\geq1,\ \beta>1.
\]
Therefore \(T_{k+1}(\beta)<T_k(\beta)\) for every integer \(k\geq1\).

**3. The unique early inversion.** The same strict increase applies to \(R(\beta)=D_1(\beta)/D_0(\beta)\). It satisfies
\[
 \lim_{\beta\downarrow1}R(\beta)
 =\frac{3\log3-4\log2}{2\log2}
 <\frac{\log(9/8)}{\log(4/3)}
 =\frac{B_1}{B_0},
\]
while \(R(\beta)\to\infty\) as \(\beta\to\infty\). The strict middle inequality can be checked by rational upper and lower bounds from the positive-series identity \(\log x=2\sum_{j\geq0}z^{2j+1}/(2j+1)\), \(z=(x-1)/(x+1)\); a standalone exact-rational checker is supplied. Continuity and strict increase give precisely one \(\beta_c>1\). Hence \(T_0<T_1\) exactly for \(1<\beta<\beta_c\), equality exactly at \(\beta_c\), and reversal for larger \(\beta\). In fact, \(T_2<T_0\) for **every** \(\beta>1\): the strict increase in the adjacent \(D\)-ratios implies strict increase of \(D_2/D_0\) with \(\beta\), while at \(\beta\downarrow1\) the inequality \(B_2/d_2<B_0/d_0\) holds. Here \(B_2=\log(16/15)\), \(d_2=10\log2-6\log3\), and \(d_0=2\log2\); the strict inequality again has an exact rational-log-series certificate in the supplied checker. Therefore the two-turn case has its trough **at count two**, with every later hazard increment strictly positive. Along with Step 2 and the exact sign test, this proves all the phase claims, the unique three-term plateau and the upper bound of two strict changes.

**4. Eventual increase and turning scale.** Taylor expansion of second differences, at each fixed \(\beta>1\), gives
\[
 B_k=k^{-2}(1+O(k^{-1})),\qquad
 D_k(\beta)=\beta(\beta-1)k^{\beta-2}(1+O_\beta(k^{-1})).
\]
Thus \(T_k\sim[\beta(\beta-1)k^\beta]^{-1}\to0\); every positive \(t\) eventually exceeds all thresholds. For sufficiently small \(t>0\), let \(m(t)\) be the least integer \(k\geq1\) for which \(t\geq T_k\). Monotonicity brackets \(t\) between two consecutive thresholds and yields \(m(t)t^{1/\beta}\to[\beta(\beta-1)]^{-1/\beta}\).

## Verification

The standalone `check_hazard.py` checks 227 assertions, including an **exact-rational** strict inequality needed for the critical crossing, high-precision reconstruction of \(\beta_c\), finite hazard sign patterns, the exceptional triple plateau, and asymptotic finite-index diagnostics. Python 3 and `mpmath` are required; run `python check_hazard.py` in a directory containing that file. Infinite-support claims depend on the analytic arguments in the Proof section, not on finite numerical experiments. No external proof assistant or independent validation is claimed.

For a concrete two-turn example, \(\beta=1.05\), \(t=4.11\) give \(h(0)=0.99179611273685\ldots\), \(h(1)=0.99181410544459\ldots\), \(h(2)=0.99180348580195\ldots\), \(h(3)=0.99190782198471\ldots\); the general proof guarantees an increase at every step after count two.

## Relationship to prior work

Yousof, Chesneau, Hamedani and Ibrahim (2021) introduced the exact DGBH tail, displayed its hazard formula and graphically described several hazard shapes (especially Sections 1–2, pp. 136–142). They did not state the exact monotone threshold sequence, the unique critical exponent, the triple plateau, or the location scaling of the late minimum. Their qualitative shape observations are not claimed as new. The earlier discrete Burr–Hatke model (El-Morshedy, Eliwa and Altun, 2020) is the \(\beta=1\) subfamily and does not imply the \(\beta>1\) transition. The separate 2021 discrete *exponentiated* Burr–Hatke construction of El-Morshedy and coauthors has CDF \((1-p^{k+1}/(k+2))^\gamma\), not the DGBH CDF \(1-\pi^{(k+1)^\beta}/(k+2)\), so its reported hazard results do not establish these thresholds. The proof uses standard second-difference and monotone likelihood-ratio methods but the exact two-parameter classification is specific to the DGBH survival form.

## Limitations

The work does not assert newness of DGBH itself, the \(\beta=1\) decreasing-hazard property, its qualitative graph shapes, or generic monotone-likelihood-ratio principles. No statistical estimation, model comparison, data application or uniform approximation in \(\beta\) is established. The numerical boundary is a reproduction aid; its mathematical definition and uniqueness are exact. Literature comparisons do not prove global historical priority, and an independent audit has not been performed.

## References

1. H. M. Yousof, C. Chesneau, G. Hamedani and M. Ibrahim, *A New Discrete Distribution: Properties, Characterizations, Modeling Real Count Data, Bayesian and Non-Bayesian Estimations*, Statistica 81(2), 135–162 (2021), DOI: https://doi.org/10.6092/issn.1973-2201/11635 ; publisher full text: https://rivista-statistica.unibo.it/article/download/11635/13248/50629 (publisher public date: 2021-10-26).
2. M. El-Morshedy, M. S. Eliwa and E. Altun, *Discrete Burr-Hatke Distribution With Properties, Estimation Methods and Regression Model*, IEEE Access 8, 74359–74370 (2020), https://doi.org/10.1109/ACCESS.2020.2988431 .
3. M. El-Morshedy, H. M. Aljohani, M. S. Eliwa, M. Nassar, M. K. Shakhatreh and A. Z. Afify, *The Exponentiated Burr–Hatke Distribution and Its Discrete Version*, Mathematics 9, 2277 (2021), https://doi.org/10.3390/math9182277 .
