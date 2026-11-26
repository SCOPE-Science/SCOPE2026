# Residue-class sign dichotomy for iterated Schemmel totients on prime powers

## Finding

Let \(m\ge2\) be an even integer. For each prime \(q\) in the interval \(m<q\le3m\), let \(e_q\) be the largest positive integer satisfying \(q^{e_q-1}(q-m)\le2m\). Set
\[
P_m=\prod_{q\le m\,\text{ prime}}q,\qquad
T_m=\prod_{m<q\le3m\,\text{ prime}}q^{e_q},\qquad B_m=\max\{m,T_m\}.
\]
Then **for every prime** \(p>m+B_m\) and **every integer** \(a\ge1\),
\[
D_m(p^a)>p^a\quad\Longleftrightarrow\quad \gcd(p-m,P_m)=1,
\]
and in the complementary case \(D_m(p^a)<p^a\). Hence none of these prime powers is \(D_m\)-perfect.

The exact relative density of abundant base primes, uniformly over **all** exponents, is
\[
\delta_m=\prod_{\substack{3\le q\le m\\q\text{ prime},\ q\nmid m}}\frac{q-2}{q-1}.
\]
With \(A_m(X)\) the number of primes \(p\le X\) for which **every** \(a\ge1\) satisfies \(D_m(p^a)>p^a\), and \(F_m(X)\) its deficient counterpart, we have
\[
A_m(X)=\delta_m\operatorname{Li}(X)+o(X/\log X),\qquad
F_m(X)=(1-\delta_m)\operatorname{Li}(X)+o(X/\log X).
\]
For example \(\delta_2=1\), \(\delta_4=1/2\), \(\delta_6=3/4\), and \(\delta_8=5/16\).

The case \(m=4\) admits a **complete**, cutoff-free prime-power sign classification:
\[
\begin{aligned}
&p\ge13,\quad a\ge1:\qquad
D_4(p^a)>p^a\ \Longleftrightarrow\ p\equiv2\pmod3,\\
&p\in\{2,3,5,7,11\},\quad a\ge1:\qquad D_4(p^a)<p^a.
\end{aligned}
\]
All other prime powers in the first display are strictly deficient, and no prime power is \(D_4\)-perfect.

## Assumptions and scope

For a fixed integer \(m\ge2\), the Schemmel totient \(L_m\) is the multiplicative arithmetic function satisfying \(L_m(1)=1\), \(L_m(0)=0\), and for a prime \(q\) and integer \(e\ge1\),
\[
L_m(q^e)=\begin{cases}0,&q\le m,\\q^{e-1}(q-m),&q>m.\end{cases}
\]
For \(n>1\), the iterated-sum function \(D_m(n)\) sums the positive iterates \(L_m(n),L_m^{(2)}(n),\ldots\), including a terminal \(1\) if present and stopping on first reaching \(0\) or \(1\); set \(D_m(1)=0\). This matches Defant's definition. An integer is called \(D_m\)-abundant, -perfect, or -deficient according as \(D_m(n)\) is greater than, equal to, or less than \(n\). The theorem makes no assertion about all integers: its quantitative asymptotic is over prime bases only.

## Proof

**1. Escape from small positive Schemmel values.** Write \(t>m\) with \(\gcd(t,P_m)=1\). In the prime-power factorization \(t=\prod q^{b_q}\), every \(q>m\), hence
\[
L_m(t)=\prod_{q\mid t}q^{b_q-1}(q-m)>0.
\]
If \(L_m(t)\le2m\), then every factor on the right is at most \(2m\); in particular \(q-m\le2m\) and \(b_q\le e_q\). Thus \(t\mid T_m\) and \(t\le T_m\le B_m\). Contrapositively,
\[
t>B_m,\quad\gcd(t,P_m)=1\quad\Longrightarrow\quad L_m(t)>2m.
\]
This finite prime-power obstruction is the key uniformity in the exponent and the prime base.

**2. Strict sign at sufficiently large prime powers.** Take a prime \(p>m+B_m\), put \(t=p-m>B_m\ge m\), and let \(a\ge1\). Then \(p>2m\) and \(\gcd(p,t)=1\). We have
\[
L_m(p^a)=p^{a-1}t,
\quad L_m^{(2)}(p^a)=
\begin{cases}L_m(t),&a=1,\\ p^{a-2}tL_m(t),&a\ge2.\end{cases}
\]
If some prime \(q\le m\) divides \(t\), then \(L_m(t)=0\). The second iterate vanishes, so \(D_m(p^a)=p^{a-1}t<p^a\).

Otherwise \(\gcd(t,P_m)=1\); step 1 yields \(L_m(t)>2m\). For \(a=1\), the first two positive iterates sum to more than \(t+2m=p+m>p\). For \(a\ge2\), using \(t>m\) and \(p=t+m\),
\[
tL_m(t)>2mt>mp.
\]
Therefore the first two positive iterates have sum
\[
p^{a-2}t\bigl(p+L_m(t)\bigr)
>p^{a-2}(pt+mp)=p^a.
\]
Subsequent terms are nonnegative, proving abundance for every exponent. Both inequalities are strict, so perfection is excluded.

