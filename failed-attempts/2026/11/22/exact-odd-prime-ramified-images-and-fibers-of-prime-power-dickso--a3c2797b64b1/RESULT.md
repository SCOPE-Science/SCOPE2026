# Exact odd-prime ramified images and fibers of prime-power Dickson maps

## Finding
Let \(p\ge5\) be prime and \(r\ge1\). For the first-kind Dickson polynomial \(D_n(X)=D_n(X,1)\), defined by \(D_0=2\), \(D_1=X\), and \(D_{n+2}=XD_{n+1}-D_n\), put \(F_r=D_{p^r}=D_p^{\circ r}\). For \(a\in\{0,\ldots,p-1\}\), set \(h(a)=2\) if \(a\equiv\pm2\pmod p\), and \(h(a)=1\) otherwise. The following hold simultaneously.

1. For all distinct \(x,y\in a+p\mathbb Z_p\),
   \[\nu_p(F_r(x)-F_r(y))=\nu_p(x-y)+r h(a).\]
   Each branch is a scaled isometry onto one full residue ball:
   \[F_r(a+p\mathbb Z_p)=F_r(a)+p^{1+r h(a)}\mathbb Z_p.\]
2. In particular, the full image is the disjoint union
   \[F_r(\mathbb Z_p)=\bigcup_{\substack{a\bmod p\\a\ne\pm2}}\big(F_r(a)+p^{r+1}\mathbb Z_p\big)\ \sqcup\ \big(2+p^{2r+1}\mathbb Z_p\big)\ \sqcup\ \big(-2+p^{2r+1}\mathbb Z_p\big).\]
   The two exceptional centers are exact, since \(F_r(2)=2\) and \(F_r(-2)=-2\).
3. For each integer \(k\ge1\), the number of distinct values of \(F_r\) modulo \(p^k\) and the normalized Haar measure of its full \(p\)-adic image are
   \[V_{p,r}(k)=(p-2)p^{\max(k-r-1,0)}+2p^{\max(k-2r-1,0)},\]
   \[\mu(F_r(\mathbb Z_p))=\frac{p-2}{p^{r+1}}+\frac2{p^{2r+1}}.\]
