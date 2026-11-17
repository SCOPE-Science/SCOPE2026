# A sharp toxin-to-conversion window for positive two-cycles in a Holling-II plankton map

## Finding
Consider the discrete phytoplankton–zooplankton map
\[
F(u,v)=\left(u(2-u)-\frac{uv}{1+cu},\quad v\left(1-r+\frac{\beta u}{1+cu}-\theta u\right)\right).
\]
For every fixed saturation parameter \(c>0\) and fixed toxin-to-conversion ratio \(q=\theta/\beta>0\), there exist positive parameters \(\beta,r\), with \(\theta=q\beta\), and a **strictly positive prime-two orbit** of \(F\) if and only if
\[
\boxed{\frac{1}{(1+c)^2}<q<1.}
\]
Here a strictly positive prime-two orbit consists of distinct points \((a,v_1),(b,v_2)\in(0,\infty)^2\) satisfying \(F(a,v_1)=(b,v_2)\) and \(F(b,v_2)=(a,v_1)\). The quantifier is existential over \(\beta,r\): this does **not** assert a two-cycle at every parameter choice inside the window.

In particular, no strictly positive prime-two orbit exists for **any** positive \(r,\beta,\theta\) when \(\theta/\beta\le(1+c)^{-2}\) or \(\theta/\beta\ge1\). Both exclusions include their endpoints. The interval is sharp: every ratio strictly inside it is realized by some positive parameters.

An exact example is
\[
\begin{aligned}
c&=1,& \beta&=\frac{55759}{306},&\theta&=\frac{55759}{612},&r&=\frac{28907}{2040},\\
(a,v_1)&=\left(\frac12,\frac9{20}\right),&
(b,v_2)&=\left(\frac35,\frac{68}{75}\right).
\end{aligned}
\]
The two points map to each other exactly and have toxin-to-conversion ratio \(q=1/2\).

## Assumptions and scope
The parameters \(c,r,\beta,\theta\) are strictly positive real numbers. The map need not preserve the entire positive quadrant for arbitrary such parameters; positivity is required **at both points of the periodic orbit**, not at all initial conditions. No stability, physical attractivity, or global-invariance assertion is included. The case \(c=0\) is outside the existence construction, though the same ordering argument excludes prime-two positive cycles at \(c=0\) for every \(r,\beta,\theta>0\).

## Proof
**1. Any positive prime-two orbit forces a strict prey ordering and predator reversal.** Let \((a,v_1)\) and \((b,v_2)\) be a prime-two orbit. If \(a=b\), the first coordinate equation uniquely determines \(v_1=v_2\), contradicting primeness. Exchange the points if needed to obtain \(0<a<b\). The first coordinate equation gives
\[
b=a\left(2-a-\frac{v_1}{1+ca}\right)<a(2-a).
\]
Because \(b>a\) and \(v_1>0\), one has \(0<a<1\), hence \(0<a<b<1\). Solving the two prey equations for the predator levels gives
\[
v_1=(1+ca)\left(2-a-\frac ba\right),\qquad
v_2=(1+cb)\left(2-b-\frac ab\right).
\]
Direct expansion yields the exact identity
\[
\boxed{v_2-v_1=\frac{b-a}{ab}\bigl(a+b-ab+abc(3-a-b)\bigr)>0.}
\]
Every term in the bracket is positive for \(0<a<b<1\) and \(c>0\). Write \(k=v_2/v_1>1\).

**2. Necessity of both parameter bounds.** Define the predator multiplier
\[
R(u)=1-r+\beta u\left(\frac{1}{1+cu}-q\right).
\]
The predator equations on a two-cycle give \(R(a)=k>1\) and \(R(b)=k^{-1}<1\). Subtracting,
\[
k-k^{-1}=\beta(b-a)\left(q-\frac{1}{(1+ca)(1+cb)}\right)>0.
\]
Therefore \(q>[(1+ca)(1+cb)]^{-1}>(1+c)^{-2}\). On the other hand \(R(a)>1\), together with \(r>0\), gives \(q<(1+ca)^{-1}<1\). This proves both strict necessary inequalities, including nonexistence at the endpoints.

