# A six-vertex sign transition for root degree and second-level terminal leaves in random recursive trees

## Finding
For a uniform random recursive tree on labels \(1,\ldots,n\), let \(R_n\) be the root's number of children and \(Q_n\) the number of childless vertices at depth exactly two. For every integer \(n\ge3\),
\[
\operatorname{Cov}(R_n,Q_n)=H_{n-2}-H_{n-2}^{(2)}-\frac{(n-2)^2}{(n-1)^2},
\]
where \(H_m^{(r)}=\sum_{j=1}^m j^{-r}\) and \(H_m=H_m^{(1)}\). This covariance is strictly negative for \(3\le n\le5\) and strictly positive for every \(n\ge6\); no integer \(n\ge3\) gives zero covariance. It grows as \(\log n+\gamma-\zeta(2)-1+o(1)\).

## Assumptions and scope
The root is vertex \(1\). Independently for each \(j=2,\ldots,n\), vertex \(j\) selects its parent uniformly from \(\{1,\ldots,j-1\}\). Depth is graph distance from vertex \(1\). A terminal leaf means no children (not merely undirected degree one). Define \(A_i=\mathbf1\{\operatorname{parent}(i)=1\}\), \(I_j=\mathbf1\{\operatorname{depth}(j)=2\}\), and \(L_j=\mathbf1\{j\text{ has no children at time }n\}\). Then \(R_n=\sum_{i=2}^n A_i\) and \(Q_n=\sum_{j=3}^n I_jL_j\).

## Proof
Independent parent choices give \(\mathbb EA_i=1/(i-1)\). Since \(I_j=\sum_{k=2}^{j-1}\mathbf1\{\operatorname{parent}(j)=k\}A_k\), we have \(\mathbb EI_j=H_{j-2}/(j-1)\). Later attachments are independent of the history at \(j\), and \(\mathbb EL_j=(j-1)/(n-1)\). Thus \(\mathbb E[I_jL_j]=H_{j-2}/(n-1)\).

Fix \(j\ge3\). If \(i<j\), then \(L_j\) is independent of \((A_i,I_j)\). Only the summand indexed by \(i\) in the expansion of \(I_j\) depends on \(A_i\), so
\[
\operatorname{Cov}(A_i,I_jL_j)=\frac1{n-1}\left(\frac1{i-1}-\frac1{(i-1)^2}\right).
\]
For \(i=j\), the events \(A_j=1\) and \(I_j=1\) are disjoint, while \(L_j\) is independent of \(A_j\), yielding
\[
\operatorname{Cov}(A_j,I_jL_j)=-\frac{H_{j-2}}{(j-1)(n-1)}.
\]
For \(i>j\), conditioning on the earlier choices, \(A_i\) and the event that \(i\) avoids attaching to \(j\) exclude two different potential parents. Using \(\mathbb P(L_j\mid A_i=1)=\frac{j-1}{n-1}\frac{i-1}{i-2}\), it follows that
\[
\operatorname{Cov}(A_i,I_jL_j)=\frac{H_{j-2}}{(n-1)(i-1)(i-2)}.
\]
Sum over \(i\), use \(\sum_{i=j+1}^n ((i-1)(i-2))^{-1}=(j-1)^{-1}-(n-1)^{-1}\), and obtain
\[
\operatorname{Cov}(R_n,I_jL_j)=\frac{H_{j-2}-H_{j-2}^{(2)}}{n-1}-\frac{H_{j-2}}{(n-1)^2}.
\]
Summing \(j=3,\ldots,n\) and applying \(\sum_{k=1}^m H_k=(m+1)H_m-m\) and \(\sum_{k=1}^m H_k^{(2)}=(m+1)H_m^{(2)}-H_m\), with \(m=n-2\), yields the claimed formula.

For \(m\ge1\), the difference between consecutive covariance values, expressed as a function of \(m\), is
\[
\left[H_{m+1}-H_{m+1}^{(2)}-\frac{(m+1)^2}{(m+2)^2}\right]-\left[H_m-H_m^{(2)}-\frac{m^2}{(m+1)^2}\right]=\frac{m^2+m-1}{(m+1)(m+2)^2}>0.
\]
Direct substitution gives the value \(-13/144\) at \(n=5\) and \(71/3600\) at \(n=6\), proving the unique strict sign switch. The harmonic-number asymptotics prove the final assertion.

## Verification
Run the standalone Python 3 script `verify.py` without external dependencies. It enumerates all \((n-1)!\) parent-choice tuples for each \(3\le n\le9\), computes the covariance using exact rational arithmetic, and independently checks the closed form. It also verifies the sign rule algebraically by exact fractions through \(n=999\). Its finite calculations are independent checks, not the proof of the unrestricted theorem.

## Relationship to prior work
Van der Hofstad, Hooghiemstra and Van Mieghem give exact covariances of **unmarked level sizes** of random recursive trees (2002); these level counts do not distinguish terminal from nonterminal vertices. Toofanpour, Javanian and Imany-Nabiyyi (2022) investigate the profile of protected versus nonprotected nodes and asymptotic joint fluctuations; a protected node is not simply a terminal leaf, and the inspected abstract does not resolve the present exact covariance. Research on root degree versus the **total** leaf count does not determine the contribution from terminal vertices specifically at depth two. The present quantity isolates a depth-and-childlessness intersection, exhibiting a sign reversal and logarithmic growth despite the bounded global root-degree/leaf-count covariance.

## Limitations
The claim concerns the standard uniform recursive-tree model and rooted terminal leaves at depth two only. It does not assert covariance formulas at arbitrary levels, negative association, or any independence interpretation at the sign transition. Historical priority is uncertain: the full text of the 1982 degree-by-stratum paper and the protected-node paper was not accessible during this comparison, and their uninspected contents remain a possible overlap risk.

## References
- L. Eslava, *Depth of vertices with high degree in random recursive trees*, arXiv:1611.07466, first posted 2016-11-22.
- R. van der Hofstad, G. Hooghiemstra, and P. Van Mieghem, *On the covariance of the level sizes in random recursive trees*, Random Structures & Algorithms (2002).
- J. Toofanpour, M. Javanian, and R. Imany-Nabiyyi, *Normal Limit Law for Protected Node Profile of Random Recursive Trees*, Theory of Probability & Its Applications 67 (2022), 452–464, doi:10.1137/S0040585X97T991040.
- M. Dondajewski and J. Szymański, *On the distribution of vertex-degrees in a strata of a random recursive tree*, Bull. Acad. Polon. Sci. Sér. Sci. Math. 30 (1982), 205–209.
