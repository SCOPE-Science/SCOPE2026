# Exact parameter census and covariance signs for quadratic near-identity permutations

## Finding
Fix an odd prime \(p\) and an integer \(N\ge2\), and write \(L=N-1\). For each parameter \(a\in\mathbb Z/p^L\mathbb Z\), consider the permutation of \(\mathbb Z/p^N\mathbb Z\)
\[
 f_a(x)=x+p(x^2-a)\pmod{p^N}.
\]
Let \(C_t(a)\) denote the number of *unoriented primitive cycles* of exact length \(p^t\), with \(0\le t\le L\). There are no other cycle lengths. Put \(R_0(a)=1\) and, for \(1\le j\le L\),
\[
 R_j(a)=\#\{x\bmod p^j:x^2\equiv a\pmod{p^j}\}.
\]
The entire cycle vector is given by the triangular formula
\[
 C_0(a)=pR_L(a),\qquad
 C_t(a)=pR_{L-t}(a)-R_{L-t+1}(a)\quad(1\le t\le L).
 \tag{1}
\]
Its exact parameter-frequency distribution has \(N+\lceil L/2\rceil\) distinct cycle vectors. The vector for \(a=0\) occurs once. For each \(0\le h<L\), parameters with \(v_p(a)=h\) form the following disjoint types: when \(h\) is odd, one cycle vector occurs \((p-1)p^{L-h-1}\) times; when \(h\) is even, the quadratic-residue and nonresidue leading-unit classes yield two different vectors, each occurring \((p-1)p^{L-h-1}/2\) times. Their vectors are obtained from (1) using the root-count formula in the proof. These are all the types, with no duplications.

For a *uniform* choice of \(a\) modulo \(p^L\), set \(b=(p-1)/p\). The complete first and second moments are
\[
 \mathbb E C_0=p,\qquad \mathbb E C_t=p-1\quad(1\le t\le L),
\]
\[
 \operatorname{Var}(C_0)=p^2bL,\qquad
 \operatorname{Var}(C_t)=b\bigl(1+(p-1)^2(L-t)\bigr)\quad(1\le t\le L),
 \tag{2}
\]
\[
 \operatorname{Cov}(C_0,C_t)
   =pb\bigl((p-1)(L-t)-1\bigr)\quad(1\le t\le L),
\]
\[
 \operatorname{Cov}(C_s,C_t)
   =b(p-1)\bigl((p-1)(L-t)-1\bigr)
 \quad(1\le s<t\le L). \tag{3}
\]
In particular, \(C_L\), the longest-cycle count, is *strictly negatively correlated with every shorter-cycle count*, whereas every pair \(C_s,C_t\) with \(s<t<L\) has *strictly positive* covariance.

There is also a heavy-tailed common limiting law. Couple the parameters by choosing a uniform Haar element \(a\in\mathbb Z_p\) and reducing it at each level. As \(N\to\infty\), for each fixed finite set of positive indices \(t\), the cycle counts \(C_t(a)\) converge almost surely to one and the same nonnegative random variable \(W\), where
\[
 \Pr\bigl(W=2(p-1)p^s\bigr)=\frac{p-1}{2p^{2s+1}}\quad(s\ge0),
 \qquad
 \Pr(W=0)=\frac{p+2}{2(p+1)}.
 \tag{4}
\]
Here \(\mathbb EW=p-1\), but \(\mathbb EW^2=\infty\). In the same coupling \(C_0(a)\to pW/(p-1)\) almost surely. Thus the linearly growing finite-level variances in (2) are genuinely produced by rare high-valuation parameters and do not contradict almost-sure stabilization.

## Assumptions and scope
All assertions are unconditional for every odd prime \(p\), every \(N\ge2\), and the *uniform parameter ensemble* \(a\in\mathbb Z/p^{N-1}\mathbb Z\). Although the map is defined modulo \(p^N\), it depends only on \(a\bmod p^{N-1}\). Fixed points are counted as cycles of length one. The covariance is taken across parameters, not across randomly sampled states. The limiting law uses a single Haar-coupled parameter across levels. No conclusion is asserted for \(p=2\), for arbitrary higher-degree displacement polynomials, or for more general ensembles.

