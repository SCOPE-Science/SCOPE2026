# Exact density spectrum of least eventual tetration congruence-speed periods

## Finding
For every fixed integer radix \(r>1\) and every positive integer \(d\), the relative natural density \(\rho_d(r)\) of bases \(a\ge2\) coprime to \(r\) whose tetration congruence speed has **least eventual period exactly \(d\)** exists, is rational, and admits a finite formula. The same proportion holds relative to all prime bases. The rational vector gives more information than the previously known set of attainable periods and the single density of nonconstant speeds.

Write \(e_p=\nu_p(r)\) for primes \(p\mid r\). For an integer \(k\), set
\[
Q_p(k)=\begin{cases}1,&p\text{ odd},\ k\le1,\\p^{1-k},&p\text{ odd},\ k\ge2,\\1,&p=2,\ k\le2,\\2^{2-k},&p=2,\ k\ge3.\end{cases}
\]
For positive rational \(t\), define
\[
W_r(t)=\prod_{p\mid r}Q_p(\lceil e_pt\rceil)-\prod_{p\mid r}Q_p(\lfloor e_pt\rfloor+1),
\qquad
\mathcal T_r=\bigcup_{p\mid r}\left\{\frac{j}{e_p}:1\le j\le2e_p\right\}.
\]
Let \(\operatorname{den}(t)\) denote the positive reduced denominator of \(t\). The complete distribution is
\[
\boxed{\rho_d(r)=\sum_{\substack{t\in\mathcal T_r,\ t\le1\\\operatorname{den}(t)=d}}W_r(t)
+\frac{r}{r-1}\sum_{\substack{t\in\mathcal T_r,\ 1<t\le2\\\operatorname{den}(t)=d}}W_r(t).}
\]
In particular, \(\rho_d(r)>0\) precisely for \(d=1\) and the integers \(d\ge2\) dividing at least one \(e_p\), and \(\sum_d\rho_d(r)=1\).

For radix \(64\), the density vector at periods \(1,2,3,6\) is
\[
\left(\frac2{63},\frac{16}{63},\frac{40}{63},\frac5{63}\right).
\]
For radix \(144\), the density vector at periods \(1,2,4\) is
\[
\left(\frac{10}{143},\frac{120}{143},\frac1{11}\right).
\]

