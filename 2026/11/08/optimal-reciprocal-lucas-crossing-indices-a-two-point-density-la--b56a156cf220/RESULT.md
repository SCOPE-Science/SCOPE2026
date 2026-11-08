# Optimal reciprocal Lucas crossing indices: a two-point density law

## Finding
Fix integers \(p\ge q\ge2\). Define the increasing Lucas sequence by \(F_0=0\), \(F_1=1\), and \(F_n=pF_{n-1}+qF_{n-2}\) for \(n\ge2\). Let \(c=p+q-1\). For each positive **odd** integer \(k\), let \(J(k)\) be the smallest integer \(J\ge k+2\) satisfying the strict crossing
\[
\frac{p-1}{F_{k+1}}+c\sum_{i=k+2}^{J}\frac1{F_i}>\frac1{F_k}.
\]
Existence of \(J(k)\) follows from Theorem 1.3 of Komornik–Pedicini [1]. Define
\[
A=\frac{p+\sqrt{p^2+4q}}2,\quad
s=\frac{q}{A^3},\quad
C=\frac{1+ps-qs^2}{1+s},\quad
\lambda=3-\log_A q,\quad
b=\log_A\left(\frac{c}{(A-1)C}\right),
\]
\[
a=\log_A c-1,\qquad
\vartheta=b-a=\log_A\left(\frac{A}{(A-1)C}\right).
\]
Then \(0<\vartheta<1\), \(\lambda\) is irrational, and, as \(k\) ranges through positive odd integers, outside a set of natural density zero,
\[
\boxed{J(k)=\lfloor\lambda k+b\rfloor+1.}
\]
Writing \(K_1(k)=\lfloor\lambda k+a\rfloor\), the published lower cutoff [1], the **actual** strict crossing has the following exact frequencies among odd indices:
\[
\boxed{\operatorname{dens}_{k\ \mathrm{odd}}\{J(k)=K_1(k)+1\}=1-\vartheta,\quad
\operatorname{dens}_{k\ \mathrm{odd}}\{J(k)=K_1(k)+2\}=\vartheta.}
\]
In particular, the actual optimal upper endpoint lies only one or two steps above the published lower endpoint for density one of the odd indices, for every allowed \(p,q\). This is an asymptotic density-one assertion, **not** an unconditional all-index classification.

For the diagonal family \(p=q\ge2\), let \(K_2(k)\) denote the upper cutoff of [1]. That paper establishes that \(K_2-K_1\) is \(1\) or \(2\), with density \(w=2-2\log_A p\) of the value \(2\). Consequently the published upper cutoff overshoots the actual optimal strict-crossing index on a set of positive density
\[
\boxed{\operatorname{dens}_{k\ \mathrm{odd}}\{K_2(k)>J(k)\}=w-\vartheta
=\log_A\left(\frac{A(A-1)C}{p^2}\right)>0.}
\]
Likewise \(\vartheta\) is the exact density of indices at which one may increase the published lower cutoff by one while preserving the strict lower inequality. For \(p=q=2\), \(\vartheta\approx0.384467393811\) and \(w\approx0.6206747332\), so the upper-cutoff overshoot density is approximately \(0.2362073394\).

