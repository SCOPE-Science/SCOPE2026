# An exact fourth-block independence window for a zero-entropy toral skew shift

## Finding

Let \(T_\alpha(x,y)=(x+\alpha,y+x)\pmod1\) preserve Haar probability on \(\mathbb T^2\), and define the stationary binary observations \(Z_j(x,y)=s(\pi_2T_\alpha^j(x,y))\), where \(s(u)=1\) on \([0,1/2)\) and \(s(u)=-1\) on \([1/2,1)\). For every real parameter \(\alpha\), all distinct pairs and all distinct triples of the observations have the joint distribution of independent fair signs.

Put \(\delta(\alpha)=\operatorname{dist}(\alpha,\tfrac12\mathbb Z)\in[0,1/4]\). The *entire four-consecutive-observation distribution* is determined by the following explicit piecewise-quadratic function:

\[
\begin{split}
C(\alpha)&=\mathbb E[Z_0Z_1Z_2Z_3]\\
&=\begin{cases}
\frac13-16\delta(\alpha)^2,&0\le\delta(\alpha)\le\frac16,\\[2pt]
-\frac13+32(\frac14-\delta(\alpha))^2,&\frac16\le\delta(\alpha)\le\frac14.
\end{cases}
\end{split}
\]

Specifically, for every sign word \(\varepsilon\in\{-1,1\}^4\),
\[
\mathbb P((Z_0,Z_1,Z_2,Z_3)=\varepsilon)
=\frac{1+C(\alpha)\prod_{j=0}^{3}\varepsilon_j}{16}.
\]
The four consecutive observations are therefore mutually independent **exactly when**
\[
\delta(\alpha)=\frac1{4\sqrt3}.
\]
There are four such parameter classes modulo \(1\), and all are irrational. At each of them the factor process has entropy zero and is not Bernoulli, despite its exactly uniform four-block distribution and its three-wise independence at arbitrary distinct times.

The four-block Shannon entropy (natural logarithm) is, without approximation,
\[
H_4(\alpha)=\log16-
\frac{1+C(\alpha)}2\log(1+C(\alpha))
-\frac{1-C(\alpha)}2\log(1-C(\alpha)),
\]
which attains its maximal possible value \(\log16\) exactly at the displayed irrational parameters.

## Assumptions and scope

The ambient torus has normalized Lebesgue (Haar) probability. Observations use half-open intervals, and endpoints do not affect any probability because they are null sets. There is no rationality condition on \(\alpha\) for the finite-block identities. Only consecutive length-four windows are classified; no claim is made that arbitrary four observation times are independent at the exceptional parameters. The assertion about unique ergodicity is used only at the irrational parameters; the entropy-zero assertion applies to every parameter.

## Proof

**1. Dynamical observations and low-order independence.** Iterating the skew map gives exactly
\[
\pi_2T_\alpha^j(x,y)
=y+jx+\binom j2\alpha\pmod1.
\]
For distinct indices \(i\ne j\), the torus homomorphism \((x,y)\mapsto(y+ix,y+jx)\) has nonzero integer determinant \(j-i\), and hence sends Haar probability to Haar probability on \(\mathbb T^2\). Thus \(Z_i,Z_j\) are independent fair signs. Translating \(y\) by \(1/2\) flips every sign simultaneously without changing Haar probability. Consequently every odd-order sign product has mean zero. The singleton, pair, and triple joint laws of fair signs are determined by their nonempty product moments. All moments of orders one, two, and three vanish, yielding the claimed three-wise independence. Four-point Fourier inversion on \(\{-1,1\}^4\) then gives the stated sign-word law in terms of the sole remaining Walsh coefficient \(C(\alpha)\).

**2. Two exact parameter symmetries.** Changing \(\alpha\) by \(1/2\) shifts the linear representatives \(y+jx+\binom j2\alpha\) by half an integer for \(j=2,3\) and by an integer for \(j=0,1\). Therefore precisely two of the four signs flip and \(C(\alpha+1/2)=C(\alpha)\). Replacing \((x,y,\alpha)\) by \((-x,-y,-\alpha)\) flips all four signs almost surely, so \(C(-\alpha)=C(\alpha)\). It suffices to evaluate \(a=\delta(\alpha)\in[0,1/4]\).

**3. A finite exact rational-area certificate.** For \(j=0,1,2,3\) set \(b_j=\binom j2=(0,0,1,3)_j\) and \(L_j=y+jx+b_ja\). Consider the convex (possibly empty) closed polygons
\[
P_{\boldsymbol k}(a)=\{(x,y)\in[0,1]^2:
\tfrac{k_j}2\le L_j\le\tfrac{k_j+1}2
\text{ for all }j=0,1,2,3\},
\]
indexed by \(k_0\in\{0,1\}\), \(k_1\in\{0,1,2,3\}\), \(k_2\in\{0,\ldots,6\}\), and \(k_3\in\{0,\ldots,9\}\). These \(560\) polygons partition the unit square up to sets of area zero. Inside the \(\boldsymbol k\)-cell the product of the four signs is \((-1)^{k_0+k_1+k_2+k_3}\), so
\[
C(a)=\sum_{\boldsymbol k}(-1)^{k_0+k_1+k_2+k_3}
\operatorname{area}(P_{\boldsymbol k}(a)).\tag{1}
\]
All boundary lines have the forms \(x=0,1\), \(y=0,1\), or \(jx+y+b_ja=k/2\), using all integers \(0\le k\le 2,4,7,10\), respectively, for \(j=0,1,2,3\). There are exactly \(31\) such lines. For rational \(a\), the polygon area in (1) is computed by clipping the unit square against the eight rational half-planes for each cell and applying the shoelace formula. The standalone certificate `verify.py` performs this *exactly*, using `fractions.Fraction`, without floating point.

