# Two-mode quantitative mixing with a doubly exponential remainder for an erasing interval map

## Finding

Let \(f_\rho\) be the erasing interval map induced by the binary two-block rule
\[\rho(00)=\epsilon,\qquad \rho(01)=1,\qquad \rho(10)=0,\qquad \rho(11)=01,\]
and put \(T=f_\rho^2\). Write \(m\) for normalized Lebesgue measure, \(P\) for the Perron--Frobenius operator of \(T\), and \(r=\mathbf1_{[1/2,1]}-\mathbf1_{[0,1/2)}\) (values at the shared endpoint are irrelevant).

**Theorem.** There is a linear functional \(\Lambda\) on real Lipschitz observables such that every real Lipschitz \(\varphi\colon[0,1]\to\mathbb R\) and every integer \(n\ge1\) satisfy
\[
\left\|P^n\varphi-\int_0^1\varphi\,dm-2^{-n}\Lambda(\varphi)r\right\|_{L^1(m)}
\le 9\,\operatorname{Lip}(\varphi)\,2^{-2^n}.
\]
In particular, for every bounded measurable \(g\),
\[
\left|\operatorname{Cov}_m(\varphi,g\circ T^n)
-2^{-n}\Lambda(\varphi)\int_0^1 rg\,dm\right|
\le9\,\operatorname{Lip}(\varphi)\,\|g\|_\infty\,2^{-2^n}.
\]
The exponential leading rate is genuinely attained by the smooth coordinate observable \(\varphi(x)=x\). In fact,
\[
\frac{38483045}{134217728}<\Lambda(x)<\frac{39007333}{134217728},
\]
so \(\operatorname{Cov}_m(x,x\circ T^n)=2^{-n}\Lambda(x)/4+O(2^{-2^n})\) with a strictly positive leading amplitude.

The same argument gives an exact finite-dimensional assertion: if \(V_m\) consists of functions constant on the \(2^m\) dyadic cells, then \(P(V_m)\subseteq V_{\lceil m/2\rceil}\). Consequently \(P^n(V_{2^n})\subseteq V_1\), and \(P\) restricted to each invariant finite-dimensional \(V_m\) has only the eigenvalues \(1\), \(1/2\), and \(0\), with both nonzero eigenvalues simple. Its other eigenvalues are nilpotent, though their Jordan block sizes are not classified here.

## Assumptions and scope

The map \(f_\rho\) follows the standard convention for nonterminating binary expansions except at a countable exceptional set; all transfer, covariance, and invariant-measure statements are understood Lebesgue-almost everywhere. The even-iterate map \(T=f_\rho^2\) preserves \(m\), as proved in the motivating measure-theoretic article. The underlying map was first studied in its equivalent \(R\) convention, differing at zero, in the earlier work on the simplest erasing substitution. Observables in the quantitative theorem are real Lipschitz functions and the norm is \(L^1(m)\); no uniform bound for arbitrary bounded measurable observables is claimed.

For a finite word \(w\), \([w]\) denotes its binary dyadic cylinder. On finite words, \(\rho\) deletes every zero; it outputs zero for a one in an odd input position and one for a one in an even position. Let \(E_m\varphi\) be the dyadic conditional expectation onto \(V_m\). Define, for every integer \(n\ge1\),
\[
\Lambda_n(\varphi)=2^n\int_0^1\bigl(P^nE_{2^n}\varphi\bigr)r\,dm.
\]
Then \(\Lambda(\varphi)=\lim_{n\to\infty}\Lambda_n(\varphi)\), with explicit effective error bound below.

## Proof

**1. Exact transfer on cylinders.** Lemma 3.6 of Corona--Della Corte gives, for each even-length word \(w\) and each dyadic cylinder \(J\),
\[
m([w]\cap T^{-1}J)=2^{|\rho^2(w)|-|w|}\,m([\rho^2(w)]\cap J).
\]
By approximation from the generating dyadic algebra, this is the \(L^1\) identity
\[
P\mathbf1_{[w]}=2^{|\rho^2(w)|-|w|}\mathbf1_{[\rho^2(w)]}.
\]
The length of \(\rho^2(w)\) equals the number of ones of \(w\) at even positions and hence is at most \(|w|/2\) for even \(|w|\). For an odd input resolution, first embed \(V_m\subseteq V_{m+1}\). Thus \(P(V_m)\subseteq V_{\lceil m/2\rceil}\). Repeatedly halving the resolution gives \(P^n(V_{2^n})\subseteq V_1\).

**2. The surviving two modes.** The four two-bit cylinders yield
\[
P\mathbf1_{[0]}=\frac14+\frac12\mathbf1_{[0]},\qquad
P\mathbf1_{[1]}=\frac14+\frac12\mathbf1_{[1]}.
\]
Here \(\mathbf1_{[0]}\) and \(\mathbf1_{[1]}\) mean the two half-interval indicators. Therefore \(P1=1\), \(Pr=r/2\), and \(\int r\,dm=0\), \(\|r\|_1=1\). On \(V_m\), the filtration by decreasing dyadic resolutions eventually reaches \(V_1\); the induced quotient is nilpotent. Since the two nonzero eigenvalues on \(V_1\) are distinct, each is simple in every \(V_m\), while all remaining eigenvalues equal zero.

