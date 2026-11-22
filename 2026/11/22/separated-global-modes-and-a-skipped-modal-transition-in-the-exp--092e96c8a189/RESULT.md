# Separated global modes and a skipped modal transition in the exponentiated discrete Lindley law

## Finding
Fix the original exponentiated discrete Lindley distribution of El-Morshedy, Eliwa and Nagy, with discrete-Lindley base parameter \(q=21/25\). There exists a **unique** exponent \(b_*\) solving
\[
W_2^{b_*}-W_1^{b_*}=W_0^{b_*},
\qquad \frac{779}{1000}<b_*<\frac{39}{50},
\]
where \(W_j\) is the base cumulative distribution function defined below. At this exponent the only global maximizers of the probability mass function are **two nonadjacent counts**, \(0\) and \(2\):
\[
p_0(b_*)=p_2(b_*)>p_j(b_*)\quad\text{for every integer }j\ge0,\ j\notin\{0,2\}.
\]
Numerically \(b_*\approx0.7797825617279781\). There is an open neighborhood of \(b_*\) in which the global modal count jumps directly from \(0\) to \(2\) as \(b\) increases, never becoming \(1\). This is a finite-parameter, infinite-support statement, not an assertion based on a finite histogram.

## Assumptions and scope
Write \(q=21/25\), \(L=-\log q=\log(25/21)\), and for every integer \(j\ge0\) put
\[
W_j=1-\frac{q^{j+1}[1+(j+2)L]}{1+L},\qquad W_{-1}=0.
\]
For every \(b>0\), define \(p_j(b)=W_j^b-W_{j-1}^b\) on the nonnegative integers. These are the probability masses of the CDF-power family studied in the cited 2018 preprint (and published in 2019). Indeed, \(0=W_{-1}<W_0<W_1<\cdots\uparrow1\), so the masses are positive and sum to one. The fixed value \(q=21/25\) is a rational parameter chosen to exhibit the natural global-modal transition, not a restriction on the published model's validity.