## Proof
**1. Exact local period lemma.** Let \(g(X)=X+pQ(X)\) with \(Q\in\mathbb Z[X]\), \(p\) odd. At an integer \(x\), set \(d=g(x)-x\) and \(v=v_p(d)\ge1\), allowing \(v=\infty\). If \(v<\infty\), for the first \(p\) iterates \(x_i=g^i(x)\) put \(\Delta_i=x_i-x\). Induction gives \(\Delta_i\equiv id\pmod{p^{v+1}}\), and \(v_p(\Delta_i)\ge v\). The integral polynomial Taylor identity
\[
 Q(x+z)=Q(x)+Q'(x)z+z^2 B(x,z),\qquad B\in\mathbb Z[X,Z],
\]
gives
\[
 g^p(x)-x=pd+pQ'(x)\sum_{i=0}^{p-1}\Delta_i
       +p\sum_{i=0}^{p-1}\Delta_i^2 B(x,\Delta_i).
\]
As \(p\) is odd, \(p\mid\sum_{i=0}^{p-1}i\); hence the second term is divisible by \(p^{v+2}\). The third has valuation at least \(2v+1\ge v+2\). Consequently \(g^p(x)-x\equiv pd\pmod{p^{v+2}}\), so \(v_p(g^p(x)-x)=v+1\). Every iterate \(g^{p^r}\) is again a polynomial congruent to \(X\) coefficientwise modulo \(p\); applying the same argument repeatedly shows
\[
 v_p\bigl(g^{p^r}(x)-x\bigr)=v+r.
\]
Moreover, for \(p\nmid q\), the same one-step congruence gives \(v_p(g^q(x)-x)=v\); apply it to \(g^{p^r}\) for arbitrary times \(p^rq\). Thus the least period modulo \(p^N\) is exactly \(p^{\max(N-v,0)}\), with a stationary point when \(d=0\). This also proves that \(g\) is a permutation: its reduction modulo \(p\) is the identity, while \(g(x)-g(y)=(x-y)(1+p(x+y))\) for the quadratic specialization, and the last factor is a unit modulo \(p^N\).

For \(g=f_a\), \(v=1+v_p(x^2-a)\). The number \(F_t(a)\) of points whose periods divide \(p^t\) is therefore
\[
 F_t(a)=p^{t+1}R_{L-t}(a)\quad(0\le t\le L),
\]
including \(R_0=1\). Since \(F_0=C_0\) and \(F_t-F_{t-1}=p^t C_t\), equation (1) follows.

**2. Quadratic-root and type classification.** For \(1\le j\le L\), write \(h=\min\{v_p(a),j\}\), interpreting \(v_p(0)=\infty\). Then
\[
 R_j(a)=
 \begin{cases}
 p^{\lfloor j/2\rfloor},& h=j,\\
 0,&h<j\text{ odd},\\
 2p^{h/2},&h<j\text{ even and }a/p^h\text{ a square unit modulo }p,\\
 0,&h<j\text{ even and }a/p^h\text{ a nonsquare unit modulo }p.
 \end{cases} \tag{5}
\]
The first case counts roots of \(x^2\equiv0\); the others follow by comparing valuations and Hensel lifting the two simple unit roots when present. Hence every parameter is classified by the first nonzero \(p\)-adic digit and, when its valuation is even, by the Legendre symbol. For distinct classes, the sequences \((R_1,\ldots,R_L)\) are distinct: the first level beyond the smaller valuation separates them (a smaller even-square class has \(2p^s\) roots instead of \(p^s\), whereas an odd or even-nonsquare class eventually has none). The all-zero parameter is distinguished at the last level. Equation (1) is invertible given \(R_0=1\), so the cycle vectors are distinct as well. Counting units in each valuation stratum gives the listed frequencies and their sum \(p^L\).

**3. Root-count martingale and covariance.** For a uniform parameter \(a\bmod p^L\), the sequence \(R_j\), \(0\le j\le L\), is a martingale with respect to the digits of \(a\): each root modulo \(p^j\) has \(p\) possible lifts, and for each lift exactly one choice of the next digit of \(a\) makes the lift a root. In particular \(\mathbb ER_j=1\).