**3. Constructing the residue and controlling the error.** Fix Lipschitz \(\varphi\), with \(L=\operatorname{Lip}(\varphi)\) and \(\mu=\int\varphi\,dm\). Since the dyadic cell diameter is \(2^{-m}\),
\[\|E_m\varphi-\varphi\|_1\le L2^{-m}.\]
Write \(P^nE_{2^n}\varphi=\mu+a_n r\), and put \(c_n=2^na_n=\Lambda_n(\varphi)\). Invariance of \(m\) justifies the common constant coefficient \(\mu\). Because \(Pr=r/2\) and \(P\) is an \(L^1\) contraction,
\[
|a_{n+1}-a_n/2|
=\left\|P^{n+1}(E_{2^{n+1}}\varphi-E_{2^n}\varphi)\right\|_1
\le 2L2^{-2^n}.
\]
It follows that
\[
|c_{n+1}-c_n|\le L2^{n+2-2^n},\qquad
|\Lambda(\varphi)-c_n|\le L2^{n+3-2^n}\quad(n\ge1).
\]
For the tail estimate, successive terms have ratio \(2^{1-2^j}\le1/2\), starting at \(j\ge1\). The sequence \(c_n\) therefore converges, linearly in \(\varphi\). Finally,
\[
\left\|P^n\varphi-\mu-2^{-n}\Lambda(\varphi)r\right\|_1
\le\|P^n(\varphi-E_{2^n}\varphi)\|_1+2^{-n}|c_n-\Lambda(\varphi)|
\le9L2^{-2^n}.
\]
Duality with the Koopman operator, \(\int P^n\varphi\,g\,dm=\int\varphi\,g\circ T^n\,dm\), establishes the covariance estimate.

**4. Strictly nonzero coordinate residue.** For \(\varphi(x)=x\), compute \(c_n\) by exact rational arithmetic on the \(2^{2^n}\) dyadic atoms. The results at \(n=1,2,3,4\) are
\[
\frac14,\quad\frac9{32},\quad\frac{1181}{4096},\quad\frac{38745189}{134217728}.
\]
The rigorous tail estimate at \(n=4\) is \(|\Lambda(x)-c_4|\le2^{-9}\), yielding the displayed positive rational interval. Moreover \(\int_0^1rx\,dm=1/4\). This proves the nonvanishing leading coordinate covariance and hence sharpness of the universal \(2^{-n}\) scale on Lipschitz observables.

## Verification

The accompanying standalone \(verify.py\) reconstructs the substitution on words and the exact cylinder-transfer matrix using rational numbers. It checks 340 cylinders at resolutions two, four, six and eight, verifies the two surviving eigenmodes, evaluates the four exact coordinate residues through \(n=4\), and checks the positive interval obtained by combining the fourth residue with the analytic tail bound. These finite calculations corroborate the stated rational coefficient; the infinite-dimensional conclusion rests on the analytical contraction, dyadic-approximation and summable-tail arguments above.

Run using `python3 verify.py` with a standard Python installation. No input files or third-party packages are needed.

## Relationship to prior work

Della Corte--Isola--Piergallini (arXiv:2102.01674, publicly submitted February 2, 2021) introduced the same substitution and a map agreeing almost everywhere with \(f_\rho\), proving primarily topological and combinatorial dynamics. Corona--Della Corte (DOI:10.1017/etds.2023.16; online March 6, 2023) established Lebesgue invariance and strong mixing of the square. Their Lemma 3.6 supplies the essential exact cylinder identity, and their proof of Lemma 3.8 already exhibits the first-bit recurrence with contraction factor \(1/2\). These ingredients are credited, not claimed anew.

The present statement is the **functional-analytic quantitative refinement**: a linear asymptotic residue for all Lipschitz observables, with an explicit doubly exponentially small remainder and a certified nonzero residue for the continuous coordinate. The earlier qualitative strong-mixing theorem does not state this all-Lipschitz expansion or its error, and a leading-bit recurrence does not by itself control infinitely many dyadic scales. The new telescoping and resolution choice supply that control.

## Limitations

This theorem does not determine the exact closed form of \(\Lambda(x)\), identify the complete transfer spectrum on a natural infinite-dimensional Banach space, or assert a sharp constant in the doubly exponential remainder. The exceptional binary-expansion points are not analyzed. The result is a deduction using a published nonstandard cylinder-transfer lemma, so future literature comparison could uncover an equivalent quantified interpolation theorem. No independent review has been performed.

## References

1. A. Della Corte, S. Isola and R. Piergallini, *The simplest erasing substitution*, arXiv:2102.01674 (first submitted February 2, 2021), https://arxiv.org/abs/2102.01674 ; later *Nonlinearity* 35 (2022), 4317–4356, https://doi.org/10.1088/1361-6544/ac7690.
2. D. Corona and A. Della Corte, *Mixing properties of erasing interval maps*, *Ergodic Theory and Dynamical Systems* 44 (2024), 408–431, published online March 6, 2023, https://doi.org/10.1017/etds.2023.16 ; author-accessible full text https://pubblicazioni.unicam.it/retrieve/e891bb2f-11bb-4aa7-92a6-55751c8ff3e9/2023c-CoronaDellaCorte-ETDS.pdf.
3. A. Della Corte and M. Farotti, *Dynamics of interval maps generated by erasing substitutions*, arXiv:2102.09374, https://arxiv.org/abs/2102.09374; later *Journal of Differential Equations* 323 (2022), 86–112, https://doi.org/10.1016/j.jde.2022.03.036.
