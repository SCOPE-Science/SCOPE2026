# A double-exponential resolvent scale and complete local power set beyond summable shift weights

## Finding
Let \(1\le p<\infty\), or let the underlying space be \(c_0\), over the complex scalars. On canonical basis vectors define the compact backward shift
\[
 Be_0=0,\qquad Be_j=\frac{1}{\log(j+e)}e_{j-1}\quad(j\ge1).
\]
For any \(x\ne0\) define the Douglas--Yang local resolvent exponent
\[
 k_B(x)=\limsup_{\lambda\to0}\frac{\log\|(\lambda I-B)^{-1}x\|}{\log\|(\lambda I-B)^{-1}\|}.
\]
The shift is quasinilpotent and has the complete power set \(\{k_B(x):x\ne0\}=[0,1]\), although the weights belong to no finite \(\ell^q\) class. More precisely, with \(t=1/|\lambda|\),
\[
 \log\|(\lambda I-B)^{-1}\|\sim\frac{e^t}{t}.
\]
For every \(a>0\), the concrete vector \(x^{(a)}_j=\exp[-aj/\log(j+e)]\) belongs to every specified space and obeys
\[
 k_B(x^{(a)})=e^{-a},\qquad
 \log\|(t^{-1}I-B)^{-1}x^{(a)}\|\sim\frac{e^{t-a}}{t}.
\]
The exponents zero and one are realized respectively by \(e_0\) and \(y_j=\exp[-j/\log^2(j+e)]\).

## Assumptions and scope
All logarithms are natural, indices start at zero, and the domain is complex \(\ell^p(\mathbb N_0)\) with \(1\le p<\infty\) or complex \(c_0(\mathbb N_0)\) with supremum norm. The resolvent is defined for every nonzero complex \(\lambda\) because \(B\) is quasinilpotent. The notation \(f(t)\sim g(t)\) means their ratio tends to one as \(t\to\infty\). The parameter \(a>0\) is arbitrary but fixed in each local asymptotic statement. In the formula for the operator norm, the asymptotic is uniform in the argument of \(\lambda\).

## Proof
**1. Compactness and the norm of each power.** Put
\[
 P_k=\prod_{j=1}^{k}\frac1{\log(j+e)},\quad P_0=1,
 \qquad F(k)=\sum_{j=1}^{k}\log\log(j+e).
\]
The weights are positive, strictly decreasing, and tend to zero, hence \(B\) is compact. Because each \(k\)-fold product beginning at index \(j\ge k\) is at most the one beginning at \(k\), \(\|B^k\|=P_k=e^{-F(k)}\). As \(F(k)/k\to\infty\), the spectral radius is zero. In particular \((\lambda I-B)^{-1}=\sum_{k\ge0}\lambda^{-k-1}B^k\) in operator norm for every \(\lambda\ne0\).

**2. Discrete saddle lemma.** For fixed \(a\ge0\), define
\[
 H_a(t)=\max_{k\ge0}\left(k\log t-F(k)-\frac{ak}{\log(k+e)}\right).
\]
Then
\[
 H_a(t)\sim\frac{e^{t-a}}{t}\qquad(t\to\infty).
\]
To verify this, write \(q(x)=x/\log(x+e)\). For large \(k\), successive differences of the quantity maximized equal
\[
 \log t-\log\log(k+1+e)-\frac a{\log k}
      +O_a\!\left(\frac1{\log^2 k}\right).
\]
Here \(\log\log(k+1+e)+a/\log k\) is ultimately strictly increasing, because its derivative has sign \(1-a/\log k+o(1)\). Thus the maximizing index is eventually unique up to an adjacent-integer tie and satisfies \(\log k=t-a+o(1)\). Summation by parts (or integration of \(\log\log x\)) gives
\[
 F(k)=k\log\log k-\operatorname{li}(k)+o(k/\log k),
 \qquad \operatorname{li}(k)\sim k/\log k.
\]
Substituting \(\log k=t-a+o(1)\) into the maximizing expression, the terms \(a k/t\) and \(-a k/t\) cancel and the remaining term is \(k/t\,(1+o(1))\). Hence the displayed asymptotic. Any finitely many exceptional small indices give only \(O(\log t)\) and cannot maximize as \(t\to\infty\).

We will also use a max-term-to-sum principle:
\[
 \log\sum_{k\ge0}\exp\left(k\log t-F(k)-a q(k)\right)
  =H_a(t)+o(e^t/t).
\]
Indeed, the sum through \(K=\lceil e^{2t}\rceil\) is at most \((K+1)e^{H_a(t)}\), whose logarithmic overhead is \(O(t)\). For \(k>K\), \(\log(k+e)>2t\), so the successive summands decrease by at least the factor \(t/\log(k+1+e)<1/2\) (and the decreasing factor \(e^{-a(q(k+1)-q(k))}\) only helps). This tail is bounded by twice its first term, itself no larger than \(e^{H_a(t)}\). The reverse inequality follows from the largest term.

**3. Global resolvent growth.** Let \(t=1/|\lambda|\). The Neumann expansion yields
\[
 \|(\lambda I-B)^{-1}\|\le t\sum_{k\ge0}t^kP_k.
\]
For each \(k\), the coefficient of \(e_0\) in \((\lambda I-B)^{-1}e_k\) has modulus \(t^{k+1}P_k\), so the resolvent norm is at least \(t\max_k t^kP_k\), for every argument of \(\lambda\). Step 2 with \(a=0\) proves the stated uniform logarithmic asymptotic.