**3. Density calculation.** Fix the integer \(m\) and reduce prime bases \(p\) modulo the squarefree modulus \(P_m\). Apart from finitely many primes dividing \(P_m\), the residue \(p\) is a unit. For a prime \(q\mid m\), every unit \(p\) makes \(p-m\not\equiv0\pmod q\). For a prime \(q\le m\) not dividing \(m\), exactly one of the \(q-1\) nonzero classes (namely \(p\equiv m\pmod q\)) makes \(q\mid p-m\). By the Chinese remainder theorem, the admissible fraction of the \(\varphi(P_m)\) unit classes is precisely \(\delta_m\). The prime number theorem in fixed arithmetic progressions gives the claimed two asymptotics; omitting finitely many bases below the proven threshold does not change either leading constant.

**4. Complete special case \(m=4\).** For \(p>4\), the odd integer \(p-4\) is divisible by \(3\) exactly when \(p\equiv1\pmod3\); in that case the second iterate vanishes and every \(p^a\) is deficient. Now assume \(p\ge13\), \(p\equiv2\pmod3\), and set \(t=p-4\). Then \(t>4\), \(\gcd(t,6)=1\). If \(L_4(t)>8\), step 2's two-iterate inequalities (which require only \(t>4\)) prove abundance.

If instead \(L_4(t)\le8\), every prime divisor of \(t\) is among \(5,7,11\). The only possibilities, found by multiplying the permitted local factors \(q^{e-1}(q-4)\le8\), are
\[
t\in\{5,7,11,25,35,55\}.
\]
The condition \(p=t+4\) prime with \(p\ge13\) leaves only \((t,p)=(25,29)\) or \((55,59)\). Direct iteration gives \(D_4(29)=25+5+1=31>29\) and \(D_4(59)=55+7+3=65>59\); for every \(a\ge2\) the first two iterates exceed \(p^a\), since respectively \(25L_4(25)=125>4(29)\) and \(55L_4(55)=385>4(59)\). Finally, for \(p\in\{2,3\}\), \(L_4(p^a)=0\); for \(p=5\), \(D_4(5^a)=1+5+\cdots+5^{a-1}<5^a\); for \(p=7\), \(D_4(7^a)=3\cdot7^{a-1}<7^a\); and for \(p=11\), \(D_4(11)=10<11\), while for \(a\ge2\),
\[
D_4(11^a)=7\cdot11^{a-1}+21\cdot11^{a-2}<11^a.
\]
These cases exhaust all prime powers.

## Verification

The standalone `verify.py` implements the Schemmel function by integer trial division and computes iterated sums directly. Its replay returned `VERIFY_OK`: 987 local-bound/prime-power sign checks, 378 exhaustive \(m=4\) prime-power sign checks at primes up to \(701\), and independent residue-class factor counts for six even values of \(m\). Exact one-step examples include \(D_4(29)=31\), \(D_4(59)=65\), and \(D_4(11)=10\). These are finite checks; the infinite result follows from the proof above and the standard prime number theorem in arithmetic progressions.

## Relationship to prior work

OEIS A241668 recorded the specific \(D_4\) sequence and sample values on April 26, 2014, but contains no prime-power sign classification. Defant, *On Arithmetic Functions Related to Iterates of the Schemmel Totient Functions* (2015), introduced the iterated sums in published research and proved in Theorem 18 that each fixed even \(m\) has infinitely many abundant prime powers, uniformly in the exponent. That proof selects one admissible congruence class and obtains a stronger lower excess along those primes. This result **does not claim** the prior existence theorem, or its lower-excess statement, as new. Here the distinction is a full residue-class **converse** (all other sufficiently large prime bases yield deficient powers), an **exact prime-density product**, and a **complete cutoff-free classification for \(m=4\)**. These refinements use the elementary finite-obstruction lemma above rather than improving the general excess bound of Theorem 18. Defant's 2014 paper on sparsely Schemmel-totient numbers addresses the one-step function's record-low values, not the sign distribution of its iterate sums.

## Limitations

The explicit general threshold \(m+B_m\) is sufficient, not claimed optimal. The density is for prime bases and does not estimate the proportion of all integers that are abundant. A natural extension beyond prime powers is not provided. The deduction uses standard prime number theory; the same density or classification could exist in unlocated literature, especially as the abundant half refines Defant's original proof. The theorem is not an independent mathematical validation.

## References

1. C. Defant, *On Arithmetic Functions Related to Iterates of the Schemmel Totient Functions*, **Journal of Integer Sequences** 18 (2015), Article 15.2.1; published January 13, 2015. https://www.maths.tcd.ie/EMIS/journals/JIS/VOL18/Defant/defant5.pdf
2. C. Defant, *On Arithmetic Functions Related to Iterates of the Schemmel Totient Functions*, arXiv:1506.05426 (June 17, 2015). https://arxiv.org/abs/1506.05426
3. C. Defant, *On Sparsely Schemmel Totient Numbers*, arXiv:1412.3080 (December 9, 2014). https://arxiv.org/abs/1412.3080
4. C. Defant, OEIS A241668, *Sum of iterates of A241663 up to and including either 0 or 1*, contributed April 26, 2014. https://oeis.org/A241668/internal