## Assumptions and scope
Integer tetration is \({}^{0}a=1\), \({}^{1}a=a\), and \({}^{h+1}a=a^{{}^{h}a}\). For integers \(a,r\ge2\) with \(\gcd(a,r)=1\), define the number of stable radix-\(r\) digits at height \(h\) by
\[
s_h^{[r]}(a)=\max\{j\ge0:{}^{h+1}a\equiv{}^h a\pmod{r^j}\},
\]
and the congruence-speed sequence by \(v_h^{[r]}(a)=s_h^{[r]}(a)-s_{h-1}^{[r]}(a)\). The least eventual period \(d_r(a)\) is the smallest positive period after some height, not the period of a least-stable digit. Ripà's exact-period theorem identifies \(d_r(a)\) with the reduced denominator of
\[
\lambda_r(a)=\min_{p\mid r}\frac{c_p(a)}{e_p},\quad
c_p(a)=\begin{cases}\nu_p(a^{p-1}-1),&p\text{ odd},\\\nu_2(a^2-1)-1,&p=2.\end{cases}
\]
The theorem here concerns all \(r>1\), including squarefree \(r\). For integer-base density, the denominator is \(\#\{2\le a\le X:\gcd(a,r)=1\}\), while for prime bases it is \(\pi(X)\); the finitely many prime divisors of \(r\) are excluded from the prime numerator. In each case the radix is held fixed while \(X\to\infty\).

## Proof
**1. Local valuation distributions.** For odd \(p\), the condition \(c_p(a)\ge k\) for a unit \(a\) is \(a^{p-1}\equiv1\pmod{p^k}\). Exactly \(p-1\) of the \((p-1)p^{k-1}\) reduced residues satisfy this. For \(p=2\), \(c_2(a)\ge k\) with \(k\ge2\) is equivalent to \(a\equiv\pm1\pmod{2^k}\), giving frequency \(2^{2-k}\). These calculations yield the stated \(Q_p(k)\). Residue conditions at distinct primes are independent by the Chinese remainder theorem.

**2. Exact atomic law of the minimum.** For each positive rational \(t\),
\[
\Pr(\lambda_r\ge t)=\prod_{p\mid r}Q_p(\lceil e_pt\rceil),\qquad
\Pr(\lambda_r>t)=\prod_{p\mid r}Q_p(\lfloor e_pt\rfloor+1).
\]
The difference is \(\Pr(\lambda_r=t)=W_r(t)\). Every positive atomic value belongs to \(\bigcup_{p\mid r}\{j/e_p:j\ge1\}\). Each equality involves only finitely many reduced congruence classes and so defines an actual natural density, not a heuristic probability.

**3. Geometric period-tail reduction.** For every \(t>1\), and all \(p\mid r\), both local thresholds occurring in \(W_r(t)\) lie where \(Q_p(k+e_p)=p^{-e_p}Q_p(k)\). At \(p=2\), this includes the boundary \(Q_2(2)=1\) and \(Q_2(3)=1/2\). Consequently
\[
W_r(t+1)=\frac1r W_r(t)\quad(t>1).
\]
Every atom \(t>1\) lies in a unique chain \(t_0,t_0+1,t_0+2,\ldots\) with \(1<t_0\le2\), and all members share their reduced denominator. Summing each chain gives \(rW_r(t_0)/(r-1)\). Atoms in \((0,1]\) must be retained separately, since the scaling identity need not hold at \(t=1\). The only necessary representative atoms have \(j\le2e_p\), yielding the displayed finite formula.

**4. Completeness, positivity and primes.** For any integer \(J>0\), the event \(\lambda_r>J\) is a finite union of reduced residue classes with probability \(\prod_{p\mid r}Q_p(Je_p+1)\), which tends geometrically to zero. This proves convergence of the countable atomic partition, \(\sum_d\rho_d(r)=1\), and existence of each period density. The prime number theorem in arithmetic progressions gives the same frequency in primes for each finite congruence event; the same geometric tail permits passage to the infinite union. The least-period identification is Ripà's exact floor-difference theorem. Its period-spectrum theorem supplies realization of every \(d\) dividing an exponent \(e_p\), while each local equality condition has positive density, hence every such period has positive density. No other period is possible.

**5. Exact examples.** In radix \(64=2^6\), \(c_2\ge2\) and \(\Pr(c_2=j)=2^{1-j}\) for \(j\ge2\), so grouping the progression \(j\bmod6\) gives the vector shown. For \(144=2^4 3^2\), the independent \(2\)-adic and \(3\)-adic tails give atomic masses \(W(1/2)=5/6\), \(W(3/4)=1/12\), \(W(1)=5/72\), \(W(5/4)=1/144\), \(W(3/2)=5/864\), \(W(7/4)=1/1728\), and \(W(2)=5/10368\). Applying the geometric tail factor \(144/143\) to atoms above one gives \(\rho_1=10/143\), \(\rho_2=120/143\), \(\rho_4=1/11\), as stated.

## Verification
Run `python3 verify_period_law.py` with Python 3 (standard library only). The script enumerates reduced residue classes modulo \(\prod_{p\mid r}p^{2e_p+1}\), computes local valuations independently using modular powers, and checks that each minimum-atom frequency at \(t\le2\) equals \(W_r(t)\), with the omitted upper tail separately counted. This is performed for radices \(4,9,36,64,72,144\), including 41,472 reduced residues at radix \(144\). Independent rational checks verify the full displayed vectors, the sum-to-one identities, geometric scaling and the previously known aggregate nonstabilization-density formulas. The script prints `TETRATION_PERIOD_DENSITY_OK`. The infinite proof is the residue argument and tail summation above; the finite checker alone does not prove it.

## Relationship to prior work
Ripà's public October 2026 note [1], in its question (c), explicitly asks for the density of each least eventual period. It already proves the period spectrum and the aggregate proportion of nonconstant-speed bases. The revised November 2026 manuscript [2], Theorems 3.3, 3.4 and 5.1, provides the key exact-period characterization and local valuation tails, but does not report the finite distribution vector for arbitrary \(r\). The present calculation develops those local ingredients into a period-resolved finite rational formula, including prime-relative frequencies and explicit mixed-radix examples. The earlier decimal congruence-speed paper [3] concerns constant speeds. The claimed contribution is the exact period-frequency classification, **not** independent discovery of the LTE criterion, period spectrum, or local tails.

## Limitations
This applies to bases coprime to the radix. It does not classify bases sharing some but not all prime divisors with \(r\), and it does not estimate the smallest base of a given period or yield a uniform error term for finite cutoff \(X\). The underlying eventual-speed characterization is taken as a stated theorem of [2]; the local residue calculations and geometric summation are reconstructed above. Equivalent unindexed calculations or consequences buried in other literature remain a priority risk. No independent mathematical audit is claimed.

## References
1. M. Ripà, *Nonconstant congruence speeds of integer tetration: period spectra, prime bases, explicit bounds, and densities*, Hexagon preprint 2610.00589v1 (initial deposit October 27, 2026), https://hexagonmath.org/2610.00589v1 ; full text also available at https://hub.valency.io/works/W_68wrv2du .
2. M. Ripà, *Nonconstant Congruence Speeds of Integer Tetration in Non-Squarefree Radices*, arXiv:2611.10018v1 (November 4, 2026), https://arxiv.org/abs/2611.10018 .
3. M. Ripà, *The congruence speed formula*, Notes on Number Theory and Discrete Mathematics 27 (2021), 43–61; lawful arXiv version arXiv:2208.02622, https://arxiv.org/abs/2208.02622 .
4. M. Ripà and G. Di Pietro, *A compact notation for peculiar properties characterizing integer tetration*, Notes on Number Theory and Discrete Mathematics 32 (2026), 477–496, https://nntdm.net/volume-32-2026/number-3/477-496/ .
