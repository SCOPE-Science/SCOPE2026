# Exact minimum secure dominating sets in Mycielskians of complete bipartite graphs

## Finding
Let \(a,b\ge4\) be integers, let \(G=K_{a,b}\) have labelled bipartition \(A\sqcup B\), and let \(\mu(G)\) denote its ordinary Mycielskian. Write \(A'\) and \(B'\) for the two corresponding shadow classes and \(w\) for the apex. A set \(S\) is *secure dominating* when it dominates and, for every vertex \(u\notin S\), an adjacent vertex \(v\in S\) can be replaced by \(u\) so that the new set still dominates.

The already-established secure domination number is \(\gamma_s(\mu(K_{a,b}))=5\). Every one of its minimum secure dominating sets has occupancy vector
\[
(p,q,r,s,z)=(|S\cap A|,|S\cap A'|,|S\cap B|,|S\cap B'|,\mathbf 1_{\{w\in S\}})
\]
belonging to the following *complete* list:
\[
\begin{array}{c|c}
\text{always present}&(1,1,1,1,1),\ (1,1,2,0,1),\ (2,0,1,1,1),\ (2,0,2,0,1),\\
& (2,0,2,1,0),\ (2,1,2,0,0)\\
\hline
\text{only when }a=4&(3,0,1,0,1)\\
\text{only when }b=4&(1,0,3,0,1)
\end{array}
\]
Conversely, **every** labelled choice of vertices with one of these vectors is a minimum secure dominating set. In particular, the exact number \(M(a,b)\) of labelled minimum sets is
\[
\boxed{\begin{aligned}
M(a,b)={}&a^2b^2+a^2\binom b2+b^2\binom a2\\
&+(a+b+1)\binom a2\binom b2\\
&+\mathbf1_{\{a=4\}}\binom a3 b
 +\mathbf1_{\{b=4\}}a\binom b3.
\end{aligned}}
\]
For example, \(M(4,4)=804\), \(M(4,5)=1330\), and \(M(5,5)=2225\).

## Assumptions and scope
All graphs are finite, simple, undirected, and have labelled vertices. The ordinary Mycielski construction has original vertices \(A\sqcup B\), shadows \(A'\sqcup B'\), and apex \(w\). There are precisely the following edges between vertex classes:
\[
A\!:\ B,B';\quad A'\!:\ B,\{w\};\quad
B\!:\ A,A';\quad B'\!:\ A,\{w\};\quad
w\!:\ A',B'.
\]
There are no edges within a class. The condition \(a,b\ge4\) is essential to the eight-profile classification; smaller classes are not asserted to obey it. The minimum size five is a previously known theorem, not a claim of novelty here.

## Proof
**Step 1 (class occupancy suffices).** Every vertex in one of the four non-apex classes has exactly the same neighborhood. For an occupancy vector \(x=(p,q,r,s,z)\) with \(0\le p,q\le a\), \(0\le r,s\le b\), \(z\in\{0,1\}\), define the domination predicate \(D_{a,b}(x)\) by requiring each class that has at least one vertex outside the selected set to have a positive selected count in an adjacent class. By the displayed class adjacencies, this is exactly
\[
\begin{aligned}
D_{a,b}(x)\Longleftrightarrow{}&
(p=a\ \lor\ r+s>0)\land(q=a\ \lor\ r+z>0)\\
&\land(r=b\ \lor\ p+q>0)\land(s=b\ \lor\ p+z>0)\\
&\land(z=1\ \lor\ q+s>0).
\end{aligned}
\]
For \(i\in\{A,A',B,B',w\}\), put \(m_i\) equal to its class size. If \(x_i<m_i\), an attack at any unselected vertex of class \(i\) is defensible precisely when there is an adjacent class \(j\) with \(x_j>0\) and \(D_{a,b}(x+e_i-e_j)\). This follows because selected vertices in each class are exchangeable. Thus this five-variable test is **exactly equivalent** to the original vertex-by-vertex security condition, for all \(a,b\), not a heuristic reduction.

**Step 2 (at most three selected per non-apex class).** Suppose a secure set has at most five vertices. If \(q\ge4\), at most one guard remains outside \(A'\), yet an outside vertex of \(A\) requires a guard in \(B\cup B'\) and an outside vertex of \(B'\) requires a guard in \(A\cup\{w\}\). These requirements are disjoint, a contradiction. The same argument handles \(s\ge4\). If \(p\ge4\) and \(w\notin S\), domination of \(A'\) and \(w\) requires two guards outside \(A\), which are unavailable. If instead \(w\in S\), the apex is the only guard outside \(A\); exchanging it for an outside vertex of \(A'\) leaves another outside vertex of \(A'\) without a guard in \(B\cup\{w\}\). The case \(r\ge4\) is symmetric. Consequently \(p,q,r,s\le3\). Since \(a,b\ge4\), all four non-apex classes contain unselected vertices before any exchange.