Here is why finitely many computations prove the unrestricted identity. Each polygon vertex is the intersection of two of these parameter-affine lines, hence is affine in \(a\) between changes of combinatorial type. A change is possible only at a triple intersection in the interior or boundary of the unit square, or at an endpoint of the parameter interval. Exhausting all triples from the \(31\) lines, solving the \(3\times3\) linear systems over \(\mathbb Q\), and retaining solutions with \(0<a<1/4\) and \((x,y)\in[0,1]^2\) yields **only \(a=1/6\)** (twelve qualifying line triples). No coincident parallel lines can arise as \(a\) varies because the slopes of lines with different \(j\) are different and parallel lines with the same \(j\) have fixed distinct offsets. Therefore (1) is quadratic separately on \((0,1/6)\) and \((1/6,1/4)\), and continuous through their boundaries.

Exact clipping gives
\[
\begin{array}{c|ccccc}
a&0&1/12&1/6&5/24&1/4\\\hline
C(a)&1/3&2/9&-1/9&-5/18&-1/3.
\end{array}
\]
Three nodes on each piece uniquely determine a polynomial of degree at most two. Interpolation yields \(1/3-16a^2\) on the first piece and \(-1/3+32(1/4-a)^2\) on the second, including all endpoints by continuity. The certificate also checks seven additional interior parameter values, including values from both pieces; those extra tests are not used as the proof of the polynomial identity.

**4. Independence parameter and entropy.** On \([0,1/6]\), the correlation is strictly decreasing from \(1/3\) to \(-1/9\) and has unique zero \(1/(4\sqrt3)\). On \([1/6,1/4]\) it remains strictly negative. The Walsh inversion from Step 1 proves both necessity and sufficiency for a uniform four-block distribution. At irrational \(\alpha\), the standard Anzai skew transformation is uniquely ergodic under Haar measure. Its entropy is zero: to trace \(n\) iterates to tolerance \(\epsilon\), an \(O(\epsilon/n)\) horizontal grid and \(O(\epsilon)\) vertical grid suffice, giving only \(O(n\epsilon^{-2})\) Bowen covering cells. Entropy cannot increase under a factor map. A nondegenerate iid fair process has entropy \(\log2>0\), so the binary process cannot be Bernoulli. Finally the Walsh formula has eight even-parity words each of probability \((1+C)/16\) and eight odd-parity words each \((1-C)/16\); direct summation gives the Shannon-entropy identity and its equality criterion.

## Verification

Run `python3 verify.py` with Python 3 and no third-party dependencies. The program enumerates all qualifying triple intersections among the \(31\) boundary lines using exact rational determinants, asserts the sole interior critical parameter is \(1/6\), and computes each polygon area exactly by half-plane clipping. It verifies the five rational interpolation values and seven additional rational values, and at each point checks that the \(560\) clipped polygon areas sum exactly to \(1\). Its successful output begins with `VERIFY_OK`. The mathematical reason that this finite certificate extends to all real parameters is the quadratic-polynomial and complete-breakpoint argument given above.

## Relationship to prior work

Bernardo, Courbage, and Truong (2004), arXiv:nlin/0410066v1, study the same Anzai skew product and half-circle binary observable. They establish pairwise independence, zero entropy, and derive general multiple Fourier-sum expressions for even moments of Birkhoff sums, notably their equation (2.0.7). Their Fourier framework encompasses the formal inputs to four-fold correlations; those ingredients and any consequences explicitly established there are not claimed as new. The present narrower contribution is the **evaluated finite-window distribution**, its *complete* piecewise-quadratic dependence on \(\alpha\), and the precise irrational values at which the length-four word distribution is uniform. Unlike an unevaluated general moment series, these identify the exact transition and all equality cases directly.

Courbage and Hamdan (2001) investigate how low-order marginals can agree for very different stationary processes. That general existence phenomenon motivates but does not provide the evaluated phase diagram for this fixed toral map. Dooley and Quas (2005) discuss analogous zero-entropy pairwise-independent skew-product examples, without the present four-word classification.

## Limitations

The finding gives the Haar-stationary four-*consecutive*-observation law, not the complete family of correlations at arbitrary four indices. The prior paper's general moment formula can be specialized in principle; unrecognized previously published explicit evaluations or a stronger specialization of it pose a historical-priority risk. The exact rational computation verifies a finite combinatorial identity together with a complete piecewise-polynomial breakpoint argument; finite sampling alone would not prove an all-parameter result. Independent expert audit and independent historical-priority certification have not been performed.

## References

1. M. Bernardo, M. Courbage and T. T. Truong, *Multidimensional Gaussian sums arising from distribution of Birkhoff sums in zero entropy dynamical systems*, arXiv:nlin/0410066v1, first publicly posted 29 October 2004. https://arxiv.org/abs/nlin/0410066
2. M. Courbage and D. Hamdan, *A family of stationary processes with infinite memory having the same p-marginals. Ergodic and spectral properties*, Colloquium Mathematicum 90 (2001), 159–179. https://doi.org/10.4064/cm90-2-2
3. A. H. Dooley and A. Quas, *Approximate transitivity for zero-entropy systems*, Ergodic Theory and Dynamical Systems 25 (2005), 443–453; https://doi.org/10.1017/S0143385704000525.