## Proof
**1. Unique crossing.** For every integer \(j\ge1\), division by \(p_0(b)=W_0^b\) yields
\[
R_j(b)=\frac{p_j(b)}{p_0(b)}=\left(\frac{W_j}{W_0}\right)^b-\left(\frac{W_{j-1}}{W_0}\right)^b.
\]
The function \(x\mapsto x^b\log x\) is strictly increasing for \(x\ge1\) and \(b>0\). Consequently \(R'_j(b)>0\). In particular, \(R_2(b)\) is continuous, increases strictly from \(0\) as \(b\downarrow0\), and tends to infinity as \(b\to\infty\); thus \(R_2=1\) has exactly one positive solution.

**2. Certified finite inequalities.** The attached standalone `check_certificate.py` performs integer-only confirmations of rational-power bounds, using a rational interval for \(L=2\operatorname{artanh}(2/23)\). Its output certifies
\[
p_2(779/1000)<p_0(779/1000),\qquad
p_2(39/50)>p_0(39/50)
\]
and, at \(b=39/50\), all four strict comparisons
\[
p_1(b)<p_0(b),\quad p_3(b)<p_0(b),\quad
p_4(b)<p_0(b),\quad p_5(b)<p_0(b).
\]
For orientation, at \(b=39/50\), the respective masses for counts \(0,1,2,3,4,5\) are approximately \(0.073644761\), \(0.072397470\), \(0.073683837\), \(0.072398552\), \(0.069395677\), \(0.065360295\). These decimals are **not** the proof: the code checks rational lower and upper bounds by raising integer numerators and denominators to integer powers. Since every \(R_j(b)\) increases, the four certified upper-endpoint inequalities remain strict at \(b_*<39/50\).

**3. Complete control of the infinite tail.** Extend the base CDF to real \(x>-1\) by
\[
W(x)=1-\frac{e^{-L(x+1)}[1+(x+2)L]}{1+L}.
\]
Direct differentiation gives
\[
W'(x)=\frac{e^{-L(x+1)}(x+2)L^2}{1+L}>0,\qquad
W''(x)=\frac{e^{-L(x+1)}L^2[1-(x+2)L]}{1+L}.
\]
The elementary logarithm bound \(L=2\operatorname{artanh}(2/23)>4/23>1/6\) implies \(W''(x)<0\) for every \(x\ge4\). Since \(0<b_*<1\), the composite \(W(x)^{b_*}\) is strictly concave there: its second derivative equals \(b_*W^{b_*-2}\{WW''+(b_*-1)(W')^2\}<0\). Therefore its unit-interval increments satisfy \(p_5(b_*)>p_6(b_*)>p_7(b_*)>\cdots\). Combined with the certified finite comparisons, this proves strict domination of every count except \(0\) and \(2\).

**4. Modal jump.** The strict gap to all other masses at \(b_*\) persists in a sufficiently small neighborhood: the finitely many counts \(1,3,4,5\) vary continuously, and for \(b<1\) the concavity argument bounds every later mass by \(p_5(b)\). The sign of \(p_2-p_0\) changes only at \(b_*\) because \(R_2\) is strictly increasing. Thus the sole global mode is \(0\) immediately below and \(2\) immediately above \(b_*\), with exactly the two global modes at equality.

## Verification
Run `python3 check_certificate.py` using Python 3 (standard library only). The script verifies a positive rational interval for \(\log(25/21)\) by an exact truncated positive series plus a geometric-series remainder bound; it then proves the six finite mass inequalities by exact cross-multiplication of integer powers. Floating-point evaluations are used only to suggest generous candidate brackets, **never to accept an inequality**. The actual replay returned `CERTIFICATE_PASS; rational-power inequality checks: 28`. The infinite-tail and uniqueness arguments are analytical and are written above rather than inferred from numerical tests.

## Relationship to prior work
El-Morshedy, Eliwa and Nagy defined this specific CDF-power distribution and displayed sample probability-mass shapes, hazards and statistical properties. Their publicly available 2018 preprint provides the exact CDF needed here, but the inspected material does not give a separated global tie or skipped modal transition. The different CDF-power construction of Singh, Pandey, Tyagi and Chesneau (2023) instead exponentiates the \(\operatorname{NB}(2,1-q)\) CDF; its masses and parameterization are **not** interchangeable with this theorem. The generalized discrete Lindley family of Salem and Ismail (2023) also has a different survival construction. General results on monotone CDF powers do not, on their own, establish a nonadjacent global-mode transition in this specific count law. Searches of relevant publicly indexed mathematical results identified other modal transitions in distinct probability families, not an implication of the present strict inequalities.

## Limitations
The theorem is a rigorous existence and local uniqueness result at **one fixed base parameter** \(q=21/25\). It does not classify all modes over the full two-parameter space or claim that all CDF-power distributions exhibit skipped transitions. The root is implicitly defined, with a certified rational interval but no algebraic closed form. The priority check is a documented best-knowledge literature comparison, not independent historical certification; independently obtaining or searching every publisher version and thesis remains outside the proof.

## References
1. M. El-Morshedy, M. S. Eliwa and H. Nagy, *Exponentiated Discrete Lindley Distribution: Properties and Applications*, arXiv:1807.09895v1, first public preprint 25 July 2018, https://arxiv.org/abs/1807.09895 (especially Section 2 and Figure 1).
2. M. El-Morshedy, M. S. Eliwa and H. Nagy, *A new two-parameter exponentiated discrete Lindley distribution: properties, estimation and applications*, *Journal of Applied Statistics*, online 8 July 2019, https://doi.org/10.1080/02664763.2019.1638893.
3. R. P. Singh, A. Pandey, A. Tyagi and C. Chesneau, *A New Exponentiated Discrete Lindley Distribution for Analyzing Count Data*, *Revista Investigación Operacional* 44(2), 166–183 (2023), https://rev-inv-ope.pantheonsorbonne.fr/sites/default/files/inline-files/44223-03.pdf (a different base CDF).
4. M. M. Salem and M. A. Ismail, *A Discrete New Generalized Two Parameter Lindley Distribution: Properties, Estimation and Applications*, *Statistics, Optimization & Information Computing* 11, 978–1000 (2023), https://doi.org/10.19139/soic-2310-5070-1392 (different generalized Lindley model).
