# A parity-dependent covariance threshold for opposite singleton runs in a binary Markov chain

## Finding
Let \(n\ge3\) and \(0<p<1\). Consider a stationary binary Markov chain \((X_i)_{i=1}^n\) with equilibrium probabilities \(1/2,1/2\) and a common flip probability \(p\) at each step. Count only fully enclosed singleton runs:
\[
U_n=\sum_{i=1}^{n-2}\mathbf1\{X_iX_{i+1}X_{i+2}=010\},\qquad
V_n=\sum_{i=1}^{n-2}\mathbf1\{X_iX_{i+1}X_{i+2}=101\}.
\]
Write \(K=n-3\) and
\[
H_K(p)=1-(1-2p)^K-2p^2+6Kp(1-p).
\]
The exact covariance is
\[
\boxed{\operatorname{Cov}(U_n,V_n)=\frac{p^2}{8}H_{n-3}(p).}
\]
Its complete sign classification is:

- \(n=3\): strictly negative, with covariance \(-p^4/4\).
- Even \(n\ge4\): strictly positive at every \(0<p<1\).
- Odd \(n\ge5\): a unique root \(p_n\in(1/2,1)\); covariance is positive for \(0<p<p_n\), zero at \(p=p_n\), and negative for \(p_n<p<1\).

The odd-length roots increase strictly, \(p_5=8/9\), and
\[
\boxed{(n-3)(1-p_n)\longrightarrow c=0.2648056367507537\ldots,}
\qquad 6c=1+e^{-2c}.
\]
For each fixed \(0<p<1\), the eventual covariance is positive:
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(U_n,V_n)}{n}=\frac34p^3(1-p).
\]
Thus an odd finite sample near deterministic alternation has an opposing-colour singleton-run anticorrelation absent at every even sample size, while every fixed interior flip rate eventually exhibits positive linear covariance.

## Assumptions and scope
All counts are on the **linear** sample; no cyclic wrap-around patterns and no truncated endpoint runs are counted. Conditional transitions satisfy \(\Pr(X_{i+1}\ne X_i\mid X_i)=p\) in both states. The initial bit is stationary and fair. All results hold for each integer \(n\ge3\) and each real \(p\in(0,1)\); no restrictions on a rational or algebraic transition probability are imposed. The finite sign thresholds apply to the cross-covariance, not to either marginal variance or to conditionally fixed-composition binary strings.

## Proof
Set \(N=n-2\), \(\rho=1-2p\), and let \(I_i\) and \(J_i\) indicate the words \(010\) and \(101\) beginning at \(i\). By stationarity, \(\mathbb EI_i=\mathbb EJ_i=p^2/2\). For any legal pair of starting positions with displacement \(h\):
\[
\operatorname{Cov}(I_i,J_{i+h})=
\begin{cases}
-p^4/4,&h=0,\\
p^3/2-p^4/4,&|h|=1,\\
-p^4\rho^{|h|-2}/4,&|h|\ge2.
\end{cases}
\]
The first case uses incompatible initial letters; the second uses \(0101\) or \(1010\), each of probability \(p^3/2\). For \(h\ge2\), the first word ends in zero; the Markov transition probability from zero to one after \(h-2\) steps is \((1-\rho^{h-2})/2\). The two disjoint word probabilities therefore give \(\Pr(I_i=J_{i+h}=1)=p^4(1-\rho^{h-2})/4\). The negative displacement follows from stationarity and reversibility.

There are \(N-|h|\) pairs at displacement \(h\). Summing these covariances, for \(N\ge2\), yields
\[
\operatorname{Cov}(U_n,V_n)
=-\frac{Np^4}{4}+(N-1)\left(p^3-\frac{p^4}{2}\right)
-\frac{p^4}{2}\sum_{j=0}^{N-3}(N-2-j)\rho^j.
\]
The sum is empty when \(N=2\). The elementary identity
\[
\sum_{j=0}^{N-3}(N-2-j)\rho^j
=\frac{(N-2)-(N-1)\rho+\rho^{N-1}}{(1-\rho)^2}
\]
(with an empty sum for \(N=2\)) and \(1-\rho=2p\) simplify the result to \(p^2H_{n-3}(p)/8\). For \(N=1\), incompatibility gives \(-p^4/4\), agreeing with \(H_0(p)=-2p^2\).

