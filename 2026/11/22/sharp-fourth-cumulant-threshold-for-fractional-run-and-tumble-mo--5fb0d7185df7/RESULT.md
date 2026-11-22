# Sharp fourth-cumulant threshold for fractional run-and-tumble motion

## Finding

A symmetric stationary telegraph drive has an exact, *different* threshold for the unstandardized fourth cumulant of its fractionally integrated displacement than the previously known variance localization threshold. With the definitions below and with \(t\to\infty\), writing \(\kappa_{4,n}(t)=\operatorname{cum}_4(X_n(t))\), one has

\[
\kappa_{4,n}(t)\longrightarrow -B_n\in(-\infty,0),\qquad 0<n<\tfrac34,
\]
\[
\kappa_{4,3/4}(t)=-\frac{3v_0^4}{\gamma^3\Gamma(3/4)^4}\log(\gamma t)+O(1),
\]
\[
\kappa_{4,n}(t)\sim-\frac{3v_0^4}{\gamma^3\Gamma(n)^4(4n-3)}t^{4n-3},\qquad n>\tfrac34.
\]
Here \(B_n>0\) is the explicit convergent integral given in the proof. Thus \(n=3/4\) is the sharp boundary between bounded fourth cumulant and unbounded negative fourth cumulant. The fact that fourth cumulants of positive telegraph filters are negative is not claimed as new.

In the delocalized variance regime, the corresponding standardized excess kurtosis \(Q_n(t)=\kappa_{4,n}(t)/\operatorname{Var}(X_n(t))^2\) decays in distinct phases:

\[
Q_n(t)\sim\begin{cases}
-\displaystyle B_n\left(\frac{\gamma\Gamma(n)^2(2n-1)}{v_0^2}\right)^2t^{-(4n-2)},&\tfrac12<n<\tfrac34,\\[3pt]
-\displaystyle\frac{3\log(\gamma t)}{4\gamma t},&n=\tfrac34,\\[3pt]
-\displaystyle\frac{3(2n-1)^2}{(4n-3)\gamma t},&n>\tfrac34.
\end{cases}
\]
At \(n=1/2\), \(Q_{1/2}(t)\sim -B_{1/2}(\pi\gamma/v_0^2)^2/[\log(\gamma t)]^2\); for \(0<n<1/2\), it tends to a strictly negative finite constant.

## Assumptions and scope

Fix real \(v_0>0\), \(\gamma>0\), and \(n>0\). Let \(\sigma(s)\in\{-1,+1\}\) be a stationary symmetric continuous-time Markov chain, initialized with equally likely signs and switching signs at rate \(\gamma\). Define the zero-initial-data fractional telegraph displacement

\[
X_n(t)=\frac{v_0}{\Gamma(n)}\int_0^t(t-s)^{n-1}\sigma(s)\,ds,\qquad t\ge0.
\]
The integral exists pathwise for every \(n>0\); no stochastic integration convention is needed. By stationary time reversibility of the two-state chain, \(X_n(t)\) has the same one-time law as \(Y_n(t)=v_0\Gamma(n)^{-1}\int_0^t u^{n-1}\sigma(u)\,du\). All cumulants in this result refer to this one-time law, not a stationary-increment or trajectory cumulant. Define \(B_n\) only for \(0<n<3/4\) as the strictly positive convergent integral below.

## Proof

**1. Connected telegraph four-point function.** Write \(\lambda=2\gamma\). For \(0\le u_1<u_2<u_3<u_4\), the Markov property and \(\mathbb E[\sigma(u)\sigma(v)]=e^{-\lambda|u-v|}\) give

\[
\mathbb E[\sigma(u_1)\sigma(u_2)\sigma(u_3)\sigma(u_4)]=
 e^{-\lambda[(u_2-u_1)+(u_4-u_3)]}.
\]
Subtracting the three Gaussian pairings cancels the adjacent pairing, while the remaining two agree. Consequently the joint fourth cumulant is exactly

\[
\operatorname{cum}(\sigma(u_1),\sigma(u_2),\sigma(u_3),\sigma(u_4))
=-2e^{-\lambda[(u_3-u_1)+(u_4-u_2)]}.
\]
Multilinearity, boundedness of \(\sigma\), and Fubini on the finite four-dimensional integration domain imply the *exact all-time formula*

\[
\boxed{\kappa_{4,n}(t)=-\frac{48v_0^4}{\Gamma(n)^4}
\int_{0<u_1<u_2<u_3<u_4<t}
\prod_{j=1}^4u_j^{n-1}
 e^{-2\gamma[(u_3-u_1)+(u_4-u_2)]}\,d\boldsymbol{u}.}
\]
This proves strict negativity and that \(-\kappa_{4,n}(t)\) is strictly increasing for every \(t>0\). These sign consequences are not the originality claim.

**2. Sharp diagonal integral.** Substitute \(s=u_1\), \(x=u_2-u_1\), \(y=u_3-u_2\), \(z=u_4-u_3\). The domain is \(s,x,y,z>0\), \(s+x+y+z<t\), and the integrand is

\[
s^{n-1}(s+x)^{n-1}(s+x+y)^{n-1}(s+x+y+z)^{n-1}
 e^{-2\gamma(x+2y+z)}.
\]
Define \(H_n(s)\) to be its integral over all \(x,y,z>0\), with no final-time constraint. For \(s\ge1\), factoring out \(s^{4n-4}\) and applying dominated convergence in the exponentially weighted gap variables gives

