# The two highest positive-shift overlaps of Apéry indices prime to five

## Finding

For the classical Apéry numbers \(A(n)=\sum_{j=0}^{n}\binom{n}{j}^{2}\binom{n+j}{j}^{2}\), let \(Q_r(h)\) count \(0\le n<5^r\) with both \(A(n)\) and \(A(n+h)\) nonzero modulo five, without reducing \(n+h\) modulo \(5^r\). Let \(\rho(h)=\lim_{r\to\infty}Q_r(h)/3^r\). The two highest values over positive shifts are \(2/3\) and \(4/9\). Precisely,

* \(\rho(h)=2/3\) if and only if \(h=2\cdot 5^i\) for some \(i\ge0\).
* \(\rho(h)=4/9\) if and only if \(h=2(5^i+5^j)\) or \(h=2(5^j-5^i)\), for \(0\le i<j\).

Every other positive shift has strictly smaller overlap. The difference family in the second item can also be written in ordinary digits as \(3\cdot5^i+4\sum_{i<t<j}5^t+5^j\).

## Proof

Gessel's Lucas congruence and the residues \((1,0,3,0,1)\) at digits \(0,1,2,3,4\) give the supported base-five digits \(D=\{0,2,4\}\). In particular odd shifts have no pairs, and \(Q_r(0)=3^r\). For an even shift \(h<5^r\), any allowed pair fits within \([0,5^r)\): if \(n+h\ge 5^r\), then \(5^r\le n+h<2\cdot5^r\), making its leading digit 1.

Write \(h/2=\sum_j \delta_j5^j\) in balanced base five, with \(\delta_j\in\{-2,-1,0,1,2\}\). Each digit is uniquely determined modulo five by the remaining integer, and iterating the subtraction and division terminates. If \(h<5^r\) is even, the representative for \(h/2\) fits in \(r\) places: the \(5^r\) digit strings give distinct integers by repeated reduction modulo five, all in \([-(5^r-1)/2,(5^r-1)/2]\), so they fill that interval. The digits of \(n\) and \(n+h\), divided by two, lie in \(\{0,1,2\}\); their coordinatewise differences must be the unique balanced digits \(\delta_j\). Each digit difference has exactly \(3-|\delta_j|\) ordered realizations, independently. Consequently, for \(r\) at least the ordinary digit length of \(h>0\), for even shifts
\[
\frac{Q_r(h)}{3^r}=\left(\frac{2}{3}\right)^{\#\{j:|\delta_j|=1\}}
\left(\frac{1}{3}\right)^{\#\{j:|\delta_j|=2\}}.
\]
This is the sparse deleted-digit intersection count in balanced notation; it is used as an input to the extremal classification, not claimed as a new intersection theorem.

A nonzero positive displacement must use at least one nonzero balanced digit, and the leading digit is positive because all smaller places combined have absolute value at most \((5^j-1)/2<5^j\). One digit of absolute value 1 gives exactly \(2/3\), with the sole digit positive. Any digit of absolute value 2 lowers the overlap to at most \(1/3\). Otherwise two nonzero digits give \(4/9\), three or more give strictly less, and the smaller of the two digits can have either sign. This yields precisely the sum and difference families and proves that no positive overlap lies between the two levels. The ordinary-base expansion of the difference follows from \(2(5^j-5^i)=5^j+3\cdot5^i+4\sum_{i<t<j}5^t\).

## Scope, prior work, and verification

The statistic is relative to the \(3^r\) supported indices at depth \(r\). Normalization by \(5^r\) instead gives limiting overlap zero; higher prime powers and multi-shift intersections are not addressed. The relevance of the extremal levels is to determine exactly which positive displacements retain the most supported indices at this sparse scale.

* Adamczewski and Bell, [*Diagonalization and Rationalization of algebraic Laurent series*](https://arxiv.org/abs/1205.4090), §9 and Figure 1, give the Apéry support automaton; Malik and Straub, [*Divisibility properties of sporadic Apéry-like numbers*](https://arxiv.org/abs/1508.00297), §1, state Gessel's Lucas congruence.
* Pedersen and Phillips, [*Intersections of Cantor sets: Hausdorff measure*](https://arxiv.org/abs/1203.4290), Proposition 1.1, the following multiplicative recurrence, Lemma 4.4 and Corollary 5.7, already give the general sparse deleted-digit intersection machinery. For \(D=\{0,2,4\}\) and \(t=h/5^r\) with even \(h\), the level-\(r\) full coincident cylinders are precisely the integer pairs counted above: their left endpoints are allowed integers scaled by \(5^{-r}\). Endpoint-only neighbor contacts cannot occur at this depth because left endpoint differences in integer units are even. The count is therefore a specialization of that framework. Kumar, Rani and Chugh, [*New 5-adic Cantor sets and fractal string*](https://doi.org/10.1186/2193-1801-2-654), Theorems 3.1–3.2, describe the same supported digits in the five-adic setting. These antecedents are distinguished from classifying the extremizing integer displacements and both runner-up families; historical priority is not certified.

The proof gives all shifts, including ties and boundary depths. The retained `verify.py` is finite corroboration of the ordinary-carry product and of both extremal levels. It is not the all-shift proof.
