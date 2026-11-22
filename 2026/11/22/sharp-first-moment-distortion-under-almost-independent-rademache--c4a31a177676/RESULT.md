# Sharp first-moment distortion under almost-independent Rademacher laws

## Finding
For every integer \(n\ge2\) and every joint law of \(n\) fair signs whose every \(n-1\) coordinates are independent, there is a unique \(\theta\in[-1,1]\) such that
\[
\mathbb P_\theta(\varepsilon=e)=2^{-n}\bigl(1+\theta\prod_{j=1}^{n}e_j\bigr),\qquad e\in\{-1,1\}^{n}.
\]
For arbitrary nonzero real or complex coefficient vectors \(a\), define the first-moment norm \(N_\theta(a)=\mathbb E_\theta|\sum_j a_j\varepsilon_j|\) and let \(N_0\) denote the independent-sign norm. Then the **exact** extreme ratios are
\[
\sup_{a\ne0}\frac{N_\theta(a)}{N_0(a)}=1+c_n|\theta|,
\qquad
\inf_{a\ne0}\frac{N_\theta(a)}{N_0(a)}=1-c_n|\theta|,
\quad c_n=\begin{cases}0,&n\ \text{odd},\\1/(n-1),&n\ \text{even}.\end{cases}
\]
Both extremes are attained by real coefficients of equal nonzero absolute magnitude, with a single sign change switching the extremes when \(n\) is even and \(\theta\ne0\). In particular, the uniform measure on just one parity half of the sign cube preserves **every** first moment exactly in odd dimension; in even dimension its maximum relative error is precisely \(1/(n-1)\). The exceptional even case \(n=2\) permits a zero lower norm, whereas all even \(n\ge4\) remain injective.

## Assumptions and scope
Signs take values in \(\{-1,1\}\), their coordinates are individually fair and every marginal on at most \(n-1\) coordinates is the uniform product law. Expectations above use probability measures, not unnormalized sums. Real or complex coefficients are allowed, with absolute value the ordinary scalar modulus. The assertion is an exact relative comparison of these specified norms on the fixed coordinate space; no claim about optimal Banach–Mazur distance under arbitrary linear coordinate changes is made. No inequality for general non-first moments is asserted.

## Proof
**Classification of the law.** For each subset \(S\subseteq\{1,\dots,n\}\), let \(\chi_S(e)=\prod_{j\in S}e_j\). Walsh inversion expresses any probability mass function as \(2^{-n}\sum_S \mathbb E\chi_S(\varepsilon)\chi_S(e)\). Fair \((n-1)\)-wise independence makes every nonempty proper coefficient vanish; the empty coefficient is one. Only \(\theta=\mathbb E\prod_j\varepsilon_j\) remains. Nonnegativity of both parity-class masses is exactly \(|\theta|\le1\), proving the claim and its converse.

**Odd dimensions.** If \(n\) is odd, complementation \(e\mapsto-e\) interchanges the two parity classes while leaving \(|\sum_j a_je_j|\) unchanged. Therefore its top Walsh coefficient \(\Delta(a)=\mathbb E_0[(\prod_j\varepsilon_j)|\sum_j a_j\varepsilon_j|]\) vanishes. Hence \(N_\theta=N_0\) pointwise for every \(\theta\).

**Even dimensions at least four.** Write \(E_+(a)\) and \(E_-(a)\) for the normalized means of \(|\sum_j a_je_j|\) over the respective parity classes. For every sign vector \(e\), let \(e^{(j)}\) flip its \(j\)-th sign and put \(S(e)=\sum_j a_je_j\). The exact vector identity
\[
(n-2)S(e)=\sum_{j=1}^nS(e^{(j)})
\]
and the triangle inequality imply \((n-2)|S(e)|\le\sum_j|S(e^{(j)})|\). For fixed \(j\), flipping the \(j\)-th sign bijects the two equally sized parity classes. Averaging over each class gives
\[
(n-2)E_+(a)\le nE_-(a),\qquad(n-2)E_-(a)\le nE_+(a).
\]
Since \(E_++E_->0\) for \(a\ne0\), subtracting and rearranging these inequalities yields
\[
\frac{|E_+(a)-E_-(a)|}{E_+(a)+E_-(a)}\le\frac1{n-1}.
\]
As \(N_0=(E_++E_-)/2\) and \(N_\theta=N_0+\theta(E_+-E_-)/2\), both desired bounds follow.

