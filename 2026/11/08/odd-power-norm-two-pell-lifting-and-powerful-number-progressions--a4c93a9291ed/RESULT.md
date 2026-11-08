# Odd-power norm-two Pell lifting and powerful-number progressions

## Finding
For every positive integer \(m\) and integer \(r\ge1\), the equation
\[
X^2-m^{2r+1}Z^2=2,\qquad X,Z\in\mathbb Z_{>0},
\]
has a solution if and only if \(m\) is odd and \(x^2-my^2=2\) has a solution in positive integers. For any odd \(m\) with such a base solution \((x,y)\), define, for every positive odd integer \(n\),
\[
X_n+Y_n\sqrt m=(x+y\sqrt m)\bigl((x^2-1)+xy\sqrt m\bigr)^{(n-1)/2}.
\]
These are positive integer solutions of \(X_n^2-mY_n^2=2\), with the **exact valuation law**
\[
\nu_p(Y_n)=\nu_p(y)+\nu_p(n)\quad\text{for every prime }p\mid m.
\]
In particular \(m^r\mid Y_{m^r}\), and \((X_{m^r},Y_{m^r}/m^r)\) solves the displayed odd-power equation. Fixing \(m\) and \(r\), infinitely many distinct such solutions arise by taking \(n=m^r(2j+1)\) for \(j\ge0\).

Among squarefree positive \(m\), the two smallest qualifying multipliers are \(7\) and \(23\). At the cubic level \(r=1\), they give respectively
\[
(X,Z)=(11427,617),\qquad
(X,Z)=(15191131279719638885,137720427724123513).
\]
For either example, and for all solutions with \(X\ge3\), the triple
\[
(X-2)^2,\quad (X-1)^2,\quad m^{2r+1}Z^2=X^2-2
\]
is an arithmetic progression of powerful integers with common difference \(2X-3\). This does not assert that its three entries are consecutive among all powerful integers.

## Assumptions and scope
A positive integer is **powerful** when each prime dividing it occurs to exponent at least two. All Pell variables are positive integers; \(m\ge1\), \(r\ge1\), and \(n\ge1\) is odd. The first equivalence includes nonsquarefree multipliers. For even \(m\) the higher odd-power equation is unsolvable, although the base equation can be solvable (for example \(m=2\)). The valuation law refers only to primes dividing \(m\), and no claim of primitivity or of consecutive powerful integers is made.

## Proof
**1. The parity boundary.** If \(m\) is even and \(r\ge1\), then \(m^{2r+1}\equiv0\pmod8\); a solution would imply \(X^2\equiv2\pmod8\), impossible. Conversely any solution at coefficient \(m^{2r+1}\) gives the base solution \((x,y)=(X,m^rZ)\). Thus it remains to lift a base solution when \(m\) is odd.

**2. An integral norm-one lift.** For odd \(m\), the equation \(x^2-my^2=2\) forces \(x,y\) both odd: opposite parity makes the difference odd, and both even make it divisible by four. Reduction modulo eight gives \(m\equiv7\pmod8\). In the quadratic ring \(\mathbb Z[\sqrt m]\), put
\[
\eta=x+y\sqrt m,\qquad
\varepsilon=(x^2-1)+xy\sqrt m=\eta^2/2.
\]
The coefficients of \(\varepsilon\) are integers and \(N(\varepsilon)=1\). Therefore \(\eta\varepsilon^{(n-1)/2}=X_n+Y_n\sqrt m\) has positive integer coefficients and norm two for every positive odd \(n\). In particular \(X_n^2-mY_n^2=2\).

**3. Exact prime-power lifting.** Let \(p\mid m\). Reduction of the norm-two equation gives \(x^2\equiv2\pmod p\). Thus \(p\nmid x\), and \(p\) is neither \(2\), \(3\), nor \(5\); in particular \(p\ge7\). From \(\eta^n/2^{(n-1)/2}\), the second coefficient is
\[
Y_n=2^{-(n-1)/2}\sum_{j=0}^{(n-1)/2}
\binom n{2j+1}x^{n-2j-1}y^{2j+1}m^j.
\]
The \(j=0\) summand has \(p\)-valuation exactly \(\nu_p(n)+\nu_p(y)\). For \(j\ge1\), the identity
\[
(2j+1)\binom n{2j+1}=n\binom{n-1}{2j}
\]
shows \(\nu_p(\binom n{2j+1})\ge\nu_p(n)-\nu_p(2j+1)\). Since \(p\ge7\), \(\nu_p(2j+1)<j\) for every \(j\ge1\) (indeed \(2j+1<7^j\)). Together with \(\nu_p(m)\ge1\), every remaining summand has \(p\)-valuation strictly greater than \(\nu_p(n)+\nu_p(y)\). The denominator is a \(p\)-unit, so the lowest-valuation summand cannot cancel. This proves
\[
\nu_p(Y_n)=\nu_p(y)+\nu_p(n).
\]