\[
H_n(s)=\frac{s^{4n-4}}{16\gamma^3}\bigl(1+O(s^{-1})\bigr).
\]
Indeed each factor \((1+q/s)^{n-1}\) is bounded by a fixed polynomial in the nonnegative gaps when \(n\ge1\), and by one when \(0<n<1\); the mean-value theorem plus finite exponentially weighted gap moments supplies the stated \(O(s^{-1})\) error. For \(0<s<1\), the four original powers are locally integrable since \(n>0\); the exponential gap factors control the unbounded gap tails. Thus \(\int_0^1H_n(s)ds<\infty\).

The omitted contribution from \(s+x+y+z\ge t\) in \(\int_0^tH_n(s)ds\) is \(O(t^{4n-4})\) if \(n\ge1\) and \(O(t^{4n-4}+e^{-c t})\) if \(0<n<1\) after splitting \(s\in[t/2,t]\) and \(s\in[0,t/2]\), for some \(c>0\), with exponentially decaying tails in the latter range. In particular it is \(o(t^{4n-3})\) when \(n>3/4\), \(O(1)\) when \(n=3/4\), and tends to zero when \(0<n<3/4\). (For the last case, domination by the globally integrable positive kernel also gives the limit directly.)

**3. The three regimes.** If \(0<n<3/4\), \(H_n(s)\sim s^{4n-4}/(16\gamma^3)\) has integrable tail; monotone convergence in the original four-point integral yields the finite positive constant

\[
B_n=\frac{48v_0^4}{\Gamma(n)^4}
\int_{0<u_1<u_2<u_3<u_4<\infty}
\left(\prod_{j=1}^4u_j^{n-1}\right)
 e^{-2\gamma[(u_3-u_1)+(u_4-u_2)]}\,d\boldsymbol{u}.
\]
If \(n=3/4\), the diagonal tail is \(s^{-1}/(16\gamma^3)+O(s^{-2})\), giving the stated logarithm with bounded remainder. If \(n>3/4\), integration of the leading \(s^{4n-4}\) term gives \(t^{4n-3}/[16\gamma^3(4n-3)]\); multiplying by the prefactor \(-48v_0^4/\Gamma(n)^4\) yields the stated coefficient. This establishes all three cumulant regimes without relying on numerical evidence.

**4. Kurtosis rates.** The exact variance is

\[
V_n(t)=\frac{v_0^2}{\Gamma(n)^2}\int_0^t\int_0^t
u^{n-1}w^{n-1}e^{-2\gamma|u-w|}\,du\,dw.
\]
For \(n>1/2\), diagonal concentration gives \(V_n(t)\sim v_0^2t^{2n-1}/[\gamma\Gamma(n)^2(2n-1)]\). At \(n=1/2\), the diagonal integral is logarithmic, \(V_{1/2}(t)\sim v_0^2\log(\gamma t)/(\pi\gamma)\). For \(0<n<1/2\), it has a strictly positive finite limit. Inserting these asymptotics in \(Q_n=\kappa_{4,n}/V_n^2\) gives all stated rates. In particular \(n=3/4\) introduces a genuine new fluctuation boundary, distinct from the variance boundary \(n=1/2\).

## Verification

The standalone standard-library checker `check.py` independently integrates moment equations for the reverse-time-weighted telegraph integral, compares the special \(n=1\) formulas against closed-form moments, and checks numerical signs and the predicted critical logarithmic slope across multiple fractional orders. It passes 156 deterministic assertions when run with `python3 check.py`. It is a finite numerical diagnostic only, not a substitute for the preceding infinite-time proof. No independent external audit is represented.

## Relationship to prior work

Dean, Majumdar and Schawe (2020 preprint, 2021 journal publication) introduce and analyze the same generalized telegraph-integral family, rigorously identify the variance localization threshold \(n=1/2\), and compute full generating functions at several special integer and half-integer orders. The present statement adds the distinct sharp \(n=3/4\) trichotomy for the *unstandardized fourth cumulant*, including prefactors and the corresponding excess-kurtosis regimes. Santra, Ajgaonkar and Basu (2023 preprint) examine the integer-order randomly accelerated case, but do not supply this all-positive-order threshold. General negativity of fourth cumulants for positive linear filters of symmetric telegraph noise is known in related literature; it is used here only as a preliminary structural fact. A published equivalent result outside the inspected and indexed material cannot be excluded.

## Limitations

The assertions require an unbiased stationary two-state telegraph drive with constant Poisson flipping rate and zero-initial-data fractional integration. They do not establish analogous thresholds for biased or non-Markovian switching, time-dependent rates, random fractional order, or multitime cumulants. The small-order limiting value \(B_n\) is provided as a convergent definite integral, not as a closed combination of elementary constants. Negative excess kurtosis alone does not establish Gaussian convergence, and numerical tests do not certify the infinite asymptotics. The proof does not claim priority against unindexed literature.

## References

1. D. S. Dean, S. N. Majumdar, and H. Schawe, *Position distribution in a generalised run and tumble process*, arXiv:2009.01487 (first posted 2020-09-03); *Physical Review E* **103**, 012130 (2021). https://arxiv.org/abs/2009.01487 .
2. I. Santra, D. Ajgaonkar, and U. Basu, *Dichotomous acceleration process in one dimension: Position fluctuations*, arXiv:2304.11378 (2023). https://arxiv.org/abs/2304.11378 .