For \(j\ge1\), the invertible substitution \((u,v)=(x-y,x+y)\) modulo \(p^j\) transforms \(x^2\equiv y^2\) into \(uv\equiv0\). The pair count is
\[
 p^j+j(p-1)p^{j-1},
\]
because \(u=0\) contributes \(p^j\), and each of the \(j\) possible valuations of nonzero \(u\) contributes \((p-1)p^{j-1}\). Thus
\[
 \mathbb E R_j^2=1+j\frac{p-1}{p},\qquad
 \operatorname{Cov}(R_j,R_k)=\frac{p-1}{p}\min(j,k),
 \tag{6}
\]
the latter from the martingale conditional-expectation identity. Substitute \(C_0=pR_L\), \(C_t=pR_{L-t}-R_{L-t+1}\) into (6) to obtain (2)–(3). At \(t=L\), the bracket in (3) equals \(-1\); for \(t<L\), it is at least \(p-2>0\). This proves both sharp signs.

**4. Haar limit.** Almost surely \(a\ne0\) as a \(p\)-adic integer. Its root counts eventually stabilize at \(R_\infty=2p^s\) when \(v_p(a)=2s\) with square leading unit, and otherwise at zero. Hence (1) gives \(C_t\to(p-1)R_\infty\) for every fixed positive \(t\), and \(C_0\to pR_\infty\). The event \(\{v_p(a)=2s,\ a/p^{2s}\text{ is a square unit}\}\) has Haar measure \((p-1)/(2p^{2s+1})\). Summing proves (4). Its first moment is \(p-1\); each nonzero atom contributes the same positive amount to the second moment, forcing divergence. No finite-level enumeration is used to justify the infinite-level assertions.

## Verification
The accompanying standalone `verify.py` computes each permutation's complete cycle graph directly for 2,606 combinations of prime, level and parameter, with odd primes \(3,5,7,11\) and sufficiently small levels. It also verifies exact first and second moments, every type multiplicity, and the type-count formula in 14 complete parameter ensembles using exact rational arithmetic. Run `python verify.py` from a directory containing the file; it requires only Python's standard library. The direct tests are consistency checks, not proofs of statements for all primes or levels. All infinite assertions follow from the proof above.

## Relationship to prior work
Panraksa and Tangboonduangjit (first posted 6 May 2026) classify fixed points and exact periods of Chebyshev maps over odd prime-power rings. They motivate exact prime-power polynomial cycle censuses, but the Chebyshev maps and their power-map parametrizations differ from this quadratic near-identity parameter ensemble. Shen (first posted 6 August 2026) treats universal root statistics for independent-coefficient random \(p\)-adic polynomials at large degrees, rather than fixed quadratic shifts and their induced cycle-covariance matrix. Caruso studies random \(p\)-adic polynomial roots and higher correlations in a different coefficient ensemble. The general 17 November 2026 time-one-map theorem of Terskii *does* imply the period of each individual state for maps congruent to identity modulo \(p\); individual period growth and quadratic-root formulas are consequently **not** claimed as new. The contribution asserted here is the **complete parameter-frequency distribution, the exact across-parameter covariance matrix with its strict sign dichotomy, and the common heavy-tailed limiting cycle-count law**.

## Limitations
This is a one-parameter quadratic family at odd primes. The same formulas need not hold for general polynomial perturbations, nonuniform parameters, or \(p=2\). Finite computational checks do not certify the infinite statements. A more general source could imply portions of the parameter statistics indirectly; that priority risk is distinct from the proof of the stated result. No independent mathematical audit has been performed.

## References
1. C. Panraksa and A. Tangboonduangjit, *Fixed points and exact periods of Chebyshev polynomials modulo odd prime powers*, arXiv:2605.04417, first version 6 May 2026. https://arxiv.org/abs/2605.04417
2. J. Shen, *Universality for Random p-adic Polynomials and Random Matrices Via the Resultant Distribution Method*, arXiv:2608.06576, first version 6 August 2026. https://arxiv.org/abs/2608.06576
3. X. Caruso, *Where are the zeroes of a random p-adic polynomial?*, arXiv:2110.03942, first version 8 October 2021. https://arxiv.org/abs/2110.03942
4. K. Terskii, *Orbits of p-adic flows: balls, time-one maps and minimal group actions*, arXiv:2611.24982v1, 17 November 2026. https://arxiv.org/html/2611.24982v1