For all integers \(K\ge0\), direct subtraction gives the strict step-two identity
\[
H_{K+2}(p)-H_K(p)=4p(1-p)\bigl(3+(1-2p)^K\bigr)>0.
\]
As \(H_1(p)=8p(1-p)>0\), all odd \(K\ge1\) are positive, proving the even-size claim. For even \(K\ge2\), \(H_K(p)\ge H_2(p)=2p(8-9p)>0\) when \(0<p\le1/2\). For \(p\in[1/2,1]\), set \(q=1-p\in[0,1/2]\). Differentiating yields
\[
\frac{d}{dq}H_K(1-q)=2K(1-2q)^{K-1}+4+6K-(4+12K)q>0.
\]
The inequality holds because \(K\) is even and the last two terms together are at least \(2\). At \(q=0\), \(H_K(1)=-2\), whereas \(H_K(1/2)>0\). Thus exactly one crossing exists; it is positive-to-negative as \(p\) increases. The step-two identity evaluated at the earlier root proves \(p_{n+2}>p_n\) for odd \(n\ge5\). For \(K=2\), \(H_2=2p(8-9p)\), giving \(p_5=8/9\).

For any fixed \(0<p<1\), the positive linear term \(6Kp(1-p)\) dominates the bounded remainder in \(H_K\), hence \(p_n\uparrow1\). To locate the boundary, set \(p=1-z/K\) along even \(K\), where \(z>0\) is fixed. Since \((1-2p)^K=(1-2z/K)^K\to e^{-2z}\),
\[
H_K(1-z/K)\longrightarrow 6z-1-e^{-2z}.
\]
The right side is strictly increasing from \(-2\) and has one positive root \(c\). Bracketing the unique zeros with any \(z_-<c<z_+\) establishes \(K(1-p_{K+3})\to c\). Finally, divide the exact covariance by \(n\): the bounded terms vanish and \(K/n\to1\), yielding \(3p^3(1-p)/4\).

## Verification
The standalone standard-library checker `check.py` enumerates every binary sample of lengths \(3\) through \(12\) at five rational flip probabilities, comparing the exact weighted joint distribution with the formula and verifying both expected counts. It also brackets odd-size roots by rational bisection through size \(201\), checks their strict ordering, and numerically checks the asymptotic root constant. Finite checks support, but do not replace, the all-size inequalities and limiting argument above. Execute `python3 check.py`.

## Relationship to prior work
Rukhin's 2006/2007 work gives general pattern-correlation and asymptotic covariance-matrix machinery for Markov sequences, and Mytalas–Zazanis (2013) derive central limit covariance formulas for Markov-dependent run counts. Those frameworks cover the general model and can support derivation of covariance formulas. The present claim is **not** novelty of Markov pattern-covariance computation itself. Its distinctive assertion is the complete *finite-sample parity-dependent sign classification* for opposite-colour exact singleton runs, including the unique and strictly increasing odd-size thresholds and their \(1/n\) critical boundary constant. The compared works did not state this specific classification in the material inspected. Related fixed-composition and independent-Bernoulli run results address different probability laws and do not by themselves imply it.

## Limitations
The sign theorem assumes stationarity, symmetric flip probabilities, and linear (noncyclic) observations. It does not extend without a new argument to unequal transition probabilities, nonstationary starts, larger run lengths, or cyclic closing patterns. A general prior pattern-covariance theorem may allow the exact covariance to be recovered as a specialization. The originality assessment concerns the sign classification and asymptotic threshold rather than the underlying covariance framework; uninspected literature may contain an equivalent specialization.

## References
1. A. L. Rukhin, *Pattern correlation matrices for Markov sequences and tests of randomness*, Teor. Veroyatnost. i Primenen. 51(4), 2006; English version, Theory Probab. Appl. 51(4), 2007, 663–679. https://doi.org/10.1137/S0040585X97982670
2. G. C. Mytalas and M. A. Zazanis, *Central limit theorem approximations for the number of runs in Markov-dependent binary sequences*, Journal of Statistical Planning and Inference 143(2), 2013, 321–333. https://doi.org/10.1016/j.jspi.2012.07.014
3. B. C. Johnson and J. C. Fu, *Approximating the distributions of runs and patterns*, Journal of Statistical Distributions and Applications 1(5), 2014. https://doi.org/10.1186/2195-5832-1-5
