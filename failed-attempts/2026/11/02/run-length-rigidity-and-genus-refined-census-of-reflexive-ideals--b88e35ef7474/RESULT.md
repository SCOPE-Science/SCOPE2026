# Run-length rigidity and genus-refined census of reflexive ideals in depth-two numerical semigroups

## Finding
For integers \(m\geq2\) and \(1\leq h<m\), consider the numerical semigroup
\[
S_{m,h}=\{0\}\cup[m,2m-h-1]\cup[2m,\infty)\subseteq\mathbb N_0.
\]
For a normalized relative ideal \(I\) of \(S_{m,h}\), meaning \(I+S_{m,h}\subseteq I\) and \(\min I=0\), put \(I^v=S_{m,h}-(S_{m,h}-I)\), where \(A-B=\{z\in\mathbb Z:z+B\subseteq A\}\). A normalized ideal is reflexive when \(I^v=I\).

Set \(H=[2m-h,2m-1]\). The complete list of normalized reflexive ideals consists of \(S_{m,h}\) and the sets
\[
I_T=S_{m,h}\cup H\cup T,\qquad T\subseteq[1,m-1],
\]
for which every maximal consecutive interval in \([1,m-1]\setminus T\) has length **at least** \(h\). The complement can be empty. No other normalized relative ideals are reflexive.

More precisely, if \(n=m-1\) and \(b_h(n,r)\) denotes the number of these ideals other than \(S_{m,h}\) having genus \(r\), then \(b_h(n,0)=1\), and for \(r\geq1\),
\[
b_h(n,r)=\sum_{j=1}^{\lfloor r/h\rfloor}
\binom{r-jh+j-1}{j-1}\binom{n-r+1}{j}.
\]
The sum is empty when \(r<h\). The normalized reflexive ideal \(S_{m,h}\) itself has genus \(m-1+h\). The complete bivariate enumerator of the nontrivial family is
\[
\sum_{n,r\geq0}b_h(n,r)z^n u^r
=\frac{1-uz+(uz)^h}{(1-z)(1-uz)-z(uz)^h}.
\]
In particular, the total normalized reflexive ideal count is
\[
1+[z^{m-1}]\frac{1-z+z^h}{(1-z)^2-z^{h+1}}.
\]

## Assumptions and scope
Intervals denote sets of all included integers, with the indicated closed endpoints. The integer \(h\) is strictly between zero and \(m\); hence the middle interval includes \(m\), and \(S_{m,h}\) has multiplicity \(m\), conductor \(2m\), and gap set \([1,m-1]\cup H\). Because the sum of any two positive semigroup elements is at least \(2m\), the displayed set is closed under addition. Every normalized relative ideal contains \(S_{m,h}\), is contained in \(\mathbb N_0\), and has a finite complement. Its genus is \(|\mathbb N_0\setminus I|\). The theorem classifies *normalized* relative ideals rather than all translations of these ideals.

## Proof
**Step 1: the two colons.** Every normalized relative ideal can be written \(I=S_{m,h}\cup T\cup U\), where \(T\subseteq[1,m-1]\), \(U\subseteq H\), and where the choices must satisfy ideal closure. The calculations below actually work for any such subset \(I\). If \(I=S_{m,h}\), then \(S_{m,h}-I=S_{m,h}\), hence \(I^v=I\). Suppose now \(I\ne S_{m,h}\). Since \(0\in I\), every element of \(S_{m,h}-I\) belongs to \(S_{m,h}\), but \(0\notin S_{m,h}-I\).

For \(z\in[m,2m-h-1]\), the only possible failures of \(z+I\subseteq S_{m,h}\) occur when \(z+t\in H\) for some \(t\in T\). Values in \(U\) never cause failures because \(z+U\subseteq[2m,\infty)\). Define
\[
W_z=[2m-h-z,\,2m-1-z]\subseteq[1,m-1].
\]
Then \(z\in S_{m,h}-I\) precisely when \(W_z\cap T=\varnothing\). As \(z\) runs across the middle interval, these \(W_z\)'s run across *every* length-\(h\) interval in \([1,m-1]\). Every \(z\geq2m\) also lies in \(S_{m,h}-I\).

**Step 2: the reflexive closure.** Write \(J=S_{m,h}-I\). Its elements are some middle-band values and the whole final ray \([2m,\infty)\). Thus \(S_{m,h}\subseteq S_{m,h}-J\), and \(H\subseteq S_{m,h}-J\): for \(x\in H\) and \(z\in J\) we have \(x+z\geq(2m-h)+m>2m-1\). For \(x\in[1,m-1]\), membership in \(S_{m,h}-J\) fails precisely when some middle-band \(z\in J\) satisfies \(x+z\in H\). By Step 1 this is equivalent to \(x\) lying in a length-\(h\) interval disjoint from \(T\). Every such interval lies in a maximal consecutive gap run of \([1,m-1]\setminus T\) having length at least \(h\), and every point in such a run belongs to some such interval.