**Step 3 (no apex).** If \(z=0\), domination of the two shadow classes gives \(p,r\ge1\), while domination of the apex gives \(q+s\ge1\). To defend an attack at \(B'\), one needs \(p\ge2\), unless \(b=4,s=3\) and the attack fills \(B'\). Similarly one needs \(r\ge2\), unless \(a=4,q=3\). In the first exception, the at-most-five-vertex budget and \(r\ge1\) force \((p,q,r,s,z)=(1,0,1,3,0)\), but an attack at \(A'\) then fails. The other exception is symmetric. Hence \(p,r\ge2\). The at-most-five-vertex budget together with \(q+s\ge1\) now forces \(p=r=2\), \(q+s=1\), giving exactly the two listed apex-free profiles.

**Step 4 (apex selected).** Let \(z=1\). We first show \(p,r\ge1\). If \(p=0\), an attack at \(B'\) has only \(w\) as a possible defender, and exchanging \(w\) leaves another outside vertex of \(B'\) undefended unless \(b=4,s=3\). In this last case the budget and domination of \(B\) force \(q=1,r=0\); an attack at \(B\) then loses its sole defender and leaves another outside vertex of \(B\) undominated. Thus \(p\ge1\), and the symmetric argument gives \(r\ge1\).

Since \(p+q+r+s\le4\), consider an attack at an outside vertex of \(A\). If \(r+s=1\), replacing its only adjacent guard leaves another outside vertex of \(A\) undominated, except when the exchange fills \(A\), namely \(a=4,p=3\). Consequently \(r+s\ge2\) or \((a,p)=(4,3)\). Similarly, \(p+q\ge2\) or \((b,r)=(4,3)\). If neither exception occurs, the budget forces both sums to equal two and yields the four apex-selected profiles in the first row. The first exception forces \((3,0,1,0,1)\), the second \((1,0,3,0,1)\).

**Step 5 (sufficiency and enumeration).** Substitution into the exact exchange criterion of Step 1 verifies security for each listed vector. For additional hand-checkability, in the four always-present apex-selected cases the adjacent defenders for attacks in \(A,A' ,B,B'\), respectively, may be taken from \((B,B,A,A)\); in the two apex-free cases one may use \((B,B,A,A,B')\) and \((B,B,A,A,A')\). For the exceptional \(a=4\) case take \((B,w,A,A)\), and for the \(b=4\) case take \((B,B,A,w)\). Every indicated post-exchange occupancy satisfies the five displayed domination clauses. (The standalone verification program also checks all candidate vectors and substitutions using the exact criterion, not just the winners.)

For occupancy vector \((p,q,r,s,z)\), the number of labelled sets is \(\binom ap\binom aq\binom br\binom bs\). Summing these factors over the six unconditional vectors gives the first four terms of the boxed expression; the two boundary vectors contribute the indicator terms. The same necessity argument started with at most five guards and forced exactly five, while the exhibited profiles attain five. Therefore no smaller secure dominating set exists, and all size-five secure sets have been counted. This independently re-establishes the known scalar minimum and proves the claimed refinement.

## Verification
The accompanying standalone Python program `verify.py` reproduces the five-class domination/exchange criterion, exhausts all possible size-five occupancy vectors for all four essential regimes \(a\in\{4,5\},b\in\{4,5\}\), and checks that only the eight displayed candidate vectors survive. The reduction of Step 2 and the fact that, with five guards, class sizes greater than four behave identically to size five make these four finite regimes exhaustive for every \(a,b\ge4\). The program separately constructs labelled Mycielskians and directly tests every five-vertex subset for several small cases, using the original vertex-level definition. This is supplementary independent implementation evidence; the unrestricted proof is the preceding case analysis.

## Relationship to prior work
Bhutani, Christiana and Ulrickson, *On the Secure Domination of Mycielskian Graphs* (arXiv:2603.17897, publicly submitted 2026-03-18), Theorem 3.3, established \(\gamma_s(\mu(K_{a,b}))=5\) for \(a,b\ge4\) and exhibited one attaining configuration. The **exact list and number of all** minimum configurations are not part of that theorem and cannot be recovered from a scalar minimum without further classification. Published formulas for secure domination on complete multipartite graphs apply to a different graph family: \(\mu(K_{a,b})\) contains an induced five-cycle, hence is not complete multipartite. Earlier secure domination and co-secure domination results are distinguished by their exact guard-exchange quantifiers.

## Limitations
The statement addresses ordinary Mycielskians and the minimum-cardinality layer for \(a,b\ge4\), not the full secure-domination polynomial, generalized Mycielskians, or smaller shores. The count depends on labelled vertex choices; orbit enumeration is not claimed. Searches and a full-text inspection of the initiating preprint support provisional originality, but cannot establish absolute historical priority. Independent mathematical audit has not been performed.

## References
1. K. R. Bhutani, A. Christiana, and P. Ulrickson, *On the Secure Domination of Mycielskian Graphs*, arXiv:2603.17897 (2026), https://arxiv.org/abs/2603.17897 .
2. W. F. Klostermeyer and C. M. Mynhardt, *Secure domination and secure total domination in graphs*, Discussiones Mathematicae Graph Theory 28 (2008), 267–284, https://doi.org/10.7151/dmgt.1405 .