**3. Constructive sufficiency at every interior ratio.** Fix \(c>0\) and \((1+c)^{-2}<q<1\). Choose \(a\in(0,1)\) with
\[
\frac{1}{(1+ca)^2}<q<\frac{1}{1+ca}.
\]
Such \(a\) exists: it suffices to choose \(z=1+ca\) strictly between \(q^{-1/2}\) and \(\min\{1+c,q^{-1}\}\). Take any \(b>a\) sufficiently close to \(a\), ensuring \(b<a(2-a)\) and \(q>[(1+ca)(1+cb)]^{-1}\). Define \(v_1,v_2\) by the preceding prey formulas; both are positive, and \(k=v_2/v_1>1\). Set
\[
\boxed{\begin{aligned}
\beta&=\frac{k-k^{-1}}{(b-a)\left(q-[(1+ca)(1+cb)]^{-1}\right)},\\
\theta&=q\beta,\\
r&=1-k+a\beta\left(\frac{1}{1+ca}-q\right).
\end{aligned}}
\]
Then \(\beta,\theta>0\). The positivity of \(r\) follows for all sufficiently close \(b>a\). Indeed, putting \(T_0=2a-a^2+a^2c(3-2a)>0\), the first-step predator comparison gives
\[
\lim_{b\downarrow a}\beta
=\frac{2T_0}{a^2(1+ca)(1-a)\left(q-(1+ca)^{-2}\right)}>0,
\]
while \(k\to1\), so
\[
\lim_{b\downarrow a}r
=a\left(\lim_{b\downarrow a}\beta\right)\left(\frac1{1+ca}-q\right)>0.
\]
Finally, the construction gives \(R(a)=k\) by definition of \(r\); the subtracted-multiplier identity gives \(R(b)=k^{-1}\). Thus both predator equations and both prey equations hold exactly, producing the required prime-two orbit. This proves sufficiency.

**4. Exact rational witness.** Substitution of the rational parameters stated above gives
\[
F\left(\frac12,\frac9{20}\right)=\left(\frac35,\frac{68}{75}\right),\qquad
F\left(\frac35,\frac{68}{75}\right)=\left(\frac12,\frac9{20}\right).
\]
All coordinates and parameters are strictly positive.

## Verification
Run `python3 verify_prime_two.py` with Python 3 (standard library only). The included script evaluates the rational witness exactly and constructs/checks 36 further exact-rational two-cycles, using four values of \(c\), three positive prey levels, and three toxin ratios inside the local admissible subinterval. The reported output is `TOXIC_PLANKTON_TWO_CYCLE_EXACT_OK generic_samples=36 rational_witness=1`. Separately, computer algebra confirmed the prey-difference identity, both predator-multiplier identities, and the finite construction limit. The universally quantified theorem follows from the four analytic proof steps, not from these finite computations.

## Relationship to prior work
Shoyimardonov's 2022 preprint introduces exactly this discrete map, classifies positive equilibria and analyzes local Neimark–Sacker bifurcations; its corresponding 2023 journal paper gives MSC 34C23. Neither the inspected preprint sections nor the journal abstract give this full positive prime-two feasibility window. A published published-finding corpus finding for a **different** linear-response plankton map, \((u,v)\mapsto(u(2-u-v),v(1-r+\gamma u))\), excludes positive prime-two cycles there; that exclusion does not imply the present sharp toxin/saturation feasibility criterion. Khan and Javaid (2021) study periodic points of a different Holling-III model, while Khan et al. (2021) use a nonstandard, positivity-preserving discretization. The 2022 Khan–Alayachi article has a potentially relevant title and mentions periodic points; its full text was not accessible for a decisive equation-by-equation comparison and is a residual originality risk.

## Limitations
The theorem concerns **existence somewhere in each \((c,q)\)-parameter fiber**, not the number, stability or basin size of two-cycles at fixed \(\beta,r\). It does not prove biological observability, global boundedness or positivity of all iterates from arbitrary positive initial states. Related unindexed literature, particularly inaccessible work explicitly mentioning periodic points, could contain an equivalent conclusion. A search failing to locate it is not proof of publication priority. No independent mathematical audit has been performed.

## References
1. S. Shoyimardonov, *Neimark–Sacker bifurcation and stability analysis in a discrete phytoplankton–zooplankton system with Holling type II functional response*, arXiv:2207.01961, first submitted 2022-07-05. https://arxiv.org/abs/2207.01961
2. S. Shoyimardonov, corresponding journal article, *Journal of Applied Analysis & Computation* 13 (2023), 2048–2064. https://doi.org/10.11948/20220345
3. A. Q. Khan and M. B. Javaid, *Discrete-time phytoplankton–zooplankton model with bifurcations and chaos*, *Advances in Difference Equations* (2021), article 415. https://doi.org/10.1186/s13662-021-03523-5
4. M. S. Khan, M. Samreen, H. Aydi and M. De la Sen, *Qualitative analysis of a discrete-time phytoplankton–zooplankton model with Holling type-II response and toxicity*, *Advances in Difference Equations* (2021), article 443. https://doi.org/10.1186/s13662-021-03599-z
5. A. Q. Khan and H. S. Alayachi, *Bifurcation and chaos in a phytoplankton–zooplankton model with Holling type-II response and toxicity*, *International Journal of Bifurcation and Chaos* 32 (2022), 2250176. https://doi.org/10.1142/S0218127422501760 (full-text comparison incomplete).