**Sharpness.** Take every \(a_j=1\) and write \(n=2m\). On the parity class whose number \(k\) of negative signs satisfies \(k\equiv m-1\pmod2\), one has \(S(e)=n-2k\ne0\), with \(|S(e)|\ge2\). Every one-coordinate flip changes \(S(e)\) by exactly \(2\) in magnitude. All the resulting \(S(e^{(j)})\) therefore have the same weak sign as \(S(e)\). Consequently the preceding triangle inequality is an equality **for each** sign vector in that class, so its normalized mean is \(n/(n-2)\) times the opposite class's mean. The displayed absolute quotient is exactly \(1/(n-1)\). Changing the sign of any one coefficient interchanges the parity classes and reverses \(\Delta\), attaining both claimed extrema for any nonzero \(\theta\). For \(\theta=0\) every ratio equals one.

**The case \(n=2\).** For two fair signs with joint-product expectation \(\theta\), the independent norm and top Walsh coefficient of a coefficient pair \((a_1,a_2)\) are
\[
N_0=\tfrac12(|a_1+a_2|+|a_1-a_2|),\qquad
\Delta=\tfrac12(|a_1+a_2|-|a_1-a_2|).
\]
The elementary bound \(|\Delta|\le N_0\) is sharp when \(a_1=a_2\ne0\), and reversing one coefficient switches its sign, proving the formula with \(c_2=1\). Thus the result holds for all \(n\ge2\).

## Verification
The attached `check.py` is a standard-library exact-integer diagnostic. Run `python check.py`. It enumerates all signs in dimensions \(2\) through \(10\), and tests parity inequalities, odd-dimensional equality, and even-dimensional flat-vector sharpness across a finite family of rational coefficient vectors. It prints `PARITY_KHINTCHINE_EXACT_OK 1547`. These tests are supplementary: the universally quantified conclusions follow from the analytic proof above.

## Relationship to prior work
Dai and Kosov (arXiv:2611.05930, initially submitted 4 November 2026) study probabilistic discretization of finite-dimensional \(L^p\) norms using independent sampling, including the first-moment endpoint. Their stated sample-count theorem does not give this exact parity-conditioned deterministic error or the classification of nearly independent sign laws. Pass and Spektor (arXiv:1708.08775) study Khintchine constants under \(k\)-wise independence, principally higher moments with \(p\ge k\); this statement instead determines the exact relative \(L^1\) norm for every law at maximal proper independence. Two relevant published numerical and Fourier results are the published-finding corpus endpoint \(L^n/L^2\) theorem for \((n-1)\)-wise independent signs, and the published-finding corpus Walsh-inertia theorem for \(p\)-moment kernels; their accessible summaries do not state this norm-comparison extremum, but full-content coverage could not be decisively excluded.

## Limitations
The result treats only the first absolute moment of a **linear sign form**, not arbitrary Lipschitz functions on the cube, higher powers, or general partial-independence conditions. The \(n=2\) degenerate endpoint is explicitly separate. A search and comparison of relevant primary literature and indexed mathematical records found no identical all-dimension sharp relative first-moment statement, but absence from those searches is not a mathematical proof of publication novelty. The relevant full GitHub texts of indexed prior findings could not be inspected and remain a bibliographic risk. Independent mathematical review has not been performed.

## References
- F. Dai and E. Kosov, *Empirical approximation of \(L^p\) norms for \(p\in(1,2)\)*, arXiv:2611.05930v1, initially publicly posted 4 November 2026. https://arxiv.org/html/2611.05930v1
- B. Pass and S. Spektor, *On Khintchine type inequalities for \(k\)-wise independent Rademacher random variables*, arXiv:1708.08775v1 (2017), https://arxiv.org/pdf/1708.08775
- *Sharp endpoint Khintchine constants for next-to-independent Rademacher vectors*, published-finding corpus ID `2026/10/11/SCOPE-sharp-endpoint-khintchine-constants-for-next-to-independent-rade--93098a285ffa`.
- *Strict Walsh inertia of Rademacher \(p\)-moment kernels and exact sampling rigidity*, published-finding corpus ID `2026/11/17/SCOPE-strict-walsh-inertia-of-rademacher-p-moment-kernels-and-exact-sa--a1ee7602ac01`.