4. A residue \(y\pmod{p^k}\) is attained if and only if it belongs to the reduction of one of the displayed balls. If it is attained, its preimage count among the \(p^k\) input residues is exactly
   \[\#\{x\bmod p^k:F_r(x)\equiv y\pmod{p^k}\}=p^{\min(k-1,r h(y\bmod p))}.\]
   For all other residues this count is zero. The least positive additive period of the function \(x\mapsto F_r(x)\pmod{p^k}\) is \(p^{\max(1,k-r)}\).
5. Accordingly its ordered collision count at precision \(p^k\) is
   \[\sum_{y\bmod p^k}\#F_r^{-1}(y)^2=p^{k-1}\big((p-2)p^{\min(k-1,r)}+2p^{\min(k-1,2r)}\big).\]

## Assumptions and scope
The prime is odd and at least five; the exceptional prime three is excluded because an extra low-degree Taylor coefficient has nonunit denominator in the convenient normalization. The parameter of the Dickson polynomial is one, and the degree is exactly a positive prime power \(p^r\). Outputs are computed on the entire ring \(\mathbb Z_p\), not just units or periodic inputs. The same statements over \(\mathbb Z/p^k\mathbb Z\) use the natural reduction and all input residues. Formulae for infinite images refer to normalized additive Haar measure.

## Proof
**Polynomial identities.** The Dickson recurrence implies \(D_{mn}=D_m\circ D_n\) and \(D_p(X)\equiv X^p\pmod p\), so \(D_p\) preserves every input class \(a\pmod p\). The derivative satisfies
\[D_p'(X)=p\,U_{p-1}(X/2),\]
where \(U_{p-1}(X/2)\in\mathbb Z[X]\). Applying the substitution \(X=z+z^{-1}\) to the standard second-kind identity gives
\[U_{p-1}(X/2)\equiv(X^2-4)^{(p-1)/2}\pmod p.\]
Indeed \((z^p-z^{-p})/(z-z^{-1})\equiv(z-z^{-1})^{p-1}\pmod p\), and the substitution map is injective on polynomials. Thus \(D_p'(a)/p\) is a unit precisely when \(a\not\equiv\pm2\pmod p\). Moreover, \(D_p(2)=2\), \(D_p(-2)=-2\), and, since \(p\) is odd,
\[D_p'(\pm2)=p^2,\qquad \frac12D_p''(\pm2)=\pm\frac{p^2(p^2-1)}{12}.\]

**Noncritical branch.** Expand at an integer representative \(a\not\equiv\pm2\). In the Taylor polynomial \(D_p(a+pt)\), every coefficient of degree \(2,\ldots,p-1\) comes from a coefficient divisible by \(p\), because \(D_p(X)\equiv X^p\pmod p\); the degree-\(p\) term contributes \(p^pt^p\). Thus, for an integer polynomial \(R_a\) and a unit \(u_a=D_p'(a)/p\),
\[D_p(a+pt)=D_p(a)+p^2(u_at+pR_a(t)).\]
The map \(t\mapsto u_at+pR_a(t)\) is an isometry of \(\mathbb Z_p\): for distinct \(s,t\), its difference is \((s-t)(u_a+pH(s,t))\) with integral \(H\), hence has valuation \(\nu_p(s-t)\). Its reduction is the affine bijection \(u_at\) and successive base-\(p\) digit lifting proves it is onto. Therefore \(D_p\) contracts all distances within this branch by exactly \(p^{-1}\) and maps it onto \(D_p(a)+p^2\mathbb Z_p\).

**Critical branches.** At \(a=2\) and \(a=-2\), the linear coefficient is \(p^2\), the quadratic coefficient displayed above has valuation at least two because \(p\ge5\), and all higher Taylor coefficients in degrees below \(p\) are divisible by \(p\). Hence for each sign there is \(R_\pm\in\mathbb Z[t]\) such that
\[D_p(\pm2+pt)=\pm2+p^3(t+pR_\pm(t)).\]
The normalized map is again of the form identity plus \(p\) times an integral polynomial, hence is a bijective isometry of \(\mathbb Z_p\). Thus the critical branch contracts distances by exactly \(p^{-2}\) and fills exactly \(\pm2+p^3\mathbb Z_p\). For any other integer representative of the same critical class, the image ball is unchanged, and the distance identity is unchanged by translating its coordinate.

**Iteration, periods, and counting.** Because \(D_p(x)\equiv x\pmod p\), all successive iterates remain in their initial class, so the preceding exact contraction factors multiply. A surjective scaled isometry maps any smaller input ball bijectively onto the corresponding smaller output ball: the distance equality identifies its preimage by distance from the center. Thus the one-step branch property remains valid on each successive image ball, and induction gives item 1. Output classes are distinct modulo \(p\), and the critical centers are fixed, establishing item 2. Reducing a ball of depth \(1+rh\) modulo \(p^k\) gives \(p^{\max(k-1-rh,0)}\) outputs and \(p^{\min(k-1,rh)}\) inputs per output. Summation proves the image, fiber, measure and collision formulae.

For a global additive input period \(T\), the equality \(F_r(x+T)\equiv F_r(x)\pmod p\) forces \(p\mid T\), since \(F_r(x)\equiv x\pmod p\). For \(p\mid T\), the distance identity gives valuation \(\nu_p(T)+r\) for any noncritical input class. Consequently the smallest period has \(\nu_p(T)=\max(1,k-r)\); the two critical branches have greater valuation, so they impose no additional condition. This proves the stated least period.

## Verification
The included `check_dickson.py` uses only Python's standard library, computes exact integer Dickson coefficients and modular iterates, and compares all input-to-output frequencies to the asserted branch balls and fiber counts. Tested ranges: \(p=5\) through precision \(5^6\), \(p=7\) through \(7^5\), \(p=11\) through \(11^4\), and \(p=13\) through \(13^3\), with two or three iterations. The checker recorded 170481 input-value checks and 4680 independent distance assertions. These finite checks are diagnostics; the proof above establishes all primes, iterations and precisions in scope.

## Relationship to prior work
Bremser and Gomez-Calderon (1991) study first-kind Dickson value sets over Galois rings. Their Theorem 5 already determines noncritical preimage counts, and their Lemmas 9–10 address critical residues, but their Theorem 11 bounds rather than exactly evaluates the complete image size in the \(p\mid d\) case. The new content here is the **exact full critical image**, all finite-level critical fibers, and the global iteration and period laws, for every \(d=p^r\) at \(p\ge5\). Gassert (2012) studies finite-field Chebyshev functional graphs, not these ramified prime-power image counts. Panraksa–Tangboonduangjit (2026) analyze periodic points and exact periods modulo odd prime powers, distinct from the full all-input image and preimage distributions here. Relevant nearby work on \(p=2\) iterated Dickson maps addresses the excluded prime and does not imply this odd-prime theorem.

## Limitations
This treats only parameter one and degrees exactly \(p^r\), not arbitrary multiples of \(p\), general Galois rings, or \(p=2,3\). It does not classify the functional-graph trees, pointwise orbit lengths, or general Dickson polynomial composition systems. Historical priority could be affected by an equivalent implicit specialization of general Galois-ring polynomial value-set results; the closest explicit theorem from 1991 supplied bounds, not these exact critical fibers. No independent mathematical audit has been performed.

## References
- P. S. Bremser and J. Gomez-Calderon, “Value Sets of Dickson Polynomials over Galois Rings,” *Journal of Number Theory* **38** (1991), 240–250, DOI: `10.1016/0022-314X(91)90087-R`; full-text accessible at https://www.academia.edu/48986625/Value_sets_of_Dickson_polynomials_over_Galois_rings.
- T. A. Gassert, “Chebyshev Action on Finite Fields,” arXiv:1209.4396, first publicly posted September 20, 2012, https://arxiv.org/abs/1209.4396.
- C. Panraksa and A. Tangboonduangjit, “Fixed points and exact periods of Chebyshev polynomials modulo odd prime powers,” arXiv:2605.04417, https://arxiv.org/abs/2605.04417.