**4. A vector with any prescribed interior exponent.** Take \(a>0\) and \(x^{(a)}_j=e^{-a q(j)}\). It belongs to all \(\ell^p\) because \(q(j)/\log j\to\infty\), and belongs to \(c_0\). Its coordinates are nonnegative. For every \(k\) and every \(j\ge k\), the \(k\)-step product of weights ending at \(j\) is bounded by \(P_k\); therefore
\[
 \|B^k x^{(a)}\|\le P_k\|(x^{(a)}_j)_{j\ge k}\|.
\]
For \(1\le p<\infty\), there exists \(C_{a,p}\) such that, for all sufficiently large \(k\),
\[
 \sum_{j\ge k}e^{-pa q(j)}\le C_{a,p}\bigl(1+\log(k+e)\bigr)e^{-pa q(k)}.
\]
For completeness, on \(k\le j\le k^2\), \(q'(u)\ge c/\log(k+e)\) for \(k\le u\le k^2\), so this part is bounded by a geometric series of length scale \(O(\log k)\) times its initial term. For \(j>k^2\), \(q(j)\ge\sqrt j\) for large \(k\), and the remaining stretched-exponential tail is negligible compared with \(e^{-pa q(k)}\). On \(c_0\), simply use the monotonicity of \(q(j)\): the tail supremum equals \(e^{-a q(k)}\). Thus, in all cases, the logarithm of the tail norm differs from \(-a q(k)\) by \(O_{a,p}(\log\log(k+e))\). The Neumann expansion and the max-term principle imply the upper bound
\[
 \log\|(\lambda I-B)^{-1}x^{(a)}\|
 \le H_a(t)+o(e^t/t).
\]
For the lower bound take positive real \(\lambda=t^{-1}\); its zeroth output coordinate equals
\[
 t\sum_{k\ge0}t^kP_k e^{-a q(k)},
\]
which has logarithm \(H_a(t)+o(e^t/t)\). Step 2 gives the claimed positive-ray asymptotic and, together with the complex uniform upper bound and Step 3, the local exponent \(e^{-a}\).

**5. Endpoints and completeness.** Since \(Be_0=0\), \((\lambda I-B)^{-1}e_0=\lambda^{-1}e_0\), giving exponent zero. Let \(y_j=\exp[-j/\log^2(j+e)]\). This belongs to every \(\ell^p\) and \(c_0\), and the same zeroth-coordinate lower bound at the maximizer \(k\sim e^t\) of \(H_0(t)\) shows a logarithmic value \((1+o(1))e^t/t\): the penalty \(k/\log^2 k=o(e^t/t)\). The operator norm upper bound gives its exponent one. For any nonzero \(x\), \(\|R(\lambda)x\|\le\|R(\lambda)\|\|x\|\) gives \(k_B(x)\le1\). Conversely, \(\|R(\lambda)x\|\ge\|x\|/\|\lambda I-B\|\) shows \(k_B(x)\ge0\). Varying \(a\) across the positive reals produces every value strictly between zero and one, completing the classification.

## Verification
The proof rests on exact weighted-shift power norms, the saddle lemma, and the tail estimate; finite calculations are diagnostics only. The included standalone Python checker compares finite saddle maxima for \(t=6,8,10\) against the predicted asymptotic scales. It does not verify any infinite limit. All six public documents, the checker, and their embedded byte hashes are included in the same package.

## Relationship to prior work
Ignatev, *The power set of a quasinilpotent backward weighted shift* (first public 18 July 2026, arXiv:2607.16743), proves a full power set for strictly decreasing weights belonging to some finite \(\ell^q\), as stated in its public abstract. The current weights fail \(\ell^q\) summability for **every** finite \(q>0\); that hypothesis does not imply this example. Hu--Ji, arXiv:2306.00387, treats certain backward weighted shifts under other hypotheses, and Ji--Zhang, arXiv:2305.09963, proves general properties of power sets. The exact non-summable logarithmic case with its doubly exponential resolvent scale and explicit exponent witnesses was not found in the compared accessible records. This comparison does not assert uniqueness or historical priority.

## Limitations
The result concerns one natural logarithmic weight family, not arbitrary non-summable weights. It proves logarithmic asymptotics of the operator and local resolvent norms, not exact multiplicative equivalents of the norms themselves. Full texts of the closest operator-theory papers could not be examined; abstract-level noncoverage cannot rule out an earlier theorem expressed differently.

## References
1. E. Ignatev, *The power set of a quasinilpotent backward weighted shift*, arXiv:2607.16743 (first public 2026-07-18), https://arxiv.org/abs/2607.16743.
2. C. Hu and Y. Ji, *Power Set of Some Quasinilpotent Weighted Shifts on \(\ell^p\)*, arXiv:2306.00387 (2023), https://arxiv.org/abs/2306.00387.
3. Y. Ji and Y. Zhang, *On the power set of quasinilpotent operators*, arXiv:2305.09963 (2023), https://arxiv.org/abs/2305.09963.