**4. All odd-power coefficients and infinite families.** Choose \(n=m^r\), which is odd. For every \(p\mid m\), the valuation law yields \(\nu_p(Y_n)\ge r\nu_p(m)\), hence \(m^r\mid Y_n\). Writing \(Z=Y_n/m^r\) gives \(X_n^2-m^{2r+1}Z^2=2\). Replacing \(n\) by any odd multiple \(m^r(2j+1)\) retains the divisibility. Since \(\varepsilon>1\), these solutions are distinct as \(j\) varies.

**5. Least squarefree multipliers and progressions.** As shown in step 2, any odd qualifying \(m\) is \(7\pmod8\). Below \(23\), only \(7\) and \(15\) qualify modulo eight, and \(15\) is excluded by \(x^2\equiv2\pmod3\). Directly, \(3^2-7\cdot1^2=2\) and \(5^2-23\cdot1^2=2\), giving the first two qualifying values. Exact powering as in step 4 yields the two numerical pairs in the statement. Finally the first and second terms in the progression are squares, while \(m^{2r+1}Z^2\) is powerful because \(2r+1\ge3\). The successive differences both equal \(2X-3\).

## Verification
Run `python3 verify.py` using Python's standard library. It checks the integral norm-one multiplier and direct binomial expansion independently, verifies the exact valuations in three base examples for ten odd indices, and tests nine higher odd-power coefficient cases, including the displayed cubic examples. The code prints `VERIFY_OK exact_cases=39` together with the two explicit cubic-level witnesses. All checks use exact integers. The proof above, not these finite checks, establishes the result for all multipliers and all exponents.

## Relationship to prior work
Van Doorn (2026, Section 3) constructs his three-term powerful-number progressions from \(X^2-7^3Z^2=2\), starting with \(x^2-7y^2=2\). After Conjecture 5 he observes that deciding which squarefree \(m\) support \(X^2-m^3Z^2=2\) is not immediate and cites Mollin's fundamental-unit criterion for the coefficient \(m^3\). The new statement replaces the cubic coefficient by the base coefficient for **every** positive odd-power level, with an exact indexwise divisibility law and the next multiplier \(23\). Mollin (2005, Theorem 2) gives a criterion for the norm-two equation at a **fixed coefficient**; it does not in the inspected theorem compare all odd powers of the coefficient. Chan (2023) constructs other progressions of powerful numbers using generalized Pell equations, without asserting the present equivalence. The use of standard Pell multiplication and binomial valuation estimates is not claimed as a new technique.

## Limitations
This result establishes the solvability equivalence and concrete powerful arithmetic progressions, not that any constructed triple consists of consecutive elements of the sequence of powerful numbers. It gives no asymptotic density or full classification of admissible odd multipliers. The exact valuation statement is for \(p\mid m\) and positive **odd** indices. The priority comparison is limited to the primary literature and accessible research records examined; an equivalent older Pell-sequence lifting formulation could exist.

## References
- Wouter van Doorn, *Three-term arithmetic progressions of consecutive powerful numbers*, arXiv:2605.06697v1, first public May 4, 2026, Section 3 and discussion after Conjecture 5. https://arxiv.org/abs/2605.06697
- Richard A. Mollin, *Generalized Lagrange criteria for certain quadratic Diophantine equations*, New York Journal of Mathematics 11 (2005), 539–545, Theorem 2. https://nyjm.albany.edu/j/2005/11-25.pdf
- Tsz Ho Chan, *Arithmetic Progressions Among Powerful Numbers*, Journal of Integer Sequences 26 (2023), Article 23.1.1. https://cs.uwaterloo.ca/journals/JIS/VOL26/Chan/chan33.pdf
