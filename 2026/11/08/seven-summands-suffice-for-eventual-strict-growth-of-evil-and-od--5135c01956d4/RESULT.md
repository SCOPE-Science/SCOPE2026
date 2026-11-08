# Seven summands suffice for eventual strict growth of evil and odious representation counts

## Finding

Let \(s_2(n)\) be the number of ones in the binary expansion of \(n\ge0\). Put
\[E=\{n\ge0:s_2(n)\equiv0\pmod 2\},\qquad O=\{n\ge0:s_2(n)\equiv1\pmod 2\}.\]
For \(A\in\{E,O\}\), and every integer \(k\ge1\), let \(R_{A,k}(n)\) count **ordered** tuples \((a_1,\ldots,a_k)\in A^k\) with \(a_1+\cdots+a_k=n\), and set \(R_{A,k}(-1)=0\). Write \(\alpha=\log_4 3\).

**Theorem.** For every fixed integer \(k\ge7\), define
\[\eta_k=\min\{1-\alpha,\ (k-2)(1-\alpha)-1\}>0.\]
For both \(A=E\) and \(A=O\), as \(n\to\infty\),
\[
R_{A,k}(n)-R_{A,k}(n-1)
=\frac1{2^k}\binom{n+k-2}{k-2}
+O_k(n^{k-2-\eta_k}).
\]
In particular, \(R_{E,k}\) and \(R_{O,k}\) are **eventually strictly increasing for every \(k\ge7\)**. Thus the previously unresolved cases \(k=7,8,9\) are affirmative. The theorem does not determine the eventual monotonicity for \(k=6\), nor an effective least threshold in any case.

## Assumptions and scope

The variables \(n\) and \(k\) are nonnegative and positive integers respectively, with \(k\) fixed in the asymptotic claim. Repeated summands and zero summands are allowed when they belong to \(A\). In particular, \(0\in E\) and \(0\notin O\). All implicit constants may depend on \(k\); the conclusion is not uniform as \(k\) varies with \(n\).

## Proof

**1. Fourier input.** Set \(\tau_j=(-1)^{s_2(j)}\) and \(T(z)=\sum_{j\ge0}\tau_j z^j\) for \(|z|<1\). The classical uniform Gelfond estimate, quoted in the motivating work, states that for some absolute \(C\), every \(M\ge1\) and real \(\theta\) satisfy
\[
\left|\sum_{j=0}^{M-1}\tau_j e^{ij\theta}\right|\le C M^\alpha,
\qquad \alpha=\frac{\log 3}{\log 4}.
\]
For \(N\ge2\), put \(\rho=e^{-1/N}\) and \(z=\rho e^{i\theta}\). Abel summation of the uniformly bounded partial exponential sums gives
\[\sup_{-\pi\le\theta\le\pi}|T(\rho e^{i\theta})|\ll N^\alpha.\tag{1}\]
Independently, Parseval and \(|\tau_j|=1\) give the **exact** identity
\[\frac1{2\pi}\int_{-\pi}^{\pi}|T(\rho e^{i\theta})|^2\,d\theta=\sum_{j\ge0}\rho^{2j}=\frac1{1-\rho^2}\ll N.\tag{2}\]
The geometric bound \(|1-\rho e^{i\theta}|\gg N^{-1}+|\theta|\) holds on \([-\pi,\pi]\). Consequently, for each fixed real \(p>1\),
\[\int_{-\pi}^{\pi}|1-\rho e^{i\theta}|^{-p}\,d\theta\ll_p N^{p-1}.\tag{3}\]

**2. Main term and errors.** The generating series of the two sets are
\[F_\pm(z)=\frac12\big((1-z)^{-1}\pm T(z)\big),\]
with plus corresponding to \(E\). The first difference \(\Delta_{\pm,k}(n)=R_{A,k}(n)-R_{A,k}(n-1)\) is the coefficient of \(z^n\) in \((1-z)F_\pm(z)^k\). Expanding exactly,
\[
2^k\Delta_{\pm,k}(n)=\binom{n+k-2}{k-2}
+\sum_{\ell=1}^k(\pm1)^\ell\binom{k}{\ell}
[z^n](1-z)^{1-k+\ell}T(z)^\ell.\tag{4}
\]
For each coefficient, integrate on \(|z|=\rho\); the factor \(\rho^{-n}=e\) is bounded. Hence it suffices to bound the angular integrals of the absolute values in (4).

For \(\ell=1\), equations (1) and (3), using \(p=k-2>1\), bound the coefficient by \(O_k(N^{k-3+\alpha})\).

For \(\ell=2\), put \(p=k-3\) and split the circle at \(|\theta|=N^{-\alpha}\). On the inner arc, use \(|1-z|^{-p}\ll N^p\), (1), and an arc length \(O(N^{-\alpha})\), giving \(O_k(N^{k-3+\alpha})\). On the outer arc use \(|1-z|^{-p}\ll N^{\alpha p}\) and (2), giving \(O_k(N^{1+\alpha(k-3)})\). Both have exponents less than \(k-2\).

