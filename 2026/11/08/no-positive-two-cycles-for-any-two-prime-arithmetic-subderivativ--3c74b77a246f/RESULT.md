# No positive two-cycles for any two-prime arithmetic subderivative

## Finding
Let \(p\) and \(q\) be any two distinct primes. For every positive integer \(n\), set
\[
D_{\{p,q\}}(n)=n\left(\frac{\nu_p(n)}{p}+\frac{\nu_q(n)}{q}\right),
\]
where \(\nu_r(n)\) is the exponent of the prime \(r\) in \(n\). Then
\[
\boxed{D_{\{p,q\}}^{\,2}(n)=n\quad\Longleftrightarrow\quad D_{\{p,q\}}(n)=n.}
\]
Thus **no two-prime arithmetic subderivative has a positive primitive cycle of length two**. In particular, every positive orbit of this map that is periodic but not fixed (if such an orbit exists) must have least period at least three.

The positive solutions of this second-iterate equation are exactly
\[
\boxed{n=p^p m\quad\text{or}\quad n=q^q m,\qquad \gcd(m,pq)=1.}
\]
This last fixed-point description is included to make the statement complete; the classification of fixed points was already established for general prime sets in previous work. **The new content is the uniform exclusion of primitive two-cycles.**

## Assumptions and scope
All integers are ordinary positive integers. The primes \(p\) and \(q\) are distinct and at least two. The subderivative is nonnegative and takes integer values, including \(D_{\{p,q\}}(1)=0\). The theorem concerns positive solutions of the second-iterate equation and does not classify cycles of length three or greater.