No negative integer belongs to \(S_{m,h}-J\): for \(x<0\) choose \(z=2m-1-x\geq2m\), so \(z\in J\) but \(x+z=2m-1\notin S_{m,h}\). Therefore
\[
I^v=S_{m,h}\cup H\cup\bigl(T\cup\{x\in[1,m-1]\setminus T:\text{the gap run containing }x\text{ has length }<h\}\bigr).
\]
This proves the claimed characterization. Conversely, every \(I_T\) of the displayed form is a relative ideal: sums from its positive elements with positive elements of \(S_{m,h}\) are either in \(H\) or at least \(2m\). The closure formula then proves reflexivity. The two families are disjoint since \(H\ne\varnothing\).

**Step 3: genus enumeration.** Encode \([1,m-1]\setminus T\) by zero symbols and \(T\) by one symbols. The reflexivity criterion says that every zero run has length at least \(h\), and its genus is the number \(r\) of zero symbols. When \(r>0\), let \(j\) be the number of maximal zero runs. Distributing \(r\) zero symbols among these \(j\) runs, each of length at least \(h\), gives \(\binom{r-jh+j-1}{j-1}\) choices. Distributing the \(n-r\) one symbols across \(j+1\) spaces, with at least one between successive zero runs, gives \(\binom{n-r+1}{j}\) choices. This proves the genus formula.

For the generating function, a nonempty one-run has series \(A=z/(1-z)\), and a nonempty zero-run has series \(B=(uz)^h/(1-uz)\). Alternating runs, allowing either kind at the ends, have series \((1+A)(1+B)/(1-AB)\), which simplifies to the claimed rational expression. Setting \(u=1\) and adding the isolated reflexive ideal \(S_{m,h}\) gives the total count. All identities are formal power-series identities.

## Verification
Two independently structured finite verifiers accompany this proof. `checker_ideals.py` constructs exact semigroup membership and both colons for all gap subsets in every case \(2\leq m\leq8\), \(1\leq h<m\) with at most thirteen gaps; it checks equality with the run criterion. `checker_words.py` compares direct word enumeration, the genus binomial formula, and coefficients of the rational generating function for \(1\leq h\leq8\) and lengths \(0\leq n\leq16\). Both returned `VERIFY_OK`; exact outputs are included. These are finite cross-checks, not the basis for the infinite classification.

For example, the total normalized reflexive ideal counts are \(13\) for \((m,h)=(6,2)\), \(12\) for \((7,3)\), and \(38\) for \((8,2)\). The extreme cases are \(1+2^{m-1}\) for \(h=1\), and \(3\) for \(h=m-1\).

## Relationship to prior work
Campochiaro, D'Anna, and García-Sánchez (arXiv:2610.06426, first posted October 5, 2026) develop the general reflexive-ideal theory, including ideal duals, Apéry sets, and structural characterization results. The present classification specializes the dual operation to a natural depth-two family with a consecutive final block of gaps and adds an exact genus-refined enumeration. The general duality principle is not claimed as new. The earlier literature on divisorial and non-divisorial ideals, including Spirito's 2018 paper and general ideal-lattice enumeration, is acknowledged. No claim is made that the family represents all depth-two numerical semigroups.

## Limitations
The classification applies to the explicitly parameterized semigroups and normalized relative ideals only. It does not enumerate all numerical semigroups of fixed genus, ideals of every numerical semigroup, or isomorphism classes of semigroup rings. An older treatment of non-divisorial ideal posets was accessible only in abstract/introductory material during literature assessment, leaving some historical-priority risk; the proof here is independent and self-contained. Formal coefficients have been validated finitely but not by an external proof assistant or independent mathematical audit.

## References
1. P. Campochiaro, M. D'Anna, P. A. García-Sánchez, *Reflexive ideals of a numerical semigroup*, arXiv:2610.06426 (version 1 publicly posted October 5, 2026). https://arxiv.org/abs/2610.06426
2. D. Spirito, *Embedding the set of non-divisorial ideals of a numerical semigroup into \(\mathbb N^n\)*, Journal of Algebra and Its Applications (2018), doi:10.1142/S0219498818502055.
3. P. Campochiaro, M. D'Anna, F. Strazzanti, *Some classes of one-dimensional rings characterized by their reflexive ideals*, arXiv:2506.13591 (2025), https://arxiv.org/abs/2506.13591.