For \(3\le\ell\le k-1\), put \(p=k-\ell-1\ge0\). The pointwise estimate \(|1-z|^{-p}\ll_k N^p\), combined with (1) for \(\ell-2\) factors of \(T\) and (2) for the remaining pair, yields
\[
O_k(N^{p+1+(\ell-2)\alpha})=O_k(N^{k-\ell+(\ell-2)\alpha}).\tag{5}
\]
For \(\ell=k\), the factor is \((1-z)\), whose modulus is at most \(2\), so (1)--(2) give \(O_k(N^{1+(k-2)\alpha})\).

**3. Positive power saving.** For all \(k\ge7\), \((k-2)(1-\alpha)>1\); indeed \(5(1-\log_4 3)>1\). Thus \(\eta_k>0\). Every exponent in the preceding bounds is at most \(k-2-\eta_k\): the \(\ell=1\) and inner \(\ell=2\) terms save \(1-\alpha\); the outer \(\ell=2\) term saves \((k-3)(1-\alpha)\); (5) saves \((\ell-2)(1-\alpha)\); and the \(\ell=k\) term saves \((k-2)(1-\alpha)-1\). Taking \(N=n\) for sufficiently large \(n\) proves the error estimate in the theorem. Since the binomial main term is positive and asymptotic to \(n^{k-2}/(k-2)!\), both first differences are eventually positive. \(\square\)

## Verification

The standalone `verification/verify.py` independently computes exact ordered representation counts from the parity-defined sets and checks the coefficient identity (4) using separately calculated powers of the signed Thue--Morse polynomial. It also enumerates the finite early failures of strict monotonicity for \(k=7,8,9,10\) within a stated finite window. These checks are finite corroborations, **not** a proof of the all-\(n\) or eventual assertion; the proof uses (1)--(5) and the cited classical exponential-sum bound. No explicit monotonicity threshold is certified by the asymptotic argument.

## Relationship to prior work

Allouche and Shallit, *Additive Properties of the Evil and Odious Numbers and Similar Sequences*, first publicly available 27 December 2021, prove eventual strict increase for ten summands in Corollary 11 using a stronger sufficient inequality \(k(1-\alpha)>2\). Their paper explicitly lists the cases \(6,7,8,9\) as unresolved, following Corollary 11. The present argument retains their signed generating series and classical Gelfond input but uses Parseval's second moment for the powers of \(T\), saving one exponent in the worst pure-Thue--Morse term. The new cases are \(k=7,8,9\); the result for \(k\ge10\) is also an independent derivation of known coverage.

Sándor and Yang (2026) obtain monotonic higher-fold representation functions for a **different** set specified by the leading base-four digit and a co-infinite density-one construction. Bell and Shallit (2022) and Shallit (2023) likewise construct other sets with monotone three-fold representation functions. None of those constructions identifies the evil/odious sets or implies their seven-fold monotonicity. The Fourier-input estimate is credited to Gelfond, as cited in Allouche--Shallit.

## Limitations

The result is asymptotic, with an ineffective-in-practice large threshold; it does not establish the conjectured sharp finite thresholds for six summands, resolve the six-summand case, or give uniform estimates for increasing \(k\). Priority beyond inspected literature and records cannot be guaranteed; the work has not undergone independent scientific review. A complete theorem-level literature priority check remains useful.

## References

1. J.-P. Allouche and J. Shallit, *Additive Properties of the Evil and Odious Numbers and Similar Sequences*, arXiv:2112.13627v3 (first submitted 2021-12-27), especially Section 4, Theorem 10, Corollary 11, and the subsequent open-status statement. https://arxiv.org/abs/2112.13627
2. A. O. Gel'fond, *Sur les nombres qui ont des propriétés additives et multiplicatives données*, Acta Arith. 13 (1967/68), 259--265; uniform exponential-sum estimate, cited as [8] in reference 1.
3. D. J. Newman and M. Slater, *Binary digit distribution over naturally defined sequences*, Trans. Amer. Math. Soc. 213 (1975), 71--78; cited as [12] in reference 1 for exponential-sum estimates.
4. C. Sándor and Q.-H. Yang, *On the Monotonicity of Higher-Fold Representation Functions*, arXiv:2606.28849v1 (2026-06-27). https://arxiv.org/abs/2606.28849
5. J. P. Bell and J. Shallit, *Counterexamples to a Conjecture of Dombi in Additive Number Theory*, arXiv:2212.12473 (2022-12-23). https://arxiv.org/abs/2212.12473
6. J. Shallit, *A Dombi Counterexample with Positive Lower Density*, arXiv:2302.02138 (2023-02-04). https://arxiv.org/abs/2302.02138