## Proof
Abbreviate \(D=D_{\{p,q\}}\). Assume \(D^2(n)=n>0\), and put \(n'=D(n)>0\). Introduce the nonnegative integers
\[
a=\nu_p(n),\quad b=\nu_q(n),\quad a'=\nu_p(n'),\quad b'=\nu_q(n'),
\]
and the positive integers
\[
N=aq+bp,\qquad N'=a'q+b'p.
\]
By definition,
\[
\frac{n'}n=\frac{N}{pq},\qquad \frac{n}{n'}=\frac{N'}{pq}.
\]
Multiplying, we obtain
\[
NN'=p^2q^2.
\]
Unique factorization, and the fact that \(p\neq q\), imply that some \(u,v\in\{0,1,2\}\) satisfy
\[
N=p^u q^v,\qquad N'=p^{2-u}q^{2-v}.
\]
Taking the \(p\)- and \(q\)-valuations of the first ratio above yields
\[
a'-a=u-1,\qquad b'-b=v-1.
\]
Consequently,
\[
\tag{1}
\boxed{p^{2-u}q^{2-v}-p^u q^v=(u-1)q+(v-1)p.}
\]
We now eliminate the eight cases other than \((u,v)=(1,1)\); this analysis is exact for arbitrary distinct primes, not a bounded prime search.

For \((u,v)=(0,0)\), the claimed identity \(N=p^u q^v\) gives \(N=1\), impossible because \(N=aq+bp>0\) is at least \(\min(p,q)\). For \((u,v)=(2,2)\), similarly \(N'=1\) is impossible. For \((0,1)\) and \((1,0)\), the left-hand side of (1) is respectively \(q(p^2-1)>0\) and \(p(q^2-1)>0\), whereas its right-hand side is respectively \(-q<0\) and \(-p<0\). For \((2,1)\) and \((1,2)\), the left-hand side is respectively \(q(1-p^2)<0\) and \(p(1-q^2)<0\), whereas the right-hand side is respectively \(q>0\) and \(p>0\).

For \((u,v)=(0,2)\), equation (1) becomes
\[
(p-q)(p+q)=p-q.
\]
As \(p\neq q\), this would force \(p+q=1\), impossible. For \((u,v)=(2,0)\), equation (1) similarly reads
\[
(q-p)(p+q)=q-p,
\]
which is again impossible. The only remaining case is \((u,v)=(1,1)\), where \(N=N'=pq\), hence \(n'/n=N/(pq)=1\). Therefore \(n'=n\), so every positive solution of \(D^2(n)=n\) is fixed. The converse is immediate.

For completeness, \(D(n)=n\) is equivalent to \(aq+bp=pq\). Reducing this congruence modulo \(p\), and using \(p\neq q\), gives \(p\mid a\). Similarly, \(q\mid b\). Writing \(a=pk\), \(b=q\ell\), the equation reduces to \(k+\ell=1\) for nonnegative integers \(k,\ell\), so \((a,b)=(p,0)\) or \((0,q)\). Every other prime factor of \(n\) is unrestricted, yielding the two stated families with \(\gcd(m,pq)=1\). This last step rederives a previously known classification and does not constitute the new claim. \(\square\)

## Verification
The standalone `verify.py` implements the map using exact integer valuations and performs two independent finite regressions. For each of the \(45\) unordered pairs of distinct primes among the first ten primes, it checks all nine possible exponent splits \((u,v)\in\{0,1,2\}^2\), finding only \((1,1)\) compatible with equation (1) and positive \(N,N'\). It separately tests every \(1\le n\le100000\) for these pairs against the defining two-step equation, finding no primitive two-cycle; whenever a positive solution occurs, its valuations agree with the fixed-point description. Actual output is in `verification_output.txt`.

These checks are regression evidence. The unrestricted result is established by the nine-case symbolic proof; testing finitely many primes or integers alone would not prove it.

## Relationship to prior work
Merikoski, Haukkanen, and Tossavainen (2019) introduced arithmetic subderivatives for arbitrary prime sets and established their Leibniz-additive properties. The inspected paper does not classify two-cycles. Talukdar and Saikia (2026) studied iterated subderivatives and classified fixed points for arbitrary prime sets, explicitly identifying nontrivial periodic points as a further direction; their fixed-point theorem supplies the known families listed here but does not imply that the second iterate has no additional fixed points.

A previously published result proves the stronger assertion that **all** positive periodic points are fixed for the particular prime set \(\{2,3\}\). Its special-prime proof does not cover arbitrary distinct \(p,q\). Conversely, the present theorem covers all pairs but excludes only primitive period two, and therefore does not supersede that special case. Work on arithmetic partial derivatives with one prime, and on the full derivative with all primes, treats different dynamics.

## Limitations
The theorem does not settle whether any two-prime subderivative admits a positive cycle of period three or greater; it establishes a uniform obstruction at period two only. It does not assert a corresponding two-cycle exclusion for prime sets of cardinality three or more, and it does not improve the stronger known all-period result for \(\{2,3\}\). The exact fixed-point families were already known. Possible equivalent work outside inspected indexed sources remains a literature risk.

## References
1. J. K. Merikoski, P. Haukkanen, T. Tossavainen, *Arithmetic Subderivatives and Leibniz-Additive Functions*, arXiv:1901.02216v1 (first publicly posted 2019-01-08); *Annales Mathematicae et Informaticae* **50** (2019), 145–157, DOI:10.33039/ami.2019.03.003.
2. C. Talukdar, H. K. Saikia, *Arithmetic Differential Equations Defined by Generalized Subderivatives*, *International Journal of Mathematics Trends and Technology* **72** (2026), 21–27, DOI:10.14445/22315373/IJMTT-V72I1P104.
3. B. Emmons, X. Xiao, *The Arithmetic Partial Derivative*, *Journal of Integer Sequences* **25** (2022), arXiv:2201.12453.
4. *No nontrivial positive cycles for the \(\{2,3\}\)-arithmetic subderivative*, online mathematical result (2026), `https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-no-nontrivial-positive-cycles-for-the-2-3-arithmetic-subderivati--19603ae53ef5`.
