# An exact probability law and cubic variance for binary complement-scattered-factor ambiguity

## Finding

Fix the ordered scattered pattern `01`. For each binary word \(w\) of length \(n\), let \(C(w,01)\) be the set of *distinct* words remaining after deleting one `0` and a later `1`; put \(Y(w)=|C(w,01)|\). Write \(T(w)\) for the number of contiguous `01` factors and \(A(w)\) for the number of contiguous `0101` factors (overlaps counted). For a uniformly random binary word \(W_n\), set \(Y_n=Y(W_n)\).

The complete joint distribution of \(T\) and \(A\), and hence the exact all-length distribution of \(Y_n\), is given by the following rational generating function:
\[
G(z,u,v):=\sum_{n\ge0}\sum_{w\in\{0,1\}^n}z^n u^{T(w)}v^{A(w)}
=\frac{1-u(v-1)z^2}{(1-z)^2-u z^2\bigl[1+(v-1)(1-z)^2\bigr]}.
\]
Specifically, for every \(n\ge0\) and integer \(y\),
\[
\Pr(Y_n=y)=2^{-n}\sum_{\substack{t,a\ge0\\\binom{t+1}{2}-a=y}}[z^n u^t v^a]G(z,u,v).
\]

The exact mean for \(n\ge3\) is \(\mathbb E Y_n=(n^2+n+4)/32\), and the **new exact variance**, for every \(n\ge6\), is
\[
\boxed{\operatorname{Var}(Y_n)=\frac{2n^3-5n^2+45n-60}{512}}.
\]
For lengths \(n=0,1,2,3,4,5\), the respective means are \(0,0,1/4,1/2,3/4,17/16\) and variances are \(0,0,3/16,1/4,5/16,143/256\). Moreover,
\[
\boxed{\frac{Y_n-\mathbb E Y_n}{n^{3/2}/16}\ \xrightarrow[n\to\infty]{\mathrm d}\ \mathcal N(0,1)}.
\]
The underlying identity \(Y(w)=\binom{T(w)+1}{2}-A(w)\) and the mean were already established in the prior run-pair result cited below; they are **not** asserted to be new. The contribution is the exact joint enumerator, complete induced ambiguity law, exact variance, and normal-fluctuation theorem.

## Assumptions and scope

Words are finite strings over \(\{0,1\}\); the empty word is included in generating functions. Deletion positions satisfy \(i<j\), with \(w_i=0\) and \(w_j=1\). Repeated output strings count once; if there is no eligible embedding, the set is empty. Occurrences of `01` and `0101` are contiguous, not scattered, and overlapping occurrences are retained. Source words are independent, equiprobable binary letters. All identities are literal/formal power series near \(z=0\). No limit theorem is claimed for a biased or dependent source.

## Proof

**Step 1 (previously established reduction).** The published run-pair theorem for a prescribed deletion of distinct letters \(ab\) states that the number of distinct remainders is the number of ordered \(a\)-run/\(b\)-run pairs less the number of contiguous \(abab\) factors. In a binary word, `01` runs alternate, so there are \(T(w)\) zero-to-one run transitions and exactly \(\binom{T(w)+1}{2}\) ordered zero-run/one-run pairs. It follows that
\[
Y(w)=\binom{T(w)+1}{2}-A(w).
\]
The prior work proves the general run-pair collision theorem, including the absence of other collisions; it is invoked here as a proved lemma. The two independent verification programs also check this specialization directly against the deletion-output definition.

**Step 2 (unique run decomposition).** Every binary word has a unique expression
\[
w=1^p(0^{a_1}1^{b_1})\cdots(0^{a_t}1^{b_t})0^q,
\qquad p,q\ge0,\quad a_i,b_i\ge1.
\]
Here \(t=T(w)\). An occurrence of `0101` crosses two consecutive displayed blocks exactly when \(b_i=a_{i+1}=1\). Let \(L=z/(1-z)\), \(S=z\), and \(D=z^2/(1-z)\). For an intermediate block, distinguish whether its terminal one-run is a singleton. The initial row of weights is \(d=(uLD,uLS)\), and the transfer matrix, with column/row order “last one-run length at least two, length one,” is
\[
M=\begin{pmatrix}
 uLD & uLS\\
 u(L+(v-1)z)D & u(L+(v-1)z)S
\end{pmatrix}.
\]
The term \((v-1)z\) rewards a singleton new zero-run after a singleton old one-run, contributing one factor of \(v\) to each `0101` occurrence. The unconstrained prefix \(1^p\) and suffix \(0^q\) contribute \((1-z)^{-2}\). Summing over all \(t\ge0\) gives
\[
G=\frac1{(1-z)^2}\left(1+d(I-M)^{-1}\binom11\right),
\]
which simplifies by ordinary \(2\times2\) inversion to the stated rational function. The empty and one-letter words are included; there is no uncontrolled convergence because this is an identity of formal power series. Taking the coefficient of \(z^n u^t v^a\) counts exactly the strings with the two contiguous-pattern counts, and Step 1 proves the asserted distribution.