## Assumptions and scope
The parameters \(p,q\) are **fixed integers** satisfying \(p\ge q\ge2\). The variable \(k\) runs over **positive odd integers**. All logarithms are of positive real numbers, and \(\log_A\) uses base \(A>1\). A strict inequality defines \(J(k)\); equality at a finite partial sum is not a crossing. Density among odd integers is \(\lim_{N\to\infty}2N^{-1}\#\{1\le k\le N:k\text{ odd and satisfies the condition}\}\) where the limit exists. The assertion does not cover \(q=1\), even \(k\), nor uniform rates as \(p,q\to\infty\).

## Proof
**1. Positive infinite overshoot and its first nonzero Binet term.** Put \(B=-q/A\) and \(\rho=q/A^2\in(0,1)\). Binet's formula, established in [1], gives
\[
\frac1{F_i}=(A-B)\sum_{j\ge0}z_j^i,
\qquad z_j=\frac{B^j}{A^{j+1}},
\]
for every \(i\ge1\). Absolute convergence permits termwise summation. Let
\[
E_k=\frac{p-1}{F_{k+1}}+c\sum_{i=k+2}^{\infty}\frac1{F_i}-\frac1{F_k}.
\]
Then
\[
E_k=(A-B)\sum_{j\ge0}z_j^k H(z_j),\qquad
H(z)=(p-1)z+\frac{cz^2}{1-z}-1
=\frac{-1+pz+qz^2}{1-z}.
\]
Since \(A^2=pA+q\), \(H(z_0)=H(1/A)=0\). The next mode has \(z_1=-q/A^3=-s\) and \(H(z_1)=-C\). For odd \(k\), the product \(z_1^kH(z_1)=Cs^k>0\). Moreover \(|z_j/z_1|=\rho^{j-1}\) for \(j\ge2\), and \(H\) is uniformly bounded on those modes. Thus their summed contribution is \(O_{p,q}(\rho^k s^k)\), and
\[
\boxed{E_k=(A-B)Cs^k(1+O_{p,q}(\rho^k))}
\qquad(k\to\infty,\ k\text{ odd}).
\]
Here and below the constants depend on the fixed parameters. The same expansion is valid regardless of possible finite-index cancellations; for all sufficiently large odd \(k\), it gives \(E_k>0\). For every odd \(k\), positivity and existence of the strict crossing follow independently from Theorem 1.3 of [1].

**2. Tail and the sharp real crossing threshold.** For any integer \(J\to\infty\), the remaining tail is
\[
T_J=c\sum_{i=J+1}^{\infty}\frac1{F_i}
=\frac{c(A-B)}{A-1}A^{-J}
\bigl(1+O_{p,q}(\rho^{J})\bigr).
\]
The coefficient on the right is obtained from the \(j=0\) geometric series; all other Binet modes have relative size at most \(O_{p,q}(\rho^J)\). Hence, for odd \(k\) and any \(J=\lambda k+O_{p,q}(1)\),
\[
\frac{E_k}{T_J}=A^{J-\lambda k-b}\bigl(1+O_{p,q}(\rho^k)\bigr).
\]
The partial-sum crossing occurs exactly when \(E_k-T_J>0\), equivalently \(E_k/T_J>1\). Because the left-hand partial sums increase strictly with \(J\), the first crossing is unique. Theorem 1.3 of [1] bounds \(J(k)\) between its cutoffs \(K_1(k)+1\) and \(K_2(k)\), both of the form \(\lambda k+O_{p,q}(1)\). The ratio estimate therefore applies at the candidate crossing integers. It follows that there are constants \(D>0\) and \(k_0\), depending on \(p,q\), such that for every odd \(k\ge k_0\) satisfying
\[
\operatorname{dist}(\lambda k+b,\mathbb Z)>D\rho^k,
\]
the signs at \(\lfloor\lambda k+b\rfloor\) and \(\lfloor\lambda k+b\rfloor+1\) are respectively negative and positive. Thus \(J(k)=\lfloor\lambda k+b\rfloor+1\) for all such indices. Only the exponentially narrow exceptional phases remain unsettled by this comparison.

**3. Irrationality and exceptional-set density.** If \(\log_A q=m/n\) were rational for positive integers \(m,n\), then \(A^m=q^n\). The number \(A\) is quadratic irrational: the discriminant \(p^2+4q\) lies strictly between \(p^2\) and \((p+2)^2\), because \(2\le q\le p\). The nontrivial field automorphism therefore sends \(A\) to \(B=-q/A\). Applying it gives \(B^m=q^n\), impossible because \(|B|=q/A<1<q^n\). Hence \(\lambda=3-\log_A q\) is irrational. The sequence \(\lambda(2m+1)+b\) is equidistributed modulo one. For every fixed \(\varepsilon>0\), all sufficiently large candidate exceptions lie within distance \(\varepsilon\) of an integer, a set of asymptotic frequency \(2\varepsilon\). Sending \(\varepsilon\downarrow0\) proves the exceptional set has density zero.

**4. Two cutoff frequencies.** From \(s=q/A^3\) and \(C=(1+ps-qs^2)/(1+s)\), we obtain
\[
C-1=\frac{s(p-1-qs)}{1+s}>0,
\qquad (A-1)(C-1)<(A-1)(p-1)\frac q{A^3}<1.
\]
The last strict inequality follows from \(A-1<A\), \(p-1<A\), and \(q<A\). Therefore \(1<(A-1)C<A\), which proves \(0<\vartheta<1\). For nonexceptional odd \(k\), setting \(u_k=\{\lambda k+a\}\) yields
\[
J(k)-K_1(k)=1+\lfloor u_k+\vartheta\rfloor.
\]
The phases \(u_k\) are equidistributed, and the second term is \(1\) precisely on an interval of length \(\vartheta\). Removing a zero-density exceptional set does not alter these limiting frequencies.

**5. Diagonal sharpness of the published upper bound.** For \(p=q\), Remark 1.7(iii) of [1] establishes density \(w=2-2\log_A p\) of \(K_2-K_1=2\) and the uniform dichotomy \(K_2-K_1\in\{1,2\}\). Since \(J\le K_2\) always, the \(\vartheta\)-density set with \(J=K_1+2\) is contained in the \(w\)-density set with \(K_2=K_1+2\), up to density-zero exceptions. Their difference is precisely the set where \(K_2>J\). Algebra gives \(w-\vartheta=\log_A(A(A-1)C/p^2)\). This is strictly positive because \(A(A-1)=(p-1)A+p>p^2\) when \(A>p\) and \(p\ge2\), while \(C>1\). This concludes the proof.

## Verification
The standalone `verify_lucas_reciprocal.py` uses `fractions.Fraction` to find the **exact** first strict crossing by direct recurrence for all parameter pairs \(2\le q\le p\le10\) and odd \(1\le k\le91\). Its high-precision decimal implementation separately computes the published lower and upper cutoffs and the proposed asymptotic phase. In 2,070 exact crossings it observed 2,069 matches of the phase formula and one explicit initial exception at \((p,q,k)=(2,2,1)\), where \(J=4\), but \(\lfloor\lambda+b\rfloor+1=3\); the intermediate partial sum equals the threshold exactly, so strictness matters. All 2,070 crossings satisfy \(K_1<J\le K_2\). Reported numerical values of \(\vartheta\) are illustrations only; the analytic proof is independent of floating-point accuracy and finite enumeration.

Reproduce using Python 3.11 or newer:

```
python verify_lucas_reciprocal.py
```

## Relationship to prior work
Komornik and Pedicini [1, Theorem 1.3] establish the two explicit bounds \(K_1,K_2\) for the **same reciprocal Lucas sum**. Their Remark 1.7(ii) supplies a table showing both bounds can be nonoptimal, and Remark 1.7(iii) computes the density of **bound-window width two**, \(K_2-K_1=2\), in the diagonal \(p=q\) family. That density is **not** a density of the true optimal index \(J\). The present result evaluates the latter for all \(p\ge q\ge2\), identifies its Binet-corrected phase constant, and subtracts it from the previously known width density to quantify actual upper-bound nonoptimality. It uses the elementary Binet identity and equidistribution rather than asserting a new expansion-existence theorem. The authors' earlier work [2,3] studies expansions in non-integer bases and does not, in the inspected public descriptions, provide this arithmetic frequency calculation. The earlier Fibonacci series estimate [4] concerns a distinct \(q=1\) regime.

## Limitations
The theorem gives an almost-everywhere-in-index formula and **limiting natural densities**; it does not prove the phase formula for every sufficiently large odd \(k\), does not classify the exceptional set, and gives no explicit effective rate of convergence of the densities. The finite test finds one small exceptional case, which does **not** establish that it is the only one. The proof depends on the published two-sided cutoff theorem of [1] for finite-index existence and sandwiching; the main asymptotic could also be used for sufficiently large indices. The motivating source is a recent preprint, so priority relative to contemporaneous or unindexed literature has not been independently certified. The auxiliary earlier articles [2–4] were assessed through public abstracts or bibliographic descriptions where unrestricted full text was unavailable, not claimed to have been exhaustively inspected.

## References
[1] V. Komornik and M. Pedicini, *Estimates of Lucas series and expansions in non-integer bases*, arXiv:2610.41658v1, first posted 30 October 2026; full text: https://arxiv.org/html/2610.41658v1 . Primary MSC 11B39.

[2] V. Komornik, P. Loreti, and M. Pedicini, *A quasi-ergodic approach to non-integer base expansions*, Journal of Number Theory **254** (2024), 146–168, DOI:10.1016/j.jnt.2023.07.009; public bibliographic abstract: https://iris.uniroma3.it/handle/11590/452807 .

[3] V. Komornik, P. Loreti, and M. Pedicini, *Multiple Kakeya expansions*, listed on M. Pedicini's publication page: https://www.mat.uniroma3.it/users/pedicini/ .

[4] M. Pedicini and V. Komornik, *Estimates of Fibonacci series*, listed as accepted in 2026 by M. Pedicini: https://www.mat.uniroma3.it/users/pedicini/ .