**Step 3 (finite moments).** Define \(D_u=u\partial_u\), \(D_v=v\partial_v\), and
\[
\mathcal L=\frac{D_u^2+D_u}{2}-D_v.
\]
Then the ordinary generating functions of the *unnormalized* first and second moments are, by direct rational differentiation of the displayed \(G\),
\[
\begin{aligned}
\mathcal L G\big|_{u=v=1}
 &=\frac{z^2(1-2z+2z^3)}{(1-2z)^3},\\
\mathcal L^2 G\big|_{u=v=1}
 &=\frac{z^2\left(8z^8-12z^7-22z^6+52z^5-30z^4-6z^3+14z^2-6z+1\right)}{(1-2z)^5}.
\end{aligned}
\]
Since there are \(2^n\) length-\(n\) binary words, divide the coefficient of each displayed series by \(2^n\). Expansion of the denominator with the binomial theorem gives, for every \(n\ge6\),
\[
\mathbb E Y_n^2=\frac{(n-1)(n^3+7n^2+6n+104)}{1024}.
\]
Subtracting the square of the mean proves the variance formula. The polynomial parts of the rational generating functions account for the explicitly listed boundary values; those values are not inferred by applying the large-length polynomial outside its stated domain.

**Step 4 (normal fluctuations).** Let \(X_i=\mathbf1_{\{W_iW_{i+1}=01\}}\), so \(T=\sum_{i=1}^{n-1}X_i\). The bounded variables \(X_i\) form a stationary one-dependent sequence, with \(\mathbb E X_i=1/4\), \(\operatorname{Var}(X_i)=3/16\), and \(\operatorname{Cov}(X_i,X_{i+1})=-1/16\), while covariances at larger separations vanish. Therefore \(\operatorname{Var}(T)=(n+1)/16\) and the standard bounded one-dependent central limit theorem yields
\[
\frac{T-(n-1)/4}{\sqrt n/4}\xrightarrow{\mathrm d}\mathcal N(0,1).
\]
Also, \(A=\sum_{i=1}^{n-3}\mathbf1_{\{W_i\cdots W_{i+3}=0101\}}\), a sum of bounded three-dependent indicators, so \(A-\mathbb EA=O_{\mathsf P}(\sqrt n)\). Set \(\mu=(n-1)/4\) and \(\delta=T-\mu=O_{\mathsf P}(\sqrt n)\). Expanding Step 1 gives
\[
Y-\mathbb EY=(\mu+1/2)\delta+\frac12\bigl(\delta^2-\mathbb E\delta^2\bigr)-(A-\mathbb EA).
\]
The first term, divided by \(n^{3/2}/16\), converges to a standard normal, while the remaining terms are \(O_{\mathsf P}(n)\) and \(O_{\mathsf P}(\sqrt n)\), respectively. Slutsky's theorem proves the final limit.

## Verification

Run `python3 verify_small.py` and `python3 verify_transfer.py` from the directory containing these files (Python 3, standard library only). The first program explicitly constructs distinct deletion outputs for **all** binary words of every length through \(12\), comparing them with the prior run-pair identity and the exact moment formulas. The second program independently enumerates joint \((T,A)\) distributions by a suffix automaton and by coefficient recurrence from the rational \(G\), checking agreement and first/second moments through \(26\). Both programs completed successfully from the packaged files. These finite tests are regression checks, not substitutes for Steps 1–4, which prove every quantified statement.

## Relationship to prior work

Adamson, Fleischmann and Huch introduce complement scattered factors and give algorithms for building \(C(w,u)\) and studying its combinatorics (arXiv:2603.20790v1, 21 March 2026). Their accessible full manuscript does not state the joint distribution or variance here. The published research result *A run-pair formula for two-letter complement scattered factors* already proves the general exact run-pair identity and an all-alphabet expected count; its full `RESULT.md` was inspected. Its binary specialization **implies** the reduction in Step 1 and the mean, which are expressly credited. It does not state an exact distribution, variance, or central limit theorem for this random variable. The rational transfer approach uses familiar finite-state word enumeration, but the final closed law and fluctuation constants are specific to the prescribed ordered scattered deletion and not supplied by that general method alone.

## Limitations

The count law and variance concern the *fixed ordered* deleted pattern `01` with a uniform binary source; they do not describe unrestricted two-deletion spheres, another pattern, or a nonuniform Markov source. Exact formulas for different pattern lengths need fresh analysis. The normal limit is asymptotic rather than a finite-sample confidence bound. Publication priority has not been independently certified; an equivalent unindexed shuffle-language or motif-statistics formula might exist. This is not a claim of independent external validation.

## References

1. D. Adamson, P. Fleischmann, and A. Huch, “(Sets of) Complement Scattered Factors,” arXiv:2603.20790v1 (21 March 2026). https://arxiv.org/html/2603.20790v1
2. “A run-pair formula for two-letter complement scattered factors,” public research result (8 November 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-run-pair-formula-for-two-letter-complement-scattered-factors--3b99e07a61fe
3. W. Hoeffding and H. Robbins, “The central limit theorem for dependent random variables,” *Duke Mathematical Journal* **15** (1948), 773–780 (standard bounded-dependence central limit theorem).
